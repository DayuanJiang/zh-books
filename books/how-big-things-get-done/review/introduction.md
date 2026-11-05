# 引言 加州梦（introduction）审校记录

全节 39 个块、18 条注释，另有 2 条译者注，中英逐块对应（`site.py status` 显示 39/39、18/18）。

## 1. 译者自检

- 执行者：translation agent（Opus 5.5）。
- 范围：全节 39 个块（节标题、两个小节标题和全部正文段落）和 18 条注释，对照英文逐段检查漏译、增译、否定、条件、数字和金额换算、日期、谁做了什么、比较对象、术语义项、人名，以及注释标记的位置。另外用脚本逐块核对了注释标记的编号和次序、每块里的数字，以及中文里有没有破折号和体例禁用的对比句式；用 `tools/term_consistency.py` 核对术语和人名，本节没有不一致的块；用 `framework/tools/book.py` 的 `compile_chapter` 按完整章节编译，两条译者注都有引用，没有报错。
- 发现并修改：
  - 第 32 块 “Hardly a detail was issued without having been thoroughly analyzed by the builders and their experts and adjusted and changed to meet every foreseen delay.”：初稿照英文的双重否定写成“几乎没有哪个细节在发出之前，不是经过……的”，句子绕，读者要倒回去理解。改成肯定的说法：“几乎每个细节在发出之前，都经过了施工方和他们的专家的透彻分析，并为应对每一种预见到的延误作过调整和修改。”
  - 第 24 块 “work began in a rush of excitement”：初稿“在一片兴奋中匆匆开工”，“匆匆”是多出来的，英文说的是一阵兴奋，没有说仓促。删去“匆匆”。
  - 第 25 块 “the first iPod was shipped to customers in November 2001”：初稿“第一台 iPod 就发货给了顾客”，“就”替作者加了强调，改为“第一台 iPod 发到了顾客手里”。同一块 “Boeing took twenty-eight months” 照原文写“用 28 个月”，没有加“只”。
  - 第 13 块 “The history of foreign aid is littered with boondoggles, and this project could easily have added to the mess.”：初稿前半句用“烂摊子”，后半句用“给这一团乱麻再添一笔”，两个比喻混在一起。改为“劳民伤财的烂项目比比皆是，这个项目本来也很容易成为其中之一”。
  - 第 3 块 “particularly if you live in California. If you do, you’re paying for it.”：初稿连说两次“如果你住在加州”，第二次改为“如果是这样，那你正在为它买单”。
  - 第 5 块 “it would be ready to roll by 2020”：初稿“2020 年就能通车”漏了 by，改为“到 2020 年就能通车”。
  - 第 4 块 “Golden State voters were asked to imagine”：初稿“加州选民被请来想象”是生硬的被动句，改为“有人请加州选民想象”。
  - 第 28 块 “stretching higher into the sky than any other building on the planet”：初稿“比地球上任何一座建筑都更高地伸向天空”不通顺，改为“直插天空，比地球上任何一座建筑都高”。
  - 第 29 块 “Smith had been the Democratic presidential candidate in the 1928 election”：初稿“在 1928 年的大选中是民主党的总统候选人”改为“在 1928 年的大选中代表民主党竞选总统”。
  - 第 36 块 “By the time the Empire State Building was officially opened by President Herbert Hoover (exactly as scheduled, on May 1, 1931)”：初稿“1931 年 5 月 1 日，帝国大厦和计划的日期分毫不差，由……宣布启用”主语和状语缠在一起，改为“帝国大厦完全按计划，在 1931 年 5 月 1 日由赫伯特·胡佛总统正式宣布启用”。
  - 第 10 块 “Not like this.”：初稿“反正不是这样”口气太随便，改为“肯定不是这样”。
- 翻译时的处理，供双语审校参考：
  - 数字照“全书统一的写法”：fourteen years 写“14 年”，twenty years 写“20 年”，twenty-eight months 写“28 个月”，eighteen months 写“18 个月”，fourteen and a half floors in ten working days 写“十个工作日里盖了 14 层半”，Twenty thousand schools 写“2 万所学校”，almost nine thousand 写“近 9000 人”，More than three thousand 写“3000 多名”，about a hundred other countries 是约数，写“其他一百来个国家”。金额换算成万、亿：330 亿、430 亿、680 亿、770 亿、将近 830 亿、1000 亿、230 亿、大约 800 亿美元；5000 万美元（8.2 亿美元）、4100 万美元（6.79 亿美元）、1.41 亿美元；注释 1 的 327.85 亿美元到 336.25 亿美元。171-mile section 照术语表体例的例子写“171 英里”，没有括注公制。
  - 核对过的数字：第 37 块的 17% 是按 2021 年美元算的：8.2 亿美元减 6.79 亿美元是 1.41 亿美元，和原文一致，再除以 8.2 亿美元，约为 17.2%；按当年的名义金额算，少花的 900 万美元除以 5000 万美元，是 18%，见下面的原文疑点。尼泊尔项目 1992 年开工、计划用 20 年，2004 年完工，提前八年，和注释 6 说实施团队用了 12 年一致。
  - 第 4 块 Golden State 是加州的别称，直接写“加州”。
  - 第 9 块的 “bullet train to nowhere” 照第 2 章的写法译“通往无处的子弹头列车”，加引号；第 23 块英文没有引号，中文也不加。
  - 第 17 块书名第一次出现，写《怎样做成大事》（*How Big Things Get Done*）；big thing 照术语表写“大事”，保留引号。第 5 块的 *visionary* 译“*富有远见*”，保留斜体。
  - 第 24 块和第 38 块的作者说法第一次出现时括注英文：“快思考，慢行动”（Think fast, act slow）、“慢思考，快行动”（Think slow, act fast）。第 39 块英文没有引号，中文也不加。
  - 第 20 块 “In any big project (meaning a project that is considered big, complex, ambitious, and risky by those in charge), people think…”：插入的定义拆成单独一句放在前面，“所谓大项目，是指负责人认为规模大、复杂、雄心勃勃、有风险的项目”。
  - 第 31 块兰姆引文里作者补的 “[the architect]” 照第 1 章的做法写成全角方括号“［建筑师］”；armature 是雕塑用的骨架，译“骨架”。第 33 块 “Empire State was finished entirely (on paper)” 用“就已经全部完工了，只不过是在纸面上”保留原文最后才点出“纸面上”的语气。
  - 人名都照 `review/terms/people-zh.tsv`，每人在本节第一次出现时括注英文：威廉·兰姆（William Lamb）、约翰·J.拉斯科布（John J. Raskob）、阿尔·史密斯（Al Smith）、赫伯特·胡佛（Herbert Hoover）、里士满·施里夫（Richmond Shreve）、菲伊·雷（Fay Wray）。第 25 块的胡佛水坝是地名，胡佛本人第一次出现在第 29 块，在那里括注。金刚是电影角色，写“金刚在银幕上”，没有括注，也没有补电影名。注释里的人名（Hans Lauritz Jørgensen、Patrick Collison、Tony Fadell 等）照写英文。
  - 机构：Bill & Melinda Gates Foundation 用通行的中文名“比尔及梅琳达·盖茨基金会”；Empire State Inc. 照术语表写“帝国大厦公司”；American Institute of Architects 写“美国建筑师协会”；Waldorf-Astoria 写“华尔道夫-阿斯托里亚酒店”，同一块第二次出现写“这家酒店”；Chrysler Building 写“克莱斯勒大厦”；Yankees 写“洋基队”；注释 6 的 Basic and Primary Education Project (BPEP) 照术语表写“基础与初等教育项目（BPEP）”，四所大学照术语表写中文名。
  - 小节标题：“Psychology and Power” 照术语表写“心理与权力”；“A New York Success Story” 译“纽约的成功故事”。
  - 注释：14 条是纯出处，照英文原样保留，注释 17 的 Ibid. 和注释 12 的 John Tauranc 也照写；另外 4 条（注释 1、4、6、10）有引导语或说明，译成中文，出处和人名照写英文。注释 6 里 “however much I loved (and love) being involved” 译“尽管我当时喜欢、现在也依然喜欢亲身参与”，去掉了破折号；“I planned and programmed the project” 译“项目的规划和方案编制由我负责”。
  - 译者注 2 条：[^t1] 照术语表说明标题 California Dreamin’ 是 The Mamas & the Papas 1965 年的歌曲《加州梦》（发行时间已查维基百科：1965 年 12 月），标记放在第 10 块“加州很大胆，敢做大梦”后面，和标题呼应；节标题本身照术语表只写“引言 加州梦”，标题里的标记会显示在目录里。[^t2] 照术语表说明注释 12 的 Tauranc 应为 Tauranac，标记放在第 28 块正文的 [^12] 后面。
- 检查：`python3 scripts/site.py status how-big-things-get-done` 显示 introduction 为 39/39、18/18；`compile_chapter` 按完整章节编译通过，两条译者注都有引用。中文正文和译者注没有破折号，也没有体例禁用的对比句式；中文里的连接号只出现在照写英文的出处里（各条注释的页码范围）和“华尔道夫-阿斯托里亚”这个名字里。`book.json` 的状态还是 `todo`，由主会话修改。
- 未决，留给主会话决定：
  - [^t2] 的位置：阅读器只把正文块里的标记算作引用，标记写在注释 12 的定义里会报“defined but never referenced”，所以放在了正文的 [^12] 后面。第 2 章处理 Sharot Tali 时是在注释 9 里直接写“（译者注：……）”。如果主会话想全书统一成第 2 章的写法，可以把 [^t2] 改成注释 12 里的括注，但那样要在出处中间插入中文。
  - 第 37 块的 17% 和名义金额算出的 18% 有出入，是否要加译者注，请主会话决定；现在照原文翻译，没有加注。
  - 小节标题 “A New York Success Story” 暂译“纽约的成功故事”，也可以译“一个纽约的成功故事”。

## 原文疑点

| 位置 | 原文 | 处理 |
| --- | --- | --- |
| 注释 12 | John Tauranc, *The Empire State Building: The Making of a Landmark* | 注释 16 引同一本书时写作 Tauranac，作者名应为 John Tauranac（`review/source.md` 已记录）。注释照原文保留，加译者注 [^t2] 说明 |
| 第 37 块 | It acually cost $41 million | acually 是 actually 的拼写错误，按 actually 翻译，没有加注 |
| 第 37 块 | It acually cost $41 million ($679 million in 2021). That’s 17 percent under budget, or $141 million in 2021 dollars. | 按 2021 年美元算，8.2 亿减 6.79 亿，再除以 8.2 亿，约为 17.2%，和 17% 对得上；按名义金额算，少花的 900 万美元除以 5000 万美元，是 18%。两种算法都说得通，作者用的是 2021 年美元，和书中按实际价值计算的口径一致。照原文翻译，没有加注 |

## 2. 双语审校

- 执行者：另一个独立上下文的 agent（Opus 5.5），没有参与翻译。
- 范围：全节 39 个块和 18 条注释，逐块对照英文；核对了数字和金额换算、日期、人名、术语、注释标记的编号和位置、注释出处和英文是否一致，以及破折号和体例禁用的句式。
- 发现：14 条（意义 3 条，术语 3 条，表达 8 条）；核实后采纳 14 条，不采纳 0 条。其中 8 条照审校者的建议修改，6 条认可问题，但换了改法，建议里和原文有出入的部分没有用。
  - 照建议修改的例子：
    - 第 25 块 “Apple hired the first employee to work on what would become the legendary iPod in late January 2001”：原译“苹果公司雇用了第一位员工，开发后来成为传奇的 iPod”会被读成苹果公司有史以来的第一位员工。改为“苹果公司为后来成为传奇的 iPod 雇来了第一位员工”。
    - 第 5 块 “And for a total cost of $33 billion it would be ready to roll by 2020.”：原译“它的总成本是 330 亿美元”像在说一个确定的数字，原文说的是当时的承诺，注释 1 也写明是估算，下一段又讲估算一路上涨。改为“总成本预计为 330 亿美元”。
    - 第 9 块 “the annual gross domestic product of Honduras, Iceland, and about a hundred other countries”：原译容易读成这些国家加起来的国内生产总值，加“各自”。
    - 第 28 块 “a financial wizard”：拉斯科布是金融家，“理财奇才”改为“金融奇才”。
    - 第 15 块 “Average practice is a disaster, best practice an outlier”：改为“平均水平的做法是一场灾难，最佳实践只是离群的特例”。“最佳实践”是管理学的通行说法，“平均水平”和“离群”保留了原文的统计口吻。
    - 第 13 块 “it finished on budget in 2004”：按术语表把“没有超出预算”改为“不超预算”，和第 9 章讲同一个尼泊尔项目时的写法一致。
    - 第 17 块 “the average home remodeler”：“普通的家庭装修者”是硬造的说法，改为“普通人装修自家房子时需要应付的”。
    - 第 22 块 “They are found whenever someone is excited by a vision”：“被一个愿景激动起来……就会遇到它们”改为“为一个愿景而兴奋……心理和权力就会出现”，主语回到心理和权力。
  - 换了改法的例子，以及建议里没有用的部分和理由：
    - 第 10 块 “Not like this. An ambitious vision is a wonderful thing.”：认可“肯定不是这样”答非所问，改为“肯定不能像这样”。建议的“至少不能像这样”多了原文没有的让步语气，没有用。“美妙的事”改为“好事”；“雄心勃勃”保留，第 20 块的 ambitious 也译“雄心勃勃”，没有换成建议的“宏大”。
    - 第 7 块 “As I write, the current highest estimate is $100 billion.”：删去和“在我写这本书的时候”重复的“目前”。建议加“已经”，原文没有这层强调，没有加。后一句 “nobody knows what the full, final cost will be” 照建议改为“谁也不知道整个项目最终要花多少钱”。
    - 第 25 块 “the first of its iconic 747s”：建议的“这款客机后来成了航空业的标志”里，“航空业”是原文没有的，而且紧接着的 iPod 一句也有“后来”。改为“第一架 747，这款客机如今已成经典”。
    - 第 31 块 “Lamb’s focus was intensely practical”：建议的“兰姆考虑的全是实际问题”比原文说得绝对。改为“兰姆处处从实际出发”。
    - 第 30 块 “skyscrapers (the thrilling new symbol of prosperous Machine Age America) were leaping up all over Manhattan”：建议的“让人心潮澎湃”渲染过度，“繁荣兴旺”又和同一句前面的“经济繁荣”重复。改为“摩天大楼在曼哈顿各处拔地而起，这些激动人心的新象征，代表着机器时代美国的兴旺发达”。
    - 第 3 块 “particularly if you live in California. If you do, you’re paying for it.”：建议用“加州人”。为高铁买单的是住在加州的纳税人，所以保留 live in 的说法，改为“住在加州的人尤其可能听说过。如果你就住在加州，那你正在为它买单”，“如果”的条件只剩一个，指代清楚了。
- 审校者的总体判断：这一节译得扎实、可读，改掉少数问题后可以定稿。39 个块和 18 条注释位置一一对应；数字和金额换算、日期和年数、人名、术语、小节标题都和术语表一致；注释标记的编号、顺序和位置都对，14 条纯出处注释和英文逐字相同；两条译者注准确；没有发现漏译、增译或否定方向译反的问题。

## 3. 中文通读

- 执行者：编辑 agent（Opus 5.5）。
- 范围：采纳审校意见后，从节标题读到最后一条译者注，检查连贯、重复、指代，以及人名和术语前后是否一致。
- 发现并修改：
  - 第 8 块 “at an estimated cost of $23 billion”：“估计耗资”改为“预计耗资”，和第 5 块新改的“预计为 330 亿美元”一致；术语表把“估计”留给一般说法。
  - 第 25 块和第 30 块按审校意见修改时，一并处理了通读时看到的重复：波音一句和 iPod 一句不再连用“后来”，第 30 块的同一句里不再出现两次“繁荣”（改法见上一节）。
  - 每处改动都回查了英文原句。
- 核对后保留：人名第一次出现时括注英文，之后只写中文（赫伯特·胡佛在第 29 块括注，第 36 块写“赫伯特·胡佛总统”）；“通往无处的子弹头列车”“快思考，慢行动”“慢思考，快行动”“帝国大厦公司”前后写法一致；第 6 块和第 7 块两次“在我写这本书的时候”对应原文的两次 As I write，保留。
- 检查：`python3 scripts/site.py status how-big-things-get-done` 显示 introduction 仍为 39/39、18/18；用 `framework/tools/book.py` 的 `compile_chapter` 编译通过；中文里没有破折号，也没有“不是……而是……”句式。

## 状态

没有未解决的意义问题。译者自检留给主会话的三项（[^t2] 的放法、第 37 块 17% 和名义金额算出的 18% 是否加注、小节标题 “A New York Success Story” 的译法）属于体例选择，仍由主会话决定。阅读器校样还没有做，`book.json` 的状态没有改。
