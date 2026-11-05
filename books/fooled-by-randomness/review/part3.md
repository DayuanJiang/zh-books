# 第三部分 我耳朵里的蜡（part3）审校记录

全节 19 个块，原文没有注释，中文没有加译者注；中英逐块对应（`site.py status` 显示 19/19）。

## 1. 译者自检

- 执行者：translation agent（Opus 5.5），译者本人。
- 范围：全节 19 块，对照原文逐段检查漏译、增译、否定、条件、数字、人名、术语和格式。另外运行了 `python3 scripts/site.py status fooled-by-randomness`（19/19）；在 `/tmp` 的一份副本里把本节设成草稿后构建通过，第 14 块的亚马逊链接正常；`tools/term_consistency.py` 对本节没有提示。也查过本节没有破折号、没有体例禁用的对比句式、中文里没有半角标点和嵌套括号。
- 发现并修改：
  - 第 8 块 “(recall Popper the man)”：括注英文名后会出现嵌套括号，改成句子“想想波普尔（Popper）这个人就知道了”。
  - 第 13 块 “This mechanism I also call Wittgenstein’s ruler”：初稿想把括注写在人名后面，成了“维特根斯坦（Wittgenstein）的尺子”，这样会把术语拆开，改为“维特根斯坦的尺子（Wittgenstein’s ruler）”，人名和术语一起括注。
  - 第 3 块 “I find the most spectacular use of such guile was against no other opponent than himself”：初稿“对手不是别人，正是他自己”用了体例不允许的句式，改为“对付的恰恰是他自己”。
  - 第 13 块开头的问句 “What is the mechanism that should convince authors to avoid reading comments on their work, except for those they solicit from specified persons for whom they have intellectual respect?”：初稿把“机制”放在句首，问句太长，改为先讲作者该怎么做，再问“让作者信服这一点的是什么机制”。
- 译法上的选择：
  - 副标题 *Living with Randomitis* 照术语表写“与随机病共处”。
  - 小标题：I Am Not So Intelligent 写“我没那么聪明”；Wittgenstein’s Ruler 写“维特根斯坦的尺子”；The Odyssean Mute Command 写“奥德修斯式的静音键”。
  - 第 4 块 Charybdis、Scylla、the sirens 不在 people-zh.tsv 里，用《奥德赛》中译本通行的“卡律布狄斯”“斯库拉”“塞壬”，前两个括注英文，塞壬是常见的名字，没有括注；Book 12 写“第 12 卷”。
  - 第 10 块 “I try to imagine that the other person is a Martian, rather than a human being” 写“把对方想象成一个火星人，别把他当人类”；“sports utility vehicle” 写“SUV”；“people in large trucks” 写“坐在大卡车里的人”。
  - 第 11 块结尾的短语 “Wax in my ears.” 补成一句“这就是我耳朵里的蜡。”，和本部分标题一致。
  - 第 13 块 conditional information 写“条件信息”，*prior* 写“*先验*”，“ten sigma” 写“十西格玛”，都照术语表。
  - 第 14 块链接 [Amazon.com](http://amazon.com) 的链接文字写“亚马逊”，链接地址不变；“forensic expert” 写“法医专家”。
  - 第 17 块 “murdering rigor” 写“扼杀严谨”；CEO 写“首席执行官”；“We are visually but not auditorily intimidated” 写“我们在视觉上被震慑住了，在听觉上却没有”；*Treatise on Laughter* 照术语表写《笑》并括注原题；pundits 写“权威评论员”。
  - 第 18 块 “a built-in bias, here prejudice” 写“一种与生俱来的偏差（这里是偏见）”。
- 人名：和 `review/terms/people-zh.tsv` 逐个核对过，每人在本节第一次出现时括注英文：奥德修斯（Odysseus）、喀耳刻（Circe）、波普尔（Popper）、维特根斯坦（Wittgenstein，和术语一起括注）、O. J. 辛普森（O. J. Simpson）、亨利·柏格森（Henri Bergson）、格雷厄姆·格林（Graham Greene）。Homerian 照表写“荷马史诗里的”。
- 未决：
  - Charybdis、Scylla、sirens 的译名请主会话决定是否补进术语表或 people-zh.tsv。
  - 双语审校、中文通读和阅读器校样还没有做；`book.json` 里本节的状态由主会话修改。

## 原文疑点

| 位置 | 原文 | 处理 |
| --- | --- | --- |
| 第 13 块 | The less you trust the ruler‘s reliability (in probability called the *prior*),the more information | 两处排印问题：ruler‘s 用了左单引号，“*prior*),the” 少了一个空格。不影响意思，`en/` 不改，中文照常译 |
| 第 17 块 | his famous description of the gap between the seriousness of a gentleman about to walk on a banana skin and the comical aspect of the situation | 疑似。柏格森《笑》里的例子是一个在街上奔跑的人绊了一跤、摔倒在地，我记得书里没有香蕉皮；香蕉皮可能是作者的发挥。没有核对原书，照原文译 |

## 2. 双语审校

- 执行者：另一个独立上下文的 agent（Opus 5.5），没有参与翻译。
- 范围：全节 19 块，逐块对照英文；同时检查了破折号、禁用句式、半角标点、人名括注、术语和第 14 块的链接。
- 发现：2 条；核实后采纳 2 条，不采纳 0 条。两条的问题都属实，措辞都另作了调整。
  - 第 13 块开头的问句 “What is the mechanism that should convince authors to avoid reading comments on their work, except for those they solicit from specified persons for whom they have intellectual respect?”：原译先摆出一长串结论，最后才用“这一点”回指并发问，要读到结尾才知道问的是什么。审校者建议写“有什么机制能让作者相信：……”，这样问的就变成了“有没有这样的机制”，下一句“这个机制是……”接得不够紧。现改为“是什么机制让作者有理由不去读别人对自己作品的评论，只看自己向某些在智识上敬重的特定人士征求来的意见？”，句首就点明问的是机制，和下一句直接衔接。
  - 第 17 块 “But this did not come without tricks.”：原译“这可不是不靠花招就能做到的”照搬了英文的双重否定。审校者建议“这得靠一些花招才做得到”；原文是过去时，说的是作者已经戒掉了电视，所以写成“不过，这是靠了一些花招才做到的”。
- 审校者的总体判断：十个分节逐块对照英文读完，总体质量很高，可以进入中文通读。每一块都已译完，中英逐块对应；没有破折号、体例禁用的对比句式和混进中文的半角标点；人名和 people-zh.tsv 一致，维特根斯坦的尺子、条件信息、先验这些术语都用了术语表的译法。没有发现事实、数字、否定或人物关系上的错误。需要处理的是少数翻译腔偏重的句子，都属于局部修改。

## 3. 中文通读

- 执行者：编辑 agent（Opus 5.5）。
- 范围：顺着中文把全节从头读到尾，看行文是否连贯、有没有重复、指代是否清楚、人名和术语前后是否一致。每一处改动都回查了英文。
- 发现并修改：
  - 第 8 块 “my emotions will respond to a different set of calculations”：“作出反应”改为“做出反应”，和本节第 14 块的“做出有效推断”、第二部分的“做出不明智的反应”写法一致。
  - 第 11 块 “I will do the same with unsolicited comments on this book.”：“对这本书的不请自来的评论”两个“的”挨得太近，删去前一个，写“对这本书不请自来的评论”。
- 核对过的地方：guile 写“计谋”，ruse 写“计策”，tricks 写“花招”或“小花招”，全节前后一致，和序章“狡猾的小花招”也对得上；维特根斯坦的尺子、条件信息、先验、十西格玛和术语表一致；奥德修斯、喀耳刻、波普尔、O. J. 辛普森、柏格森、格林都只在第一次出现时括注英文。改完后没有破折号、禁用句式和半角标点，`site.py status` 仍显示 19/19。

## 状态

- 没有未解决的意义问题。第 17 块香蕉皮一事是译者记下的疑似出入，照原文译，不影响译文。
- 留给主会话的事项：卡律布狄斯、斯库拉、塞壬是否补进术语表（见译者自检的未决事项）；阅读器校样还没有做；`book.json` 里本节的状态由主会话修改。

## 第三轮：GPT-6 Astra 独立审校

- 审校者：GPT-6 Astra，通过 Codex 运行，只读，和译者属于不同的模型家族。
- 发现：5 条。逐条找到中英文对应的句子，读过上下文后核实：成立并修改 5 条，不成立 0 条。其中四条的改法和审校者建议的措辞不同，原因写在各条里。
- 成立并修改：
  - 第 14 块 “The information from an anonymous reader on [Amazon.com](http://amazon.com) is all about the person, while that of a qualified person, is going to be all about the book.”：原译“亚马逊上一位匿名读者给出的信息，说的全是这个人自己；一位够格的人给出的信息，说的才全是这本书。”“说的”容易读成书评的内容在谈书评人自己，作者的意思是读者从这种信息里能推知的全是这个人的情况。现改为“亚马逊上一位匿名读者给出的信息，反映的全是这个人自己；一位够格的人给出的信息，反映的才全是这本书。”审校者建议前半句写“透露的全是关于这个人本人的信息”，后半句写“反映的才全是书本身的情况”，意思对，可是前后两半换了动词，句子也长了，所以两半都用“反映”。
  - 第 4 块 “The indescribable beauty of the sirens’ songs is contrasted with the moldering corpses of sailors who strayed into the area around them.”：原译“塞壬的歌声美得无法形容，和闯进她们周围海域的水手那些正在腐烂的尸体形成对照。”定语很长，“那些”夹在“水手”和“尸体”中间，读到这里要回头重新断句。现改为“塞壬的歌声美得无法形容，和它形成对照的，是那些误入她们周围海域的水手正在腐烂的尸体。”strayed 也从“闯进”改成更贴切的“误入”。审校者建议写成“已成了正在腐烂的尸体，两者形成鲜明对照”，多了原文没有的“鲜明”，所以没有照用。
  - 第 7 块 “The epiphany I had in my career in randomness came when I understood that I was not intelligent enough, nor strong enough, to even try to fight my emotions.”：原译“在和随机性打交道的职业生涯里，我的顿悟来自我明白了一件事：我既不够聪明，也不够坚强，连跟自己的情绪斗一斗都不够格。”顿悟和明白说的是同一件事，“来自”把两者写成了因果，两个“我”挨着，句子拖沓。现改为“在和随机性打交道的职业生涯里，我有过一次顿悟：我明白了自己既不够聪明，也不够坚强，连跟自己的情绪斗一斗都不够格。”前半句用了审校者建议的“我有过一次顿悟”，冒号后面加上“我明白了”，保留 understood 的意思。
  - 第 13 块 “A book review, good or bad, can be far more descriptive of the reviewer than informational about the book itself.”：原译“一篇书评，不管是好评还是差评，描述书评人的成分可能远远多于提供的关于这本书本身的信息。”拿“成分”和“信息”比多少，比较的两边对不上。现改为“一篇书评，不管是好评还是差评，透露的关于书评人的信息，可能远远多于它提供的关于这本书本身的信息。”两边比的都是信息，“透露”也和前一句“一句话透露的关于说话人自己的东西”呼应。“书评人”沿用本节原来的写法，没有换成审校者建议的“评论者”。
  - 第 19 块 “This part, the conclusion of this book, presents the human aspect of dealing with uncertainty.”：原译“这一部分是全书的结尾，讲的是应对不确定性时人的一面。”“人的一面”所指不清，“时人”两个字连在一起还可能读错。现改为“讲的是应对不确定性时人性的一面”。审校者建议改成“从人性的角度探讨如何应对不确定性”，把 presents the human aspect 写成了讨论问题的角度，离原文远一些，所以保留原句的结构，把“人的一面”换成“人性的一面”。
- 不成立，保留原译：无。
- 按全书统一的写法修改：1 处。
  - 第 13 块 “*Unless you have confidence in the ruler’s reliability, if you use a ruler to measure a table you may also be using the table to measure the ruler.*”：原来写 `*除非你对尺子的可靠性有信心，否则你用尺子量桌子，可能也是在用桌子量尺子。*你越不信任`，斜体以句号结尾、后面紧跟汉字，CommonMark 闭合不了。用构建脚本所用的 markdown-it-py 试过，原写法会把“你越不信任尺子的可靠性（在概率论里叫作”错配成斜体，“先验”反而成了正体。按“粗体、斜体旁边的标点”一条，把句号移到斜体外面，写成 `*……可能也是在用桌子量尺子*。你越不信任`。改后全节渲染出 5 处斜体，页面上没有残留的星号。
  - 其他各条逐一对过，本节已经符合：our predisposition to take information seriously 写“我们把信息当真的倾向”；人名每人在本节第一次出现时括注英文，维特根斯坦的尺子把括注放在整个说法后面；《奥德赛》《笑》第一次出现时括注斜体原题；“第 12 卷”“一纳秒”“十西格玛”符合数字的写法；taking themselves seriously 写“把自己当回事”，和第 9 章同一说法的写法一致；Homerian 照 people-zh.tsv 写“荷马史诗里的”，和第 11 章一样不括注。
- 对英文原文的疑问：审校者没有提出。译者自检记下的两处（第 13 块 ruler‘s 的引号和 “*prior*),the” 少的空格，第 17 块柏格森的香蕉皮）仍照原文译，见上面的原文疑点表。
- 核实与修改：agent（Opus 5.5）。改完后运行 `python3 scripts/site.py status fooled-by-randomness`，part3 显示 19/19 块已译，本节没有注释；全书 1294/1294 块已译。也查过改后的本节没有破折号、没有体例禁用的对比句式、中文里没有混进半角标点。
