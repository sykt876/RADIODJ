# Apify Actor 候補リスト — 全世界調査（2026-09-16）

関連: [制約確定後の結論](./contrarian-opportunities-2026.md#4-2-制約が確定した場合の結論2026-09-16-追記)

---

## 0. 調査結果：前提が覆った

**「非英語圏は空白」という仮説は完全に間違いだった。** 各国のローカル開発者が既に埋めている。

| 地域 | 既存Actorの状況 |
|---|---|
| 🇯🇵 日本 | メルカリ（複数）、ヤフオク（複数）、ラクマ、PayPayフリマ、Buyee、楽天、SUUMO、食べログ、Yahoo!ニュース |
| 🇨🇳 中国 | 微博、小紅書（6モード）、B站、豆瓣、雪球、百度/今日頭條/抖音トレンド、**さらに5プラットフォーム横断のMCPサーバーまで** |
| 🇰🇷 韓国 | Coupang（検索・詳細・レビューの3種）、Naver Shopping（価格履歴つき） |
| 🇷🇺 ロシア | Ozon・Wildberries・Yandex Market・Avito を1本に統合したものが存在 |
| 🌏 東南アジア | Shopee（11市場）、Lazada（6市場）、Tokopedia |
| 🌎 中南米 | MercadoLibre（9市場） |
| 🇮🇳 インド | Flipkart（5本以上）、Meesho、IndiaMART |
| 🇵🇱 ポーランド | Allegro |
| 🌍 アフリカ | Jumia |
| 🏛 公的データ | SEC EDGAR、USAspending、Grants.gov、TED tenders、OFAC制裁、ClinicalTrials.gov、openFDA、Europe PMC、日本KKJ入札 |

ストアには**70,000 Actor**がある。地理で空白を探すのはもう筋が悪い。

### では空白はどこにあるか

調査で見えたのは3つだけ。

1. **壊れているもの** — Lazadaは2026年9月以降、キーワード検索・カテゴリ・ショップページに**アンチボットページを返す**ようになった。Shopeeは2026年半ばに全商品ページをクライアントレンダリングへ移行
2. **意図的に避けられているもの** — Zhihu（一部Actorが明示的に除外）、WeChat（公開インターフェース無し）、Douyin本体（範囲外と明記）
3. **束ねられていないもの** — 個別は揃っているが、横断・正規化されていない組み合わせ

---

## 1. 選定原理（非エンジニア向けに再設定）

> **空白は「地域」ではなく「①壊れているもの ②公式APIがあるのに手薄なもの ③束ねられていないもの」にある。**

ただし**①は非エンジニアには最も不向き**。2026年のアンチボットは6〜8層の独立した検出を同時に通す複合スコアリングで、TLSフィンガープリント、JS チャレンジ、行動監視、Turnstile CAPTCHA を組み合わせる。素のPlaywrightは数秒でブロックされる。residential proxy とフィンガープリント回転の保守地獄が待っている。さらに **Web Bot Auth（2026年5月登場、まだ普及率は低い）** という次の波も来る。

**→ 狙うのは ②と③の交差点。**

**非エンジニア適性の判定基準**

| 記号 | 条件 |
|---|---|
| ◎ | 公式API・APIキー不要・ログイン不要 → 壊れない、proxy不要、出力が読める |
| ○ | 公式APIだがキーが必要 |
| △ | HTML解析だがアンチボット無し |
| ✗ | アンチボットあり → **手を出さない** |

---

## 2. 候補リスト

### Tier S：公式API × 手薄 × 非エンジニア向き

| # | 候補 | 地域 | 既存状況 | 適性 | なぜ狙えるか |
|:--:|---|---|---|:--:|---|
| 1 | **Nostr**（リレー） | 🌐 グローバル | **検索で1本も発見できず** | ◎ | 完全オープン、APIキー不要、リレーに接続するだけ。**唯一Actorが見つからなかったプロトコル**。最有力 |
| 2 | **Fediverse横断**（Mastodon + Lemmy + Bluesky + Farcaster を1コール） | 🌐 | 個別は存在、**横断は発見できず** | ◎ | 中国系では「5プラットフォーム横断・正規化・重複排除」が既に商品化されている。同じ形が分散SNS側に無い |
| 3 | **Bluesky 特化**（歴史アーカイブ以外の切り口） | 🌐 | 存在するが**最大手で約240ユーザー** | ◎ | 登録3,000万人超、AT Protocol完全オープン。Google Maps 59.6万ユーザーと比べて無風 |
| 4 | **台湾**（PTT、Dcard、露天拍賣） | 🇹🇼 | **検索で発見できず** | ○〜△ | 中国本土は飽和だが台湾は未確認。PTT/Dcardは台湾の主要言論空間 |
| 5 | **韓国コミュニティ**（DCInside、Clien、당근마켓/Karrot） | 🇰🇷 | **EC系のみ存在、コミュニティ系は発見できず** | △ | Coupang/Naverは埋まっているがコミュニティ側が空いている可能性 |

### Tier A：地域未確認（Store Analyzerで要検証）

| # | 候補 | 地域 | 状況 |
|:--:|---|---|---|
| 6 | **Trendyol / Hepsiburada / Sahibinden** | 🇹🇷 トルコ | 検索で発見できず。人口8,500万の単一市場 |
| 7 | **Noon / Dubizzle** | 🇦🇪🇸🇦 中東 | 検索で発見できず。湾岸ECは高単価 |
| 8 | **Tiki / Sendo / Chợ Tốt** | 🇻🇳 ベトナム | 発見できず。Shopee/Lazadaの陰 |
| 9 | **Takealot / Konga** | 🇿🇦🇳🇬 アフリカ | Jumiaのみ存在 |
| 10 | **Bol.com / Otto / Leboncoin / Willhaben / Idealo** | 🇳🇱🇩🇪🇫🇷🇦🇹 欧州 | Allegro以外は未確認。欧州は国ごとに勝者が違う |
| 11 | **各国政府オープンデータAPI**（韓国・台湾・ブラジル・インド・インドネシア） | 🌏 | 米・EU・日本は埋まっている。**それ以外は未確認** |

### Tier B：束ねる（既存を組み合わせる）

| # | 候補 | 内容 |
|:--:|---|---|
| 12 | **日本の中古市場を1本で** | メルカリ＋ヤフオク＋ラクマ＋PayPayフリマ＋Buyee を横断し、相場を正規化。個別は全部あるが**横断は手薄** |
| 13 | **新興国EC横断** | Flipkart＋Meesho＋Jumia＋MercadoLibre を同一スキーマに正規化 |
| 14 | **エージェント向けMCP化** | 上記のどれかを MCP サーバーとして提供。Apifyは5,000ツールをMCPで公開しており、`Actor.charge()` を足すだけで従量課金に乗る。**月13万件の新規登録と3.6万人の開発者が既にAI向けツールを探している** |

### ❌ 非推奨（高収益だが非エンジニアには地雷）

| 候補 | 理由 |
|---|---|
| Lazada 修復 | 2026年9月からアンチボットページ。既存Actorが壊れている＝需要はあるが、突破と保守が本業になる |
| Shopee 修復 | 2026年半ばにクライアントレンダリング化。11市場ぶんの保守 |
| WeChat / Douyin本体 | 公開インターフェースが存在しない。プロが避けている領域 |
| Cloudflare配下の一般サイト | 6〜8層の複合検出。Web Bot Auth の普及で今後さらに悪化 |

---

## 3. 重要な注意

**「検索で発見できなかった」は「存在しない」ではない。** 本調査はウェブ検索に基づくもので、Apify Store の全数調査ではない。この環境からは `api.apify.com` が egress ポリシーで遮断されている（実測: `CONNECT tunnel failed, 403`）ため、一次データを取得できていない。

**確定させる方法は一つだけ、そしてそれは非エンジニアにもできる。**

Apify Console で **Store Analyzer**（`scraper_guru/apify-store-analyzer` または `extractmaster01/apify-store-scraper`）を実行する。Actorあたり**35フィールド**（使用状況トレンド、**実行成功率**を含む）が取れる。ボタンを押すだけで、プログラミングは不要。

結果のJSONを共有してもらえれば、以下の3軸で数字で絞り込む：

1. **ユーザー数が少ない**（＝競合が薄い）
2. **成長している**（＝需要がある）
3. **実行成功率が低い**（＝既存が壊れている ← ただし①のアンチボット案件は除外する）

---

## 4. 推奨する最初の1本

**候補1（Nostr）と候補2（Fediverse横断）** を軸に見ている。理由：

- **公式プロトコルなので壊れない** — アンチボットも proxy もログインも不要。非エンジニアの最大の弱点（緊急の故障対応）を構造的に回避できる
- **出力を目視で検証できる** — 投稿とプロフィールなので、正しいかどうかが読めば分かる
- **中国系で既に証明された形** — 「複数プラットフォームを1コールで正規化・重複排除」は中国側で商品化済み。同じ形が分散SNS側に存在しない
- **エージェント需要に直結** — MCP経由でAIエージェントのツールとして呼ばれる導線がある

まずStore Analyzerで **Nostr / Fediverse横断 / 台湾 / トルコ** の4点の実数を取り、最も薄いところから1本目を出す。

---

## 5. 参考リンク

**Apify ストア動向・ニッチ検証**
- [Apify Store Market Analyzer](https://apify.com/scraper_guru/apify-store-analyzer) / [Apify Store Scraper: Competitor & Niche Intelligence](https://apify.com/extractmaster01/apify-store-scraper) / [Most Popular Apify Actors in 2026](https://use-apify.com/docs/best-apify-actors/most-popular-actors)
- [Build and monetize MCP servers（Apify）](https://apify.com/mcp/developers) / [Apify MCP server（公式ドキュメント）](https://docs.apify.com/integrations/mcp)

**地域別の既存Actor（飽和の根拠）**
- 日本: [Mercari Japan Scraper](https://apify.com/datalab-jp/mercari-japan-listings-scraper) / [Yahoo Auctions Japan](https://apify.com/datalab-jp/yahoo-auctions-flea-market-scraper) / [Japanese Web Scraper（楽天・SUUMO・食べログ）](https://apify.com/project_bbb/japanese-web-scraper/api)
- 中国: [Chinese Social Media Brand Monitor](https://apify.com/zhorex/chinese-brand-monitor/api) / [China Trends Tracker](https://apify.com/nexgendata/china-trends-tracker/api) / [Weibo Scraper](https://apify.com/zen-studio/weibo-search-scraper/api)
- 韓国・ロシア: [Naver Shopping Scraper](https://apify.com/zen-studio/naver-shopping-scraper) / [Coupang Scraper](https://apify.com/parsebird/coupang-scraper/api) / [RU Marketplaces Price Monitor](https://apify.com/isolovyev/ru-marketplaces-price-monitor)
- 東南アジア・中南米: [Shopee Scraper](https://apify.com/lergassy/shopee-scraper) / [Lazada Scraper](https://apify.com/lergassy/lazada-scraper) / [MercadoLibre Scraper](https://apify.com/devcake/mercadolibre-scraper)
- インド・アフリカ: [Flipkart Scraper](https://apify.com/parseforge/flipkart-scraper) / [Meesho Scraper](https://apify.com/parseforge/meesho-india-scraper)
- 分散SNS: [Mastodon Scraper](https://apify.com/perconey/mastodon-scraper) / [Bluesky Scraper](https://apify.com/goat255/bluesky-scraper/api) / [Lemmy Scraper](https://apify.com/goat255/lemmy-scraper) / [Farcaster Scraper](https://apify.com/brick_joey_yto/farcaster-scraper/api)
- 公的データ: [ClinicalTrials.gov Scraper](https://apify.com/logiover/clinicaltrials-gov-scraper) / [Apify Public Data MCP（30種の公的データ抽出）](https://github.com/jlucasmcrell/apify-scrapers)

**アンチボットの現状（①を避ける根拠）**
- [How to Build Scrapers That Survive Anti-Bot Updates 2026](https://plainenglish.io/web-scraping/how-to-build-scrapers-that-survive-anti-bot-updates-2026) / [How to Bypass Cloudflare When Web Scraping 2026](https://scrapfly.io/blog/posts/how-to-bypass-cloudflare-anti-scraping)
