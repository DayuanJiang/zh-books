# 注释（notes）审校记录

全章 443 个块，中英逐块对应（`site.py status` 显示 443/443）。书末注释按章分组，每条注释开头是一句“提示语”，也就是引出这条注释的那句正文原话，后面是说明文字和英文引文。引文（作者、标题、刊名、出版社、页码）保留英文，引文前后的说明文字译成中文。译者注共 6 条，编号按出现顺序排列。

## 原文修复

### 译者的修复

导入的 EPUB 里，书末注释有 49 处乱码。翻译这一章的 agent 按上下文和已知文献修复后再翻译，修复后英文从 446 块变为 443 块：有两处乱码把一条注释断成了两段，已合并；另有一个游离的乱码段落已删除。

编辑核对时，又用了用户上传的同一本书的 Kindle 文件（`/tmp/zed-uploads-1000/` 下的 AZW3）。用 `mobi` 工具包把它解开后，Kindle 文件里的注释没有这些乱码，于是逐段比较了它和修复后的英文。去掉开头的总标题和“引言”小标题后，两边都是 441 段（包括各章的小标题），一一对应。下表最后一列是核对结果：

| 损坏的原文 | 修复后 | 和 Kindle 文件核对 |
| --- | --- | --- |
| `Annual Review of Psychology 59 (2008): 25 {59 eight="0%"5–78.` | `Annual Review of Psychology 59 (2008): 255–78.` | 一致 |
| `followed by Y ELLOW printed in green` | `followed by YELLOW printed in green` | 一致 |
| `Wouter Kool et {ute979): 1289al.,` | `Wouter Kool et al.,` | 一致 |
| `po {"><21; : Sian L. Beilock` | `pointless anxious thoughts: Sian L. Beilock` | 一致 |
| `M. Rosario Rued { Rocenca et al.` | `M. Rosario Rueda et al.` | 一致 |
| `Journal of Personality and Social Psychology {gy` | `Journal of Personality and Social Psychology 58 (1990): 308–18.` | 一致 |
| `Matthew S. Mc Glone` | `Matthew S. McGlone` | Kindle 文件里也有这个空格，属于电子书的排版残留，保留修复 |
| `Rhyme as Reas {RhyPsychological Science` | `Rhyme as Reason in Aphorisms,” Psychological Science` | 一致 |
| `Influence Shortand Long-Run` | `Influence Short- and Long-Run` | Kindle 文件里也丢了连字符，保留修复 |
| `Affect Determine {ectition Intuitive` | `Affect Determine Intuitive` | 一致 |
| `“Forming {#823.` 加下一段 `Impressions of Personality,”` | `“Forming Impressions of Personality,”` | 一致 |
| `95–96 sentence was literally true: … Howard G. Boo {How>` 加下一段 `Journal of Verbal` | `sentence was literally true: Sam Glucksberg, Patricia Gildea, and Howard G. Bookin, “On Understanding Nonliteral Speech: Can People Ignore Metaphors?” Journal of Verbal` | 作者名和论文标题与 Kindle 文件一致；句首的 `95–96` 在 Kindle 文件里也有，应是纸质版注释按页码分组时的页码，删除保留 |
| `happiness quest {ppiournal ofion.` | `happiness question.` | 一致 |
| `Person {pantion ality and Social` | `Personality and Social` | 一致 |
| `Alexander Rotliman` | `Alexander Rothman` | Kindle 文件里也是 Rotliman，属于文字识别错误（h 认成了 li），保留修复 |
| `351 (1996): 141–20.` | 译者改为 `1413–20.` | Kindle 文件里也是 `141–20`，这处毛病出在英文电子书本身，编辑撤回了这处修复，列入下面的原文疑点 |
| `the solutions that have {ns problems,the largest benefits` | `the solutions that have the largest benefits` | 一致 |
| `A Social Institutionist Approach` | 译者改为 `A Social Intuitionist Approach` | Kindle 文件里也是 Institutionist，编辑撤回了这处修复，列入原文疑点 |
| `said 4, 000 children` | `said 4,000 children` | Kindle 文件里也有这个空格，保留修复 |
| `(.03/. 97 = .031)` | `(.03/.97 = .031)` | Kindle 文件里也有空格，保留修复 |
| `4 × . 031 = 12.4` | `4 × .031 = 12.4` | 同上 |
| `From these odds you can { odes as l compute` | `From these odds you can compute` | 一致 |
| `12.4/112. 4 = .11` | `12.4/112.4 = .11` | Kindle 文件里也有空格，保留修复 |
| `.706/1. 706 = .41` | `.706/1.706 = .41` | 同上 |
| `when the statistica {he deviatiol distributions` | `when the statistical distributions` | 一致 |
| `The relevant formula is v (1–r2)` | `The relevant formula is √(1–r²)` | Kindle 文件里也是 `v (1–r2)`，根号和上标在电子书里丢了，保留修复 |
| `Outcome Bias in Decision {s iiv> Evaluation` | `Outcome Bias in Decision Evaluation` | 一致 |
| `Rosenz {lenlatweig, The Halo Effect.` | `Rosenzweig, The Halo Effect.` | 一致 |
| `(Mean-while, his replacement` | `(Meanwhile, his replacement` | Kindle 文件里也有这个断词连字符，保留修复 |
| `Expert Political Judgment:̶> How Good is It?` | `Expert Political Judgment: How Good is It?` | 一致 |
| `## 2 {ce` | `## 22: Expert Intuition: When Can We Trust It?` | 一致 |
| `impersonality of procedures: Fo {i>How Doctors Think` | 译者改为 `impersonality of procedures: Jerome Groopman, How Doctors Think` | Kindle 文件里作者名前还有一句引导语，编辑按 Kindle 文件补全为 `For an example of the doubts about evidence-based medicine, see Jerome Groopman, How Doctors Think` |
| `Journal of Business Venturing 24 ( {>` | `Journal of Business Venturing 24 (2009): 149–64.` | 一致 |
| `Michael T. Stalk-fleet` | `Michael T. Stalkfleet` | Kindle 文件里也有这个断词连字符，保留修复 |
| `## 26: Prospect Theory` 后面游离的 `ast="2%">` 段落 | 删除 | 一致（块数和 Kindle 文件对得上） |
| `in the range of 1. 5 and 2.5` | `in the range of 1.5 and 2.5` | Kindle 文件里也有空格，保留修复 |
| `Organiz {an>y did not ational Behavior` | `Organizational Behavior` | 一致 |
| `Brian Knutson an {an utson et ad Stephanie M. Greer` | `Brian Knutson and Stephanie M. Greer` | 一致 |
| `Kne {ers): tsch’s exchange` | `Knetsch’s exchange` | 一致 |
| `you will not be unable to afford` | 译者改为 `you will be unable to afford` | Kindle 文件里也有 not，编辑撤回了这处修复，见下文 |
| `5 (200 {/spFac1): 323.` | `5 (2001): 323.` | 一致 |
| `commit you to accept an { to>` | 译者补为 `commit you to accept and that is guaranteed to cause a loss.` | 意思对，措辞和 Kindle 文件不同，编辑按 Kindle 文件改为 `commit you to accept and is guaranteed to end up in a loss.` |
| `“The {r, n>: C. A Affect Heuristic.”` | `“The Affect Heuristic.”` | 一致 |
| `Journal of E {>Joenon?&conomic Behavior` | `Journal of Economic Behavior` | 一致 |
| `some attributes {e a#822become evaluable` | `some attributes become evaluable` | 一致 |
| `Asian flu epidem {an s less ic of 1957.` | `Asian flu epidemic of 1957.` | 一致 |
| `but { thk-e she was regarded` | `but she was regarded` | 一致 |
| `distributio {i>dll-Being: Ed Diener` | `distribution of emotional pain: Ed Diener` | 一致 |
| `American C {he on, Rouncil on Education` | `American Council on Education` | 一致 |

49 处里，31 处与 Kindle 文件完全一致；13 处 Kindle 文件里也有同样的毛病，都是数字里多出的空格、丢失的连字符或符号、文字识别错误和纸质版页码这类电子书排版残留，修复保留；其余 5 处由编辑撤回或改正，见下一节。

### 译者没有把握的 11 处

| 位置 | 译者的处理 | 核对结果 |
| --- | --- | --- |
| 第 3 章 `po {"><21; :` | 恢复为 pointless anxious thoughts | Kindle 文件证实 |
| Greenberg 等人 1990 年的论文，卷号和页码丢失 | 补为 `58 (1990): 308–18` | Kindle 文件证实 |
| `Rhyme as Reas {Rhy` | 补为 Rhyme as Reason in Aphorisms,” | Kindle 文件证实 |
| 第 8 章 Glucksberg 一条，作者名截断，标题丢失 | 补成 Bookin 和完整标题，删掉句首的 `95–96`，两段合并 | Kindle 文件证实作者名和标题；`95–96` 在 Kindle 文件里也有，是纸质版页码，删除正确 |
| Damasio 的页码 `141–20` | 改为 `1413–20` | Kindle 文件里也是 `141–20`，撤回，列入原文疑点 |
| Haidt 的 Institutionist | 改为 Intuitionist | Kindle 文件里也是 Institutionist，撤回，列入原文疑点 |
| 第 23 章 `Fo {i>How Doctors Think` | 补为 Jerome Groopman, How Doctors Think | 作者名正确；Kindle 文件里前面还有一句 For an example of the doubts about evidence-based medicine, see，已补上，中文相应译为“怀疑循证医学的一个例子，见” |
| Cassar 与 Craig 的出处 | 补为 `24 (2009): 149–64` | Kindle 文件证实 |
| you will not be unable to afford | 删掉 not | Kindle 文件里也有 not，撤回。这个双重否定读作“仍然买得起另一样东西”也讲得通：比较富裕的人买东西时知道自己仍然买得起别的，所以不觉得花钱是损失。中文改为“是否意识到自己仍然买得起另一样东西” |
| 荷兰赌一条，句尾截断 | 按定义补全 | 按 Kindle 文件的原句改正 |
| 第 37 章 `distributio {i>dll-Being:` | 恢复为 distribution of emotional pain | Kindle 文件证实 |

### 编辑做的修复

- 第 20 章 `This “disposition effect” is discussed further.` 改为 `This “disposition effect” is discussed further in chapter 32.`。在 Kindle 文件里，“is discussed further”是一个链接，目标是 `part0039.xhtml#ch32`，也就是第 32 章；导入时去掉了链接，读者就不知道后面在哪里讨论。补上的 in chapter 32 就是这个链接的目标，中文译为“在第 32 章还会进一步讨论”。
- 撤回译者的 3 处修复，恢复为原文：`141–20`、`Institutionist`、`will not be unable`。理由是 Kindle 文件里也是这样写的，这些是原书本身的疑点；按这一章对其他原书错误的处理办法，引文照原文保留，统一列在下面。
- 按 Kindle 文件补全 Groopman 一条的引导语，改正荷兰赌一条的措辞（见上表）。
- 这些改动和译者的修复一样写在 `en/58-notes.md` 里。`tools/source_fixes.json` 目前只记录了引言的修复；以后如果从 EPUB 重新导入，这一章的修复需要重新应用。

### 保留未改的原文疑点

下面这些在导入的 EPUB、用户上传的另一份 EPUB 和 Kindle 文件里写法都一样，可见出在英文电子书本身，英文和中文的引文都照原文保留：

- `Science 15 (1967)`，应为 157。
- `Quarterly Journal of Economics 24 (2009)`（Malmendier 与 Tate，Superstar CEOs），应为 124。
- `Organizational Behavior and Human Decision Processes 66 (1966)`（Ritov），年份应为 1996。
- `American Journal of Psychology 13 (1944)`（Heider 与 Simmel），卷号应为 57。
- `Journal of Finance 42 (1992)`（Grinblatt 与 Titman），卷号应为 47。
- `Journal of Finance 55 (2002)`（Barber 与 Odean，Trading Is Hazardous to Your Wealth），年份应为 2000。
- `Quarterly Journal of Economics 116 (2006)`（Barber 与 Odean，Boys Will Be Boys），年份应为 2001。
- `Philosophical Transactions: Biological Sciences 351 (1996): 141–20`（Damasio），页码应为 `1413–20`。
- `A Social Institutionist Approach`（Haidt），论文标题是 Intuitionist。
- 引言注释里的 `Ease of Retrieval of Information`，第 12 章注释的简写和原论文都是 `as Information`。
- 人名拼写：`Richard Lucus`（Lucas）、`Ulrich Schmimmack`（Schimmack）、`Miles O. Bidwel`（Bidwell）。
- 第 30 章 `Slovic, Monahan, and MacGregor, “Violence Risk Assessment and Risk Communication.”` 是简写，全部注释里没有它的完整出处（大概是 Law and Human Behavior 24 (2000) 上的那篇论文）。
- 编辑另外注意到：结论注释里 Becker 与 Murphy 的刊名写作 `Journal of Political Economics`，实际是 Journal of Political Economy；第 32 章注释里 Thaler 的 `Journal of Economic Behavior and Organization 39 (1980): 36–90`，实际是 `1 (1980): 39–60`。没有逐条核对全部引文，可能还有别的。
- 正文里的疑点：第 13 章英国毒理学会一条说成本和收益“必然是负”相关，紧接着又说收益最大的方案成本最高，前后矛盾，中文照译并加了译者注；第 14 章汤姆·W 的计算写成 4 × .031 = 12.4，中文照译并用译者注说明不影响 11% 的结论；第 31 章的“较差的选项 BC”见双语审校一节。

这一节的内容还应当补进 `review/source.md`，由主会话处理。

## 1. 译者自检

- 执行者：翻译这一章的 agent（Opus 5.5），译者本人。
- 范围：全章 443 块；英文的 897 行先通读修复，再从上到下逐块翻译。
- 做法：
  - 每块的结构是“中文提示语：说明文字加英文引文”。英文引文由脚本从修复后的英文里原样拼接，说明文字和 Ibid.、see、cited by、Personal communication 这类连接词译成中文。
  - 英文提示语和中文提示语逐块对照，没有错位；用脚本比对了每块的数字，差异都是格式换算（月份、世纪、a dime 写成 10 美分、Ninety-four percent 写成 94%、小数前补 0）。
  - 逐段复核了较长的说明，检查否定、条件、量词和谁做了什么。
- 自检中修改：
  - “所以美国心理学会要求”改为“美国心理学会也要求”，原文的 and 没有因果关系。
  - 盖蒂青年雕像一条中，“鉴定”改为“察看”，原文是 view。
  - 天气与幸福感一条中，“切断了”改为“削弱了”，原文是 undermining。
  - 综合社会调查一条补上“似乎”，对应原文的 suggest。
  - 吉仁泽一条删掉英文引文末尾多出的句点；Dale T. Miller 一条重排语序并补上空格；“概率(蓝色)”的半角括号改为全角；“确定的数额”改为术语表里的“确定的事”。
  - 提示语对齐了引言、第 1 章至第 3 章的现有译文；为了和第 2 章一致，“被试”全部改为“受试者”。
- 译者注：加了 4 条，两条说明英文注释只有提示语，一条解释 prime 原指给水泵引水，一条说明汤姆·W 计算里 12.4 的写法。
- 格式：中文正文没有破折号；全角标点和中西文之间的空格用脚本检查过。

## 2. 双语审校

- 执行者：另一个独立上下文的 agent（Opus 5.5），没有参与翻译。
- 范围：全章 443 块，逐块对照英文，并对照已译各章核对提示语和术语。
- 发现：22 条。编辑逐条对照英文和各章译文核实，21 条成立并修改（其中 2 条只采纳了一部分），1 条不成立。主要几类：
  - **意思**：第 31 章正文已把写反的 BC 改按 AD 翻译，注释仍写“较差的选项 BC”，读者对不上。处理：提示语保留原文的 BC，加译者注说明按上下文应为 AD，和第 31 章的译者注一致。
  - **术语**：提示语和书中术语与已译各章不一致，例如“轻松”改为“放松”（与认知放松一致）、“狂妄假说”改为“自大假说”、“不理性”改为“非理性”、“阿拉”改为“阿拉尔”、“补事件”改为“对立面”、“任务设定”改为“任务定势”、“盖洛普-Healthways 幸福指数”改为“盖洛普-健康之路幸福指数”，并在括号里附上英文全名。
  - **提示语与正文不一致**：按各章现有译文改了 11 条提示语，例如“摇着理性的狗”“例子想起来的容易程度”“以往的研究……个人的情绪反应”“对自己近来的整体生活有多满意”“希望战胜了经验”“毁灭价值的兼并”“做选择时的情境”“如果他们……手握权力”“宁要名牌，不要无品牌的普通商品”“反复接触带来的后果……心理稳定和社会稳定”“按要求做好记录”。
  - **表达**：漏译的 Also 译为“另见”；穷人一条的比较对象改为“比境况较好的人的行为”；雕像指甲一条消除歧义；insider view 和 outsider view 改为成对的“局内人视角”“局外人视角”；后代一条的时间状语移到“后代”之后；汽车一条的长定语改短。
  - **原文**：处置效应一条按 Kindle 文件里的链接目标补上第 32 章；原书引文的卷号和年份错误照原文保留，列在上面的原文疑点里。
- 不成立或只采纳一部分的：
  - “每人不限购”改为“每人不限量”：不成立。第 11 章正文写的就是“每人不限购”，和注释一致。
  - 提示语一批中的 The Far Side 改为“漫画《远方》（The Far Side）”：不成立。第 4 章正文写作“加里·拉森的漫画 The Far Side”，没有用《远方》，注释的“The Far Side 漫画”与它一致，保留。
  - 同一批中的“必要的记录保存”：采纳，改为“按要求做好记录”。审校者建议的写法带“没有”，对应正文的 failures to，这几个词在英文提示语的引号之外。
  - 引言注释的 “Ease of Retrieval of Information”：审校者建议可以按第 12 章注释统一为 as Information。三份电子书文件都写作 of，属于原书疑点，照原文保留并记录。
- 审校者的总体判断：整体质量较高，逐块对应、章标题、人名、标点和空格都符合规则，引文前后的说明文字译得准确，数字和计算逐一核对无误；主要问题在提示语和已译正文的说法不一致。

## 3. 中文通读

- 执行者：编辑 agent（Opus 5.5），写这份记录的就是它，没有参与翻译和双语审校。
- 范围：只读中文，从头读到尾；改动处都回查了英文。另外用脚本把每条提示语和所属章节的中文正文比对了一遍。
- 发现并修改：
  - 诺贝尔奖一条，“不满意增设一个……诺贝尔奖”改为“对增设一个……诺贝尔奖感到不满”。
  - 茨威格一条，“数千万美元的薪酬，被颁给了一些‘个人’成就，而这些成就主要是由……造成的”改为“奖励的是一些‘个人’成就，而这些成就主要来自……”。
  - 第 11 章提示语“‘合理的’音量”改为正文的“‘合理’的音量”。
  - 结论一条里混进来的 Nudge 提示语，“助推”改为书名《助推》，和结论一章一致。
  - 第 13 章英国毒理学会一条加译者注：后半句说收益越大的方案成本越高，这通常叫作正相关，原文却写“负的”。
  - 引言和第 19 章两条只有提示语的注释，译者注补充说明：在英文电子版里，这两句提示语分别链接到第 9 章 回答一个更容易的问题、第 7 章 急于下结论的机器（光环效应在那一章讨论）。
  - 跟随英文改动调整中文：Groopman 一条补上“怀疑循证医学的一个例子，见”；“仍然买得起另一样东西”；荷兰赌一条改为“最终注定让你亏损”；Damasio 和 Haidt 的引文恢复原文。
  - 译者注按出现顺序重新编号为 t1 到 t6。
- 没有改的：
  - 中文小数补前导零（0.66、r = 0.84）：第 17 章、第 20 章和两篇附录等已译章节都这样写，保持一致。
  - 英文引文里自带的破折号（`Journal of Experimental Psychology—General`，`Three Cheers—Psychological, Theoretical, Empirical—for Loss Aversion`）：引文保留英文原样，规则限制的是中文句子，保留。
  - Jing Xu：不知道原名的汉字，保留拉丁字母。
  - 结论注释里 accept future addiction 和 Nudge 两条合在一段：Kindle 文件里也是一段，而且 Nudge 不像别的提示语那样用斜体，所以保持一块。
- 还剩的：按脚本比对，有 133 条提示语在所属章节的中文里找不到完全相同的字句。这些大多是没有引号的短语，意思和正文一致，只是措辞不同；带引号的引语里，和正文字句不同的只剩 4 条，都是有意保留的：保留英文加释义的 finds he it yellow instantly、两个词各带引号的“放松”与“紧张”，以及意译的“‘风险’并不存在”“生前的诊断”。各章还在修改，定稿时建议再用脚本比对一遍。

## 4. 阅读器校样

待主会话在阅读器里校样。

## 状态

前三项已完成，没有未解决的意义问题；原书本身的疑点照原文保留，已在上面列出。四项审校要等主会话在阅读器里校样之后才算全部完成；`book.json` 里的状态由主会话在校样之后修改。

## 第二轮：对照干净原文与术语统一

- 执行者：agent（Opus 5.5）。
- 干净原文：用户提供的同一版本的 AZW3 文件，解开后的注释全文。文件开头的 25 条是附录 A 的注释，属于附录 A 那一节，这里没有比较。
- 范围和做法：比较脚本有 436 块没能对上，所以全节重新逐块比较。两边的英文都按空行切成块，忽略引号样式、斜体、链接地址和空白，再逐词比较。两边都是 443 块，一一对应；有差异的块共 12 个。

### 英文的改动

| 原文 | 改为 | 中文是否更新 |
| --- | --- | --- |
| `This “disposition effect” is discussed further in chapter 32.` | `This “disposition effect” is discussed further.` | 已更新：正文改为“这种‘处置效应’后面还会进一步讨论”，加译者注 t6，说明英文电子版里 is discussed further 是一个链接，指向第 32 章 记分；原来的 t6（较差的选项 BC）顺延为 t7 |
| `Alexander Rothman` | `Alexander Rotliman` | 已更新：中文里的英文引文同样改为 Rotliman |

- 处置效应一条：in chapter 32 是第一轮编辑按链接目标补进英文的，干净原文里没有这几个词。这一轮英文恢复原文的措辞，链接指向哪一章改由译者注说明，读者仍然能找到第 32 章。
- Rotliman：第一轮把它当作文字识别错误，保留了修复。干净原文也写作 Rotliman，这一轮按原文恢复，和 Lucus、Schmimmack、Bidwel 这几个人名拼写的处理办法一致，英文和中文的引文都照原文。正确的拼写是 Rothman（Alexander J. Rothman），补入上面的原文疑点。

### 忽略的排版差异

共 12 处，分布在 10 块里，英文保持现状：

- `Mc Glone`（McGlone）、`Shortand`（Short- and）、`Mean-while`（Meanwhile）、`Stalk-fleet`（Stalkfleet）：干净原文里断词或丢了连字符。
- `4, 000`、`.03/. 97`、`. 031`、`112. 4`、`1. 706`、`1. 5`：干净原文的数字里多了空格，共 6 处。
- `v (1–r2)`：干净原文丢了根号和上标，我们写作 `√(1–r²)`。
- `95–96 sentence was literally true`：句首的 `95–96` 是纸质版注释按页码分组时留下的页码，我们的英文不带页码。

### 术语

- 任务文件标出 151 条，统一 3 条，保留 148 条。
- 统一的 3 条：
  - 第 3 章“optimal experience”的提示语，“最优体验”改为术语表的“最佳体验”，和第 3 章正文这一轮的改法一致。
  - 第 33 章“reversals of judgment and choice”的提示语，“判断和选择的逆转”改为“判断与选择的逆转”，和第 33 章正文的“判断与选择逆转”一致。
  - 第 32 章“loss averse for aspects of your life”的提示语，“对生活的某些方面更厌恶损失”改为“对于生活的某些方面，损失厌恶更强”，用术语表的“损失厌恶”，也和第 32 章正文的“你的损失厌恶可能更强”对得上。
- 保留的 148 条：
  - 147 条里，这个词只出现在保留英文的引文中，例如论文和书的标题、刊名（Journal of Behavioral Decision Making、Heuristics and Biases、Choices, Values, and Frames 等）和作者名（Amos Tversky 15 条），中文照英文原样保留。
  - 1 条是第 24 章 eBay 一条里的 prime time，意思是“黄金时段”，和启动效应无关。
- 另外用第二批术语逐条扫描了全节的英文和中文，除上面的“最佳体验”以外，没有发现其他译法不一致的地方。

### 结果

- `python3 scripts/site.py status thinking-fast-and-slow` 显示 notes 一行为 443/443，全部已译。
- 译者注现在共 7 条，按出现顺序编号为 t1 到 t7，引用和定义一一对应。
