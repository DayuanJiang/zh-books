# 附录（appendix）审校记录

全节 111 个块，原文没有脚注，中英逐块对应（`site.py status` 显示 111/111）；译文另加 2 条译者注（[^t1]、[^t2]）。下文的“第 N 块”按 `site.py status` 计数的 111 个可译块编号，从节名算起，图片不计；列表整体算一块。

## 1. 译者自检

- 执行者：translation agent（Opus 5.5），译者本人。
- 范围：全节 111 块，逐块对照英文：术语表 18 条、系统原理汇总 9 组 40 条、八种陷阱和出路、干预系统的 12 个位置、15 条生活准则、模型方程 9 个模型。检查漏译、增译、否定、条件、数字、比较对象、术语义项、斜体和粗体；用框架的 markdown-it 逐块渲染中英两边，比较每块的 `<em>`、`<strong>` 个数和数字；逐块比较行数和行尾硬换行（两边都是 124 行硬换行，每块行数相同）；全文查破折号和体例禁用的对比句式；用 `tools/term_consistency.py` 的 `TERMS` 只查附录这一节，191 处都用了约定的译法。
- 发现并修改：
  - 第 73 块 “you may well find that you wish to learn more about building your own formal mathematical models of systems”：初稿漏了 your own，补上后又和前面的“自己想”重复，改为“自己想进一步学习怎样亲手为系统建立正式的数学模型”。
  - 第 74 块 “The following model equations are those used for the nine dynamic models discussed in chapters 1 and 2.”：初稿“下面的模型方程，用于……九个动态模型”像是在说方程的用途，改为“下面是第 1 章和第 2 章讨论过的九个动态模型所用的方程”。
  - 第 111 块 “starts at 1 when the resource is fully stocked, but falls (non-linearly)”：初稿漏了 but，补“但会”。
  - 第 105 块 “for Figure 41, price starts at 1.2 when yield per unit capital is high”：初稿“用于图 41 时，价格在……高时”两个“时”挨得太近，改为“在图 41 里，价格在单位资本产量高时从 1.2 开始”。
  - 第 10 块 “Systems organized in such a way as to create a larger system. Subsystems within systems.”：初稿第二句加了“也就是”，原文只是并列的两个短语，删去。
  - 第 51 块 “When the state of one stock is determined by trying to surpass the state of another stock—and vice versa—then there is a reinforcing feedback loop”：初稿拆成两句后，When 的条件关系弱了，改回“如果……而另一个存量也是这样，那么就有一个增强回路”。
  - 第 13 块 “where the cause does not produce a proportional (straight-line) effect”：初稿一句里三个“关系”，改为“其中原因产生的效果不成比例（不呈直线）”。
  - 第 61 块 “If you are the one with an unsupportable dependency”：初稿“陷入了难以为继的依赖的人”拗口，改为“如果你就是那个依赖已经难以为继的人”。
  - 第 43、45 块：“各方都满意、能让所有目标都实现”两个“都”，改为“让各方满意、所有目标都能实现”；“有一种大家共享的资源时”改为“一种资源由大家共享时”。
  - 和第 2 章译稿对齐：第 2 章的中文译稿（`zh-cn/14-2-a-brief-visit-to-the-systems.md`）在我翻译期间已经写出。系统原理汇总里来自第 2 章的 12 条原理，我的初稿是独立译的，后来改成和第 2 章页边原理的现有译文一致：英文相同的照抄；英文略有不同的，只在不同处改，例如第 2 章写 no physical system can grow forever、toward a constraint or limit，附录写 no system、toward a limit，中文相应写“没有哪个系统”“趋向某种极限的量”。模型方程里的 fertility 也照第 2 章写“生育率”，deliveries 照第 2 章写“到货量”，inventory of cars on the lot 写“停车场上的汽车库存”，very leaky house 照第 2 章的“漏热”写“非常漏热的房子”。
- 写法上的决定，供主会话参考：
  - 术语表条目：照正文粗体定义的写法括注英文，例如“**基模**（archetypes）：”，括注用英文条目名的小写。这是我加的格式，原文条目只有英文词加冒号；如果主会话觉得术语表里不必括注，删掉 18 处括注即可。
  - 页边原理：第 1 章的 10 条照样章一字不差。de-coupled and independent 和第 1 章的 decoupled and to be independent 在中文里没有区别，两处都写“存量让流入量和流出量可以脱钩、各自独立”。第 2 章原理 can only affect 和附录 can affect only 意思相同，中文都写“只能影响”。第 1 章正文的三条浴缸原理是 As long as the sum of all inflows…，附录写 If the sum of inflows…，中文相应写“如果流入量之和大于流出量之和”。
  - 干预系统的 12 个位置：照术语表“两处出现的标题”写成“**12. 数字：** 常数和参数……”，冒号后面加空格，粗体才能正常渲染。附录第 12 条是 subsidies, taxes, and standards，写“补贴、税收和标准”；第 3 条只写 The purpose of the system，写“系统的目的”。
  - 陷阱和出路：段首标签写“*陷阱*：”“*出路*：”。第 49 块滑向低绩效的出路，最后一句 Set up a drift toward high performance! 写“让系统滑向高绩效！”，保留和陷阱名“滑向低绩效”相对的双关。第 64 块 “not in the direction of beating the rules, but in the direction of achieving the purpose of the rules” 避开禁用句式，写成“别用在钻规则的空子上，转而用在实现规则的目的上”。
  - 模型方程：变量名译成中文并保留斜体（*浴缸里的水量(t)*）；Stock: 写“存量：”，Initial stock value(s): 写“存量初始值：”，Run time 写“运行时长”，Converter(s) 写“转换器”；“. . . for …”写“……用于……”，for time 0 to 5 写“时间从 0 到 5”；minimum of A or B 写“A 和 B 中的较小值”，maximum 写“较大值”。$100、$/年、°C、% 照写；gal、minutes、hours、days、years 写“加仑、分钟、小时、天、年”。
  - 小数 .009、.021、.030 写成 0.009、0.021、0.030，数值不变，照中文习惯补上整数位的 0。6.6 billion people 写“66 亿人”。
  - 两条译者注：照术语表“原文疑点”一条，For Figures 14–20 和 for Figures 30–40 照原文写“图 14 到 20”“图 30 到 40”，各加一条译者注。第 2 章核对过：图 14 是第 1 章的“资本的再投资”，恒温器的图是 15 到 20；不可再生资源模型的图是 37 到 41，图 30 到 36 是汽车库存模型。
- 检查：
  - `site.py status` 显示 111/111；`book.compile_chapter` 编译这一节通过，两条译者注都渲染成“译者注”按钮。
  - 渲染后的中文页面文字里没有残留的星号；每块的斜体、粗体个数和英文相同。
  - 本节没有人名；机构和产品名 STELLA、iThink、Vensim、isee systems、Ventana Systems、High Performance Systems 照写原名，Inc. 写“公司”。
  - 全节中文没有破折号（模型方程里表示减号的 – 照原文保留），也没有体例禁用的对比句式。
- 未决：
  - 系统原理汇总里来自第 2 章的 12 条，现在跟的是第 2 章还没审校的译稿；来自第 3 章（4 条）和第 4 章（9 条）的原理，以及八种陷阱和出路的段落（第 5 章方框里有几乎相同的英文），是我独立译的。第 5 章的中文译稿在我完稿时已经写出，方框里的陷阱和出路和附录的译文措辞不同；术语表只要求两处的陷阱名一致，所以我没有照抄这份还没审校的译稿，建议第 5 章审校后，主会话逐句挑定一个版本，两处用同一句中文。这几章定稿后，要按术语表“页边原理和附录汇总”一条回查附录，让英文相同的句子中文一字不差。第 5 章方框和附录的英文差别只有两处：政策阻力一段第 5 章写 system stock、附录写 system state；滑向低绩效的出路最后一句，第 5 章写 Use the same structure to set up a drift toward high performance!，附录只写 Set up a drift toward high performance!。（已定：以附录的写法为准，见文末“状态”第 2 条。）
  - fertility 照第 2 章译稿写“生育率”。模型里的定义是每 1000 人中的出生人数，人口学上叫“出生率”更准确；全书怎样写，留给主会话统一定。（已定：写“出生率”，见文末“状态”第 3 条。）
  - 第 2 条译者注说“大概是指图 38 到 40”，依据是 `review/source.md` 的判断和同一段价格一行（for Figures 38, 39, and 40）的写法；图 41 的增长目标原文没有明说。

## 原文疑点

| 位置 | 原文 | 处理 |
| --- | --- | --- |
| 第 4 块 | also know as a “negative feedback loop” | 应为 also known as，`review/source.md` 已列。照正确的意思译“也叫”，不加注 |
| 第 86 块 | **Thermostat**—For Figures 14–20 | 恒温器的图是 15 到 20，`review/source.md` 已列。照原文写“图 14 到 20”，加译者注 [^t1] |
| 第 105 块 | *growth goal* = *capital* × 10% . . . for Figures 30–40 | 这个模型的图是 37 到 41，`review/source.md` 已列。照原文写“图 30 到 40”，加译者注 [^t2] |
| 第 93 块 | *fertility* starts at .021, drops to .009, but then rises .030 | 少了 to，应为 rises to .030。照正确的意思译“又回升到 0.030”，不加注 |
| 第 109 块 | Converters: *capital lifetime* = 20 | 上一个模型写 20 years，这里没有单位，应该也是 20 年。照原文写“= 20”，不补单位 |

## 2. 双语审校

- 执行者：另一个独立上下文的 agent（Opus 5.5），没有参与翻译。
- 范围：全节 111 块逐块对照英文：术语表 18 条、系统原理汇总 40 条、八种陷阱和出路、干预系统的 12 个位置、15 条准则、9 个模型的方程，以及两条译者注。另外把系统原理汇总和第 1 到 4 章的页边原理逐句对照，把陷阱和出路的段落和第 5 章方框对照，按第 1、2 章的图题核对了两条译者注里的图号。
- 发现：16 条；编辑逐条查对英文和中文后，采纳 15 条，不采纳 1 条。
  - 采纳，和第 4 章页边原理对齐：来自第 4 章、英文一字不差的原理里，有 6 条中文和第 4 章不同，违反术语表“英文相同的，中文一字不差”一条。照第 4 章改为：“世界是一个连续体。”“在任何时刻，对系统最重要的输入，就是限制作用最大的那个输入。”“任何有多种输入和输出的实体，都被层层限制包围着。”（Any physical entity with multiple inputs and outputs is surrounded by layers of limits，第 4 章小节标题也是“层层限制”，原译“一层又一层的极限”）“反馈回路里有很长的延迟时，某种预见就必不可少。”“系统里每个行动者的有限理性，不一定会带来增进整个系统福祉的决策。”“我们的模型远远不能完整地反映真实的世界。”（Our models fall far short of representing the real world fully，原译“表现真实世界”）
  - 采纳，两处一起改：Everything we think we know about the world is a model. 附录原译“我们自以为知道的关于世界的一切”，“的”字叠用；第 4 章写“我们自以为对世界的一切认识”，缺一个“的”，可以读成“我们以为：对世界的一切认识都是模型”。附录改为“我们对世界自以为知道的一切，都是模型。”第 4 章第 15 行的页边原理要由主会话同步改成同一句，改之前两处不一致。
  - 采纳，意思：The system deteriorates; more and more of the solution is then required. 原译“于是需要越来越多的解决办法”，容易读成需要越来越多种办法；原文说的是同一种办法用量越来越大，和上瘾的意思对应，改为“于是这种解决办法就得越用越多”。
  - 采纳，歧义：Rules to govern a system can lead to rule-beating 原译“管理系统的规则”，“管理系统”容易读成一个名词，改为“用来治理系统的规则”。If you are the one with an unsupportable dependency 原译“如果你就是那个依赖已经难以为继的人”，可以读成“依赖一个已经难以为继的人”。审校者建议的“依赖干预、已经难以为继的一方”让“难以为继”落到了“一方”上，原文的 unsupportable 修饰 dependency，所以改为“如果你就是依赖干预的一方，而且这种依赖已经难以为继”。
  - 采纳，翻译腔和生造的说法：If you are the intervenor, work in such a way as to restore or enhance the system’s own ability to solve its problems, then remove yourself. 原译“你的工作方式应该是恢复……能力，然后自己退出”，改为“就要设法恢复或增强系统自己解决问题的能力，然后抽身退出”。every user benefits directly from its use 原译“从使用它当中直接得到好处”，改为“直接从使用中得到好处”。(i.e., *sales* smoothed over *perception delay*) 原译“（即 *销量* 在 *感知延迟* 内经过平滑）”，改为“（即在 *感知延迟* 内对 *销量* 做平滑）”。Yield per unit capital increases overall from least efficient in Figure 43 … 原译“整体上逐图提高”，改为“总体上依次提高”。when the resource is either fully stocked or completely depleted 原译“资源满额”，审校者建议“资源量饱和”；“饱和”多用于溶液和市场，这里两处都改为“资源存量最大”，和上一个模型的“资源存量高时”说法相近。
  - 采纳，译者注：第 2 条译者注原来推测 for Figures 30–40 “大概是指图 38 到 40”。同一行后半句说图 40 另取 6%、8%、10%、12% 做四次对比运行，第 2 章正文又说 If you compare Figure 41 with Figure 38, where price was held constant，可见图 41 的增长目标也是 10%。改为“这里大概是指图 38 到 41，其中图 40 另作四次对比运行。”
  - 采纳，留给主会话处理：八种陷阱和出路的段落，英文和第 5 章方框几乎一字不差，中文却是两套（例如附录“抹黑战”“不断升高的音量”，第 5 章“抹黑运动”“不断升级的喧闹”）。第 5 章还没有定稿，本轮没有改附录的这些段落；第 5 章定稿后由主会话逐句选定一个版本，英文不同的两处（附录 system state 和第 5 章 system stock，以及第 5 章多出的 Use the same structure to）保留差别。第 5 章方框里也有上面改过的两句（“需要越来越多的解决办法”“管理系统的规则”），建议照附录现在的写法一并修改。（已定：第 5 章方框已照附录改，见文末“状态”第 2 条。）
  - 不采纳：fertility 写“生育率”还是“出生率”。审校者认为第 2 章两种写法混用、全书不统一。核对后，第 2 章的“出生率”都对应英文 birth rate（第 2 章英文第 85、125、127、195 行），“生育率”都对应 fertility，两个英文词各有固定的译法。附录写“生育率”和第 2 章一致，同一行又写明“即每 1000 人中有 21 人出生”，读者不会误解成按育龄妇女计算的比率。所以本节不改；fertility 是否全书改成“出生率”，留给主会话决定。（已定：全书写“出生率”，附录已改，见文末“状态”第 3 条。）
- 审校者的总体判断：附录译文质量较高，可以作为定稿基础。没有发现漏译、增译或否定写反的地方；模型方程里的数字、单位、图号、最大值和最小值的写法都核对无误；`site.py status` 显示 111/111，硬换行两边都是 124 处；全文没有破折号，也没有体例禁用的对比句式；节标题、陷阱名、杠杆点和准则的译法和术语表一致，两条译者注所说的图号和第 1、2 章的图题相符。主要问题是系统原理汇总里来自第 4 章的原理措辞和第 4 章不一致，以及陷阱和出路的段落和第 5 章方框是两套中文；其余是几处读者会卡住的单句措辞、一处意思上的细微偏差和第 2 条译者注的推测，改动都在单句范围内。

## 3. 中文通读

- 执行者：编辑 agent（Opus 5.5）。
- 范围：从节名读到第 2 条译者注，看行文是否顺、有没有重复、指代是否清楚、本节里的术语和名称是否前后一致。
- 发现并修改：
  - 竞争升级的陷阱段：“最终会以某一方的崩溃告终：指数增长不可能永远持续下去。”冒号后面读起来像另起一个论断。原文是 the spiral will be stopped by someone’s collapse—because exponential growth cannot go on forever，改为“告终，因为指数增长不可能永远持续下去”，因果关系更清楚，也和第 5 章方框的写法相同。
  - 双语审校改过的句子放回上下文里重读：“依赖干预的一方”和上一段的“干预者”对应，读得通；“资源存量最大”和同一模型下文的“资源量的中段”“资源存量减少”说法相容；“层层限制”和下一条“增长总有极限”分别对应英文 layers of limits 和 limits to growth，两处用词不同是照第 4 章的写法。
  - 本节术语：`tools/term_consistency.py` 对附录没有报出不一致。“受不可再生资源约束的可再生存量”和第 2 章小节标题“受不可再生存量约束的可再生存量”不同，原因是英文一处写 Nonrenewable Resource、一处写 Nonrenewable Stock，保留。
  - 以上改动都回查过英文。
- 检查：`site.py status` 显示附录 111/111；`site.py check` 的草稿构建通过；全文没有破折号和体例禁用的对比句式；行尾硬换行两边都是 124 处。

## 状态

- 没有未解决的意义问题。译者自检“未决”里关于第 2 条译者注图号的一条，已在双语审校中改定。
- 还需要主会话处理的一致性问题（2026-11-05 术语表“全书统一的写法（译完后定）”已对下面四条作出决定，都已办完）：
  1. 第 4 章第 15 行页边原理改成“我们对世界自以为知道的一切，都是模型”，和附录一致。第 4 章审校时如果再改其他 8 条原理，附录要跟着改。（已定：术语表“页边原理”一条，第 4 章开头的“三条真理”第 1 条和页边方框都已照附录改；附录里连续体、层层限制等几句照第 4 章写，以后改任何一处，另一处跟着改。）
  2. 第 5 章定稿后，统一附录和第 5 章方框里陷阱和出路的中文。（已定：术语表“第 5 章方框和附录‘摆脱系统陷阱’”一条，以附录的写法为准，第 5 章方框已照附录改；公地悲剧的出路写“监管所有使用者对这种资源的取用”，富者愈富的出路写“采取拉平赛场的政策”，附录已改。第三轮逐段核对过，两处只剩 system state 和 system stock、Use the same structure to 这两处照英文保留的差别。）
  3. fertility 全书写“生育率”还是“出生率”。（已定：术语表“出生率和生育率”一条，人口模型的 fertility 写“出生率”，附录模型方程 5 处已改。）
  4. `review/source.md` 对 for Figures 30–40 写的是“应是 38 到 40”，第 2 条译者注现在写“大概是指图 38 到 41”，建议同步。（已定：术语表“附录图号的译者注”一条，`review/source.md` 已同步为“大概指图 38 到 41”。）

## 第三轮：GPT-6 Astra 独立审校

- 审校者：GPT-6 Astra，通过 Codex 运行，只读，和译者属于不同的模型家族。
- 发现：3 条。逐条找到中英文对应的句子，读过上下文后核实：成立并修改 1 条，不成立 2 条。
- 成立并修改：
  - 模型方程第一段 “you may well find that you wish to learn more about building your own formal mathematical models of systems”：formal 在这里指用明确的数学形式写出来的模型，和头脑里的心智模型相对；中文的“正式的”多指官方的、合乎规矩的，读者容易理解偏。原译“自己想进一步学习怎样亲手为系统建立正式的数学模型”，改为“自己想进一步学习怎样亲手为系统建立形式化的数学模型”。审校者建议整句改成“自行建立形式化的系统数学模型”；这句的其余部分在译者自检时已经调过（补了 your own，去掉和“自己想”的重复），所以只换这一个词。
- 不成立，保留原译：
  - 富者愈富的出路 “Diversification, which allows those who are losing the competition to get out of that game and start another one”，现译“多样化，让在竞争中落败的人能退出那场游戏，另开一局”。审校者认为“另开一局”会被读成在同一场竞争里重新开始，建议改为“退出原有竞争，转向其他领域”。前半句已经说了退出那场游戏，“另”字也表明是另一场游戏，读者不会理解成回到原来的竞争；原文用的是游戏的比喻，建议的写法把比喻换成了解释，而第 5 章正文讲多样化的两段（物种利用新资源，企业开发不直接竞争的新产品）已经把这层意思讲清楚。这一段和第 5 章方框逐字相同，按术语表要两处一起改，单改附录会让两处不一致。
  - 竞争升级的陷阱 “When the state of one stock is determined by trying to surpass the state of another stock—and vice versa—then there is a reinforcing feedback loop”，现译“如果一个存量的状态取决于要胜过另一个存量的状态，而另一个存量也是这样，那么就有一个增强回路”。审校者认为句法生硬，这是文风上的意见。现译保留了原文 the state of one stock、is determined by 和 vice versa 的意思，条件关系也清楚；建议的“双方都以超过对方的存量水平为目标来调整各自的存量”丢了 state，也把“由……决定”改成了“调整”。译者自检时比较过拆成两句的写法，最后选了现在的句式。这一段同样和第 5 章方框逐字相同。
- 按全书统一的写法修改：本轮 0 处。术语表“全书统一的写法（译完后定）”里和附录有关的条目，脚本此前已经在附录改了 7 处：人口模型里的 *生育率* 改为 *出生率* 5 处；公地悲剧的出路“管制所有使用者对这种资源的取用”改为“监管所有使用者对这种资源的取用”；富者愈富的出路“采取让竞争环境变得公平的政策”改为“采取拉平赛场的政策”。本轮再逐条核对：数字（模型方程里的参数、初始值和时间用阿拉伯数字，“九个动态模型”“三次模型对比运行”写汉字）、physical（实体系统、实体、非物质的反馈、物理定律）、“坚持绝对的绩效标准”、第 4 章页边原理“我们对世界自以为知道的一切，都是模型”、第 2 条译者注里的图号，附录都已经照这些条目写，没有需要再改的地方。八种陷阱的 16 段和第 5 章方框逐段比对，只剩术语表列出的两处照英文保留的差别（system state 和 system stock，Use the same structure to）。上文“状态”一节里留给主会话决定的 4 条，术语表新一节都已定下，已在原处注明“已定”；译者自检和双语审校里对应的几句也加了同样的注。
- 对英文原文的疑问：
  - 审校者列了 5 条。其中 4 条前面的“原文疑点”表和 `review/source.md` 已经列过：also know as 和 rises .030 照正确的意思译，不加注；For Figures 14–20 和 for Figures 30–40 照原文写，各有一条译者注。
  - 新的一条，核实后成立：汽车库存模型 *orders to factory* 的公式，原文写 “maximum of (*perceived sales* + *discrepancy*) or 0 . . . for Figure 32; maximum of (*perceived sales* + *discrepancy*/*response delay*) or 0 . . . for Figures 34–36”。下文给图 32 设的 *response delay* 是 3 天，第 2 章正文（英文第 229 行）也说经销商每次订货只补上缺口的三分之一；图 30 的三种延迟都是 0，除以反应延迟的公式在图 30 算不出来。所以不除以反应延迟的公式更可能是图 30 用的，除以反应延迟的公式应该用于图 32 到 36。译文照原文写“用于图 32”“用于图 34 到 36”，没有加注，因为术语表“原文疑点”一条只给两处图号加译者注。要不要加第三条译者注、列入 `review/source.md`，留给主会话决定。
- 核实与修改：agent（Opus 5.5）。改完后运行 `python3 scripts/site.py status thinking-in-systems`：附录显示 111/111，全书 1115/1115 块都已翻译；附录英文没有脚注，两条译者注 [^t1]、[^t2] 保留。改动只在一行之内，行数和行尾硬换行不变；中文没有破折号，也没有体例禁用的对比句式。
