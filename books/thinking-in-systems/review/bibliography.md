# 系统学习资源书目（bibliography）审校记录

全节 24 个块，原文没有脚注，中英逐块对应（`site.py status` 显示 24/24）；译文没有加译者注。下文的“第 N 块”按 `site.py status` 计数的 24 个可译块编号，从节名算起。

## 1. 译者自检

- 执行者：translation agent（Opus 5.5）。
- 范围：从节名到最后一个条目，全节 24 块逐块对照英文：节名、开头的说明段、6 个分组标题、16 个书目和机构条目（第 12 块一段里有两个机构条目）。检查漏译、增译、否定、条件、数字和日期、谁做了什么、比较对象、术语义项、人名、书名和链接；用框架的 markdown-it 逐块渲染中英两边，比较每块的斜体和链接个数（两边相同）以及数字（两边相同）；在 `/tmp` 下复制一份书，把本节临时设成 draft 构建，24 个单元都在，中文页面文字里没有残留的星号；用 `tools/term_consistency.py` 查本节；全文查破折号和体例禁用的对比句式。
- 发现并修改：
  - 第 14 块 “dedicated to the development and use of systems thinking and system dynamics around the world”：初稿“面向在世界各地致力于发展和运用……的研究者”，读起来像是说这些研究者分布在世界各地；原文 around the world 修饰的是发展和运用。改为“面向致力于在世界各地发展和运用系统思考与系统动力学的研究者、教育者、咨询顾问和实践者”。
  - 第 2 块 “the items listed here are jumping off points”：初稿“这里列出的条目”，这段说明在条目前面，改为“下面列出的条目也是一些起点”；破折号后面的 places to start your search 改成冒号后的一句“你可以从这里出发，去寻找更多观察系统、了解系统的途径”。
- 写法上的决定，供主会话参考：
  - 条目格式：照术语表“参考书目条目照写英文”，每个条目的作者、书名、卷名、出版地、出版社和年份逐字照英文，斜体和标点也照英文；条目后面的英文说明译成中文，接在英文出处后面，中间空一格。例如第 7 块 “First published in 1968, this is the original introductory text on system dynamics.” 写“此书初版于 1968 年，是系统动力学最早的入门教材。”。没有说明文字的 6 个条目（第 8、18、19、21、23、24 块）中文和英文相同，其中第 23 块按原文疑点改了一个拼写，见下面“原文疑点”。
  - 机构条目：段首的机构名照写英文（Creative Learning Exchange、isee systems, inc.、Pegasus Communications、Ventana Systems, Inc.），英文的破折号改成中文冒号。System Dynamics Society 有通行的中文名，第 14 块写“System Dynamics Society（系统动力学学会）：”，同一块说明文字里的 the System Dynamics Society 照术语表写“系统动力学学会”。附录正文把这两家公司写成“isee systems 公司”“Ventana Systems 公司”；这里是条目名，保留了英文的 inc.、Inc.。
  - 刊物和软件名：*The CLE Newsletter*、*The Systems Thinker*、*Leverage Points*、*System Dynamics Review* 这几份刊物没有通行的中文名，照写英文并保留斜体，写法和条目里的出处一致；软件 *STELLA*、*iThink*、*Vensim* 同样照写。
  - 第 12 块 “in K–12 education”：写“在幼儿园到 12 年级的基础教育中”，范围照术语表写“到”。
  - 第 17 块 “mental-model flexibility and visioning”：写“保持心智模型的灵活性、构建愿景”，mental model 照术语表写“心智模型”，visioning 照《第五项修炼》中译本的“愿景”写“构建愿景”。
  - 分组标题：Books 写“图书”，Organizations, Websites, Periodicals, and Software 写“机构、网站、期刊与软件”，Business 写“商业”，Society, and Social Change 写“社会与社会变革”。
  - 第 2 块英文在网址后面没有句号，中文句末补了句号。
- 检查：
  - `site.py status` 显示 24/24；临时构建里本节 24 个单元都在，节名显示为“系统学习资源书目”。
  - `term_consistency.py` 在本节报了 21 处，都在照写英文的出处里：16 处是条目里的英文人名（Bossel、Forrester、Laszlo、Richardson、Sweeney、Meadows、Senge、Sherwood、Sterman、Ford、Macy），其余 5 处是书名或刊名里的词：第 6 块 *System Zoo Simulation Models* 的 system zoo，第 13 块 *Leverage Points* 的 leverage point，第 18、19 块书名里的 Systems Thinking。说明文字里没有提到人，所以本节没有需要括注的中文人名。
  - 数字：“100 多个”“1968 年”“30 个”“12 年级”和英文一致；出处里的年份照英文。
  - 全节中文没有破折号，也没有体例禁用的对比句式。
- 未决：
  - 第 17、19 块的 *The Fifth Discipline* 和 *Business Dynamics* 有通行的中译本（《第五项修炼》《商务动态分析方法》），第 24 块 *The Global Citizen* 和正文的“全球公民”专栏同名。按术语表，条目照写英文，我没有加译者注；如果主会话想让中文读者知道有中译本，可以考虑在这几条后面加译者注。（已定：不加译者注。术语表“全书统一的写法（译完后定）”里“参考书目”一条写明条目照写英文，有通行中译本的书（The Fifth Discipline 即《第五项修炼》，Business Dynamics）不加译者注；第 24 块的 *The Global Citizen* 照术语表“机构、产品与地名”表里 The Global Citizen 一行，参考书目里同名的书照写英文，同样不加注。）

## 原文疑点

| 位置 | 原文 | 处理 |
| --- | --- | --- |
| 第 23 块 | Albany, NY: Stat University of New York Press | 应为 State University of New York Press，`review/source.md` 已列。按术语表“原文疑点”一条，中文的出处写成 State |
| 第 14 块 | *The Systems Dynamics Review* is the official journal of the System Dynamics Society | 这份期刊的名字是 *System Dynamics Review*（系统动力学学会网站和出版社 Wiley 的期刊页都这样写），原文多了 The 和 s。中文写 *System Dynamics Review* |
| 第 12 块 | …[www.clexchange.org](http://www.clexchange.org) isee systems, inc.—Developer of *STELLA*… | Creative Learning Exchange 和 isee systems 两个条目在同一段里，其他机构条目都是一条一段，可能是纸质版转 EPUB 时漏了分段。`en/` 照原样保留，中文也写成一块，两个条目之间照英文空一格 |

## 2. 双语审校

- 执行者：另一个独立上下文的 agent（Opus 5.5），没有参与翻译。
- 范围：全节 24 块逐块对照英文：节名、开头的说明段、6 个分组标题、16 个书目和机构条目。核对了条目出处是否逐字照英文（作者、书名、卷名、出版地、出版社、年份、斜体和标点），六个链接、数字、人名括注、破折号和体例禁用的对比句式，以及原文疑点表里的三处处理。
- 发现：4 条（1 条意义，3 条表达）；编辑逐条对照英文核实后采纳 4 条，不采纳 0 条。其中两条按审校者的思路采纳，但用了编辑自己的写法：
  - 采纳（意义），第 14 块 “an international forum for researchers, educators, consultants, and practitioners dedicated to the development and use of systems thinking and system dynamics around the world”：初稿把“致力于……”安在研究者等人身上。dedicated to 说的是学会这个论坛本身：学会自己的介绍写 “an international, nonprofit organization devoted to encouraging the development and use of systems thinking and System Dynamics modeling around the world”，编辑在学会网站的文件里查到了这句话；上一条 Creative Learning Exchange 的 an organization devoted to developing 也是同样的结构。改为“一个面向研究者、教育者、咨询顾问和实践者的国际论坛，致力于在世界各地发展和运用系统思考与系统动力学”。审校者建议写“汇聚研究者……”，编辑用“面向”，和原文的 a forum for 更贴近。
  - 采纳（表达），第 12、15 块 “Developer of *STELLA* and *iThink* software for modeling dynamic systems”“Developer of *Vensim* software for modeling dynamic systems”：“用于为动态系统建模的软件……的开发商”两层定语叠在一起。改为“动态系统建模软件 *STELLA* 和 *iThink* 的开发商”“动态系统建模软件 *Vensim* 的开发商”，用了审校者给的第二种写法，保留英文 Developer of 的名词句式。
  - 采纳（表达），第 5 块 “for understanding and modeling the complex systems shaping the dynamics of our world, with a large bibliography on systems”：两句里“复杂系统”出现三次；“大量关于系统的参考书目”改成一份书目更清楚。改为“介绍理解复杂系统、为它们建模的基本概念和方法，这些系统塑造着我们这个世界的动态。书中还附有一份很长的系统类参考书目”。审校者建议的“正是这些系统”加了原文没有的强调，“书后”原文也没有说，这两处编辑没有用。
  - 采纳（表达），第 17 块 “the broader philosophical tools that arise from and complement systems thinking, such as mental-model flexibility and visioning”：前置定语太长，“系统思考”一句里出现三次。审校者建议的写法把“例如……”放在“相辅相成”后面，例子离“哲学工具”太远。编辑改为“也讲述范围更广的哲学工具，例如保持心智模型的灵活性、构建愿景；这些工具源自系统思考，又与它相辅相成”，例子紧跟“哲学工具”，“系统思考”减到两次。
- 审校者的总体判断：译文总体可靠，可以接受。条目数和顺序、各级标题、出处、链接、数字都和英文一致，原文疑点表里的三处处理符合术语表；需要改的是 System Dynamics Society 条目里“致力于”说的是谁，以及三处偏欧化的表达。这几处改完后，本节可以进入中文通读。

## 3. 中文通读

- 执行者：编辑 agent（Opus 5.5）。
- 范围：按上面四处改动后的中文，从节名读到最后一个条目，检查连贯、重复、指代，以及机构名、软件名、刊物名和术语（系统思考、系统动力学、心智模型、动态）在全节是否一致。
- 发现并修改：1 处，已回查英文。
  - 第 12 块 “Creative Learning Exchange—an organization devoted to developing “systems citizens” in K–12 education. Publisher of *The CLE Newsletter* and books for teachers and students.”：“一个致力于在幼儿园到 12 年级的基础教育中培养‘系统公民’的组织”是一串带两个“的”的前置定语，和本次已经改掉的长定语是同一个问题；“出版 *The CLE Newsletter*，以及……书籍”中间的逗号把书籍和通讯隔开了。改为“这个组织致力于在幼儿园到 12 年级的基础教育中培养‘系统公民’，出版 *The CLE Newsletter* 以及面向教师和学生的书籍”。an organization 的意思由“这个组织”保留，出版的东西和英文一样是通讯和书两样。
- 检查：改动后 `site.py status` 仍显示本节 24/24；全节中文没有破折号，也没有体例禁用的对比句式；斜体和链接都没有动。

## 状态

本节没有未解决的意义问题。原文疑点表里的三处都已按术语表处理。译者自检里提出的一个可选做法还等主会话决定：要不要给 *The Fifth Discipline*、*Business Dynamics* 等有通行中译本的条目加译者注。（已定：不加译者注，见术语表“全书统一的写法（译完后定）”里“参考书目”一条。）

## 第三轮：GPT-6 Astra 独立审校

- 审校者：GPT-6 Astra，通过 Codex 运行，只读，和译者属于不同的模型家族。
- 发现：0 条。审校者逐块核对了全节，结论是没有需要修改的实质性翻译问题，也没有明确违反体例的地方。核实者又逐块找到中英文对应的句子，读过上下文后复核：成立并修改 0 条，不成立 0 条。复核时用脚本比对了 12 个书目条目的出处部分，11 条和英文逐字相同，第 23 块只差原文疑点表里改过的 State 一词；6 个链接、斜体、数字（“100 多个”“1968 年”“30 个”“12 年级”）都和英文一致。
- 成立并修改：无。
- 不成立，保留原译：无。
- 按全书统一的写法修改：0 处。逐条对照了术语表的“全书统一的写法”和“全书统一的写法（译完后定）”，这一节已经符合：
  - 节名“系统学习资源书目”和“各节标题”表一致。
  - “参考书目”一条：条目照写英文，*The Fifth Discipline*、*Business Dynamics* 不加译者注，现在的译文就是这样写的。
  - “人名”一条：条目里的作者照写英文；说明文字里没有提到人，所以没有要照 people-zh.tsv 译的人名。
  - 机构和软件：Pegasus Communications、Creative Learning Exchange 照写原名，说明文字里的 the System Dynamics Society 写“系统动力学学会”，*STELLA*、*iThink*、*Vensim* 照写原名，都和术语表“机构、产品与地名”表一致。
  - 数字：“100 多个”和第 2 章脚注 2 的“100 多种‘动物’”写法相同；“两份通讯”是十以内的数，写汉字；“30 个”是 11 以上的确数，写阿拉伯数字。
  - 中文没有破折号，也没有体例禁用的对比句式；K–12 写“幼儿园到 12 年级”，范围写“到”。
- 留给主会话决定的事项：译者自检的“未决”和文末“状态”里都写着，要不要给有通行中译本的条目加译者注还等主会话决定。术语表“全书统一的写法（译完后定）”里“参考书目”一条已经定下：不加译者注。两处都已在原处标为已定。
- 对英文原文的疑问：审校者提出 2 条，都已在上面“原文疑点”表里，中文已经按正确的写法处理：
  - 第 14 块 *The Systems Dynamics Review* 应为 *System Dynamics Review*，中文写 *System Dynamics Review*。
  - 第 23 块 Stat University of New York Press 应为 State University of New York Press，中文写 State。
- 核实与修改：agent（Opus 5.5）。核实后中文译文没有改动，审校记录里两处待定事项标为已定。运行 `python3 scripts/site.py status thinking-in-systems`，bibliography 一行显示 review，24/24 块已译，这一节没有脚注；全书 19 节都是 review，1115/1115 块已译。
