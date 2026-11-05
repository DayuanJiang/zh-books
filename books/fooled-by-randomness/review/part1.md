# 第一部分 梭伦的警告（part1）审校记录

全节 6 个块，原文没有注释，中文没有加译者注；中英逐块对应（`site.py status` 显示 6/6）。

## 1. 译者自检

- 执行者：translation agent（Opus 5.5），译者本人。
- 范围：全节 6 块，对照原文逐段检查漏译、增译、否定、条件、数字、人名、术语和格式。另外运行了 `python3 scripts/site.py status fooled-by-randomness`（6/6）；在 `/tmp` 的一份副本里把本节设成草稿后构建通过；`tools/term_consistency.py` 对本节没有提示。也查过本节没有破折号、没有体例禁用的对比句式、中文里没有半角标点和嵌套括号。
- 发现并修改：
  - 第 5 块 “that which came with the help of luck could be taken away by luck (and often rapidly and unexpectedly at that)”：初稿括号里写“来得又快又突然”，动词用错了，这里说的是被运气拿走，改为“拿得又快又出人意料”。
  - 第 3 块 “he gave similar examples of heroic but terminated lives”：初稿想写“早早结束的人生”，原文没有“早”的意思（梭伦的意思是这些人生已经走完，可以下定论了），改为“英勇、但已经结束了的人生”。
  - 第 5 块 “Part I is concerned with the degree to which a situation may yet, in the course of time, suffer change”：初稿给“随着时间的推移，仍然可能发生变化”加了引号，原文没有引号，去掉引号后把句子理顺为“随着时间的推移，一种处境仍然可能发生多大的变化”，措辞和梭伦那段话的译法保持一致。
  - 第 5 块 “the goddess Fortuna—Jupiter’s firstborn daughter”：括注英文名后会出现嵌套括号，改成分句“福尔图娜是朱庇特（Jupiter）的长女”。
- 译法上的选择：
  - 副标题 *Skewness, Asymmetry, Induction* 照术语表写“偏态、不对称、归纳”。
  - 第 3 块梭伦的话里，作者用方括号补的 [guaranteed] 写“［保证］”，保留方括号；“Romance languages” 写“罗曼语族的语言”。
  - 第 4 块 “it ain’t over until it’s over” 照体例写“不到最后，不算结束”；“it ain’t over until the fat lady sings” 写“胖女人还没开唱，戏就不算完”；“historical facts that benefited from the imagination of the chroniclers” 是反讽，照字面译作“得益于编年史家想象力的历史事实”，不加引号。
  - 第 5 块 the problem of induction、*black swan*、*rare event*、*skewness* 照术语表写“归纳问题”“*黑天鹅*”“*稀有事件*”“*偏态*”，保留斜体；“more resistant to randomness” 写“更经得起随机性”。
  - 第 6 块 “(something like)” 写“（大意是）”；“People were thoughtful at that time.” 写“那个时代的人懂得深思”。
- 人名：和 `review/terms/people-zh.tsv` 逐个核对过，每人在本节第一次出现时括注英文：克罗伊斯（Croesus）、梭伦（Solon）、约吉·贝拉（Yogi Berra）、命运女神福尔图娜（Fortuna）、朱庇特（Jupiter）、居鲁士（Cyrus）。标题里的“梭伦的警告”不括注。
- 数字：三个世纪按十以内的数用汉字。
- 未决：
  - 第 6 块的 “Solon’s warning” 照术语表写“梭伦的警告”；梭伦的英文括注在第 3 块他第一次单独出现的地方。
  - 双语审校、中文通读和阅读器校样还没有做；`book.json` 里本节的状态由主会话修改。

## 2. 双语审校

- 执行者：另一个独立上下文的 agent（Opus 5.5），没有参与翻译。
- 范围：全节 6 块，逐块对照英文；同时检查了破折号、禁用句式、半角标点、人名括注和术语。
- 发现：0 条；核实后采纳 0 条，不采纳 0 条。审校者对本节没有提出问题。
- 审校者的总体判断：十个分节逐块对照英文读完，总体质量很高，可以进入中文通读。每一块都已译完，中英逐块对应；没有破折号、体例禁用的对比句式和混进中文的半角标点；人名和 people-zh.tsv 一致，术语用的都是术语表的译法。没有发现事实、数字、否定或人物关系上的错误。

## 3. 中文通读

- 执行者：编辑 agent（Opus 5.5）。
- 范围：顺着中文把全节从头读到尾，看行文是否连贯、有没有重复、指代是否清楚、人名和术语前后是否一致。改动回查了英文。
- 发现并修改：
  - 第 5 块 “Part I is concerned with the degree to which a situation may yet, in the course of time, suffer change. For we can be tricked by situations involving mostly the activities of the goddess Fortuna”：原译第二句以“因为”开头单独成句，读起来像半句话；改为用逗号接在上一句后面：“……一种处境仍然可能发生多大的变化，因为有些处境主要是命运女神福尔图娜（Fortuna）在起作用，我们可能会被它们蒙骗”。
- 核对过的地方：梭伦的警告、黑天鹅、稀有事件、偏态、归纳问题的写法和序章一致；克罗伊斯、梭伦、约吉·贝拉、福尔图娜、朱庇特、居鲁士都只在第一次出现时括注英文；第 5 块转述梭伦答话的那句和第 3 块的引文用的是同一种措辞（“随着时间的推移，仍然可能发生变化”）。改完后没有破折号、禁用句式和半角标点，`site.py status` 仍显示 6/6。

## 状态

- 没有未解决的意义问题。
- 阅读器校样还没有做；`book.json` 里本节的状态由主会话修改。

## 第三轮：GPT-6 Astra 独立审校

- 审校者：GPT-6 Astra，通过 Codex 运行，只读，和译者属于不同的模型家族。
- 发现：2 条。逐条找到中英文对应的句子，读过上下文后核实：成立并修改 2 条，不成立 0 条。
- 成立并修改：
  - 第 5 块 “that which came with the help of luck could be taken away by luck”：could 说的是可能性，原译“也会”读起来像必然如此。旧译“靠运气得来的东西，也会被运气拿走”，新译“靠运气得来的东西，也可能被运气拿走”。后面括号里的“（而且往往拿得又快又出人意料）”不变。
  - 第 3 块 “he gave similar examples of heroic but terminated lives”：原译照搬英文的修饰结构，顿号后面接“但”也不合中文习惯。旧译“梭伦又举了几个类似的例子，都是英勇、但已经结束了的人生”，新译“梭伦又举了几个类似的例子，这些人活得英勇，但都已离世”。审校者建议写“这些人一生英勇”，前一句已经两次用到“一生”（“一个人的一生”“此人一生高尚”），所以这里写“活得英勇”。
- 不成立，保留原译：无。
- 按全书统一的写法修改：0 处。逐条对照过：数字（“三个世纪”用汉字）；人名括注（六个人都在本节第一次出现时括注英文，第 6 块的“梭伦的警告”出现时梭伦已经在第 3 块括注过，不再括注）；“命运女神福尔图娜”照 people-zh.tsv 的说明写；斜体旁边的标点放在星号外面；“不到最后，不算结束”照体例写。本节没有外文词、书名、译者注，也没有“当真”“姐夫”“进化”这类固定说法，这些条目都已经符合。
- 对英文原文的疑问：第 3 块梭伦答话里的 “with all variety of future” 和前半句的 future 重复，搭配也不通。作者引的是德莱顿（Dryden）译、克拉夫（Clough）修订的普鲁塔克《梭伦传》，这个译本在 MIT Internet Classics Archive 上的文本写作 “with every possible variety of fortune”，所以书里的 future 可能是 fortune 之误。美国国会图书馆网站为本书登记的样章也写作 “with all variety of future”，说明印刷版本来就是这样，导入 EPUB 时没有出错。中文照原文译作“未来有着形形色色的变化”，按 fortune 来读也讲得通，所以保留原译；全书统一的写法规定，原文和上下文矛盾、读者对照时会看到两边意思相反才加译者注，这一处够不上，不加。
- 核实与修改：agent（Opus 5.5）。改完后运行 `python3 scripts/site.py status fooled-by-randomness`，part1 显示 6/6，原文没有注释；`tools/term_consistency.py` 对本节没有提示；本节仍然没有破折号、体例禁用的对比句式和混进中文的半角标点。
