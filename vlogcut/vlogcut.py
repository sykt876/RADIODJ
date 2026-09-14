#!/usr/bin/env python3
"""vlogcut - 長尺の旅行/ドライブ動画から「絵になる」区間だけを自動で抜き出して並べる。

音声は常に捨てる (-an)。音楽・字幕は後段の編集ソフトで載せる前提で、
その手前の「素材を小さくする」工程だけを自動化する。

やっていること:
  1. 各動画を低解像度・低フレームレートでサンプリング (ffmpeg -> rawvideo pipe)
  2. フレームごとに シャープさ / 露出 / 色の豊かさ / コントラスト / 動き量 を数値化
  3. clip-len 秒の窓をスライドさせて区間スコアを作る
     (手ブレ = 動き量のばらつき、シーン切り替わりまたぎ、品質のムラ を減点)
  4. 時間的に散らばるように貪欲選択して、目標尺になるまで採用
  5. 切り出し (clips/) / 繋いだラフカット (roughcut.mp4) / EDL (csv, json) /
     コンタクトシート (contactsheet.jpg) を書き出す
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import os
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass, asdict
from pathlib import Path

import numpy as np

# 出力ディレクトリに置く目印。過去の実行結果を素材として拾い直さないために使う。
MARKER = ".vlogcut-output"

VIDEO_EXTS = {".mp4", ".mov", ".m4v", ".avi", ".mkv", ".mts", ".m2ts", ".mpg", ".mpeg", ".webm", ".wmv", ".insv"}

# 解析用サンプリング解像度。小さいほど速いが、ボケ判定が鈍くなる。
ANALYZE_W = 192
ANALYZE_H = 108


# --------------------------------------------------------------------------
# ffmpeg の場所
# --------------------------------------------------------------------------

def find_ffmpeg() -> str:
    exe = os.environ.get("FFMPEG")
    if exe and Path(exe).exists():
        return exe
    exe = shutil.which("ffmpeg")
    if exe:
        return exe
    try:
        import imageio_ffmpeg  # type: ignore
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        pass
    sys.exit(
        "ffmpeg が見つかりません。\n"
        "  macOS:   brew install ffmpeg\n"
        "  Ubuntu:  sudo apt install ffmpeg\n"
        "  もしくは: pip install imageio-ffmpeg\n"
        "  環境変数 FFMPEG=/path/to/ffmpeg でも指定できます。"
    )


def find_ffprobe() -> str | None:
    exe = os.environ.get("FFPROBE")
    if exe and Path(exe).exists():
        return exe
    return shutil.which("ffprobe")


def probe(path: Path, ffprobe: str | None) -> dict:
    """解像度・fps を取れれば取る。取れなくても解析は続行できる。"""
    info: dict = {}
    if not ffprobe:
        return info
    cmd = [
        ffprobe, "-v", "error", "-select_streams", "v:0",
        "-show_entries", "stream=width,height,r_frame_rate:format=duration",
        "-of", "json", str(path),
    ]
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=60).stdout
        data = json.loads(out)
        st = (data.get("streams") or [{}])[0]
        info["width"] = st.get("width")
        info["height"] = st.get("height")
        rate = st.get("r_frame_rate") or ""
        if "/" in rate:
            num, den = rate.split("/", 1)
            if float(den) > 0:
                info["fps"] = float(num) / float(den)
        dur = (data.get("format") or {}).get("duration")
        if dur:
            info["duration"] = float(dur)
    except Exception:
        pass
    return info


# --------------------------------------------------------------------------
# フレームサンプリングと特徴量
# --------------------------------------------------------------------------

@dataclass
class FrameFeatures:
    """1 ファイル分の、サンプリングフレームごとの生の特徴量。"""
    times: np.ndarray      # 各フレームの秒数
    sharp: np.ndarray      # ラプラシアン分散 (ボケ検出)
    bright: np.ndarray     # 平均輝度 0..1
    contrast: np.ndarray   # 輝度の標準偏差 0..1
    colorful: np.ndarray   # Hasler-Susstrunk colorfulness
    clipped: np.ndarray    # 白飛び/黒潰れ画素の割合 0..1
    motion: np.ndarray     # 前フレームとの平均絶対差 0..1
    histdiff: np.ndarray   # 前フレームとのヒストグラム L1 距離 (シーン切替検出)


def sample_features(path: Path, ffmpeg: str, sample_fps: float, quiet: bool) -> FrameFeatures | None:
    """ffmpeg から生 RGB を流し込み、フレームを1枚ずつ捨てながら特徴量だけ貯める。

    フレームを全部メモリに載せないので、何時間の素材でもメモリは一定。
    """
    w, h = ANALYZE_W, ANALYZE_H
    cmd = [
        ffmpeg, "-nostdin", "-v", "error",
        "-i", str(path),
        "-map", "0:v:0",
        "-vf", f"fps={sample_fps},scale={w}:{h}:flags=fast_bilinear",
        "-pix_fmt", "rgb24", "-f", "rawvideo", "-",
    ]
    frame_bytes = w * h * 3
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    sharp, bright, contrast, colorful, clipped, motion, histdiff = ([] for _ in range(7))
    prev_gray: np.ndarray | None = None
    prev_hist: np.ndarray | None = None
    n = 0

    assert proc.stdout is not None
    while True:
        buf = proc.stdout.read(frame_bytes)
        if not buf or len(buf) < frame_bytes:
            break
        arr = np.frombuffer(buf, dtype=np.uint8).reshape(h, w, 3).astype(np.float32)
        r, g, b = arr[..., 0], arr[..., 1], arr[..., 2]
        gray = 0.299 * r + 0.587 * g + 0.114 * b

        # ボケ: ラプラシアンの分散。ピンボケ・被写体ブレで急落する。
        lap = (4.0 * gray[1:-1, 1:-1] - gray[:-2, 1:-1] - gray[2:, 1:-1]
               - gray[1:-1, :-2] - gray[1:-1, 2:])
        sharp.append(float(lap.var()))

        bright.append(float(gray.mean()) / 255.0)
        contrast.append(float(gray.std()) / 255.0)

        # colorfulness (Hasler & Susstrunk 2003)。空・緑・夕焼けなど「絵になる」色に反応する。
        rg = r - g
        yb = 0.5 * (r + g) - b
        colorful.append(
            float(math.sqrt(rg.std() ** 2 + yb.std() ** 2)
                  + 0.3 * math.sqrt(rg.mean() ** 2 + yb.mean() ** 2))
        )

        clipped.append(float(np.mean((gray > 250.0) | (gray < 5.0))))

        hist = np.concatenate([
            np.histogram(r, bins=16, range=(0, 256))[0],
            np.histogram(g, bins=16, range=(0, 256))[0],
            np.histogram(b, bins=16, range=(0, 256))[0],
        ]).astype(np.float32)
        hist /= max(hist.sum(), 1.0)

        if prev_gray is None:
            motion.append(0.0)
            histdiff.append(0.0)
        else:
            motion.append(float(np.abs(gray - prev_gray).mean()) / 255.0)
            histdiff.append(float(np.abs(hist - prev_hist).sum()))

        prev_gray, prev_hist = gray, hist
        n += 1
        if not quiet and n % 200 == 0:
            print(f"    ... {n / sample_fps:7.0f}s 解析済み", file=sys.stderr)

    proc.stdout.close()
    err = proc.stderr.read().decode("utf-8", "replace") if proc.stderr else ""
    proc.wait()

    if n < 2:
        if not quiet:
            print(f"  [skip] {path.name}: フレームを読めませんでした {err.strip()[:200]}", file=sys.stderr)
        return None

    # 先頭フレームの motion/histdiff は比較対象が無いので、2枚目の値で埋める。
    motion[0] = motion[1]
    histdiff[0] = histdiff[1]

    return FrameFeatures(
        times=np.arange(n, dtype=np.float64) / sample_fps,
        sharp=np.asarray(sharp, dtype=np.float64),
        bright=np.asarray(bright, dtype=np.float64),
        contrast=np.asarray(contrast, dtype=np.float64),
        colorful=np.asarray(colorful, dtype=np.float64),
        clipped=np.asarray(clipped, dtype=np.float64),
        motion=np.asarray(motion, dtype=np.float64),
        histdiff=np.asarray(histdiff, dtype=np.float64),
    )


# --------------------------------------------------------------------------
# スコアリング
# --------------------------------------------------------------------------

def robust_norm(x: np.ndarray, lo: float = 5.0, hi: float = 95.0) -> np.ndarray:
    """外れ値に引きずられないように 5..95 パーセンタイルで 0..1 に正規化する。"""
    if x.size == 0:
        return x
    a, b = np.percentile(x, lo), np.percentile(x, hi)
    if b - a < 1e-12:
        return np.zeros_like(x)
    return np.clip((x - a) / (b - a), 0.0, 1.0)


def frame_scores(all_feats: list[FrameFeatures], w_sharp: float, w_color: float) -> list[np.ndarray]:
    """全ファイルを串刺しで正規化してからフレームスコアを出す (ファイル間の比較を公平にする)。"""
    lens = [f.times.size for f in all_feats]
    cat = lambda attr: np.concatenate([getattr(f, attr) for f in all_feats])

    # シャープさはダイナミックレンジが広いので対数を取ってから正規化する。
    n_sharp = robust_norm(np.log1p(cat("sharp")))
    n_color = robust_norm(cat("colorful"))
    n_contrast = robust_norm(cat("contrast"))

    bright = cat("bright")
    clipped = cat("clipped")
    # 露出: 0.45 付近を最良として、そこからの距離で落とす。白飛び/黒潰れは追加減点。
    expo = np.clip(1.0 - np.abs(bright - 0.45) / 0.45, 0.0, 1.0)
    expo = np.clip(expo - 2.0 * np.clip(clipped - 0.02, 0.0, None), 0.0, 1.0)

    w_contrast, w_expo = 0.20, 0.25
    total = w_sharp + w_color + w_contrast + w_expo
    score = (w_sharp * n_sharp + w_color * n_color
             + w_contrast * n_contrast + w_expo * expo) / total

    # ボケは vlog にとって最も致命的なので、加点だけでなく乗算のゲートもかける。
    # 色や露出がどれだけ良くても、ピンボケなら上位に来られないようにする。
    score *= 0.55 + 0.45 * n_sharp

    out, i = [], 0
    for ln in lens:
        out.append(score[i:i + ln])
        i += ln
    return out


@dataclass
class Candidate:
    file_index: int
    path: str
    start: float
    end: float
    base: float          # 窓内フレームスコアの平均
    unevenness: float    # 窓内スコアのばらつき (生値)
    jitter: float        # 動き量のばらつき = 手ブレ (生値)
    motion: float        # 平均の動き量 (生値)
    has_cut: bool        # 窓の途中でシーンが切り替わるか
    score: float = 0.0   # 正規化後の最終スコア


def build_candidates(
    feats: FrameFeatures, fscore: np.ndarray, file_index: int, path: Path,
    sample_fps: float, clip_len: float, step: float,
    trim_edges: float, cut_threshold: float,
) -> list[Candidate]:
    n_win = max(2, int(round(clip_len * sample_fps)))
    n_step = max(1, int(round(step * sample_fps)))
    total = fscore.size
    duration = total / sample_fps
    if duration < clip_len + 2 * trim_edges:
        return []

    cuts = feats.histdiff > cut_threshold
    lo_i = int(round(trim_edges * sample_fps))
    hi_i = total - n_win - int(round(trim_edges * sample_fps))

    out: list[Candidate] = []
    for i in range(lo_i, max(lo_i, hi_i) + 1, n_step):
        seg = fscore[i:i + n_win]
        if seg.size < n_win:
            break
        mot = feats.motion[i:i + n_win]
        out.append(Candidate(
            file_index=file_index,
            path=str(path),
            start=i / sample_fps,
            end=i / sample_fps + clip_len,
            base=float(seg.mean()),
            unevenness=float(seg.std()),
            jitter=float(mot.std()),
            motion=float(mot.mean()),
            has_cut=bool(cuts[i + 1:i + n_win].any()),
        ))
    return out


def score_candidates(cands: list[Candidate], allow_cuts: bool) -> None:
    """窓レベルの減点項目も全体で正規化してから最終スコアにする。"""
    if not cands:
        return
    uneven = robust_norm(np.array([c.unevenness for c in cands]))
    jitter = robust_norm(np.array([c.jitter for c in cands]))
    motion = robust_norm(np.array([c.motion for c in cands]))

    for k, c in enumerate(cands):
        s = c.base
        s -= 0.30 * uneven[k]                          # 途中で質が変わる区間は避ける
        s -= 0.35 * jitter[k]                          # 手ブレ (動き量が暴れる) を嫌う
        s -= 0.25 * max(0.0, float(motion[k]) - 0.70)  # 極端に速いパン・振り回しを嫌う
        s -= 0.10 * max(0.0, 0.05 - float(motion[k]))  # 完全な静止画は少しだけ嫌う
        if c.has_cut and not allow_cuts:
            s -= 1.0                                   # 実質的に除外
        c.score = s


def select(
    cands: list[Candidate], target_total: float, clip_len: float,
    min_gap: float, per_file_max: int, min_score_ratio: float,
) -> tuple[list[Candidate], float]:
    """スコア順に貪欲採用。同一ファイル内で min_gap 秒以上離し、1ファイルの偏りも抑える。

    目標尺に届かなくても品質フロアを下回る区間は採らない。
    「尺を埋めるために微妙なカットを混ぜる」のは素材選別としては逆効果なので、
    足りないときは足りないと報告する。戻り値は (採用リスト, 使ったフロア値)。
    """
    best = max(c.score for c in cands)
    floor = best * min_score_ratio if best > 0 else float("-inf")

    chosen: list[Candidate] = []
    taken: dict[int, list[tuple[float, float]]] = {}
    counts: dict[int, int] = {}

    for c in sorted(cands, key=lambda x: x.score, reverse=True):
        if len(chosen) * clip_len >= target_total:
            break
        if c.score < floor:
            break
        if per_file_max and counts.get(c.file_index, 0) >= per_file_max:
            continue
        conflict = any(
            c.start < e + min_gap and s - min_gap < c.end
            for s, e in taken.get(c.file_index, [])
        )
        if conflict:
            continue
        chosen.append(c)
        taken.setdefault(c.file_index, []).append((c.start, c.end))
        counts[c.file_index] = counts.get(c.file_index, 0) + 1

    chosen.sort(key=lambda c: (c.file_index, c.start))
    return chosen, floor


# --------------------------------------------------------------------------
# 書き出し
# --------------------------------------------------------------------------

def run(cmd: list[str], quiet: bool) -> bool:
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0 and not quiet:
        print(f"  [ffmpeg] {res.stderr.strip()[-400:]}", file=sys.stderr)
    return res.returncode == 0


def vf_fit(height: int, fps: int) -> str:
    width = height * 16 // 9
    if width % 2:
        width += 1
    return (f"scale={width}:{height}:force_original_aspect_ratio=decrease,"
            f"pad={width}:{height}:(ow-iw)/2:(oh-ih)/2:color=black,"
            f"setsar=1,fps={fps},format=yuv420p")


def render_clips(chosen: list[Candidate], outdir: Path, ffmpeg: str, args) -> list[Path]:
    clipdir = outdir / "clips"
    clipdir.mkdir(parents=True, exist_ok=True)
    paths: list[Path] = []

    for k, c in enumerate(chosen, 1):
        dst = clipdir / f"{k:03d}_{Path(c.path).stem[:40]}_{int(c.start)}s.mp4"
        if args.mode == "copy":
            cmd = [ffmpeg, "-nostdin", "-v", "error", "-y",
                   "-ss", f"{c.start:.3f}", "-i", c.path, "-t", f"{c.end - c.start:.3f}",
                   "-map", "0:v:0", "-an", "-c", "copy", str(dst)]
        else:
            cmd = [ffmpeg, "-nostdin", "-v", "error", "-y",
                   "-ss", f"{c.start:.3f}", "-i", c.path, "-t", f"{c.end - c.start:.3f}",
                   "-map", "0:v:0", "-an",
                   "-vf", vf_fit(args.height, args.fps),
                   "-c:v", "libx264", "-crf", str(args.crf), "-preset", args.preset,
                   "-movflags", "+faststart", str(dst)]
        if run(cmd, args.quiet):
            paths.append(dst)
            if not args.quiet:
                print(f"  [{k:3d}/{len(chosen)}] {dst.name}", file=sys.stderr)
    return paths


def render_roughcut(clips: list[Path], outdir: Path, ffmpeg: str, args) -> Path | None:
    if len(clips) < 1:
        return None
    dst = outdir / "roughcut.mp4"

    if args.xfade > 0 and len(clips) > 1 and args.mode != "copy":
        d = min(args.xfade, args.clip_len / 3.0)
        cmd = [ffmpeg, "-nostdin", "-v", "error", "-y"]
        for c in clips:
            cmd += ["-i", str(c)]
        parts, prev, total = [], "0:v", args.clip_len
        for i in range(1, len(clips)):
            label = f"v{i}"
            parts.append(f"[{prev}][{i}:v]xfade=transition={args.transition}:"
                         f"duration={d:.3f}:offset={total - d:.3f}[{label}]")
            total += args.clip_len - d
            prev = label
        # xfade は入力の pix_fmt を引き継いで yuv444p を吐くことがあり、
        # そのままだと QuickTime やブラウザで再生できない。必ず yuv420p に落とす。
        parts.append(f"[{prev}]format=yuv420p[vout]")
        cmd += ["-filter_complex", ";".join(parts), "-map", "[vout]", "-an",
                "-c:v", "libx264", "-crf", str(args.crf), "-preset", args.preset,
                "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(dst)]
        if run(cmd, args.quiet):
            return dst
        print("  クロスフェード結合に失敗したのでカット繋ぎにフォールバックします。", file=sys.stderr)

    listfile = outdir / "concat.txt"
    listfile.write_text("".join(f"file '{c.resolve()}'\n" for c in clips), encoding="utf-8")
    cmd = [ffmpeg, "-nostdin", "-v", "error", "-y", "-f", "concat", "-safe", "0",
           "-i", str(listfile), "-an", "-c", "copy", "-movflags", "+faststart", str(dst)]
    ok = run(cmd, args.quiet)
    listfile.unlink(missing_ok=True)
    return dst if ok else None


def render_contactsheet(chosen: list[Candidate], outdir: Path, ffmpeg: str, quiet: bool) -> Path | None:
    if not chosen:
        return None
    dst = outdir / "contactsheet.jpg"
    with tempfile.TemporaryDirectory() as tmp:
        tmpd = Path(tmp)
        n = 0
        for c in chosen:
            mid = (c.start + c.end) / 2.0
            thumb = tmpd / f"t{n + 1:04d}.jpg"
            cmd = [ffmpeg, "-nostdin", "-v", "error", "-y", "-ss", f"{mid:.3f}", "-i", c.path,
                   "-map", "0:v:0", "-frames:v", "1",
                   "-vf", "scale=320:180:force_original_aspect_ratio=decrease,"
                          "pad=320:180:(ow-iw)/2:(oh-ih)/2:color=black",
                   str(thumb)]
            if run(cmd, True):
                n += 1
        if n == 0:
            return None
        cols = min(5, max(1, int(math.ceil(math.sqrt(n)))))
        rows = int(math.ceil(n / cols))
        cmd = [ffmpeg, "-nostdin", "-v", "error", "-y", "-framerate", "1",
               "-i", str(tmpd / "t%04d.jpg"),
               "-vf", f"tile={cols}x{rows}:margin=6:padding=4:color=black",
               "-frames:v", "1", "-q:v", "3", str(dst)]
        if not run(cmd, quiet):
            return None
    return dst


def write_edl(chosen: list[Candidate], outdir: Path) -> tuple[Path, Path]:
    def tc(sec: float) -> str:
        h, rem = divmod(sec, 3600)
        m, s = divmod(rem, 60)
        return f"{int(h):02d}:{int(m):02d}:{s:06.3f}"

    csv_path = outdir / "edl.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as fh:
        wr = csv.writer(fh)
        wr.writerow(["no", "source", "in_sec", "out_sec", "in_tc", "out_tc", "score"])
        for k, c in enumerate(chosen, 1):
            wr.writerow([k, c.path, f"{c.start:.3f}", f"{c.end:.3f}",
                         tc(c.start), tc(c.end), f"{c.score:.4f}"])

    json_path = outdir / "edl.json"
    json_path.write_text(
        json.dumps([{**asdict(c), "no": k} for k, c in enumerate(chosen, 1)],
                   ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return csv_path, json_path


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def collect_inputs(inputs: list[str], outdir: Path) -> list[Path]:
    """入力を集める。出力先の中身は必ず除外する。

    `vlogcut.py . -o out` のように出力先が入力フォルダ配下にあると、
    2回目の実行で自分が書いた roughcut.mp4 や clips/ を素材として拾ってしまうため。
    """
    out_res = outdir.resolve()

    def is_own_output(q: Path) -> bool:
        """今回の出力先、または過去の vlogcut 出力 (MARKER 入り) の中なら True。"""
        try:
            qr = q.resolve()
        except OSError:
            return False
        if out_res == qr or out_res in qr.parents:
            return True
        return any((d / MARKER).exists() for d in qr.parents)

    files: list[Path] = []
    for item in inputs:
        p = Path(item).expanduser()
        if p.is_dir():
            files += [q for q in sorted(p.rglob("*"))
                      if q.suffix.lower() in VIDEO_EXTS and not is_own_output(q)]
        elif p.exists():
            if is_own_output(p):
                print(f"  [warn] 出力先の中なので除外: {p}", file=sys.stderr)
            else:
                files.append(p)
        else:
            print(f"  [warn] 見つかりません: {item}", file=sys.stderr)
    # 名前に含まれる数字で自然順に並べる (DJI_0002 < DJI_0010)
    def natkey(p: Path):
        return [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\d+)", p.name)]
    return sorted(dict.fromkeys(files), key=natkey)


def parse_args(argv: list[str] | None = None):
    ap = argparse.ArgumentParser(
        prog="vlogcut",
        description="長尺の旅行/ドライブ動画から見どころだけを自動抽出して繋ぐ (音声は破棄)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="例:\n"
               "  python3 vlogcut.py ~/Videos/trip -o out --total 180 --clip-len 4\n"
               "  python3 vlogcut.py a.mp4 b.mp4 --dry-run\n",
    )
    ap.add_argument("inputs", nargs="+", help="動画ファイル、またはフォルダ (再帰的に探す)")
    ap.add_argument("-o", "--outdir", default="vlogcut_out", help="出力先 (既定: vlogcut_out)")

    ap.add_argument("--total", type=float, default=120.0, help="仕上がりの目標尺 (秒, 既定: 120)")
    ap.add_argument("--clip-len", type=float, default=4.0, help="1カットの長さ (秒, 既定: 4)")
    ap.add_argument("--min-gap", type=float, default=20.0,
                    help="同一ファイル内でカット同士を最低これだけ離す (秒, 既定: 20)")
    ap.add_argument("--per-file-max", type=int, default=0,
                    help="1ファイルから採用する最大カット数 (0 = 無制限)")
    ap.add_argument("--min-score-ratio", type=float, default=0.75,
                    help="最高スコアに対する品質の足切り比率。目標尺に届かなくても "
                         "これを下回る区間は採用しない。0 で足切り無効 (既定: 0.75)")
    ap.add_argument("--trim-edges", type=float, default=1.5,
                    help="各ファイルの先頭と末尾を無視する秒数 (既定: 1.5)")

    ap.add_argument("--sample-fps", type=float, default=2.0,
                    help="解析時のサンプリングfps。判定の細かさが変わる。"
                         "律速はデコードなので速度はほぼ変わらない (既定: 2)")
    ap.add_argument("--step", type=float, default=1.0, help="窓をずらす刻み (秒, 既定: 1)")
    ap.add_argument("--cut-threshold", type=float, default=0.45,
                    help="シーン切り替わり判定のしきい値 (既定: 0.45)")
    ap.add_argument("--allow-cuts", action="store_true",
                    help="シーンの切り替わりをまたぐ区間も許可する")
    ap.add_argument("--prefer-sharp", type=float, default=0.30, help="シャープさの重み (既定: 0.30)")
    ap.add_argument("--prefer-color", type=float, default=0.25, help="色の豊かさの重み (既定: 0.25)")

    ap.add_argument("--height", type=int, default=1080, help="出力の高さ (既定: 1080)")
    ap.add_argument("--fps", type=int, default=30, help="出力fps (既定: 30)")
    ap.add_argument("--crf", type=int, default=18, help="x264 CRF。小さいほど高画質 (既定: 18)")
    ap.add_argument("--preset", default="medium", help="x264 preset (既定: medium)")
    ap.add_argument("--mode", choices=["encode", "copy"], default="encode",
                    help="encode=正確な位置で再エンコード / copy=無劣化・高速だがキーフレーム単位 (既定: encode)")
    ap.add_argument("--xfade", type=float, default=0.0,
                    help="ラフカットのクロスフェード秒数。0 でカット繋ぎ (既定: 0)")
    ap.add_argument("--transition", default="fade", help="xfade のトランジション名 (既定: fade)")

    ap.add_argument("--no-roughcut", action="store_true", help="繋いだ roughcut.mp4 を作らない")
    ap.add_argument("--no-contactsheet", action="store_true", help="contactsheet.jpg を作らない")
    ap.add_argument("--dry-run", action="store_true", help="解析だけして採用予定を表示する")
    ap.add_argument("--quiet", action="store_true", help="進捗を出さない")
    return ap.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    ffmpeg = find_ffmpeg()
    ffprobe = find_ffprobe()

    outdir = Path(args.outdir).expanduser()
    files = collect_inputs(args.inputs, outdir)
    if not files:
        print("対象の動画がありません。", file=sys.stderr)
        return 1
    if not args.quiet:
        print(f"対象 {len(files)} ファイルを解析します (ffmpeg: {ffmpeg})", file=sys.stderr)

    feats_list: list[FrameFeatures] = []
    kept: list[Path] = []
    for i, f in enumerate(files, 1):
        if not args.quiet:
            meta = probe(f, ffprobe)
            dur = meta.get("duration")
            extra = f" ({dur / 60:.1f}分)" if dur else ""
            print(f"  [{i}/{len(files)}] {f.name}{extra}", file=sys.stderr)
        ft = sample_features(f, ffmpeg, args.sample_fps, args.quiet)
        if ft is not None:
            feats_list.append(ft)
            kept.append(f)

    if not feats_list:
        print("解析できる動画がありませんでした。", file=sys.stderr)
        return 1

    scores = frame_scores(feats_list, args.prefer_sharp, args.prefer_color)

    cands: list[Candidate] = []
    for idx, (ft, sc, path) in enumerate(zip(feats_list, scores, kept)):
        cands += build_candidates(
            ft, sc, idx, path, args.sample_fps, args.clip_len, args.step,
            args.trim_edges, args.cut_threshold,
        )
    if not cands:
        print(f"候補区間がありません。--clip-len ({args.clip_len}s) が素材より長い可能性があります。",
              file=sys.stderr)
        return 1

    score_candidates(cands, args.allow_cuts)
    chosen, floor = select(cands, args.total, args.clip_len, args.min_gap,
                           args.per_file_max, args.min_score_ratio)
    if not chosen:
        print("採用できる区間がありませんでした。--min-gap を小さくしてみてください。", file=sys.stderr)
        return 1

    got = len(chosen) * args.clip_len
    print(f"\n{len(chosen)} カット / 合計 {got:.0f}秒 を採用 (品質フロア {floor:.3f}):", file=sys.stderr)
    for k, c in enumerate(chosen, 1):
        print(f"  {k:3d}. {Path(c.path).name}  {c.start:8.1f}s - {c.end:8.1f}s   score {c.score:.3f}",
              file=sys.stderr)
    if got < args.total - args.clip_len / 2:
        print(f"\n  ! 目標 {args.total:.0f}秒 に対して {got:.0f}秒 しか採れませんでした。"
              f"基準を満たす区間が足りません。\n"
              f"    --min-score-ratio を下げる / --min-gap を小さくする / 素材を足す "
              f"のいずれかで増やせます。", file=sys.stderr)

    if args.dry_run:
        return 0

    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / MARKER).write_text(
        "vlogcut の出力先です。このファイルがあると、次回以降ここは素材として読まれません。\n",
        encoding="utf-8",
    )

    print("\n切り出し中...", file=sys.stderr)
    clips = render_clips(chosen, outdir, ffmpeg, args)
    if not clips:
        print("切り出しに失敗しました。", file=sys.stderr)
        return 1

    csv_path, json_path = write_edl(chosen, outdir)
    results = [f"clips/           : {len(clips)} カット", f"edl.csv / edl.json: {csv_path.name}, {json_path.name}"]

    if not args.no_roughcut:
        print("繋ぎ中...", file=sys.stderr)
        rc = render_roughcut(clips, outdir, ffmpeg, args)
        if rc:
            results.append(f"roughcut.mp4     : {rc.name}")
    if not args.no_contactsheet:
        print("コンタクトシート作成中...", file=sys.stderr)
        cs = render_contactsheet(chosen, outdir, ffmpeg, args.quiet)
        if cs:
            results.append(f"contactsheet.jpg : {cs.name}")

    print(f"\n完了: {outdir.resolve()}", file=sys.stderr)
    for line in results:
        print(f"  {line}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
