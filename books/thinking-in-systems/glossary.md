# 术语表

翻译前根据 `review/terms/` 里的统计数据裁定（来源和门槛见 [review/terms/README.md](review/terms/README.md)）。“出现次数”和“首次出现”由 `tools/term_stats.py` 按 `TERMS` 里的正则统计英文正文，不含脚注和标题；按词形匹配，同词根的普通用法也会算进去，例如 system、model、rule、structure。状态都是“初定”，由 Claude 裁定，等用户确认；改动时要回查已经译完的章节。

这本书的 EPUB 没有纸质版索引。作者自己在附录里写了一张术语表（System Definitions: A Glossary，18 条），正文第一次给出定义的词用粗体排出，第 1 章的星号注释说明了这一点。这 18 条都收进下面的核心概念，译法和附录术语表的条目名保持一致。

## 体例

- **人名**：用 [review/terms/people-zh.tsv](review/terms/people-zh.tsv) 的译名。每节第一次出现时在中文名后括注英文原名，写法照这一处的原文，例如“杰伊·福里斯特（Jay Forrester）”“杰伊·W.福里斯特（Jay W. Forrester）”，之后只写中文。只写姓或只写名的（a Brezhnev、Jay、Dana、Nathan）也照这个办法。寓言和漫画里的人物（霍拉、坦普斯、卡尔文、霍布斯、苏茜）也括注。脚注里的人名照写原文。
- **署名行**：章首题词和引文后面的署名行，英文以“—”开头，中文不写破折号，写成“罗素·艾可夫（Russell Ackoff），运筹学家”。署名里的身份照原文译（economist 写“经济学家”，18th century poet 写“18 世纪诗人”），书名和报刊名按下一条。阅读器按英文一侧认出署名行，中文不用加任何符号。
- **机构、产品、地名**：见下面“机构、产品与地名”。没有通行中文名的照写原名，和汉字之间加空格。
- **书名、报刊、文章**：正文里用《》，每节第一次出现时括注原题，原题用斜体，例如《增长的极限》（*The Limits to Growth*）；文章、专栏、讲演的题目用引号，原题也用引号、不用斜体，例如“全球公民”专栏（“The Global Citizen”）。有通行中译本的书用中译本的书名。《国际先驱论坛报》不括注，见“全书统一的写法”。脚注和参考书目条目里的出处保留原文，不加书名号。
- **数字**：年份、日期、百分比和多位数字用阿拉伯数字，和汉字之间加空格，例如“1972 年”“66 亿人”“2%”。金额换算成中文的万、亿：$1 billion 写“10 亿美元”，$12.5 million 写“1250 万美元”。细则见“全书统一的写法”。
- **温度和单位**：温度照原文的符号写，例如“18°C（65°F）”“37°C（98.6°F）”。英制单位照原文译出（加仑、英亩、英里），数字要紧时括注公制。模型方程里的单位写中文（加仑、分钟、小时、年），°C、%、$ 照写。
- **引语和俗语**：第 5、6 章的报纸摘录照新闻文体译，引文里的省略号“. . .”写“……”。引言里的俗语用通行的中文说法，例如 Don’t put all your eggs in one basket 写“不要把所有鸡蛋放在一个篮子里”，The rich get richer and the poor get poorer 写“富者愈富，贫者愈贫”；《马可福音》4:25 用和合本：“因为有的，还要给他；没有的，连他所有的也要夺去。”
- **脚注**：出处（作者、书名、刊名、出版地、出版社、日期、页码、网址）保留英文原样；连接的说法和解释性的句子要翻译。常见格式：
  - Poul Anderson, quoted in Arthur Koestler, *The Ghost in the Machine* … → Poul Anderson，转引自 Arthur Koestler, *The Ghost in the Machine* …
  - Paraphrased from Herbert Simon, … → 转述自 Herbert Simon, …
  - See Jonathan Kozol, … → 见 Jonathan Kozol, …
  - quoted in ibid, 44. → 转引自同上，44。
  - Thanks to David Holmstrom of Santiago, Chile. → 感谢智利圣地亚哥的 David Holmstrom。
  - This story was told to me by Ed Roberts of Pugh-Roberts Associates. → 这个故事是 Pugh-Roberts Associates 的 Ed Roberts 讲给我听的。
  - 第 1 章脚注 2 写“粗体词的定义见附录的术语表。”
- **脚注标记**：`[^n]` 放在中文里对应词句的后面，编号与英文一致。第 1 章的星号注释是脚注 2，所以第 1 章的脚注 3 到 6 对应原书注释 2 到 5。
- **粗体定义**：正文用粗体排出、附录术语表收录的 18 个词，中文也用粗体，并在第一次出现的这一处括注英文，例如“**存量**（stock）”。页边原理是整句粗体，中文也整句粗体。
- **页边原理和附录汇总**：页边原理（引文块里的粗体句子）在附录 Summary of Systems Principles 里又出现一次。英文相同的，中文一字不差；英文略有不同的（例如第 1 章的 decoupled and to be independent 和附录的 de-coupled and independent），中文也只在这些地方不同。对照表见 [review/terms/principles.tsv](review/terms/principles.tsv)。第 5 章的八种陷阱、第 6 章的十二个杠杆点、第 7 章的十五条准则，在附录里也各出现一次，译名照下面“两处出现的标题”。
- **斜体**：原文用斜体强调的词句，中文也用 `*…*` 标出（阅读器把中文斜体显示成加重的无衬线字体）。附录模型方程里斜体的模型变量名译成中文，保留斜体，例如 *water in tub(t)* 写 *浴缸里的水量(t)*。
- **图题和图号**：图题开头的 Figure 12. 写“图 12：”。分图上方的 A: Growth 这类标签写“A：增长”。正文里的 (See Figure 46.) 写“（见图 46。）”，Figures 14–20 写“图 14 到 20”。图片里的英文不改。
- **硬换行**：附录“干预系统的位置”和模型方程的段落，每行行尾有两个空格，中文照样保留，行数相同。两首诗（第 3 章斯威夫特、第 4 章博尔丁）也是一行一个硬换行。
- **分隔线**：分隔线 `---` 只写在英文文件里。
- **破折号和句式**：中文译文不用破折号（——），原文的破折号按意思改成逗号、冒号、括号或另起一句；表示范围的短横线写“到”，例如“1941 年到 2001 年”“图 15 到 20”。也不用“不是……而是……”这种句式，换成直接的说法。

## 各节标题

| 章节 id | 英文 | 中文标题（`#` 一级标题照这一列写） |
| --- | --- | --- |
| dedication | Dedication | 献辞 |
| authors-note | A Note from the Author | 作者的话 |
| editors-note | A Note from the Editor | 编者的话 |
| epigraph | Epigraph | 题词 |
| introduction | Introduction: The Systems Lens | 引言 系统的视角 |
| part1 | Part One: System Structure and Behavior | 第一部分 系统的结构与行为 |
| ch01 | 1. The Basics | 第 1 章 基本概念 |
| ch02 | 2. A Brief Visit to the Systems Zoo | 第 2 章 系统动物园速览 |
| part2 | Part Two: Systems and Us | 第二部分 系统与我们 |
| ch03 | 3. Why Systems Work So Well | 第 3 章 系统为什么运转得这么好 |
| ch04 | 4. Why Systems Surprise Us | 第 4 章 系统为什么出人意料 |
| ch05 | 5. System Traps . . . and Opportunities | 第 5 章 系统陷阱……与机遇 |
| part3 | Part Three: Creating Change—in Systems and in Our Philosophy | 第三部分 创造变革：改变系统，也改变我们的理念 |
| ch06 | 6. Leverage Points—Places to Intervene in a System | 第 6 章 杠杆点：干预系统的位置 |
| ch07 | 7. Living in a World of Systems | 第 7 章 生活在系统的世界里 |
| appendix | Appendix | 附录 |
| bibliography | Bibliography of Systems Resources | 系统学习资源书目 |
| acknowledgments | Editor’s Acknowledgments | 编者致谢 |
| about-the-author | About the Author | 关于作者 |

已出版的中文版（《系统之美》，邱昭良译，2012 年）把各章意译成“系统之基础”“系统大观园”“系统之美”“系统之奇”“系统之危与机”等，这里只作参考，标题按原文的意思译，和正文的说法对得上（例如第 2 章正文反复说“系统动物园”）。译者读完一章后，如果觉得标题另有更贴切的译法，在汇报里提出，由主会话统一修改。

### 两处出现的标题

第 5 章的陷阱、第 6 章的杠杆点和第 7 章的准则，在附录里又各列一遍。两处的中文要一致。

| 英文 | 中文 | 出现的地方 |
| --- | --- | --- |
| Policy Resistance—Fixes that Fail | 政策阻力：失效的对策 | 第 5 章 `##`；附录 `###` 只写 Policy Resistance，写“政策阻力” |
| The Tragedy of the Commons | 公地悲剧 | 第 5 章、附录 |
| Drift to Low Performance | 滑向低绩效 | 第 5 章、附录 |
| Escalation | 竞争升级 | 第 5 章、附录 |
| Success to the Successful—Competitive Exclusion | 富者愈富：竞争排斥 | 第 5 章；附录只写 Success to the Successful，写“富者愈富” |
| Shifting the Burden to the Intervenor—Addiction | 把负担转嫁给干预者：上瘾 | 第 5 章；附录只写前半，写“把负担转嫁给干预者” |
| Rule Beating | 钻规则的空子 | 第 5 章、附录 |
| Seeking the Wrong Goal | 追求错误的目标 | 第 5 章、附录 |
| THE TRAP: … / *Trap*: | 陷阱：…… / *陷阱*： | 第 5 章方框标题 THE TRAP: POLICY RESISTANCE 写“陷阱：政策阻力”；附录段首的斜体标签写“*陷阱*：” |
| THE WAY OUT / *The Way Out*: | 出路 / *出路*： | 第 5 章方框标题；附录段首的斜体标签 |
| 12. Numbers | 12. 数字：常数和参数，如补贴、税收、标准 | 第 6 章 `##` 写成“12. 数字：……”，附录写成“**12. 数字：** ……”，冒号后面的说明两处照各自的英文译 |
| 11. Buffers | 11. 缓冲：起稳定作用的存量相对于其流量的大小 | 同上 |
| 10. Stock-and-Flow Structures | 10. 存量流量结构：实体系统及其交汇节点 | 同上 |
| 9. Delays | 9. 延迟：时间长短相对于系统变化的速度 | 同上 |
| 8. Balancing Feedback Loops | 8. 调节回路：反馈的强度相对于它们要纠正的冲击 | 同上 |
| 7. Reinforcing Feedback Loops | 7. 增强回路：驱动回路的增益强度 | 同上 |
| 6. Information Flows | 6. 信息流：谁能获得信息、谁不能获得信息的结构 | 同上 |
| 5. Rules | 5. 规则：激励、惩罚、约束 | 同上 |
| 4. Self-Organization | 4. 自组织：增加、改变或演化系统结构的力量 | 同上 |
| 3. Goals | 3. 目标：系统的目的或功能 | 同上；附录只写 The purpose of the system，写“系统的目的” |
| 2. Paradigms | 2. 范式：系统（它的目标、结构、规则、延迟、参数）赖以产生的思维模式 | 同上 |
| 1. Transcending Paradigms | 1. 超越范式 | 同上 |
| Get the Beat of the System | 摸清系统的节拍 | 第 7 章 `##`；附录“生活在系统世界里的准则”第 1 条 |
| Expose Your Mental Models to the Light of Day | 把你的心智模型摆到阳光下 | 第 2 条 |
| Honor, Respect, and Distribute Information | 珍视、尊重并传播信息 | 第 3 条 |
| Use Language with Care and Enrich It with Systems Concepts | 谨慎用词，并用系统概念丰富语言 | 第 4 条 |
| Pay Attention to What Is Important, Not Just What Is Quantifiable | 关注重要的东西，别只关注能量化的东西 | 第 5 条 |
| Make Feedback Policies for Feedback Systems | 为反馈系统制定反馈式政策 | 第 6 条 |
| Go for the Good of the Whole | 追求整体的利益 | 第 7 条 |
| Listen to the Wisdom of the System | 倾听系统的智慧 | 第 8 条 |
| Locate Responsibility in the System | 在系统内部落实责任 | 第 9 条（附录写 within the system，同样译） |
| Stay Humble—Stay a Learner | 保持谦逊，做一个学习者 | 第 10 条 |
| Celebrate Complexity | 拥抱复杂性 | 第 11 条 |
| Expand Time Horizons | 拓展时间视野 | 第 12 条 |
| Defy the Disciplines | 打破学科的界限 | 第 13 条 |
| Expand the Boundary of Caring | 扩大关怀的边界 | 第 14 条 |
| Don’t Erode the Goal of Goodness | 不要侵蚀向善的目标 | 第 15 条 |

### 附录小节、方框和插曲的标题

| 英文 | 中文 |
| --- | --- |
| System Definitions: A Glossary | 系统术语表 |
| Summary of Systems Principles | 系统原理汇总 |
| Springing the System Traps | 摆脱系统陷阱 |
| Places to Intervene in a System (in increasing order of effectiveness) | 干预系统的位置（按效果由弱到强排列） |
| Guidelines for Living in a World of Systems | 生活在系统世界里的准则 |
| Model Equations | 模型方程 |
| Chapter One / Chapter Two（模型方程的小标题） | 第 1 章 / 第 2 章 |
| THINK ABOUT THIS | 想一想 |
| A NOTE ON LANGUAGE | 关于用词 |
| HINT ON REINFORCING LOOPS AND DOUBLING TIME | 提示：增强回路与倍增时间 |
| A NOTE ON READING GRAPHS OF BEHAVIOR OVER TIME | 怎样读行为随时间变化图 |
| QUESTIONS FOR TESTING THE VALUE OF A MODEL | 检验模型价值的几个问题 |
| How to read stock-and-flow diagrams. | 怎样读存量流量图。 |
| Interlude • … | 插曲 • ……（保留圆点，前后各一个空格），例如“插曲 • 盲人摸象” |
| One-Stock Systems / Two-Stock Systems | 单存量系统 / 双存量系统 |

## 全书统一的写法

开始翻译前先定下来的写法。译完后编辑再提出各章不一致的地方，补在这一节。

- **数字**：一到十，以及带“几、十几、数百、上千”的约数，用汉字（三种东西、几十年）；11 以上的确数用阿拉伯数字（49 幅图、30 年）；万和亿前面的数字也用阿拉伯数字（66 亿人）；年份、日期、钟点、金额、百分比、温度一律用阿拉伯数字。原文用英文单词写的章号（Chapter One、Chapters One and Two）写“第 1 章”“第 1 章和第 2 章”。倍数写“增长到原来的 N 倍”，不写“增长了 N 倍”；doubling 写“翻一番”或“增长一倍”。
- **书名、报刊括注**：每节第一次出现时括注原题，原题用斜体。《国际先驱论坛报》（International Herald Tribune）是作者 1992 年那一周读的报纸，第 5、6 章的署名行里反复出现，一律不括注。指本书时，*Thinking in Systems* 写《系统之美》，沿用中文版书名。
- **人名**：名人也照常在每节第一次出现时括注英文。脚注里的人名，无论在出处里还是在说明句里，一律照写英文。参考书目条目照写英文，条目后面的说明文字里提到的人照这张表译。
- **系统的组成**：function 和 purpose 分别写“功能”和“目的”，goal 写“目标”，三者不混用。第 1 章“关于用词”方框专门区分了 function 和 purpose。
- **回路**：balancing feedback loop 和 balancing loop 都写“调节回路”，reinforcing feedback loop 和 reinforcing loop 都写“增强回路”；不带 loop 的 balancing feedback、reinforcing feedback 写“调节反馈”“增强反馈”。图里的 B 和 R 照写。附录术语表的条目名写“调节回路”“增强回路”。
- **存量和库存**：stock 写“存量”，inventory 写“库存”，股市里的 stocks 写“股票”，stock market 写“股市”。capital stock 写“资本存量”。
- **physical**：和信息相对的 physical flow 写“物质流动”；physical elements、physical entity、physical system、physical stock 写“实体要素”“实体”“实体系统”“实体存量”，和第 10 个杠杆点里的“实体系统”一致；physical capital 写“实物资本”；physical things 和 A stock does not have to be physical 这类说法写“有形的”；physical law(s) 写“物理定律”。第 1 章样章已按这样写。
- **韧性和稳定**：resilience 写“韧性”，stability 写“稳定性”。作者在第 3 章专门说两者不同，译文里不要互换。
- **两个名字的陷阱**：drift to low performance 写“滑向低绩效”，原文另说的 eroding goals 写“目标侵蚀”，boiled frog syndrome 写“温水煮青蛙综合征”。policy resistance 写“政策阻力”，fixes that fail 写“失效的对策”。
- **“系统”的复合词**：systems thinking 写“系统思考”，systems thinker 写“系统思考者”，system dynamics 写“系统动力学”，systems analysis 写“系统分析”，systems zoo 写“系统动物园”。
- **脚注里的术语**：第 4 章脚注的 satisficing 写“满意即止”，第一次出现时括注原文。
- **原文疑点**：`review/source.md` 列出的原文疑点（多一个词、少一个词、拼错的词），译文按正确的意思译，不加注。附录模型方程里两处可能写错的图号（For Figures 14–20、for Figures 30–40），照原文写，各加一条译者注说明应为哪几幅图。
- **报纸摘录**：第 5、6 章引的 1992 年报纸，引文里方括号中的补充（[when taxes are expected to be higher]）照样用方括号译出。

## 核心概念

| 英文 | 首选译法 | 适用的意思 | 不要混同 | 首次出现 | 出现次数 | 状态 |
| --- | --- | --- | --- | --- | --- | --- |
| system / systems | 系统 | 一组相互连接的要素，按一定方式组织起来，实现某种功能或目的；附录术语表条目 | 体系、制度 | authors-note | 989 | 初定 |
| element | 要素 | 系统三种组成之一，可以是有形的东西，也可以是无形的东西（大学的荣誉感） | 元素（化学） | introduction | 40 | 初定 |
| interconnection / interconnected | 相互连接 / 相互连接的 | 把要素联系在一起的关系，很多通过信息流起作用；interrelated 写“相互关联” | 互联（网络） | introduction | 35 | 初定 |
| function / purpose | 功能 / 目的 | function 用于非人类系统，purpose 用于人类系统（第 1 章“关于用词”方框）；两词并列时写“功能或目的” | 目标（goal） | authors-note | 111 | 初定 |
| goal | 目标 | 调节回路要达到或维持的状态，也是第 3 个杠杆点；goal-seeking 写“寻求目标的” | 目的（purpose） | introduction | 138 | 初定 |
| structure / system structure | 结构 / 系统结构 | 存量、流量和反馈回路相互连接的方式；“结构决定行为” | 组织架构 | editors-note | 108 | 初定 |
| behavior / behavior over time | 行为 / 随时间变化的行为 | 系统随时间表现出来的模式；behavior-over-time graph 写“行为随时间变化图”；pattern of behavior 写“行为模式” | 举止、表现 | editors-note | 172 | 初定 |
| event | 事件 | 某一时刻发生的单个结果；第 4 章区分事件、行为模式和系统结构三个层次 | 行为 | editors-note | 35 | 初定 |
| surprise / system surprises | 意外 / 系统带来的意外 | 第 4 章的主题：系统的行为出乎我们的预料 | 惊喜 | introduction | 48 | 初定 |
| subsystem | 子系统 | 系统里嵌套的较小系统 |  | ch01 | 26 | 初定 |
| systems thinking / systems thinker | 系统思考 / 系统思考者 | 《第五项修炼》中译本和 2012 年中文版的说法 | 系统思维 | authors-note | 47 | 初定 |
| system dynamics | 系统动力学 | 福里斯特创立的学科和建模方法；MIT System Dynamics group 写“麻省理工学院系统动力学小组” | 动态（dynamics） | authors-note | 10 | 初定 |
| systems analysis / systems analyst | 系统分析 / 系统分析师 |  |  | authors-note | 9 | 初定 |
| systems zoo / zoo animal | 系统动物园 / 动物园里的动物 | 第 2 章的比喻，概念来自博塞尔：把常见的系统结构当作动物园里的动物逐个参观 | 系统大观园（2012 年中文版的章名） | introduction | 12 | 初定 |
| stock | 存量 | 系统里随时间积累起来的物质或信息；附录术语表条目 | 库存（inventory）、股票 | ch01 | 296 | 初定 |
| flow / inflow / outflow | 流量 / 流入量 / 流出量 | 一段时间内进入或离开存量的物质或信息；附录术语表条目；作动词时照常译“流” | 流动、通量 | ch01 | 233 | 初定 |
| stock-and-flow diagram / structure | 存量流量图 / 存量流量结构 | 第 10 个杠杆点叫“存量流量结构” |  | ch01 | 5 | 初定 |
| cloud | 云 | 存量流量图里表示流量从哪里来、到哪里去的云形符号；第 4 章 Beware of clouds! 写“当心那些云！” |  | ch01 | 21 | 初定 |
| bathtub / faucet / drain | 浴缸 / 水龙头 / 排水口 | 第 1 章的浴缸模型；流量上的 T 形符号表示“水龙头” | 阀门 | ch01 | 37 | 初定 |
| dynamic equilibrium | 动态平衡 | 流入量等于流出量，存量的水平不变；附录术语表条目 | 静态平衡、均衡 | ch01 | 8 | 初定 |
| dynamics / dynamic | 动态 / 动态的 | 系统或其组成部分随时间变化的行为；附录术语表条目 | 动力学（只用于学科名 system dynamics） | introduction | 52 | 初定 |
| decoupled / de-coupled | 脱钩 | 第 1 章原理：存量让流入量和流出量可以脱钩、各自独立 | 解耦 | ch01 | 2 | 初定 |
| inventory | 库存 | 第 2 章汽车经销商模型里的存量 | 存量（stock） | ch01 | 60 | 初定 |
| capital / capital stock | 资本 / 资本存量 | 机器、工厂等实物资本；output 写“产出”，investment 写“投资” | 资金 | ch01 | 147 | 初定 |
| depreciation / lifetime | 折旧 / 寿命 | 资本的折旧和平均寿命 |  | ch01 | 44 | 初定 |
| renewable / nonrenewable resource | 可再生资源 / 不可再生资源 | 第 2 章双存量系统 |  | ch02 | 40 | 初定 |
| stock-limited / flow-limited | 受存量限制 / 受流量限制 | 不可再生资源受存量限制，可再生资源受流量限制 |  | ch02 | 4 | 初定 |
| regeneration / extraction / harvest rate | 再生速率 / 开采速率 / 捕捞速率 | 第 2 章双存量系统里的流量；harvest 在渔业模型里写“捕捞量”，在林业里写“采伐量” |  | ch02 | 22 | 初定 |
| carrying capacity | 承载能力 |  | 容量 | ch04 | 6 | 初定 |
| feedback / feedback loop | 反馈 / 反馈回路 | 存量的变化通过决策、规则或物理规律反过来影响进出这一存量的流量，形成闭合的因果链；附录术语表条目 | 反馈环、回馈 | introduction | 233 | 初定 |
| balancing feedback loop / balancing loop | 调节回路 | 寻求目标、维持稳定的反馈回路，图中标 B；附录术语表条目；2012 年中文版同 | 平衡回路 | ch01 | 75 | 初定 |
| reinforcing feedback loop / reinforcing loop | 增强回路 | 自我增强、带来指数增长或失控崩溃的反馈回路，图中标 R；附录术语表条目；2012 年中文版同 | 强化回路 | introduction | 66 | 初定 |
| negative / positive feedback loop | 负反馈回路 / 正反馈回路 | 附录术语表给出的别名，只在原文这样写时用 | 调节回路、增强回路 | appendix | 2 | 初定 |
| stabilizing / runaway | 稳定 / 失控 | 第 1 章小标题 Stabilizing Loops、Runaway Loops 写“稳定回路”“失控回路”；stabilizing stocks 写“起稳定作用的存量” |  | ch01 | 19 | 初定 |
| vicious cycle / virtuous circle | 恶性循环 / 良性循环 |  |  | ch01 | 4 | 初定 |
| goal-seeking | 寻求目标的 | 调节回路的特征 |  | ch01 | 9 | 初定 |
| discrepancy | 差距 | 目标和存量实际水平之间的差 | 偏差、矛盾 | ch01 | 26 | 初定 |
| exponential growth / doubling time | 指数增长 / 倍增时间 |  | 几何级数增长 | ch01 | 29 | 初定 |
| shifting dominance | 主导地位的转换 | 相互竞争的反馈回路相对强弱随时间的变化；附录术语表条目；dominate 写“占主导” |  | ch02 | 13 | 初定 |
| delay | 延迟 | 信息或物质在系统里传递需要的时间；第 9 个杠杆点 | 滞后、拖延 | introduction | 138 | 初定 |
| perception / response / delivery delay | 感知延迟 / 反应延迟 / 交货延迟 | 第 2 章汽车经销商模型的三种延迟 |  | ch02 | 35 | 初定 |
| oscillation | 振荡 | 延迟造成的反复上下波动 | 波动（fluctuation） | ch02 | 34 | 初定 |
| overshoot | 过冲 | 超过目标或极限；overshoot and collapse 写“过冲与崩溃” | 超越极限（只用于书名《超越极限》） | ch02 | 11 | 初定 |
| threshold | 阈值 | critical threshold 写“临界阈值” | 门槛 | ch02 | 6 | 初定 |
| gain | 增益 | 第 7 个杠杆点里驱动回路的增益 |  | appendix | 1 | 初定 |
| self-correcting / self-reinforcing / self-enhancing | 自我校正 / 自我强化 / 自我增强 | self-maintaining 写“自我维持”，self-repairing 写“自我修复” |  | ch01 | 8 | 初定 |
| model | 模型 | 计算机模型，也包括头脑里的模型 |  | authors-note | 120 | 初定 |
| mental model | 心智模型 | 和“模型”保持字面联系；《第五项修炼》中译本作“心智模式” | 思维模式（mind-set） | ch01 | 12 | 初定 |
| simulation / scenario | 模拟 / 情景 | driving scenarios 写“驱动情景”；“what if” questions 写“‘如果……会怎样’的问题” | 场景 | authors-note | 17 | 初定 |
| converter | 转换器 | 附录模型方程里的常数或由其他变量算出的量（STELLA 的用语） |  | appendix | 10 | 初定 |
| resilience / resilient | 韧性 / 有韧性的 | 系统受扰动后恢复、修复或反弹的能力；附录术语表条目；2012 年中文版作“适应力” | 稳定性（stability）、适应（adapt） | ch01 | 48 | 初定 |
| meta-resilience | 元韧性 | 能恢复或重建反馈回路的反馈回路；meta-meta-resilience 写“元元韧性” |  | ch03 | 2 | 初定 |
| stability / stable | 稳定性 / 稳定的 | 作者把稳定和韧性分开讲 | 韧性 | introduction | 26 | 初定 |
| self-organization | 自组织 | 系统自己构建结构、学习、多样化的能力；附录术语表条目；第 4 个杠杆点 | 自我组织 | ch01 | 51 | 初定 |
| hierarchy / hierarchical | 层级 / 层级式的 | 系统和子系统一层套一层的安排；附录术语表条目；2012 年中文版作“层次性” | 等级制度 | ch01 | 38 | 初定 |
| suboptimization | 次优化 | 子系统的目标压过整个系统的目标而产生的行为；附录术语表条目 | 局部最优 | ch03 | 3 | 初定 |
| Koch snowflake / fractal | 科赫雪花 / 分形 | 第 3 章自组织一节的例子 |  | ch03 | 6 | 初定 |
| linear / nonlinear relationship | 线性关系 / 非线性关系 | 附录术语表的两个条目 |  | introduction | 42 | 初定 |
| boundary | 边界 | 为了讨论而给系统划定的边界；boundary of caring 写“关怀的边界” | 国界（地理意义除外） | ch02 | 52 | 初定 |
| limiting factor | 限制因素 | 某一时刻最限制系统活动的那项必要输入；附录术语表条目 | 制约因素 | ch04 | 10 | 初定 |
| law of the minimum | 最小因子定律 | 李比希的定律 |  | ch04 | 1 | 初定 |
| limits to growth | 增长的极限 | 原理“增长总有极限”；同名书写《增长的极限》 |  | editors-note | 7 | 初定 |
| bounded rationality | 有限理性 | 西蒙的概念；附录术语表条目 | 有界理性 | ch04 | 19 | 初定 |
| invisible hand / invisible foot | 看不见的手 / 看不见的脚 | 斯密和戴利的说法 |  | ch04 | 3 | 初定 |
| archetype | 基模 | 产生典型行为模式的常见系统结构；附录术语表条目；system archetype 写“系统基模”；《第五项修炼》中译本同 | 原型 | introduction | 16 | 初定 |
| system trap / trap | 系统陷阱 / 陷阱 | 第 5 章的八种基模 |  | introduction | 49 | 初定 |
| the way out | 出路 | 第 5 章方框标题和附录的段首标签 | 编者的话里 on the way out 写“撤退时” | ch05 | 25 | 初定 |
| policy resistance | 政策阻力 | 第一种陷阱 |  | introduction | 12 | 初定 |
| fixes that fail | 失效的对策 | 政策阻力的另一个名字 | 治标不治本（2012 年中文版） | ch05 | 1 | 初定 |
| tragedy of the commons / commons | 公地悲剧 / 公地 | 哈丁的概念；common sinks 写“公共的排污场所” |  | introduction | 31 | 初定 |
| mutual coercion, mutually agreed upon | 相互同意的相互强制 | 哈丁的说法，全书引用时一字不差 |  | ch05 | 3 | 初定 |
| drift to low performance | 滑向低绩效 | 第三种陷阱 | 目标侵蚀（eroding goals；2012 年中文版用它作这个陷阱的名字） | ch04 | 9 | 初定 |
| performance standard | 绩效标准 | 滑向低绩效陷阱里，标准跟着过去的绩效往下调 |  | ch05 | 4 | 初定 |
| eroding goals | 目标侵蚀 | 原文说是滑向低绩效的另一个名字 | 滑向低绩效 | introduction | 6 | 初定 |
| boiled frog syndrome | 温水煮青蛙综合征 | 滑向低绩效的又一个名字 |  | ch05 | 1 | 初定 |
| escalation | 竞争升级 | 第四种陷阱，军备竞赛、价格战都属于这一类 |  | ch05 | 35 | 初定 |
| success to the successful | 富者愈富 | 第五种陷阱；success-to-the-successful loop 写“富者愈富回路” | 引言俗语 The rich get richer 也写“富者愈富”，意思相通 | ch05 | 15 | 初定 |
| competitive exclusion principle | 竞争排斥原理 | 生态学原理，富者愈富的别名 | 竞争排除 | introduction | 4 | 初定 |
| shifting the burden / intervenor | 转嫁负担 / 干预者 | 第六种陷阱全名 Shifting the Burden to the Intervenor 写“把负担转嫁给干预者” |  | ch05 | 21 | 初定 |
| addiction | 上瘾 | 第六种陷阱的别名；addict 写“上瘾者”“瘾君子”（按语境） | 成瘾 | introduction | 32 | 初定 |
| rule beating | 钻规则的空子 | 第七种陷阱；rule beaters 写“钻空子的人” | 违反规则 | ch05 | 17 | 初定 |
| seeking the wrong goal | 追求错误的目标 | 第八种陷阱 |  | ch05 | 5 | 初定 |
| leverage point | 杠杆点 | 系统里一个小小的改变就能让行为发生大变化的地方 | 支点 | introduction | 39 | 初定 |
| places to intervene | 干预系统的位置 | 第 6 章标题和附录小节 | 介入点 | ch06 | 3 | 初定 |
| intervene / intervention | 干预 |  | 干涉（interfere） | ch05 | 23 | 初定 |
| parameter / constant / numbers | 参数 / 常数 / 数字 | 第 12 个杠杆点 |  | ch01 | 51 | 初定 |
| buffer | 缓冲 | 第 11 个杠杆点：起稳定作用的存量 |  | ch01 | 14 | 初定 |
| information flow | 信息流 | 第 6 个杠杆点 |  | ch04 | 9 | 初定 |
| rule | 规则 | 第 5 个杠杆点 |  | introduction | 105 | 初定 |
| paradigm / transcending paradigms | 范式 / 超越范式 | 第 2 和第 1 个杠杆点 | 模式 | ch06 | 25 | 初定 |
| mind-set | 思维模式 | 系统从中产生的那套共同的想法 | 心智模型 | ch07 | 3 | 初定 |
| intrinsic responsibility | 内在责任 | 第 7 章：系统的设计让决策者直接、迅速地承受决策的后果 |  | ch07 | 4 | 初定 |
| time horizon | 时间视野 | 决策时考虑的时间长短；第 7 章准则 Expand Time Horizons | 时间范围 | ch01 | 7 | 初定 |
| error-embracing | 拥抱错误 | 唐·迈克尔的说法，第一次出现时括注原文 |  | ch07 | 2 | 初定 |
| tyrannese | 暴政语 | 贝里造的词，第一次出现时括注原文 |  | ch07 | 2 | 初定 |
| Slinky | 弹簧圈 | 引言里的弹簧玩具，每节第一次出现时括注 Slinky | 彩虹圈 | introduction | 12 | 初定 |
| mess | 乱局 | 艾可夫的说法：一组相互作用、不断变化的问题；第 5 章 make a mess 照常译“弄脏” |  | introduction | 4 | 初定 |
| holistic / reductionist | 整体的 / 还原论的 | unholistic 写“非整体的” |  | introduction | 7 | 初定 |
| sustainability / sustainable | 可持续 | Sustainability Institute 写“可持续发展研究所” |  | editors-note | 11 | 初定 |
| GNP | 国民生产总值（GNP） | 每节第一次出现写全称再括注 GNP，之后写 GNP |  | ch04 | 17 | 初定 |
| thermostat / furnace | 恒温器 / 暖气炉 | 第 1、2 章的恒温器模型 | 温控器 | ch01 | 71 | 初定 |

## 机构、产品与地名

| 英文 | 译法 | 说明 |
| --- | --- | --- |
| MIT / Massachusetts Institute of Technology | 麻省理工学院 | MIT System Dynamics group 写“麻省理工学院系统动力学小组” |
| Dartmouth College / Environmental Studies Program | 达特茅斯学院 / 环境研究项目 |  |
| Harvard University / Stanford | 哈佛大学 / 斯坦福大学 | Stanford prison experiment 写“斯坦福监狱实验” |
| University of British Columbia / University of New Brunswick / University of Kassel | 不列颠哥伦比亚大学 / 新不伦瑞克大学 / 卡塞尔大学 |  |
| Sustainability Institute | 可持续发展研究所 | 作者 1996 年创办 |
| Chelsea Green Publishing | Chelsea Green 出版社 | 本书出版社 |
| Balaton Group / Environmental Systems Analysis Group at Kassel | 巴拉顿小组 / 卡塞尔大学环境系统分析小组 | 编者致谢 |
| Foundation for the Third Millennium / Presidio School of Management | 第三个千年基金会 / 普雷西迪奥管理学院 | 编者致谢 |
| Pew Scholar in Conservation and the Environment / MacArthur Fellowship | 皮尤环境保护学者 / 麦克阿瑟奖 |  |
| National Geographic Society / Committee on Research and Exploration | 美国国家地理学会 / 研究与探索委员会 |  |
| International Panel on Climate Change | 政府间气候变化专门委员会 | 原文的名称不准确（应为 Intergovernmental），照通行中文名写 |
| UN / United Nations / World Bank / OPEC | 联合国 / 世界银行 / 欧佩克 |  |
| North American Free Trade Agreement / Montreal Protocol | 《北美自由贸易协定》 / 《蒙特利尔议定书》 |  |
| Club of Rome / Rocky Mountain Institute | 罗马俱乐部 / 落基山研究所 |  |
| Congress / Supreme Court / Federal Reserve Bank / the Fed | 国会 / 最高法院 / 联邦储备银行 / 美联储 |  |
| Medicaid / Social Security / Prohibition | 联邦医疗补助 / 社会保障 / 禁酒令 |  |
| U.S. Endangered Species Act / Act 250 / Toxic Release Inventory | 美国《濒危物种法》 / 《250 号法案》 / 有毒物质排放清单 | Act 250 是佛蒙特州的土地使用法 |
| General Motors / IBM / Wal-Mart / Disney / Dun & Bradstreet | 通用汽车 / IBM / 沃尔玛 / 迪士尼 / 邓白氏公司 |  |
| Dow Jones Industrial Average | 道琼斯工业平均指数 |  |
| Christian Democratic Union / Labor / Social Democrats / Finance Ministry | 基督教民主联盟 / 工党 / 社会民主党 / 财政部 | 按所在国家的通行译名 |
| Alcoholics Anonymous | 匿名戒酒会 |  |
| International Herald Tribune | 《国际先驱论坛报》 | 不括注；2012 年中文版作《国际先驱导报》，那是另一份报纸 |
| World3 | World3 模型 | 《增长的极限》用的计算机模型 |
| STELLA / iThink / Vensim / isee systems / Ventana Systems / High Performance Systems | 照写原名 | 建模软件和开发公司 |
| Pegasus Communications / Creative Learning Exchange / System Dynamics Society | 照写原名 / 照写原名 / 系统动力学学会 | 参考书目条目照写英文，说明文字里照这一列 |
| The Limits to Growth / Beyond the Limits / Thinking in Systems | 《增长的极限》 / 《超越极限》 / 《系统之美》 | *Limits* 单独出现时写《增长的极限》 |
| Zen and the Art of Motorcycle Maintenance / Chaos: Making a New Science | 《禅与摩托车维修艺术》 / 《混沌：开创新科学》 |  |
| The Global Citizen | “全球公民”专栏 | 作者写了 15 年的周专栏；参考书目里同名的书照写英文 |
| Calvin and Hobbes | 漫画《卡尔文与霍布斯》 | 脚注里照写原文 |
| Mark 4:25 | 《马可福音》4:25 | 用和合本译文 |
| Soviet Union / United States / Romania / Hungary / Sweden / Germany / East Germany / West Germany | 苏联 / 美国 / 罗马尼亚 / 匈牙利 / 瑞典 / 德国 / 东德 / 西德 |  |
| Czechoslovakia / Czech Republic / Poland / South Africa / Iraq / Kuwait | 捷克斯洛伐克 / 捷克共和国 / 波兰 / 南非 / 伊拉克 / 科威特 |  |
| Gaza Strip / India / Japan / Mexico / Guatemala / Canada | 加沙地带 / 印度 / 日本 / 墨西哥 / 危地马拉 / 加拿大 |  |
| Vermont / New Hampshire / Plainfield / Kentucky / New England / Los Angeles | 佛蒙特州 / 新罕布什尔州 / 普兰菲尔德 / 肯塔基州 / 新英格兰 / 洛杉矶 | 普兰菲尔德是作者农场所在的小镇 |
| New Brunswick / Zermatt / Waikiki / Budapest / Amsterdam / Rio de Janeiro / Kassel | 新不伦瑞克省 / 采尔马特 / 怀基基 / 布达佩斯 / 阿姆斯特丹 / 里约热内卢 / 卡塞尔 |  |
| Ghor | 古尔 | 引言插曲（苏菲派故事）开头的地名 |
| Middle East / Sufis / Native Americans / Eskimos | 中东 / 苏菲派 / 美洲原住民 / 爱斯基摩人 | Eskimos 照原文写“爱斯基摩人” |
| spruce budworm / balsam fir / spruce / fir | 云杉卷叶蛾 / 香脂冷杉 / 云杉 / 冷杉 | 第 4 章插曲 |
| DDT / fenitrothion / Sevin | DDT / 杀螟硫磷 / 西维因 | 杀虫剂 |
| khat / cassava | 恰特草 / 木薯 |  |
| America’s Cup | 美洲杯帆船赛 | 第 5 章插曲 |
| Industrial Revolution / Middle Ages | 工业革命 / 中世纪 |  |
| Freedom of Information Act / Constitution | 《信息自由法》 / 宪法 | 第 6 章 |
| People’s Republic of China / Nazi Germany / Israeli / Palestinians | 中华人民共和国 / 纳粹德国 / 以色列的 / 巴勒斯坦人 |  |
| Forrester’s World model | 福里斯特的“世界”模型 | 第 6 章；指福里斯特《世界动力学》里的模型 |
| Nobel Prize | 诺贝尔奖 | Nobel Prize–winning economist 写“诺贝尔奖得主、经济学家” |
| Monopoly | 大富翁游戏 | 第 5 章，富者愈富的例子 |
| Stealth bombers / Titanic | 隐形轰炸机 / 泰坦尼克号 | arranging the deck chairs on the Titanic 写“在泰坦尼克号上摆弄甲板躺椅” |
| *Homo sapiens* | 智人（*Homo sapiens*） | 学名保留斜体 |
