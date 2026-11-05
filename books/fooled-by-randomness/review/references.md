# 参考文献（references）审校记录

全节 240 个块（一级标题 1 块，文献条目 239 块），原文没有注释；中英逐块对应（`site.py status` 显示 240/240）。

## 1. 译者自检

- 执行者：translation agent（Opus 5.5）。
- 范围：全节 240 块。按术语表的体例，这一节的条目照抄英文原文，标题译成中文：一级标题照“各节标题”表写“参考文献”，239 条文献从 `en/30-references.md` 原样复制。核对方式：
  - 用脚本比较中英两个文件，除第一行标题以外逐字节相同，块数、空行和顺序都和英文一致。
  - `python3 scripts/site.py status fooled-by-randomness` 显示本节 240/240；`python3 scripts/site.py check fooled-by-randomness` 草稿构建通过，只提示这本书还没有生成字体子集。
  - 本节没有脚注标记和脚注定义，也没有译者注。除标题外没有中文行文，所以没有需要检查漏译、增译、否定、数字和人名译法的中文句子。
- 发现并修改：复制以后没有需要改动的地方。逐条通读 239 条文献时，找到 19 项疑似笔误（作者姓名、书名、期刊名拼错，或标题缺后引号），列在下面“原文疑点”里；按体例照抄原文，中文文件里没有更正。
- 未决：
  - 条目里照抄了英文的破折号：44 条用 “———” 表示作者同上一条，Brock and De Lima (1995) 和 Gladwell (1996) 两条的英文标题里各有一个 “—”，49 条的页码或年份范围用 “–”（例如 41–42）。这些都是英文文献信息的一部分，按体例保留。如果主会话认为“中文里不用破折号”的规则也管这一节，需要另定写法，例如把 “———” 换成作者姓名。
  - 下面列出的笔误是否在中文版更正，请主会话决定。其中 Schleifer 和 Taszka 两个拼法也写在 `review/terms/people-zh.tsv` 里（Andrei Schleifer、T. Taszka），Brocas and Carillo 还出现在本节另外三条的交叉引用里；书末注释的“作者（年份）”引用要和参考文献对应，改的话要几处一起改。
  - 双语审校、中文通读和阅读器校样还没有做；`book.json` 里本节的状态仍是 `todo`，由主会话修改。

## 原文疑点

位置按 `site.py` 的块序号计，第 1 块是标题。中文文件全部照抄原文，未改。

| 位置 | 原文 | 处理 |
| --- | --- | --- |
| 第 7 块（Arthur 1994） | Arthur, Brian W. | 作者是 W. Brian Arthur，姓在前的写法应为 Arthur, W. Brian。照抄原文。 |
| 第 20 块（Brocas and Carillo 2003），以及引用它的第 17、92、234 块 | J. Carillo；In Brocas and Carillo. | 编者是 Juan D. Carrillo（查过牛津大学出版社的书目），应拼作 Carrillo。照抄原文。 |
| 第 29、44、73、107、176、223 块（Camerer et al. 2003；Dawes et al. 1989；Gigerenzer 1996；Kahneman and Lovallo 1993；Sen 1977；Tversky and Kahneman 1992） | 例如 “Clinical Versus Actuarial Judgment. *Science,* | 文章标题有前引号，缺后引号。照抄原文。 |
| 第 47 块（Debreu 1959） | *Theorie de la valeur* | 法文书名应为 Théorie，缺重音符号。照抄原文。 |
| 第 65 块（Frank and Cook 1995） | *The WinnerTake-All Society* | 书名应为 The Winner-Take-All Society，少一个连字符。照抄原文。 |
| 第 66 块（Frederick and Loewenstein 1999） | in Kahneman, Diener and Schwartz | 这本书的编者是 Norbert Schwarz，第 185 块引用同一本书写作 Schwarz。照抄原文。 |
| 第 77 块（Gilbert et al. 2002） | T. Weatley | 作者是 Thalia Wheatley，应拼作 Wheatley。照抄原文。 |
| 第 87 块（Goodman 1954） | *Facts, Fiction and Forecast* | 书名是 Fact, Fiction, and Forecast。照抄原文。 |
| 第 105 块（Kahneman, Knetsch and Thaler 1986） | ———, J. L. Knetsch, and R. H. Thaler, 1986, “Rational Choice and the Framing of Decisions.” | 作者和题目对不上。这个题目的论文作者是 Tversky and Kahneman，刊在 Journal of Business 第 59 卷第 4 期第 2 部分，页码 S251 到 S278（查过 JSTOR 上这一期的目录）。Kahneman、Knetsch 和 Thaler 在同一期发表的是 “Fairness and the Assumptions of Economics”，页码 S285 到 S300。书末注释“相对地位与绝对地位”一条写“见 Kahneman, Knetsch and Thaler (1986)”，读者按这一条去找，会找到 Tversky 和 Kahneman 的论文；按注释的内容，作者想引的可能是这三人 1986 年讨论公平的论文，属于疑似。照抄原文。 |
| 第 116 块（Keynes 1937） | “The General Theory.” In *Quarterly Journal of Economics,* Vol. LI, 209–233. | 文章题目是 “The General Theory of Employment”，刊在第 51 卷第 2 期（1937 年 2 月），页码是 209 到 223（JSTOR 1882087）。照抄原文。 |
| 第 117 块（Keynes 1989 (1920)） | ———, 1989 (1920), *Treatise on Probability.* | 这本书初版于 1921 年，原题是 A Treatise on Probability。书末注释“凯恩斯”和“概率的思想家与哲学家”两条也写作 (Keynes, 1989, 1920)，和这一条一致。照抄原文。 |
| 第 121 块（Krebs and Davies 1993） | Kreps, J., and N. B. Davies | 《行为生态学导论》的作者是 J. R. Krebs，应拼作 Krebs；和第 120 块的 David M. Kreps 不是同一个人。照抄原文。 |
| 第 136 块（Magee 1997） | Weidenfeld & Nicholson | 出版社名是 Weidenfeld & Nicolson。照抄原文。 |
| 第 137 块（Mandelbrot 1997） | Springder-Verlag | 出版社名是 Springer-Verlag。照抄原文。 |
| 第 139 块（Meehl 1954） | *Clinical Versus Statistical Predictions: A Theoretical Analysis and Revision of the Literature.* | 书名是 Clinical versus Statistical Prediction: A Theoretical Analysis and a Review of the Evidence（查过 Internet Archive 收的原书和纽约大学图书馆的目录）。原文把 Prediction 写成了复数，副标题也不对。书末注释“临床知识”一条引用的 Meehl (1954) 指的就是这本书。照抄原文。 |
| 第 162 块（Rabin 2000） | Rabin, Mathew | 作者名是 Matthew Rabin。照抄原文。 |
| 第 172 块（Shleifer 2000） | Schleifer, Andrei | 作者姓 Shleifer。照抄原文。 |
| 第 175 块（Searle 2001） | Searle, John, J. | 作者是 John R. Searle（John Rogers Searle），中间名的缩写应为 R.，原文写成了 J.。名字和缩写之间的逗号和第 176 块 “Sen, Amartya, K.” 的写法一样，是本书的格式，不算错。照抄原文。 |
| 第 176 块（Sen 1977） | “Rational: A Critique of the Behavioral Foundations of Economic Theory. | 论文题目是 “Rational Fools: A Critique of the Behavioral Foundations of Economic Theory”，少了 Fools，也缺后引号。照抄原文。 |
| 第 185 块（Shizgal 1999） | Brain Simulation Rewards | 应为 Brain Stimulation Reward（脑刺激奖赏）。照抄原文。 |
| 第 215 块（Tyszka and Zielonka 2002） | Taszka, T. | 作者是 Tadeusz Tyszka（查过论文 PDF），应拼作 Tyszka。照抄原文。 |
| 第 220 块（Tversky and Kahneman 1971） | *Psychology Bulletin* | 期刊名是 Psychological Bulletin。照抄原文。 |
| 第 229 块（Weinberg 2001） | *Facing Up: Science and Its Cultural Adversaries.* Working Paper. Harvard University. | 这是哈佛大学出版社 2001 年出版的文集（查过哈佛大学出版社和 Internet Archive 的书目），原文把它标成了工作论文（Working Paper）。第三轮审校时补进。照抄原文。 |
| 第 237 块（Zajdenweber 2000） | *L’économie des extrèmes* | 法文应为 extrêmes。照抄原文。 |
| 第 238 块（Zajonc 1980） | Preferences Need No Infderences | 应为 Inferences。照抄原文。 |
| 第 239 块（Zajonc 1984） | *American Psychologist,* 39, 117–123, 114. | 这篇文章刊在第 39 卷第 2 期，页码是 117 到 123（查过出版信息）。后面的 “, 114” 含义不明，疑为多余。照抄原文。 |

## 2. 双语审校

- 执行者：另一个独立上下文的 agent（Opus 5.5），没有参与翻译。
- 范围：对照英文逐块看完全节 240 块，核对中文文件和英文是否逐块对应、除标题以外是否逐字照抄、Markdown 斜体和链接是否保留；逐条核对了译者列出的 19 项原文疑点，并用脚本检查了引号是否成对和破折号的数量。本节没有脚注和译者注。审校者没有改动文件，发现交给编辑逐条核实后处理。
- 发现：4 条；核实后采纳 4 条，不采纳 0 条。四条都是英文条目本身的笔误，译者自检时没有记下。编辑逐条对照了英文原文，又查了外部书目（JSTOR、Internet Archive 和图书馆目录），每条说的都成立。按体例，中文文件照抄原文，不作更正；这些笔误补进了“原文疑点”表。
  - 第 105 块，作者写作 Kahneman, J. L. Knetsch, and R. H. Thaler，题目是 “Rational Choice and the Framing of Decisions.”：采纳，四条里这一条最要紧。JSTOR 上 Journal of Business 1986 年第 59 卷第 4 期第 2 部分的目录显示，这个题目的作者是 Tversky 和 Kahneman（S251 到 S278 页）；Kahneman、Knetsch 和 Thaler 三人在同一期发表的是 “Fairness and the Assumptions of Economics”（S285 到 S300 页）。书末注释“相对地位与绝对地位”一条写“见 Kahneman, Knetsch and Thaler (1986)”，读者按这一条去找会找错文章。编辑在表里另外写明：按注释的内容，作者想引的可能是这三人 1986 年讨论公平的论文，属于疑似。
  - 第 116 块 “The General Theory.” In *Quarterly Journal of Economics,* Vol. LI, 209–233.：采纳。文章题目是 “The General Theory of Employment”，第 51 卷第 2 期，页码是 209 到 223（JSTOR 1882087 的出版信息）。
  - 第 139 块 *Clinical Versus Statistical Predictions: A Theoretical Analysis and Revision of the Literature.*：采纳。Internet Archive 收的原书和纽约大学图书馆的目录都写作 Clinical versus Statistical Prediction: A Theoretical Analysis and a Review of the Evidence，原文把 Prediction 写成了复数，副标题也不对。
  - 第 175 块 “Searle, John, J.”：采纳，表里的说法改了一处。作者是 John R. Searle，错在中间名的缩写写成了 J.。审校者还说缩写前面多了一个逗号，可是第 176 块 “Sen, Amartya, K.” 也在名字和缩写之间加逗号，这是本书条目的统一格式，所以表里没有把这个逗号算作笔误。
  - 审校者在总体判断里顺带提到第 117 块 “1989 (1920), *Treatise on Probability.*” 的初版年份：也采纳。这本书初版于 1921 年，原题是 A Treatise on Probability；书末注释两处写作 (Keynes, 1989, 1920)，和这一条一致，一并记在表里。
  - 编辑核对时另外发现一处，也补进了表里：第 239 块 Zajonc (1984) 的页码写作 “117–123, 114”，查到的页码是 117 到 123，后面的 “, 114” 含义不明。
  - 没有不采纳的发现。
- 审校者的总体判断：译文本身没有问题，可以通过。中文文件和英文逐块对应（240/240），第一行“# 参考文献”和术语表的“各节标题”一致，其余 239 条和英文逐字节相同，斜体和链接原样保留，符合术语表“这一节的条目照抄英文原文，只译标题”的体例。译者列出的 19 项原文疑点，块序号、引文和正确拼法都核对无误；缺后引号的正好是表里列的 6 条，破折号的统计也和文件一致。条目里的 “———”、“—” 和 “–” 都属于照抄的英文书目信息（“———” 表示作者同上一条，“–” 用在页码范围里），“中文不用破折号”的规则管的是中文行文，这一节没有中文行文，保留是对的，审校者建议关闭译者自检里的这一项“未决”。需要补的只有上面四条原文笔误。

## 3. 中文通读

- 执行者：编辑 agent（Opus 5.5）。
- 范围：采纳双语审校以后，从标题读到第 240 块。这一节的中文行文只有标题“参考文献”，所以通读检查的是：标题和术语表一致；条目照抄英文，能和书末注释里“作者（年份）”形式的引用对上；人名按体例保留英文；条目的顺序和空行和英文一致。
- 发现并修改：没有需要修改的地方。中文文件没有改动，所以没有需要回查英文的改动。检查过、保留原样的：
  - 用脚本比较中英两个文件，第 2 块到第 240 块逐字节相同；Burnham (1997)、Mumford (1999)、Rabin (2000) 和 Slovic et al. (2003) 四条里的链接，链接文字和链接地址都和英文一样。
  - 书末注释引用的 Kahneman, Knetsch and Thaler (1986)、Meehl (1954) 和 (Keynes, 1989, 1920) 在本节都有对应条目，写法一致。这几条的原文笔误已经记进“原文疑点”，注释那一节如果要加说明，可以参照这里。
  - 有几条在逗号后漏了空格（例如第 52 块 “Easterly, William,2001”，第 112 块 “,and A. Tversky,1982,”），属于排版问题，不影响查找文献，按体例照抄，没有记进“原文疑点”。
- 修改后的检查：`python3 scripts/site.py status fooled-by-randomness` 显示本节 240/240；`python3 scripts/site.py check fooled-by-randomness` 草稿构建通过，只提示这本书还没有生成字体子集。

## 状态

- 没有未解决的意义问题。全节条目照抄英文原文，25 项原文疑点（含这次补的 6 项）都记在“原文疑点”表里，中文文件没有更正。
- 译者自检留下的两项“未决”，编辑的意见：
  - 破折号：同意审校者的看法，条目里的 “———”、“—” 和 “–” 属于照抄的英文书目信息，按术语表的体例保留。请主会话确认后关闭这一项。
  - 原文笔误是否在中文版更正：仍由主会话决定。要改的话，第 20 块的 Carillo 要和第 17、92、234 块一起改，Schleifer 和 Taszka 要和 `review/terms/people-zh.tsv` 一起改；第 105 块如果更正，书末注释“相对地位与绝对地位”一条的引用也要一起处理。
- 还没做的：阅读器校样（第 4 节）。`book.json` 里本节的状态仍是 `todo`，由主会话修改。

## 第三轮：GPT-6 Astra 独立审校

- 审校者：GPT-6 Astra，通过 Codex 运行，只读，和译者属于不同的模型家族。
- 发现：0 条。审校者逐块核对了全节，认为译文没有问题：标题照“各节标题”写“参考文献”，239 条文献照抄英文，条目里的 “———”“—”“–” 属于术语表允许的英文书目格式。逐块找到中英文对应的句子，读过上下文后复核：成立并修改 0 条，不成立 0 条。另外，审校者列了 20 条对英文原文的疑问，见下面“对英文原文的疑问”。
- 成立并修改：无。
- 不成立，保留原译：无。
- 按全书统一的写法修改：0 处。逐条对照后本节已经符合：用脚本比较中英两个文件，除第一行标题外逐字节相同，符合“参考文献条目和书末注释的‘作者（年份）’引用照抄原文，原文的笔误也照抄”这一条；Brocas and Carillo、Schleifer、Taszka、Kahneman, Knetsch and Thaler (1986) 的题目和 Keynes 两条的年份、页码都照原文保留，中文版不加说明；标题“参考文献”和“各节标题”一致；本节没有中文句子，所以数字、人名括注、破折号和体例禁用的对比句式这几条没有可改的地方。
- 对英文原文的疑问：审校者列了 20 条，逐条对照英文和上面的“原文疑点”表：
  - 19 条表里已经有了，说法和表里一致：缺后引号的 6 条，Carillo，WinnerTake-All，Weatley，Facts, Fiction and Forecast，Kahneman, Knetsch and Thaler (1986) 的作者和题目对不上，Keynes (1937) 的题目和页码，Keynes 的初版年份，Kreps 应为 Krebs，Springder-Verlag，Mathew，Schleifer，Searle, John, J.，Sen (1977) 漏了 Fools，Shizgal (1999) 的 Brain Simulation Rewards，Taszka，Psychology Bulletin，Infderences，Zajonc (1984) 页码后多出的 114。
  - 1 条是新的，补进了表里：第 229 块 Weinberg (2001) 写作 “*Facing Up: Science and Its Cultural Adversaries.* Working Paper. Harvard University.”。查了哈佛大学出版社和 Internet Archive 的书目，这是哈佛大学出版社 2001 年出版的文集，原文把它标成了工作论文。书名和年份都对，读者按这一条能找到书末注释“公共知识分子与科学知识分子”一条引用的 Weinberg (2001)。按体例照抄原文，中文文件没有更正。现在“原文疑点”表里一共 26 项。
- 核实与修改：agent（Opus 5.5）。本轮没有改动 `zh-cn/30-references.md`，只在本记录的“原文疑点”表里补了第 229 块一行。运行 `python3 scripts/site.py status fooled-by-randomness`，本节显示 240/240 块已译，原文没有注释。
