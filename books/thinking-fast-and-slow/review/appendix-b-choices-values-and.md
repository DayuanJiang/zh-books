# 附录 B 选择、价值与框架（appendix-b-choices-values-and）审校记录

全章 126 个块，中英逐块对应（`site.py status` 显示 126/126）。另有 2 张图片只在英文文件里。没有原书脚注，译者注 4 条。下文的块号按 `status` 的顺序数。

## 原文修复

EPUB 里这一节有 14 处乱码或断文，译者修复后再翻译。修复依据是上下文，以及 1984 年 American Psychologist 刊出的原文：

1. `The paradigmatic example of decision un ^v>`（第 6 块）：EPUB 在这里断掉，后面四句话都丢了。译者按期刊原文补成 `The paradigmatic example of decision under risk is the acceptability of a gamble that yields monetary outcomes with specified probabilities. A typical riskless decision concerns the acceptability of a transaction in which a good or a service is exchanged for money or labor. In the first part of this article we present an analysis of the cognitive and psychophysical factors that determine the value of risky prospects. In the second part we extend this analysis to transactions and trades.`
2. `or to Wn indispan> – $20` 改为 `or to W – $20`
3. `that should g ctha211;$850)overn the preferences` 改为 `that should govern the preferences`
4. `The same cd Cce f pattern of results` 改为 `The same pattern of results`
5. `(when the chance of winning is nil cinntric. We) and one` 改为 `(when the chance of winning is nil) and one`
6. `one chan ce i toce in four` 改为 `one chance in four`
7. `a hypotheti ct arnative cal vaccine` 改为 `a hypothetical vaccine`
8. `sets up a men cset optiotal account` 改为 `sets up a mental account`
9. `This finding cThinchsupports the notion` 改为 `This finding supports the notion`
10. `problems apparent clemosition ly enabled` 改为 `problems apparently enabled`
11. `(S2, T2), and c2< that most subjects` 改为 `(S2, T2), and that most subjects`
12. `offer objecti coffler problevely identical options` 改为 `offer objectively identical options`
13. `complicates the relati ces maker won between` 改为 `complicates the relation between`
14. `and A. Tver c, aistsky.` 改为 `and A. Tversky.`

编辑根据双语审校的意见，又补了 2 处丢失的连字符：

15. 第 65 块：`the mortality survival statistics` 改为 `the mortality-survival statistics`。期刊原文有连字符，中文不用改。
16. 第 121 块（参考文献）：`InformationProcessing Effects` 改为 `Information-Processing Effects`。这个词是行末断字时丢了连字符，中英两个文件都改了。

拿不准的修复：

- 第 1 条：只看 EPUB 无法确定丢掉的原文。编辑把补上的四句和期刊原文 PDF 的文字逐词比对过，完全一致。期刊版和书中附录在别处有几处小的编辑差异（例如书里删掉了 “(see Figure 2)”，把 “in press” 改成了具体年份），所以纸书这一段也可能和期刊略有不同。如果方便，建议拿纸书核对一下。
- 第 15 条：期刊原文有连字符，但没有核对纸书。书里有的连字符确实被编辑改掉了（例如 Adaptation-level 写成了 Adaptation Level），所以纸书这里也可能没有连字符。补上连字符不改变意思。

原书本身的问题，英文保持原样：

- 第 3 块：出处说明写作 “vol. 34, 1984”。这篇文章实际刊登在 American Psychologist 第 39 卷第 4 期（1984 年 4 月），第 341 到 350 页，期刊 PDF 首页印着 “Vol. 39, No. 4, 341-350”。EPUB 写的也是 34，所以这是原书的错误。中文照原书写“第 34 卷”，另加译者注 t4 说明正确的卷期。
- 第 96 块：`the correspondence of decision values between experience values` 语法不通，应为 between decision values and experience values。期刊原文和 EPUB 都是这样写的，中文按作者的本意译出。
- 第 104 块（参考文献）：条目拼作 `Erakar`，正文第 14 块引作 `Eraker and Sox 1981`，作者的正确拼法是 Stephen E. Eraker。期刊原文的参考文献里就拼成了 Erakar。中文照抄条目，没有改。
- 第 59 块：`an 85% chance to win $45`，前文问题 5 用的是 80%。期刊原文也是 85%。这句话报告的是一个实验结果，无法确认是印错，所以没有加译者注。

以上第 15、16 条修复和译者的 14 条修复，还没有记进 `tools/source_fixes.json`；上面列出的原书问题也还没有记进 `review/source.md`。这两个文件需要主会话补上。

## 1. 译者自检

- 执行者：负责翻译这一节的 agent（Opus 5.5），译者本人。
- 英文部分：译者把修复后的附录 B 和 1984 年 American Psychologist 刊出的原文逐词比对过，原文 PDF 是用 pypdf 提取的。剩下的差异只有三类：一是排版产生的杂字；二是书中有意做的编辑，例如删掉了 (see Figure 2)，把 in press 改成年份；三是原刊本身的错字。英文里共修复 14 处，其中 13 处是乱码，1 处是断文，没有漏掉的。
- 中文部分：译者逐段对照了漏译、增译、否定、条件、量词、比较对象、谁做了什么和术语，并改了以下几处：
  1. “两个问题的回答之间的差别耐人寻味”：初稿写成“差别很大”，多加了程度，已改回原文的意思。
  2. 摘要里“相对于中等概率的事件”：初稿语序容易误读，已调整。
  3. 伯努利那一句：初稿的“这些结果”指代不清，已改明确。
  4. 商科学生那条告诫和“标准表征”之间的因果关系：已改得更清楚。
  5. 保险风险那一句（“有 25% 的可能损失 200 美元”）：初稿不通顺，已改写。
  6. “还取决于一个关键因素”：初稿有翻译腔，已改写。
  7. 莫里哀译者注里“说了四十多年”：已改成和剧本一致。
- 译者还用脚本把每对中英段落里的数字逐一比对过，剩下的差异只有三种：英文里粘在数字后面的逗号，中文补出的“8 月”，以及为了说清楚而重复的数字，数字本身都对得上。中文里没有破折号，也没有强行对比的句式。
- 格式：负数和 W − 20 用数学减号 −。参考文献原样照抄，只有原书用“———”表示“作者同上”的两条，译者改成重复写出作者名（Kahneman, D., and A. Tversky. 1982；Thaler, R. 1985），这样中文文件里不会出现破折号。
- 译者注加了三条：t1 解释“像说散文一样”出自莫里哀《贵人迷》；t2 和 t3 翻译图 1、图 2 坐标轴上的英文。
- 运行 `python3 scripts/site.py status thinking-fast-and-slow`，这一节显示 126/126。译者还用 framework 的 `compile_chapter` 在内存里把这一节编译了一遍，没有报错，三条译者注都能识别。译者为这个任务在 /tmp 下建的临时目录都已删除。`book.json` 里的状态仍是 todo，没有改。
- 留给编辑的问题有 7 条，编辑的处理如下：
  1. 出处说明的卷号：原书写 vol. 34，实际是第 39 卷第 4 期。其他章节遇到确认的原书错误时都加了译者注（第 29 章的“表 13”，第 30 章的 999,999，第 31 章的 AD 和 BC），这里照同样的做法，加了译者注 t4，正文仍照原书写“第 34 卷”。
  2. 第 59 块的 85%：保留，不加译者注（理由见上面“原书本身的问题”）。
  3. 参考文献里的“———”：保留译者的处理，重复写出作者名。条目包含的信息和英文相同，中文文件里也就没有破折号。
  4. 参考文献页码范围里的短横（如 23–36）和 von Neumann–Morgenstern 里的短横：保留。它们属于原样照抄的英文引文，附录 A 和书末注释也是这样处理的。
  5. 人名：Kunreuther 改为“昆鲁斯”，和第 13 章的“霍华德·昆鲁斯”一致。斯洛维奇、菲施霍夫、利希滕斯坦、塞勒、萨维奇、冯·诺伊曼、摩根斯坦都和其他章节一致。麦克尼尔、波克、索克斯、休梅克、赫尔希、布里克曼在其他章节的中文正文里没有出现（书末注释里只出现在英文引文中），不存在统一的问题。
  6. 第 65 块的 mortality survival：英文按期刊原文补上了连字符（见“原文修复”第 15 条），中文“死亡率和存活率的统计数据”不用改。
  7. positive domain：“正向领域”读者不容易看懂。这一句承接上文的保险例子，上文的选项全是损失，下面的问题 10 和问题 11 都有赢钱的机会，所以改写为“在有机会赢钱的情形中，我们也观察到了类似的效应”（见第 3 节第 6 条）。

## 2. 双语审校

- 执行者：另一个独立上下文的 agent（Opus 5.5），没有参与翻译。
- 范围：全节 126 块，逐块对照原文；同时核对了块对齐、标题、三条译者注和图中英文、所有数字、百分比、样本量和实验逻辑（问题 1 到 11 的选项与比例、问题 3 和问题 4 的占优推导、问题 5 和问题 6 的概率换算）、标点和空格。
- 审校者的总体判断：译文整体质量很好，可以进入审校状态；需要改的主要是几处表达和两处术语，另有两处意思略有偏差，五处源文问题。
- 发现：17 条。编辑 agent（Opus 5.5）逐条对照英文核实，必要时查了 1984 年期刊原文 PDF 和 EPUB，17 条都成立，全部采纳，其中几条调整了措辞。驳回：无。
  - **意思**（2 条）：
    - 第 49 块：contribute to 说的是“起一部分作用”，原译“既让彩票有吸引力，也让保险有吸引力”把它说成了全部原因。改为“彩票和保险之所以都有吸引力，决策权重的这些特点是原因之一”。审校者建议的“都起了一部分作用”读着有些别扭，编辑换了说法。
    - 第 98 块：anticipates 是预料、预期，原译“预示”是征兆的意思。按建议改为“不仅是对体验的预期，还会塑造体验”。
  - **术语**（2 条）：
    - 第 89 块：Kunreuther 原译“昆罗伊特”，改为第 13 章用过的“昆鲁斯”。
    - 第 97 块：aspiration 和后面的 expectations 原来都译成“期望”，中文读者会以为是同一个概念。aspiration level 在心理学里通译“抱负水平”，第 38 章也把 aspirations 译作“抱负”，改为“适应水平或抱负水平”。
  - **表达**（7 条）：
    - 第 26 块：“按这种方式评估选项的人，预期会……”容易读成这些人自己预期，英文是作者在预测。按建议改为“可以预料，按这种方式评估选项的人会……”。
    - 第 27 块：sophisticated 和 naive respondents 指受过训练和没受过训练的人，原译“老练”“天真”像在说性格。附录 A 把同样的说法译作“外行还是内行”，改为“无论受访者是内行还是外行，它都同样常见”。
    - 第 58 块：“报酬是真实的金钱和假设的金钱时”像是说报酬同时是真钱又是假设的钱。编辑把几种条件分开写：“报酬用真钱时和用假设的钱时都是如此（……），结果换成人命时，以及不分阶段地呈现随机过程时，也是如此”。
    - 第 61 块：exclusive 指两种病毒株是互斥的情况，一个病人只会是其中一种。原译“互相排斥”容易读成病毒株之间在生物学上互相排斥，改为“每个病人只会感染其中一种，两种的可能性相等，引起的症状也完全相同”。
    - 第 63 块：“支配结果和事件如何被框定的过程”定语太长，还夹着被动句。改为“现在我们转而讨论，结果和事件的框架是由哪些过程决定的”。
    - 第 70 块：“相对于比如每月的开销来评估”被“比如”拆开了，改为“相对于每月开销之类的数目来评估的”。通读时这一句又改了一次（见第 3 节第 4 条）。
    - 第 88 块：“留着买相机所需那笔钱”可以读成“留着钱去买相机”，比较的对象就反了。改为“如果相机的主观价值，超过把买相机要花的那笔钱留在手里的价值，人就会买相机”。
  - **标点**（1 条）：
    - 第 86 块：(S1, T1)、(S2, T2) 是记号，原译用全角括号包着半角逗号。附录 A 的 C(10, k) 也用半角，改为半角括号，前后和汉字之间加空格。这一块里的四处都改了。
  - **源文**（5 条）：
    - 第 3 块，卷号 34 应为 39：核实成立，加了译者注 t4（见第 1 节编辑处理的第 1 条）。
    - 第 65 块，mortality-survival 丢了连字符：英文已补上。
    - 第 96 块，between 的语病：原刊就是这样写的，英文和中文都不改。
    - 第 104 块，Erakar 的拼写：原刊参考文献里就是这样拼的，英文和中文都照原样保留。
    - 第 121 块，InformationProcessing：中英两个文件都改为 Information-Processing。
  - 这些源文问题都列在上面的“原文修复”一节里，需要主会话转记到 `review/source.md`。

## 3. 中文通读

- 执行者：编辑 agent（Opus 5.5），只读中文，从头读到尾。
- 发现并修改 7 处，每处都回查了原文：
  1. 第 9 块：“与期望值更高或相等的赌局相比更偏好确定的结果，称为风险规避”读着拗口，也和后半句“放弃确定的事，选择……称为风险寻求”不对称。改为“宁要确定的结果，不要期望值更高或相等的赌局，称为风险规避”，对应 a preference for a sure outcome over a gamble that has higher or equal expectation，说法和第 41 块的“宁要确定的收益，不要收益型赌局”一致。
  2. 第 49 块：“在图 2 中，在大部分范围内”连用两个“在”，改为“在图 2 中，决策权重在大部分范围内都低于对应的概率”。
  3. 第 61 块：“保险能否被人接受，可以通过怎样框定各种可能发生的情况来操纵”结构别扭，改为“人们是否接受一份保险，可以通过对各种可能情况的框定来操纵”，对应 the acceptability of insurance can be manipulated by the framing of the contingencies，说法和第 64 块的“对结果和各种可能情况的框定”一致。
  4. 第 70 块：“包括在一个更综合的账户里，在那个账户里，省下的钱……”重复了“账户里”，改为“包括在一个更综合的账户里，这时省下的钱是相对于每月开销之类的数目来评估的”。
  5. 第 74 块：“由按主题组织的方式决定”读不顺，改为“取决于账户按主题组织的方式”，对应 is controlled by topical organization。
  6. 第 87 块：“放弃了的选项”改为“已经放弃的选项”，对应 foregone alternatives。
  7. 第 90 块：“我们在正向领域也观察到了类似的效应”，读者不知道“正向领域”指什么。上文保险问题里的结果全是损失，下面的问题 10 和问题 11 都有赢钱的机会，改为“在有机会赢钱的情形中，我们也观察到了类似的效应”，对应 in the positive domain。
- 全节检查过没有破折号；中文和数字、拉丁字母之间的空格齐全；章名和术语（前景理论、损失厌恶、风险规避与风险寻求、确定的事、决策权重、框架效应、心理账户、禀赋效应、现状、参照点）和术语表一致；人名前后一致。
- 通读后运行 `status`，这一节显示 126/126。编辑在内存里调用 `book.compile_chapter` 编译了这一节，得到 128 个单元（126 个译文块加 2 张图片），4 条译者注都能识别，t4 在斜体的出处说明里也能正常生成注释按钮。

## 4. 阅读器校样

待主会话在阅读器里校样。需要特别看一下：第 3 块斜体出处说明里的译者注 t4；图 1、图 2 的图题和译者注 t2、t3；问题 1 到 11 的引用块和选项段落；参考文献里第 113、114、121 块这三条跨两行的引用块。

## 状态

译者自检、双语审校和中文通读已经完成，没有未解决的意义问题；四项审校要等主会话做完阅读器校样才算全部完成。`book.json` 里这一节的状态仍是 `todo`，由主会话改为 `review`。另外需要主会话把“原文修复”一节的 16 处修复记进 `tools/source_fixes.json`，把原书本身的问题记进 `review/source.md`。
