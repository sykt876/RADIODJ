# クロードコード（Claude Code）で自動化しやすく、マネタイズしやすいSNS — 全世界規模調査

> ⚠️ このレポートは「配信チャネルとしてのSNS」に限定した調査です。手段をSNSに限定せず「自動化して稼ぐ」全体を比較した上位版は [automation-monetization-playbook.md](./automation-monetization-playbook.md) を参照してください。

調査日: 2026-09-16 / 対象: グローバル主要SNS + 地域系プラットフォーム + パブリッシング系

---

## 0. 先に結論（TL;DR）

**「自動化しやすさ」と「マネタイズしやすさ」は、2026年時点でほぼ反比例している。**

- APIが無料で開かれている（= 自動化しやすい）Bluesky / Mastodon / Threads / Telegram は、**プラットフォーム直接の広告収益がほぼゼロ**。
- 直接の広告収益が大きい（= マネタイズしやすい）YouTube / Facebook / TikTok は、**「量産AIコンテンツ」への取り締まりが2026年に最も激化した**領域であり、素朴な全自動投稿は収益化剥奪リスクが高い。

したがって実務的な最適解は、単一プラットフォーム選定ではなく **3層ポートフォリオ**：

| 層 | 役割 | 推奨プラットフォーム | 理由 |
|---|---|---|---|
| **L1: 自動配信層**（完全自動可） | 到達・実験・SEO | Telegram, Bluesky, Mastodon, Threads, Pinterest, X(選択的) | API無料 or 安価、審査が軽い、自動化がToS上も許容 |
| **L2: 収益エンジン層**（半自動 + 人間レビュー） | 広告RPM収益 | YouTube(長尺+Shorts), Facebook Reels(CMP), TikTok | 直接ペイアウトの絶対額が大きいが、品質審査が厳しい |
| **L3: 所有資産層**（完全自動可 + 収益100%自分） | LTV最大化 | Ghost / beehiiv（ニュースレター）, Telegram有料チャンネル, 自社商品 | API完全開放 + プラットフォーム手数料0〜10% |

**総合1位（自動化 × マネタイズの積）: Telegram**（Bot API完全無料 + 1,000人から広告収益50%分配 + Stars決済）
**収益額の絶対値1位: YouTube**（ただし「人間の編集判断」を挟むワークフロー必須）
**自動化の純粋な楽さ1位: Bluesky / Mastodon**（直接のマネタイズは不可 → 送客専用）

---

## 1. 評価軸の定義

### 自動化しやすさ（Claude Code から叩く前提）
| 観点 | 意味 |
|---|---|
| A1. 公式投稿APIの有無 | スクレイピング不要で `POST` できるか |
| A2. 審査の重さ | App Review / 監査 / パートナー認定が必要か、承認までの現実的な難度 |
| A3. コスト | API利用料（従量 or 固定 or 無料） |
| A4. レート制限 | 1日あたり何回投稿できるか |
| A5. ToS上の自動化許容度 | ボット投稿が明示的に許されているか、黙認か、禁止か |

### マネタイズしやすさ
| 観点 | 意味 |
|---|---|
| M1. 直接ペイアウト | プラットフォームが現金を払うか（広告分配等） |
| M2. 参入閾値 | フォロワー数・視聴時間などの条件 |
| M3. 単価（RPM） | 1,000ビューあたりの実収入 |
| M4. 外部送客の自由度 | アフィリエイト/自社商品へのリンクが機能するか |
| M5. 自動生成コンテンツの許容度 | AI量産が収益化剥奪対象になるか |

---

## 2. 総合スコア表（5点満点、2026-09時点）

| プラットフォーム | 自動化 | マネタイズ | 総合 | 一言 |
|---|:--:|:--:|:--:|---|
| **Telegram** | 5 | 4 | **9** | Bot API無料・無審査、広告50%分配+Stars決済。最良のバランス |
| **YouTube** | 4 | 5 | **9** | API簡単・単価最強。ただしAIスロップ取締りが最厳格 |
| **Ghost / beehiiv**（ニュースレター） | 5 | 4 | **9** | Admin API全開放、手数料0%。SNSではないが収益効率は最高 |
| **Facebook (Page/Reels)** | 4 | 4 | **8** | Graph APIで自動投稿可、CMPで55%分配。ただし招待制 |
| **Pinterest** | 4 | 3 | **7** | API無料・外部リンク歓迎。直接収益は無いがアフィリエイト最適 |
| **Threads** | 4 | 1 | **5** | 無料API・250投稿/日。収益ゼロ、完全に送客用 |
| **Bluesky** | 5 | 1 | **6** | AT Protocol完全無料、ボット公認。収益機能なし |
| **TikTok** | 2 | 4 | **6** | 監査通過まで投稿が「自分だけに公開」に制限される |
| **X (Twitter)** | 3 | 2 | **5** | 従量課金化。リンク付き投稿$0.20/件が自動化の致命傷 |
| **Instagram** | 3 | 2 | **5** | API無料だが審査あり。直接ペイアウトが最弱（招待制ボーナスのみ） |
| **Reddit** | 2 | 2 | **4** | 事前承認必須化。非商用のみ無料。商用は高額 |
| **Mastodon / Fediverse** | 5 | 1 | **6** | 完全オープン。収益機能ゼロ |
| **Discord** | 4 | 3 | **7** | Bot API無料、App Subscriptionsで課金可。コミュニティ前提 |
| **LinkedIn** | 2 | 3 | **5** | 自分のフィードへの投稿のみ可。自動化取締り強化 |
| **Snapchat** | 1 | 3 | **4** | 公開投稿APIが実質なし。自動化困難 |
| **Farcaster** | 4 | 2 | **6** | プロトコル開放・Neynar APIが充実。母数が小さい |
| **中国系（抖音/小紅書/微信）** | 1 | 5 | **6** | 海外個人開発者には公開APIが事実上存在しない |

---

## 3. プラットフォーム別カルテ

### 3-1. Telegram — 【総合最良】
**自動化**
- Bot API は完全無料・審査なし・BotFatherでトークン即発行。Claude Code から `curl` 一発で投稿可能。
- チャンネル自動投稿、スケジューリング、Mini Apps、決済まで一気通貫。

**マネタイズ**
- **公開チャンネル 1,000 サブスクライバー以上で、チャンネル内広告収益の 50% を分配**（出典により50〜70%と幅あり）。収益はインプレッション・地域・広告主入札で決まる。
- 出金は暗号通貨（TON）経由、**最低出金 $100**、手数料なし。Telegram Ads・コレクティブルユーザーネーム・Premiumギフトへの再投資も可能。
- Bot/Mini Apps 内でデジタル商品を売る場合は **Telegram Stars の使用が必須**。

**Claude Code 実装**: 最も摩擦が少ない。`sendMessage` / `sendPhoto` / `sendVideo` + cron だけで完結。

---

### 3-2. YouTube — 【収益額の絶対王者、ただし最大の地雷原】
**自動化**
- Data API v3、デフォルト **10,000ユニット/日**、太平洋時間0時リセット。
- 2025-12-04 の変更で `videos.insert` は約1,600ユニット→約100ユニットに低下、さらに **2026-06-01 以降はアップロード専用バケットに分離され、1コール1ユニット・デフォルト100コール/日**（＝実質1日100本まで、読み取り予算と競合しない）と報じられている。※この項は二次情報、要公式確認。
- OAuth は自チャンネルなら容易。審査負荷は低い。

**マネタイズ**
- YPP要件: 1,000登録者 + （4,000有効公開視聴時間/12ヶ月 **or** Shorts 1,000万有効視聴/90日）。
- **2026-08-10 発表 / 2027-02-01 施行の YPP 全面改訂で、要件が 8,000視聴時間 or Shorts 2,000万視聴へと倍増**予定。2018年以来の大改訂。
- レベニューシェア: **長尺 55% / Shorts 45%**。
- RPM: 長尺 $0.50〜$20（ニッチ・国次第。米国 $3〜11、豪州はCPM $36〜40で世界最高水準、インド $0.80〜3）。**Shorts は $0.01〜$0.12** と桁が違う。

**最大リスク: inauthentic content policy（2026-07-20 に明文化）**
- 対象3類型: ①汎用・反復・テンプレ的コンテンツ、②不快/不安を煽るコンテンツ、③健康・金融などセンシティブ領域をAIペルソナに語らせるもの。
- 検出は**動画単位ではなくチャンネル単位**。
- **2026-01: 累計47億再生・3,500万登録の16チャンネルを一括削除**、年間約$1,000万の広告収益が消滅。警告段階を飛ばしての即時BAN。
- 共通する「指紋」: 合成ナレーション、テンプレサムネ、ストック映像ループ、人間の編集工程では不可能な投稿ペース。
- **AIを補助に使った本物のオリジナル制作は対象外**と明言されている。→ **全自動ではなく「自動生成 + 人間の編集判断」を必ず挟む設計**にすること。

---

### 3-3. Facebook（Page / Reels）— 【意外な穴場】
**自動化**: Meta Graph API、**課金なし**。Page への自動投稿は Instagram より制約が緩い。
**マネタイズ**:
- **Content Monetization Program (CMP)** が Reels Play / In-Stream Ads / Performance Bonus を統合。
- 要件: 10,000フォロワー + 直近60日で600,000分視聴 + 動画5本以上 + 18歳以上 + 対象国。
- **招待制** — 条件充足は「候補になる」だけで、Metaからの招待が必要。
- レベニューシェア約 **55%（Meta 45%）**。
- Reels RPM: 一般エンタメで $0.02〜$0.20（100万再生で$20〜$200）。**金融・ビジネス・テクノロジー × 米英オーディエンスなら $8〜$20+** と50〜100倍の差。→ **ニッチ選定がすべて**。

---

### 3-4. TikTok — 【監査の壁】
**自動化**
- Content Posting API の Direct Post には `video.publish` スコープ + 各クリエイターのOAuth認可が必要。
- **監査（audit）を通過するまで、APIで投稿したコンテンツはすべて「非公開（自分のみ）」に制限される。**
- 監査は手動レビューキュー、**有料の優先審査レーンは存在しない**。商用コンテンツ開示トグルの実装も必須。

**マネタイズ**
- Creator Rewards Program: 10,000フォロワー + 直近30日10万再生 + 18歳以上 + 対象国 + **60秒以上のオリジナル動画**。
- RPM **$0.40〜$1.20**（ニッチ・視聴者国次第）。月次払い（毎月1〜5日）、最低 $10〜$20。
- 対象国は限定的（米・英・独・日・韓・仏・墨・伯など）。

**判断**: 監査コストを払える中〜大規模プロジェクト向け。個人の高速立ち上げには不向き。

---

### 3-5. X (Twitter) — 【従量課金化で自動化の経済性が崩れた】
**自動化**
- **2026-02-06: 新規開発者向け無料ティア廃止、従量課金（pay-per-use）がデフォルトに。**
- 価格: **投稿作成 $0.015/件、リンクを含む投稿は $0.20/件**、読み取り $0.005/件。月額最低額なし。
- **2026-04-20: follow / like / quote post の書き込みエンドポイントが全セルフサーブ層から削除され、Enterprise専用に。**
- レガシー Basic($200/月) は 2026-06-01 以降強制移行、Pro($5,000/月) も 2026-08-14 に廃止発表、2026-09-01 以降順次移行。新規は従量課金かEnterpriseのみ。
- 従量課金は約13,000リンクなし投稿/月まではBasicより安いが、その規模ではレート制限が先にボトルネックになる。

> ⚠️ **アフィリエイト自動化にとって致命的**: リンク付き投稿が1件$0.20 = 1日10投稿で月$60。収益が出る前にAPI代が先行する。

**マネタイズ**
- Revenue Sharing は **2026-09-07 で終了**、**2026-08-08 発表の Original Content Rewards Program** に置換。
- 新要件: X Premium 加入 + **500 verified followers** + 直近90日で **Home Timeline 上の適格インプレッション 50万**（Premium系サブスクライバーによる、投稿の50%以上が表示された一意のインプレッション。**リプライは除外**）+ オリジナリティ基準の充足。
- 既存メンバーは 2026-09-08 から申請可能、審査は3営業日、初回支払いは 2026-09-25 見込み。隔週払い。
- 旧Revenue Sharing時代に分配プールが50〜80%削減されたと報じられており、収益期待値は低下傾向。

---

### 3-6. Instagram / Threads — 【送客役に徹すべき】
**Instagram**
- Graph API: **Metaからの従量課金はなし**。ただし **1日100投稿の上限**、Business/Creator アカウント必須、App Review 必要、Business Use Case のレート制限式（4800 × インプレッション）が小規模アカウントを静かに縛る（実質 約200コール/時）。
- マネタイズは**単一のファンドが存在しない**：Gifts/Stars（1スター $0.01、Reelsは500フォロワーから）、Subscriptions（10,000フォロワー）、Live Badges、**ボーナス（招待制・算定式非公開・予告なく終了しうる）**、ブランドコンテンツ。
- ネイティブ収益は $0.01〜$0.05 / 1,000再生程度。→ **直接収益を当てにしない。**

**Threads**
- API は無料。**250投稿/24h（リプライは除外）、リプライ1,000件、削除100件**。Instagram Graph API より摩擦が小さい。
- 2025-09-23 に Instagram 未連携プロフィールにも開放、2026-01-30 に `followers_count` / `follower_demographics` も拡張。
- **直接マネタイズ手段は実質なし** → 完全に送客・実験用。

---

### 3-7. Pinterest — 【アフィリエイト自動化の最適解】
- アクセス階層: **Trial（1,000リクエスト/日/アプリ、生成物は自分にしか見えないサンドボックス）** → **Standard（100リクエスト/秒/ユーザー、完全公開）**。**両方とも無料**。
- Standard 昇格には **OAuthフローを実演した動画の提出**によるレビューが必要（ads_write は300/日と厳しめ）。
- **直接ペイアウトは無いが、外部リンクを歓迎する数少ないプラットフォーム**（Instagramのようにキャプション内リンクが死んでいない）。ピンのタイトル・説明文が検索インデックス対象 = SEOがそのまま効く。
- 毎日少量を継続投稿するアカウントを優遇するアルゴリズム = **自動化と相性が完全に一致**。

---

### 3-8. Bluesky / Mastodon / Farcaster — 【無料・無制限に近い配信層】
**Bluesky**
- AT Protocol は**無料**、**最大約1,666投稿/時**という実質無制限レート。公式ドキュメントにボットのスターターテンプレートあり。
- ルール: スパム禁止（同一内容の大量投稿、無差別リプライ、全アカウントフォローは明確にNG）。**ボットアカウントはプロフィールにセルフラベルを付けること**。
- ネイティブ収益機能なし。

**Mastodon/Fediverse**: 完全オープンAPI、自前サーバーも可。収益機能ゼロ → Patreon/自社商品と組み合わせる前提。

**Farcaster**: 2026年に **Neynar が Merkle から Farcaster（プロトコル、Warpcastクライアント、リポジトリ、Clanker）を買収**。Neynar の API/Mini App スタックで開発体験は良好。収益化ツールは今後の期待段階、母数は小さい。

---

### 3-9. Reddit — 【承認制になり難度上昇】
- 無料枠: OAuth ありで **100 QPM**、なしで 10 QPM（10分平均でバースト可）。**非商用のみ**（個人プロジェクト、ボット、モデレーターツール、学術研究）。
- **2025-11 の Responsible Builder Policy により自己登録が終了**。新規OAuthクライアントは手動チケット審査、応答時間の公表なし、却下もあり得る。
- 商用利用は Reddit の承認 + 有償契約（**$0.24 / 1,000コール**、エンタープライズは月$12,000〜・5,000万コール規模と報じられる）。
- マネタイズは直接収益より**送客 → アフィリエイト/自社商品**が主。ただしサブレディットごとの自己宣伝規制が厳しい。

---

### 3-10. LinkedIn — 【自動化取締り強化中】
- 公式APIでできるのは実質 **①氏名 ②メールアドレス ③認証ユーザー本人のフィードへの投稿・コメント・いいね** のみ。**他者のコンテンツへの代理操作は不可、メッセージング自動化（コールドアウトリーチ）はToSで明確に禁止**。
- 多くのAPIはパートナー認定制。Sales Navigator API (SNAP) は新規パートナー申請を停止。
- ポリシー自体は従来から変わらないが、**2026年に検知・執行のスピードと規模が強化**された（ブラウザ自動化・スクレイピングはアカウント停止リスク）。
- 直接収益は無いが B2B リード獲得単価は全SNS中最高。→ **手動 + 予約投稿の範囲に留めるのが合理的。**

---

### 3-11. Snapchat — 【自動化不可に近い】
- 公開投稿を行うサードパーティAPIが実質なし。
- Spotlight 収益化: 概ね5万フォロワー、Snap Star ステータス、18歳以上、対象国、Spotlight動画は概ね1分以上。招待基準は総15,000時間のうち **Spotlight 3,000時間** を含む。
- **2026-05 以降、直近28日で Spotlight 視聴100時間以上の維持**が最大報酬の条件に追加。最低出金 $100、アプリ内で随時申請。
- → 自動化前提のポートフォリオからは除外推奨。

---

### 3-12. 中国系（抖音 Douyin / 小紅書 Xiaohongshu / 微信 WeChat）
- **抖音（Douyin）: サードパーティ向けの公開REST APIは存在しない**（ByteDance は外部開発者にデータAPIを開放していない）。
- **小紅書（Xiaohongshu / RED）**: エンタープライズ提携・認証企業・既存サービスプロバイダ優先の統制型アクセスモデル。Instagram/TikTok のような開かれたAPIエコシステムではない。
- 海外開発者は**中国サイバーセキュリティ法 + GDPR の双方への準拠**が必要。
- → 収益ポテンシャルは巨大だが、**個人・小規模が Claude Code で自動化する対象としては現実的でない**。中国市場を狙うなら現地代理店/MCN経由が唯一の実務解。

---

### 3-13. ニュースレター系（Ghost / beehiiv / Substack）— 【SNSではないが収益効率は最高】
| | 手数料 | API | 備考 |
|---|---|---|---|
| **Ghost** | **0%** | **Admin API 全開放**、コードインジェクション、独自テーマ、Zapier 6,000+連携 | セルフホスト可。自動化と所有権の両立で最良 |
| **beehiiv** | **0%** | API あり + 広告ネットワーク | 成長ツールが充実 |
| **Substack** | **10%**（+ Stripe 約2.9%+$0.30 ≒ 実質13%） | 基本的な有料購読設定のみ、API弱い | 発見性は最強（3,500万有効購読、500万有料購読、17,000+有料ライター） |

→ **SNSで集めた注意を、手数料0%の所有メディアに変換する**のが最終的な収益最大化パス。

---

## 4. Claude Code での実装アーキテクチャ

### 4-1. 2つの接続方式
| 方式 | 内容 | 向くケース |
|---|---|---|
| **A. MCPサーバー経由** | Postiz（OSS・セルフホスト可・30+プラットフォーム）、Ayrshare（13+プラットフォーム）、Blotato。Claude Code の MCP 設定にURLを追加して認証するだけ | 多プラットフォーム一括配信、初期立ち上げ最速 |
| **B. 各API直叩き** | Telegram / Bluesky / YouTube / Meta Graph を個別クライアントで実装 | コスト最小、レート制御を自前で最適化したい場合 |
| **C. ワークフローツール** | n8n / Make / Zapier の MCP（投稿ステップは自前で組む必要あり） | 既にそれらを使っている場合のみ |

**推奨**: L1配信層は **B（直叩き）**、L2収益層は **A（MCP）+ 人間レビュー**。Telegram と Bluesky は直叩きが圧倒的に楽なので MCP を挟む意味が薄い。

### 4-2. 最小構成の設計
```
content-core/            # 1本のソースコンテンツ（要旨・素材・リンク）
  └─ transform/          # プラットフォーム別に自動整形
       ├─ telegram.ts    # 無審査・無料・即時
       ├─ bluesky.ts     # 無料・1,666投稿/時
       ├─ threads.ts     # 無料・250投稿/24h
       ├─ pinterest.ts   # 無料・Standardなら100 req/s
       ├─ youtube.ts     # 100アップロード/日、※人間レビュー必須ゲート
       └─ facebook.ts    # Page投稿・CMP対象
review-gate/             # ← YouTube/FB/TikTok 向けは必ずここを通す
scheduler/               # GitHub Actions cron（リポジトリを状態ストアに）
```

### 4-3. 「AIスロップ判定」を回避する設計原則
2026年の最大リスクはAPI制限ではなく**収益化剥奪**。以下をパイプラインに組み込む：
1. **投稿ペースを人間的に保つ**（1日数十本の量産は検知の主要シグナル）
2. **テンプレサムネ・ストック映像ループ・合成ナレーションの3点セットを避ける**
3. **健康・金融などセンシティブ領域をAIペルソナに語らせない**（YouTubeの明示禁止類型）
4. **チャンネル単位で評価される**ため、1本の失敗ではなくチャンネル全体の均質性が問題になる
5. **AI利用の開示**（TikTokの商用コンテンツ開示、各社のAI表示要件）

---

## 5. 推奨実行プラン

### 0〜30日：摩擦ゼロの層で基盤を作る
- **Telegram チャンネル**開設 + Bot API 自動投稿（→1,000サブスクライバーが最初の収益マイルストーン）
- **Bluesky + Threads + Mastodon** に同時配信（コスト0、ボットのセルフラベル付与）
- **Ghost or beehiiv** を所有メディアとして立ち上げ（Admin API でSNS→ニュースレター送客を自動化）

### 30〜60日：アフィリエイト動線
- **Pinterest** Trial → Standard 昇格申請（OAuthフロー動画を用意）。外部リンク × SEOで最初の収益化。
- ニッチ選定は **金融 / ビジネス / テクノロジー × 米英オーディエンス**（RPMが一般エンタメの50〜100倍）。

### 60〜90日：広告収益エンジン
- **YouTube**（長尺優先、Shortsは送客用と割り切る）+ **Facebook Page/Reels**。
- **必ず人間レビューゲートを通す**。**2027-02-01 のYPP要件倍増前に既存要件で収益化を通しておく**のが時間的に有利。
- TikTok は Content Posting API の監査を並行申請（承認まで公開投稿不可のため早期着手）。

### 見送り推奨
- **X**: リンク付き投稿 $0.20/件 + 新報酬プログラムの高い閾値（50万適格インプレッション/90日）で、自動化前提の投資対効果が最も悪い。既存フォロワーがある場合のみ。
- **LinkedIn / Snapchat / 中国系**: 自動化の余地が構造的に無い。
- **Instagram の直接収益**: 期待しない（送客専用に割り切る）。

---

## 6. 検証上の注意（重要）

- 本調査はウェブ検索結果（2026年時点の二次情報）に基づく。**本セッションのネットワーク方針により、docs.x.com / developers.google.com / developers.facebook.com / telegram.org など公式ドキュメントへの直接アクセスがegressプロキシでブロックされたため、一次情報での裏取りは未実施**。
- 特に以下は変動が激しく、実装前に必ず公式ドキュメントで再確認すること：
  - X API の従量課金単価（$0.015 / $0.20 / $0.005）
  - YouTube `videos.insert` の 2026-06-01 以降のクォータ仕様（1ユニット/100コール/日）
  - Telegram の広告分配率（50% と 50〜70% で出典が割れている）
  - 各収益化プログラムの対象国リスト
- 料率・閾値はいずれも予告なく変更される。**2026年だけで X の課金体系、YouTube のYPP、Meta の収益プログラム統合、Reddit の登録方針がすべて変わっている。**

---

## 7. 参考リンク

**API・自動化**
- [X (Twitter) API Pricing 2026 — Blotato](https://www.blotato.com/blog/twitter-api-pricing) / [Postproxy](https://postproxy.dev/blog/x-api-pricing-2026/) / [SocialCrawl](https://www.socialcrawl.dev/blog/x-twitter-api-2026)
- [YouTube API Quota Limits 2026 — Phyllo](https://www.getphyllo.com/post/youtube-api-limits-how-to-calculate-api-usage-cost-and-fix-exceeded-api-quota) / [YouTube Upload API — Postproxy](https://postproxy.dev/blog/youtube-upload-api-guide/)
- [TikTok Direct Post — TikTok for Developers](https://developers.tiktok.com/docs/en/content-posting-api-reference-direct-post) / [Vorp Labs](https://vorplabs.com/agent-tools/tiktok-content-posting-api)
- [Threads API Pricing 2026 — Blotato](https://www.blotato.com/blog/threads-api-pricing) / [SocialCrawl](https://www.socialcrawl.dev/blog/threads-api)
- [Instagram API Pricing — Phyllo](https://www.getphyllo.com/post/instagram-api-pricing-explained-iv)
- [Bluesky API Pricing — Blotato](https://www.blotato.com/blog/bluesky-api-pricing) / [Are Bots Allowed on Bluesky](https://useagentsky.com/blog/are-bots-allowed-on-bluesky)
- [Reddit API Pricing 2026 — SocialCrawl](https://www.socialcrawl.dev/blog/reddit-data-api-2026) / [Prowlo](https://prowlo.com/blog/reddit-data-api)
- [Pinterest access tiers（公式）](https://developers.pinterest.com/docs/key-concepts/access-tiers/) / [Pinterest rate limits（公式）](https://developers.pinterest.com/docs/reference/rate-limits/)
- [LinkedIn API 2026 Reality Check — SocialCrawl](https://www.socialcrawl.dev/blog/linkedin-data-api-2026) / [LinkedIn Automation Crackdown 2026](https://linkedinsider.blog/linkedin-automation-crackdown-2026)
- [Xiaohongshu API Integration Guide — Hashmeta](https://hashmeta.com/blog/xiaohongshu-api-integration-complete-developer-guide-for-marketers/)
- [9 Best Social Media MCP Servers for Claude — Blotato](https://www.blotato.com/blog/best-social-media-mcp-servers) / [Postiz MCP](https://postiz.com/mcp)

**マネタイズ**
- [Social Media Monetization Requirements 2026 — Mavely](https://www.joinmavely.com/creator-tips/social-media-monetization-requirements/) / [How Social Platforms Pay Creators in 2026 — WeRSM](https://wersm.com/how-social-platforms-pay-creators-2026/)
- [Sharing Revenue with Channel Owners（Telegram公式）](https://telegram.org/blog/monetization-for-channels) / [Telegram Monetization 2026 — Scrile](https://www.scrile.com/blog/telegram-monetization)
- [Facebook Content Monetization Program 2026 — ShortSync](https://www.shortsync.app/resources/facebook-content-monetization-program-2026)
- [TikTok Creator Rewards 2026 — ShortSync](https://www.shortsync.app/resources/tiktok-creator-rewards-program-2026) / [Creators Agency](https://creatorsagency.co/blog/tiktok-creator-rewards-program-2026)
- [Original Content Rewards Program（X公式ヘルプ）](https://help.x.com/en/using-x/original-content-rewards) / [X replaces revenue sharing — TechCrunch](https://techcrunch.com/2026/08/08/x-replaces-misaligned-revenue-sharing-program-with-original-content-rewards/)
- [Instagram Creator Monetization 2026 — Conbersa](https://www.conbersa.ai/learn/instagram-creator-monetization-2026) / [Kompozy](https://kompozy.io/creator-growth/instagram-monetization-2026)
- [YouTube Shorts RPM 2026 — Mediacube](https://mediacube.io/en-US/blog/youtube-shorts-rpm) / [Average YouTube RPM 2026](https://ytmoneycalculator.com/blog/average-youtube-rpm/)
- [Snapchat Monetization 2026 — Creators Agency](https://creatorsagency.co/blog/snapchat-monetization-requirements-2026)
- [Substack vs Ghost 2026 — Sequenzy](https://www.sequenzy.com/versus/substack-vs-ghost)

**リスク（AI生成コンテンツ規制）**
- [YouTube clarifies policies around AI slop — TechCrunch](https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/)
- [YouTube's AI Slop Crackdown: 4.7B Views Wiped — OutlierKit](https://outlierkit.com/resources/youtube-ai-slop-crackdown-2026/)
- [YouTube Monetization Policy Changes 2026 Timeline — AIR Media-Tech](https://air.io/en/monetization/youtube-monetization-policy-changes-2026-a-complete-dated-timeline)
