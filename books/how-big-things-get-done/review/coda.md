# 结语 更好地领导项目的 11 条启发式（coda）审校记录

全节 25 个块、6 条注释，另有 1 条译者注，中英逐块对应（`site.py status` 显示 coda 为 25/25、6/6）。

## 1. 译者自检

- 执行者：translation agent（Opus 5.5），译者本人。
- 范围：全节 25 个块（一级标题、开头两段、11 个小节标题和各自的一段正文）和 6 条注释，从第一块译到最后一块，没有跳过。对照英文逐段检查漏译、增译、否定、条件、数字、比较对象、谁做了什么、术语义项、人名，以及注释标记的位置和注释定义。另外用脚本核对了注释标记的编号和次序（中英完全一致），检查了中文里有没有破折号和“不是……而是……”句式；用 `tools/term_consistency.py` 核对了术语和人名，coda 没有被标出的块。
- 发现并修改：
  - 第 3 块 “The following are eleven of my favorite heuristics”：初稿“下面是我最喜欢的 11 条启发式”像是作者最喜欢的启发式一共就这 11 条，英文说的是其中的 11 条。改为“下面是我最喜欢的启发式中的 11 条”。
  - 注释 3 “and how they may be mitigated”：初稿“以及怎样减轻这些影响”漏了 may，改为“以及可以怎样减轻它们的影响”。
  - 第 23 块 “which was a main motivation for writing it”：初稿“这正是写作本书……的一个主要动机”，“正是”把它说成了唯一的理由，改为“这也是写作本书、反复推敲出这份启发式清单的一个主要动机”。
  - 第 25 块 “The Great Chicago Fire Festival failed not because Jim Lasko couldn’t predict …; it failed because …”：初稿“芝加哥大火节失败了，但失败的原因并不在于……”，“但”读起来像让步，改为“芝加哥大火节的失败，原因并不在于……。它失败，是因为……”。
- 翻译时的处理，供双语审校参考：
  - 对照句按体例改成直接的说法，意思不变：第 17 块 “participating is not about winning but about not losing” 译“参加这项比赛，求胜倒在其次，关键是不输”；第 25 块 “failed not because …; it failed because …” 拆成两句；同块 “The greatest threat Lasko faced wasn’t out in the world; it was in his own head” 先说肯定的一面，译“拉斯科面临的最大威胁，就在他自己的头脑里，在他的行为偏差之中，并不在外部世界”；注释 3 “best understood as complementary models …, not as competing models for explaining the same thing” 译“最好把它们理解为互补的模型，分别用来理解启发式的不同方面，它们并没有在相互竞争，争着解释同一件事”。
  - 破折号按意思改成逗号、括号或另起一句：第 2 块 “—plus your grandmother and anyone else with *phronesis*—” 改成并列的分句；第 5 块 “the masterbuilder—named after the skilled masons …—” 放进括号；第 11 块 “the Lego brick—the basic building block—” 译“乐高积木，也就是基本构件”；第 13 块 “can happen—and *has* happened—” 译“都可能发生，而且*已经*发生过”；第 15 块 “—building a time machine, engineering a black hole—” 译“比如造一台时间机器，或者人工造出一个黑洞”；第 23 块三处破折号改成另起一句或“包括”；第 25 块 “new management—the list goes on” 改成逗号。
  - 小节标题照术语表的结语小节标题表写；第 12 块的 Think Slow, Act Fast 写“慢思考，快行动”。
  - 术语照术语表和已译各章：heuristic 写“启发式”，rules of thumb 写“经验法则”，fast and frugal 写“快速、节俭”，tacit 写“默会”，*phronesis* 照写斜体，本节第一次出现括注“实践智慧”；masterbuilder 写“建造大师”；the box on the right 写“右边的方框”，project chart 照第 3 章写“项目流程图”；basic building block 和 server farm 照第 9 章写“基本构件”“服务器集群”，solar farm 写“太阳能发电场”；planning 和 delivery 写“规划”“实施”；window on risk 照第 1 章的窗口比喻写“风险之窗”，“开得小一些”“关上”；outside view 和 inside view 写“外部视角”“内部视角”；reference-class forecasts 写“参照类别预测”（原文这里没有缩写，没有括注 RCF）；fat-tailed risk 写“肥尾风险”；mitigate、mitigation 讲风险时写“降低”，讲气候时写“减缓”，climate mitigation 写“减缓气候变化”，mitigation (and adaptation) projects 写“减缓（和适应）项目”；upside 写“上行收益”，和小节标题“留意下行风险”对应；contingencies 写“应急储备”；bias for action 写“行动偏好”；behavioral biases 写“行为偏差”；multibillion-dollar 写“数十亿美元”。
  - 引号里的说法第一次出现括注原文：“慢思考，快行动”（Think slow, act fast）、“其中之一”（one of those）。
  - 人名照 `review/terms/people-zh.tsv`，本节第一次出现时括注英文，之后只写中文：艾德·卡特姆（Ed Catmull）、安德鲁·沃尔斯滕霍姆（Andrew Wolstenholme）、史蒂夫·乔布斯（Steve Jobs）、亚里士多德（Aristotle）、吉姆·拉斯科（Jim Lasko）。注释里的人名照写英文，包括注释 3 说明句里的 Gerd Gigerenzer、Daniel Kahneman、Amos Tversky。
  - 机构和地名：Heathrow’s Terminal 5 写“希思罗机场 5 号航站楼”，Great Chicago Fire Festival 写“芝加哥大火节”，Apple 写“苹果”，Tour de France 写“环法自行车赛”，Washington, DC 写“华盛顿特区”。
  - 数字照“全书统一的写法”：eleven 写“11 条”，twenty-one days 写“21 天”，three-week 写“三周”，dozens of people 写“几十人”，thousands more 写“数千个”，more than half his time 写“一半以上的时间”，decades 写“几十年”。
  - 斜体强调保留：第 13 块 *has* 写“*已经*”，第 23 块 *and* 写“*又*”。
  - 第 13 块列举的几场噩梦都是前面各章的例子（大贝尔特工程隧道被淹、疫情关闭影院、五角大楼选址、悉尼歌剧院炸掉已完工部分、墨西哥城地铁高架桥垮塌），照英文的说法译，没有补出项目名称。
  - 第 19 块 “Say no to monuments” 指项目发起人给自己立纪念碑的那类工程（第 1 章哥本哈根歌剧院、第 2 章都讲到过），译“对纪念碑式的项目说不”。
  - 第 3 块 paint-by-numbers 写“按数字填色”；第 2 块 grandmother 写“祖母”。
  - 第 7 块卡特姆的引文按英文译出，没有对照《创新公司》中译本的措辞。
  - 注释：注释 1、2、5、6 是纯出处，照英文原样保留；注释 3、4 有说明句，译成中文，出处照写英文。注释 3 里出处后面接中文句子时，照第 1 章注释 17 的做法用中文句号收尾。注释 3 的 positive heuristics 和 negative heuristics 写“正面启发式”“负面启发式”，加引号并括注原文（英文原文有引号）；recognition heuristic 写“再认启发式”，take-the-best heuristic 写“择优启发式”，availability heuristic 写“可得性启发式”，anchoring heuristic 写“锚定启发式”。注释 4 的 tease them out 和第 2 块的 teased out 一样写“提炼出来”。
  - 译者注 1 条：[^t1] 放在第 2 块的 *Eureka!* 后面，说明 heuristic 和 *Eureka!* 都来自古希腊语动词 heuriskein（发现、找到），见下面“原文疑点”。中文正文写“英文 heuristic（启发式）一词”，让读者知道说的是英文词的来历。
- 检查：`python3 scripts/site.py status how-big-things-get-done` 显示 coda 为 25/25、6/6。中文里没有破折号，也没有“不是……而是……”句式；中文里的连接号只出现在照写英文的出处里（页码范围 650–69、75–90、207–32、296–312、303–36、515–26 和卷期 nos. 3–4）。每块的数字都核对过，和英文的差别只是英文单词写的数转成了阿拉伯数字或汉字。
- 未决，留给双语审校或主会话决定：
  - 译者注 [^t1] 不在术语表“需要译者注的地方”的清单里，是本节译者加的；如果主会话觉得不需要，删掉它和正文里的标记即可，正文照原文的说法也读得通。
  - 注释 3 的“正面启发式”“负面启发式”“再认启发式”“择优启发式”“可得性启发式”“锚定启发式”还没有进术语表；第 2 章讲 availability 和 anchoring 时，如果用的是别的写法，需要统一。
  - 第 19 块“对纪念碑式的项目说不”是按全书语境解释的译法；如果审校觉得应该照字面写“对纪念碑说不”，可以改。
  - `book.json` 里 coda 的状态还是 todo，需要主会话改成 draft 或 review（本任务不改 `book.json`）。

## 原文疑点

| 位置 | 原文 | 处理 |
| --- | --- | --- |
| 第 2 块 | The word has its origin in the ancient Greek word *Eureka!,* | heuristic 并不直接来自 Eureka，两者都来自古希腊语动词 heuriskein（发现、找到），Eureka 是它的一种变位，意思是“我找到了”。正文照原文译，加译者注 [^t1] 说明 |
| 第 2 块 | *Eureka!,* | 逗号排在斜体里面，只影响英文排版，中文照常译 |
| 注释 5 | *Creativity, Inc: Overcoming the Unseen Forces …* | 书名通常写 Creativity, Inc.（Inc 后有句点）。出处照英文原样保留，没有改 |

## 2. 双语审校

- 执行者：另一个独立上下文的 agent（Opus 5.5），没有参与翻译。
- 范围：全节 25 个块和 6 条注释（另有 1 条译者注），逐块对照英文；审校者用脚本核对了注释 3、4 的出处，和英文逐字相同。编辑 agent（Opus 5.5）对每条发现重新查看英文和中文，核实后再决定是否采纳。
- 发现：12 条（意思方面 2 条，表达方面 10 条）；核实后采纳 12 条，不采纳 0 条。采纳的 12 条里，有 6 条在审校者建议的基础上另换了更贴切的写法，原因写在各条后面。
  - 采纳的例子：
    - 注释 3 “But they are best understood as complementary models for understanding different aspects of heuristics, not as competing models for explaining the same thing.”：原译后半句“它们并没有在相互竞争”把作者“最好怎样理解”的建议写成了事实判断，和前一句“两派之间确实存在重要的分歧”放在一起，像是作者否认两派有竞争。改为“但最好把两派看作互补的模型，各自用来理解启发式的不同方面，用不着把它们当成争着解释同一件事的对手”。审校者建议的“最好把它们理解为……用来理解……”里“理解”连用两次，所以前一个改用“看作”。
    - 第 7 块 “This is why the role of masterbuilder is not as solitary as it sounds”：“孤单”偏向情绪上的寂寞，这里说的是一个人包揽全部工作，改为“单打独斗”。审校者建议句首用“所以”，而同一段下一句也以“所以”开头，句首改用“正因为如此”。
    - 第 9 块 “noted Andrew Wolstenholme, the leader who delivered Heathrow’s Terminal 5 in chapter 8”：原译“第 8 章里建成希思罗机场 5 号航站楼的负责人”字面上像航站楼是在第 8 章里建成的，改为“第 8 章讲到的、主持建成希思罗机场 5 号航站楼的负责人”。
    - 第 9 块 “As the project sails into a storm of events and details”：“由各种事件和细节掀起的风暴”多出一层因果，英文说的是由事件和细节构成的风暴，改为“各种事件和细节交织而成的风暴”。
    - 第 13 块 “Good planning boosts the odds of a quick, effective delivery”：原译“提高实施快速、有效的几率”难断句。审校者建议“又快又有效”，可前一句刚用过“又贵又危险”，改为“好的规划能让实施更有可能做到快速、有效”。
    - 第 25 块 “it failed because he took the inside view … Because focusing on the particular case and ignoring the class is what human psychology inclines us to do.”：前一句补上“之所以”，写成“它之所以失败，是因为……”；后一句改为“因为人类的心理让我们倾向于只盯着具体的个案，忽视它所属的类别”。审校者建议的“人的心理天生就让我们……”多了英文没有的“天生”，这个词没有用。
    - 第 21 块 “he spent more than half his time acting like a diplomat”：“都在像外交官一样工作”生硬，改为“都在扮演外交官的角色”。审校者建议给“外交官”加引号，英文这里没有引号，中文也照英文不加。
    - 注释 3 “Today, two main schools exist in thinking about heuristics.”和“Chapter 2 covered central aspects of negative heuristics, their impact on decision making, and how they may be mitigated.”：改为“如今，在启发式问题上主要有两个学派”和“第 2 章讨论了负面启发式的几个核心方面、它们对决策的影响，以及可以怎样减轻这种影响”，central aspects 译得更贴切，也去掉了“影响”的重复。审校者建议的“在启发式的研究上”把 thinking 说窄成了“研究”，换成“在启发式问题上”。
    - 其余 4 条照审校者的建议改：第 3 块 “The following are eleven of my favorite heuristics” 改为“下面从我最喜欢的启发式里挑出 11 条”，仍然表明是其中的 11 条；第 5 块 “possesses all the *phronesis* needed to make your project happen” 改为“拥有把你的项目做成所需的全部 *phronesis*”；第 19 块 “will the project have the people and funds, including contingencies, needed to succeed?” 改为“这个项目会有成功所需的人手和资金（包括应急储备）吗？”；第 23 块 “quickly accelerating and scaling up the effort” 改为“让这项工作迅速提速、扩大规模”，同句的“遵循本书提出的原则”也照建议改为“按照本书提出的原则”。
  - 不采纳的：没有。12 条都对照英文核实过，指出的问题都成立。
- 审校者的总体判断：全节逐块对照，整体质量很高，可以进入中文通读；没有发现漏译、增译、否定写反、数字或谁做了什么方面的错误。人名和 `review/terms/people-zh.tsv` 一致，本节第一次出现时都括注了英文（艾德·卡特姆、安德鲁·沃尔斯滕霍姆、史蒂夫·乔布斯、亚里士多德、吉姆·拉斯科）；11 个小节标题和术语表的结语小节标题表逐字相同，核心术语照术语表写；注释标记 [^1] 到 [^6] 的位置和次序都对，注释 1、2、5、6 原样保留，注释 3、4 的出处和英文逐字相同，说明句译成了中文；中文正文没有破折号，也没有“不是……而是……”句式。译者注 [^t1] 内容准确，对中文读者有用，建议保留。需要改的主要是注释 3 后半句的语气和第 7 块的“孤单”，其余是几处拗口的句子。

## 3. 中文通读

- 执行者：编辑 agent（Opus 5.5）。
- 范围：采纳审校意见之后，从一级标题读到译者注，顺着中文读完全节，检查是否连贯、有没有重复、指代是否清楚，以及人名、术语和小节标题在本节和前面各章里是否一致。
- 发现并修改（每处改动都回查了英文，意思没有变）：
  - 第 7 块 “When possible, hire a masterbuilder. And the masterbuilder’s team.”：原译后一句“还有建造大师的团队。”单独成句，容易读成“另外还有一个团队”，看不出团队也要一起请。改为“还要把建造大师的团队一起请来”，仍然分成两句，保留英文的节奏。
  - 第 17 块 “forget about forecasting risk; go directly to mitigation by spotting and eliminating dangers”：原译“面对这种风险，别再想着预测风险，直接去降低风险”一句里“风险”出现三次，改为“面对这种风险，别再想着怎么预测，直接着手降低”。
  - 第 23 块 “which was a main motivation for writing it and for hammering out this list of heuristics”：原译“这也是……的一个主要动机”里的“也”在前文找不到呼应的对象，改为“这是写作本书、反复推敲出这份启发式清单的主要动机之一”，仍然表示它是几个主要动机中的一个。
  - 注释 3 “But they are best understood as complementary models”：“它们”紧跟在一长串出处后面，可能被读成那几篇文献，改为“两派”，和前一句“两派之间确实存在重要的分歧”对应。
- 读过、保留原样的地方：第 17 块 “participating is not about winning but about not losing” 译“求胜倒在其次，关键是不输”，和后一句 “Only after that can you consider winning”（“做到了这一点，才谈得上考虑赢”）衔接得上，保留。安德鲁·沃尔斯滕霍姆的写法和第 8 章相同；“右边的方框”“风险之窗”“行动偏好”“行为偏差”“应急储备”“减缓气候变化”都照术语表；“锚定”“可得性”和第 2 章、第 6 章的写法一致。`tools/term_consistency.py` 没有标出本节的块。
- 检查：`python3 scripts/site.py status how-big-things-get-done` 显示 coda 仍为 25/25、6/6。中文正文没有破折号，也没有“不是……而是……”句式；连接号仍然只出现在照写英文的页码和卷期里。`en/` 没有改动。

## 状态

没有未解决的意义问题。原文疑点（heuristic 的词源、*Eureka!,* 的逗号位置、注释 5 的书名写法）照上面“原文疑点”表的处理保留。译者自检留下的事项仍由主会话决定：注释 3 的“正面启发式”“负面启发式”“再认启发式”“择优启发式”“可得性启发式”“锚定启发式”是否补进术语表；第 19 块“对纪念碑式的项目说不”的译法，双语审校没有提出异议；`book.json` 里 coda 的状态现在仍是 todo。双语审校建议保留译者注 [^t1]。第 4 节阅读器校样还没有做。
