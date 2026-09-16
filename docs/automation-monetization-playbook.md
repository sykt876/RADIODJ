# Claude Code で「自動化して稼ぐ」— 全世界・全手段の調査（SNSに限定しない版）

調査日: 2026-09-16 / 前提: 目的は自動化そのものではなく **収益化**。チャネルは問わない。
関連: [SNS特化版の調査](./sns-automation-monetization-research.md)（配信チャネルの深掘り）

---

## 0. 最重要の結論

**2026年に起きた構造変化は一行で要約できる。**

> 「AIでコンテンツを量産し、広告で稼ぐ」モデルは全方位で潰された。
> 「AIで**道具**と**労働**を作って売る」モデルは手数料が下がり、需要が急増した。

### 潰された側（2026年の実際の執行）
| 領域 | 何が起きたか |
|---|---|
| YouTube | 2026-01に累計**47億再生・3,500万登録の16チャンネルを一括削除**、年約$1,000万の広告収益消滅。判定は動画単位でなく**チャンネル単位** |
| Google検索 | **scaled content abuse** で手動対策（ランク低下ではなく**検索からの完全削除**）。2026年3月コアアップデートが明示的に標的化。AI記事を大量公開したサイトは**50〜80%の流入減** |
| 検索流入そのもの | AI Overviews がほぼ半数のクエリで発火。**パブリッシャーへの参照流入は前年比-38%**、AIO表示時のオーガニックCTRは**-61%**、ゼロクリック率は全世界**約60%**（モバイル77%） |
| 広告ネットワーク | **Ezoic が2026年2月に最低要件を月1万ユーザー→25万ユーザーへ25倍引き上げ**。小規模サイトの受け皿が消滅 |
| AI音楽 | Spotifyは**年1,000ストリーム未満のトラックは収益ゼロ**。DistroKidは未編集AI楽曲の大量投稿を stream farming として検知 |
| オーディオブック | **ACXは2026-04-15更新の規約で人間ナレーション必須**、無許可のTTS/AI/自動録音を明示禁止 |

### 伸びている側（同じく2026年の実データ）
| 領域 | 条件 |
|---|---|
| Apify Actors | 開発者取り分 **80%**。月$1.4Mを約3,000人に分配（平均約$470/人）、トップは**$10,000〜50,000/月** |
| Shopify アプリ | **最初の$1,000,000は開発者100%**、超過分85%（+決済2.9%） |
| Chrome拡張 | 成功者は**単一拡張で$2,000〜50,000/月**。94%が無料、**上位6%が総収益の73%**を占める |
| AI自動化代行 | 生産化サービスの相場**$1,500〜4,500/月/社**（小規模$1,000〜3,500、中堅$2,500〜8,000、上位$10,000〜25,000+） |
| リカーリングアフィリエイト | **30% lifetime**（ConvertKit, Podia, Thinkific, Pipedrive 等）が標準化 |

**したがって推奨は「コンテンツ量産」ではなく「①動かすたびに課金される道具」＋「②今すぐ現金になる代行」＋「③手数料0%の所有資産」の3本立て。**

---

## 1. 総合ランキング（自動化適性 × 収益化速度 × プラットフォームリスク）

| 順位 | 手段 | 初収益まで | 手数料/取り分 | 自動化適性 | 主リスク |
|:--:|---|---|---|:--:|---|
| **1** | **AI自動化の受託・生産化サービス** | **2〜6週** | 0%（直接契約） | ★★★★☆ | 営業が必要 / 属人化 |
| **2** | **Apify Actor（実行課金ツール）** | 1〜3ヶ月 | 開発者**80%** | ★★★★★ | プラットフォーム依存 |
| **3** | **Micro SaaS / API プロダクト** | 2〜6ヶ月 | Stripe 2.9%+30¢ / LS 5%+50¢ | ★★★★★ | 集客が最大の壁 |
| **4** | **Chrome拡張 / VS Code拡張** | 1〜4ヶ月 | 決済代行のみ | ★★★★★ | ストア審査・Manifest変更 |
| **5** | **Shopify アプリ / WordPress プラグイン** | 3〜9ヶ月 | **$1Mまで0%**／15% | ★★★★☆ | 審査が重い・中央値は月$1,000未満 |
| **6** | **ニュースレター + リカーリングアフィリエイト** | 2〜6ヶ月 | Ghost/beehiiv **0%** | ★★★★★ | 立ち上がりが遅い |
| **7** | **デジタル商品（Gumroad / Etsy）** | 2〜8週 | Gumroad 10% / Etsy 約9.5%+$0.20 | ★★★★☆ | 差別化困難・価格競争 |
| **8** | **KDP（電子書籍）** | 1〜3ヶ月 | 印税 **70%**（$2.99〜$12.99） | ★★★☆☆ | AI開示義務・品質審査 |
| **9** | SNS広告分配（YouTube/FB/TikTok） | 3〜12ヶ月 | 45〜55%分配 | ★★☆☆☆ | **AIスロップ判定でBAN** |
| **10** | 広告収益型コンテンツサイト | 6〜18ヶ月 | AdSense/Mediavine | ★★☆☆☆ | **検索流入崩壊 + 手動対策** |
| **11** | AI音楽・AIオーディオブック量産 | — | — | ★★☆☆☆ | **各社が明示的に規制済み** |

---

## 2. Tier S：Claude Code と構造的に相性が最高の3つ

### 2-1. Apify Actor —「一度公開し、動くたびに課金」
**なぜ最適か**: Claude Code が最も得意な「スクレイパー/データ変換/API化」がそのまま商品になる。集客をApify Storeが肩代わりする。

- 課金モデルは **pay-per-event（PPE）**：イベント発火をプログラム側から任意に定義して課金できる
- **開発者取り分80%**、支払いは月次（11日前後の請求サイクル）。最低出金は銀行振込$100 / PayPal $20
- 実績: **月$1.4Mを約3,000開発者に分配**（平均$470/人）、ストアは約54,000ツールに拡大、トップは$10,000〜50,000/月
- ⚠️ **レンタル課金モデルは2026-04-01に新規受付停止、2026-10-01に完全廃止** → 新規は必ずPPEで設計する
- RapidAPI も手数料20%で同等。ただしApifyの方が実行環境込みで摩擦が少ない

**作るべきもの**: 特定業界に刺さる縦型データ抽出（求人/不動産/価格監視/規制文書）、AI前処理付きのデータクリーニング、ニッチAPIのラッパー。

### 2-2. Micro SaaS / API プロダクト
**決済の選択（2026年時点の相場）**

| | 手数料 | 販売主体(MoR) | 税務 |
|---|---|---|---|
| **Stripe** | 2.9% + 30¢ | 自分 | **VAT/売上税は全て自己責任** |
| **Lemon Squeezy** | **5% + 50¢**（月額固定費なし、階層なし） | LS | 200+法域で代理徴収・納付 |
| **Paddle** | 5% + 50¢ | Paddle | 同上 |

- $10k MRR 時点で MoR のプレミアムは月$250〜350程度 → **海外課金があるならMoRを選ぶ方が実質安い**（税務コンプラ工数を時給換算すると確実に得）
- ⚠️ **Stripeは2024年7月にLemon Squeezyを買収、2026年2月に自社MoR「Stripe Managed Payments」をパブリックプレビュー投入** → LSの将来的な位置づけは要注視

**日本在住者への実務注記**: MoRを使うと消費税・海外VATの登録義務を自分で背負わずに済む。個人・マイクロ法人で海外向けに売るなら Paddle / Lemon Squeezy が現実的。

### 2-3. Chrome拡張 / VS Code拡張
- 収益モデル構成比: フリーミアム/サブスク **約35%**、広告25%、買い切り15%、アフィリエイト10%、寄付8%、エンタープライズ5%、データライセンス2%
- フリーミアムの有料転換率は **2〜5%**
- **Chrome Web Store の決済機能は廃止済み** → 外部決済（Stripe / Lemon Squeezy / Dodo Payments 等）を自前で繋ぐ必要がある
- 市場は極端な集中: **94%が無料、上位6%が総収益の73%**

---

## 3. Tier A：最速で現金になる — AI自動化の受託・生産化サービス

**Claude Code を持っている人間にとって、2026年に最も早く・最も確実に現金化できるのはこれ。**

| 規模 | 月額相場 |
|---|---|
| 小規模事業者（監視付きワークフロー2〜3本） | **$1,000〜3,500** |
| 生産化サービス（標準パッケージ） | **$1,500〜4,500** |
| 中堅企業プロジェクト | **$2,500〜8,000** |
| 上位クライアント | **$10,000〜25,000+** |
| 基本自動化（メールトリガー、チャットボット） | $99〜500 |

- ハイブリッド型（例: AI Ops 基本$4,000/月 + 新規ワークフロー従量）が主流化
- 買い手の意思決定基準は「月$5,000のエージェンシー vs 社内採用1人（福利厚生・管理コスト込み）」→ **$5,000/月でも社内採用より安い**という比較で通る
- 安いインフラ + 強いモデル + 単純な自動化 という組み合わせが、SaaSを作らずに個人が高マージンを取れる構造を作っている

**戦略**: 受託で現金を作り、その過程で得た再現パターンを Tier S（Actor / SaaS / 拡張）にプロダクト化する。**受託は最良の市場調査**でもある。

---

## 4. Tier B：手数料の低い所有資産

### 4-1. ニュースレター × リカーリングアフィリエイト
| | 手数料 | API |
|---|---|---|
| **Ghost** | **0%** | **Admin API 全開放**、セルフホスト可、Zapier 6,000+連携 |
| **beehiiv** | **0%** | API + 広告ネットワーク内蔵 |
| Substack | **10%**（+Stripe約2.9%+$0.30 ≒ 実質13%） | 弱い。発見性は最強（3,500万有効購読 / 500万有料購読 / 17,000+有料ライター） |

**30% lifetime のリカーリングアフィリエイト**（ConvertKit / Podia / Thinkific / Pipedrive / Arvow 等）と組み合わせると、1件の紹介が解約まで永続的に積み上がる。3年スパンでは lifetime 型が圧倒的に有利。

### 4-2. デジタル商品
| | 手数料（$25の商品） | 特性 |
|---|---|---|
| **Gumroad** | 一律**10%**（$2.50）、出品料なし | 集客は自前。既に読者がいるなら最適 |
| **Etsy** | 出品$0.20（4ヶ月更新）+ 取引6.5% + 決済約3%+$0.25（計約$2.78+） | **検索需要が既にある**のが最大の価値 |

- Gumroad に AI固有の開示規定は2026年5月時点で存在しない（一般的な「正確な表示義務」のみ）
- 実務パターン: **Etsyで発見 → Gumroadでリピート・バンドル販売**の二段構え

### 4-3. Amazon KDP
- 印税 **70%**（$2.99〜$12.99）。**2026年7月に70%帯の上限が$9.99→$12.99へ引き上げ**（$9.99超は70%オプションを手動選択する必要あり）
- **AI生成テキスト・画像・翻訳は申告必須**（新規出版時・既存更新時）。ただし**ブレスト、文法チェック、人間の文章の推敲、人間作画像の改善は申告不要**
- 「大幅に編集してもAI生成であることは変わらない」と明記。申告はAmazon内部情報であり商品ページには表示されない
- **印税率・ランキングには影響しない**とAmazonが明言。非申告のペナルティは出品削除・アカウント停止・既販売分の印税没収

---

## 5. Tier C：手を出すべきでない（2026年時点）

### 5-1. 広告収益型コンテンツサイト
- 参照流入 -38%、AIO表示時CTR -61%、DMG Media は一部検索で**約90%減**を報告
- **Ezoic の最低要件が月1万→25万ユーザー**（2026年2月）に引き上げられ、小規模の入口が消滅
- Mediavine: 年間広告収益$5,000 or 月5万セッション / Raptive: 月2.5万PV（2025年10月に引き下げ）だが実質は米国中心10万PV+ / AdSense: 要件なしだが RPM $1〜5
- Mediavine/Raptive の RPM $15〜50 は魅力的だが、**そこに到達する流入経路そのものが壊れている**

### 5-2. AI音楽の量産投稿
- Spotify: 年1,000ストリーム未満は収益ゼロ（AIバルクスパムの長尾を非収益化する目的で導入）
- Suno Pro($120/年) + DistroKid($23.99/年) の回収に **年間約6万ストリームが必要**（$0.003/ストリーム換算）
- DistroKid は生プロンプト出力の大量投稿を明示的にフラグ
- Spotifyの2025年9月ポリシー（音声保護・スパムフィルタ・**DDEXによるAI開示**）は2026年3月時点で継続、DistroKid含む各ディストリビューターで展開中

### 5-3. AIナレーション・オーディオブック
- **ACXは人間ナレーション必須**（2026-04-15規約）。合法な道はAmazon純正の **Virtual Voice**（KDP経由、リスナーに「Narrator: Virtual Voice」と表示、Amazon内のみ配信、印税率はACXより低い）か招待制の Voice Replica ベータのみ
- 第三者AIナレーションは **Spotify / Google Play Books / Apple Books / Kobo なら開示付きで可**。**Google Play の自動ナレーション52%はAudibleの非独占レートを上回る**

---

## 6. 意思決定フロー

```
今すぐ現金が必要か？
├─ YES → ①AI自動化の受託/生産化サービス（2〜6週で入金）
│         └→ 得た再現パターンを②へプロダクト化
└─ NO（積み上げ可能）
   ├─ 技術資産がある（スクレイピング/データ/API）
   │   → ②Apify Actor（PPE）→ ③Micro SaaS
   ├─ 特定業務の痛みを知っている
   │   → ④Chrome拡張 or ⑤Shopifyアプリ
   └─ 発信できるテーマがある
       → ⑥Ghost/beehiiv + 30% lifetime アフィリエイト
```

**やってはいけない**: 「AIで大量生成 → 大量投稿 → 広告収益」。2026年に全プラットフォームが個別に潰した唯一の共通パターンがこれ。

---

## 7. 90日プラン（推奨構成）

### Day 1–30：現金化ラインを1本通す
- **受託を1件取る**（$1,000〜3,500/月の小規模枠から）。Claude Code で2〜3本の監視付きワークフローを納品する形が最も売りやすい
- 同時に **Ghost or beehiiv** を立ち上げ（手数料0%、Admin APIで投稿自動化）。受託過程の知見をそのまま記事化 → 次の案件の営業資産になる

### Day 31–60：実行課金ツールを1本公開
- **Apify Actor を PPE で公開**（レンタルモデルは2026-10-01廃止なので必ずPPE）
- 題材は受託で実際に作ったものの汎用化が最短。Claude Code で Actor 化 → Store が集客を担う

### Day 61–90：所有プロダクトへ
- Actor の利用ログから需要が確認できたものを **Micro SaaS 化**（決済は海外向けなら Paddle / Lemon Squeezy、米国中心なら Stripe）
- または **Chrome拡張**（フリーミアム、転換率2〜5%を前提に価格設計）
- ニュースレターに **30% lifetime アフィリエイト**を組み込む

### 並行して回してよいもの
- Telegram / Bluesky / Threads への自動配信（コストほぼ0、送客専用。[SNS版レポート](./sns-automation-monetization-research.md)参照）
- Gumroad / Etsy でのデジタル商品（受託の副産物テンプレートをそのまま商品化）

---

## 8. 検証上の注意

- 本調査はウェブ検索で得た **2026年時点の二次情報**に基づく。本セッションのegressポリシーにより公式ドキュメント（shopify.dev / docs.apify.com / Amazon KDPヘルプ等）への直接アクセスがブロックされたため、**一次情報での裏取りは未実施**
- 特に実装前の再確認が必須な数値:
  - Apify の PPE 取り分（80%）とレンタル廃止日（2026-10-01）
  - Shopify の$1M閾値と15%（+2.9%決済手数料）
  - Lemon Squeezy / Paddle の料率と、Stripe Managed Payments 投入後の扱い
  - KDP の70%帯上限（$12.99）とAI申告要件
  - 各広告ネットワークの最低要件（Ezoicは2026年2月に25倍変更済み）
- **2026年だけで、Ezoicの要件・Apifyの課金モデル・ACXのAI規約・KDPの価格帯・Stripeの製品構成がすべて変わっている。**四半期ごとの再確認を前提に設計すること

---

## 9. 参考リンク

**実行課金・プラットフォーム**
- [Pay per event（Apify公式）](https://docs.apify.com/platform/actors/publishing/monetize/pay-per-event) / [Monetize Actors（公式）](https://docs.apify.com/platform/actors/publishing/monetize) / [Apify Actor Passive Income 2026](https://agentbyline.com/articles/apify-actor-passive-income-what-really-earns-in-2026-67lcfr)
- [Revenue share for Shopify App Store developers（公式）](https://shopify.dev/docs/apps/launch/distribution/revenue-share) / [Shopify App Revenue Benchmarks 2026](https://weekonelabs.com/blog/shopify-app-revenue-benchmarks-2026/)
- [Browser Extension Monetization Statistics 2026](https://konabayev.com/blog/extension-monetization-statistics-2026/) / [How to Monetize a Chrome Extension 2026 — Fungies](https://fungies.io/monetize-chrome-extension-2026/)

**決済・MoR**
- [Stripe vs Paddle vs Lemon Squeezy vs Gumroad: Fees Compared 2026](https://www.globalsolo.global/blog/stripe-vs-paddle-vs-lemon-squeezy-2026) / [Merchant of Record for SaaS 2026 — Fungies](https://fungies.io/merchant-of-record-for-saas-guide-2026/) / [Lemon Squeezy vs Stripe vs Paddle for Solo Devs](https://dev.to/devtoolpicks/lemon-squeezy-vs-stripe-vs-paddle-which-should-solo-devs-use-in-2026-2jm9)

**受託・生産化サービス**
- [AI Automation Agency Pricing 2026 — Taskip](https://taskip.net/ai-automation-agency-pricing/) / [Productized AI services: 7 offers buyers want in 2026](https://buildwithdew.com/blog/productized-ai-services-7-offers-buyers-want-2026) / [AI Agency Pricing Guide 2026](https://digitalagencynetwork.com/ai-agency-pricing/)

**所有資産・物販**
- [Gumroad vs Etsy 2026 Fee Comparison](https://fluxnote.io/guides/gumroad-vs-etsy-for-digital-products) / [Gumroad Pricing 2026](https://www.schoolmaker.com/blog/gumroad-pricing)
- [Amazon KDP AI Content Policy 2026](https://univers.studio/blog/ai-generated-content-kdp/) / [KDP AI Disclosure Rules 2026](https://kdpbuilder.com/blog/kdp-ai-disclosure-rules)
- [Substack vs Ghost 2026](https://www.sequenzy.com/versus/substack-vs-ghost) / [27 Best SaaS Affiliate Programs 2026](https://supademo.com/blog/saas-affiliate-programs) / [12 Best SaaS Affiliate Programs (Lifetime Pay)](https://arvow.com/blog/best-saas-affiliate-programs)

**リスク（2026年の規制・執行）**
- [Google's August 2026 Spam Update — Scaled Content Abuse（ケーススタディ）](https://www.gsqi.com/marketing-blog/august-2026-google-spam-update-case-studies/) / [Scaled Content Abuse Crackdown Guide](https://www.digitalapplied.com/blog/scaled-content-abuse-google-march-update-ai-pages-decimated)
- [Organic Traffic Crisis Report 2026 Update](https://thedigitalbloom.com/learn/organic-traffic-crisis-report-2026-update/) / [Zero-Click Search Statistics 2026](https://www.omnibound.ai/blog/zero-click-search-statistics) / [AI Overviews Impact on Publishers — SEJ](https://www.searchenginejournal.com/impact-of-ai-overviews-how-publishers-need-to-adapt/556843/)
- [AdSense vs Mediavine vs Ezoic vs Raptive 2026](https://earnifyhub.com/blog/blogging/mediavine-vs-raptive-vs-ezoic-rpm) / [Best Ad Networks for Publishers 2026](https://newormedia.com/blog/best-ad-networks-for-publishers-2026/)
- [Spotify AI Music Policy 2026](https://dynamoi.com/learn/ai-music-distribution/spotify-ai-music-policy) / [DistroKid AI Music Policy 2026](https://lastplaydistro.com/blog/ai-music-monetization-distribution-policies-2026) / [Streaming Fraud Crackdown 2026](https://www.chartlex.com/blog/business/music-streaming-fraud-crackdown-2026)
- [Does ACX Allow AI Narration? 2026 Policy](https://www.inkfluenceai.com/blog/ai-narration-audible-acx-policy-2026) / [Are AI Audiobooks Accepted on Audible in 2026](https://storyvox.app/blog/are-ai-audiobooks-accepted-on-audible-2026-rules)
- [YouTube AI Slop Crackdown 2026](https://outlierkit.com/resources/youtube-ai-slop-crackdown-2026/) / [YouTube clarifies policies around AI slop — TechCrunch](https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/)
