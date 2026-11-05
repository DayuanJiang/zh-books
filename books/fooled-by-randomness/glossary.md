# 术语表

翻译前根据 `review/terms/` 里的统计数据裁定（来源和门槛见 [review/terms/README.md](review/terms/README.md)）。“出现次数”和“首次出现”由 `tools/term_stats.py --evidence` 按英文词形统计，不含第 7 章的脚注定义和参考文献；按正则匹配，可能把同词根的普通用法也算进去。“各章概要”一节逐字重复了各章开头的内容提要，所以不少术语的首次出现是 summaries。状态都是“初定”，由 Claude 裁定，等用户确认；改动时要回查已经译完的章节。

## 体例

- **人名**：用 [review/terms/people-zh.tsv](review/terms/people-zh.tsv) 的译名。每节第一次出现时在中文名后括注英文原名，例如“卡尔·波普尔（Karl Popper）”，之后只写中文。书中人物也一样，例如“尼禄·图利普（Nero Tulip）”。表里依据写 keep 的人照写英文：只在两版致谢里出现的作者亲友和同事，以及只在书末注释的文献引用里出现的作者。
- **书末注释的文献引用**：“作者（年份）”形式的引用照写英文，和参考文献对应，例如 See Fischhoff (1982). 写“见 Fischhoff (1982)。”；Kahneman and Tversky (1973) 照写。同一个人在注释的行文里被提到时，按上一条写中文名并括注。注释开头粗体的主题词译成中文，保留粗体，冒号放在粗体外面，例如 `**后见之明偏差**：`（写成 `**后见之明偏差：**` 时，粗体在 CommonMark 里闭合不了）。
- **参考文献**：这一节的条目照抄英文原文，只译标题“参考文献”。
- **脚注**：第 7 章的两条脚注是作者的说明，全文翻译，`[^1]`、`[^2]` 放在中文里对应词句的后面。
- **机构、地名、报刊**：见下面“机构、地名与报刊”。没有通行中文名的公司照写原名，和汉字之间加空格。
- **书名、报刊、文章**：书名和报刊用《》，每节第一次出现时括注原题，原题用斜体，例如《邻家的百万富翁》（*The Millionaire Next Door*）。文章、论文的原题保留引号，不用斜体。常见报刊不括注，见下表。本书书名 *Fooled by Randomness* 指这本书时写《随机漫步的傻瓜》，不括注；作者把它当形容词用时（“my emotions (completely *Fooled by Randomness*)”）译“被随机性愚弄”，保留斜体。
- **外文引语**：法语、拉丁语、希腊语、意第绪语等引语照写原文并保留斜体；作者自己给了英文意思的，翻译他的英文；没有给的，在后面括注中文意思，例如 *Homo sum*（我是人）。
- **数字**：见下面“全书统一的写法”。金额换算成中文的万、亿：$10 million 写“1000 万美元”，$500,000 写“50 万美元”，$1 million 写“100 万美元”。百分比照写，例如 99.9%。英制单位照原文，必要时括注公制。
- **下标**：第 6 章的 W₀、W₁、W₂ 照写；同一句里的 Wt 照原文写 Wt（原文疑点见 `review/source.md`）。
- **图表**：表和图的编号照写，标题译成中文，例如“表 P.1 混淆表”“图 6.1”。这个 EPUB 缺了图表本身，正文提到的“左栏”“右栏”照原文译。
- **交叉引用**：Chapter 11 写“第 11 章”，Part I 写“第一部分”，Chapters 8 and 9 写“第 8 章和第 9 章”。
- **各章概要**：每章的二级标题照下面“各节标题”一列写，例如 `## 第 1 章 你这么有钱，怎么不够聪明？`；概要正文和各章开头的斜体内容提要逐字相同，译文也要相同。
- **语气**：作者用第一人称，爱讽刺、爱插话，括号里的旁白很多。括号照样保留，反讽照字面译出，不加解释。口语化的地方译成口语，例如 “it ain’t over until it’s over” 译“不到最后，不算结束”。
- **强调**：原文用斜体强调的词，中文照样用斜体，例如“我*自己*思维上的缺陷”。
- **分隔线**：分隔线 `---` 只写在英文文件里。
- **破折号和句式**：中文译文不用破折号（——），原文的破折号按意思改成逗号、冒号、括号或另起一句；也不用“不是……而是……”这种句式，换成直接的说法。章节标题里的破折号改成冒号，例如第 5 章、第 10 章。

## 全书统一的写法

从《AI 帝国》（books/empire-of-ai）译完后定下的写法里，挑出适用于这本书的几条，并补上这本书自己的情况：

- **数字**：一到十，以及带“几、十几、数百、上千”的约数，用汉字（三个部分、十年后、几十名交易员）；11 以上的确数用阿拉伯数字（18 年、4000 本书、241 分钟），万和亿前面的数字也用阿拉伯数字（1 万只猴子、1000 万美元）；年份、日期、钟点、金额、百分比、概率和标准差倍数一律用阿拉伯数字（1987 年夏天、凌晨 3 点、15% 的超额收益、1/1000 的概率）。倍数写“增长到原来的 N 倍”，不写“增长了 N 倍”。“ten sigma”写“十西格玛”。
- **书名、报刊括注**：每节第一次出现时括注原题，原题用斜体；文章、论文的原题保留引号，不用斜体。《华尔街日报》《经济学人》《纽约客》《新闻周刊》《福布斯》《名利场》这些常见报刊不括注。
- **人名**：名人也照常在每节第一次出现时括注英文。书末注释的“作者（年份）”引用一律照写英文。“布什总统”这类说法不括注。
- **诺贝尔奖**：作者在第 13 章特意指出经济学奖不算诺贝尔奖。Nobel Prize 写“诺贝尔奖”，Nobel Memorial Prize in Economics 写“诺贝尔经济学纪念奖”，Bank of Sweden Prize、Swedish Central Bank Prize 写“瑞典中央银行奖”；作者顺口说 Nobel economist 时写“诺贝尔经济学奖得主”。
- **代词**：作者泛指读者或某类人时常用 he，中文按语境写“他”“这个人”，不必刻意改成“他或她”。
- **原文的笔误**：人名拼错的地方（Steven Jay Gould、Nozik、Bernouilli、Pissaro、Patrocles、Percy Diaconis、Paul Valery），中文用正确的译名，括注也写正确的拼法（Stephen Jay Gould、Robert Nozick、Persi Diaconis、Paul Valéry），原文的拼法记在 people-zh.tsv 的 note 里，正文不加译者注。第 2 章的 the George Wills around 是复数，指乔治·威尔这一类人，不算笔误。参考文献和书末注释的“作者（年份）”引用照抄原文，见“全书统一的写法（译完后定）”。

## 全书统一的写法（译完后定）

各节译完后，编辑在报告里提出了一些全书范围的问题，统一如下。写着“已改”的地方已经用脚本改进 zh-cn/；写着“待改”的要看上下文改，留给下一轮各节的编辑；写着“待用户定”的由用户决定。

- **章首提要和“各章概要”**：两处逐字相同。2026-11-05 逐字比对后，第 2、11、14 章的章首提要照“各章概要”改成“在随机性上的智慧”“新闻造成的污染”“它是一种让人觉得自己战胜了随机性的幻觉”（已改），现在 14 章全部一致。以后改其中一处，另一处要跟着改。
- **章节标题**：后记的原题是 Postscript: Three Afterthoughts in the Shower，写“后记 淋浴时的三点想法”（已改，见“各节标题”）。
- **人名括注**：
  - 括注照本节第一次出现时英文的写法。章首提要里只写了姓的人（Soros、Popper、Montherlant），括注也只写姓，正文后面出现全名时不再括注，第 7、11、13、14 章都这样处理。
  - 作者自己的说法里带着人名，而这个人恰好在本节第一次出现时，英文括注放在整个说法后面，说法本身保持完整，例如梭伦的警告（Solon’s warning）、维特根斯坦的尺子（Wittgenstein’s ruler）、布里丹之驴（Buridan’s donkey）。第 1 章第 48 块原来写“梭伦（Solon）的警告”（已改）。哥德尔定理、图灵测试这类通行的科学术语不括注。
  - 第 7 章脚注里的人名和正文一样，写中文名并括注英文，例如塞克斯都·恩披里柯（Sextus Empiricus）。
  - 括注落在外层括号的结尾时，照写“））”，例如第 10 章“（罪魁祸首：……保罗·萨缪尔森（Paul Samuelson））”。第 3、10、11 章各有一处，保持原样。
  - 作者的名字 Nassim 出现在别人的话里时（序言、第 6 章），写“纳西姆（Nassim）”。
  - 第 14 章 the stern Cato 照原文写“加图（Cato）”，可能指小加图，说明写在 people-zh.tsv 里。
- **参考文献和文献引用**：参考文献条目和书末注释的“作者（年份）”引用照抄原文，原文的笔误也照抄，包括 Brocas and Carillo（应为 Carrillo）、Schleifer（应为 Shleifer）、Taszka（应为 Tyszka）、Nozik (1993)、Kahneman, Knetsch and Thaler (1986) 的题目，以及 Keynes 两条的年份和页码。核对结果记在 review/references.md 的原文疑点表里，中文版不加说明。条目里的 “———”“—”“–” 属于英文书目的格式，照抄；中文不用破折号这一条管的是译文的句子。
- **粗体、斜体旁边的标点**：粗体或斜体以中文标点结尾、后面紧跟汉字时，CommonMark 闭合不了，标点放在标记外面，例如 `**享乐跑步机**：`。全书已经用 markdown-it 渲染检查过，页面上没有残留的星号。
- **文章的题目**：中文题目用《》，括注里的原题用引号，原文把文章题目排成斜体时也一样。书末注释里芒福德的《随机性时代的黎明》在参考文献里是一篇文章，括注写（“The Dawning of the Age of Stochasticity”）（已改）。
- **外文词**：英文里常用的拉丁语词（per se、a priori、ad hoc、vice versa）直接译成中文，用正体（第 2 章第 20 块的“*本身*”、第 13 章第 12 块的“*真正意义上*”要去掉斜体，第 13 章第 33 块的“*ad hoc*（临时拼凑的）”要改成中文，待改）；作者当作外文引用的词（*bête noire*、*péché mignon*、*schadenfreude*）照写原文，保留斜体，并括注中文意思。
- **译者注**：写成 `[^tN]`，以“译者注：”开头。下面三种情况加译者注：原文和上下文矛盾，中英对照时读者会看到两边意思相反（第 1、9 章，第 11 章两条，后记两条）；双关或套用的名言译不出来（第 6 章、尾声）；中文读者缺少看懂这句话的背景（第 8 章的 SAT，第 12 章的地中海，书末注释的潘格罗斯）。人名拼错和书目笔误不加。第 14 章坦佩尔斯曼在葬礼上读的诗和原文说的不一致，第 2 章第 38 块的“右栏、左栏”指的表 P.1 在这个 EPUB 里缺失，这两处暂时不加。现有的 11 条译者注留不留，请用户逐条确认（待用户定）。
- **固定说法**：
  - take knowledge / science / information / things seriously（把它们看得太重、太相信）写“当真”，例如“别太把知识当真”“为什么把科学当真并不科学”“我们把信息当真的倾向”；take someone seriously，或者结果、模型 can be taken seriously（值得重视）写“认真看待”“认真对待”。第 11 章第 74 块的 takes his science too seriously 现在写“把自己的科学看得太认真”，要改用“当真”（待改）。
  - the X in me / in us 写“我身上那个……”“我们身上那个……”，例如“我身上那个唯美主义者”；说的是一种习气时可以写“那股”，例如第 10 章“我身上那股知识分子的势利劲儿”。
  - brother-in-law 写“姐夫”。原文没说是哪一种姻亲，中文又没有统称，全书选这一种（序言、第 2 章、第 9 章；第 2 章原来的“小舅子”已改）。
  - evolution、evolve 写“进化”（第 3 章、第 11 章原来的两处“演化”已改）。
  - market call 写“行情判断”（第 2 章原来的“市场判断”已改）。
  - bottom line（商务套话）写“最终结果”；“底线”留给第 5 章的 lines in the sand。
  - my grandfather：第 3 章第 44 块指作者的外祖父（当过黎巴嫩副总理），写“外祖父”；第 8 章第 24 块买黎巴嫩镑国库券的那位，原文看不出是哪一边，写“祖父”。两处请用户一起确认（待用户定）。
- **数字**：编辑没有报告数字写法不一致的地方。抽查全书，一到十写成阿拉伯数字的地方都是概率、频率、钟点和统计量，符合上面的数字规定。第 5 章“每 1,000,000,000,000,000,000,000,000 年发生 1 次”照原文写出一长串零，保留作者的夸张。
- **只出现一两次、没有收进表里的说法**：fat tails 写“肥尾”，adding to the winner 写“给赢家加仓”，backfit 按上下文写“倒推出来的”（以上见序言）；salespeople 写“销售人员”，crisis hunters 写“危机猎人”，financial engineering 写“金融工程”（第 6 章）；social security money 写“社保基金”（第 8 章）；hypothesis testing 写“假设检验”（第 12 章）；at large discounts 写“大幅折价”或“以极低的价格”（尾声）。

## 各节标题

| 章节 id | 英文 | 中文标题（`#` 一级标题照这一列写） |
| --- | --- | --- |
| preface | Preface: Taking Knowledge Less Seriously | 序言 别太把知识当真 |
| summaries | Chapter Summaries | 各章概要 |
| prologue | Prologue: Mosques in the Clouds | 序章 云中的清真寺 |
| part1 | Part I: Solon’s Warning | 第一部分 梭伦的警告 |
| ch01 | 1. If You’re So Rich, Why Aren’t You So Smart? | 第 1 章 你这么有钱，怎么不够聪明？ |
| ch02 | 2. A Bizarre Accounting Method | 第 2 章 一种古怪的记账方法 |
| ch03 | 3. A Mathematical Meditation on History | 第 3 章 用数学沉思历史 |
| ch04 | 4. Randomness, Nonsense, and the Scientific Intellectual | 第 4 章 随机性、胡话与科学知识分子 |
| ch05 | 5. Survival of the Least Fit—Can Evolution Be Fooled by Randomness? | 第 5 章 最不适者生存：进化会被随机性愚弄吗？ |
| ch06 | 6. Skewness and Asymmetry | 第 6 章 偏态与不对称 |
| ch07 | 7. The Problem of Induction | 第 7 章 归纳问题 |
| part2 | Part II: Monkeys on Typewriters | 第二部分 打字机前的猴子 |
| ch08 | 8. Too Many Millionaires Next Door | 第 8 章 邻家的百万富翁太多了 |
| ch09 | 9. It Is Easier to Buy and Sell Than Fry an Egg | 第 9 章 买卖比煎蛋还容易 |
| ch10 | 10. Loser Takes All—On the Nonlinearities of Life | 第 10 章 输家通吃：论生活的非线性 |
| ch11 | 11. Randomness and Our Mind: We Are Probability Blind | 第 11 章 随机性与我们的头脑：我们是概率盲 |
| part3 | Part III: Wax in My Ears | 第三部分 我耳朵里的蜡 |
| ch12 | 12. Gamblers’ Ticks and Pigeons in a Box | 第 12 章 赌徒的怪癖与箱中的鸽子 |
| ch13 | 13. Carneades Comes to Rome: On Probability and Skepticism | 第 13 章 卡尔内阿德斯来到罗马：论概率与怀疑论 |
| ch14 | 14. Bacchus Abandons Antony | 第 14 章 酒神离弃安东尼 |
| epilogue | Epilogue: Solon Told You So | 尾声 梭伦早就说过 |
| postscript | Postscript: Three Afterthoughts in the Shower | 后记 淋浴时的三点想法 |
| dedication | Dedication | 献辞 |
| acknowledgments-first | Acknowledgments for the First Edition | 第一版致谢 |
| acknowledgments-second | Acknowledgments for the Updated Second Edition | 修订第二版致谢 |
| notes | A Trip to the Library: Notes and Reading Recommendations | 去图书馆走走：注释与阅读推荐 |
| references | References | 参考文献 |
| about-the-author | About the Author | 关于作者 |

- 中信出版社的中译本《随机漫步的傻瓜》（2012）给各章另起了标题（例如第 1 章“赚钱的随机性”、第 5 章“最不适者可能生存吗？”、第 12 章“赌徒的迷信和笼中的鸽子”），只作参考。这里按原题直译，保留作者的反语和典故：第 1 章反用美国俗语 “If you’re so smart, why aren’t you rich?”（你这么聪明，怎么没发财？）；第 14 章出自卡瓦菲斯的诗 “The God Abandons Antony”，原诗只说“神”，按普鲁塔克的记载是酒神，作者直接写成 Bacchus。
- 三个部分的副标题在原文里是标题下面的斜体段落：Skewness, Asymmetry, Induction 写“偏态、不对称、归纳”；Survivorship and Other Biases 写“幸存者偏差及其他偏差”；Living with Randomitis 写“与随机病共处”。
- 译者读完一章后，如果觉得标题另有更贴切的译法，在汇报里提出，由主会话统一修改。

## 核心概念

| 英文 | 首选译法 | 适用的意思 | 不要混同 | 首次出现 | 出现次数 | 状态 |
| --- | --- | --- | --- | --- | --- | --- |
| randomness / random | 随机性 / 随机的 | 全书主题：结果里不由能力和因果决定的成分 | 偶然（chance）、运气（luck） | preface | 289 | 初定 |
| luck / lucky | 运气 / 走运的、幸运的 | 落在某个人身上的随机结果，书里和 skill 相对；by luck 写“靠运气” | 机遇（chance） | preface | 91 | 初定 |
| chance | 偶然 / 机遇 | 不受人控制的因素；chance alone 写“纯属偶然” | 运气（luck） | preface | 27 | 初定 |
| skill / skills / nonluck | 能力 / 非运气 | 和运气相对、真正靠本事得来的部分；nonluck 是作者的说法，序章括注“that is, skills” | 技巧（具体技艺按搭配写棋艺、技能） | preface | 43 | 初定 |
| determinism / deterministic | 决定论 / 确定性的 | 认为结果完全由原因决定；序章说随机性被误认成“非随机性，也就是决定论” | 宿命论 | preface | 10 | 初定 |
| lucky fool | 幸运的傻瓜 | 作者的定义：分到不成比例的好运，却把成功归于别的、往往很具体的原因的人 | 傻子、白痴 | preface | 6 | 初定 |
| fool of randomness / randomness fool | 被随机性愚弄的人 | 被随机性骗了而不自知的人；the fool of all fools 写“傻瓜中的傻瓜” |  | preface | 13 | 初定 |
| fooled by randomness | 被随机性愚弄 | 作为短语时的译法；指本书时写书名《随机漫步的傻瓜》 |  | preface | 28 | 初定 |
| Table of Confusion / Table P.1 | 混淆表 / 表 P.1 | 序章的表：左栏是运气、随机性、噪声一类，右栏是能力、决定论、信号一类，全书讲的就是把左栏误认作右栏；EPUB 缺了表的内容 |  | prologue | 7 | 初定 |
| noise | 噪声 | 随机的波动，和有意义的信息相对；noise and meaning 写“噪声与意义” | 噪音（日常意义的嘈杂声） | prologue | 48 | 初定 |
| signal | 信号 | 噪声之外真正有用的成分 |  | ch01 | 11 | 初定 |
| black swan / black swan problem | 黑天鹅 / 黑天鹅问题 | 作者对稀有事件和归纳问题的叫法：观察到再多的白天鹅，一只黑天鹅就能推翻“天鹅都是白的” | 后来《黑天鹅》一书里更严格的定义 | preface | 18 | 初定 |
| rare event / rare-event fallacy | 稀有事件 / 稀有事件谬误 | 发生概率很低、后果很大的事件 | 小概率事件（可用作解释） | preface | 52 | 初定 |
| Solon’s warning | 梭伦的警告 | 梭伦对克罗伊斯说，人没到生命终点，不能说他幸福；作者的人生座右铭 |  | summaries | 8 | 初定 |
| skewness / skewed | 偏态 / 偏斜的 | 作者的概念：成功的频率并不重要，失败的代价太大时就不能承受；讲统计量时可写“偏度” | 不对称（asymmetry） | summaries | 18 | 初定 |
| asymmetry / asymmetric | 不对称 / 不对称的 | 赔率或输赢的幅度两边不对称 |  | summaries | 19 | 初定 |
| alternative histories / alternative history | 或然历史 | 作者的概念：事情本来可能走的其他路；评价一个结果时要把这些路一起算进去 | 另类历史（中信版的译法）、架空历史 | summaries | 12 | 初定 |
| visible history / invisible histories | 看得见的历史 / 看不见的历史 | 实际发生的那一种历史和没有发生的或然历史 |  | prologue | 4 | 初定 |
| resistance to randomness / resistant to randomness | 对随机性的抵抗力 / 经得起随机性 | 第一部分的主题：靠运气得来的东西也会被运气拿走，很少靠运气得来的东西更经得起随机性；第 1 章拿牙医和中了彩票的清洁工对比 |  | part1 | 5 | 初定 |
| possible worlds | 可能世界 | 哲学概念（莱布尼茨、克里普克）；possible worlds semantics 写“可能世界语义学” |  | ch02 | 6 | 初定 |
| Russian roulette | 俄罗斯轮盘赌 | 作者用来说明或然历史的思想实验 |  | preface | 15 | 初定 |
| Monte Carlo | 蒙特卡罗 | 用计算机随机生成大量样本路径的方法：Monte Carlo simulation / engine / generator / simulator 写“蒙特卡罗模拟 / 引擎 / 生成器 / 模拟器”；地名也写“蒙特卡罗”，保留作者把赌场和数学方法连起来的说法 | 蒙特卡洛 | summaries | 48 | 初定 |
| generator | 生成器 | 产生随机结果的机制；“the generator of the problem”这类说法按上下文写“根源” | 发电机 | summaries | 22 | 初定 |
| sample path / random run | 样本路径 / 随机轨迹 | 随机过程的一次实现，也就是一段可能的历史；alternative sample paths 写“其他的样本路径” | 样本 | ch01 | 21 | 初定 |
| survivorship bias / survivors | 幸存者偏差 / 幸存者 | 只看到留下来的赢家，对成功概率的判断因此偏高；double survivorship biases 写“双重幸存者偏差” | 存活者偏差（中信版的译法） | summaries | 36 | 初定 |
| monkeys on typewriters / monkey | 打字机前的猴子 / 猴子 | 第二部分的比喻：猴子够多，总有一只打出《伊利亚特》；第 1 章已经提到猴子 |  | ch01 | 21 | 初定 |
| track record / past performance | 过往业绩 / 过去的表现 | 用来判断能力的历史成绩 |  | preface | 29 | 初定 |
| hindsight bias | 后见之明偏差 | 事后看过去的事件，觉得它没那么随机；书末注释的 Monday morning quarterback 写“事后诸葛亮” |  | preface | 9 | 初定 |
| heuristics and biases / heuristic | 启发式与偏差 / 启发式 | 卡尼曼和特沃斯基的研究传统；quick and dirty heuristics 写“粗糙快捷的启发式”；和《思考，快与慢》一致 | 启发法 | prologue | 31 | 初定 |
| affect heuristic / availability heuristic / anchoring | 情感启发式 / 可得性启发式 / 锚定 | 同《思考，快与慢》 | 易得性 | ch03 | 12 | 初定 |
| bounded rationality / satisficing | 有限理性 / 满意即止 | 赫伯特·西蒙的概念：人只求“够好”，不求最优 | 满足 | prologue | 8 | 初定 |
| System 1 / System 2 | 系统 1 / 系统 2 | 同《思考，快与慢》 | 系统一 | ch11 | 8 | 初定 |
| probability / probabilistic / probability blind | 概率 / 概率的 / 概率盲 | 第 11 章标题的 probability blind 写“概率盲”；probability theory 写“概率论” | 可能性（likelihood、possibility） | preface | 264 | 初定 |
| expectation / expected value | 期望 / 期望值 | 各种结果的概率乘以收益再相加；mathematical expectation 写“数学期望”，in expectation 写“按期望算”；rational expectations 写“理性预期”；日常意义的 expectation 按上下文写“预期”“可能性”，例如第 9 章 The expectation of having a fraud 写“碰上……骗子，这种可能性” | 期待、预期（日常意义） | ch01 | 24 | 初定 |
| mean / median | 均值 / 中位数 | 第 6 章借古尔德的文章讲两者的差别；mean 也叫 average、expectation |  | ch06 | 15 | 初定 |
| variance | 方差 | 结果分散的程度；作者常拿它指运气造成的那部分结果，第 1 章的 Wild success is attributable to variance 写“大获成功，就要归因于方差了” | 波动率（volatility） | ch01 | 7 | 初定 |
| conditional probability / conditional information | 条件概率 / 条件信息 | 第三部分：信息的价值取决于来源的可靠性；unconditional 写“无条件的” |  | ch03 | 21 | 初定 |
| prior | 先验 | 维特根斯坦的尺子里，对尺子可靠性的事先估计 |  | ch02 | 3 | 初定 |
| Wittgenstein’s ruler | 维特根斯坦的尺子 | 不信任尺子时，用尺子量桌子也是在用桌子量尺子；书评更多反映的是书评人 |  | part3 | 3 | 初定 |
| regression to the mean | 均值回归 | 同《思考，快与慢》 | 回归分析 | ch09 | 4 | 初定 |
| ergodicity | 遍历性 | 时间足够长时，运气的作用被抵消，能力才显现出来 |  | ch03 | 6 | 初定 |
| birthday paradox | 生日悖论 |  |  | summaries | 4 | 初定 |
| data mining / data snooping | 数据挖掘 / 数据窥探 | 在历史数据里大量尝试，总能“找到”规律 |  | ch09 | 10 | 初定 |
| backtester / backtesting | 回测工具 / 回测 | 用历史数据检验交易规则 |  | ch09 | 3 | 初定 |
| nonlinearity / nonlinear | 非线性 / 非线性的 |  |  | summaries | 24 | 初定 |
| path dependence / path dependent | 路径依赖 / 依赖路径的 | 结果取决于先发生了什么；path dependence of beliefs 写“信念的路径依赖” |  | ch10 | 7 | 初定 |
| sandpile effect / critical point | 沙堆效应 / 临界点 | 第 10 章：多加一粒沙，整个沙堆就塌 |  | ch10 | 8 | 初定 |
| power law | 幂律 | Pareto power laws 写“帕累托幂律” |  | ch10 | 4 | 初定 |
| Polya process | 波利亚过程 |  |  | ch10 | 3 | 初定 |
| network externalities / informational cascades | 网络外部性 / 信息瀑布 |  |  | ch10 | 3 | 初定 |
| winner-take-all / loser takes all | 赢家通吃 / 输家通吃 | 第 10 章标题反用“赢家通吃” |  | summaries | 4 | 初定 |
| Buridan’s donkey | 布里丹之驴 |  |  | ch10 | 8 | 初定 |
| problem of induction / induction / inductive | 归纳问题 / 归纳 / 归纳的 |  | 诱导、感应 | preface | 30 | 初定 |
| deduction / deductive | 演绎 / 演绎的 |  |  | summaries | 8 | 初定 |
| falsification / falsifiable / falsificationism | 证伪 / 可证伪的 / 证伪主义 | 波普尔的思想；naive falsificationist 写“朴素的证伪主义者” |  | prologue | 10 | 初定 |
| empiricism / empiricist | 经验主义 / 经验主义者 | 作者自称 skeptical empiricist，写“怀疑论的经验主义者”；naive empiricism 写“朴素经验主义”，指从有限的观察草率概括；第 7 章脚注里作者给 empiricism 加了引号，按他的意思译 | 实证主义（positivism） | preface | 29 | 初定 |
| skepticism / skeptic | 怀疑论 / 怀疑论者 | 古代的怀疑论派和作者的立场；日常的“怀疑”按上下文 |  | preface | 34 | 初定 |
| epistemology / epistemologist | 认识论 / 认识论学者 |  |  | ch03 | 8 | 初定 |
| epistemic opacity | 认知不透明 | 第 6 章：我们看不到产生结果的机制 |  | summaries | 2 | 初定 |
| problem of demarcation | 划界问题 | 科学和非科学的分界 |  | ch07 | 2 | 初定 |
| positivism / logical positivists / Vienna Circle | 实证主义 / 逻辑实证主义者 / 维也纳学派 |  |  | ch04 | 9 | 初定 |
| fallibilism / fallibility | 可错论 / 可错性 | 皮尔士提出的概念 | 可谬论 | prologue | 3 | 初定 |
| open society | 开放社会 | 波普尔的概念 |  | ch07 | 5 | 初定 |
| Pascal’s wager | 帕斯卡的赌注 |  |  | summaries | 2 | 初定 |
| epiphenomena / epiphenomenalism | 副现象 / 副现象论 | 第 2 章：误把同时出现的事当作因果，例如“罗盘推动了船” | 附带现象 | ch02 | 3 | 初定 |
| round-trip fallacy | 往返谬误 | 作者的说法：没有逻辑的统计是错的，没有统计的逻辑却不算错 |  | preface | 1 | 初定 |
| denigration of history / historical determinism | 轻视历史 / 历史决定论 |  |  | ch02 | 4 | 初定 |
| stationarity / Lucas critique / peso problem | 平稳性 / 卢卡斯批判 / 比索问题 | 第 6 章；problem of stationarity 写“平稳性问题” |  | ch06 | 7 | 初定 |
| scientism | 唯科学主义 | 贬义，作者自认是它的批评者 | 科学精神 | ch06 | 2 | 初定 |
| science wars | 科学大战 | 第 4 章：科学知识分子和文学知识分子之争 |  | summaries | 3 | 初定 |
| scientific intellectual / literary intellectual | 科学知识分子 / 文学知识分子 |  |  | summaries | 14 | 初定 |
| pseudoscience / charlatan | 伪科学 / 江湖骗子 | pseudothinker 写“伪思想家”，charlatanism 写“骗术” |  | summaries | 19 | 初定 |
| Utopian Vision / Tragic Vision | 乌托邦愿景 / 悲剧愿景 | 序章：索维尔提出、平克推广的两种人性观 |  | prologue | 4 | 初定 |
| reverse Turing test / exquisite cadaver / Dada Engine | 反向图灵测试 / 精致的尸体 / 达达引擎 | 第 4 章：用随机生成的文字冒充思想；exquisite cadaver 是超现实主义的集体写作游戏 |  | ch04 | 7 | 初定 |
| Darwinism / naive Darwinism | 达尔文主义 / 朴素达尔文主义 | 作者批评在生物学以外滥用“适者生存” | 进化论 | summaries | 7 | 初定 |
| survival of the least fit | 最不适者生存 | 第 5 章标题，反用“适者生存” |  | summaries | 2 | 初定 |
| evolutionary psychology | 进化心理学 | evolution、evolve 全书都写“进化” | 演化心理学（统一写进化） | ch01 | 8 | 初定 |
| stoicism / stoic | 斯多葛主义 / 斯多葛派的 | 第 14 章：作者把它理解为人在随机性面前保持风度 | 禁欲主义 | preface | 18 | 初定 |
| personal elegance / dignity | 个人风度 / 尊严 |  |  | summaries | 16 | 初定 |
| gamblers’ ticks | 赌徒的怪癖 | ticks 指 tics，交易员不自觉养成的小迷信 | 蜱虫 | summaries | 6 | 初定 |
| superstition | 迷信 |  |  | prologue | 12 | 初定 |
| taxi-cab English | 出租车英语 | 第 12 章：作者把赚钱和出租车司机的蹩脚英语联系起来的迷信 |  | summaries | 4 | 初定 |
| Skinner pigeon experiment | 斯金纳的鸽子实验 |  |  | summaries | 6 | 初定 |
| wax in my ears | 耳朵里的蜡 | 第三部分标题：奥德修斯让水手用蜡封住耳朵，作者用来比喻对付自己弱点的小办法 |  | prologue | 5 | 初定 |
| Randomitis | 随机病 | 第三部分副标题里的造词 |  | part3 | 1 | 初定 |
| pecking order | 地位排序 | 社会上的高低次序，原是动物学的“啄序” |  | summaries | 13 | 初定 |
| schadenfreude | 幸灾乐祸 | 德文词，第 1 章作者自己解释了意思；每节第一次出现时括注原词，写“幸灾乐祸（Schadenfreude）”，尾声原文是斜体，括注也用斜体 |  | ch01 | 2 | 初定 |
| work ethics | 敬业精神 | 作者常反讽地用，例如数据挖掘的研究者 |  | preface | 11 | 初定 |
| middlebrow | 半吊子 | 有点知识但不深的人；beware the middlebrow 写“当心半吊子” | 中产阶级 | ch03 | 4 | 初定 |
| empty suit | 空架子 | 后记：只会装样子的人 |  | postscript | 2 | 初定 |
| inverse rule / corporate political skill | 反向法则 / 公司政治手腕 | 后记：职位越高，越难证明本人对业绩的贡献 |  | postscript | 2 | 初定 |
| trader / trading | 交易员 / 交易 |  | 商人 | preface | 255 | 初定 |
| proprietary trading | 自营交易 | 用公司自有资金交易 |  | ch01 | 2 | 初定 |
| head trader / pit trader | 交易主管 / 场内交易员 | 交易所的行话：pits 写“交易池”；第 1 章的斜体 *local* 写“*场内自营商*（local）”，指在交易池里用自己的钱做交易的人 | 首席交易员 | ch01 | 4 | 初定 |
| market maker | 做市商 |  |  | ch09 | 2 | 初定 |
| blow up | 爆仓 | 作者的定义：亏得比预想的多得多，以至于被赶出这一行 | 爆炸 | ch01 | 32 | 初定 |
| stop loss | 止损 |  |  | ch05 | 3 | 初定 |
| option / option seller / premium seller | 期权 / 期权卖方 / 期权费卖方 | option buyer 写“期权买方”，call option 写“看涨期权”，out-of-the-money 写“价外”，in the money 写“价内” | 选择 | ch01 | 53 | 初定 |
| naked option | 裸期权 | 卖出期权而不做对冲，可能的亏损很大；第 1 章原文带引号，中文也加引号 |  | ch01 | 2 | 初定 |
| volatility / long volatility | 波动率 / 做多波动率 | 讲起伏的大小或把它当作指标时写“波动率”（第 9 章“这个数目也取决于波动率”）；讲收益上下起伏这个现象时写“波动”（第 6 章“牙医不喜欢波动”） |  | ch02 | 18 | 初定 |
| high-yield / emerging markets | 高收益 / 新兴市场 | high-yield trader 写“高收益债券交易员”；Brady bonds 写“布雷迪债券” |  | ch01 | 29 | 初定 |
| Treasury bond / junk bond | 国债 / 垃圾债券 | 尼禄只把储蓄投在美国国债上；junk bonds 是高收益债券的俗称；Treasury bills 写“国库券” |  | ch01 | 8 | 初定 |
| averaging down / lines in the sand | 摊低成本 / 底线 | 第 5 章：亏损时加仓；大家以为价格跌不破的那几道线 | 最终结果（商务套话 bottom line） | ch05 | 3 | 初定 |
| quant | 宽客 | 做数量分析的人，每节第一次出现时括注原文 |  | ch03 | 6 | 初定 |
| hedge fund / leverage / shorting | 对冲基金 / 杠杆 / 做空 |  |  | ch03 | 18 | 初定 |
| bull / bear / bullish / bearish | 牛市、多头 / 熊市、空头 / 看涨 / 看跌 | 第 6 章说这两个词离开动物学意义有限，按上下文选词 |  | summaries | 51 | 初定 |
| ten sigma | 十西格玛 | 偏离均值十个标准差，被当作“不可能”的事件 |  | ch05 | 5 | 初定 |
| statistical significance / confidence level | 统计显著性 / 置信水平 |  |  | ch06 | 11 | 初定 |
| bell curve / standard deviation | 钟形曲线 / 标准差 |  |  | ch03 | 6 | 初定 |
| time series / econometrics | 时间序列 / 计量经济学 |  |  | preface | 26 | 初定 |
| sampling theory / sample size / law of large numbers | 抽样理论 / 样本量 / 大数定律 |  |  | summaries | 10 | 初定 |
| type I and type II errors | 第一类错误和第二类错误 |  |  | ch12 | 1 | 初定 |
| behavioral finance / behavioral economics | 行为金融学 / 行为经济学 |  |  | ch03 | 4 | 初定 |
| neoclassical economics / efficient markets / homo economicus | 新古典经济学 / 有效市场 / 经济人 |  |  | ch02 | 11 | 初定 |
| endowment effect / attribution bias / overconfidence | 禀赋效应 / 归因偏差 / 过度自信 |  |  | prologue | 7 | 初定 |
| flow | 心流 | 心理学意义，契克森米哈赖的概念；其他意义按上下文 | 流量 | ch01 | 8 | 初定 |
| emotional brain / limbic system / neocortex | 情绪脑 / 边缘系统 / 新皮质 | 第 11 章 |  | ch11 | 10 | 初定 |
| state space / scenario analysis | 状态空间 / 情景分析 | 第 2 章 |  | ch02 | 3 | 初定 |
| summing under histories | 对历史求和 | 作者借用费曼的说法 |  | ch03 | 1 | 初定 |
| cross-sectional problem / temporal aggregation | 横截面问题 / 时间加总 | 第 5 章 |  | ch05 | 2 | 初定 |
| firehouse effect | 消防站效应 | 马蒂·奥康奈尔的说法：一群人整天待在一起，想法越来越像 |  | ch05 | 2 | 初定 |
| spontaneous remission / cancer clusters | 自发缓解 / 癌症聚集 | 第 9 章 |  | ch09 | 2 | 初定 |
| funds of funds | 基金中的基金 |  |  | ch09 | 1 | 初定 |
| Zorglubs | 佐格鲁布 | 作者在蒙特卡罗模拟里虚构的快速变异动物 |  | ch03 | 3 | 初定 |
| risk taking / risk taker / risk manager | 冒险 / 冒险者 / 风险经理 | risk management 写“风险管理”，risk aversion 写“风险厌恶” |  | preface | 29 | 初定 |
| Masters of the Universe | “宇宙主宰” | 人们对华尔街交易员的称呼，保留引号 |  | ch01 | 2 | 初定 |
| nonsense | 胡话 | 第 4 章标题；Fashionable Nonsense 是书名《时髦的空话》 |  | preface | 19 | 初定 |
| practitioner | 实干者 | 作者自称 practitioner of randomness / uncertainty，写“和随机性打交道的实干者” | 从业者（只指职业时用） | preface | 7 | 初定 |
| market call | 行情判断 | 交易员对市场走势的判断；第 6 章作者不肯发表的就是这种判断 |  | ch02 | 3 | 初定 |
| outlier | 离群值 | 统计意义上远离其余观察值的数据 |  | ch06 | 2 | 初定 |
| derivative / derivatives | 衍生品 | 作者的本行，derivatives trader 写“衍生品交易员”；第 1 章 derivative securities 写“衍生证券” |  | ch01 | 8 | 初定 |
| probabilist | 概率学家 | 研究概率的学者 |  | ch03 | 5 | 初定 |
| fitness / reproductive fitness | 适应度 / 繁殖适应度 | 进化论意义：第 5 章说达尔文讲的是繁殖适应度，光活下来不算数 | 健身、健康 | ch03 | 8 | 初定 |
| regime switch / regime switching | 状态切换 | 第 5 章：一个系统的所有属性都变了，变到观察者认不出来；第 3 章写“市场状态切换” |  | ch03 | 3 | 初定 |
| desk / trading desk | 交易台 | 银行里的交易部门，也指交易员的座位；普通的桌子写“办公桌”“书桌” |  | summaries | 14 | 初定 |
| dip buyers / buy dips | 逢低买进的人 / 逢低买进 | 第 5 章：价格一出现短暂的恐慌就加仓 |  | ch05 | 1 | 初定 |
| business sense | 生意头脑 | 第 5 章约翰的口头禅“他的脑子，加上我的生意头脑” |  | ch05 | 2 | 初定 |
| potential mate / eligibility | 潜在配偶 / 抢手的择偶对象 | 第 5 章讲进化和择偶时的说法 |  | ch05 | 3 | 初定 |
| burnout / trader’s burnout | 倦怠 / 交易员倦怠 | 第 3 章 | 心力交瘁（emotionally drained） | ch03 | 1 | 初定 |
| accumulators | 积累者 | 第 8 章：愿意推迟消费来攒钱的人 |  | ch08 | 3 | 初定 |
| treadmill effect / hedonic treadmill | 跑步机效应 / 享乐跑步机 | 人习惯了财富，满足感又回落到原来的水平；social treadmill effect 写“社会跑步机效应”，psychological treadmill effect 写“心理上的跑步机效应”，后记的 internal treadmill effects 写“内心的跑步机效应” |  | ch08 | 4 | 初定 |
| domain-specific / domain-general / domain specificity | 领域特定的 / 领域通用的 / 领域特定性 | 第 11 章和书末注释：大脑用不同的模块处理不同领域的问题 |  | ch11 | 7 | 初定 |
| cheater / cheater detection module | 欺骗者 / 识别欺骗者的模块 | 进化心理学的说法，第 11 章和书末注释 | 江湖骗子（charlatan） | ch11 | 4 | 初定 |
| fast and frugal / ecological rationality | 快速节俭 / 生态理性 | 吉仁泽的概念，第 11 章 | 粗糙快捷（quick and dirty） | ch11 | 3 | 初定 |
| representativeness heuristic / simulation heuristic / Linda problem | 代表性启发式 / 模拟启发式 / 琳达问题 | 第 11 章；琳达问题归在代表性启发式下面 |  | ch11 | 4 | 初定 |
| Charybdis / Scylla / sirens | 卡律布狄斯 / 斯库拉 / 塞壬 | 《奥德赛》里的漩涡怪、海怪和女妖，第三部分和第 11 章；第 11 章原文用法文拼法 Carybde，括注写 Charybdis |  | ch11 | 7 | 初定 |

## 机构、地名与报刊

| 英文 | 译法 | 说明 |
| --- | --- | --- |
| Wall Street / Wall Streeters | 华尔街 / 华尔街的人 |  |
| New York University / Courant Institute of Mathematical Sciences | 纽约大学 / 库朗数学科学研究所 | 作者任教的地方，简称 Courant 写“库朗研究所” |
| Wharton School / Harvard / University of Chicago / Yale Law School | 沃顿商学院 / 哈佛 / 芝加哥大学 / 耶鲁法学院 |  |
| Bocconi / Monash University / Carnegie-Mellon University | 博科尼大学 / 莫纳什大学 / 卡内基梅隆大学 |  |
| Chicago Mercantile Exchange / Chicago Board of Trade / New York Stock Exchange | 芝加哥商品交易所 / 芝加哥期货交易所 / 纽约证券交易所 |  |
| Federal Reserve Board / SEC / FASB / International Monetary Fund | 美联储 / 美国证券交易委员会 / 美国财务会计准则委员会 / 国际货币基金组织 |  |
| Santa Fe Institute / ABC Group (Adaptive Behavior and Cognition) | 圣塔菲研究所 / ABC 研究组（适应性行为与认知） |  |
| Long Term Capital Management (LTCM) | 长期资本管理公司（LTCM） | 之后写 LTCM |
| Salomon Brothers / Credit Suisse First Boston | 所罗门兄弟公司 / 瑞士信贷第一波士顿 |  |
| Empirica / Paloma Partners / Odeon / Regine’s | 照写原名 | 作者的公司、合作的基金、Tribeca 的餐厅、纽约的夜总会；Odeon Circle 写“Odeon 小圈子” |
| J. Wiley & Sons / Random House / Texere | 约翰·威利父子出版公司 / 兰登书屋 / Texere |  |
| Microsoft / Google / Amazon.com / Starbucks / Cisco | 微软 / 谷歌 / 亚马逊 / 星巴克 / 思科 |  |
| Bloomberg (machine) / Omega TradeStation / PalmPilot / PowerPoint | 彭博终端 / Omega TradeStation / PalmPilot / PowerPoint |  |
| CNBC / CNN / BBC / NPR / PBS / WNYC | 照写原名 |  |
| Barnes and Noble / Borders Books | 巴诺书店 / 博德斯书店 | 第 11 章 a Borders Books chain bookstore 写“一家博德斯连锁书店” |
| Memorial Sloan-Kettering Cancer Center | 纪念斯隆-凯特琳癌症中心 |  |
| Victoria and Albert Museum / Musée d’Orsay / Carnegie Hall / Metropolitan Opera | 维多利亚与艾伯特博物馆 / 奥赛博物馆 / 卡内基音乐厅 / 大都会歌剧院 |  |
| Academy / New Academy / Roman Senate | 学园 / 新学园 / 罗马元老院 | 第 13 章 |
| Nobel Prize / Fields medal | 诺贝尔奖 / 菲尔兹奖 | 经济学奖的写法见“全书统一的写法” |
| New York / Manhattan / Park Avenue / Fifth Avenue / Upper East Side / Midtown / Tribeca / SoHo | 纽约 / 曼哈顿 / 公园大道 / 第五大道 / 上东区 / 中城 / 翠贝卡 / 苏荷 | 街道写“第十八街”“第五十二街” |
| New Jersey / Greenwich, Connecticut / the Hamptons / Long Island | 新泽西 / 康涅狄格州格林尼治 / 汉普顿斯 / 长岛 |  |
| London / Kensington / Battersea Park / Cotswolds / Cambridgeshire | 伦敦 / 肯辛顿 / 巴特西公园 / 科茨沃尔德 / 剑桥郡 |  |
| Las Vegas / Bel Air / Lourdes / Ulan Bator / Seychelles Islands | 拉斯维加斯 / 贝莱尔 / 卢尔德 / 乌兰巴托 / 塞舌尔群岛 |  |
| Lydia / Persia / Athens / Rome / Cyrene / Alexandria / Antioch / Constantinople / Levant / Mesopotamia | 吕底亚 / 波斯 / 雅典 / 罗马 / 昔兰尼 / 亚历山大港 / 安条克 / 君士坦丁堡 / 黎凡特 / 美索不达米亚 |  |
| Levantine / Grecosyrian / Phoenician | 黎凡特人的 / 希腊叙利亚人 / 腓尼基的 | 作者自称 Levantine；修饰习俗、说法时写“黎凡特的”，例如第 12 章 Levantine beliefs 写“黎凡特民间说法” |
| The Wall Street Journal / The Economist / Newsweek / Forbes / The New Yorker / Vanity Fair | 《华尔街日报》/《经济学人》/《新闻周刊》/《福布斯》/《纽约客》/《名利场》 | 不括注 |
| Foreign Affairs / Paris Match / Tatler | 《外交事务》/《巴黎竞赛画报》/《尚流》 | 每节第一次出现时括注原题 |

## 常提到的书

| 英文 | 译法 | 说明 |
| --- | --- | --- |
| Iliad / Odyssey | 《伊利亚特》/《奥德赛》 |  |
| The Millionaire Next Door / The Millionaire Mind | 《邻家的百万富翁》/《百万富翁的智慧》 | Stanley 的书；序言和书末注释都写《百万富翁的智慧》，华文出版社 2011 年出过中译本（ISBN 9787507533460），中文书名没有核实 |
| Irrational Exuberance | 《非理性繁荣》 | 希勒 |
| The Bible Code / The Da Vinci Code | 《圣经密码》/《达·芬奇密码》 |  |
| The Tipping Point | 《引爆点》 | 格拉德威尔 |
| Descartes’ Error / The Emotional Brain | 《笛卡尔的错误》/《情绪大脑》 | 达马西奥 / 勒杜；后一本的中译本书名没有核实 |
| Mean Genes / The Selfish Gene | 《卑鄙的基因》/《自私的基因》 |  |
| Fashionable Nonsense | 《时髦的空话》 | 索卡尔和布里克蒙 |
| In Search of Time Lost | 《追忆似水年华》 | 作者用的英译题名 |
| The Trial | 《审判》 | 卡夫卡 |
| Treatise on Probability / Treatise on Human Nature | 《概率论》/《人性论》 | 凯恩斯 / 休谟 |
| The Open Society / The Alchemy of Finance | 《开放社会及其敌人》/《金融炼金术》 | 波普尔 / 索罗斯 |
| Simple Heuristics That Make Us Smart | 《简捷启发式：有限理性让我们更聪明》 | 吉仁泽等人编的论文集，用已出版的中译本书名（机械工业出版社，ISBN 9787111582458） |
| The Nature of Rationality | 《合理性的本质》 | 诺齐克；第 6 章 |
| Letters from a Stoic | 《道德书简》 | 塞涅卡的书信集 |
| Manhattan Transfer / Earth in the Balance / Memoirs of My Life | 《曼哈顿中转站》/《濒临失衡的地球》/《我的一生》 | 多斯·帕索斯 / 戈尔 / 卡萨诺瓦 |
| Flatland / Against the Gods / Treatise on Laughter / Les gommes / We | 《平面国》/《与天为敌》/《笑》/《橡皮》/《我们》 |  |
| The Sign of Four / Silver Blaze | 《四签名》/《银色马》 | 柯南·道尔 |
