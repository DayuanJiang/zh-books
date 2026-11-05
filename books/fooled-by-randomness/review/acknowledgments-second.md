# 修订第二版致谢（acknowledgments-second）审校记录

全节 11 个块，原文没有注释，中文没有加译者注；中英逐块对应（`site.py status` 显示 11/11）。

## 1. 译者自检

- 执行者：translation agent（Opus 5.5），译者本人。
- 范围：全节 11 块，对照原文逐段检查漏译、增译、否定、比较、人名、机构名、数字和格式，名单里的人名逐个和英文核对过数目和顺序。另外运行了 `python3 scripts/site.py status fooled-by-randomness`（11/11）；在 `/tmp` 的一份副本里把本节设成草稿后构建通过；`tools/term_consistency.py` 对本节没有提示。也查过本节没有破折号、没有体例禁用的对比句式、中文里没有半角标点和嵌套括号。
- 发现并修改：
  - 第 5 块 “a matter that makes an extra edition of an existing book far more likely to break through the critical point than a new one”：初稿漏了 far，补成“远比一本新书更有可能突破临界点”。
  - 第 5 块括号里的长旁白 “(he tried to convince me to not do this second edition, I begged him to do a second one of his own *Irrational Exuberance*, be it only for my own consumption; I think that I won both points)”：书名括注原题后会出现嵌套括号，所以去掉外层括号，改成独立的句子，内容不变。
  - 第 3 块 “Somehow there was the *pre-* and *post-Fooled* life.”：Fooled 指这本书，照体例写《随机漫步的傻瓜》，斜体落在“*之前*”“*之后*”上。
  - 第 9 块 “Sole Marittimi (now Riley)”：原文没有说改姓的原因，初稿想写“现在随夫姓 Riley”，改为“现在姓 Riley”。
  - 第 9 块 “another Levantine-tradder-mathematician-physicist-turned-philosopher-of-science-probability-markets (though without the neurobiology)”：拆成“又是一位黎凡特人，交易员、数学家、物理学家出身，后来转行成了研究科学、概率和市场的哲学家（不过没有神经生物学这一项）”。“another” 说的是作者自己也是这样的人，中文用“又是一位”表达。
- 译法上的选择：
  - 小标题：Out of the Library 写“走出图书馆”；Shrinking the World 写“世界变小了”；Thank You, Google 写“谢谢你，谷歌”。
  - 第 3 块 “plain library-ratting” 写“单纯泡图书馆”，和小标题对应；“While the acknowledgments for the first edition hold more than ever” 写“第一版的致谢如今比以往任何时候都更作数”。
  - 第 5 块 heuristic、critical point、network externalities、informational cascades 照术语表写“启发式”“临界点”“网络外部性”“信息瀑布”；“fare incrementally better in their second editions than brand-new ones” 写“出到第二版时，会比全新推出的东西表现得更好，而且优势逐步递增”；“crash theorist” 写“研究崩盘的理论家”。
  - 第 6 块 “the Nobel medal” 写“那枚诺贝尔奖章”，“the other recent Nobel economists” 照全书统一的写法写“近来其他几位诺贝尔经济学奖得主”；*His work matters* 写“*他的研究很重要*”，*real* 写“*真正*”，保留斜体；（a）（b）用全角括号；“Now understanding happiness is a *real* pursuit.” 写“而理解幸福，才是*真正*值得追求的事”。
  - 第 7 块 “the shibboleth” 写“一句暗号”；“suspiciously unnoticed work” 写“那项不受注意得可疑的研究”；“performance differential” 写“业绩之间的差异”；“illusionary causes in economic development” 写“在经济发展问题上，随机性让人看到了一些虚幻的原因”。
  - 第 10 块 Courant Institute of Mathematical Sciences 照术语表写“库朗数学科学研究所”；*employees* 写“*员工*”，保留斜体；“cut-throat” 写“你死我活”。
  - 书名照样章的做法括注原题：《平面国》（*Flatland*）、《非理性繁荣》（*Irrational Exuberance*）、《卑鄙的基因》（*Mean Genes*）。Borders Books 照术语表写“博德斯书店”，Google 写“谷歌”。
- 人名：照 people-zh.tsv。basis 写 keep 的作者亲友、同事和学者照写英文；有中文译名的人写中文，并在本节第一次出现时括注英文：罗伯特·希勒（Robert Shiller）、迪迪埃·索内特（Didier Sornette）、丹尼尔·卡尼曼（Daniel Kahneman）、阿莫斯·特沃斯基（Amos Tversky）、特里·伯纳姆（Terry Burnham）、彼得·麦克伯尼（Peter McBurney）、马尔科姆·格拉德威尔（Malcolm Gladwell）、阿特·德瓦尼（Art De Vany）、威廉·伊斯特利（William Easterly）、杰克·施瓦格（Jack Schwager）、保罗·威尔莫特（Paul Wilmott）、马克·斯皮茨纳格尔（Mark Spitznagel）、唐纳德·萨斯曼（Donald Sussman）。
- 数字：23 个世纪、20 年前、第 10 章用阿拉伯数字；两次晚饭、一个世纪用汉字。
- 未决：
  - 双语审校、中文通读和阅读器校样还没有做；`book.json` 里本节的状态由主会话修改。

## 原文疑点

| 位置 | 原文 | 处理 |
| --- | --- | --- |
| 第 9 块 | another Levantine-tradder-mathematician-physicist-turned-philosopher-of-science-probability-markets | tradder 是 trader 的笔误。`en/` 不改，中文按 trader 译作“交易员” |

## 2. 双语审校

- 执行者：另一个独立上下文的 agent（Opus 5.5），没有参与翻译。
- 范围：全节 11 块，逐块对照英文；同时检查了破折号、禁用句式、半角标点、人名（包括照写英文的亲友同事）、名单的人数和顺序、术语和数字。
- 发现：3 条；核实后采纳 3 条，不采纳 0 条。其中 1 条问题属实，措辞另作了调整。
  - 第 5 块 “leaving him with the muffins and other unfashionable food (and nothing to drink)”：原译“（而且没什么可喝的）”容易理解成“没什么好喝的”；原文是一点喝的也没留给他，因为咖啡和水都被作者喝了。采纳，改为“（一点喝的也没给他留）”。
  - 第 5 块 “network externalities make religions and fads fare incrementally better in their second editions than brand-new ones”：incrementally better 说的是第二版比全新的东西多占一份优势，原译“而且优势逐步递增”另外加进了优势随时间扩大的意思。采纳，改为“会比全新推出的东西多占一些优势”。
  - 第 7 块 “Ramaswami Ambarish and Lester Siegel showed me (with their suspiciously unnoticed work) that …”：原译“不受注意得可疑的研究”不合中文语法。问题属实。审校者建议把说明放进括号，插在长句中间；现在把它拆成前一个分句：“Ramaswami Ambarish 和 Lester Siegel 有一项研究，一直没人注意，冷落得让人起疑；他们用这项研究向我表明：……”，后面那句长的结论读起来不再被括号打断。
- 审校者的总体判断：十个分节逐块对照英文读完，总体质量很高，可以进入中文通读。每一块都已译完，中英逐块对应；没有破折号、“不是……而是……”句式和混进中文的半角标点；写 keep 的亲友同事照写英文，名单的人数和顺序跟原文一致；网络外部性、信息瀑布、临界点这些术语和 23 个世纪这类数字都正确。没有发现事实、数字、否定或人物关系上的错误。

## 3. 中文通读

- 执行者：编辑 agent（Opus 5.5）。
- 范围：顺着中文把全节从头读到尾，看行文是否连贯、有没有重复、指代是否清楚、人名和术语前后是否一致；审校带来的三处改动连同上下文回查了英文。
- 发现并修改：通读没有发现需要再改的地方。
- 核对过的地方：启发式、临界点、网络外部性、信息瀑布、诺贝尔经济学奖得主的写法和术语表一致；第 9 块名单 14 人，人数和顺序和英文一致；Jamil Baz、David Wilson、Myles Thompson、Jim Gatheral、Tom Witz 的写法和第一版致谢一致；保罗·威尔莫特、马克·斯皮茨纳格尔、唐纳德·萨斯曼在本节第一次出现时括注英文。改完后没有破折号、禁用句式和半角标点，`site.py status` 仍显示 11/11。

## 状态

- 没有未解决的意义问题。
- 阅读器校样还没有做；`book.json` 里本节的状态由主会话修改。
