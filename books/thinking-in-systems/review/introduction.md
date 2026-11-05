# 引言 系统的视角（introduction）审校记录

全节 53 个块、2 条脚注，中英逐块对应（`site.py status` 显示 53/53、2/2）。下文的“第 N 块”按 `site.py status` 计数的 53 个可译块编号，从节名算起。

## 1. 译者自检

- 执行者：translation agent（Opus 5.5）。
- 范围：全节 53 块和 2 条脚注，从节名到插曲末段逐块对照英文，检查漏译、增译、否定、条件、数字、责任主体、比较对象、术语义项、人名和脚注标记；人名对照 `review/terms/people-zh.tsv`；术语用 `tools/term_consistency.py` 检查；用框架的 markdown-it 渲染中文，看斜体有没有因为紧挨中文标点而失效；全文查破折号和体例禁用的对比句式。译文语气照第 1 章样章。
- 发现并修改：
  - 第 4 块 “or walk itself downstairs”：初稿“自己一级一级走下楼梯”，“一级一级”是原文没有的，删去。
  - 第 13 块 “As our world continues to change rapidly and become more complex, systems thinking will help us …”：初稿把前半句写成并列的陈述，丢了 As 的伴随关系，改为“随着我们的世界继续迅速变化、变得越来越复杂，系统思考会帮助我们……”。
  - 第 26 块 “Serious problems have been solved by focusing on external agents”：初稿“把注意力放在外部因素上，确实解决过一些严重的问题”，“确实”是原文没有的强调，改为“有些严重的问题，是靠着把注意力集中在外部因素上解决的”。
  - 第 30 块 “Systems happen all at once.”：初稿“系统却是同时发生的”，读者看不出同时发生的是什么，改为“系统里的一切却是同时发生的”。同一块 “They are connected not just in one direction, but in many directions simultaneously.” 按体例避开对比句式，写成“系统里的连接同时指向许多方向，并不只朝着一个方向”。
  - 第 33 块 “You’ll see how a few of these creatures behave and why and where they can be found.”：初稿“为什么会这样，在哪里能找到它们”把 why 接到了行为上。按句法，why 和 where 都修饰 can be found，改为“也会看到它们为什么会出现、在哪里能找到”。
  - 第 35 块 “the nature of relationships in a family, a community, or a nation”：初稿“人际关系的性质”把国家内部的各种关系也说成了人与人的关系，改为“各种关系的性质”。同一块 “Or we identify … Or we see … Or we witness …” 和前面的 “we find ourselves saying” 一样，说的是经常会发生的事，初稿“认出了”“看到了”“目睹了”读起来像一次性的经历，改为“会认出”“会看到”“会目睹”。
  - 第 39 块 “and then dropped by our offices”：初稿“来我们办公室坐了坐”，“坐了坐”是添出来的细节，改为“顺道到我们的办公室来了一趟”。同一块 “Somehow you come at the world in a different way.”：初稿“和别人不同”多出一个比较对象，改为“不知怎么，你们对待世界的方式就是不一样”。
  - 第 47 块 “they groped sightlessly”：初稿“只能看不见地摸索”不通，改为“又看不见，只能摸索”。
  - 第 53 块 “This ancient Sufi story was told to teach a simple lesson but one that we often ignore”：初稿“这个古老的苏菲派故事，是为了讲一个简单的道理”，讲故事的人不见了，主语也不顺，改为“人们讲这个古老的苏菲派故事，是为了传授一个简单的道理，可我们常常忽视这个道理”。
- 写法上的决定：
  - 节名照术语表写“引言 系统的视角”。正文第 40、41 块的 lens 是具体的比喻（人眼、显微镜、望远镜），写“透镜”，“系统思考这面透镜”和前文一致。
  - 第 3 块署名行写“罗素·艾可夫（Russell Ackoff）[^1]，运筹学家”，operations theorist 照术语表的示例写“运筹学家”，脚注标记的位置照第 5 章已译的署名行。
  - 第 2 块和第 26 块的 messes 照术语表写“乱局”，没有括注英文，术语表没有要求括注。
  - 第 4 块 Slinky 在本节第一次出现，写“弹簧圈（Slinky）”，之后只写“弹簧圈”。
  - 第 22 到 24 块：三组“系统原理加一句俗语”的引文块，英文俗语前面的破折号去掉，斜体保留。A stitch in time saves nine 用通行的中文说法“小洞不补，大洞吃苦”；《马可福音》4:25 用术语表给出的和合本译文，经文出处放在斜体里面，“或者”放在斜体外面，和英文的 or 一样；The rich get richer and the poor get poorer 和 Don’t put all your eggs in one basket 照术语表。
  - 第 30 块 time graphs 写“随时间变化的曲线图”，读者一看就懂；它和术语表里的“行为随时间变化图”指同一类图。
  - 第 34 块 “how and why systems work so beautifully” 写“系统怎样运转得这么出色、为什么运转得这么出色”，和第 3 章章名“系统为什么运转得这么好”意思相通；“surprise and confound us” 写“让我们意外、让我们困惑”，“意外”照术语表。
  - 第 36 块 archetypes 写“基模”，system traps 写“系统陷阱”，and opportunities 写“与机遇”，和第 5 章章名“系统陷阱……与机遇”对得上。基模在第 5 章用粗体给出定义并括注英文，这里没有括注。
  - 第 44 块插曲标题照术语表的示例写“插曲 • 盲人摸象”。第 45 块的 Ghor 照术语表写“古尔”。
- 检查：
  - `site.py status` 显示引言 53/53、2/2。
  - 人名：罗素·艾可夫和 people-zh.tsv 一致，在本节第一次出现时括注英文；Idries Shah 只出现在脚注里，照写英文。
  - 术语：`term_consistency.py` 没有标出本节的任何块。反馈延迟、增强回路、竞争排斥原理、公地悲剧、目标侵蚀、政策阻力、上瘾、基模、系统陷阱、杠杆点、系统动物园、要素、相互连接、系统思考者都照术语表；holism、reductionism 写“整体论”“还原论”，unholistic 写“非整体的”。
  - 机构和地名：麻省理工学院、达特茅斯学院、欧佩克、工业革命、苏菲派、古尔，都照术语表。
  - 斜体：渲染后 8 处中文斜体（4 句俗语和经文，“重构”“做事”“看事情”“想事情”）都生效，页面上没有残留的星号。
  - 脚注：两条都只是出处，和英文逐字相同，页码范围 93–104 照原样保留。
  - 第 17 块的五条列表：否定和限定逐条核对过，“rarely”写“很少”，“not solely responsible”写“不能全怪”，“at least in part”写“至少部分”，“no one person … not even the addict”写“没有哪个人能单凭一己之力……就连上瘾者自己也做不到”。
  - 全节中文没有破折号，也没有体例禁用的对比句式。
- 未决：
  - 第 44 块插曲标题：“盲人摸象”是术语表的示例，原题 The Blind Men and the Matter of the Elephant 里 the Matter of 的语气没有单独体现。要不要换成更贴近原文的标题，由主会话决定。
  - 第 22 块俗语：“小洞不补，大洞吃苦”保留了缝补的意思，没有保留原文“一针省九针”的数字。更贴近字面的说法是“及时一针省九针”，但在中文里不如前者通行。
  - 第 2 块“乱局”：这是艾可夫的专门说法，第 26 块又出现一次。要不要在第一次出现时括注 messes，可由主会话统一决定。

## 原文疑点

| 位置 | 原文 | 处理 |
| --- | --- | --- |
| 第 35 块 | That discussion will lead to us to look at | 多了一个 to（`review/source.md` 已列），按 will lead us to look at 译，不加注 |
| 第 38 块 | the Appendix provides ways to dig deeper into the subject with a glossary, a bibliography of systems thinking resources, a summary list of systems principles, and equations | 本版的参考书目（Bibliography of Systems Resources）是附录后面单独的一节，没有收在附录里。说法不影响理解，照原文译，不加注 |

## 2. 双语审校

- 执行者：另一个独立上下文的 agent（Opus 5.5），没有参与翻译。
- 范围：对照英文逐块读完全节 53 块和 2 条脚注，审校时没有改动文件；`site.py status` 显示 53/53、2/2，第一行标题和术语表一致。审校意见由编辑 agent（Opus 5.5）逐条对照英文核实后处理。
- 发现：19 条（意思 6 条，用词和语感 12 条，标点 1 条）；核实后采纳 18 条，不采纳 1 条。采纳的 18 条里，有 6 条换了比审校者建议更合适的写法。
  - 采纳的例子：
    - 第 17 块第 5 条 “no one person, no matter how tough, no matter how loving, can cure a drug addict”：原译“没有哪个人能单凭一己之力治好一个吸毒上瘾的人，不管他多么严厉，多么有爱心”，“他”紧跟在“吸毒上瘾的人”后面，读者会以为严厉、有爱心说的是上瘾者。改为“任何一个人，不管多么严厉、多么有爱心，都没法单凭一己之力治好一个吸毒上瘾的人”，让步的分句紧挨着它修饰的“任何一个人”。
    - 同一条 “Drug addiction is not the failing of an individual”：failing 指品性上的弱点，“过失”偏指疏忽造成的错误，改为“毒瘾并不是个人品性上的缺陷”。
    - 第 14 块 “interconnected in such a way that they produce their own pattern of behavior over time”：原译“以某种方式相互连接，产生出……”读起来像两件并列的事，改为“它们相互连接的方式，使它们产生出自己特有的、随时间变化的行为模式”，保留“连接的方式决定行为”这层因果。
    - 第 13 块 “help us manage, adapt”：“管理、适应”两个动词都缺宾语，改为“应对局面、适应变化”。同一块 “gives us the freedom to identify root causes”：审校者建议“不受束缚”，编辑改为“给了我们自由，让我们能找出问题的根本原因”，保留 freedom 这个词。
    - 第 24 块 “than a uniform system with little diversity”：“单一系统”容易读成“单独一个系统”，改为“和一个成分单一、缺乏多样性的系统相比”。
    - 第 23 块 “rewards the winner of a competition with the means to win further competitions”：改为“拿继续取胜的手段来奖励竞争中的赢家”，去掉“赢家得到赢得”的重复，补回 rewards 的“奖励”。
    - 第 20 块 “magnificent examples of integrated, interconnected, self-maintaining complexity”：原译三个“的”字定语堆在“复杂性的绝妙范例”前面。审校者建议把 complexity 改成“复杂整体”，编辑最后定为“我们的身体整合为一体、相互连接、能够自我维持，是复杂性的绝妙范例”，拆掉定语堆叠，也保留了“复杂性”（过程见第 3 节）。
    - 第 39 块 “Somehow you come at the world in a different way.”：“对待世界的方式”偏指待人处事。come at 指着手认识、切入问题，教授前面说的是“你们问的问题不一样”“你们看得到我看不到的东西”，改为“你们认识世界的路数就是不一样”，比审校者建议的“看世界”多保留了提问这一层。
    - 第 4 块 “pour back and forth from hand to hand”：“倾泻”指大量的水急泻而下，画面不对；审校者建议“像水一样……来回流淌”，多了一个比喻。改为“在两只手之间倒来倒去”，pour 照字面写“倒”，这也是中文描述弹簧圈玩法的常见说法。
    - 其余采纳：第 15 块 “The system, to a large extent, causes its own behavior!” 改为“系统的行为，在很大程度上是它自己造成的！”；第 17 块第 3 条 “had not built economies that are vulnerable to supply interruptions” 原译“造就出”带褒义，改为“没有让本国经济变得经不起供应中断”；第 25 块 “would much rather … rather than …” 改为“宁可……也不愿……”；第 26 块 “those most rooted in the internal structure” 改为“在复杂系统内部结构里扎根最深的那些问题”；第 29 块和第 40 块的“看待方式”缺对象，改为“观察和思考方式”“用系统的眼光看问题，比用还原论的方式想问题更好”“每一种观察方式”；第 34 块 “jump into a kind of behavior” 原译“跳进一种……行为”搭配不通，改为“表现出一种……行为”，突然的意思由前面的“突然之间、毫无预兆地”表达；第 35 块 “an allocation system for sharing water resource among communities or financial resources among schools” 的长定语拆成“各个社区之间分享水资源的分配系统，或者各所学校之间分享资金的分配系统”，顿号后面的“或者”也随之去掉；第 46 块 “some sightless from among this blind community” 原译“这群盲人当中有几个看不见的人”像笔误，删去“看不见的”。
  - 不采纳：
    - 第 33 块 “You’ll see how a few of these creatures behave and why and where they can be found.”：审校者认为 why 说的是“它们为什么有这样的行为”，建议改为“有怎样的行为、为什么会这样，以及在哪里能找到它们”，并请主会话裁定。编辑不采纳。英文按印出来的样子，why 和 where 并列在 they can be found 前面；要读成 “behave and why”，得假设原文漏了一个逗号，没有足够的根据。第 2 章既解释每种结构为什么会出现那样的行为，也举出现实中在哪些地方会遇到它，两种读法都和内容相符，所以照英文的句法译。译者自检时已经按同样的理由，从“为什么会这样”改成了“为什么会出现”。保留“它们为什么会出现、在哪里能找到”；前半句在中文通读时改得更顺（见第 3 节）。这一处不算原文错误，没有记入原文疑点。
- 审校者的总体判断：译文忠实、完整，没有漏译、增译、否定错误或数字错误；人名、术语、机构名和地名都照术语表，罗素·艾可夫在本节第一次出现时括注了英文；两条脚注的出处和英文逐字相同，标记位置正确；全文没有破折号，也没有“不是……而是……”句式。最要紧的是第 17 块毒瘾一条里“他”的指代歧义，其次是系统定义句的因果关系，再往后是几处缺宾语、搭配不当、定语堆叠和照英文副词硬译的地方。这些改完以后，这一节可以进入中文通读。审校者也看了译者自检留下的三条未决事项（插曲标题、“小洞不补，大洞吃苦”、乱局是否括注），认为都在合理范围内，没有另提意见。

## 3. 中文通读

- 执行者：编辑 agent（Opus 5.5）。
- 范围：采纳审校意见以后，顺着中文从节名读到插曲末段，检查连贯、重复、指代，以及人名和术语前后是否一致。
- 发现并修改（每一处都回查了英文）：
  - 第 20 块：采纳审校意见时先写成“我们的身体就是绝妙的范例，它是一个……的复杂整体”，和前半句“我们自己就是复杂系统”连用两个“就是”，complexity 也变成了“整体”。通读时改为“我们的身体整合为一体、相互连接、能够自我维持，是复杂性的绝妙范例”。同一块末句 “and how to work with them”：前面已经用“和复杂系统打过交道”译 dealt with，末句又写“怎样和它们打交道”，改为“怎样和它们配合”，也更贴近 work with。
  - way of seeing 在本节出现五次，原译分别写成“看法”“看待和思考方式”“看待方式”“看待方式”“看待世界的方式”。审校意见改了中间三处，通读时把另外两处也统一过来：第 28 块 “An old way of seeing” 由“一种古老的看法”改为“一种古老的观察方式”（“看法”容易读成意见、主张），第 41 块 “the more ways of seeing, the better” 由“看待世界的方式越多越好”改为“观察世界的方式越多越好”。第 40 块对比 seeing 和 thinking 的那一句保留“用系统的眼光看问题”“用还原论的方式想问题”。
  - 第 31 块 “because you can see all the parts of a picture at once”：“一眼同时看到”语义重复，改为“一眼看到”。
  - 第 33 块：“你会看到其中几种生物的行为是什么样的”改为“你会看到其中几种生物有怎样的行为”，后半句不变。
- 读过、保留原样的地方：第 26 块 “Because they are embedded in larger systems” 的 they 在英文里可以指前面列举的做法，也可以指问题，中文“由于它们嵌在更大的系统之中”保留了同样的指代，紧接在预防天花等几项做法后面，读起来不费解。第 45 块“带着随从……带来了军队”对应 with his entourage 和 brought his army，两个“带”读起来自然。
- 检查：罗素·艾可夫在本节第一次出现时括注英文，正文没有别的人名，Idries Shah 只在脚注里，照写英文；“乱局”“弹簧圈”“增强回路”“竞争排斥原理”“公地悲剧”“目标侵蚀”“政策阻力”“上瘾”“基模”“杠杆点”“系统思考者”前后一致；`term_consistency.py` 没有标出本节的块；全文没有破折号，也没有“不是……而是……”句式；`site.py status` 仍显示引言 53/53、2/2。

## 状态

- 没有未解决的意义问题。第 33 块 why and where 的归属有两种读法，编辑照英文的句法裁定，理由见第 2 节；主会话如果倾向另一种读法，只需改这一个分句。
- 译者自检留下的三条写法上的未决事项（插曲标题“盲人摸象”、俗语“小洞不补，大洞吃苦”、“乱局”第一次出现时要不要括注 messes）不涉及意思，仍由主会话决定。
- 还差第 4 节阅读器校样。
