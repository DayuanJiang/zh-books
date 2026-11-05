# 尾声 帝国如何崩塌（epilogue）审校记录

全章 40 个块、22 条注释，中英逐块对应（`site.py status` 显示 40/40、22/22）；没有加译者注。

## 1. 译者自检

- 执行者：translation agent（Opus 5.5）。
- 范围：全章 40 块和 22 条注释，对照原文逐段检查漏译、增译、否定、条件、数字和日期、谁做了什么、比较对象、术语义项、人名、脚注标记和定义。另用脚本逐块比对了中英两边的数字和脚注标记：标记的编号和顺序完全一致；数字的差异都来自英文拼写的数字改成阿拉伯数字或汉字（例如 six hundred eighty thousand hours 写作“68 万小时”，two hundred thousand recordings 写作“约 20 万条录音”），或月份改写（例如 November 2021 写作“2021 年 11 月”）。
- 发现并修改：
  - “a little more than the minimum wage in Colombia, around $335 a month”：335 美元是哥伦比亚的最低工资，初稿“挣到比哥伦比亚最低工资多一点的钱，每月约 335 美元”读起来像是她的收入，改为“比哥伦比亚最低工资（每月约 335 美元）多一点的钱”。
  - “For the same reasons AI researchers first gravitated toward language to build their technologies, the loss of a language extends far beyond the loss of a form of communication”：两件事的原因相同，译作“失去一门语言，远远不只是失去一种交流方式，其中的道理，和 AI 研究人员当初被语言吸引、选中它来打造技术的理由是一样的”，保留原文的因果对应。
  - “this impending existential threat, a fundamentally different conception of what is existential”：作者拿语言消亡和 AI 圈说的生存风险对比，中文括注“这里的‘生存’，和 AI 生存风险里的‘生存’含义截然不同”，把对比对象写了出来（见“未决”）。
  - 按体例改写原文的对比句式，否定的对象和原文一致：“not by any means meant to dismiss AI in its entirety. What I reject is...” 译作“绝无全盘否定 AI 的意思。我反对的是……”；“not the theoretical rogue AI harms of Doomerism, but the existing real-world harms” 译作“这里说的安全，针对的是现实中已经存在的危害……末日派所说的失控 AI 那种理论上的危害，不在其列”；“rather than be posted freely online” 译作“不会随意公开到网上”。
  - “can only be derived from, indeed, will *ever* emerge from”：保留斜体强调，译作“只能依靠这样一种技术愿景，甚至以为益处*真的会*从这种愿景中产生”。
  - “Half a year later, after going public about his OpenAI experience through my article in *The Wall Street Journal*, he also started a nonprofit”：“半年后”指创办 TCA 的时间，公开经历在此之前，译作“半年后，他已经通过我在《华尔街日报》上的文章，公开讲述了自己为 OpenAI 工作的经历，这时又……创办了自己的非营利组织”。
  - “Goodness, benefit to humanity”：初稿“好，造福人类”读不通，改为“‘好’也罢，‘造福人类’也罢，这些说法的含义永远因人而异”。
  - “about a third have some online presence”：初稿“在网上有一些存在”生硬，改为“在网上多少有些内容”。
  - “He was fielding various requests”：初稿“应付”带敷衍的意思，改为“处理”。
  - “I wrote about Te Hiku’s work before ChatGPT swiftly seized the dominant AI development paradigm, all but tossing consent, reciprocity, and sovereignty out the window”：初稿两句连用“此后”，改为“是在 ChatGPT 问世之前。ChatGPT 很快主导了 AI 开发的范式，几乎把同意、互惠和主权全都抛到了九霄云外”。
  - 脚注标记：[^2]、[^3]、[^7]、[^20]、[^22] 原文落在词组中间或句首，中文挪到对应词句的末尾，注释开头的粗体照中文实际字句写；[^19] 的粗体用省略号缩写为“2019 年，……里娅·卡卢里发表演讲”，[^22] 缩写为“正如麻省理工学院教授……约瑟夫·维森鲍姆”。注释里的采访和通信说明按体例翻译（例如注释 5 的 November 2021–January 2022 写作“2021 年 11 月至 2022 年 1 月”），出处照原文保留。
- 人名：全章人物都按 `review/terms/people-zh.tsv` 译，第一次出现时括注英文；Fuentes 第一次出现写全名“奥斯卡丽娜·贝罗妮卡·富恩特斯·阿纳亚”，之后写“富恩特斯”。原文只写 “the Schumer forums”，中文补全为“参议员查克·舒默（Chuck Schumer）召集的那几场论坛”，和第 13 章的说法一致。注释里的人名照原文（Caleb Moses 不在译名表里，只出现在注释中）。
- 术语和专名：te reo Māori 译“毛利语”，第一次出现括注原文；kaitiakitanga 按术语表写作“*kaitiakitanga*（守护）”；Aotearoa 译“奥特亚罗瓦”并括注；Native Schools Act 译《原住民学校法》并括注；Kaitāia 译“凯塔亚”并括注；Te Hiku Media、DeepSpeech、MOSACAT、Equidem、Hugging Face 照写原名；DAIR 写作“分布式 AI 研究所（Distributed AI Research Institute）”；Data Workers’ Inquiry 译“数据工作者调查”；African Content Moderators Union 译“非洲内容审核员工会”；Techworker Community Africa 译“非洲技术工作者社区”，和译名表里马森盖的说明一致；Fairwork 沿用第 9 章的“公平工作”；Queer in AI 沿用第 7 章的“AI 界酷儿”；CFPB、FDA 写出中文全称再括注缩写；Energy Star 译“能源之星”；Doomerism 按术语表的“末日派”写作“末日派所说的”；axes of power 译“权力的维度”；“If OpenAI’s mission is a formula for constructing empire” 里的 formula 译“公式”，和第 18 章标题“帝国的公式”呼应。
- 未决：
  - “a fundamentally different conception of what is existential” 的括注点明了和 AI 生存风险对比，原文没有写出对比对象，审校时可以判断是否保留这层补充。
  - “He had met with US representatives who came to visit Nairobi” 译作“美国众议员”。representatives 一般指众议员，但也可能泛指美国政府派来的代表；如果有材料能确认身份，再相应改动。
  - “Olin College” 译“欧林工程学院”（学校全名 Franklin W. Olin College of Engineering）；“Bay Area–based research lab of the Chinese company Baidu” 译“百度设在旧金山湾区的研究实验室”，没有写出实验室的名字。
  - 术语表里没有的说法：data imperative 译“对数据的硬性需求”；public contestation window 译“公众异议期”；shell entities 译“空壳实体”；Big Tech 译“科技巨头”。
  - 注释 7 的页码范围 1–2 和注释 22 的论文标题 “ELIZA—a Computer Program...” 含连接号和破折号，按“出处照原文”的规则保留，中文部分没有破折号。

## 原文疑点

| 位置 | 原文 | 处理 |
| --- | --- | --- |
| 注释 22 | *Communications of the ACM* 9, no. 1, (January 1966) | 疑似排版错误，括号前多了一个逗号；题词注释 1 引用同一篇论文，写作 9, no. 1 (January 1966)。照原文保留 |
| 注释 19 | posted December 9, 2019, by NIPS 2019 | 疑似体例不一致，其他视频出处都写作 posted on（例如注释 3）。照原文保留 |
| 正文第 2 段 | After rapid urbanization swept across the country in the early 1900s, Māori communities disbanded and dispersed | 疑似时间有出入：新西兰全国的城市化在 20 世纪初已经开始，毛利人大规模迁往城市却发生在第二次世界大战以后。Te Ara 新西兰百科（teara.govt.nz/en/taupori-maori-maori-population-change/page-4）和 NZHistory 的数字是：住在城市的毛利人 1936 年占 17%，1945 年占 26%，1966 年占 62%，1971 年占 71%。原文的意思可能是全国的城市化，也可能把时间写早了。译文照原文写“20 世纪初”，未加译者注 |

## 2. 双语审校

- 执行者：另一个独立上下文的 agent（Opus 5.5），没有参与翻译。
- 范围：全章 40 个块和 22 条注释，逐块对照英文，核对事实、数字、日期、金额、谁做了什么、人名和译名表是否一致、脚注标记的编号、顺序和位置、注释开头的粗体和出处格式、标题、分隔线、破折号和句式，并对译者自检列出的未决项逐条给出意见。审校者报告事实、数字和日期全部准确，没有整句漏译或增译。
- 发现：20 条（意思偏差 5 条，术语和前后章节不一致 3 条，翻译腔或搭配不当 12 条）；编辑逐条回查英文和相关章节后，采纳 20 条，不采纳 0 条。其中 5 条的具体改法和审校者的建议不同，下面注明。
  - “once they had the resources, they would also buy their own on-site Nvidia GPUs”：前一个分句刚说“语言学习资源”，“等有了资源”容易被读成这些学习资源。改为“等有了足够的资金”。
  - “the data would stay under Te Hiku’s stewardship rather than be posted freely online”：“随意公开”偏离了 posted freely（放到网上供人自由取用）。改为“不会放到网上任人取用”；审校者建议的“任人免费取用”多了“免费”这层意思，没有照用。
  - “Once a particular program is unmasked, once its inner workings are explained in language sufficiently plain to induce understanding, its magic crumbles away.”：这是题词里维森鲍姆那段话的一部分，作者在结尾回扣开篇。引文改成和题词译文一字不差的“一旦某个程序被揭去面纱，一旦有人用足够浅显、足以让人领会的语言把它的内部运作讲清楚，它的魔力就土崩瓦解了”；下一句 “I hope this book is just one offering to help induce understanding” 改为“我希望这本书能尽一份绵薄之力，帮助人们领会”，用“领会”和引文呼应，也去掉了没有所指的“其中”。
  - “after the Schumer forums”：第 13 章把这一系列论坛译作“AI 洞察论坛（AI Insight Forum）”，改为“参议员查克·舒默（Chuck Schumer）召集的那一系列 AI 洞察论坛”，读者能对上第 13 章。
  - “which so often happens under shell entities”：第 12 章同一种做法译作“借空壳公司的名义”，改为“这些洽谈往往借空壳公司的名义进行”。
  - “In August 2024, as we caught up”：这是一次采访（注释 14），后文又说 “Not long before our call”，可以确定是通话。“叙旧”改为“我和奥金伊再次通话时”。
  - “Te Hiku’s radical approach as even more relevant and vital”：“激进”在中文里常带贬义，和作者的赞许相反；“切合现实”也偏离了 relevant。改为“这种彻底另辟蹊径的做法更有现实意义，也更加重要”，同时删掉和“越来越觉得”重复的“变得”。改法比审校者建议的“从根本上另起炉灶”短一些。
  - “communities affected by but not yet typically represented in AI research ... toward one they wanted to inhabit”：affected by 和 represented in 共用宾语 AI research，改为“受 AI 研究影响、在 AI 研究中却通常还没有自己声音的社群”。结尾“改造成他们想要生活的样子”容易读成生活方式，改为“把世界重塑成他们愿意生活的地方”；审校者建议的“他们愿意生活其中的样子”仍然别扭，没有照用。
  - “It imagines how AI and its development could be exactly the opposite. ... their training data contained and knowable”：改为“在它的设想里，AI 和 AI 的开发方式可以和现在恰恰相反”和“训练数据范围有限，内容也查得清楚”。审校者建议的“它让我们看到”和前一句“Te Hiku 让我们看到了另一条路”重复，所以换了说法。
  - “the collective product of millions of people across time”：“跨越时间的千百万人”是直译。审校者建议的“世世代代”上一段已经用过（“世世代代遭受了骇人的对待”），改为“千百万人在漫长岁月里共同创造的产物”。
  - 其余采纳的都是表达问题，照审校者的意思改：“按照……条款和服务”改为“接受……条款和服务”（with new restrictive terms and services）；“数据工作周围”改为“说到数据工作”（false logic around data work）；“AI 如何改变权力”改为“AI 让权力怎样转移”，“拉回民主”改为“拉回民主的方向”（how AI shifts power ... wrest us back toward democracy）；“都是重新分配权力可以做、也需要做的工作的例子”改为“都是例子，说明要重新分配权力，有哪些工作可以做，也需要做”；“甚至以为益处*真的会*从这种愿景中产生”改为“认为 AI 的广泛益处只能来自这样一种技术愿景，甚至认为这种愿景*真的会*带来这些益处”，补出“认为”的主语关系，斜体照旧；“又是其他产品早已接受评估”改为“情况也和前面一样：其他产品早就要接受评估，AI 产品却不用”（once again already submit to evaluations）；“一片新的地基”改为“一块新的基石，让后来的更多人站在上面奋起”（a new ground upon which many more after will rise up and build）；“直接外包雇用”改为“直接签约雇用”（directly contracted）；“绝不全面”改为“远远谈不上全面”，“新形式 AI”改为“新型 AI”（by no means comprehensive ... new forms of AI）；“风靡全球、让全世界为之着迷”改为“大受追捧、让全世界浮想联翩”（wildly popular demonstrations that captivate global imagination）。
- 对译者自检未决项的处理：
  - “生存威胁”后的括注（a fundamentally different conception of what is existential）：审校者认为括注把作者暗含的对比讲清楚了，编辑同意，保留。
  - “US representatives” 译“美国众议员”：审校者没有找到相反的证据，编辑同意，保留。
  - “欧林工程学院”“百度设在旧金山湾区的研究实验室”“对数据的硬性需求”“公众异议期”“科技巨头”：审校者认为可以，保留。
  - “空壳实体”：已按审校者意见改为“空壳公司”。
  - 原文疑点：按审校者建议补记一条，原文说毛利社群在 the early 1900s 的快速城市化中解体，毛利人大规模迁往城市一般认为在第二次世界大战以后。译文照原文写“20 世纪初”，详见上面“原文疑点”表。
- 审校者的总体判断：译文质量高，事实、数字、日期和金额全部准确，人名、脚注、注释粗体和出处都符合体例，正文没有破折号和“不是……而是……”句式，语气贴近样章。需要修改的是两处意思偏差、一处维森鲍姆引文和题词译文不一致、两处说法和前面章节不一致、“叙旧”用词不当，以及十来处翻译腔或搭配不当的句子；改完就可以进入中文通读。

## 3. 中文通读

- 执行者：编辑 agent（Opus 5.5）。
- 范围：采纳双语审校的修改之后，从章首读到章尾，检查连贯、重复、指代、人名和术语前后是否一致。人名都和 `review/terms/people-zh.tsv` 一致，每人第一次出现都括注了英文；术语和第 12、13 章及题词的说法一致。
- 发现并修改：3 处，每处都回查了英文。
  - “That data pool paled in comparison to the six hundred eighty thousand hours of audio that OpenAI ripped from around the web”：中文句子先讲 OpenAI 的 68 万小时，再说“这个数据池显得微不足道”，读者可能以为“这个数据池”指 OpenAI 的数据。改为“Te Hiku 的这个数据池”；注释 7 的粗体“这个数据池显得微不足道”仍然和正文对应。
  - “she paid them a standard researcher’s salary in Germany, where she is based”：“按她所在的德国的研究人员标准薪酬”连用两个“的”，读起来拗口。改为“按德国研究人员的标准薪酬付给他们报酬（她本人在德国工作）”。
  - “He was fielding various requests from global organizations”：“各个国际组织发来的各种请求”里“各个”和“各种”重复，改为“国际组织发来的各种请求”。
- 修改后检查：正文没有破折号，也没有“不是……而是……”句式；中文文件没有分隔线；`site.py status` 显示本章 40/40 块、22/22 条注释，中英逐块对应。

## 状态

双语审校的 20 条意见都已处理，中文通读的修改也已回查英文，没有未解决的意义问题。“US representatives” 译“美国众议员”是最常见的读法，审校者和编辑都同意保留，如果以后有材料说明来访者其实是美国政府派来的官员，再相应改动。原文疑点 3 条（注释 22 的逗号、注释 19 的 posted、正文第 2 段的城市化时间）都照原文翻译，记录在上面的表里。下一步是阅读器校样。

## 第三轮：GPT-6 Astra 独立审校

- 审校者：GPT-6 Astra，通过 Codex 运行，只读，和译者属于不同的模型家族。
- 发现：6 条。逐条找到中英文对应的句子，读过上下文后核实：成立并修改 5 条，不成立 1 条。其中 3 条按建议的方向修改，但措辞另行调整。
- 成立并修改：
  - Te Hiku 发起社群竞赛的一段，“three hundred ten hours of high-quality transcribed audio”：原译“310 小时高质量的转写音频”，“转写音频”可以读成动宾结构“把音频转写”，看不出这些音频已经配好文字。改为“310 小时配有文字转写的高质量音频”。审校者建议的“附有转写文本”意思相同，换成更口语的说法。
  - 亚历克斯·汉纳加入 DAIR 的一段，“one of the Google coauthors on the ‘Stochastic Parrots’ paper”：原译“‘随机鹦鹉’论文”。术语表写明这篇论文的中文标题是《论随机鹦鹉的危险》，第 10 章和第 12 章第一次提到它时都写作《论随机鹦鹉的危险》（“On the Dangers of Stochastic Parrots”），本章只提到这一次，也按每章第一次出现括注原题的规则处理。改为“论文《论随机鹦鹉的危险》（“On the Dangers of Stochastic Parrots”）的谷歌合著者之一”。
  - 奥金伊为“数据工作者调查”写的文章，“As the dust settles on this chapter”：原译“这一页尘埃落定之际”。chapter 在这里指 Remotasks 突然封号这段经历，中文说“翻过这一页”，却不说“这一页尘埃落定”，两个说法混在一起不通。改为“这场风波尘埃落定之际”，注释 16 开头的粗体同步改为“‘这场风波尘埃落定之际’”。
  - 瓦解帝国的公式那一段讲独立知识生产，“help us understand, rather than merely speculate about, the textured realities of the impact of these technologies”：原译“帮助我们真正了解这些技术带来的影响在现实中有哪些具体而复杂的面貌，不再只是凭空推测”，“影响……有哪些……面貌”层层套叠。改为“帮助我们切实了解这些技术在现实中造成了哪些具体而复杂的影响，不再只是凭空推测”。
  - 最后一段讲面向大众的教育，“about the worldviews and fallibility of the people and companies developing these technologies”：原译“了解开发这些技术的人和公司持有怎样的世界观，又会犯哪些错误”。fallibility 说的是这些人和公司也会犯错，原译读起来像要列出他们会犯的具体错误。审校者建议“也认识到他们同样可能犯错”，打断了这一句连用“了解”的排比。改为“了解开发这些技术的人和公司持有怎样的世界观，了解他们同样会犯错”。
- 不成立，保留原译：
  - 全书正文最后一句，“May it be a new ground upon which many more after will rise up and build.”：原译“愿它成为一块新的基石，让后来的更多人站在上面奋起，继续建造”。审校者认为“站在上面奋起，继续建造”搭配别扭，建议改为“愿这本书奠定新的基础，让更多后来者行动起来，继续推进这项事业”。原文本身就是“在地基上站起来、接着建造”的比喻，build 也没有宾语；rise up 在这本讲抵抗的书里同时有“起来反抗”的意思，“奋起”保留了这一层。建议的改法丢掉了比喻，又加进原文没有的“这项事业”。第二轮双语审校已经斟酌过这一句，保留原译。
- 对英文原文的疑问：审校者指出，注释 21 对应的萨莎·卢乔尼引语说汽车和家电都有 Energy Star 评级，但能源之星只用于家电、建筑等，不用于汽车；美国新车贴的是 EPA 的燃油经济性标签。我查了 energystar.gov 的标识使用规则（energystar.gov/partner-resources/brand-guidelines/recognition-marks），里面明确写着认证标识 “Do not use on cars, vans, or other vehicles”，审校者的说法成立。这是采访中的口头引语，可能是说话人随口把两种标签说成一种，译文照引语原样译出，不加译者注。上面原文疑点表里的三条记录不变。
- 按全书统一的写法修改：1 处。Doomerism 按统一写法改为“末日论”：拉吉谈现实危害的一段，“末日派所说的失控 AI 那种理论上的危害”改为“末日论所说的失控 AI 那种理论上的危害”。其余各项逐条核对过，不用改：数字都符合规则（“二十多年来”“十天之内”“五个数据标注平台”“两块 GPU”用汉字，“15 种”“15 名工人”“2500 人”“400 多人”“30 天”用阿拉伯数字，“1 到 5 美分”“每小时 25 欧元”是金额）；《原住民学校法》（*Native Schools Act*）第一次出现已括注斜体原题，和其他章节里法案的写法一致，《华尔街日报》《时代》不括注；注释里的人名都写英文；每人在本章第一次出现时都括注了英文，译名和 `review/terms/people-zh.tsv` 一致；本章没有出现 Twitter、inference、cochairman、communications team、corporate vice president、fellow 等其他几项。
- 核实与修改：agent（Opus 5.5）。改完后运行 `python3 scripts/site.py status empire-of-ai`，本章显示 40/40 个块、22/22 条注释，脚注标记与英文同号同序；正文仍然没有破折号，也没有“不是……而是……”句式，唯一的破折号在注释 22 照原文保留的论文标题里。
