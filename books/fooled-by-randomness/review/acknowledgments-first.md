# 第一版致谢（acknowledgments-first）审校记录

全节 8 个块，原文没有注释，中文没有加译者注；中英逐块对应（`site.py status` 显示 8/8）。

## 1. 译者自检

- 执行者：translation agent（Opus 5.5），译者本人。
- 范围：全节 8 块，对照原文逐段检查漏译、增译、否定、人名、机构名、数字和格式，名单里的人名逐个和英文核对过数目和顺序。另外运行了 `python3 scripts/site.py status fooled-by-randomness`（8/8）；在 `/tmp` 的一份副本里把本节设成草稿后构建通过；`tools/term_consistency.py` 对本节没有提示。也查过本节没有破折号、没有体例禁用的对比句式、中文里没有半角标点和嵌套括号。
- 发现并修改：
  - 第 5 块 “Genius loci (‘the spirit of the place’) and outstanding Odeon staff member Tarek Khelifi made sure that we were well taken care of … We owe him a lot.”：初稿用顿号把 genius loci 和 Tarek Khelifi 并列，读起来像两个人。原文说的是同一个人（后面用 him），改为“Tarek Khelifi 是这里的 genius loci（‘此地之灵’），也是 Odeon 的杰出员工，他总是把我们照顾得妥妥帖帖”。
  - 第 2 块 “Stan Jonas (I do not know any other designation that would do him justice)”：中文名括注英文后会接上第二组括号，所以把身份挪到名字后面：“斯坦·乔纳斯（Stan Jonas），纽约的知识分子、随机性专家（我想不出还有什么别的称呼能配得上他）”。
  - 第 2 块 “my lucid Popperian colleague Jonathan Waxman … Karl Popper’s ideas”：Popperian 出现在卡尔·波普尔全名之前，改成“他是卡尔·波普尔（Karl Popper）的信徒”，括注落在全名第一次出现的地方。
  - 第 3 块 “someone who has a passion for probability and randomness, who is obsessed with literature but happens to be a trader, rather than a generic ‘expert’”：写成“一个热爱概率和随机性的人，痴迷文学，碰巧当了交易员；他没有把我看成泛泛的‘专家’”，避开体例禁用的句式。
- 译法上的选择：
  - 人名照 people-zh.tsv：basis 写 keep 的作者亲友和同事照写英文；有中文译名的七人写中文，并在本节第一次出现时括注英文：斯坦·乔纳斯（Stan Jonas）、吉米·鲍尔斯（Jimmy Powers）、卡尔·波普尔（Karl Popper）、保罗·威尔莫特（Paul Wilmott）、弗朗切斯科·科列利（Francesco Corielli）、马克·斯皮茨纳格尔（Mark Spitznagel）、唐纳德·萨斯曼（Donald Sussman）。Myles、David 后面只写名时照原文写英文名。
  - 机构照术语表：Salomon Brothers 写“所罗门兄弟公司”，J. Wiley & Sons 写“约翰·威利父子出版公司”，Bocconi 写“博科尼大学”，Courant class 写“我库朗研究所的课”，Tribeca 写“翠贝卡”，Greenwich, Connecticut 写“康涅狄格州格林尼治”；Odeon、Empirica、Paloma Partners 照写原名，“Odeon Circle” 写“Odeon 小圈子”，“Camp Empirica” 写“Empirica 营地”。
  - 第 2 块 “probabilists are born, not made” 写“概率学家是天生的，后天培养不出来”；“the formation of ‘new’ and ‘old’ money” 写“‘新钱’和‘老钱’是怎样形成的”；“anyone can buy and sell” 写“买卖谁都会”，和第 9 章标题的意思对应；“(very long) walks” 写“散步（而且一走就是很久）”。
  - 第 3 块 “the off-the-rack publisher” 写“那些照现成模子出书的出版商”；“nonintrusive” 写“从不越俎代庖”。
  - 第 4 块 “the usual suspects” 写“照例要点名的那几位”。
  - 第 5 块 genius loci 原文不是斜体，照写，不加斜体；10 p.m. 写“晚上 10 点”。
  - 第 6 块 “a shadow copy editor” 写“在幕后担任文字编辑”；“All mistakes are mine.” 写“书中的错误全都归我”。
  - 第 7 块 “sporadic (and random) bursts of letters” 写“时不时（而且随机地）引来一阵阵来信”。
  - 第 8 块 “(I had experienced one of my best professional years while writing these lines)” 写“写下这几行字的时候，我刚刚度过了职业生涯里最好的年份之一”。
- 数字：1987 年夏天、晚上 10 点用阿拉伯数字。
- 未决：
  - 双语审校、中文通读和阅读器校样还没有做；`book.json` 里本节的状态由主会话修改。

## 2. 双语审校

- 执行者：另一个独立上下文的 agent（Opus 5.5），没有参与翻译。
- 范围：全节 8 块，逐块对照英文；同时检查了破折号、禁用句式、半角标点、人名（包括照写英文的亲友同事）、名单的人数和顺序，以及机构名。
- 发现：2 条；核实后采纳 2 条，不采纳 0 条。
  - 第 8 块 “(I had experienced one of my best professional years while writing these lines)”：原文说的是写这些文字的那段时间正好是最好的年份之一，原译“刚刚度过了”把时间推到了写作之前。采纳，改为“（写这几行字的那段时间，正是我职业生涯里最好的年份之一）”。
  - 第 8 块 “This book was written and finished after I founded Empirica”：原译“写成、完成的”意思重复。采纳；审校者建议“写完的”，现写“这本书是在我创办 Empirica 之后写成的”，保留了原句“是……之后”的结构。
- 审校者的总体判断：十个分节逐块对照英文读完，总体质量很高，可以进入中文通读。每一块都已译完，中英逐块对应；没有破折号、“不是……而是……”句式和混进中文的半角标点；写 keep 的亲友同事照写英文，名单的人数和顺序跟原文一致。没有发现事实、数字、否定或人物关系上的错误。

## 3. 中文通读

- 执行者：编辑 agent（Opus 5.5）。
- 范围：顺着中文把全节从头读到尾，看行文是否连贯、有没有重复、指代是否清楚、人名和机构名前后是否一致。每一处改动都回查了英文。
- 发现并修改：
  - 第 8 块 “after I founded Empirica, my intellectual home, ‘Camp Empirica,’ in the woods in the back country of Greenwich, Connecticut”：原译“Empirica 是我精神上的家，‘Empirica 营地’，坐落在……”把两个名称直接并列，读不出它们的关系；原文里 “Camp Empirica” 是同一个地方的另一个叫法，加上“也就是”。
  - 第 8 块 “all the like-minded people who helped fuel the stimulating atmosphere there”：原译“帮着营造那里那种激发灵感的气氛的人”，“那里那种”拗口，改为“帮着营造出那里激发灵感的气氛的人”。
- 核对过的地方：第 4 块 18 人、第 6 块 8 人加 Erik Stettler、第 8 块 6 人加 Paloma Partners 的两人，人数和顺序都和英文一致；斯坦·乔纳斯、吉米·鲍尔斯、卡尔·波普尔、保罗·威尔莫特、弗朗切斯科·科列利、马克·斯皮茨纳格尔、唐纳德·萨斯曼只在第一次出现时括注英文；Odeon、Empirica、Paloma Partners 照写原名。改完后没有破折号、禁用句式和半角标点，`site.py status` 仍显示 8/8。

## 状态

- 没有未解决的意义问题。
- 阅读器校样还没有做；`book.json` 里本节的状态由主会话修改。
