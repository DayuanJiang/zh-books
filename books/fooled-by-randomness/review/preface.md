# 序言 别太把知识当真（preface）审校记录

全节 30 个块，原文没有注释，中文没有加译者注；中英逐块对应（`site.py status` 显示 30/30）。

## 1. 译者自检

- 执行者：translation agent（Opus 5.5），译者本人。
- 范围：全节 30 块（1 个一级标题、5 个二级标题、24 个段落），对照原文逐段检查漏译、增译、否定、条件、数字和日期、责任主体、比较对象、术语义项、人名和格式。另外做了这些检查：
  - `python3 scripts/site.py status fooled-by-randomness`：preface 30/30。
  - `tools/term_consistency.py`：本节没有提示。
  - 用 markdown-it（CommonMark）渲染中英两个文件：中文 29 处斜体，英文 29 处。英文的 *Newsweek* 在中文按体例写《新闻周刊》，不用斜体；英文 “affirming the consequent” 那一处的星号没有被解析成斜体（见“原文疑点”），中文按原意写成斜体的“*肯定后件*”。中文渲染后没有残留的星号，链接只有 `[亚马逊](http://amazon.com)` 一处，URL 和英文相同。
  - 在 `/tmp` 的一份副本里把本节设成草稿，用 `framework/tools/build.py --drafts` 构建通过。`site.py check fooled-by-randomness` 也通过。
  - 本节没有破折号，没有体例禁用的对比句式，中文里没有半角标点，也没有嵌套括号。
- 发现并修改：
  - 第 22 块 “If I write that I doubt that my neighbor’s success is devoid of some measure, small or large, of luck”：草稿写成“我怀疑他的成功里没有运气成分”，中文的“怀疑……没有”会被读成“我猜他的成功里没有运气”，意思正好反了。改为“我不相信他的成功能和运气毫不沾边，不管运气的分量是大是小”。
  - 第 13 块 “but they are by far the most interesting”：初稿“到目前为止它是最有意思的一个”把 by far（远远超过）误解成了“迄今为止”，改为“不过它比其他陷阱有意思得多”。
  - 第 15 块 “The consolation for the lack of attacks”：初稿“没有人来攻击我”和上一段说的亚马逊上的匿名抨击矛盾。作者盼的是“who are you to judge Warren Buffett”那种当面的怒信，改为“攻击没有等来，安慰倒是以另一种形式来了”。
  - 第 10 块 “(which explains the warnings against economists and finance professors …)”：初稿“书里为什么一再告诫读者提防”，“一再”是原文没有的，删掉。
  - 第 11 块 “considering that alternative outcomes could have taken place, that the world could have been different, is the core of probabilistic thinking”：初稿以“考虑到……”开头，中文容易读成表示原因的连词，改为“把别的结果本来也可能发生、世界本来也可能是另一番样子考虑进去，就是概率思维的核心”。
  - 第 6 块 “a little less of a student of uncertainty … and more of a researcher into how people are fooled by it”：初稿“研究不确定性少了一点，研究人们怎样被它愚弄多了一点”丢了 student 和 researcher 的对照，改为“变得不太像一个研究不确定性的学生了……更像一个研究人们怎样被随机性愚弄的研究者”。
  - 第 22 块 “I am not saying that Warren Buffett is not skilled; only that …”：初稿“我并不是说……；我只是说……”接近体例禁用的句式，改为“我并没有说……；我只是说……”。
  - 第 20 块 “even though it seems intuitively correct to think so”：原文这句插在假设和结论之间，指的是把命题反过来推的那种想法。初稿放在句首，读起来像是在说“好品质导致成功”这个假设凭直觉没错，挪到句末，写成“……都必定是聪明、勤奋、坚持不懈的人，尽管凭直觉这么想似乎没错”。
- 下面这些地方，原文括号里有人名或第二层括号，照搬会出现嵌套括号或两组括号相连，所以调整了句子结构，意思不变：
  - 第 10 块 “Hume’s Problem of Induction (or Aristotle’s inference to the general)”：写成“从休谟（Hume）的归纳问题引出来的东西，也可以说是从亚里士多德（Aristotle）所说的由个别推出一般引出来的”。
  - 第 13 块 “(I used as a model my second-generation friend Jacques Merab)”、第 15 块 “(not coincidentally also dominated by Daniel Kahneman, …)”：拆成独立的句子。
  - 第 17 块 “(clearly I lost the debate to the formidable Desmond Fitzgerald … —I was even tempted to switch sides!)”：拆成两个分句，破折号改为逗号。
  - 第 21 块 “*The Millionaire Next Door* (that I discuss in Chapter 8)”：写成“《邻家的百万富翁》（*The Millionaire Next Door*）是一本误入歧途的书，我会在第 8 章讨论它”。
  - 第 24 块 “(including a hilarious *dialogue de sourds* on a Las Vegas radio station …)”：括号里还要按体例括注中文意思，所以改成括号外的一句，写“*dialogue de sourds*（聋子的对话）”。
  - 第 27 块 “(like George Will, who will appear in Chapter 2)”：去掉外层括号，放到句末，写“比如第 2 章会出场的乔治·威尔（George Will）”。
  - 第 29 块 “Kojo Anandi (NPR), Robin Lustig (BBC), …”：人名括注英文后还有电台名的括号，改成“NPR 的科乔·阿南迪（Kojo Anandi）”这种写法。
- 译法上的选择：
  - 第 2 块 “the no-nonsense practitioner of uncertainty” 和后面 “willing to be fooled by any form of nonsense” 是文字游戏，写“容不得胡话、和不确定性打交道的实干者”和“只要胡话够精致……他都甘愿被它愚弄”，保留呼应；nonsense 照术语表写“胡话”，practitioner 照术语表写“实干者”。“the fool of randomness” 写“被随机性愚弄的人”。
  - 第 3 块 “straight from the gut” 写“完全出自本能”；“scientific name dropping” 写“搬出科学家的名字来撑场面”；“random use of borrowed wisdom” 写“随手借用别人的智慧”；拉丁语引文照写原文，作者给的英文意思译成“只在言语胜过沉默时开口”。
  - 第 5、6 块 “adding to the winner” 是交易员的行话，指在赚钱的头寸上继续加码，小标题和正文都写“给赢家加仓”；“fat tails” 写“肥尾”，术语表没有收这个词。
  - 第 7 块 *hindsight bias* 照术语表写“*后见之明偏差*”，保留斜体；“backfit explanations concocted ex post” 写“在事后编出来、倒过来套上去的解释”，第 26 块 “the backfit logic” 写“倒推出来的逻辑”；“deranged subjects” 指实验的受试者，写“精神错乱的受试者”；“timing moves” 写“择时出手”。
  - 第 9 块 “intellectual insecurity” 写“智识上的不安全感”，小标题 “Insecurity and Probability” 写“不安全感与概率”；“Half a millennium later” 写“五百年后”。
  - 第 12 块小标题 “Vindicating (Some) Readers” 写“为（一些）读者正名”；正文里 “felt vindicated by the book” 写“觉得这本书证明了他们是对的”。
  - 第 13 块 “second-generation friend” 理解为两代人的交情，写“世交好友”；第 15 块 “brother-in-law” 中文没有统称，写“姐夫”。
  - 第 16、17 块 “all-or-none” 写“全有或全无”；“Cambridge Union Debate” 写“剑桥联合会一场广受关注的辩论”；“City Hotshots” 指伦敦金融城的人，写“伦敦金融城大腕”；“Lucky Fools” 照术语表写“幸运的傻瓜”；“The Fooled by Randomness symptom” 原文没有斜体，写“这种被随机性愚弄的症状”。
  - 第 20 块 “affirming the consequent” 写“*肯定后件*”，和书末注释的主题词一致；“two systems of reasoning” 写“两种推理系统”，和第 11 章的小标题一致。
  - 第 21 块 *The Millionaire Mind* 照术语表写《百万富翁的智慧》；“a textbook case of naive empiricism” 照术语表写“朴素经验主义的一个教科书式的案例”。
  - 第 22 块 “round-trip fallacy” 照术语表写“往返谬误”；“*me-too* publishers” 写“*跟风*的出版商”，保留斜体；Texere 照写原名。
  - 第 24、29 块 “sound bites” 写加引号的“金句”。
  - 第 26 块 “people think that there is a story when there is none” 和主持人的 “There was a story about Cisco this morning” 是双关，写“明明没有故事，人们也以为有故事”和“今天早上就有一个关于思科的新闻故事”，保留“故事”二字。
  - 第 29 块 “the quality of the discussion correlates inversely with the luxury of the studios” 写“呈负相关”；“this side of Kazakhstan” 写“在哈萨克斯坦以外”。
  - 第 30 块 *Homo sum* 照体例的示例写“*Homo sum*（我是人）”。
  - 第 14 块链接 `[amazon.com](http://amazon.com)` 的文字按术语表写“亚马逊”，URL 不变。
- 人名：和 `review/terms/people-zh.tsv` 逐个核对过，每人在本节第一次出现时括注英文：蒙田（Montaigne）、笛卡尔（Descartes）、休谟（Hume）、亚里士多德（Aristotle）、雅克·梅拉布（Jacques Merab）、沃伦·巴菲特（Warren Buffett）、丹尼尔·卡尼曼（Daniel Kahneman）、塔勒布（Taleb）、德斯蒙德·菲茨杰拉德（Desmond Fitzgerald）、乔治·威尔（George Will）、科乔·阿南迪（Kojo Anandi）、罗宾·拉斯蒂格（Robin Lustig）、罗伯特·斯卡利（Robert Scully）、布赖恩·莱勒（Brian Lehrer）。原文只写姓的人，括注也只写姓。机构照术语表：美国证券交易委员会、NPR、BBC、PBS、WNYC。
- 数字：16 世纪、第 2 章、第 8 章、第 11 章、第 13 章和第 14 章、全书 14 章、50 多万读者用阿拉伯数字；十年、三分之一、三章、五百年、半个世纪、一千多名、三只股票、几个月、一个小时用汉字。
- 未决：
  - 第 28 块 “This guy Nassim” 是作者本人，第 17 块已经括注过“塔勒布（Taleb）”。这里换了称呼，读者未必知道纳西姆就是塔勒布，所以照第 6 章的写法括注成“纳西姆（Nassim）”。如果全书要求同一个人只括注一次，请主会话删掉这处括注。
  - 第 21 块的书名照术语表写《百万富翁的智慧》，书末注释序言部分的主题词写的是“百万富翁的头脑”，两处不一致，请主会话统一。
  - 第 15 块 “brother-in-law” 写“姐夫”是一种取舍，原文没有说是哪一种姻亲。
  - 小标题“给赢家加仓”“为（一些）读者正名”“错过一场恶作剧”是译者拟的，请主会话确认。
  - 双语审校、中文通读和阅读器校样还没有做；`book.json` 里本节的状态由主会话修改。

## 原文疑点

| 位置 | 原文 | 处理 |
| --- | --- | --- |
| 第 3 块 | *Aut tace aut loquere meliora silencio* | 这句拉丁语出自斯托拜乌斯的文集，萨尔瓦多·罗萨（Salvator Rosa）自画像上的铭文写作 silentio（Web Gallery of Art 的作品说明和维基百科的条目都是这个拼法），silencio 疑为拼写变体或笔误。外文引语照原文写 silencio，不加注 |
| 第 6 块 | less, far less, random that it actually is | that 应为 than，按 than 的意思译“把世界看得不如它实际那样随机” |
| 第 20 块 | logical fallacy\*—affirming the consequent—\*can | en/ 文件里的星号紧贴着破折号，按 CommonMark 规则不会被解析成斜体，英文页面上会直接显示两个星号；原书这里应是斜体。中文按原意写“*肯定后件*”；en/ 没有改，是否修正英文的标记请主会话决定 |
| 第 29 块 | Kojo Anandi (NPR) | NPR 系统的节目主持人里有 Kojo Nnamdi，可能是同一人，原文拼错了；people-zh.tsv 已经注明。照原文和 people-zh.tsv 写“科乔·阿南迪（Kojo Anandi）” |

## 2. 双语审校

- 执行者：另一个独立上下文的 agent（Opus 5.5），没有参与翻译。
- 范围：全节 30 块（1 个一级标题、5 个二级标题、24 个段落），逐块对照英文；人名对照 people-zh.tsv，术语、书名、机构名对照术语表。本节原文没有脚注，中文没有译者注。
- 发现：18 条（意思 5 条，措辞 13 条）；核实后采纳 18 条，不采纳 0 条。其中 7 条采纳了审校者指出的问题，改法由编辑另写。每一条编辑都对照英文核实过。
  - 采纳，按建议改：
    - 第 22 块 “This text is a series of logical thought experiments, not an economics term paper” 和第 10 块 “In this book probability is principally a branch of applied skepticism, not an engineering discipline”：“算不上”带有“够不上那个标准”的意思，作者说的是这本书属于另一类东西，两处都改为“并非”。第 3 块 “not exactly a treatise, and certainly, god forbid, not a piece of scientific reporting” 的两个“算不上”保留：not exactly 本来就是“称不上”的意思，后一处前面有“老天保佑”，读者看得出作者并不想把书写成科学报告。
    - 第 4 块 “I have also added new material to most chapters, most notably in Chapter 11”：原译“补得最多的是第 11 章”把强调说成了数量上的比较，改为“尤其是第 11 章”。
    - 第 26 块 “When invited to an hour-long discussion on a financial radio show”：原译“一家财经电台”把节目写成了整家电台，改为“一档财经广播节目”。
    - 第 3 块 “This comes straight from the gut”：“完全出自本能”偏向条件反射，改为“全凭直觉写成”。译者自检里记下的这一写法随之改掉。
    - 第 10 块 “It is presented as flowing from Hume’s Problem of Induction (or Aristotle’s inference to the general) as opposed to the paradigm of the gambling literature”：原译重复两次“引出来”，最后一个分句没有主语承接，改为“书里讲的概率，源自休谟（Hume）的归纳问题，或者说源自亚里士多德（Aristotle）所说的由个别推出一般，并不源自赌博文献的那套范式”。
    - 第 10 块段首 “There are many intellectual approaches to probability and risk” 和后面讲 “probability” 在各学科意思略有不同的一句：原文破折号处的逗号让两句连成一口气，改为冒号（审校者建议用分号，冒号更能表明后一句是在解释前一句）；“和定量的、‘科学的’路子相对”改为“而非定量的、‘科学的’路子”。
    - 第 9 块 “I got sucked into the implications of the difference between Montaigne and Descartes”：“这些问题让我一头扎了进去”缺了去处，改为“我一头扎进了这些问题里”，前面的“去寻求确定性”后加逗号断开。
    - 第 15 块 “the unexpected large-impact random event (the loss of a baby)”：“失去了一个婴儿”带着英文冠词的痕迹，改为“孩子夭折”。
    - 第 21 块 “He observes that in the representative cohort of more than a thousand millionaires whom he studied …”：定语堆叠，拆成“他研究了一千多名百万富翁，这是一个有代表性的群体。他观察到，其中大多数人……”。
    - 第 30 块 “the buildup of rules of thumb that do not have empirical validity”：“没有经验依据的经验法则”改为“没有实证依据的经验法则”，并删掉原文没有的“也”。
  - 采纳了问题，改法另写：
    - 第 6 块 “a little less of a student of uncertainty (we can learn so little about randomness) and more of a researcher into how people are fooled by it”：原译“研究不确定性的学生”会被读成在校学生，“不太像……了”也比 a little less 重；审校者的建议连用好几个“的”，句子太长。改为“作者身上渐渐起了变化：研习不确定性的那一面少了一点（关于随机性，我们能学到的实在太少），研究人们怎样被随机性愚弄的那一面多了一点”。“研习”和“研究”保留了 student 和 researcher 的对照，“学到”接上括号里的 learn，“少了一点”“多了一点”对应 a little less 和 more。译者自检里记下的“研究不确定性的学生”随之改掉。
    - 第 19 块 “No, I am not saying that what your grandmother told you about the value of work ethics is wrong!”：审校者建议的“我并没有说你祖母跟你讲的敬业精神有多可贵，那些话是错的”会被读成“我没说敬业精神可贵”，意思走样。改为“你祖母跟你讲敬业精神有多可贵，我并没有说她讲错了！”
    - 第 25 块 “A famous television show was told that …”：审校者建议的“一档著名的电视节目听人说”仍然让节目去听话。改为“有一档著名的电视节目，节目组听人说……”；后面的“请我上节目讲讲”改为“请我去讲讲”，这样一句里只出现两次“节目”。
    - 第 22 块 “If I write that I doubt that my neighbor’s success is devoid of some measure, small or large, of luck, owing to the randomness in his profession, I do not need to ‘test’ it”：拆成两句，“设想我写下这么一句：我邻居那一行有随机性，所以我不相信他的成功能和运气毫不沾边（不管运气的分量是大是小）。这句话我用不着去‘检验’……”。审校者建议的“充满随机性”比 the randomness in his profession 说得重，保留“有随机性”。
    - 第 11 块 “clearly and by far the least original chapter of the book”：“而且远远排在最后”会被读成名次，改为“显然是全书独创性最低的一章，比其他各章低得多”；建议里的“独创性最差”搭配不顺，换成“最低”。
    - 第 3 块 “did not come from a writer whom I had intimately frequented over the years”：“一直亲近的作家”会被读成和作家本人有私交，改为“多年来反复研读、十分熟悉的作家”。定语因此变长，整句改为“我尽量只用这样的引语：它们是自然而然从记忆里冒出来的，出自我多年来反复研读、十分熟悉的作家”。
    - 第 15 块 “people who did not fare well in life, through no fault of their own”：“却并非自己过错的人”缺了主语，改为“那些人生不顺、错又不在自己的人”，比建议里的“错却不在自己”顺口。
  - 不采纳：无。
- 审校者的总体判断：译文忠实、完整，读起来基本自然，可以小改后进入中文通读。30 块中英对得上；人名、术语、书名、机构名、数字、斜体和外文引语的处理都合乎体例；没有破折号，没有体例禁用的对比句式。问题以措辞为主，没有严重误译；意思上的细微偏差有五处：两处“算不上”、“补得最多的是第 11 章”、财经广播节目写成了电台、“多年来一直亲近的作家”。

## 3. 中文通读

- 执行者：编辑 agent（Opus 5.5）。
- 范围：采纳审校意见之后，从一级标题读到最后一段，看行文是否连贯、有没有重复、指代是否清楚、人名和术语前后是否一致。每一处改动都回头对照了英文。
- 发现并修改（4 处）：
  - 第 21 块 “From this, one can naively infer that chance plays no part in success.”：前一句刚用过“于是推断”，这里又写“由此可以天真地推断”，改为“由此还可以天真地得出结论：偶然在成功中不起任何作用”。
  - 第 21 块 “My intuition is that if millionaires are close in attributes to the average population, then I would make the more disturbing interpretation …”：“我的直觉是，如果……，我会作出……”前后接不上，改为“按我的直觉，如果……，我会作出一个更让人不安的解释”。
  - 第 29 块 “Casually, the quality of the discussion correlates inversely with the luxury of the studios”：“随便说一句”在中文里不太常用，改为“随口说一句”，保留作者随口一提、并不严谨的口气。
  - 第 30 块 “I find that injecting the personality of the author (imperfections included) enlivens the text”：这里的 I find 是作者的看法，“我发现”改为“我觉得”；这样三句之内只剩两个“发现”。
- 读过、没有改的地方：
  - 第 10 块连续三句分别以“这本书里的概率”“书里讲的概率”“在这本书里”起头。英文也用 In this book、It is presented、In this book probability 三次强调，保留。
  - 第 22 块 “logic does not require empirical verification” 写“经验验证”，第 30 块 “empirical validity” 写“实证依据”。前者是哲学里的常见说法；后者紧挨着“经验法则”，用“实证”读起来不绕。两处语境不同，保留。
  - 第 9 块 “A reader turned pen pal made me rediscover …”：这位笔友的性别原文没有说，“是他让我”按中文泛指的习惯写“他”，保留。
- 一致性：人名在本节第一次出现时都括注英文，之后只写中文，沃伦·巴菲特、塔勒布、蒙田、笛卡尔、布赖恩·莱勒的第二次出现都核对过。运气、能力、机遇、被随机性愚弄、胡话、实干者、敬业精神、黑天鹅、稀有事件、过往业绩、往返谬误、俄罗斯轮盘赌的写法全节一致；`tools/term_consistency.py` 对本节没有提示。
- 检查：`python3 scripts/site.py status fooled-by-randomness` 显示 preface 30/30；全节没有破折号，没有体例禁用的对比句式，没有半角标点。`site.py check fooled-by-randomness` 的草稿构建通过，提示字体子集缺字，发布前要运行 `site.py fonts`。

## 状态

- 没有未解决的意义问题。双语审校指出的五处意思偏差都已改正，中文通读没有发现新的意思问题，也没有新的原文疑点。
- 译者自检留给主会话的几项还没有定：第 28 块“纳西姆（Nassim）”的括注是否保留；《百万富翁的智慧》和书末注释主题词“百万富翁的头脑”怎样统一；第 15 块 “brother-in-law” 写“姐夫”，是在几种姻亲里选了一种，原文没有说明是哪一种；三个小标题“给赢家加仓”“为（一些）读者正名”“错过一场恶作剧”的确认；英文第 20 块的斜体标记是否修正。
- 阅读器校样还没有做；`book.json` 里本节的状态（现在是 todo）由主会话修改。

## 第三轮：GPT-6 Astra 独立审校

- 审校者：GPT-6 Astra，通过 Codex 运行，只读，和译者属于不同的模型家族。
- 发现：6 条（意思 3 条，措辞 3 条）。逐条找到中英文对应的句子，读过上下文后核实：成立并修改 4 条，不成立 2 条。
- 成立并修改：
  - 第 21 块 “That all millionaires were persistent, hardworking people does not make persistent hard workers become millionaires”：原译“所有百万富翁都是坚持不懈、勤奋工作的人，并不能让坚持不懈、勤奋工作的人都变成百万富翁”。逗号后面的“并不能让”没有主语，按中文的习惯会接上前一分句的“所有百万富翁”，读成百万富翁没法让勤奋的人变成百万富翁。审校者建议改成“不能据此推断”，可作者在这里特意用了表示因果的 make，接的是上一句“把*必要的*东西和起因果作用的东西混为一谈”，所以保留“让……变成”，补上主语。新译：“所有百万富翁都是坚持不懈、勤奋工作的人，这一点并不能让坚持不懈、勤奋工作的人都变成百万富翁”。
  - 第 22 块 “only that a large population of random investors will *almost necessarily* produce someone with his track records *just by luck*”：原译“一大群随机的投资者里”。“随机的”放在指人的名词前面，中文常读成“随机抽出来的”，例如“随机的路人”；作者说的是投资决定全凭随机的人，对应前面“构造一群智力欠佳的人”的思想实验。审校者建议的“一大群随机作出投资决策的人里”偏长。新译：“一大群随机投资的人里”。
  - 第 25 块 “this guy Taleb believes that stock analysts are just random forecasters”：原译“股票分析师不过是随机的预测者”，问题和上一条相同。改成说预测本身是随机的，也和后面“随机挑三只股票来谈”接得上。新译：“股票分析师不过是在随机地做预测”（审校者建议“在随机给出预测”，意思相同）。
  - 第 29 块 “However, media journalism is less standardized than it appears; it attracts a significant segment of thoughtful people”：原译“不过，媒体新闻并不像看上去那样千篇一律”。能吸引有思想的人进来、让他们摆脱商业体制的是这个行业，“媒体新闻”指的是报道内容。按审校者的建议，新译：“不过，新闻业并不像看上去那样千篇一律”，和第 2 章、第 3 章、第 9 章 journalism 的写法一致。第 24 块 “the book’s aggressive warning against media journalism” 写“提防媒体新闻”，说的是读者该提防的报道，保留。
- 不成立，保留原译：
  - 第 3 块 “This comes straight from the gut”：审校者认为“这本书全凭直觉写成”改变了原意，建议写“这本书写的是我的肺腑之言”。from the gut 说的是凭本能、未经推敲，下文紧接着讲作者写第一版时定的规矩：只写亲眼见过或自己想出来的东西，删掉像是跑了一趟图书馆才写出来的段落，凡是像干活的一律不要，正是凭直觉写的意思。“肺腑之言”强调真诚，偏离了这一层。上一轮双语审校已经把“完全出自本能”改成现在的写法，保留。
  - 第 11 块 “Probability is not a mere computation of odds on the dice or more complicated variants”：审校者认为 odds 指几率，“赔率”把概率和赌注的回报混在一起，建议改成“各种结果出现的概率”。全书把 odds 统一写成“赔率”（第 1、2、3、6、9、11、12、13 章），第 13 章章首提要的 “probability is not about the odds” 写“概率和赔率无关”，和这一句前后呼应；“赔率”在赌博的语境里也常用来指胜算。改成“概率”以后，这句会变成“概率的意义远不止计算……的概率”，作者拿赌桌上的计算和概率对比的意思就没了。保留。
- 按全书统一的写法修改：2 处。
  - 第 9 块座右铭 “*my principal activity is to tease those who take themselves and the quality of their knowledge too seriously.*”：按“take knowledge seriously 写‘当真’”，“取笑那些把自己和自己知识的质量看得太重的人”改为“取笑那些把自己和自己知识的质量太当真的人”，和标题“别太把知识当真”呼应。
  - 第 7 块 “much of what he was saying was just backfit explanations concocted ex post by his deluded mind”：按“backfit 按上下文写‘倒推出来的’”，“在事后编出来、倒过来套上去的解释”改为“在事后倒推、编造出来的解释”，和第 26 块“倒推出来的逻辑”一致。
  - 其余各条核对过，这一节已经合乎规定：Nassim 出现在别人的话里，写“纳西姆（Nassim）”；brother-in-law 写“姐夫”；书名写《百万富翁的智慧》。译者自检和中文通读留给主会话的这三项，统一写法里已经有了结论。数字（16 世纪、十年、五百年、一千多名、三只股票、50 多万读者）合乎规定，“五百年”是 half a millennium 的约数。《新闻周刊》不括注。ex post 写“事后”，用正体；*dialogue de sourds*、*Homo sum* 保留斜体并括注中文。本节非生物学意义的 evolution、evolve 写“我个人的变化”“变成成功的商人”，第 3 章、第 13 章同类的用法也按上下文写成“演变”“演进”，保留。“休谟（Hume）的归纳问题”和书末注释“古德曼（Goodman）的归纳之谜”写法相同，保留。本节没有需要加译者注的地方。
- 对英文原文的疑问：审校者提了两条，都已经记在本记录的原文疑点表里：第 6 块 “less, far less, random that it actually is” 的 that 应为 than；第 29 块 “Kojo Anandi” 可能是 Kojo Nnamdi 的误拼，照 people-zh.tsv 写“科乔·阿南迪（Kojo Anandi）”。本轮没有新的疑点。
- 核实与修改：agent（Opus 5.5）。改完后运行 `python3 scripts/site.py status fooled-by-randomness`：preface 30/30，本节没有注释；全书 1294/1294 块已译。用 markdown-it 渲染本节，29 处斜体，没有残留的星号；中英两个文件都是 59 行，块的对应没有变；没有破折号，没有体例禁用的对比句式。
