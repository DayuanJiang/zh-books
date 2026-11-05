# 术语表

翻译前根据 `review/terms/` 里的统计数据裁定（来源和门槛见 [review/terms/README.md](review/terms/README.md)）。“出现次数”和“首次出现”由 `tools/term_stats.py` 按英文词形统计，含标题；按正则匹配，可能把同词根的普通用法也算进去，例如 learning、meeting、commit。状态都是“初定”，由 Claude 裁定，等用户确认；改动时要回查已经译完的章节。

这本书没有查到中文译本，书名、章节标题和术语都是这里自己定的。

## 体例

- **人名**：用 [review/terms/people-zh.tsv](review/terms/people-zh.tsv) 的译名。每节第一次出现时在中文名后括注英文原名，例如“史蒂夫·布兰克（Steve Blank）”，之后只写中文。只有名的人（Marcy、Pete、Tim）也一样括注。原文拼错的名字，括注写正确拼法：Gordon Ramsey 写“戈登·拉姆齐（Gordon Ramsay）”。
- **机构、产品、网站**：见下面“机构、产品与地名”。没有通行中文名的公司和产品照写原名，和汉字之间加空格。网址、邮箱和推特账号照写，链接地址不动。
- **书名**：用《》，每节第一次出现时括注原题，原题用斜体，例如《四步创业法》（*4 Steps to the E.piphany*）。有中译本的用中译本书名。
- **数字和金额**：见“全书统一的写法”。
- **称呼**：作者对读者说话用“你”，不用“您”。your mom 写“你妈妈”，不写“你妈”。
- **示例对话**：每句一段，说话人加粗，后面是中文冒号，台词放在中文引号里，作者的旁白用斜体放在台词后面，和英文一样：`**儿子：**“妈，妈，我有个生意点子，能跟你说说吗？” *我要把自尊心亮出来了，千万别伤我的心。*`。说话人统一这样写：You 写“你”，Them 写“对方”，Me 写“我”，Mom 写“妈妈”，Son 写“儿子”，Your Team 写“你的团队”。台词前后括号里的舞台说明，例如 (Back at the office)、(More delicious workflow data)，照原样放在括号里译出。原文个别台词没有引号（第 3 章两句），照原文不加。
- **经验法则**：每节末尾的 *Rule of thumb:* 写成 `*经验法则*：`，斜体只包住“经验法则”四个字，冒号放在斜体外面，后面直接接正文。冒号不能放进斜体：阅读器用 markdown-it 按 CommonMark 渲染，`*经验法则：*客户` 这样结尾的星号前面是全角标点、后面紧跟汉字，斜体不会生效，页面上会露出星号。加粗也一样：第 3 章两句没有引号的台词写成 `**你**：`，有引号的台词照“示例对话”的写法（`**你：**“`，后面是引号，没有这个问题）。第 1 章译完后发现并改正（原来写的是 *经验法则：*）。
- **列表和引用块**：列表的项数、嵌套层级和列表符号照英文写。速查表 “The process before, during and after the meeting” 下面三个连着的列表，中间那个英文用 `*`，中文也必须用 `*`，否则 Markdown 会把三个列表合成一个，中英两边对不上。示范邮件是引用块，每封一个，空行处的 `>` 照写。
- **原文的引号和括注**：直引号和弯引号，中文一律用“”。示范邮件里括注的斜体标签，(*vision*) 写成（*愿景*），对照“Vision / Framing / Weakness / Pedestal / Ask”一行。
- **代号和占位字母**：X、Y、Z、customer A 这类占位符照写，例如“像是给 Y 用的 X”。
- **表情和符号**：:)、:( 和笔记符号 ☇ ⨅ ☐ ⤴ ^ ☑ ＄ ♀ ☆ 照写。
- **e.g.**：作者常把 e.g. 当 i.e. 用（例如 “(e.g. fluffy)”），按“也就是”的意思译，见 [review/source.md](review/source.md)。
- **原文笔误**：按作者显然要表达的意思译，不加译者注；只有会影响理解的地方才加。各处笔误和处理方式见 [review/source.md](review/source.md) 的“原文疑点”。
- **破折号和句式**：中文译文不用破折号（——），原文的破折号按意思改成逗号、冒号、括号或另起一句；也不用“不是……而是……”这种句式，换成直接的说法。这本书里 “X, not Y”“X instead of Y” 很多，例如 “Talk about their life instead of your idea”，可以译成“谈他们的生活，别谈你的想法”这样的说法。

## 各节标题

| 章节 id | 英文 | 中文标题（`#` 一级标题照这一列写） |
| --- | --- | --- |
| introduction | Introduction | 引言 |
| ch01 | 1. The Mom Test | 第 1 章 妈妈测试 |
| ch02 | 2. Avoiding bad data | 第 2 章 避开坏数据 |
| ch03 | 3. Asking important questions | 第 3 章 问重要的问题 |
| ch04 | 4. Keeping it casual | 第 4 章 轻松随意地聊 |
| ch05 | 5. Commitment and advancement | 第 5 章 承诺与推进 |
| ch06 | 6. Finding conversations | 第 6 章 找到交谈的机会 |
| ch07 | 7. Choosing your customers | 第 7 章 选定你的客户 |
| ch08 | 8. Running the process | 第 8 章 管好整个流程 |
| conclusion | Conclusion and cheatsheet | 结语与速查表 |
| acknowledgments | Acknowledgements | 致谢 |

小节标题（`##`、`###`）由译者照原文译，全部列在 [review/terms/headings.tsv](review/terms/headings.tsv)。速查表的 Key skills 一项列的就是各章的主题，要和章标题、小节标题的说法一致，例如 Keeping it casual 写“轻松随意地聊”，Deflect compliments 写“挡开恭维”。在书里出现不止一次的句子和列表项（速查表大多照抄正文）列在 [review/terms/repeats.tsv](review/terms/repeats.tsv)，各处译法要一字不差。第 1 章和第 5 章的 `###` 小标题重复前面列表里待判断的问题，译文要和列表里的一字不差（第 5 章列表写 intro you to，小标题写 introduce you to，照各自原文译，意思相同）。

译者读完一章后，如果觉得标题另有更贴切的译法，在汇报里提出，由主会话统一修改。

## 全书统一的写法

参照仓库里其他书译完后统一下来的写法，结合这本书先定下来，各章从一开始就照这里写；译完后有新的不一致，再补在这里。

- **数字**：一到十，以及带“几、十几、数百、上千”的约数，用汉字（三条规则、三个大问题、两周、五分钟、几十次谈话）；11 以上的确数用阿拉伯数字（20 次谈话、90 分钟）；年份、日期、钟点、金额、百分比、评分刻度一律用阿拉伯数字（35%、1 到 5 分）。范围的两头只要有一个大于十，都用阿拉伯数字，中间写“到”：10-15 minutes 写“10 到 15 分钟”，3-5 conversations 写“三到五次谈话”。#1、#2 写“第 1 条”“第 2 条”。
- **金额**：换算成中文的万、亿，币种照原文：$40 写“40 美元”，$50k 写“5 万美元”，$5-50k 写“5000 到 5 万美元”，£100/month 写“每月 100 英镑”，£1.2k 写“1200 英镑”，£120,000 写“12 万英镑”，$10,000/month 写“每月 1 万美元”。口语的 bucks 是美元：10 million bucks 写“1000 万美元”，half a million bucks 写“50 万美元”。2 or 3 grand 写“两三千美元”。
- **章节引用**：Chapter 5 写“第 5 章”；速查表的 (Chapters 1 & 3) 写“（第 1 章和第 3 章）”。
- **书名括注**：每节第一次出现时括注原题，原题用斜体。《四步创业法》在引言、第 4 章和致谢各括注一次。
- **人名括注**：名人也照常在每节第一次出现时括注英文，例如“埃隆·马斯克（Elon Musk）”。同一段里后面只写名的（Elon、Reid、Gordon），写姓：马斯克、霍夫曼、拉姆齐。
- **平台名**：写 Twitter，不写“推特”；“推文”照用。Google 写“谷歌”，动词 google / Googled 写“上网搜”或“用谷歌搜”。
- **英文缩写**：B2B、CRM、CSV、PDF、PR、HR、CTO、VC、UX 照写；第一次出现时，原文自己括注了解释的（CRM (contact management)、CSV (data file)），中文照样括注。PR 第一次出现时写“公关（PR）”，VC 写“风险投资人（VC）”。PhD 写“博士”，PhD student 写“博士生”。
- **代词**：对话里泛指的 they、them 写“对方”或“他们”；说话人 Them 一律写“对方”。
- **作者的笑话和双关**：ba-dum tish 这类拟声照意思译（“咚咚锵”）；Hack it 一节 hack 的双关见核心概念表的 hack 一行。七度分隔照原文写“七度”，可以加译者注说明通行说法是六度。

## 核心概念

| 英文 | 首选译法 | 适用的意思 | 不要混同 | 首次出现 | 出现次数 | 状态 |
| --- | --- | --- | --- | --- | --- | --- |
| The Mom Test | 妈妈测试 | 书名，也是全书的核心方法：三条提问规则，照这三条问出来的问题，连你妈妈都没法对你说谎。pass / fail The Mom Test 译“通过 / 通不过妈妈测试”。正文里不加书名号和引号 | 《妈妈测试》（只有指这本书时才用书名号） | ch01 | 25 | 初定 |
| customer conversation | 客户对话 | 和客户、潜在客户聊天，从中了解对方。作者特意用小写，和大写的 Customer Development 区分；引言里下定义时括注英文，并保留“小写”“大写”的说明 | 客户访谈、客户开发 | introduction | 28 | 初定 |
| Customer Development | 客户开发 | 史蒂夫·布兰克提出的整套方法，作者用大写；客户对话只是其中一部分 | 客户对话、客户发展 | introduction | 6 | 初定 |
| Lean Startup | 精益创业 | 埃里克·莱斯提出的方法 |  | introduction | 2 | 初定 |
| Design Thinking / User Experience (UX) | 设计思维 / 用户体验（UX） | 引言列举的几个社群；the UX community 译“用户体验圈子” |  | introduction | 3 | 初定 |
| learning (n.) / customer learning | 收获、了解到的东西 / 了解客户 | 名词 learning 指从对话里得到的认识，按上下文译“收获”“了解到的东西”“学到的东西”；customer learning 译“了解客户”。动词 learn 照常译“了解”“学到”“得知” | 学习（作名词时读起来生硬，尽量少用） | introduction | 48 | 初定 |
| bad data | 坏数据 | 第 2 章：误导你的三种信息，恭维、空话和想法 | 错误数据 | ch02 | 9 | 初定 |
| compliment | 恭维 | 第一种坏数据：对方说的好听话（“很酷，我喜欢”），作者认为几乎都是客套，没有价值。名词也可写“恭维话”，complimenting you 译“恭维你” | 称赞、表扬（语气偏真诚） | ch01 | 61 | 初定 |
| fishing for compliments | 讨夸奖 | 有意寻求认可，想听别人说你的想法好；速查表 Mistakes and symptoms 第一项同 |  | ch02 | 6 | 初定 |
| fluff / fluffy | 空话 / 空泛的 | 第二种坏数据：笼统的说法、假设和对未来的许诺。fluff-inducing question 译“引出空话的问题”。第 2 章 “3 cuddly shapes” 拿 fluff（绒毛）开玩笑，可译“三种软绵绵的样子” | 废话 | ch02 | 30 | 初定 |
| generic / generics | 笼统 / 笼统的说法 | “我通常”“我总是”“我从不”这类概括。generic question 译“笼统的问题”，start more generic 译“从更宽泛的问题问起”。第 1 章说菜谱的 generic set of recipes、generic recipes 指大众化的基础菜谱，和 niche recipes（小众菜谱）相对，译“家常菜谱” | 通用 | ch01 | 29 | 初定 |
| hypothetical | 假设性的 / 假设 | “我可能会”“我也许会”这类说法；hypothetical question 译“假设性问题”，hypothetical la-la-land 译“假设的幻境” |  | ch01 | 10 | 初定 |
| specifics in the past | 过去的具体事情 | 妈妈测试第二条：问已经发生过的具体事情，别问笼统的情况或对未来的看法 |  | ch01 | 3 | 初定 |
| opinion | 看法 | 对方对你的想法、对未来的主观判断。Opinions are worthless. 译“看法一文不值” | 意见（feedback 译“反馈”） | ch01 | 17 | 初定 |
| idea | 想法 | 你的生意想法；也是第三种坏数据（对方提的想法）。business idea 译“生意点子” | 创意 | introduction | 101 | 初定 |
| deflect | 挡开 | deflect compliments 译“挡开恭维”：不接对方的恭维，把话题拉回事实 | 反驳 | ch02 | 13 | 初定 |
| anchor | 锚定 / 锚点 | anchor fluff 译“锚定空话”：把对方的空话拉回到过去的具体事例上；anchor on / from 按上下文译“抓住……追问”；price anchor 译“价格锚点” |  | ch01 | 18 | 初定 |
| dig / dig beneath | 深挖 / 挖下去 | 追问请求、想法和情绪背后的原因。Dig beneath ideas 译“深挖想法背后的东西”；作者单独一句 Dig. 译“挖下去。” |  | introduction | 30 | 初定 |
| feature request | 功能需求 | 对方要求加的功能；符号 ☑ 的说明也用这个译法 | 功能请求 | ch01 | 11 | 初定 |
| feature creep | 功能蔓延 | 功能越加越多，失去重点 |  | ch02 | 2 | 初定 |
| killer feature / must-have | 杀手级功能 / 必备的 | must-have feature 译“必备功能”，must-have product 译“非买不可的产品”，must-have purchasing criteria 译“必须满足的购买标准” |  | ch02 | 5 | 初定 |
| approval / seeking approval | 认可 / 寻求认可 | 想得到别人对你想法的肯定 | 批准 | ch02 | 7 | 初定 |
| The Pathos Problem | 悲情问题 | 作者起的名字：你把自尊心亮出来，对方觉得应该护着你，于是只说好话。第 2 章第一次出现时括注 The Pathos Problem；速查表 aka The Pathos Problem 译“也叫悲情问题” | 情感诉求 | ch02 | 5 | 初定 |
| ego | 自尊心 | expose your ego 译“把自尊心亮出来”，your ego is on the line 译“你的自尊心押在了上面” | 自我（心理学术语）、自负 | ch01 | 7 | 初定 |
| pitch / pitching / pitch mode / pitchy | 推销 / 推销模式 / 推销味重 | 向对方兜售你的想法。slip into pitch mode 译“一不小心进入推销模式”，Cut off pitches 译“打住推销”，startup pitches 译“创业公司的推销” | 路演（只在指向投资人的正式演示时用） | ch01 | 21 | 初定 |
| false positive / false negative | 假阳性 / 假阴性 | 第 2 章开头的定义：假阴性是以为想法不行其实行，假阳性是以为自己对了其实不对 | 误报 | introduction | 10 | 初定 |
| signal | 信号 | 对话里透露出的线索，包括情绪、定价、需求；mixed signals 译“相互矛盾的信号” |  | ch01 | 31 | 初定 |
| lukewarm | 不冷不热 | lukewarm response / signal 译“不冷不热的反应 / 信号” |  | ch01 | 7 | 初定 |
| zoom / premature zoom | 聚焦 / 过早聚焦 | 还没确认对方在乎，就盯住一个具体问题追问细节。zoom in 译“聚焦”，zoom back out 译“退回去看全局”；第 3 章小标题 Look before you zoom 可译“先看全局，再聚焦” | 缩放、放大 | ch02 | 18 | 初定 |
| the elephant (in the room) | 房间里的大象 | 大家心知肚明却回避的关键问题；第 3 章小标题 Look at the elephant 可译“正视房间里的大象” |  | ch03 | 3 | 初定 |
| failure point | 可能失败的环节 | 生意成败取决于的几个环节，任何一个不成立都要大改想法 | 故障点 | ch01 | 3 | 初定 |
| de-risk | 降低风险 | de-risking and validating the business 译“降低风险、验证生意” |  | ch03 | 2 | 初定 |
| product risk / market risk | 产品风险 / 市场风险 | 产品风险：能不能做出来、做大、留住用户；市场风险：有没有人要、肯不肯付钱、人够不够多 |  | ch03 | 9 | 初定 |
| must-solve problem / nice-to-have | 非解决不可的问题 / 有了更好的东西 | 前者对应止痛药，后者对应维生素；must-solve-right-now 译“必须马上解决的” | 刚需（这个流行词和作者的语气不合，不用） | ch03 | 7 | 初定 |
| painkiller / vitamin | 止痛药 / 维生素 | 第 3 章的比喻 |  | ch03 | 2 | 初定 |
| 3 big questions / list of 3 | 三个大问题 / 三问清单 | 每批谈话前和团队定好的三个最重要的问题；Prepare your list of 3 译“准备好你的三问清单”，big 3 learning goals 译“三个最想弄清的问题” |  | ch03 | 12 | 初定 |
| Keeping it casual | 轻松随意 | 第 4 章：把见面变成随意的聊天，不约正式会面。keep it casual 译“保持轻松随意”；作者大写成专名（Keeping it Casual）时也用这个译法，句子里容易和普通说法混在一起时加引号 | 随便（带贬义） | ch03 | 14 | 初定 |
| The Meeting Anti-Pattern | 会面反模式 | 作者借软件工程的“反模式”：把每次和客户交谈的机会都塞进日程表里，变成正式会面。第 8 章 a common anti-pattern 也译“反模式” |  | ch04 | 3 | 初定 |
| meeting | 会面 | 和客户、投资人等的见面。sales meeting 译“销售会面”，product meeting 译“产品会面”，formal meeting 译“正式会面”；calendar block 译“日程表里的一个时段”；Good meeting / bad meeting 译“好会面，坏会面” | 会议（团队内部开会、行业会议才用） | introduction | 131 | 初定 |
| formal / formality | 正式 / 拘泥形式 | 作者反对的做法：约正式会面、按访谈提纲提问。Symptoms of formality 译“过于正式的症状”，Being too formal 译“太正式” |  | introduction | 17 | 初定 |
| commitment / commit | 承诺 | 第 5 章：对方拿出自己看重的东西（时间、声誉、金钱），表明自己是认真的。time / reputation / financial commitment 译“时间上的承诺 / 拿声誉作的承诺 / 资金承诺”；commit to it 译“为它作出承诺”。第 4 章普通意义的 a big time commitment 译“要花很多时间” | 许诺（promise） | ch01 | 53 | 初定 |
| advancement / advance | 推进 | 第 5 章：把销售关系推进到下一步，作者说这是销售里的说法。push for advancement 译“争取推进”；Commitment & Advancement 作专名时译“承诺与推进” | 进步、晋升 | ch01 | 20 | 初定 |
| promise | 许诺 | 对未来的口头保证，属于空话。future-promise statement 译“对未来的许诺”，fluffy future promises 译“空泛的未来许诺” | 承诺（commitment） | ch01 | 11 | 初定 |
| next steps | 下一步 | 见面结束时约好的后续安排；clear next steps 译“明确的下一步” |  | ch04 | 24 | 初定 |
| currency | 货币 | 第 5 章 The currencies of conversation 的比喻：对方为你付出的东西，主要有时间、声誉风险和现金；think in terms of currency 译“从货币的角度想” |  | ch05 | 5 | 初定 |
| reputation risk | 声誉风险 | 对方拿自己的声誉冒险，例如把你引荐给老板或公开推荐你 |  | ch05 | 6 | 初定 |
| letter of intent / pre-order / deposit | 意向书 / 预订 / 订金 | 三种资金承诺；pre-purchase 也译“预订”。意向书原文括注 non-legal but gentlemanly agreement，译“没有法律约束、凭君子风度的购买约定” | 定金（法律上有特定含义） | ch01 | 10 | 初定 |
| lead (n.) / zombie leads | 潜在客户、线索 / 僵尸线索 | 销售意义的 lead 按上下文译“潜在客户”或“线索”：qualified leads 译“合格的潜在客户”，cold leads 译“不认识的潜在客户”，real leads 译“真正的潜在客户”；第 1 章 promising leads 指值得追下去的线索。zombie leads 指一直和你见面、说好话，却从不掏钱的潜在客户（或投资人） | 动词 lead（引导） | ch01 | 14 | 初定 |
| friend-zoned | 被发好人卡 | 第 5 章的比喻：对方对你客客气气，就是不买；get out of the friend-zone 译“摆脱好人卡” | 朋友区（直译读者看不懂） | ch05 | 2 | 初定 |
| funnel / pipeline | 漏斗 / 销售管道 | acquisition funnel 译“获客漏斗”，real-world funnel 译“现实中的销售漏斗” |  | ch05 | 5 | 初定 |
| stalling tactic | 拖延战术 | 对方用来脱身的客气话，例如“上线了告诉我”；compliment-stall 译“恭维加拖延” |  | ch02 | 8 | 初定 |
| earlyvangelists | 早期布道者 | 史蒂夫·布兰克的造词，由 early evangelists 合成，原文自己括注了；中文写“早期布道者（earlyvangelists，即 early evangelists）” | 早期使用者（early adopters） | ch05 | 2 | 初定 |
| first customers / early customers / crazy customers | 第一批客户 / 早期客户 / 疯狂的客户 | 第 5 章：最早买你东西的人都是“疯子”，作者说是褒义 |  | ch02 | 4 | 初定 |
| customer segment / segment | 客户群 | 一群需求、目标相近，找得到的客户。focused segment 译“聚焦的客户群”，slice that segment 译“把这个客户群切得更细” | 细分市场（只在原文明确说 market 时用） | ch01 | 35 | 初定 |
| segmentation | 客户细分 | 第 7 章小标题和速查表 Customer segmentation |  | ch07 | 6 | 初定 |
| Customer Slicing / slice | 客户切分 / 切分 | 第 7 章作者命名的做法：把客户群一层层切成更具体的小群，直到知道他们是谁、去哪儿找。第一次出现时括注 Customer Slicing | 切片 | ch07 | 8 | 初定 |
| who-where pair | “谁”和“在哪儿”的组合 | 好的客户群要同时知道是谁、在哪儿找得到 |  | ch07 | 2 | 初定 |
| demographic | 人口特征 / 人群 | demographic data 译“人口统计数据”，demographic groups 译“按人口特征划分的人群”，demographic constraint 译“人口特征上的限定” |  | ch03 | 6 | 初定 |
| workaround | 变通办法 | 客户现在自己凑合着用的解决办法；符号 ⤴ 的说明也用这个译法 | 权宜之计 | ch01 | 9 | 初定 |
| makeshift / home-brew / duct-tape solution | 临时凑合的办法 / 自制的土办法 / 胶带粘起来的办法 | 早期布道者的特征之一：已经自己拼凑出解决办法。duct-tape prototype 译“胶带粘起来的原型” |  | ch01 | 6 | 初定 |
| pain | 痛点 | 客户的问题和麻烦；符号 ☇ Pain or problem 译“痛点或问题”。it’s a big pain 这类口语按“很麻烦”译 |  | ch01 | 8 | 初定 |
| budget / budget owner | 预算 / 掌握预算的人 | budget-holder 同 budget owner；discretionary budget 译“可以自己支配的预算” |  | ch01 | 12 | 初定 |
| decision maker / stakeholders | 决策者 / 利益相关方 | 第 7 章：采购流程复杂的企业里，容易漏掉的人 |  | ch05 | 4 | 初定 |
| purchasing process / buying criteria | 采购流程 / 购买标准 | purchasing criteria 同 buying criteria |  | ch01 | 9 | 初定 |
| enterprise / B2B / consumer | 企业 / B2B / 消费者 | enterprise sales 译“企业销售”，enterprise software 译“企业软件”，consumer products 译“面向消费者的产品”，in the consumer space 译“在消费者市场” |  | ch01 | 14 | 初定 |
| intro / warm intro | 引荐 / 熟人引荐 | make intros 译“帮忙引荐”；warm intro 指通过共同的熟人介绍；intro train 译“一连串的引荐”；Creating warm intros 译“争取熟人引荐” | 介绍（产品介绍） | ch01 | 24 | 初定 |
| cold (calls, emails, conversations, approaches) | 陌生（电话、邮件、对话、接触） | 主动联系不认识的人。cold calls 译“陌生电话”，cold conversations 译“和陌生人的谈话” | 冷淡 | ch06 | 12 | 初定 |
| serendipity / serendipitous | 偶遇 / 意外的 | Seizing serendipity 译“抓住偶遇的机会”，serendipitous encounters 译“偶然的相遇”，serendipitous learning 译“意外的收获” |  | ch03 | 4 | 初定 |
| landing page | 落地页 | 第 6 章。同一段的 value proposition 译“价值主张”，conversion rate 译“转化率”，metrics 译“指标” |  | ch06 | 3 | 初定 |
| framing / frame | 定调 | 约见面和见面开头时，说明这次见面是为了什么、你处在什么阶段，让对方有合适的预期。Asking for and framing the meeting 译“约见面并定调”，frame expectations 译“给对方的预期定调” | 框架、陷害 | ch06 | 14 | 初定 |
| Vision / Framing / Weakness / Pedestal / Ask | 愿景 / 定调 / 示弱 / 捧高对方 / 请求帮助 | 第 6 章约见面的五个要素。示范邮件里括注的斜体标签照这一列写，(*ask*) 写“（*请求*）”，(*authority*) 写“（*权威*）”。口诀 Very Few Wizards Properly Ask [for help] 保留英文（五个词的首字母对应五个要素），后面括注中文意思和对应关系 |  | ch06 | 14 | 初定 |
| advisor / the advisory flip | 顾问 / 换上找顾问的心态 | 第 6 章：别抱着找客户的心态去谈，改为寻找懂行业的顾问；the sales-advisor switch 同义，译“从销售到顾问的转换”。industry advisors 译“行业顾问”，advisory board 译“顾问委员会” |  | introduction | 16 | 初定 |
| opportunity cost | 机会成本 |  |  | ch06 | 2 | 初定 |
| learning bottleneck | 信息瓶颈 | 第 8 章：对客户的了解全卡在一个人脑子里，传不到团队。Being a learning bottleneck 译“成为信息瓶颈”，bottleneck（动词）译“卡住信息” | 学习瓶颈 | ch08 | 7 | 初定 |
| prepping / reviewing | 会前准备 / 复盘 | 第 8 章的两个环节；review your notes with your team 译“和团队一起复盘笔记”，Prep questions 译“准备时要问的问题” | 审查、评论 | ch04 | 25 | 初定 |
| notes / signal symbols | 笔记 / 信号符号 | 第 8 章和速查表的记笔记符号。符号照写，说明照这里统一：Excited 兴奋，Angry 生气，Embarrassed 尴尬，Pain or problem 痛点或问题，Goal or job-to-be-done 目标或待完成的任务，Obstacle 障碍，Workaround 变通办法，Background or context 背景或情境，Feature request or purchasing criteria 功能需求或购买标准，Money or budgets or purchasing process 钱、预算或采购流程，Mentioned a specific person or company 提到具体的人或公司，Follow-up task 后续任务；括号里的 symbol is a lightning bolt 译“符号是一道闪电” |  | introduction | 56 | 初定 |
| job-to-be-done | 待完成的任务 | 客户想办成的事，出自“待完成的任务”（jobs to be done）理论 | 工作 | ch08 | 2 | 初定 |
| going through the motions | 走过场 | Signs you’re just going through the motions 译“你只是在走过场的迹象” |  | ch08 | 3 | 初定 |
| desk research | 案头调研 | 上网、查资料就能回答的问题，先自己查 |  | ch08 | 3 | 初定 |
| validation / validate | 验证 / 肯定 | 用证据确认想法成立，译“验证”；作者批评的 taken it as validation，说的是把恭维当成了想法成立的证据，译“当成了对想法的肯定” |  | ch01 | 13 | 初定 |
| visionary leap | 凭远见迈出的一步 | 了解客户之后，自己构想解决方案的那一步；take the leap 按上下文译“迈出这一步” |  | ch01 | 5 | 初定 |
| Rule of thumb | 经验法则 | 每节末尾的斜体标签，写成 `*经验法则*：`，冒号在斜体外面（原因见体例“经验法则”一条） |  | ch01 | 38 | 初定 |
| hack | 巧招 | 结语 Hack it 一节：hack 既有“砍”的意思，也指取巧的捷径，作者拿亚历山大斩断戈尔迪之结的故事双关。小标题可译“快刀斩乱麻”，a hack 译“一记巧招”，hack through the knot 译“一刀斩断这个结” |  | ch06 | 4 | 初定 |
| founder / entrepreneur / startup | 创始人 / 创业者 / 创业公司 | startup knowledge 译“创业知识”，startup life 译“创业生活”，early stage 译“早期” |  | introduction | 65 | 初定 |
| customer / user | 客户 / 用户 | 一般写“客户”；指使用产品的人时写“用户”，例如 alpha users、critical mass of users |  | introduction | 194 | 初定 |
| business | 生意 / 公司 / 业务 | whether your business is a good idea 译“你的生意点子好不好”，build your business 译“把公司做起来” |  | introduction | 69 | 初定 |
| industry expert | 行业专家 |  |  | ch01 | 4 | 初定 |
| dealflow | 项目来源 / 销售机会 | 第 4 章投资人的 dealflow 指收到的投资项目；第 6 章 doubling up on learning and dealflow 指对话同时带来收获和销售机会 |  | ch04 | 2 | 初定 |
| case study / testimonial | 案例 / 推荐语 | be a case study for launch 译“在发布时当我们的案例” |  | ch05 | 4 | 初定 |
| trial / prototype / alpha users / beta keys | 试用 / 原型 / 内测用户 / 测试版激活码 | paid trial 译“付费试用”，free trial 译“免费试用” |  | ch03 | 18 | 初定 |
| local maximum | 局部最优 | 第 4 章 |  | ch04 | 1 | 初定 |
| thought experiment | 思想实验 | 第 3 章 |  | ch03 | 1 | 初定 |
| meetup / office hours / happy hour | 聚会 / 答疑时间 / 下班小聚 | industry meet-up 译“行业聚会”，Organise meetups 译“自己组织聚会”，HR professionals happy hour 译“HR 从业者下班小聚” |  | ch04 | 6 | 初定 |
| mom-and-pop / SMEs / e-tailers / creative agencies | 夫妻店 / 中小企业 / 电商 / 创意代理公司 | 第 7 章作者早年面对的各种广告主；Big brands or mom & pop? 译“大品牌还是夫妻店？” |  | ch07 | 6 | 初定 |
| Inbox 0 | 收件箱清零 | 第 2 章：把收件箱处理到零封未读的习惯，第一次出现时括注 Inbox 0 |  | ch02 | 2 | 初定 |
| 7 degrees of separation | 七度分隔 | 第 6 章：作者写成 7，通行说法是“六度分隔”。照原文写七，可加译者注；小标题 7 degrees of bacon 可译“贝肯七度” |  | ch06 | 2 | 初定 |
| Gordian Knot | 戈尔迪之结 | 结语 Hack it 一节的传说 |  | conclusion | 7 | 初定 |

## 机构、产品与地名

| 英文 | 译法 | 说明 |
| --- | --- | --- |
| Habit | 照写 | 作者的第一家公司，做社交广告技术 |
| iPad / iPhone / App Store / YouTube | 照写 |  |
| Google / Google Reader / Google Docs | 谷歌 / Google Reader / Google Docs | Google Reader 第一次出现时括注“谷歌阅读器”；动词 google 见“全书统一的写法” |
| Dropbox / Excel / Skype / LinkedIn / Wordpress / Evernote | 照写 | Wordpress 照原文大小写 |
| Twitter / reddit / Hacker News / Instagram / flickr | 照写 | 不写“推特”；flickr、reddit 照原文小写 |
| Groupon / Kickstarter / Buffer | 照写 | Groupon 第一次出现时可括注“团购网站” |
| Sony / MTV / McKinsey / Amazon | 索尼 / MTV / 麦肯锡 / 亚马逊 |  |
| Paypal / EBay | PayPal / eBay | 原文写作 Paypal、EBay，用公司自己的写法 |
| Stanford / Harvard / Oxford / UN | 斯坦福大学 / 哈佛大学 / 牛津大学 / 联合国 |  |
| Toastmasters | 国际演讲会（Toastmasters） | 第一次出现时括注原名 |
| Pez dispensers | Pez 糖果盒 | 带卡通头像的糖果分装器，收藏品 |
| Braintrust | 照写 | 作者参加的创业者互助小组 |
| Post-it notes / index cards | 便利贴 / 索引卡 | 第 4 章、第 8 章 |
| 4 Steps to the E.piphany / The Startup Owner’s Manual | 《四步创业法》/《创业者手册》 | 史蒂夫·布兰克的两本书，用中译本书名；E.piphany 是双关，也是布兰克创办过的公司名 |
| Lafley/Martin’s strategy book | 雷富礼和马丁讲战略的书 | 原文没写书名，指《宝洁制胜战略》（*Playing to Win*）；正文照原文不补书名，需要时加译者注 |
| momtestbook.com / thestartuptoolkit.com / foundercentric.com / heisenbergmedia.com | 照写 | 2013 年的网址，链接地址不动 |
| London / Tokyo / UK / Costa Rica / Kiev | 伦敦 / 东京 / 英国 / 哥斯达黎加 / 基辅 |  |
| Africa / the Indian rice belt / America | 非洲 / 印度的水稻产区 / 美国 |  |
| Christmas / the Sunday paper | 圣诞节 / 周日的报纸 |  |
