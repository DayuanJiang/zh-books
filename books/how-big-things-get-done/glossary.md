# 术语表

翻译前根据 `review/terms/` 里的统计数据裁定（来源和门槛见 [review/terms/README.md](review/terms/README.md)）。“出现次数”和“首次出现”由 `tools/term_stats.py --glossary` 按英文词形统计，含标题，不含脚注；按正则匹配，同词根的普通用法也会算进去，例如 plan、experience、team、design。状态都是“初定”，由 Claude 裁定，等用户确认；改动时要回查已经译完的章节。

## 体例

- **人名**：用 [review/terms/people-zh.tsv](review/terms/people-zh.tsv) 的译名。每节第一次出现时在中文名后括注英文原名，例如“弗兰克·盖里（Frank Gehry）”，之后只写中文。原文只有名的人（第 3 章的戴维和德博拉、献辞里的卡丽莎）也照这个办法。表里收的虚构人物（詹姆斯·邦德）也照这个办法。表里标 keep 的人（Edwin Chan、Tensho Takemori 等）照写原名。脚注里的人名照写原文。
- **叙述者**：书里的“我”是傅以斌，合著者丹·加德纳不以第一人称出现；we 有时指作者和他的研究团队，有时泛指人们，按上下文译“我们”或省略。
- **机构、产品、地名**：见下面“机构、产品与地名”。没有通行中文名的公司和产品照写原名，和汉字之间加空格。
- **书名、报刊、电影、歌曲、论文**：正文里用《》，每节第一次出现时括注原题，原题用斜体，例如《权力掮客》（*The Power Broker*）；文章、论文的原题保留引号，不用斜体，例如赫希曼的文章《隐藏之手原理》（“The Principle of the Hiding Hand”）。常见报刊不括注，见“全书统一的写法”。已有中译本的书用中译本的书名，见“书名与作品”。脚注里的出处保留原文，不加书名号。
- **数字**：年份、日期、百分比和多位数字用阿拉伯数字，和汉字之间加空格，例如“2008 年”“8.5%”“171 英里”。金额换算成中文的万、亿：$33 billion 写“330 亿美元”，$900,000 写“90 万美元”，$1.2 million 写“120 万美元”；丹麦克朗、加元等照原文的币种。细则见“全书统一的写法”。
- **单位**：原文公制在前、英制括注的，照样保留两种，例如 250 meters (820 feet) 写“250 米（820 英尺）”；原文只有英制的照译（英里、英尺、平方英尺），数字要紧时括注公制；华氏温度括注摄氏度。
- **引语**：盖里、道格特、施工主管哈珀等人的访谈很口语，按原文的语气译；第 7 章引文里的粗话（f \*\*\*ing）保留力度和原文的星号遮挡。
- **脚注**：这本书的脚注由书末注释改成，开头没有被注释的词句，整条是出处或说明。出处（作者、标题、刊名、出版地和出版社、卷期、日期、网址、页码）保留英文原样，Ibid. 和 et al. 也照写；说明性的句子要翻译，句中的人名照写英文。常见格式：
  - Author interview with Louis Thompson, April 22, 2020. → 作者对 Louis Thompson 的访谈，2020 年 4 月 22 日。
  - Author interviews with X → 作者对 X 的多次访谈
  - Personal communication with X → 与 X 的私人通信
  - See X / See also X → 见 X / 另见 X
  - For an overview, see Appendix A. → 概述见附录 A。
  - For more on X, see Y → 关于 X 的更多内容，见 Y
  - 第 1 章注释 30 解释了 author interview 的意思：由两位作者之一或两人一起做的访谈，译“作者访谈”。
  - 出处串的标点见“全书统一的写法（译完后定）”。
- **脚注标记**：`[^n]` 放在中文里对应词句的后面，编号与英文一致。引文以引号结束时，标记放在右引号后面。
- **译者注**：写成 `[^t1]:`，在正文里引用；定义的写法和标记的位置见“全书统一的写法（译完后定）”。全书现有的译者注：引言标题 California Dreamin’ 来自同名歌曲，注释 12 的 John Tauranc 应为 Tauranac；第 1 章铁律示意图里的英文，normal distribution 的双关，拉丁语 festina lente，富兰克林 1758 年的原文只写到骑手；第 2 章萨默维尔要求的面积和“一半在六个月内建成”与史料不符，注释 9 的 Sharot Tali 是 Tali Sharot 的名姓颠倒；第 3 章 Oprah-speak；第 4 章 experiri；第 5 章标题 Are You Experienced? 是亨德里克斯的专辑名，Big O 和 Big Owe 的谐音；第 6 章 Empty State Building 和 Empire State Building 的谐音，inchstone 仿 milestone 造词；第 7 章 Hiding Hand 仿“看不见的手”（Invisible Hand）；第 9 章两张图里的英文，正文的几个升温度数和 IPCC 图 SPM.6 对不上，小节标题 Blowin’ in the Wind 是鲍勃·迪伦的歌；结语里 heuristic 和 Eureka! 都来自 heuriskein；致谢里的 guapa。
- **“下一页”**：附录 A 的 The table on the next page 和第 9 章的 The chart on the next page 指纸质版的版面，阅读器里表格和图就在后面，译“下表”“下图”。
- **图片和表格**：图片只在英文文件里，替代文字不译。附录 A 的表头和项目类型译成中文，数字照写。
- **分隔线**：分隔线 `---` 只写在英文文件里。
- **参考文献**：2026-11-05 从 EPUB 补入。580 条书目和注释里的出处一样照录英文原样，中文文件只把标题译成“参考文献”。
- **破折号和句式**：中文译文不用破折号（——），原文的破折号按意思改成逗号、冒号、括号或另起一句；也不用“不是……而是……”这种句式，换成直接的说法。小节标题 Projects Don’t *Go* Wrong, They *Start* Wrong 这类对照句，也改成直接的说法。

## 各节标题

| 章节 id | 英文 | 中文标题（`#` 一级标题照这一列写） |
| --- | --- | --- |
| dedication | Dedication | 献辞 |
| introduction | Introduction: California Dreamin’ | 引言 加州梦 |
| ch01 | 1. Think Slow, Act Fast | 第 1 章 慢思考，快行动 |
| ch02 | 2. The Commitment Fallacy | 第 2 章 承诺谬误 |
| ch03 | 3. Think from Right to Left | 第 3 章 从右向左思考 |
| ch04 | 4. Pixar Planning | 第 4 章 皮克斯式规划 |
| ch05 | 5. Are You Experienced? | 第 5 章 你有经验吗？ |
| ch06 | 6. So You Think Your Project Is Unique? | 第 6 章 你以为你的项目独一无二？ |
| ch07 | 7. Can Ignorance Be Your Friend? | 第 7 章 无知会是你的朋友吗？ |
| ch08 | 8. A Single, Determined Organism | 第 8 章 一个意志坚定的有机体 |
| ch09 | 9. What’s Your Lego? | 第 9 章 你的乐高积木是什么？ |
| coda | Coda: Eleven Heuristics for Better Project Leadership | 结语 更好地领导项目的 11 条启发式 |
| appendix-a | Appendix A: Base Rates for Cost Risk | 附录 A 成本风险的基础比率 |
| appendix-b | Appendix B: Further Readings by Bent Flyvbjerg | 附录 B 傅以斌著作延伸阅读 |
| acknowledgments | Acknowledgments | 致谢 |
| bibliography | Bibliography | 参考文献 |
| about-the-authors | About the Authors | 关于作者 |

中文版《怎样做成大事》（贾拥民译，浙江科学技术出版社 2024 年版）的章名只作参考：它给不少章名加了副题或改写，例如第 2 章“承诺谬误：你承诺的，和你想的不一样”，第 3 章“以终为始，从右向左思考”，第 8 章“打造一支上下一心的团队”，第 9 章“模块化，你的‘乐高积木’是什么”。这里按原书的章名翻译：引言标题 California Dreamin’ 是 1965 年的同名歌曲，中文通称《加州梦》，加译者注；第 5 章标题照应亨德里克斯的专辑 *Are You Experienced*，正文讲的是经验，所以译“你有经验吗？”，加译者注；第 8 章标题出自第 7 章末尾，作者把团队比作 a single, determined organism，保留“有机体”这个比喻；第 4 章的 planning 和全书一样译“规划”。

小节标题由各章译者译出；结语的 11 个小节标题是作者的 11 条启发式，照下表写，正文里引用它们时也用同样的说法。

| 结语小节标题 | 中文 |
| --- | --- |
| Hire a Masterbuilder | 聘请建造大师 |
| Get Your Team Right | 组建合适的团队 |
| Ask “Why?” | 问“为什么？” |
| Build with Lego | 用乐高积木搭建 |
| Think Slow, Act Fast | 慢思考，快行动 |
| Take the Outside View | 采用外部视角 |
| Watch Your Downside | 留意下行风险 |
| Say No and Walk Away | 学会说不，及时退出 |
| Make Friends and Keep Them Friendly | 结交朋友，维护友谊 |
| Build Climate Mitigation into Your Project | 把减缓气候变化纳入项目 |
| Know That Your Biggest Risk Is You | 要知道最大的风险是你自己 |

译者读完一章后，如果觉得标题另有更贴切的译法，在汇报里提出，由主会话统一修改。

## 全书统一的写法

翻译开始前先定下的写法，各章都照此执行；译完后编辑提出的新问题，定在下一节“全书统一的写法（译完后定）”。

- **数字**：一到十，以及带“几、十几、数百、上千”的约数，用汉字（两座桥、五个月、几十个项目）；11 以上的确数用阿拉伯数字（25 种项目类型、258 个项目、24 小时），万和亿前面的数字也用阿拉伯数字（1.6 万多个项目、2 万所学校）；年份、日期、钟点、金额、百分比一律用阿拉伯数字（凌晨 4 点、86 美元、0.5%）。原文用英文单词写的数（fourteen years、twenty-six-story、one hundred projects）同样按这条规则转换：14 年、26 层、100 个项目。倍数写成“是原来的 N 倍”；百分比照原文写“超支 157%”“降低 35% 到 40%”。范围不用连接号，写“5 到 10”“35% 到 40%”。
- **书名、报刊括注**：每节第一次出现时括注原题，原题用斜体；文章、论文的原题保留引号，不用斜体。《纽约时报》《华尔街日报》《纽约客》《卫报》《连线》《哈佛商业评论》这些常见报刊不括注；其他刊物（《纽约书评》*The New York Review of Books*、《新闻日报》*Newsday*、《旧金山纪事报》*San Francisco Chronicle*、《蒙特利尔公报》*Montreal Gazette*）每节第一次出现时括注。
- **人名**：名人也照常在每节第一次出现时括注英文。脚注里的人名，无论在出处里还是在说明句里，一律照写英文。“爵士”“勋爵”这类称呼放在中文名后面：约翰·伊根爵士、伯纳德·詹金爵士、哈迪勋爵。“罗斯福政府”“伊丽莎白女王”这类说法不括注。
- **平台名**：写 Twitter，不写“推特”；Facebook、Instagram 照写原名。
- **头衔**：CEO 写“首席执行官”，chairman 写“董事长”，executive 按上下文写“高管”；governor 写“州长”，premier of New South Wales 写“新南威尔士州州长”，mayor 写“市长”；secretary of the interior 写“内政部长”，secretary of defense 写“国防部长”，secretary of state 写“国务卿”；parliamentary budget officer（加拿大）写“议会预算官”。作者简介里 knighted by the Queen of Denmark 写“获丹麦女王授予爵士勋位”。
- **项目和阶段**：project 一律写“项目”；planning 写“规划”，plan 写“计划”，planner 写“规划者”；delivery 写“实施”，deliver 按上下文写“完成”“建成”“交付”，on time and on budget 写“按期、不超预算”。project leader 写“项目负责人”，project management 写“项目管理”。
- **引号里的说法**：原文用引号标出的说法和作者造的词（“Think slow, act fast”“break-fix cycle”“one of those”“honest numbers”），中文也加引号，每节第一次出现时括注原文。
- **原文疑点**：引言注释 12 的 John Tauranc（注释 16 作 Tauranac）、第 2 章注释 9 的 Sharot Tali、致谢里的 Juan de Dios Ortúza（应为 Ortúzar）照原文保留，前两处加译者注；索引里的 Del Ray 正文作 Del Rey，译文照正文。导入时发现的原文疑点见 [review/source.md](review/source.md)，翻译时发现的记在各节审校记录 `review/<章节 id>.md` 的“原文疑点”表里。

## 全书统一的写法（译完后定）

各节译完后，编辑提出了一些各节写法不一、或者术语表没有写到的地方，统一如下：

- **译者注的写法**：定义一律以“译者注：”开头。正文同一处已有原注标记时，译者注标记紧跟在后面，例如“比地球上任何一座建筑都高[^12][^t2]”“过度自信的物种[^9][^t2]”，注释正文里不另加括号说明。章题和小节标题的译者注放在正文里第一处呼应标题的地方，例如引言的“敢做大梦[^t1]”，或者放在章首导语的第一句后面。译者注里提到的外文词用正体（festina lente、inchstone、heuriskein、guapa），书名照书名的体例用斜体。
- **脚注里的出处**：“见”“另见”后面的出处串照英文原样写，出处之间的分号、and 和逗号都照英文写，例如第 7 章注释 9 的“……1, 3, 7, 13; and ……”。出处在注释末尾时，末尾的英文句点照样保留；出处后面接着写中文时，出处末尾用中文标点，例如“……614–18。写给喜欢数学和统计的读者：……”“……164–68；另见 Gary Klein, ……”。出处以网址结尾、后面接中文句号时，网址和句号之间空一格。
- **数字**：引语和名言里的整万数也照“数字”一条写阿拉伯数字，例如爱迪生的“我并没有失败 1 万次”。
- **官员和高管**：official 指政府里的人写“官员”，指公司里的人写“高层管理人员”或“高管”，例如港铁的 a top official 写“一位高层管理人员”。
- **延误**：名词 delay / delays 写“延误”（一连串的延误、早期延误、延误和超支）；动词 delay 按上下文写“推迟”“拖延”“耽误”；说项目 late、years delayed 时可以写“延期完工”“推迟了好几年”。
- **低于预算**：under budget 写“低于预算”或“花的钱比预算少”，胡佛水坝的 a little under budget 写“略低于预算”；“不超预算”“没有超出预算”只用于 on budget。
- **预计耗资**：at an estimated cost of、would cost 这类说法写“预计耗资”“预计为”；名词 estimated cost 写“估算成本”；“估计”只用于一般说法。
- **项目类型名**：附录 A 的表格和正文写全称，fossil thermal power 写“化石燃料火电”，energy transmission 和 electricity transmission 写“输电”，hydroelectric dams 写“水电站大坝”，nonhydroelectric dams 写“非水电大坝”。第 9 章那张从肥尾到瘦尾的图上印的是简称，译者注照图上的字写，Thermal 写“火电”，Dam 写“大坝”。
- **其他说法**：bullet train to nowhere 写“通往无处的子弹头列车”（引言、第 2 章）；Just do it 写“想做就做”（第 2 章，第 7 章的小节标题）；calculated risk taking 写“经过权衡的冒险”，take calculated risks 写“冒经过权衡的风险”（第 2 章、第 5 章）；cut the tail 写“砍掉尾部”（第 6 章、第 9 章；第 9 章原文加了引号，中文也加引号并括注原文）；a machine for jumping to conclusions 写“急于下结论的机器”，和本仓库《思考，快与慢》第 7 章标题相同；best practice 写“最佳实践”。
- **原文的事实出入**：作者原文和史料有出入的地方，正文都照原文译，记在各节审校记录的“原文疑点”表里；出入会影响读者理解时才加译者注（第 1 章富兰克林的谚语、第 2 章五角大楼的面积、第 9 章 IPCC 的升温度数）。第 4 章说 Ed Catmull 当时是皮克斯的首席执行官（其实是总裁），第 5 章伦敦和洛杉矶举办奥运的次数，引言帝国大厦的 17%（按名义金额算是 18%），都照原文译，不加注。

## 核心概念

| 英文 | 首选译法 | 适用的意思 | 不要混同 | 首次出现 | 出现次数 | 状态 |
| --- | --- | --- | --- | --- | --- | --- |
| megaproject | 超大型项目 | 作者研究的对象：极大的项目，通常耗资 10 亿美元以上；megaproject management 写“超大型项目管理” | 大项目（big project）、重大项目（major project） | introduction | 25 | 初定 |
| big project / big thing | 大项目 / 大事 | 书名和全书说的“大”是相对的，家庭装修对普通人也是大项目；书名 How Big Things Get Done 写《怎样做成大事》 | 超大型项目 | introduction | 88 | 初定 |
| Iron Law of Megaprojects / Iron Law | 超大型项目铁律 / 铁律 | 作者从数据里总结的规律：超出预算，超出工期，效益不足，一再重演；作者说明它是社会科学意义上的概率规律 | 物理定律 | ch01 | 5 | 初定 |
| over budget, over time, under benefits, over and over again | 超出预算，超出工期，效益不足，一再重演 | 铁律的完整说法，全书引用时保持一致；小节标题 Over Budget, Over Time, Over and Over Again 写“超出预算，超出工期，一再重演” |  | ch01 | 3 | 初定 |
| on budget / on time / on benefits | 不超预算 / 按期 / 达到预期效益 |  |  | introduction | 27 | 初定 |
| cost overrun / schedule overrun | 成本超支 / 工期超期 | 书中的超支都按实际值计算，不含通货膨胀；overrun 单用时按对象写“超支”或“超期” | 超额 | ch01 | 65 | 初定 |
| benefit shortfall | 效益不足 | 实际效益低于预期 |  | ch01 | 5 | 初定 |
| estimate / forecast | 估算 / 预测 | cost estimate 写“成本估算”；forecasting 写“预测” | 估计（只在一般说法里用） | introduction | 155 | 初定 |
| think slow, act fast / think fast, act slow | 慢思考，快行动 / 快思考，慢行动 | 作者对成功和失败项目的概括：规划阶段慢慢想清楚，实施阶段快速完成；第 1 章标题和结语的一条启发式 | 卡尼曼的快思考和慢思考（系统 1 和系统 2） | introduction | 19 | 初定 |
| planning / delivery | 规划 / 实施 | 作者把项目分成两个阶段：先规划，再实施；电影业叫 development and production（开发和制作），建筑业叫 design and construction（设计和施工） | 交付（deliver 指交出成品时才用） | introduction | 199 | 初定 |
| plan / planner | 计划 / 规划者 | 名词 plan 写“计划”，a plan worthy of its name 写“名副其实的计划” |  | introduction | 124 | 初定 |
| window of doom / window | 厄运之窗 / 窗口 | 项目持续的时间像一扇敞开的窗，开得越久，越可能有意外闯进来；比喻里的 open window 写“敞开的窗”，close the window 写“关上窗”，window of time 写“时间窗口”，window of vulnerability 写“脆弱之窗” |  | ch01 | 10 | 初定 |
| Make haste slowly / festina lente | 慢慢地赶快 / festina lente | 奥古斯都的座右铭，拉丁语照写斜体原文，加译者注；第 1 章同名的小节标题写“赶快，但要慢慢来” | 欲速则不达 | ch01 | 3 | 初定 |
| Projects don’t go wrong, they start wrong | 项目一开始就错了 | 第 1 章小节标题；中文用直接的说法 |  | ch01 | 2 | 初定 |
| honest numbers | “诚实的数字” | 沃尔特·威廉斯的说法，第 1 章小节标题写“诚实的数字” |  | ch01 | 2 | 初定 |
| black swan / black swan management | 黑天鹅 / 黑天鹅管理 | 塔勒布的概念：概率低、后果严重的事件；黑天鹅管理是作者提出的做法，第 6 章小节标题 |  | ch01 | 27 | 初定 |
| normal distribution / bell curve | 正态分布 / 钟形曲线 | Gaussian 写“高斯分布” |  | ch01 | 10 | 初定 |
| fat tail / fat-tailed | 肥尾 / 肥尾的 | 极端结果远多于正态分布的分布；fat-tailed distribution 写“肥尾分布”；作谓语写“是肥尾的”“被称为‘肥尾’类型” | 厚尾（统一用肥尾） | ch01 | 35 | 初定 |
| thin-tailed | 瘦尾 | 和肥尾相对，第 9 章小节标题 Thin-Tailed Projects 写“瘦尾项目” | 薄尾（统一用瘦尾） | ch09 | 2 | 初定 |
| tail | 尾部 | 分布的尾部；in the tail 写“落在尾部”；tail risk 写“尾部风险” |  | ch01 | 40 | 初定 |
| regression to the mean / regression to the tail | 均值回归 / 向尾部回归 | 前者是统计学概念，和《思考，快与慢》同；后者是作者仿前者造的说法，第 6 章小节标题 |  | ch01 | 7 | 初定 |
| power law | 幂律 | power-law distribution 写“幂律分布” |  | ch05 | 3 | 初定 |
| normal accidents | “正常事故” | 佩罗的概念：复杂系统里难以避免的事故 | 常规事故 | ch01 | 1 | 初定 |
| break-fix cycle | “边坏边修”的循环 | 作者的说法：实施中不断出问题、不断修补 |  | ch01 | 2 | 初定 |
| commitment fallacy | 承诺谬误 | 作者的概念：还没想清楚就过早锁定一个方案；第 2 章标题 |  | ch02 | 4 | 初定 |
| lock-in / lock in | 锁定 | premature lock-in 写“过早锁定” |  | ch02 | 5 | 初定 |
| escalation of commitment | 承诺升级 | 投入越多越难回头，继续把钱投进失败的项目 |  | ch02 | 3 | 初定 |
| rush to commit | 急于承诺 | 第 2 章小节标题 The Rush to Commit 写“急于承诺” |  | ch02 | 2 | 初定 |
| Commit to not commit | 承诺暂不承诺 | 第 2 章最后一节的标题：先下决心不要过早拍板 |  | ch02 | 2 | 初定 |
| optimism / optimism bias | 乐观 / 乐观偏差 | 和《思考，快与慢》同；optimist 写“乐观主义者” | 乐观偏见 | introduction | 25 | 初定 |
| planning fallacy / planning fallacy writ large | 规划谬误 / 放大版的规划谬误 | 卡尼曼和特沃斯基的概念：低估完成任务所需的时间；和《思考，快与慢》同 | 计划谬误（中文版的译法，本书统一用规划谬误） | ch02 | 2 | 初定 |
| Hofstadter’s Law | 侯世达定律 | 侯世达的戏言：总是比你预期的久，即使你考虑到了侯世达定律 |  | ch02 | 3 | 初定 |
| bias for action / bias against thinking | 行动偏好 / 排斥思考的偏好 | 前者是商界常说的“重行动、轻空谈”，亚马逊领导力准则的中文版写“崇尚行动”；后者是第 2 章小节标题 A Bias against Thinking | 偏差 | ch02 | 5 | 初定 |
| strategic misrepresentation | 策略性虚假陈述 | 作者的概念：为了策略目的故意、系统地歪曲信息，例如为了项目获批而压低估算 | 撒谎、误报 | ch02 | 9 | 初定 |
| psychology and power | 心理与权力 | 作者说的项目成败的两大驱动因素：心理（例如乐观）和权力（例如首席执行官或政客硬推自己偏爱的项目）；引言小节标题 Psychology and Power 写“心理与权力”；策略性虚假陈述属于权力和政治这一侧 | 心理学（psychology 指学科时才用） | introduction | 5 | 初定 |
| bias / cognitive bias / behavioral bias | 偏差 / 认知偏差 / 行为偏差 | 可以预测的系统性错误；和《思考，快与慢》同 | 偏见（对群体的成见） | ch02 | 46 | 初定 |
| System One / System Two | 系统 1 / 系统 2 | 和《思考，快与慢》同，原文拼成 System One 也写“系统 1” | 系统一 | ch02 | 13 | 初定 |
| WYSIATI (What You See Is All There Is) | 所见即全部（WYSIATI） | 卡尼曼的说法，和《思考，快与慢》同 |  | ch02 | 4 | 初定 |
| snap judgment / intuitive judgment | 快速判断 / 直觉判断 |  |  | ch02 | 10 | 初定 |
| sunk cost / sunk-cost fallacy | 沉没成本 / 沉没成本谬误 | 和《思考，快与慢》同 |  | ch02 | 7 | 初定 |
| Start digging a hole | “先挖个坑” | 威利·布朗的说法，卡赞也讲过同样的做法：先开工，把坑挖得够大，就只能继续拿钱来填；第 2 章小节标题 |  | ch02 | 5 | 初定 |
| Driving into the Blizzard | 冒着暴风雪开车 | 第 2 章小节标题，沉没成本的例子：球票买得越贵，越可能冒着暴风雪开车去看比赛 |  | ch02 | 5 | 初定 |
| Somervell’s Spiral | 萨默维尔螺旋 | 第 2 章小节标题，萨默维尔仓促定下五角大楼的方案，问题越滚越大 |  | ch02 | 2 | 初定 |
| think from right to left | 从右向左思考 | 作者的方法：先定右边方框里的目标，再想左边方框里的手段；第 3 章标题 | 倒推（backcasting 另有译法） | ch03 | 7 | 初定 |
| the box on the right | 右边的方框 | 目标；左边的方框是手段 |  | ch03 | 14 | 初定 |
| Why? | 为什么？ | 第 3 章小节标题和结语的启发式 Ask “Why?”（问“为什么？”） |  | ch03 | 6 | 初定 |
| means and ends | 手段与目的 |  |  | ch03 | 2 | 初定 |
| backcasting | 回推法 | 先描绘想要的未来，再往回推需要做什么；第一次出现括注原文 | 回测 | ch03 | 3 | 初定 |
| working backwards / PR/FAQ | 逆向工作 / PR/FAQ | 亚马逊的做法：先写新闻稿（press release）和常见问题解答（FAQ），再倒推产品；PR/FAQ 第一次出现写“PR/FAQ（新闻稿和常见问题解答）” |  | ch03 | 12 | 初定 |
| Pixar planning | 皮克斯式规划 | 作者的概念：像皮克斯一样用模拟和反复迭代来规划；第 4 章标题 | 皮克斯计划 | ch01 | 8 | 初定 |
| experiri | experiri | 拉丁语“尝试、检验”，experiment（试验）和 experience（经验）都从这个词来；作者用它概括“试验加经验”的规划方法；照写斜体原文，第一次出现括注意思并加译者注 |  | ch04 | 10 | 初定 |
| experience / experienced | 经验 / 有经验的 |  | 体验（只在 experience 指亲身感受时用） | introduction | 158 | 初定 |
| experiment / experimentation / testing | 试验 / 测试 | experiment 写“试验”；testing 写“测试”，第 4 章小节标题 Testing, Testing 写“测试，再测试” | 实验（科学实验才用） | introduction | 86 | 初定 |
| experiential learning | 经验学习 | 理论家的说法：从做中学 |  | ch04 | 1 | 初定 |
| iteration / iterate | 迭代 | 第 4 章小节标题 Why Iteration Works 写“迭代为什么管用” | 重复（repetition） | ch01 | 33 | 初定 |
| simulation / simulate | 模拟 |  | 仿真（工程语境也可，统一用模拟） | ch01 | 15 | 初定 |
| digital twin / CATIA | 数字孪生 / CATIA | CATIA 是达索系统的设计软件，照写原名 |  | ch04 | 8 | 初定 |
| maximum virtual product | 最大虚拟产品 | 作者的说法：做不了最小可行产品时，做一个极其逼真、细致的模型；第 4 章小节标题 |  | ch04 | 3 | 初定 |
| minimum viable product (MVP) / lean startup | 最小可行产品（MVP）/ 精益创业 | 埃里克·莱斯的说法 |  | ch04 | 8 | 初定 |
| brain trust | 智囊团 | 皮克斯内部给影片提意见的一小群电影人，和《创新公司》中译本同 |  | ch04 | 2 | 初定 |
| illusion of explanatory depth | 解释深度错觉 | 自以为懂，要解释时才发现不懂 |  | ch04 | 2 | 初定 |
| learning curve / positive learning / negative learning | 学习曲线 / 正向学习 / 负向学习 | positive learning curve 写“正向学习曲线”：越做越容易、越便宜；negative learning 是越学越难、越贵 |  | ch04 | 11 | 初定 |
| uniqueness bias / unique | 独特性偏差 / 独一无二 | 作者的概念：把自己的项目看成独一无二、没什么可借鉴的 | 独特偏见 | ch01 | 25 | 初定 |
| Eternal Beginner Syndrome | 永远的新手综合征 | 作者的说法：奥运会总是由没有办过奥运的城市来办 |  | ch05 | 1 | 初定 |
| frozen experience / unfrozen | 凝固的经验 / 未凝固的经验 | 作者仿谢林“建筑是凝固的音乐”（frozen music）造的说法：技术是凝固的经验；未凝固的经验指人亲身积累的经验 |  | ch05 | 8 | 初定 |
| tacit knowledge | 默会知识 | 波兰尼的概念：我们知道的比我们能说出的多；第 5 章小节标题 We Know More Than We Can Tell 写“我们知道的比能说出来的多” | 隐性知识（统一用默会知识） | ch05 | 6 | 初定 |
| phronesis / practical wisdom | phronesis / 实践智慧 | 亚里士多德的概念，照写斜体原文，第一次出现括注“实践智慧” |  | ch05 | 15 | 初定 |
| masterbuilder | 建造大师 | 作者的说法，得名于建造欧洲中世纪大教堂的石匠大师：经验丰富、具备实践智慧的项目负责人 | 建筑大师（指著名建筑师）；《清单革命》的“总建造师” | ch07 | 10 | 初定 |
| one-building architect | 只有一座建筑的建筑师 | 第 7 章说乌松：悉尼歌剧院之后被边缘化，再没有得到建造杰作的委托 |  | ch07 | 1 | 初定 |
| reference-class forecasting (RCF) | 参照类别预测（RCF） | 作者根据卡尼曼和特沃斯基的外部视角发展出的预测方法，和《思考，快与慢》同；第一次出现写全称再括注 RCF | 参考类别预测（中文版的译法） | ch06 | 27 | 初定 |
| reference class | 参照类别 | 同类项目组成的类别 | 参照点 | ch06 | 11 | 初定 |
| outside view / inside view | 外部视角 / 内部视角 | 卡尼曼和特沃斯基的说法，和《思考，快与慢》同 |  | ch06 | 14 | 初定 |
| one of those | “其中之一” | 把项目看成某一类项目里的一个，第 6 章小节标题 |  | ch05 | 10 | 初定 |
| anchoring and adjustment / anchor | 锚定与调整 / 锚 | 和《思考，快与慢》同；right anchor 写“正确的锚” |  | ch06 | 35 | 初定 |
| base rate | 基础比率 | 和《思考，快与慢》同；附录 A 标题写“成本风险的基础比率” | 基数、基本比率（中文版的译法） | appendix-a | 6 | 初定 |
| availability bias | 可得性偏差 | 和《思考，快与慢》同 | 易得性 | ch02 | 1 | 初定 |
| survivorship bias | 幸存者偏差 |  |  | ch07 | 3 | 初定 |
| mean / average | 均值 / 平均值 | 统计语境写“均值”，mean cost overrun 写“平均成本超支”；日常语境写“平均” |  | introduction | 45 | 初定 |
| unknown unknowns | 未知的未知 | 拉姆斯菲尔德让这个说法出了名 |  | ch06 | 8 | 初定 |
| risk mitigation / mitigate | 降低风险 / 降低、减轻 | 讲气候时 climate mitigation 写“减缓气候变化” |  | ch06 | 23 | 初定 |
| contingency / reserve | 应急储备 / 储备金 | 预算里留出的不可预见费用；contingency plans 写“应急预案” |  | ch02 | 9 | 初定 |
| buffer | 缓冲资金 / 缓冲 | 预算或工期里为超支预留的余量；每节第一次出现写“缓冲资金”，之后可简称“缓冲”；buffers of time or money 写“时间或资金上的缓冲” | 应急储备（contingency） | ch01 | 4 | 初定 |
| in real terms / final investment decision / business case | 按实际价值计算 / 最终投资决策 / 商业论证 | 作者计算成本超支的口径：不计通货膨胀，以最终投资决策时（最终商业论证里）的估算为基准；final business case 写“最终商业论证”，early outline or draft business case 写“早期的商业论证纲要或草案”；in inflation-adjusted dollars 写“按经通货膨胀调整的美元计算” | 实际上（日常说法） | ch01 | 6 | 初定 |
| nuclear storage / water projects | 核废料储存项目 / 水务项目 | 项目类型名，第 1 章和附录 A 的表格用同样的说法；water 是供水、污水处理一类项目，大坝另列（hydroelectric dams 写“水电站大坝”） | 水利工程 | ch01 | 4 | 初定 |
| inchstone / milestone | “寸程碑” / 里程碑 | inchstone 是作者团队仿 milestone 造的词，比里程碑更细的进度节点；第一次出现括注原文并加译者注 |  | ch06 | 7 | 初定 |
| Hiding Hand / providential ignorance | 隐藏之手 / 天赐的无知 | 赫希曼的说法：有一只手把困难藏了起来，人们低估了困难才敢上项目，而项目的效益常常超出预期；作者用数据反驳了这个说法。第一次出现加译者注，说明它仿“看不见的手” |  | ch07 | 5 | 初定 |
| ignorance / ignorant | 无知 / 无知的 | 第 7 章标题 |  | ch07 | 6 | 初定 |
| Hero’s Journey | 英雄之旅 | 第 7 章小节标题 The Real Hero’s Journey 写“真正的英雄之旅” |  | ch07 | 2 | 初定 |
| opportunity cost | 机会成本 |  |  | ch07 | 1 | 初定 |
| single, determined organism | 意志坚定的有机体 | 作者对好团队的比喻，第 8 章标题 |  | ch07 | 2 | 初定 |
| team / integrated team | 团队 / 一体化团队 |  |  | ch01 | 64 | 初定 |
| psychological safety | 心理安全感 | 埃德蒙森的概念：可以放心说出想法 |  | ch08 | 2 | 初定 |
| design for manufacture and assembly | 面向制造和装配的设计 | 工厂里预制、现场组装的做法 |  | ch08 | 2 | 初定 |
| modularity / modular | 模块化 / 模块化的 | 第 9 章的核心：用标准的小模块搭出大东西 |  | ch01 | 53 | 初定 |
| Lego | 乐高积木 / 乐高 | 作者对标准模块的比喻，what’s your Lego 写“你的乐高积木是什么”；公司名写“乐高” |  | ch09 | 33 | 初定 |
| scale-free scalability / scale up | 无标度的可扩展性 / 扩大规模 | 作者的说法：同样的做法放大缩小都适用，第 9 章小节标题 | 规模化 | ch08 | 18 | 初定 |
| one huge thing / many small things | 一个庞然大物 / 许多小东西 | 第 9 章开头两节的标题和全章的对照 |  | ch09 | 19 | 初定 |
| repetition / repeat | 重复 | Repeat, repeat, repeat 写“重复，重复，再重复” | 迭代（iteration） | ch01 | 36 | 初定 |
| bespoke / bespokeness | 定制 / 定制化 | 量身定制、没有标准部件；custom 也写“定制”；bespoke 和 custom 并列时写“量身定做”（“定制”和“量身定做”），tailored suit 写“量身定做的西装” |  | ch05 | 11 | 初定 |
| heuristic | 启发式 | 简单的经验法则，和《思考，快与慢》同；结语写“11 条启发式”；结语注释 3 的 positive / negative heuristics 写“正面启发式”“负面启发式”，recognition heuristic 写“再认启发式”，take-the-best heuristic 写“择优启发式”，availability heuristic 和 anchoring heuristic 写“可得性启发式”“锚定启发式” | 启发法 | ch02 | 15 | 初定 |
| leadership / project leader | 领导力 / 项目负责人 | project leadership 写“项目领导力” | 项目经理（project manager） | ch02 | 23 | 初定 |
| climate crisis / climate change | 气候危机 / 气候变化 | 第 9 章小节标题 Climate Crisis 写“气候危机” |  | ch01 | 16 | 初定 |
| renewable energy / wind power / solar power | 可再生能源 / 风电 / 太阳能发电 | offshore wind farm 写“海上风电场”，wind turbine 写“风力涡轮机” |  | ch04 | 61 | 初定 |
| high-speed rail | 高铁 | California High-Speed Rail 写“加州高铁” |  | introduction | 24 | 初定 |
| IT project | IT 项目 | information technology (IT) 第一次出现写“信息技术（IT）” |  | ch01 | 14 | 初定 |
| tunnel-boring machine | 隧道掘进机 | 第 1 章大贝尔特工程的盾构机，boring machine 和 borer 也写“掘进机” |  | ch01 | 11 | 初定 |
| contractor | 承包商 | principal contractor 写“总承包商” |  | ch01 | 25 | 初定 |
| Flyvbjerg Database | 傅以斌数据库 | 作者的项目数据库，1.6 万多个项目；附录 A 表下的 Source: Flyvbjerg Database 写“来源：傅以斌数据库” |  | ch01 | 8 | 初定 |
| Empty State Building | “空置大厦” | 大萧条时帝国大厦租不出去的绰号，谐音 Empire State Building；加译者注 |  | ch06 | 1 | 初定 |

## 机构、产品与地名

| 英文 | 译法 | 说明 |
| --- | --- | --- |
| California High-Speed Rail / Peer Review Group | 加州高铁 / 同行评审小组 | 引言起反复出现；Merced、Bakersfield、Central Valley 写“默塞德”“贝克斯菲尔德”“中央谷地” |
| Empire State Building / Empire State Inc. | 帝国大厦 / 帝国大厦公司 | Starrett Brothers and Eken 写“斯塔雷特兄弟与埃肯公司” |
| Hoover Dam | 胡佛水坝 |  |
| Great Belt project | 大贝尔特工程 | 丹麦连接西兰岛和菲英岛的桥隧工程 |
| Copenhagen Opera House / Royal Danish Opera | 哥本哈根歌剧院 / 丹麦皇家歌剧院 |  |
| Sydney Opera House | 悉尼歌剧院 |  |
| Guggenheim Museum Bilbao | 毕尔巴鄂古根海姆博物馆 | Guggenheim Bilbao 写“毕尔巴鄂古根海姆”；Solomon R. Guggenheim Foundation 写“所罗门·R.古根海姆基金会” |
| Walt Disney Concert Hall | 华特·迪士尼音乐厅 |  |
| Pentagon / Arlington Farm / Quartermaster Depot | 五角大楼 / 阿灵顿农场 / 军需仓库 | Arlington National Cemetery 写“阿灵顿国家公墓”；Construction Division 写“建设处”；War Department 写“陆军部” |
| Heathrow Terminal 5 (T5) / BAA | 希思罗机场 5 号航站楼（T5）/ BAA | BAA 原名英国机场管理局（British Airports Authority），第一次出现括注；T5 Agreement 写“T5 协议” |
| XRL / MTR | 广深港高铁香港段（XRL）/ 港铁公司（MTR） | Legislative Council 写“立法会” |
| Olympic Games / International Olympic Committee (IOC) | 奥运会 / 国际奥委会 | Montreal Olympic Stadium 写“蒙特利尔奥林匹克体育场” |
| Monju | 文殊（快中子增殖反应堆） | 日本的核电站 |
| Madrid Metro | 马德里地铁 |  |
| Ørsted / DONG Energy | 沃旭能源 / DONG Energy | 沃旭能源是公司的官方中文名，第一次出现括注 Ørsted；物理学家写“奥斯特” |
| Vestas / Maersk | 维斯塔斯 / 马士基 |  |
| Pixar / Disney / Disney Animation | 皮克斯 / 迪士尼 / 迪士尼动画 |  |
| Apple / Amazon / Microsoft / Google / Tesla / IKEA / Lego | 苹果 / 亚马逊 / 微软 / 谷歌 / 特斯拉 / 宜家 / 乐高 | Amazon Prime、Fire Phone 写“亚马逊 Prime”“Fire Phone 手机” |
| Facebook / Instagram / Twitter / SpaceX / Theranos | 照写原名 |  |
| Gigafactory 1 (Giga Nevada) | 1 号超级工厂（内华达超级工厂） |  |
| Planet Labs / CubeSat | Planet Labs / 立方星 | 卫星公司，正文也只写 Planet |
| United Artists / Columbia Pictures / Warner Bros. | 联美公司 / 哥伦比亚影业 / 华纳兄弟 |  |
| Electric Lady Studios | 电子女士录音室 | 亨德里克斯在纽约格林尼治村建的录音室；Generation nightclub 写“Generation 夜总会” |
| Gehry Partners / Gehry’s firm | 盖里事务所 |  |
| Dassault Systèmes | 达索系统 | CATIA 的开发商 |
| University of Oxford / Saïd Business School / Oxford Global Projects | 牛津大学 / 赛德商学院 / 牛津全球项目咨询公司 | OGP 写“牛津全球项目咨询公司” |
| IT University of Copenhagen / Aalborg University / Delft University of Technology | 哥本哈根信息技术大学 / 奥尔堡大学 / 代尔夫特理工大学 |  |
| McKinsey & Company / Random House / Macmillan | 麦肯锡公司 / 兰登书屋 / 麦克米伦 |  |
| International Energy Agency / International Renewable Energy Agency | 国际能源署 / 国际可再生能源署 |  |
| OPEC / OECD / United Nations / World Health Organization / UNESCO / European Union | 欧佩克 / 经合组织 / 联合国 / 世界卫生组织 / 联合国教科文组织 / 欧盟 |  |
| NASA / James Webb Space Telescope / International Space Station / Project Apollo | 美国国家航空航天局（NASA）/ 詹姆斯·韦布空间望远镜 / 国际空间站 / 阿波罗计划 |  |
| National Health Service / HealthCare.gov / Obamacare | 英国国家医疗服务体系 / HealthCare.gov / 奥巴马医改 |  |
| Basic and Primary Education Project (BPEP) | 基础与初等教育项目（BPEP） | 作者参与设计的尼泊尔学校项目 |
| Great Chicago Fire Festival | 芝加哥大火节 |  |
| Scottish Parliament Building / Brandenburg Airport / High Speed 2 (HS2) | 苏格兰议会大楼 / 柏林勃兰登堡机场 / 英国高铁 2 号线（HS2） |  |
| Channel Tunnel / Suez Canal / Ever Given | 英吉利海峡隧道 / 苏伊士运河 / “长赐”号 |  |
| Lötschberg Base Tunnel / Thames Barrier / Wembley Stadium | 勒奇山基线隧道 / 泰晤士河防洪闸 / 温布利球场 |  |
| State Route 99 tunnel | 西雅图 99 号州道隧道 |  |
| Fukushima / Chernobyl / Three Mile Island | 福岛 / 切尔诺贝利 / 三里岛 |  |
| Hornsea Project / Irish Sea | 霍恩西项目 / 爱尔兰海 | 英国的海上风电场 |
| Cobble Hill / Brooklyn / Manhattan / Greenwich Village | 科布尔山 / 布鲁克林 / 曼哈顿 / 格林尼治村 |  |
| Bilbao / Basque Country | 毕尔巴鄂 / 巴斯克地区 |  |
| Hong Kong / Pearl River Delta / Guangzhou | 香港 / 珠江三角洲 / 广州 |  |
| Nobel Prize / Pritzker Architecture Prize / Pulitzer Prize / Sonning Prize / Wolf Prize | 诺贝尔奖 / 普利兹克建筑奖 / 普利策奖 / 松宁奖 / 沃尔夫奖 |  |
| NIMBY | 邻避（NIMBY） | not in my back yard，第一次出现括注 |

## 书名与作品

| 英文 | 译法 | 说明 |
| --- | --- | --- |
| *How Big Things Get Done* | 《怎样做成大事》 | 本书，沿用中文版书名 |
| *Thinking, Fast and Slow* | 《思考，快与慢》 | 卡尼曼 |
| *The Power Broker* | 《权力掮客》 | 罗伯特·卡罗写罗伯特·摩西 |
| *The Pentagon: A History* | 《五角大楼史》 | 史蒂夫·沃格尔，暂译 |
| *Final Cut* | 《最后的剪辑》 | 史蒂文·巴赫，暂译 |
| *Easy Riders, Raging Bulls* | 《逍遥骑士，愤怒公牛》 | 彼得·比斯金德 |
| *The Box* | 《集装箱改变世界》 | 马克·莱文森，用中译本书名 |
| *The Lean Startup* | 《精益创业》 | 埃里克·莱斯 |
| *Creativity, Inc.* | 《创新公司》 | 艾德·卡特姆，只在注释里出现，注释里照写英文 |
| *Infinite Jest* | 《无尽的玩笑》 | 大卫·福斯特·华莱士 |
| *Development Projects Observed* | 《发展项目述评》 | 赫希曼 |
| “The Principle of the Hiding Hand” | 《隐藏之手原理》 | 赫希曼的文章，原题保留引号 |
| *Superforecasting* / *Risk* / *Future Babble* | 《超预测》/《风险》/《未来的胡话》 | 丹·加德纳的书，后两本暂译 |
| *Heaven’s Gate* / *Lawrence of Arabia* | 《天堂之门》/《阿拉伯的劳伦斯》 | 第 2 章 |
| *Jaws* / *Easy Rider* / *The Last Movie* | 《大白鲨》/《逍遥骑士》/《最后的电影》 | 第 7 章 |
| *King Kong* / *No Time to Die* | 《金刚》/《007：无暇赴死》 |  |
| *Toy Story* / *Up* / *Inside Out* / *Soul* / *Finding Nemo* / *The Incredibles* | 《玩具总动员》/《飞屋环游记》/《头脑特工队》/《心灵奇旅》/《海底总动员》/《超人总动员》 | 皮克斯电影 |
| *The Simpsons* | 《辛普森一家》 | 盖里客串过一集 |
| *Electric Ladyland* / *Are You Experienced* | 《电子女士之地》/《你体验过吗》 | 亨德里克斯的专辑 |
| “California Dreamin’” | 《加州梦》 | 1965 年的歌曲，引言标题 |
