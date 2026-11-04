# 附录 A 不确定条件下的判断：启发式与偏差（appendix-a-judgment-under）审校记录

全章 73 个块，中英逐块对应（`site.py status` 显示 73/73），25 条参考文献脚注全部译出（25/25），另有 1 条译者注 `[^t1]`。下文的块号按 `status` 的顺序数：第 1 块是一级标题，第 2 块是作者署名，第 3 块是出处说明。

## 原文修复

EPUB 里这一节的乱码比其他章节多，译者按上下文修复后再翻译，并把修复后的全文和 1974 年 Science 上的原文（斯坦福大学的公开 PDF）逐字比对过。编辑没有再改英文。

乱码和排版残留，共 24 处：

1. `Additional support for this research wass r"0%" wid provided by` 改为 `Additional support for this research was provided by`
2. `seen less sharply than Vt pofreak/>stimated when visibility is good` 改为 `seen less sharply than nearer objects. However, the reliance on this rule leads to systematic errors in the estimation of distance. Specifically, distances are often overestimated when visibility is poor because the contours of objects are blurred. On the other hand, distances are often underestimated when visibility is good`（这里乱码吞掉了两句半，按 1974 年原文补回）
3. `rather than to a lawy [hanerser. In one` 改为 `rather than to a lawyer. In one`
4. `should be (.7/.3)2, or 5.44` 改为 `should be (.7/.3)², or 5.44`
5. `in a random sample often men will be` 改为 `in a random sample of ten men will be`
6. `A certain town is s [ainquote wierved by two hospitals.` 改为 `A certain town is served by two hospitals.`
7. `the sequence H-H-H-T- [enc. IT-T, which` 改为 `the sequence H-H-H-T-T-T, which`
8. `In one o [pand tf these studies,` 改为 `In one of these studies,`
9. `Mo [r vs tre generally, consider` 改为 `More generally, consider`
10. `recalling such occurrences a [occpunishmentmong one’s acquaintances` 改为 `recalling such occurrences among one’s acquaintances`
11. `committees of k members, 2 = k= 8.` 改为 `committees of k members, 2 ≤ k ≤ 8.`
12. `overestimated the frequency of [ frpici co-occurrence of` 改为 `overestimated the frequency of co-occurrence of`
13. `Two groups of high school student [choult os estimated,` 改为 `Two groups of high school students estimated,`
14. `10% red marbles and 9% white marbles` 改为 `10% red marbles and 90% white marbles`
15. `to overestimate the pr [timrall obability of conjunctive` 改为 `to overestimate the probability of conjunctive`
16. `if exactly ![](images/00019.jpg)% of the true values` 改为 `if exactly Π% of the true values`
17. `below his stated values of X![](images/00019.jpg).` 改为 `below his stated values of XΠ.`
18. `either smaller than X0l or greater` 改为 `either smaller than X01 or greater`
19. `A similar anchoring [lariciently effect will occur` 改为 `A similar anchoring effect will occur`
20. `training in statistics. [ticor pri[^23] Although` 改为 `training in statistics.[^23] Although`
21. `not entirely satisfactory [ saf sub, because` 改为 `not entirely satisfactory, because`
22. 注释 6 末尾 `(New York: Wiley, 1968), 17–52. [t="orm` 改为 `(New York: Wiley, 1968), 17–52.`
23. 注释 20 `Confirmation of the Inertial-? Effect` 改为 `Confirmation of the Inertial-ψ Effect`
24. 注释 21 `[^21]: M. Alpe [spa Acta Psychologica 35 (1971): 478–94;` 改为 `[^21]: M. Alpert and H. Raiffa, unpublished manuscript; C. A. S. von Holstein, “Two Techniques for Assessment of Subjective Probability Distributions: An Experimental Study,” Acta Psychologica 35 (1971): 478–94;`

导入遗留的链接，共 15 处：正文里引用参考文献 1 到 15 的 `[n](#filepos…)` 链接（例如 `[1](#filepos1138148)`）改成脚注标记 `[^n]`。

拿不准的修复，编辑的处理如下：

1. **注释 21**：没有找到 2011 年英文版的原文措辞。译者依据 1974 年文章的第 11 条参考文献（“M. Alpert and H. Raiffa, unpublished manuscript; C. A. S. von Holstein, Acta Psychol. 35, 478 (1971)”），按本书其他注释的格式重写，并从期刊补上了 von Holstein 那篇的标题。编辑查到这篇论文的期刊记录：作者署名是 Carl-Axel S. Staël von Holstein，标题是 “Two techniques for assessment of subjective probability distributions: An experimental study”，Acta Psychologica 第 35 卷，478 到 494 页，和修复后的标题、卷号、页码一致。书里可能写出 Alpert 和 Raiffa 那篇的标题（“A Progress Report on the Training of Probability Assessors”），姓名也可能写成 “Staël von Holstein”。这些还要对照纸质书确认，暂时保留译者的写法。
2. **注释 20 的 ψ**：字母可以确定是 psi，大小写看不出来。其他文献引用这篇论文时多用小写，暂时保留小写 ψ。
3. **两处 Π**：修复后不再引用 `images/00019.jpg`（一张 25×13 像素的 “Π%” 小图），这张图片现在没有用到。编辑同意用字符 Π 代替图片：两处都换成字符，第一处是 Π%，第二处是 XΠ，写法一致；只删第一处多出的 %，第二处会变成 XΠ%。图片文件是否删除，由主会话决定。
4. **(.7/.3)²**：丢失的是上标，严格说不算乱码。5.44 正好是 (7/3)² 的值，编辑同意这样修复。
5. **15 处链接**：这是 `tools/curate_source.py` 的遗漏，EPUB 本身没有乱码。以后重新运行整理脚本，这些链接还会回来，除非脚本里的正则也匹配同一文件内的 `#filepos` 链接，或者把这些修复记进 `tools/source_fixes.json`。

双语审校指出、这一节暂时没有修复的三类源文问题：

1. **二项式系数 (10/k)**（第 42 块）：原书是上下堆叠的“10 选 k”，EPUB 里压平成了 `(10/k)`，看起来像除法；`k= 5` 也少一个空格。EPUB 里就是这样，导入没有出错。中文写成“二项式系数 C(10, k)”，意思正确，不需要改。英文保持原样。
2. **丢失的下标**（第 58 到 63 块）：EPUB 里 X<sub>90</sub>、X<sub>01</sub>、X<sub>99</sub>、X<sub>10</sub> 和 X<sub>Π</sub> 都是下标，导入后变成 X90、X01 这样的普通文字，中文照搬了英文。Unicode 里没有下标的 Π，改用 Unicode 下标数字会让 XΠ 一处写法不同；改用 HTML 的 `<sub>` 标签，阅读器能渲染，但全书英文里还没有用过行内 HTML。这是全书的格式问题，编辑没有改，留给主会话决定。
3. **丢失的段首斜体小标题**（第 9、13、25、27、30、32、38、40、42、45、50、56、58 块）：EPUB 里这些段首短语（如 “Insensitivity to prior probability of outcomes.”）是斜体，导入时去掉了，读起来像一个没有主语的句子开头。全书导入都去掉了行内斜体，要不要恢复由主会话统一决定；如果恢复英文斜体，中文同步标出，例如 `*对结果的先验概率不敏感*。`

上面的修复都还没有记进 `tools/source_fixes.json`，三类没有修复的问题也还没有记进 `review/source.md`，需要主会话补上。

## 1. 译者自检

- 执行者：负责翻译这一节的 agent（Opus 5.5），译者本人。
- 修复英文：修复后把全文和 1974 年 Science 原文逐字比对。剩下的差别只有 PDF 识别时产生的乱字，以及 2011 年版自己改的两处：删掉了 “(180 centimeters)”，“50-50 chances” 改成了 “a 50–50 chance”。据此判断，英文里的乱码都已找到并修好。
- 范围：译完后逐段对照英文，检查漏译、增译、否定、条件、数量、施动者和术语，并用脚本核对了每一块的脚注标记和数字。查出的不一致都在预料之中，原因有三种：概率写法从 .7 改成了 0.7；英文拼写的 ten 写成了 10；有几处把 X10、50% 再说了一遍，意思没变。
- 自检中改了四处措辞：
  1. “对证据影响的低估”改为“研究者一再观察到人们低估证据的影响”。
  2. business venture 改译为“商业项目”。
  3. k 人委员会和 (10 − k) 个非成员的对应关系，换了一种更顺的说法。
  4. not equipped to cope 改为“没有准备好应对”。
- 格式处理：概率一律写成 0.x；减号用 −；抛硬币的 H 和 T 加了译者注 `[^t1]`；r、road、car、thought、love、door、water 这些英文单词保留原文；二项式系数写成 C(10, k)。
- 运行 `site.py status`，本节 73/73 块、25/25 条注释都已翻译。在内存里调用 `book.compile_chapter` 编译这一对文件，没有报错。没有修改 `book.json`、`glossary.md` 或其他文件，临时目录 `/tmp/appA` 已经删掉。
- 留给编辑的问题有 6 条，编辑的处理如下：
  1. **二项式系数**：同意写成 C(10, k)。这是中文教材里组合数的常见写法，读者不会看成除法，不需要另加译者注。
  2. **查普曼夫妇**：同意。Loren J. Chapman 和 Jean P. Chapman 是夫妻，注释 17 的两篇论文都是两人合写，“夫妇”说的是事实，读起来也比“查普曼和查普曼”自然。
  3. **Ibid. 写成“同上”**：同意。书末注释一节（`58-notes.md`）也把 Ibid. 写成“同上”，其余引文保留英文，两处做法一致。
  4. **作者署名和出处说明保留斜体**：附录 B 的署名和出处说明也是斜体，两篇附录一致，编辑没有改。中文斜体在阅读器里会显示成倾斜的字形，好不好看要在阅读器校样时看真实页面，留给主会话决定。
  5. **“(180 centimeters)”**：同意不补。EPUB 里这一处没有乱码标记，应该是 2011 年版自己删掉的，译文按本书的英文翻译。
  6. **概率写成 0.7**：同意。第 17、18、19、25 章和附录 B 都写成 0.x，这一节和它们一致。

## 2. 双语审校

- 执行者：另一个独立上下文的 agent（Opus 5.5），没有参与翻译；只读审校，没有改动文件。
- 范围：全节 73 块和 25 条注释，逐块对照原文；同时核对了数字、实验逻辑、概率计算、人名、章节标题、术语表、标点和中西文之间的空格。
- 审校者的总体判断：译文准确完整，没有漏译，也没有改动否定和条件；需要处理的是两处术语不统一和两处小的意义偏差，另有十来处表达可以更顺。
- 发现：19 条。其中意义 2 条，术语 3 条，表达 11 条，源文 3 条。编辑 agent（Opus 5.5）逐条对照英文核实，19 条都成立，全部采纳：16 条修改了中文，其中 2 条调整了措辞；3 条源文问题没有改动正文，记在本文“原文修复”一节。
  - **意义**：
    - 第 69 块：in the sense that 原译“之所以是主观的，是因为”，把解释词义的说法译成了因果。改为“说推导出的概率是主观的，意思是允许不同的人对同一事件给出不同的概率”。
    - 第 69 块：has implications for 原译“有重要意义”，多出了“重要”，两个“对”连用也拗口。改为“对认知偏差的实证分析，关系到判断出的概率在理论和应用中所起的作用”。
  - **术语**：
    - 贝叶斯推断里的 odds：书末注释一节写作“几率”（后验几率 = 先验几率 × 似然比），这一节原来写作“赔率”。第 9 块和第 24 块的贝叶斯语境统一改为“几率”，共 6 处。编辑在第 9 块第一次出现时加了括注“几率（两者的概率之比）”，因为“几率”在日常中文里常指可能性，括注说明它在这里是两个概率之比，和书末注释的解释一致。第 4 块“以数字形式表达……比如赔率”、第 23 块“两人各自应该给出多大的赔率”、第 58 块“9 比 1 的赔率”、第 62 和 63 块的“均等赔率”和“赔率中位数”是下注语境，保留“赔率”。
    - sample size：第 7 章和第 10 章都写作“样本量”，这一节原来大多写作“样本大小”。第 13、22、24、67 块统一改为“样本量”；第 13 块的 samples of various sizes 原译“不同大小的样本”，编辑改为“不同规模样本”，没有生硬地套用“样本量”。
    - 第 3 块：期刊名按全书规则保留英文，“本文原载于《科学》第 185 卷”改为“本文原载于 Science 第 185 卷”，和附录 B 的“原载 American Psychologist 第 34 卷”一致。
  - **表达**：
    - 第 29 块：remote criterion 原译“遥远标准”，改为“远期指标（5 年后当教师是否成功）”；“相对于一个指定的群体”照英文语序插在动词前，改为“以某个指定群体为参照，用百分位分数评价”。
    - 第 31 块：两个很长的前置定语夹在比较句里。按建议拆成两句，编辑把第二句调整为“预测前者最终的平均绩点时，人们比预测后者时更有信心”，让“人们”出现在比较之前。
    - 第 32 块：“从在”两个介词叠用、“就会发现……会好一些”两个“会”重复，按建议改写。
    - 第 34 块：“不认识回归的重要性”改为“认识不到回归的意义”。
    - 第 38 块：“名人更有名的那个类别”语义重复，改为“名单上人物更有名的那个类别（性别）”。
    - 第 56、57 块：“对……评估中的偏差”结构不通，改为“评估合取事件和析取事件时的偏差”“评估复合事件时出现的偏差”。
    - 第 62 块：they suggest different modes of adjustment 原译“暗示了……进行调整”，看不出谁在调整，改为“这两种程序会引导人从不同的锚出发，以不同的方式调整”。
    - 第 47、67 块：“终身的经验”改为“一生的经验”。
    - 第 68 块：“可以想象，一个人可以”两个“可以”紧挨着，改为“可以设想，一个人只要统计……就能知道……”。
    - 第 73 块：development 原译“某种发展”，改为“某种事态发展”。
  - **源文**：二项式系数 (10/k)、丢失的下标、丢失的段首斜体小标题，三条都成立，处理见“原文修复”一节。
- 驳回：无。

## 3. 中文通读

- 执行者：编辑 agent（Opus 5.5），采纳审校意见后只读中文，从头读到尾。
- 发现并修改 11 处，每处都回查了原文：
  1. 第 8 块：“不受几个本应影响概率判断的因素的影响”里“影响”出现两次，改为“因为有几个因素本应影响概率判断，相似性（也就是代表性）却不受它们影响”。
  2. 第 9 块：“这些描述所取自的群体由……组成”是照英文从句写的，改为“这些描述取自一个由 70 名工程师和 30 名律师组成的群体”。
  3. 第 9 块：“几率”第一次出现时加括注“（两者的概率之比）”，理由见第 2 节术语部分。
  4. 第 29 块：前面写“实习课”，后面写“试讲课”，读者会以为是两种课。英文 practice lesson 和 trial lesson 指的是同一堂课，统一为“实习课”；a single 写成“仅凭……一堂”。
  5. 第 30 块：“一再有研究证明……这充分证明了”两个“证明”重复，后一个改为“说明”，对应 amply attests。
  6. 第 31 块：“相关统计中的一个基本结论”容易读成“有关的统计”，改为“相关分析中的一个基本结论”，对应 the statistics of correlation。
  7. 第 34 块：“由于教官们在学员着陆好时表扬他们……他们便得出了”里的“他们”分不清指教官还是学员，改为“教官们在学员着陆好时表扬，在着陆差时训斥，因此得出了……”。
  8. 第 38 块：elementary demonstration 原译“一个基础实验”，容易理解成基础研究，改为“一个简单实验”。
  9. 第 43 块：“很容易看出，构造……很容易”两个“容易”重复，前一个改为“一眼就能看出”，对应 readily sees。
  10. 第 58 块：段首短语“主观概率分布评估中的锚定”改为“评估主观概率分布时的锚定”，和第 56、57 块改过的说法一致。
  11. 第 13 块：samples of various sizes 写成“不同规模样本”（见第 2 节术语部分）。
- 全节检查过没有破折号、半角标点和直引号，中文和数字、拉丁字母之间都有空格。
- 通读后运行 `status`，本节一行显示 73/73、25/25。编辑在内存里调用了 `book.compile_chapter`，全节能正常编译，译者注 `[^t1]` 有定义、有引用；没有构建站点，也没有启动服务器。

## 4. 阅读器校样

待主会话在阅读器里校样。需要特别看一下：第 2、3 块中文斜体的显示效果；第 14 到 19 块医院问题的 6 个引用块和第 52、54 块的两个乘法算式；25 条参考文献脚注和译者注 `[^t1]` 的弹窗；第 59 块的 Π 和注释 20 的 ψ 能否正常显示。

## 状态

译者自检、双语审校和中文通读已经完成，没有未解决的意义问题；四项审校要等主会话做完阅读器校样才算全部完成。`book.json` 里这一节的状态仍是 `todo`，由主会话修改。另外还有几件事需要主会话处理：

1. 把上面 24 处乱码修复和 15 处链接修复记进 `tools/source_fixes.json`，或者补上 `curate_source.py` 对同一文件内 `#filepos` 链接的处理。
2. 在 `review/source.md` 里记下二项式系数 (10/k)、丢失的下标和丢失的段首斜体三类问题，并决定下标和段首斜体要不要在全书恢复。
3. 决定 `images/00019.jpg` 是否删除。
4. 对照纸质书确认注释 21 的措辞和注释 20 里 ψ 的大小写。
5. 建议在术语表里补两条：odds 在贝叶斯语境写“几率”、在下注语境写“赔率”；sample size 写“样本量”。
