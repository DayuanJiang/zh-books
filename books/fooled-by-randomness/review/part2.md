# 第二部分 打字机前的猴子（part2）审校记录

全节 14 个块，原文没有注释，中文没有加译者注；中英逐块对应（`site.py status` 显示 14/14）。

## 1. 译者自检

- 执行者：translation agent（Opus 5.5），译者本人。
- 范围：全节 14 块，对照原文逐段检查漏译、增译、否定、条件、数字、人名、术语和格式。另外运行了 `python3 scripts/site.py status fooled-by-randomness`（14/14）；在 `/tmp` 的一份副本里把本节设成草稿后构建通过；`tools/term_consistency.py` 对本节没有提示。也查过本节没有破折号、没有体例禁用的对比句式、中文里没有半角标点和嵌套括号。
- 发现并修改：
  - 第 4 块 “Think about the monkey showing up at your door with his impressive past performance”：初稿写“过往业绩”。术语表里 past performance 写“过去的表现”，track record 才写“过往业绩”，同一段前面也用了“过去的表现”，改为“带着骄人的过去表现”。
  - 第 8 块 “(perhaps Casanova’s *Memoirs of My Life*)”：初稿写“比如”，原文是 perhaps，改为“打出来的也许是卡萨诺瓦（Casanova）的《我的一生》”。原文的括号紧跟在“某部名著”后面，中文括注书名原题后会嵌套括号，所以挪到句末，写成分句。
  - 第 8 块 “some well-known (but unspecified) piece of work”：unspecified 指事先不指定是哪一部（猴子多到这个程度，打出随便哪一部名著都不稀奇），写“（事先并不指定是哪一部）”。
  - 第 9 块 “to calculate, instead of the probability of success, the conditional probability of successful runs given the number of investors in operation over a given market history”：原文用 instead of 作对比，改写为“再据此计算：在一段给定的市场历史里，考虑到参与其中的投资者人数，出现连续成功的条件概率是多少，用它来代替单纯的成功概率”。
  - 第 11 块 “We do not respond to probability, but to society’s assessment of it.”：写成“我们对概率本身没有反应，只对社会怎样评估概率有反应”，避开体例禁用的句式。
- 译法上的选择：
  - 副标题 *Survivorship and Other Biases* 照术语表写“幸存者偏差及其他偏差”。
  - 小标题：It Depends on the Number of Monkeys 写“要看有多少只猴子”；Vicious Real Life 写“凶险的现实生活”；This Section 写“这一部分”。
  - 第 3 块 “clap away” 写“噼里啪啦地乱敲”；“Such probability is ridiculously low” 照原文写“这种概率低得可笑”（指一只猴子打出《伊利亚特》的概率）。
  - 第 5 块 “beware the middlebrow” 照术语表写“当心半吊子”；Track records 写“过往业绩”；“such a successful run” 写“这种连续成功”。
  - 第 8 块 “a billion to the power one billion” 写“10 亿的 10 亿次方”。
  - 第 14 块 (a)(b)(c) 写全角的（a）（b）（c）；作者用的章名简称 “Too Many Millionaires”“Fry an Egg”“Loser Takes All” 写“百万富翁太多了”“煎蛋”“输家通吃”，和各章标题的译法对应；“a.k.a. monkeys on a typewriter” 写“又叫打字机前的猴子”。
  - 书名照样章的做法，常见的书也在本节第一次出现时括注原题：《伊利亚特》（*Iliad*）、《奥德赛》（*Odyssey*）、《我的一生》（*Memoirs of My Life*）、《濒临失衡的地球》（*Earth in the Balance*）。
- 人名：和 `review/terms/people-zh.tsv` 核对过：卡萨诺瓦（Casanova）、阿尔·戈尔（Al Gore）、尼禄·图利普（Nero Tulip）。
- 数字：五只猴子、两个因素用汉字；第 8 章、第 9 章、第 10 章、第 11 章和“10 亿”用阿拉伯数字。
- 未决：
  - 双语审校、中文通读和阅读器校样还没有做；`book.json` 里本节的状态由主会话修改。

## 原文疑点

| 位置 | 原文 | 处理 |
| --- | --- | --- |
| 第 14 块 | (Chapter 11, “Randomness and Our Brain”) | 第 11 章的标题是 “Randomness and Our Mind: We Are Probability Blind”，这里写成了 Our Brain。前面两处（“Too Many Millionaires”“Fry an Egg”）也是作者的简称，所以可能是有意的简写，也可能是笔误。照原文译作“随机性与我们的大脑”，不加注 |

## 2. 双语审校

- 执行者：另一个独立上下文的 agent（Opus 5.5），没有参与翻译。
- 范围：全节 14 块，逐块对照英文；同时检查了破折号、禁用句式、半角标点、人名括注和术语。
- 发现：2 条；核实后采纳 2 条，不采纳 0 条。其中 1 条问题属实，改法换了一种。
  - 第 4 块 “How much can past performance (here the typing of the *Iliad*) be relevant in forecasting future performance?”：原译“对预测将来的表现能有多大关系”搭配不顺。采纳，改为“对预测将来的表现能有多大参考价值”，保留了 can 对应的“能”。
  - 第 5 块 “They call on the rule of the likelihood of such a successful run”：原译“他们搬出这种连续成功出现的可能性那套法则”定语叠得太长，读者要回头才能理清“法则”指什么。问题属实。审校者建议写成“这样连续成功的可能性很小”这条法则，其中“很小”是从上下文推出来的，原文没有说；所以改为“他们搬出关于这种连续成功可能性的那条法则，告诉自己：……”，同时把后面的逗号换成冒号，引出他们告诉自己的话。
- 审校者的总体判断：十个分节逐块对照英文读完，总体质量很高，可以进入中文通读。每一块都已译完，中英逐块对应；没有破折号、体例禁用的对比句式和混进中文的半角标点；人名和 people-zh.tsv 一致，术语用的都是术语表的译法。没有发现事实、数字、否定或人物关系上的错误。需要处理的是少数翻译腔偏重、搭配别扭的句子，都属于局部修改。

## 3. 中文通读

- 执行者：编辑 agent（Opus 5.5）。
- 范围：顺着中文把全节从头读到尾，看行文是否连贯、有没有重复、指代是否清楚、人名和术语前后是否一致。每一处改动都回查了英文。
- 发现并修改：
  - 第 5 块 “For common wisdom among people with a budding knowledge of probability laws is to base their decision making on the following principle”：原译“流行着这样一条常识，他们据此做决策：”把一句话拆成了两截，改为“因为在刚懂一点概率法则的人当中，通行的看法是，做决策要依据下面这条原则：”。
  - 第 5 块 “there is a great chance of his performing better than the crowd in the future—and a very great one at that”：原译“有很大的可能也比众人好，而且可能性非常大”把“可能”说了两遍，改为“那么他将来表现得比众人好的可能性很大，甚至非常大”，保留了原文层层加码的语气。
- 核对过的地方：past performance 写“过去的表现”，track record 写“过往业绩”，和术语表一致；猴子、幸存者偏差、半吊子、条件概率、稀有事件前后一致；卡萨诺瓦、阿尔·戈尔、尼禄·图利普都只在第一次出现时括注英文。改完后没有破折号、禁用句式和半角标点，`site.py status` 仍显示 14/14。

## 状态

- 没有未解决的意义问题。第 14 块 “Randomness and Our Brain” 的原文疑点照译者自检的处理，不加注。
- 阅读器校样还没有做；`book.json` 里本节的状态由主会话修改。

## 第三轮：GPT-6 Astra 独立审校

- 审校者：GPT-6 Astra，通过 Codex 运行，只读，和译者属于不同的模型家族。
- 发现：1 条。逐条找到中英文对应的句子，读过上下文后核实：成立并修改 1 条，不成立 0 条。审校者另外提出 2 条对英文原文的疑问，见下面。
- 成立并修改：
  - 第 13 块 “The business of Part II is more pedestrian; I will rapidly provide a synthesis of the biases of randomness as discussed in the now abundant literature on the subject.”：前一句说第一部分阐述的是文献里还没人探讨过的个人想法，pedestrian 在这里指第二部分的内容寻常，没有多少新意。“任务比较平淡”搭配别扭；“很快地综述一下”容易读成“不久就会综述”，rapidly 说的是讲得简短。旧译“第二部分的任务比较平淡：我会很快地综述一下随机性带来的偏差”，新译“第二部分的内容要常规一些：我会简要地综述一下随机性带来的偏差”，后半句“如今关于这个题目的文献已经很丰富了”不变。审校者建议写“第二部分的内容则比较常规：我会简要综述”；这里写“要常规一些”，对应原文 more 的比较语气，前一句开头已经有“不过”，所以省去“则”。
- 不成立，保留原译：无。
- 按全书统一的写法修改：0 处。逐条对照过：数字（“五只猴子”“两个因素”用汉字，“10 亿的 10 亿次方”“第 8 章”用阿拉伯数字）；书名括注（《伊利亚特》《奥德赛》《我的一生》《濒临失衡的地球》都在本节第一次出现时括注斜体原题，后面不再括注）；人名括注（卡萨诺瓦、阿尔·戈尔、尼禄·图利普在本节第一次出现时括注英文，和 people-zh.tsv 一致；“那位古代诗人”原文没有点名，不补荷马）；代词（作者用 he 指猴子，中文写“它”）；斜体旁边的标点放在星号外面；第 14 块的章名简称和“各节标题”的译法对应。本节没有外文词、译者注，也没有“当真”“姐夫”“进化”这类固定说法，这些条目都已经符合。
- 对英文原文的疑问：
  - 第 3 块：前一句说无穷多只猴子里必然有一只打出《伊利亚特》，后一句接着说 “Such probability is ridiculously low”，读者要自己补上“单独一只猴子打出来的概率”才讲得通。Goodreads 收录的这段引文也是这样写的，说明出版的文本本来如此，导入 EPUB 时没有出错。中文照原文写“这种概率低得可笑”，指向和原文一样含糊；中英两边意思没有相反，够不上加译者注的条件，不加。
  - 第 11 块 “in real life the other monkeys are not countable, let alone visible”：let alone 通常引出更难做到的一项。按下一句 “They are hidden away”，看不见才是没法数的原因，写成 not visible, let alone countable 更合逻辑，也可能是作者随口的说法。中文照原文的顺序写，不加注。核实这一句时还改了一处：原译“数不清”在中文里多指数量太多、数不过来，和原文有偏差；原文说这些猴子藏了起来，没人能去清点，正好接着第 9 块“我很少见到有人去数猴子”。旧译“其他猴子数不清，更别说看见了”，新译“其他猴子没法数，更别说看见了”。
- 核实与修改：agent（Opus 5.5）。改完后运行 `python3 scripts/site.py status fooled-by-randomness`，part2 显示 14/14，原文没有注释；`tools/term_consistency.py` 对本节没有提示；本节仍然没有破折号、体例禁用的对比句式和混进中文的半角标点。
