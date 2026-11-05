# 序章 云中的清真寺（prologue）审校记录

全节 16 个块，原文没有注释，中文没有加译者注；中英逐块对应（`site.py status` 显示 16/16）。

## 1. 译者自检

- 执行者：translation agent（Opus 5.5），译者本人。
- 范围：全节 16 块，对照原文逐段检查漏译、增译、否定、条件、数字、人名、术语和格式。另外运行了 `python3 scripts/site.py status fooled-by-randomness`（16/16）；在 `/tmp` 的一份副本里把本节设成草稿后用 `framework/tools/build.py --drafts` 构建通过，表 P.1 标题的硬换行渲染成了换行；`tools/term_consistency.py` 对本节只有一处提示，是误报（第 4 块的 Arthur Rimbaud 被当成了 people-zh.tsv 里的 Brian Arthur）。也查过本节没有破折号、没有体例禁用的对比句式、中文里没有半角标点和嵌套括号。
- 发现并修改：
  - 第 9 块 “99.9% of their past performance is attributable to chance, and chance alone”：初稿“有 99.9% 要归于偶然，纯属偶然”意思重复，按术语表 chance alone 的写法改为“有 99.9% 纯属偶然”。
  - 第 13 块 “your local college English professor”：初稿“你们当地大学的英语教授”和后面“你那位姑婆”人称不一致，改为“你身边那所大学里的英语教授”。
  - 第 14 块 “Delivering advice assumes that our cognitive apparatus rather than our emotional machinery exerts some meaningful control over our actions”：初稿“认知器官（而非情绪机制）”是对比句式，改为“假定对我们的行动起着某种实质控制作用的是认知器官，情绪机制则起不了这种作用”。
  - 第 3 块 “to bring on the much-needed rain”：初稿“用来求来急需的雨水”重复“来”字，改为“求得”。
  - 第 14 块 “Karl Popper (falsificationism and distrust of intellectual ‘answers,’ …), Friedrich Hayek and Milton Friedman (suspicion of governments), …”：照原文把思想标签放在括号里，会和英文名的括注连成两组括号，所以改成分号隔开的列表，每人后面加一个短句，例如“卡尔·波普尔（Karl Popper），他主张证伪主义……；弗里德里希·哈耶克（Friedrich Hayek）和米尔顿·弗里德曼（Milton Friedman），他们对政府抱着怀疑”。
  - 第 15 块 “My colleague Bob Jaeger (he followed the opposite course of mine …)” 和 “(his hero: Wittgenstein; his villain: Descartes)”：括注英文名后会出现连续或嵌套的括号，所以都拆成了独立的句子。
  - 第 4 块 “few claim that art is a tool of investigation of the Truth—rather than an attempt to escape it or make it more palatable”：原文用破折号加 rather than，改写成两个分句：“说艺术是探究真理的工具的人很少，艺术更常被看成一种逃避真理、或者让真理变得容易入口的尝试。”
- 译法上的选择：
  - 第 2 块 nonluck、non-randomness 照术语表写“非运气”“非随机性”，括号里的 skills、determinism 写“能力”“决定论”；*lucky fool* 写“*幸运的傻瓜*”，保留斜体。
  - 第 3 块 “the right time and the right place” 写“天时地利”；Federal Reserve Board 写“美联储”。
  - 第 6 块 “the fool of all fools” 照术语表写“傻瓜中的傻瓜”；“randomness foolishness” 写“只是被随机性愚弄了”；“rather the victims of delusions … than the opposite” 写“与其说是清醒的，不如说是错觉的受害者”。
  - 第 11 块表题照术语表写“表 P.1 混淆表”，保留粗体和硬换行，副题写“列出本书所用的核心区分”。
  - 第 12 块 “practitioner of uncertainty” 照术语表 practitioner 的写法，写“和不确定性打交道的实干者”；“snake-oil salesmen” 写“兜售万灵油的骗子”；“standard error” 写“标准误差”。
  - 第 13 块 “how-to-reach-happiness-in-twenty-steps and how-to-become-a-better-person-in-a-week book writer” 不是具体书名，写成加引号的“20 步获得幸福”“一周成为更好的人”，没有用书名号。
  - 第 14 块 Peirce “born a hundred years too early” 是夸张的说法，按约数写“早生了一百年”；“Papal infallibility” 写“教皇无谬论”；“(not *Fooled by Randomness*)”“(completely *Fooled by Randomness*)” 照体例写“没有*被随机性愚弄*”“完全*被随机性愚弄*”，保留斜体。
  - 第 15 块 “the generator of the *Fooled by Randomness* problem” 照术语表写“*被随机性愚弄*这个问题的根源”；“keep-it-simple-stupid” 写“保持简单，傻瓜”并括注原文。
  - 第 16 块 “Solon’s warning” 照术语表写“梭伦的警告”。梭伦的英文括注放在紧接着的“梭伦（Solon）对稀有事件的那番感慨”里，“梭伦的警告”这个术语因此保持完整；“wax in my ears” 写“我耳朵里的蜡”，和第三部分标题一致。
- 人名：和 `review/terms/people-zh.tsv` 逐个核对过，每人在本节第一次出现时括注英文：阿蒂尔·兰波（Arthur Rimbaud）、保尔·瓦莱里（Paul Valéry）、普吕多姆先生（Monsieur Prudhomme）、伊尔玛（Irma）、卢梭（Rousseau）、葛德文（Godwin）、孔多塞（Condorcet）、托马斯·潘恩（Thomas Paine）、卡尔·波普尔（Karl Popper）、弗里德里希·哈耶克（Friedrich Hayek）、米尔顿·弗里德曼（Milton Friedman）、亚当·斯密（Adam Smith）、赫伯特·西蒙（Herbert Simon）、阿莫斯·特沃斯基（Amos Tversky）、丹尼尔·卡尼曼（Daniel Kahneman）、乔治·索罗斯（George Soros）、查尔斯·桑德斯·皮尔士（Charles Sanders Peirce）、鲍勃·耶格尔（Bob Jaeger）、维特根斯坦（Wittgenstein）、笛卡尔（Descartes）、梭伦（Solon）。原文只写姓的人，括注也只写姓。
- 数字：19 世纪、19 岁、99.9% 用阿拉伯数字；三十几岁、三个部分、一百年用汉字；“20 步”按 11 以上的确数写阿拉伯数字。
- 未决：
  - 第 5 块原文拼作 Paul Valery（少了重音符号），按 people-zh.tsv 的 name 一列括注成 Paul Valéry。如果全书要求括注照抄原文拼法，请主会话改回 Paul Valery。
  - 第 16 块梭伦的括注位置（见上面“译法上的选择”），请主会话和其他章节统一。
  - 双语审校、中文通读和阅读器校样还没有做；`book.json` 里本节的状态由主会话修改。

## 原文疑点

| 位置 | 原文 | 处理 |
| --- | --- | --- |
| 第 4 块 | *I saw mosques in the clouds* announced Arthur Rimbaud | 兰波《地狱一季》“言语炼金术”的原文是 “je voyais très-franchement une mosquée à la place d’une usine”（我分明看见工厂的位置上是一座清真寺），后面才有“天上道路的马车”（des calèches sur les routes du ciel）。“云中的清真寺”是作者的转述，并非原句。属于已核实的出入（依据法国国家图书馆 essentiels.bnf.fr 的“L’alchimie du verbe”节选），不影响作者的论点。照原文译，正文不加注 |

## 2. 双语审校

- 执行者：另一个独立上下文的 agent（Opus 5.5），没有参与翻译。
- 范围：全节 16 块，逐块对照英文；同时检查了破折号、禁用句式、半角标点、人名括注和术语。同一位审校者也审了第一、二、三部分的导言、第 14 章、尾声、献辞、两版致谢和关于作者，见各自的记录。
- 发现：7 条；核实后采纳 7 条，不采纳 0 条。其中 1 条问题属实，改法换了一种。
  - 第 6 块 “we underestimate the share of randomness in about everything”：原译“我们几乎低估了一切事物里随机性所占的份额”把“几乎”放在动词前面，容易读成“差一点就低估了”。采纳，改为“几乎在所有事情上，我们都低估了随机性所占的份额”。
  - 第 14 块 “We are so defective and so mismatched to our environment that we can just work around these flaws.”：原译“只能绕开这些缺陷行事”带出了别无选择的无奈，和上一句“不必费力去纠正”的轻松口气接不上。采纳，改为“绕开这些缺陷行事就行了”。
  - 第 2 块 “It is endemic in politics”：原译“更是根深蒂固”多了一层和商界的比较，原文只说这种混淆在政治里很普遍。采纳，改为“在政治里，这种混淆随处可见”。
  - 第 6 块 “economic ‘risk takers’ are rather the victims of delusions … than the opposite”：原译“与其说是清醒的，不如说是错觉的受害者”用了生硬的对比句式，“清醒的”也是译者替 the opposite 补出来的。采纳，改为“多半是错觉的受害者（……），相反的情况很少”。
  - 第 4 块 “At the cost of appearing biased”：原译“冒着显得有偏见的风险”照搬了英文的结构，句首偏重。采纳，改为“这么说难免显得我有偏见，但我不得不说”。
  - 第 12 块 “carried around a large sword”：普吕多姆先生的典故里是一把军刀，“大刀”会让中文读者想到长柄大刀。采纳，改为“一把大军刀”。
  - 第 16 块 “The first is an introspection into Solon’s warning, as his outburst on rare events became my lifelong motto.”：审校者指出梭伦的英文括注没有落在他在本节第一次出现的地方，同一句里“梭伦”还重复了两次。问题属实。审校者建议写“梭伦（Solon）的警告”，这样会把术语表里的“梭伦的警告”拆开，`term_consistency.py` 也会报告；现在照第三部分“维特根斯坦的尺子（Wittgenstein’s ruler）”的做法，把括注放在整个术语后面：“第一部分审视梭伦的警告（Solon’s warning）：他对稀有事件的那番感慨，成了我毕生的座右铭。”译者自检里关于梭伦括注位置的未决事项就此了结。
- 审校者的总体判断：十个分节逐块对照英文读完，总体质量很高，可以进入中文通读。每一块都已译完，中英逐块对应；没有破折号、体例禁用的对比句式和混进中文的半角标点；人名和 people-zh.tsv 一致，术语用的都是术语表的译法。没有发现事实、数字、否定或人物关系上的错误。需要处理的是几处语气和意思的细节，以及少数翻译腔偏重、搭配别扭的句子，都属于局部修改，改完不需要重新对齐分块。

## 3. 中文通读

- 执行者：编辑 agent（Opus 5.5）。
- 范围：顺着中文把全节从头读到尾，看行文是否连贯、有没有重复、指代是否清楚、人名和术语前后是否一致。每一处改动都回查了英文。
- 发现并修改：
  - 第 3 块 “biographies of successful men and women presenting their specific explanation on how they made it big in life”：原译“书里讲的都是他们自己怎样发迹的具体解释”，“讲的是……解释”搭配不顺，改为“他们在书里各自给出具体的解释，讲自己是怎样发迹的”。
  - 第 4 块：“一种逃避真理、或者让真理变得容易入口的尝试”里的顿号多余，删去。
  - 第 9 块 “For it is the area of human undertaking where the confusion is greatest and its effects the most pernicious.”：原译以“因为”开头单独成句，读起来像半句话；改为用逗号接在上一句“经济生活是最好的（也是最有趣的）实验室”后面，因果关系保留。
  - 第 14 块 “We are faulty and there is no need to bother trying to correct our flaws.”：“缺陷”在相邻两句里出现了四次，删去第一句末尾的“这些缺陷”，写“我们有缺陷，也不必费力去纠正”。
- 核对过的地方：每个人仍然只在本节第一次出现时括注英文，梭伦在本节只出现这一次；幸运的傻瓜、噪声、混淆表、骗术、乌托邦愿景、悲剧愿景、可错论、斯多葛主义、我耳朵里的蜡前后一致。改完后再查过：没有破折号，没有体例禁用的对比句式和“与其说……不如说……”，中文里没有半角标点；`site.py status` 仍显示 16/16；`term_consistency.py` 对本节只剩第 4 块那条已知的误报（Arthur Rimbaud 被当成 Brian Arthur）。

## 状态

- 没有未解决的意义问题。
- 留给主会话的事项：第 5 块 Paul Valéry 括注的拼法（见译者自检的未决事项），属于格式问题；阅读器校样还没有做；`book.json` 里本节的状态由主会话修改。

## 第三轮：GPT-6 Astra 独立审校

- 审校者：GPT-6 Astra，通过 Codex 运行，只读，和译者属于不同的模型家族。
- 发现：5 条。逐条找到中英文对应的句子，读过上下文后核实：成立并修改 5 条，不成立 0 条。其中 3 条问题属实，改法换了一种（第 4、5、16 块）。
- 成立并修改：
  - 第 4 块 “the literary mind can be intentionally prone to the confusion between *noise* and *meaning*”：原译“文学头脑可能会有意地倾向于混淆*噪声*和*意义*”，“文学头脑”是直译，“有意地倾向于”把“故意”和“倾向”叠在一起，读起来生硬。审校者建议写“习惯用文学眼光看问题的人，有时会有意把*噪声*和*意义*混为一谈”，这样后半句“也就是混淆随机拼凑出来的排列和精心设计的讯息”也得跟着改。现在改为“文人的头脑有时会故意混淆*噪声*和*意义*”，后半句保持原样。
  - 第 5 块 “my profound allergy to most teachers of literature and ‘critics’”：原译“我对大多数文学教师和‘评论家’深深的过敏”，“深深的”和“过敏”搭配别扭，这一点成立。审校者建议改成“极度反感”，可是 allergy 是作者反复用的比喻，第 1、4、6 章都写“过敏”（“尼禄对商务谈话的那套词汇过敏”“我对胡话和空洞辞藻的过敏”“我对自信满满的陈词滥调的过敏”），所以保留比喻，改为“严重的过敏”。
  - 第 6 块 “probability applied to practice is almost nonexistent as a discipline”：原译“应用于实践的概率，作为一门学科几乎还不存在”，读起来像是说概率本身还不成学科。采纳审校者的改法，改为“概率的实际应用几乎还没有形成一门学科”。
  - 第 8 块 “Even popular opinion warns that bad information is worse than no information at all.”：原译“坏信息比没有信息还糟”，“坏信息”容易读成坏消息；上下文讲的是从随机现象里读出并不存在的模式，bad 指错误的信息。采纳，改为“错误的信息比完全没有信息还糟”。
  - 第 16 块 “a collection of probability biases I encountered (and suffered from) in my career in randomness”：原译“遇到过（也吃过苦头）的一系列概率偏差”，括号里的“吃过苦头”和后面的“概率偏差”接不上，这一点成立；suffered from 在这里指作者自己也受这些偏差影响，紧接着的一句就是“这些偏差至今还在愚弄我”。改为“遇到过（自己也深受其害）的一系列概率偏差”。审校者还建议把“概率偏差”改成“概率判断偏差”，这一部分不采纳：序言里 probability biases 也写“概率偏差”（“我在这一章里把有关概率偏差的文献全都浓缩了进去”），两处保持一致。
- 不成立，保留原译：没有整条不成立的发现。第 5 块和第 16 块各有一部分建议没有照办，理由写在上面对应的条目里。
- 按全书统一的写法修改：0 处。逐条对照了“全书统一的写法”和“全书统一的写法（译完后定）”，本节已经符合：数字里 19 世纪、19 岁、99.9%、20 步用阿拉伯数字，三十几岁、三个部分用汉字，“早生了一百年”是作者夸张的约数，写汉字；21 个人名都在本节第一次出现时括注英文，和 people-zh.tsv 一致，瓦莱里的括注写正确拼法 Paul Valéry，符合“原文的笔误”一条，正文不加注；“梭伦的警告（Solon’s warning）”符合“作者自己的说法里带着人名”一条；“play the game too seriously”写“玩得太当真”，和“当真”一条一致；“*我在云中看见了清真寺*”“*噪声*和*意义*”等斜体旁边的标点都能正常闭合。本节没有书名、文章题目、拉丁语词、倍数、诺贝尔奖、brother-in-law 这类条目涉及的说法。
- 对英文原文的疑问：审校者指出表 P.1 在英文里只有表题和副题，没有表格内容，正文却多次提到它的左栏、右栏和分项。这和术语表“图表”“译者注”两条的记录一致：这个 EPUB 缺了这张表，第 2 章第 38 块提到的左右栏也是这张表，目前照原文译，暂不加译者注。是否补表或加注，留给用户决定。
- 核实与修改：agent（Opus 5.5）。改完后运行 `python3 scripts/site.py status fooled-by-randomness`，序章显示 review、16/16，本节没有注释。`tools/term_consistency.py` 对本节仍然只有第 4 块那条已知的误报（Arthur Rimbaud 被当成 people-zh.tsv 里的 Brian Arthur）。也查过改动后的译文没有破折号和体例禁用的对比句式。
