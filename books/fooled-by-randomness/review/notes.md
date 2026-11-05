# 去图书馆走走：注释与阅读推荐（notes）审校记录

全节 154 个块，原文没有脚注，中文另加 1 条译者注 [^t1]；中英逐块对应（`site.py status` 显示 154/154）。

## 1. 译者自检

- 执行者：translation agent（Opus 5.5）。
- 范围：全节 154 块和 1 条译者注，从第 1 块到第 154 块逐块对照原文，检查漏译、增译、否定、条件、数字和日期、谁做了什么、比较对象、术语义项、人名、文献引用和格式。另外做了这些机械检查：
  - `python3 scripts/site.py status fooled-by-randomness`：notes 一行是 154/154，没有对不上的块。
  - 用框架的 `book.compile_chapter` 编译这一节（它在 `book.json` 里还是 `todo`，草稿构建不会包含它），全部块和 [^t1] 都能编译，译者注的弹窗内容正确。
  - 用框架的 markdown-it 渲染每一块：中文渲染后的文字里没有残留的 `*`；每块的粗体、斜体、链接个数和英文一致，不一致的五处都是有意的（见下面“格式”）。
  - 逐块比较中英两边的数字，差异都是换算造成的（April 写“4 月”，1960s 写“20 世纪 60 年代”，$1 million 写“100 万美元”，twelve-month 写“12 个月”，twenty-one 写“21 岁”，$10,000 写“1 万美元”，a quarter of a million 写“25 万英镑”，Finance 101 写“金融学入门课”）。
  - `tools/term_consistency.py`：notes 里只报了一处，第 70 块的引用 Nozik (1993)，见“原文疑点”。
  - 全文没有破折号，没有体例禁用的对比句式，没有夹在汉字之间的半角标点。
- 发现并修改：
  - 粗体主题词的写法。照术语表的例子写成 `**后见之明偏差：**也就是……` 时，框架用的 CommonMark 解析器认不出粗体的结尾（结尾的 `**` 前面是全角标点、后面紧跟汉字），页面上会直接露出星号。108 个主题词都改成 `**后见之明偏差**：`，冒号放在粗体外面。第 49 块的 “Why don’t we learn from our past history?:” 同理写成 `**我们为什么不从自己过去的经历里吸取教训**？`，只保留问号。
  - 斜体同样的问题：第 116 块的规则 “*If a card has a vowel on one side, then it has an even number on the other side.*” 和第 66 块 E. O. Wilson 引文里的斜体两句，句号放进斜体时也渲染不出来，改成把句号放在斜体外面。
  - 第 66 块 “Evolution is principally a probabilistic concept”：初稿“本质上”说得比 principally 重，改为“主要是”。
  - 第 66 块 “One of them will fare better than the other”：初稿“混得好”太口语，也偏离了赌场里输赢的意思，改为“其中一个的结果会比另一个好”。
  - 第 92 块 “Their dynamics, conditional on past growth, become predictable”：初稿“它的动态”指代不清，their 指销量，改为“销量的动态”。
  - 第 29 块 “how some physical traits and the manner of a given individual promote certain emotional responses in others”：初稿“会激起什么情绪反应”丢了 how 和 certain，改为“怎样在别人身上激起某些情绪反应”。
  - 第 125 块 “the debate is bitter not because of large divergences of opinions but because of small ones”：按体例换掉对比句式，写“这场论战之所以激烈，起因是意见上的小分歧，和大分歧无关”。
- 译法上的处理（供后面的审校参考）：
  - 原文的 not X but Y 句子都换成了直接的说法。第 8 块 “not that everything we think about needs to be deductive” 写“他并没有说我们思考的一切都必须是演绎的”；第 48 块 “rather than some CD-style recording” 写“并没有把它看成某种 CD 式的录音”；第 76 块 “not an ascending market but one that *ascends then crashes*” 写“与其说是一个上涨的市场，不如说是一个*先涨后崩*的市场”，“not blue but ‘grue’” 写“这样的东西应该叫‘绿蓝’（grue），叫它‘蓝’就错了”；第 86 块 “not as a statistical device” 写“并没有把它当作统计工具”；第 102 块 “it does not describe how people *do* act but rather how they *should* act” 写“它描述的是人*应该*怎样行动，并不描述人*实际上*怎样行动”；第 142 块 “not rickety but plain wrong” 写“岂止摇摇欲坠，根本就是错的”，“a matter of knowledge, not one of computation” 写“知识问题，和计算关系不大”。
  - 文献引用：“作者（年份）”形式照写英文，包括 and、et. al. 和原文的拼法（Knetch、Damasion、Nozik、Wilson, et. al.）；例外是第 137 块和第 93 块，见“原文疑点”。引用后面的标点用中文标点，例如 “Hacking (1990),or” 写“Hacking (1990)，或者”。
  - 人名：和 `review/terms/people-zh.tsv` 逐个核对过。在行文里出现的人，每人第一次出现时括注英文，之后只写中文，共 50 多人，例如彼得·麦克伯尼（Peter McBurney）、戴维·芒福德（David Mumford）、米尔（Meehl）、皮尔士（Peirce）、吉仁泽（Gigerenzer）；第 153 块的 Gerd Gigerenzer 是第二次出现，写“格尔德·吉仁泽”，不括注。原文只写姓的，括注也只写姓。表里写 keep 的人（Evans、E. O. Wilson 等）照写英文。第 141 块名单里的 Bernouilli 写“伯努利（Bernoulli）”，括注用正确的拼法。表里没有的三个名字：Damasio 书里的失忆症患者 David 写“戴维（David）”；第 13 块例句里的 Smith family 写“史密斯家”，是虚构的例子，没有括注；第 96 块的 “A.” 照写，加“扔打火机的”交代他是第 9 章那位。
  - 主题词里的书名：*The Selfish Gene*、*Les gommes*、*The Tipping Point* 写成 `**《自私的基因》（*The Selfish Gene*）**`，保留粗体，括注原题。第 15 块 “The millionaire mind” 和第 81 块 “The millionaire next door” 在原文里是小写、不用斜体的主题词，写成普通的短语“百万富翁的头脑”“邻家的百万富翁”；第 81 块原文没有粗体，中文也没有。
  - 术语：沿用术语表的写法（后见之明偏差、事后诸葛亮、乌托邦愿景、可错论、情感启发式、可得性启发式、副现象、朴素达尔文主义、负偏态、生成器、卢卡斯批判、幸存者偏差、黑天鹅、归因偏差、数据挖掘、幂律、帕累托-莱维分布、莱维稳定分布、样本路径、看跌期权、概率盲、经济人、系统 1、有限理性、情绪脑、行为金融学、心流、启发式与偏差、阿罗不可能定理、夏普比率、唯科学主义、斯多葛主义）。术语表里没有、这一节新定的说法：肯定后件、不可错论、临床预测、精算方法、免疫忽视、前景理论、小数定律、小数问题、归纳谬误、自主运动效应（autokinetic effect）、正反馈循环、选美比赛、股权溢价之谜、热手效应、变异系数、专家经纪人、订单流、元分析、厚尾、转变点、价内、行权价、标的证券、公地悲剧、近因和终极因、模块性、封装性、领域特异性、沃森选择任务（Wason selection task）、识别骗子的模块、搭便车的人、腹内侧额叶皮质、神经经济学、享乐跑步机、基础比率谬误、心理账户、风险价值（value at risk）、主观概率、熵、绿蓝（grue）。
  - 口语和反讽：“Monday morning quarterback” 按术语表写“事后诸葛亮”；Ingersoll 那本书 “dry and very, very boring, like the personality of its author” 写“枯燥，非常非常乏味，就像它的作者的为人”；“They smoke us with math” 写“他们用数学唬住我们”；“Portfolio theory (alas)” 写“投资组合理论（唉）”；格拉德威尔父亲的顺口溜 “Tomato ketchup in a bottle—None will come and then the lot’ll” 写成押韵的“番茄酱装在瓶子里，一滴不来，一来全来”，原文的破折号去掉。
  - 外文词：*homo economicus* 写“经济人（*homo economicus*）”；*per se* 直接译成“本身”，没有保留拉丁文；“Panglossian” 写“潘格罗斯式的”，加译者注 [^t1] 说明潘格罗斯是伏尔泰《老实人》里的人物，中文读者多半不熟悉这个典故。
  - 补出的词：第 151 块福尔摩斯的话 “a quarter of a million upon the London poor” 写“将近 25 万英镑”，补了“英镑”，《四签名》原文说的是英镑；第 94 块 “4 times more people with an income higher than $1 million than people with $2 million” 写“收入高于 100 万美元的人数，会是收入高于 200 万美元的人数的 4 倍”，后半句补了“收入高于”。
  - 格式：第 76 块重复的变量 *t* 两处都用斜体；第 99 块第二次出现的 *homo economicus* 写“这种经济人”；第 141 块和第 144 块第二次出现的书名只写中文书名，不再括注原题；第 142 块的 *per se* 没有保留；所以这五块的斜体数和英文不同。第 120 块 “(Bates, 1994) of Fodor’s nine criteria … (ironically Bates is a skeptic on the subject)” 两个括号挨在一起不好读，改成“伊丽莎白·贝茨（Elisabeth Bates）在 Bates (1994) 里对福多（Fodor）九条模块性标准的介绍（说来讽刺……）”。第 22 块平克和索维尔的先后顺序调换，避免括号套括号。
- 未决：
  - 粗体主题词的写法和术语表的例子 `**后见之明偏差：**` 不同，原因见上面“发现并修改”的第一条。请主会话决定是否把术语表的例子改成 `**后见之明偏差**：`；第 5 章引用块里七段开头的粗体短语也会遇到同样的问题。
  - 第 15 块和第 81 块的两个主题词写成普通短语。如果希望读者一眼看出这是 Stanley 的两本书，可以改成书名《百万富翁的智慧》《邻家的百万富翁》并括注原题，请主会话决定。
  - 第 19 块芒福德的文章，书末注释里用斜体，参考文献里用引号。中文照这一节的斜体写成《随机性时代的黎明》（*The Dawning of the Age of Stochasticity*）；如果按术语表“文章的原题保留引号”的规则，括注应改成 “The Dawning of the Age of Stochasticity”。
  - 第 125 块 *Simple Heuristics That Make Us Smart* 写《简单启发式让我们更聪明》，没有查到中译本，书名是直译。
  - 第 126 块 “The evolutionary theorists split into domain general (unconditional probability) as opposed to domain specific (conditional).” 句子不完整，看不出 split 的宾语。按上下文理解为进化理论家把这个问题区分成领域一般的（无条件概率）和领域特异的（条件概率）两种，留给双语审校再看。
  - 第 64 块 “written in light, but with extremely intuitive mathematics”，in light 后面像是少了一个词，理解为“写得轻松”。
  - [^t1] 请用户决定是否保留。
  - 这一节在 `book.json` 里仍是 `todo`（按分工不改 `book.json`），需要主会话改成 `review`，之后才能在 `serve --drafts` 的阅读器里看到。双语审校、中文通读和阅读器校样还没有做。

## 原文疑点

| 位置 | 原文 | 处理 |
| --- | --- | --- |
| 第 137 块 | al-Ghazl (1989) | 转换造成的乱码，丢了带长音符号的字母。`review/source.md` 说参考文献里的同一处已经改成 al-Ghazālī，这一节的没有改到。中文写 al-Ghazālī (1989)，和参考文献对应；en/ 没有动，建议主会话用 `curate_source.py` 一并改掉 |
| 第 70 块 | Nozik (1993) | 参考文献写的是 Nozick, Robert, 1993。按“引用照写英文”的体例（和第 122 块的 Damasion 一样）保留 Nozik，`term_consistency.py` 因此报了这一处。是否改成 Nozick (1993)，请主会话决定 |
| 第 93 块 | (Gladwell,1996) | 逗号后漏了空格，`curate_source.py` 补空格时没有覆盖到这一处。中文写 (Gladwell, 1996) |
| 第 52 块 | the atrophy of the hycocampus | hycocampus 是 hippocampus（海马体）的笔误，译“海马体” |
| 第 141 块 | Bernouilli | Bernoulli 的笔误，术语表已经记录。中文写“伯努利（Bernoulli）”，括注用正确的拼法 |
| 第 86 块 | the concept has been commonly used in statistics and called “coefficient of variation.” | 统计学的变异系数是标准差除以均值，夏普比率是收益除以标准差，两者互为倒数，作者说成同一个概念不够准确。照原文译出 |
| 第 86 块 | the “Sharpe ratio” differences for two uncorrelated managers would exceed 1.8 with close to 50% probability | 按常用的近似，一年数据估计出的年化夏普比率标准误约为 1，两个独立估计之差的标准误约为 1.41，差值超过 1.8 的概率约为 20%，接近 50% 的门槛大约是 0.95。作者可能用了别的假设，属于疑似。照原文译出 |
| 第 76 块 | something blue until time *t,* beyond which it is green—that such object is not blue but “grue.” | 古德曼原来的定义是：在 *t* 之前是绿色、之后是蓝色才叫 grue；作者说的“先蓝后绿”在古德曼那里叫 bleen。不影响论证，照原文译出 |
| 第 78 块 | the prophetic Hayek (1994), first published in 1945 | 参考文献里 Hayek (1994) 是《通往奴役之路》（*The Road to Serfdom*），初版于 1944 年。照原文写 1945 年 |
| 第 94 块 | the incidence of a deviation of a multiple of *x* will be that multiple to a given power exponent | 照字面是“发生率等于这个倍数的幂次”，会随倍数变大，和前一句的例子（收入翻倍，人数降为四分之一）以及后一句“指数越高，大偏离的概率越低”矛盾。按作者的本意译成“发生率要除以这个倍数的幂指数次方” |
| 第 66 块 | Why do they think in this shortsighted way? “The reason is simple: | E. O. Wilson 的引文中间多了一个左引号，应是原书引文分段留下的。中文去掉这个引号，整段作为一处引文 |
| 第 151 块 | “When I’m thinking about … *The Sign of Four.* “It is of the first importance … the London poor.” | 贝弗林的话里套着福尔摩斯的话，内层引文用了双引号，也没有单独的结束引号。中文外层用“”，内层用‘’，结尾写成 ’” |
| 第 11 章「讲大脑生理结构的书」（第 121 块） | see causal descriptions in Ratey (2001) | 疑为 casual 的笔误，属于疑似。后面列的 Ratey、Ramachandran、Carter、Goleman 等都是通俗读物，“因果性的描述”放在这里说不通；作者在书里别处也用 casual 表示“浅显、随意”（例如 casual knowledge、casual weather forecaster）。按“通俗的介绍”译 |

## 2. 双语审校

- 执行者：另一个独立上下文的 agent（Opus 5.5），没有参与翻译。
- 范围：全节 154 块和译者注 [^t1]，逐块对照英文，检查意思、数字、文献引用、人名、术语和其他章节的一致性，以及中文是否读得顺；还用 markdown-it 逐块渲染，检查有没有残留的星号。
- 发现：20 条；核实后采纳 20 条，不采纳 0 条。每一条我都回到英文和中文原句核对过，其中几条采纳了意思，换了比审校建议更贴切的写法。编辑（Opus 5.5）逐条核实的结果如下。
  - 意思上的偏差，三条都采纳：
    - 芒福德的引文 “devising gambling strategies and counting corpses in medieval London”：in medieval London 只修饰 counting corpses（指伦敦的死亡统计），赌博策略是意大利和法国的数学家研究的。改为“最初是用来设计赌博策略、在中世纪的伦敦清点尸体的”。
    - 福尔摩斯的话 “not to allow your judgment to be biased by personal qualities”：《四签名》里华生刚夸过摩斯坦小姐迷人，后面的例子也是“最迷人的女人”和“最讨人厌的男人”，“品性”会让人理解成道德品质。审校建议写“好恶印象”，我改成“不能让一个人讨人喜欢还是讨人厌左右你的判断”，和后面两个例子直接对应。
    - 古德曼一段 “not an ascending market but one that *ascends then crashes*”：“与其说……不如说”把作者的判断说软了。改为“按这个理论，我们眼前看到的其实是一个*先涨后崩*的市场”；后文已经有“照这种逻辑”，这里用“按”，避免重复。
  - 疑似原文笔误，采纳：第 11 章 “see causal descriptions in Ratey (2001)” 改译“通俗的介绍见”，并在上面的“原文疑点”表里补了一行。
  - 和其他章节、术语表不一致的术语，五条都采纳：
    - “Dogs not barking” 改为“没有叫的狗”，和第 9 章小节标题、各章概要一致。
    - “a cheater detection module” 改为“识别欺骗者的模块”，和第 11 章正文“识别欺骗者”“揭穿欺骗者”一致，也避开全书给 charlatan 用的“骗子”。
    - domain specificity、domain general、domain specific、Domain-specific adaptations 四处，统一成第 11 章的“领域特定性”“领域通用的”“领域特定的”“领域特定的适应”。
    - “The millionaire mind: Stanley (2000)” 和 “The millionaire next door: Stanley (1996)” 改成术语表的书名，括注原题：`**《百万富翁的智慧》（*The Millionaire Mind*）**` 和《邻家的百万富翁》（*The Millionaire Next Door*）。第二处原文没有粗体，中文照样不加。这样也解决了译者自检“未决”里的第二条。
    - *Simple Heuristics That Make Us Smart*：我在网上核实了中译本，书名是《简捷启发式：有限理性让我们更聪明》，机械工业出版社出版，ISBN 9787111582458。改用这个书名，替换原来的直译《简单启发式让我们更聪明》。
  - 读起来会卡住的句子，十一条都采纳，例如：
    - “People are sensitive to sign rather than magnitude” 原译“人们对正负比对大小更敏感”，“比对”容易被读成一个词，改为“人们对正负敏感，对大小不那么敏感”，和第 6 章正文“对某个刺激有没有出现很敏感，对它的大小却不那么敏感”呼应。
    - “except in very narrow matters where linearity is justified” 原译“除了在线性站得住脚的极少数问题上”，“在线性”会先读成“在线”，very narrow 也不等于“极少数”。改为“除了线性关系确实成立的一些很窄的问题”。
    - “they present agents as interested in differences and resetting their pain/pleasure level at zero” 一句里两个“他们”指不同的人，后一个改为“这些人”。
    - “Just put two people in a random environment, say a gambling casino, for a weekend.” 原译“只要……”后面没有结果，审校建议的“……待一个周末，比如赌场”又让“比如赌场”跟在“周末”后面。改为“不妨把两个人放进赌场这样的随机环境，待上一个周末”。
    - “with the ‘small number problem’” 原译“也就是‘小数问题’”把文献和问题说成了一回事。改为“最早的解释线索来自研究不确定性下行为的早期文献里提出的‘小数问题’”。
    - 其余几条：“the camouflage of the properties comes into play” 改为“分布的性质会被掩盖起来”；“the debate is bitter not because of large divergences of opinions but because of small ones” 改为“这场论战吵得这么凶，起因却只是意见上的一点小分歧”；Ingersoll 那本书 “like the personality of its author” 改为“就跟作者的为人一样”；“Two strains of literature” 改为“有两类文献”；“One observation about philosophers” 改为“我注意到一点”；“does not provide them with such luxury” 改为“用帕累托-莱维分布，他们可就享受不到这种奢侈了”。
  - 不采纳的：没有。审校提出的每一条都能在英文里找到依据，改动后的中文也更准确或更好读。
- 审校者的总体判断：译文整体质量高，可以进入中文通读。154 个块逐块对齐，数字、金额换算、年份和百分比都和原文一致；文献引用照写英文，主题词的引导语都译了；人名和 people-zh.tsv 一致，每人首次出现都括注了英文；全文没有破折号和禁用句式；粗体主题词把冒号放在粗体外面是渲染的需要，做法合理。需要改的是三处意思偏差、一处疑似原文笔误、几处和其他章节或术语表不一致的术语，以及几处读起来会卡住的句子。

## 3. 中文通读

- 执行者：编辑 agent（Opus 5.5）。
- 范围：采纳审校意见以后，从标题到译者注顺着中文读完全节，看连贯、重复、指代、人名和术语前后是否一致。
- 发现并修改（5 处，每一处都回查了英文）：
  - 第 4 章「公共知识分子与科学知识分子」：“开设了培养公共知识分子的博士学位，培养的是文学知识分子”连用两个“培养”。英文在 “a Ph.D. to become a public intellectual” 后面补了一个 “literary”，后半句改为“这里说的是文学知识分子”。
  - 第 7 章「古德曼的归纳之谜」：改过的“照这个理论”和后面的 “Accordingly, by such logic”（照这种逻辑）挨得太近，前一处改为“按这个理论”；末句 “It confirms that we are observing a rising-crashing market.” 原译“它证实的是，我们观察到的是……”连用两个“是”，改为“它证实我们观察到的是一个先涨后崩的市场”。
  - 第 12 章「知识的错觉」：“人们做出的推断比数据所能支持的更强，他们把这种倾向叫作……”，“他们”紧跟在“人们”后面，读者会以为是普通人在命名。英文的 they 指 Barber and Odean，改为“两位作者把这种倾向叫作‘知识的错觉’”。
  - 第 13 章「风险价值」：“人们以为自己有办法……以为自己能从过去的数据里观察到概率分布”连用两个“以为”。英文是 “people imagine that … thinking that they were able from past data to observe the probability distributions”，后一处改为“自认为”。
- 通读中核对过、没有改的地方：人名在每节第一次出现时括注英文，之后只写中文（米尔、希勒、凯恩斯、彼得·麦克伯尼、吉仁泽、格尔德·吉仁泽等）；“行为主体”“封装性”“小数定律”和“小数问题”“幸存者偏差”“黑天鹅”在全节前后一致；“欺骗者”“领域特定”现在和第 11 章一致。
- 机械检查：`python3 scripts/site.py status fooled-by-randomness` 的 notes 一行仍是 154/154；用框架的 markdown-it 逐块渲染，没有残留的星号；全文没有破折号，也没有体例禁用的对比句式。

## 状态

- 没有未解决的意义问题。第 11 章 causal 疑为 casual 的笔误，按“通俗的介绍”译出，记在“原文疑点”里，属于疑似，等有原书纸本时可以再核对。
- 需要主会话处理的事（都不涉及意思）：
  - 术语表“核心概念”可以补上 domain-specific / domain-general 写“领域特定的 / 领域通用的”，cheater 写“欺骗者”；“常提到的书”可以补上 *Simple Heuristics That Make Us Smart* 写《简捷启发式：有限理性让我们更聪明》。
  - 术语表“体例”里粗体主题词的例子 `**后见之明偏差：**` 渲染不出来，建议改成 `**后见之明偏差**：`（译者自检“未决”第一条）。
  - 译者自检“未决”里其余几条仍待决定：芒福德文章的括注用斜体还是引号、Nozik 是否改成 Nozick、en/ 里 al-Ghazl 的乱码、[^t1] 是否保留。
  - 这一节在 `book.json` 里仍是 `todo`，需要改成 `review` 才能在阅读器里校样；第 4 节“阅读器校样”还没有做。

## 第三轮：GPT-6 Astra 独立审校

- 审校者：GPT-6 Astra，通过 Codex 运行，只读，和译者属于不同的模型家族。
- 发现：8 条。逐条找到中英文对应的句子，读过上下文后核实：成立并修改 8 条，不成立 0 条。其中第 8、26、119、124 块的四条采纳了审校的意思，换了更贴近原文的写法。
- 成立并修改：
  - 第 8 块「蒙田与笛卡尔」，“the so-called Cartesian mind corresponds to someone with an appetite for certainties”：原译“可所谓的笛卡尔式头脑，对应的却是一个渴求确定性的人”，“头脑对应一个人”搭配生硬。改为“可所谓的笛卡尔式头脑，指的却是渴求确定性的人”。审校建议的“可所谓具有笛卡尔式头脑的人，却渴求确定性”丢掉了“这个称呼指的是什么人”的意思，没有采用。
  - 第 23 块「可错性与不可错论」，皮尔士的话 “Nothing can be more completely contrary to a philosophy, the fruit of a scientific life, than infallibilism”：原译“对于一种作为科学生涯之果实的哲学来说，没有什么比不可错论更与它背道而驰了”，“作为……之果实的”这层修饰读起来拗口。改为“对于一种积一生科学工作而成的哲学来说，没有什么比不可错论更与它背道而驰了”，后半句不变。
  - 第 26 块，“Even more vicious results have been shown by researchers who studied how much people would *pay* to lower other people’s income”：原译“他们得出的结果更加恶毒”，恶毒的是研究揭示出来的行为，“结果恶毒”搭配不当。改为“他们发现的行为更加恶毒”。
  - 第 92 块「非线性动力学」，“Sornette goes beyond just characterizing the process as fat-tailed”：原译“索内特（Sornette）不只是把这个过程描述为厚尾”。术语表“只出现一两次、没有收进表里的说法”规定 fat tails 写“肥尾”，序言也写“肥尾”。改为“索内特（Sornette）不只是说这个过程具有肥尾，说它的概率分布……”。译者自检列出的新定说法里的“厚尾”随之作废。
  - 第 101 块，“Another problem is seen in Arrow’s voter’s impossibility theorem.”：原译“另一个问题见于阿罗（Arrow）的投票不可能定理。”people-zh.tsv 的说明写“阿罗不可能定理”，术语表也规定哥德尔定理这类通行的科学术语不括注人名。改为“另一个问题见于阿罗不可能定理。”
  - 第 119 块，“show evidence of a cheater detection module”：原译“这证明存在一个识别欺骗者的模块”，把“提供了证据”说成了“证明”，语气比原文强。改为“这表明存在一个识别欺骗者的模块”。
  - 第 119 块，“we adapted to the enforcement of cooperative tasks and are quick at identifying free riders”：原译“我们适应了执行合作任务，很快就能认出搭便车的人”，读者会理解成我们自己去做合作的事。enforcement 指确保每个人都尽到合作的义务，这样才和后面认出搭便车的人连得上。改为“我们已经适应了督促大家完成合作任务，很快就能认出搭便车的人”。
  - 第 124 块「享乐跑步机」，“If things do not accumulate well then it follows that humans should follow a different set of strategies.”：原译“如果事情不能很好地累积，那么人类就应该采取另一套策略。”“事情”指代空泛。前一句说的是糟糕的一天就能抹掉过去所有成功的效果，改为“如果成功的效果累积不起来，那么人类就应该采取另一套策略。”审校建议的“成功带来的满足感”比原文多了一层解释，没有采用。
- 不成立，保留原译：没有。
- 按全书统一的写法修改：1 处。另有 2 处和上面的审校发现重合（第 92 块的“肥尾”、第 101 块的“阿罗不可能定理”），记在上面。
  - 第 76 块的粗体主题词 “Goodman’s riddle of induction”：原译 `**古德曼（Goodman）的归纳之谜**`。“全书统一的写法（译完后定）”规定，带人名的说法里，这个人恰好在本节第一次出现时，英文括注放在整个说法后面，例如布里丹之驴（Buridan’s donkey）；people-zh.tsv 也写明 Goodman 只在这个说法里出现。改为 `**古德曼的归纳之谜（Goodman’s riddle of induction）**`，用框架的 markdown-it 渲染，粗体正常闭合。
  - 其余规定逐条对过，这一节已经符合：数字（一到十用汉字；“4 倍”是幂指数为 2 时算出来的比值，“6 点”是骰子的点数，照写阿拉伯数字）、书名和文章的括注（芒福德的文章括注用引号）、人名在本节第一次出现时括注英文、文献引用照抄原文的笔误（Taszka、Schleifer、Nozik、Knetch、Damasion）、粗体斜体旁边的标点、per se 写“本身”、译者注 [^t1] 的格式、take ... seriously 写“当真”或“认真对待”、evolution 写“进化”。
- 对英文原文的疑问：审校提出 4 条，都已经记在上面的“原文疑点”表里（第 52 块的 hycocampus、第 76 块的 grue、第 86 块的夏普比率和变异系数、第 94 块帕累托一段的幂次）。审校补充了两点，记在这里，译文照旧：
  - 第 76 块：古德曼给 grue 下的定义以“在时刻 *t* 之前有没有被观察过”为条件（在 *t* 之前被观察过并且是绿色，或者没有被观察过并且是蓝色），并不要求同一个东西到了 *t* 就变色。作者的说法在这一点上也和原定义不同。
  - 第 86 块：夏普比率的分子通常是相对于基准（例如无风险利率）的超额收益，变异系数是标准差除以均值。按作者自己给的定义（收益除以标准差），两者才互为倒数；按哪一种定义，两者都算不上同一个概念。
- 核实与修改：agent（Opus 5.5）。改完后运行 `python3 scripts/site.py status fooled-by-randomness`，notes 一行是 154/154，全书 28 节、1294/1294 块都已译完；用框架的 markdown-it 逐块渲染，没有残留的星号；全文没有破折号，也没有体例禁用的对比句式。
