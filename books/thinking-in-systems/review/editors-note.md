# 编者的话（editors-note）审校记录

全节 11 个块，原文没有脚注，中英逐块对应（`site.py status` 显示 11/11）。下文的“第 N 块”按 `site.py status` 计数，从节名算起。

## 1. 译者自检

- 执行者：translation agent（Opus 5.5），译者本人。
- 范围：全节 11 块（节名、九段正文、署名行），逐块对照英文，检查漏译、增译、否定、条件、数字和日期、谁做了什么、比较对象、术语义项、人名、书名和机构名；人名对照 `review/terms/people-zh.tsv`，书名和机构名对照 `glossary.md`；术语用 `tools/term_consistency.py` 检查；用框架的 markdown-it 渲染中文，确认三处书名的斜体生效；全文查破折号和“不是……而是……”句式。
- 发现并修改：
  - 第 2 块 “Dana died quite unexpectedly in 2001—before she completed this book.”：初稿“2001 年，达娜十分意外地去世了”，“意外地去世”容易读成死于意外事故。原文说的是谁都没有料到，改为“2001 年，达娜突然去世，谁都没有料到，那时她还没有完成这本书”；破折号改成逗号，后半句另起分句。
  - 第 5 块 “Will another book really help the world and help you, the reader? I think so.”：初稿“我想能。”太生硬，改为“我想会的。”
  - 第 10 块 “It is a book for those who want to shape a better future.”：初稿“它是写给那些想塑造更美好未来的人的”，句末“的人的”拗口，前一句又刚用过“写给”，改为“这本书是为那些想塑造更美好未来的人准备的”。
- 写法上的决定：
  - 人名：Donella (Dana) Meadows 照 people-zh.tsv 写“德内拉（达娜）·梅多斯（Donella (Dana) Meadows）”，之后写“达娜”；纳尔逊·曼德拉、莱赫·瓦文萨、瓦茨拉夫·哈维尔在本节第一次出现时括注英文；署名行写“黛安娜·赖特（Diana Wright），2008 年”。
  - 书名：《增长的极限》（*The Limits to Growth*）第一次出现时括注，第 7 块的 *Limits to Growth* 只写《增长的极限》；*Thinking in Systems* 照“全书统一的写法”写《系统之美》，在本节第一次出现，括注原题；《超越极限》（*Beyond the Limits*）括注原题；《国际先驱论坛报》照体例不括注。
  - 第 3 块 “The Limits to Growth—a best-selling and widely translated book”：破折号改成逗号，后面另起一句“这本书十分畅销，被译成多种语言”。
  - 第 3 块 “6.6 billion people” 写“66 亿人”；“physical growth” 译“物质增长”，指人口、经济在物质上的扩张（术语表 physical 一条没有收这个搭配，见汇报）；“its updates” 译“它后来几次更新版”。
  - 第 4 块 “correct our course” 保留航行的比喻，译“修正我们的航向”。
  - 第 5 块 “seeing others ‘push back’ against your good ideas and good intentions”：保留引号，译“眼看着你的好主意和好意愿遭到别人的‘抵制’”。原文写的 functions 是动词，译“运作方式”，`term_consistency.py` 把这一块报告为 function 没有写“功能”，这是有意的。
  - 第 7 块 “the twenty-year update to *Limits to Growth*” 译“《增长的极限》出版 20 年后的更新版”；Pew Scholar in Conservation and the Environment、Committee on Research and Exploration for the National Geographic Society 照术语表写“皮尤环境保护学者”“美国国家地理学会的研究与探索委员会”。
  - 第 8 块 “burning oil fields on the way out” 照术语表写“撤退时放火焚烧了油田”；“Labor leader Lech Walesa” 译“工会领袖莱赫·瓦文萨”，瓦文萨领导的是团结工会；The International Panel on Climate Change 照术语表写“政府间气候变化专门委员会”（见下面的原文疑点）。
  - 第 9 块 “during a single week” 译“仅仅一个星期”；“systems in need of better management or complete redesign” 拆成“许多系统的例子，这些系统需要更好的管理，或者需要彻底重新设计”，读起来更顺。
  - 第 10 块 “This is a simple book for and about a complex world.” 译“这是一本简单的书，写给一个复杂的世界，也写这个复杂的世界”，保留 for 和 about 两层意思。
- 检查：`site.py status` 显示 11/11；渲染后没有残留的星号；数字“1993 年”“2001 年”“1972 年”“66 亿”“20 年”“20 世纪 90 年代初”“2008 年”都和原文一致；中文没有破折号，也没有体例禁用的对比句式。
- 未决：
  - 第 3 块 “The cautions … are recognized today as the most accurate warnings of how unsustainable patterns could, if unchecked, wreak havoc across the globe.” 译“如今被公认为最准确的警告，讲的是不可持续的模式如果不加遏制，可能怎样在全球造成浩劫”。原文的“最准确”是编者的评价，照译；句子较长，留给中文通读时再看。
  - 第 7 块 “In all aspects of her work, she was immersed in the events of the day.” 译“在工作的方方面面，她都密切关注着当时发生的事件”。immersed 比“密切关注”更深一层，也可以写“都和当时发生的事件紧紧连在一起”，留给审校者判断。

## 原文疑点

| 位置 | 原文 | 处理 |
| --- | --- | --- |
| 第 8 块 | The International Panel on Climate Change | 机构的正式名称是 Intergovernmental Panel on Climate Change。照 `glossary.md` 写通行中文名“政府间气候变化专门委员会”，不加注 |
| 第 8 块 | “emissions from human activities are substantially increasing the atmospheric concentrations of greenhouse gases and that this will enhance the greenhouse effect and result in an additional warming of the Earth’s surface.” | 和 1990 年第一次评估报告第一工作组决策者摘要的原句有出入：原句是 emissions resulting from human activities … the greenhouse gases carbon dioxide, methane, chlorofluorocarbons (CFCs) and nitrous oxide. These increases will enhance the greenhouse effect, resulting on average in an additional warming of the Earth’s surface。书中把两句并成一句，略去了气体名称和 on average，意思没有变。照书中的引文译，不加注 |
| 第 8 块 | poet Václav Havel | 哈维尔通常被称为剧作家，他也出版过诗集，说法不算错。照原文译“诗人” |

## 2. 双语审校

- 执行者：另一个独立上下文的 agent（Opus 5.5），没有参与翻译。
- 范围：这次审校一起看了献辞、作者的话、编者的话、题词、三个部分页、编者致谢和关于作者九节。本节 11 块逐块对照英文，核对了人名和括注、书名、机构名、年份和数字（1993 年、2001 年、1972 年、66 亿人、20 年、20 世纪 90 年代初、2008 年），以及上面三条原文疑点的处理。
- 发现：10 条（意义 3 条，表达 7 条）；核实后采纳 10 条，不采纳 0 条。10 条指出的问题都对照英文核实过，确实存在；其中 5 条用了和建议不同的字句，原因写在下面。
  - 照建议改的：
    - 第 4 块 “Dana helped usher in the notion that …”：“开启观念”搭配不当，改为“达娜推动了这样一种观念的兴起”。
    - 第 4 块 “systems thinking is a critical tool”：系统思考是一种思维方法，“一件工具”改为“一种关键的工具”。第 10 块说这本书是“一件有用的工具”，书是有形的东西，那一处保留“件”。
    - 第 5 块 “seeing others ‘push back’ against your good ideas and good intentions”：“好意愿”不是通行说法，改为“你的好主意和一片好心遭到别人的‘抵制’”。
    - 第 8 块 “Iraq’s army invaded Kuwait and then retreated, burning oil fields on the way out.”：去掉紧挨着的“撤退，撤退时”，改为“随后在撤退时放火焚烧了油田”；术语表规定的“撤退时”保留，retreated 的意思也还在。
    - 第 9 块 “In publishing Dana’s manuscript, I hope to increase the ability of readers to understand and talk about the systems around them and to act for positive change.”：初稿句首“出版达娜的书稿”没有主语，后面叠了两个带长定语的“能力”。改为“我出版达娜的书稿，是希望读者能更好地理解和谈论身边的系统，也更有能力为积极的改变而行动”。
  - 改法和建议不同的：
    - 第 2 块 “one of the best communicators in the world of systems modeling”：初稿“最善于和人沟通”读起来像在说人际交往能力。审校者建议“最善于把思想讲清楚、传达给大众的人之一”，英文没有提到大众，编辑改为“最善于传达思想的人之一”。
    - 第 8 块 “because their teachings are as relevant now as they were then”：“切题”指文章扣住题目，用在这里不对。审校者建议“和在当年一样有现实意义”，“现实意义”放到“当年”上说不太顺，编辑改为“因为它们给人的启示放到今天，也和当年一样适用”。
    - 第 7 块 “In all aspects of her work, she was immersed in the events of the day.”：“密切关注”把她写成了旁观者，这也是译者自检留下的未决。审校者建议“深深投入当时的时事之中”。event 是术语表的核心概念“事件”，下一句 “She understood those events to be …” 用“这些事件”回指，第 9 块的 the events of the day 也写“事件”，所以编辑保留“事件”，改为“她都深深投入到当时发生的事件之中”。
    - 第 3 块 “The cautions she and her fellow authors issued then are recognized today as the most accurate warnings of how unsustainable patterns could, if unchecked, wreak havoc across the globe.”：初稿把警告的内容用“讲的是”补在句尾，这也是译者自检留下的未决。采纳审校者先讲告诫内容、再讲评价的语序，改为“她和合著者当年发出告诫：不可持续的模式如果不加遏制，可能在全球造成浩劫。这些告诫在今天被公认为这方面最准确的警告。”建议里的“如今，”换成“在今天”，因为同一段后面还有一句“如今，石油产量到了峰值”。
    - 第 5 块 “are struggling to see how your business or organization can be part of a shift toward a better world”：初稿“成为走向更美好世界的这场转变的一部分”连用三个“的”，“这场”又把泛指的 a shift 写成了特指。审校者建议“投身到一场让世界变得更好的转变中去”，“投身”用在企业或组织上略显拟人，编辑改为“怎样才能参与到一场让世界变得更好的转变之中”，“参与”也更贴近 be part of。
  - 不采纳：无。
- 审校者的总体判断：九节译文整体可靠，中英逐块对应完整，这几节原文都没有脚注；人名和 people-zh.tsv 一致，每节第一次出现都括注了英文；术语、机构名、书名和三个部分页标题都和术语表一致；年份和数字都和原文相符；中文没有破折号，也没有“不是……而是……”句式；没有发现漏译、增译、否定方向或谁做了什么的错误。需要改的地方主要在编者的话：communicators、relevant、immersed 三处用词偏离原意，另有几句长定语、搭配不当或重复用词。三条原文疑点的处理都恰当。

## 3. 中文通读

- 执行者：编辑 agent（Opus 5.5）。
- 范围：改完双语审校的意见后，从节名顺着读到署名行，看连贯、重复、指代是否清楚，人名、书名和术语是否前后一致。
- 发现并修改（每一处都回查了英文，意思没有变）：
  - 第 5 块 “Perhaps you’re a manager who has worked hard to fix some important problems …, only to see other challenges erupt in their wake.”：初稿“结果却眼见别的难题跟着冒了出来”，和前一句的“眼看着你的好主意……”挨得太近，改为“结果却发现别的难题跟着冒了出来”。
  - 第 6 块 “there remains a clear need for an approachable and inspiring book”：“显然仍然需要”两个“然”连读拗口，改为“显然仍需要”。
- 核对过、没有改的地方：
  - 人名：德内拉（达娜）·梅多斯第一次出现括注英文，之后写“达娜”；曼德拉、瓦文萨、哈维尔和署名行的赖特都括注英文。
  - 书名：《增长的极限》第一次出现括注，第 7 块不再括注；《系统之美》《超越极限》括注原题；《国际先驱论坛报》照体例不括注。
  - 前后用词：lead author 写“第一作者”，和关于作者一节一致；第 6 块和第 10 块的 approachable 都写“平易近人”；第 7 块和第 9 块的 events 都写“事件”。
  - 第 3 块改后“这些告诫”回指前一句的“告诫”，“这本书指出”回指本段开头的《增长的极限》，指代清楚。
  - 全节没有破折号和“不是……而是……”句式；`site.py status` 显示 11/11。

## 状态

- 没有未解决的意义问题。译者自检留下的两条未决（第 3 块的长句、第 7 块的 immersed）都在双语审校中改定。
- 上面“原文疑点”表里的三条照旧，审校者认为处理恰当；这次没有发现新的原文疑点。
- 第 4 节阅读器校样还没有做。
