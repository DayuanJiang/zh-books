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
- 审校者的总体判断：十个分节逐块对照英文读完，总体质量很高，可以进入中文通读。每一块都已译完，中英逐块对应；没有破折号、“不是……而是……”句式和混进中文的半角标点；人名和 people-zh.tsv 一致，维特根斯坦的尺子、条件信息、先验这些术语都用了术语表的译法。没有发现事实、数字、否定或人物关系上的错误。需要处理的是少数翻译腔偏重的句子，都属于局部修改。

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
