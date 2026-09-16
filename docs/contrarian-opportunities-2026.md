# 逆張り案と需要検証 — 2026年、人がまだ見ていない場所

調査日: 2026-09-16
関連: [自動化×マネタイズ全体](./automation-monetization-playbook.md) / [SNS特化](./sns-automation-monetization-research.md)

---

## 0. 逆張りの原理

> **「ゴールドラッシュではツルハシを売れ」は、2026年にはもう全員がやっている。**
> **売るべきは、ゴールドラッシュの"後始末"だ。**

2026年のAI関連プレイヤーは、ほぼ全員が「**作る側**」に立っている。生成する、配信する、取得する、エージェント化する。
しかし金が発生し始めているのは、**作られた後に必ず生まれる問題**の側だ。

| みんなが走っている方向 | 空いている裏側 |
|---|---|
| AIでコンテンツを作る | **それが法的に開示されているかの継続監査**（義務化済み・罰金€15M） |
| AIに引用されにいく（GEO/AEO） | **AIが間違えたことを直す**（ツールは10社超、"直す"は誰も売っていない） |
| データを取りに行く（スクレイパー） | **扉が閉じた**（Cloudflareが2026-09-15にデフォルトブロック開始） |
| エージェントを作る | **エージェントから読まれる側の整備**（<200msのagent-facing API） |
| 新しいプラットフォームに乗る | **追い出された人たち**（Ezoicは一晩で90%を締め出した） |

**構造的な美しさ**: AIで儲けようとする人が増えれば増えるほど、規制対象者と被害者と難民が増える。
つまりこれは **AIブームに賭けるのではなく、AIブームの排出物に賭ける**ポジション。ブームが終わっても規制と後始末は残る。

---

## 1. まず、需要データで死んだ案（正直に記録）

思いついたが、調べたら既に埋まっていた。**この2つは追わない。**

### ❌ 死亡①：日本の官公庁データ（入札・補助金）のスクレイパー
「日本語データは英語圏の開発者が触らないから空白」という仮説は**間違いだった**。Apifyに既に複数存在する：
- `hitujino56/jp-procurement`（Japan Government Procurement Scraper）
- `datakura/japan-tenders-scraper`（**$2/1,000 tenders** と価格まで付いている）
- `jpopendata/japan-datagojp-catalog`（data.go.jp カタログ）

しかもKKJポータルは**認証不要のREST APIを公式提供**しており、入札・補助金・施設登録・再エネ認証・金融ライセンス・貿易統計が既に構造化されている。→ 参入する理由がない。

### ❌ 死亡②：利用規約・プライバシーポリシーの変更監視
「地味すぎて誰もやらない」と思ったが**完全に飽和**していた：
- Apify内: `peterdrucker481/policy-change-monitor`（節単位の差分、重要度をlow/medium/highで分類）、`riad_h/policy-change-detector`
- 外部: TOSTracker（引用可能な永続URL付き差分）、TermGuard（24時間監視＋AI要約）、PageCrawl.io

→ 「地味だから空いている」は成り立たない。**地味な領域こそ先に埋まっている。**

---

## 2. 【最大の発見】難民カレンダー2026

**2026年だけで、これだけの強制移行が発生している。**

| 日付 | 何が起きた | 難民の規模 |
|---|---|---|
| **2026-02** | **Ezoic が最低要件を月1万→25万ユーザーへ（2,500%増）** | **パブリッシャーベースの90%を一晩で締め出し**。月5万訪問のサイトが軒並み対象外に |
| 2026-02-06 | X API 無料枠を新規廃止、従量課金へ | 個人ボット運用者が全滅 |
| 2026-03 | **OpenAI が Instant Checkout を約5ヶ月で撤退** | 導入した約30 Shopify店舗が宙ぶらりん（売上はほぼゼロだった） |
| 2026-04-20 | X API の follow/like/quote 書き込みがEnterprise専用に | 自動化ツールが機能停止 |
| 2026-09-01 | X API レガシーPro($5,000/月)廃止・強制移行 | 既存契約者全員 |
| **2026-09-15** | **Cloudflare が mixed-use AIクローラーをデフォルトブロック開始** | **新規顧客・新規サイト・既存無料顧客の全て**。昨日から壊れているスクレイパーとエージェントが大量にある |
| **2026-10-01** | **Apify レンタル課金モデルが完全廃止** | 全レンタルActorが pay-per-event へ移行必須 |
| **2026-12-02** | **EU AI Act：既に市場にあるマーキングシステムの適合期限** | まだ誰も騒いでいない。**あと2.5ヶ月** |
| **2027-02-01** | **YouTube YPP 要件が倍増**（8,000時間 / Shorts 2,000万） | 予告済み。**今から仕込める唯一の未来の難民** |

### 難民ビジネスが構造的に強い4つの理由
1. **期限がある** → 「いつか」ではなく「今月中に」買う
2. **痛みが具体的** → 「収益が止まった」「動かなくなった」。説明不要
3. **競合がまだ気づいていない** → 移行需要は発生から数週間、無風地帯
4. **顧客リストが公開されている** → 誰がそのサービスを使っていたかは外から分かる

**そして移行ツールは、コードそのもの。Claude Code との相性が完璧。**

---

## 3. 逆張り案 5本（需要根拠と競合状況つき）

### 案1 ⭐️ EU AI Act 第50条「開示の継続監査」— **本命**

**なぜ逆張りか**: 2026-06-29の Digital Omnibus で **高リスクAIの義務が2027-12-02へ延期された**ため、業界の注目が一斉に離れた。
**しかし第50条（透明性）は延期されていない。2026-08-02から既に施行中**である。この非対称性が空白を生んでいる。

**義務の内容**（高リスクかどうかに関係なく適用）
1. チャットボットは自分が機械であると名乗る
2. **AI生成物は機械可読な形式でマーキング**（かつ可能な限り人間にも知覚可能に）
3. ディープフェイク・AI生成ニュースはラベル表示
4. 感情認識・生体分類は本人に通知

「**最初の対話・接触の時点で**、明確かつ識別可能な方法で」が要件。利用規約の奥やフッター、メニューの裏に埋めるのは**明確に不可**。

**罰則**: **€1,500万 または 全世界売上の3%**（高い方）。**域外適用** — EUに establish していなくてもEUユーザーに提供していれば対象。

**既存競合**（調査済み）
- `Article50Ready`: 無料スキャナー、35以上のチャットボット/AIウィジェットを検出、24のEU言語で開示文を生成、証拠PDF
- `DiscloseKit`: 10言語、サインアップ不要の無料トライアル
- `TIP Protocol`: 暗号署名ベースの機械可読ラベル標準

**残っている空白（＝ここを取る）**
- ✅ **継続監視**。上記3つは全て「今コンプラか」の**一発診断**。しかしC2PAの最大の弱点は**保存性** — アップロード、スクリーンショット、書き出し、プラットフォーム変換でメタデータは壊れる。「先月は適合していたが、今は壊れている」を検知する商品が**存在しない**。監視＝繰り返し課金に自然に乗る
- ✅ **2026-12-02のマーキングシステム期限**。既存ツールは 8/2 を訴求しており、12/2 を訴求していない。**あと2.5ヶ月の無風地帯**
- ✅ **日本語圏が完全に空白**。域外適用なので、EU向けに何か売っている日本企業＋チャットボット＝全員対象。だが日本企業のこの認知はほぼゼロ。英語圏ツールはここにリーチしない

**商品形態**: 無料診断（URLを入れるだけ）→ 継続監視の月額 → 証拠文書の自動生成。Actor / MCPサーバー / SaaS のいずれでも実装可能。

---

### 案2 ⭐️ Cloudflare 9/15 難民の「合法な移行」案内

**なぜ逆張りか**: 全員がスクレイパーを作っている最中に、**扉が閉じ始めた**。2026-09-15から Cloudflare が mixed-use AIクローラー（検索インデックスとAI学習/エージェント用収集を兼ねるもの）を広告表示ページからデフォルトでブロック。対象は新規顧客・新規サイト・**既存の無料顧客すべて**。
さらに Cloudflare は Pay Per Crawl を **Pay Per Use** へ進化させている — **取得された時ではなく、コンテンツがAIの回答を形作った時に**パブリッシャーへ支払う。初期パートナーは Ceramic.ai と You.com。

**⚠️ 設計上の絶対条件**: これは「**ブロック回避**」ではない。回避を売るのは倫理的にもToS的にもアウトで、持続もしない。
売るのは「**合法な経路への移行**」— 公式API、RSS、ライセンス契約、Pay Per Use、TollBit等への振り替え。

**需要**: 昨日から発生中。壊れた側はまだ「なぜ取れなくなったか」を理解していない。
**競合**: クローラー**分析**側は飽和（AWS WAFが2026-02にAI活動ダッシュボード、Cloudflare Bot Management、Profound、Hall、TollBit）。だが**「壊れた取得側を合法経路へ移す」側は無風**。

---

### 案3 「AIが間違えたことを直す」— GEOの完全な裏返し

**なぜ逆張りか**: 「AIに見えているか」のダッシュボードは10社以上が売っている（Profound、AthenaHQ、Peec AI、Otterly.ai、Knowatoa、Scrunch AI、Brandlight、Goodie AI、Ahrefs Brand Radar、Semrush AI Toolkit）。
**しかし誰も「直す」を売っていない。** 全員が計測器を売り、治療を売っていない。

**需要の実データ**
- GEOは月間検索22,000回のカテゴリに成長。だが**AI検索をトラッキングしている企業はまだ16%**
- ブランド文脈の「ハルシネーション」の大半は**無から作られた嘘ではなく、古い事実・誤ったページ・別会社への紐付け**。つまり**直せる**
- 修正手順は既に確立: 証拠取得 → 引用元ページの修正 → 周辺レコードの修正 → 再クロール強制 → 製品内フィードバック提出 → 回答が反転するまで再テスト
- 反映速度: Perplexityは数日、ChatGPT/Claudeは数週間〜数ヶ月

**空白**: 既存ツールは全てエンタープライズ向けダッシュボード。**中小企業向けに「検知して直すところまで」を定額で請け負う商品が存在しない**。
これは**サービス**であり、監視部分だけClaude Codeで自動化すれば、残りは再現可能な手順書になる。

---

### 案4 「エージェントから見えているか」診断 — GEOとは別物

**なぜ逆張りか**: OpenAIのInstant Checkoutは2026-03に約5ヶ月で撤退し、導入した約30店舗の売上はほぼゼロだった。**派手な製品は死んだ**。
だが基盤は生きている — ChatGPT Shopping は全米ユーザーに展開済みで、Etsyと**100万以上のShopify店舗**が接続。ACP（OpenAI・Stripe・Metaが共同策定）が標準に。

**核心**: 「**機械可読な形で露出していない店舗は、この段階で存在しないのと同じ**」。
さらに agent-facing エンドポイントは**200ms以下**の応答が必要で、「現行のほとんどの技術スタックはこの水準にない」。

**GEOとの違い**: GEOは「文章で言及されるか」。これは「**取引できる形になっているか**」。前者は10社が争い、後者は空いている。

---

### 案5 「AIに見えない地方の店」— 低テック・高需要

**需要の実データ**
- 2026年初頭、米Google検索の**68%がノークリック**で終了（2024年の約60%から上昇）。**AI Overviews が出る検索では83%がノークリック**
- AIの回答に引用される店は、**例外なく Google Business Profile が完全かつ能動的に管理されている**
- AI Overview内に引用されたブランドは、同じページに表示されているが引用されていないブランドより**約35%多くクリックを得る**

**空白**: 日本の中小事業者のGBP放置率は極めて高い。監査はClaude Codeで自動化でき、改善作業は定型化できる。
**弱点**: 営業が重い（1件あたりの単価が低く、対面が必要）。→ 受託寄りの選択肢。

---

## 4. 推奨：どれを取るか

**本命は案1（EU AI Act 第50条の継続監査）。** 理由は4つ。

1. **支払い意思が構造的に巨大** — 罰金€1,500万/売上3%。コンプライアンス予算は景気に左右されない
2. **繰り返し課金に自然に乗る** — 監視は本質的にサブスクリプション。一発診断ツールは売り切りで終わる
3. **競合の空白が二重にある** — 「継続監視」と「12/2期限」。既存3社は両方とも訴求していない
4. **日本語圏が丸ごと空いている** — 域外適用なのに日本企業の認知はゼロに近い。英語圏ツールは日本にリーチしない

そして最大の理由：
> **AIで何かを作る人が増えるほど、この商品の顧客が増える。**
> AIブームに賭けるのではなく、AIブームの排出物に賭けている。ブームが終わっても規制は残る。

**併走させるなら案2（Cloudflare難民）**。発生が昨日で、無風期間が最も短いため先に手を付ける価値がある。ただし必ず「合法経路への移行」として設計すること。

---

## 5. 最初の7日（案1の場合）

| Day | やること |
|---|---|
| 1–2 | 第50条の4類型を判定ロジックに落とす。チャットボットウィジェット検出、AI生成物のマーキング有無、C2PA/メタデータの生存確認 |
| 3–4 | **無料診断**として公開（URLを入れるだけ）。Apify Actor + 静的ページの二面展開。課金はpay-per-event |
| 5 | 日本語の診断レポートと、**域外適用の説明**を用意。ここが英語圏ツールとの差 |
| 6–7 | **12/2期限**を軸にした告知。診断した企業に「継続監視」を提示して反応を測る |

**測る指標**: 診断実行数ではなく、**「継続監視はいくらですか」と聞かれた回数**。それがゼロなら案2か案3へ2週間で乗り換える。

---

## 6. 検証上の注意

- 本調査はウェブ検索による2026年時点の二次情報。egressポリシーにより一次情報（EU公式文書、Cloudflare公式ブログ、Apify Store実データ等）への直接アクセスは未実施
- **法規制を商品にする以上、条文の一次確認は絶対に必要**。特に以下：
  - EU AI Act 第50条の条文と、2026-12-02のマーキングシステム適合期限の正確な射程
  - Digital Omnibus による延期対象の正確な範囲（**第50条は延期対象外**という前提が本案の根幹）
  - 罰則額（€1,500万 / 全世界売上3%、中小企業は低い方）と域外適用の条件
- 法的助言を提供する商品ではなく、**技術的な検出と証拠生成**に留める設計にすること（越境すると別の規制対象になる）
- Cloudflare案は「回避」ではなく「合法経路への移行」から一歩も出ないこと

---

## 7. 参考リンク

**EU AI Act 第50条**
- [The EU AI Act's Transparency Rules: A Practical Guide to Article 50](https://artificialintelligenceact.eu/transparency-rules-article-50/) / [Article 50: In Force Since 2 August 2026](https://www.regulation-ai.eu/en/transparency-obligations/) / [CSA: Article 50 Transparency Obligations Take Effect](https://labs.cloudsecurityalliance.org/research/csa-research-note-eu-ai-act-article-50-transparency-20260729/)
- [高リスク義務の2027-12-02への延期（CSA）](https://labs.cloudsecurityalliance.org/research/csa-research-note-eu-ai-act-omnibus-vii-deadline-delay-20260/) / [Digital AI Omnibus（DLA Piper）](https://knowledge.dlapiper.com/dlapiperknowledge/globalemploymentlatestdevelopments/2026/The-Digital-AI-Omnibus-Proposed-deferral-of-high-risk-AI-obligations-under-the-AI-Act)
- 既存競合: [Article 50 Ready](http://article50ready.com/) / [DiscloseKit](https://disclosekit.com/) / [TIP Protocol](https://theailab.org/eu-ai-act)
- [C2PA Adoption Status 2026](https://www.eyesift.com/faq/c2pa-content-credentials-2026-cryptographic-provenance-adoption/) / [C2PA の限界（TrueScreen）](https://truescreen.io/articles/c2pa-standard-history-limitations/)

**Cloudflare / クローラー**
- [Cloudflare's new policy pushes AI companies to pay — TechCrunch](https://techcrunch.com/2026/07/01/cloudflares-new-policy-pushes-ai-companies-to-pay-for-publishers-content/) / [Sept 15 AI Crawler Wall（fastCRW）](https://fastcrw.com/blog/cloudflare-ai-crawler-block-september-2026) / [The Closing Web in 2026](https://www.coronium.io/blog/closing-web-ai-crawler-blocking-pay-per-crawl-2026)
- [AWS WAF AI activity dashboard（2026-02）](https://aws.amazon.com/about-aws/whats-new/2026/02/aws-waf-ai-activity-dashboard/) / [Best Tools to Track AI Crawlers 2026](https://www.xseek.io/blogs/articles/best-tools-to-track-ai-crawlers-on-your-website-2026)

**GEO / ハルシネーション修正**
- [Best GEO tools for AI search 2026（Profound）](https://www.tryprofound.com/blog/best-generative-engine-optimization-tools) / [AI Search Visibility Tools 2026: 10 Compared](https://industry-lens.com/intelligence/ai-search)
- [AI is Saying Wrong Things About My Company](https://trackmybusiness.ai/blog/ai-is-saying-wrong-things-about-my-company-how-to-fix-hallucinations-in-2026/) / [AI Hallucinations About Your Brand（Insightland）](https://insightland.org/blog/ai-hallucinations-about-your-brand-what-to-do-when-models-get-the-facts-wrong/)

**エージェント／コマース**
- [How to Prepare for Agentic Commerce（Bluestone PIM）](https://www.bluestonepim.com/blog/how-to-prepare-for-agentic-commerce) / [Agentic Commerce 2026: A Reality Check for Retailers](https://www.redvanworkshop.com/red-van-blog/agentic-commerce-2026-reality-check) / [Product Feed for Agentic Checkout](https://www.get-ryze.ai/blog/prepping-your-product-feed-for-agentic-checkout-after-instant-checkout)

**難民（強制移行）**
- [Ezoic が小規模パブリッシャーを締め出した件](https://newormedia.com/blog/best-ezoic-alternatives-2/) / [Ezoic Review 2026](https://newormedia.com/blog/ezoic-review-is-it-worth-it/)
- [Apify レンタルモデル廃止と PPE](https://docs.apify.com/platform/actors/publishing/monetize/pay-per-event)
- [Local SEO 2026: GBP × AI](https://www.digitalapplied.com/blog/local-seo-2026-google-business-profile-ai-guide) / [AI Overviews と小規模事業者の引用](https://nickthrolson.com/google-ai-overviews-small-business/)

**死亡確認した案の根拠**
- [Japan Government Procurement Scraper（Apify）](https://apify.com/hitujino56/jp-procurement) / [Japan Tenders Scraper $2/1K（Apify）](https://apify.com/datakura/japan-tenders-scraper) / [JP Open Data（Apify）](https://apify.com/jpopendata)
- [Vendor Policy, Terms & Privacy Change Monitor（Apify）](https://apify.com/peterdrucker481/policy-change-monitor) / [TOSTracker](https://tostracker.app/) / [TermGuard](https://www.termguard.app/)
