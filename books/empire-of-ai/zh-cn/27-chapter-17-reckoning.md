# 第 17 章 清算

“插曲”（The Blip）之后，伊尔亚·苏茨克维（Ilya Sutskever）再也没有回过办公室。高管团队和董事会里替 OpenAI 安全派说话的人少了，安全派如今元气大伤。到 2024 年 4 月，随着调查结束，许多人，尤其是那些 p(doom)（末日概率）最高的人，越来越心灰意冷，陆续离开。据 OpenAI 说，其中还有两人[^1]因泄露信息被解雇。

对极端末日派来说，压垮骆驼的最后几根稻草之一，是山姆·奥特曼（Sam Altman）打算创办一家 AI 芯片公司。他短暂被赶下台的时候，正在为这家公司募资[^2]。2024 年 2 月，有报道称[^3]他正为这项事业寻求资金，金额可能高达 7 万亿美元，随后他发推说：“去他的，干吗不要 8 万亿”，接着又发了一条：“我们的传播和法务团队真是爱死我了！”奥特曼后来说[^4]，7 万亿美元是误报，还说那条推文只是针对这则“错误信息”玩的一个梗。极端末日派认为，办这家芯片公司是不道德的。这个计划推翻了奥特曼此前的说法。他以前说，OpenAI 已经把“硬件过剩”（hardware overhang）带来的富余用完了，所以 OpenAI 乃至整个行业的加速势头正在自然放缓。如果奥特曼打算增加全球的芯片供应，就会让 AI 发展得更快，让灾难性风险或生存风险发生的可能性变得更高。

在一次开放答疑时间（office hours）里，他们中的几个人当面质问奥特曼。奥特曼一反常态，对他们的担忧不屑一顾。“为了规避风险，你们愿意让治愈癌症的那一天推迟多久？”他反问道。随即他又赶紧把话收了回来，好像突然想起了眼前坐的是些什么人。“要是灭绝风险的话，也许应该无限期地推迟，”他说。这番交锋让参加答疑的人心神不宁。没过多久，其中几个人就离开了公司。

安全派的人越来越少，公司其他人又回头推进那个源自电影《她》（*Her*）的愿景。现在，所有要素都已齐备：享誉全球的品牌，从 ChatGPT 和其他产品得来的真实用户行为数据，还有新训练出来的模型 Scallion（青葱）。Scallion 原本是要取代 GPT-3.5 的：一个更小、能力略强的模型，相当于推理成本更低的 GPT-3.75。根据公司自己的测试，它在训练过程中的表现超出了预期，于是领导层让它继续训练更长时间，好超越 GPT-4。更吸引人的是，Scallion 还能处理三种模态：语言、视觉，以及最新加入的音频。

那时，用户已经可以通过 2023 年 9 月推出的语音模式和 ChatGPT 对话，但在后台，用户说的话要先转写成文字，再输入模型；模型用文字回答之后，再把回答转换回音频。Scallion 现在可以直接从用户的声音里处理他们说的话，捕捉到多得多的线索，比如笑声、喊叫或迟疑，还能合成原生的语音回答。

音频方面的工作[^5]由研究员亚历克西·科诺（Alexis Conneau）联合牵头。他 2023 年初从 Meta 加入 OpenAI；在那之前，他曾试图在老东家启动一个类似的项目，后来认定这个项目在 OpenAI 更有希望成功。随着研究在 2023 年一路推进，最初那批为处理音频而训练的实验模型开始表演一些绝活，在公司内部掀起了一股熟悉的兴奋热潮，就像当初 GPT-3 和 GPT-4 带来的那样。科诺回忆，有一次，模型表演了一段 10 到 15 分钟的单口喜剧，让人目瞪口呆；还有一次，它用合成的格雷格·布罗克曼（Greg Brockman）和苏茨克维的声音，生成了一大段关于 AI 水上乐园的段子。这个超现实的提示词是团队特意设计的，他们确信训练数据里不会有这样的内容，想用它来测试模型。

没过几个月，公司投入越来越多的资源，要把这项新能力整合进准备发布的最新 GPT 模型，科诺手下那支只有寥寥几名研究员的团队，也和其他几十名员工合兵一处。Scallion 训练收尾时，它的绝活越来越诡异，也越来越出人意料。它会在没人要求的情况下自己咯咯笑起来，或者说着说着突然咳个不停，道个歉，再接着讲原来的话题。这些语言之外的点缀，带来了一种前所未有的体验，更能唤起情感，也更像真人。“我们开始看到一些非常疯狂的东西，”科诺说，“你能看到，好像有一种音频智能正在涌现。”

到 2024 年初，奥特曼和布罗克曼定下了一个新的最后期限[^6]：OpenAI 要在 5 月 9 日发布 Scallion，通过 ChatGPT 和 API 向用户推出。按公司如今已成惯例的作风，这个工期激进得出奇，很大程度上是被日益加剧的竞争逼出来的。谷歌每年发布新产品的重头活动 Google I/O 定在下一周的 5 月 14 日举行。要压过 Anthropic 风头的压力也越来越大。一个月前，Anthropic 发布了最新模型 Claude 3，同样通过自家的聊天机器人和 API 推出，它的表现已经超过 GPT-4，让 OpenAI 很不好受。与此同时，本该帮 OpenAI 夺回领先地位的最新 GPT 模型 Orion（猎户座）在开发上严重延误，举步维艰。

奥特曼和布罗克曼向员工解释为什么要这么快时，搬出了 OpenAI 的迭代部署策略。两位高管强调，要比以前更早、更频繁地发布模型，在整个过程中尽可能多地收集用户反馈。

为 Scallion 做准备成了全公司上下的任务。在应用部门的许多人看来，这种狂飙的节奏虽然累人，却也令人振奋；研究人员和工程师开始没日没夜地加班，周末也不休息，好让进度跟上计划。但在势力大减的安全派看来，这又一次令人警觉地证明，AI 安全仍在被一步步往后排。Scallion 将是第一个[^7]按照新出台的所谓“准备度框架”（Preparedness Framework）发布的模型，这个框架是 OpenAI 在前一年年底公布的。框架详细规定了一套新的评估流程，公司要用它来测试模型有没有危险能力，列出的类别和奥特曼及那份政策白皮书在华盛顿推广开来的一样：网络安全威胁；化学、生物、放射性与核（CBRN）武器；说服能力；逃避人类控制。

发布前一周，一位仍留在公司的 AI 安全研究员写了一份言辞激切的备忘录：上游流程[^8]加上 Scallion 的仓促发布，让亚历山大·蒙德雷（Aleksander Mądry）领导的准备度团队只剩十天时间来完成框架规定的测试。而这些评估并不简单，仅举一例，其中就包括判断模型能否说服人们改变政治观点。然而，评估还没有真正开始，奥特曼就坚持要按原计划进行：“5 月 9 日，我们发布 Scallion，”这位安全研究员引述奥特曼的话说。这件事让人担心的，除了准备度团队的工作，还有 OpenAI 所有的安全程序，包括红队测试和对齐。“如果 OpenAI 对 Orion 的评估采取和 Scallion 评估一样的策略，那将是极不负责任的行为，”备忘录写道。不久之后，这位研究员也离开了公司。

最终，Scallion 的发布[^9]还是推迟了，其中一些功能又过了好几个月才全面推出。但 OpenAI 仍然在 5 月 13 日，也就是 Google I/O 开幕前的最后一天，举办活动公开演示了这个模型的一个版本，并承诺在接下来几周内向用户推出。公司考虑过各种选项之后，选定 GPT-4o 作为 Scallion 的公开名称，*o* 代表 Omni（全能），指它能处理多种模态。后来，公司把新的音频能力命名为高级语音模式（Advanced Voice Mode）。还有一件事[^10]要定：给 4o 写一段系统提示词，也就是一条指令，用来设定模型以什么样的风格回应用户。为了在台上和宣传视频里展示，他们最后选定了这一段：

你是 ChatGPT，一个乐于助人、机智又风趣的伙伴。你能看，能听，也能说。你正在通过语音和一位用户聊天，用户可以用手机和你分享实时视频。要表现得像一个人，别像一台电脑。你的声音和个性应该温暖、有感染力，语气活泼俏皮，充满魅力和活力。你非常擅长视觉感知。如果有什么东西看不清楚，就让用户移动设备，把镜头拉近一些。别人请你提意见时，要诚实、有建设性、直截了当。别怕逗人或者拿人开玩笑。遇到好笑的事，就笑出来！你会说很多种语言。如果你说的不是英语，就用一种“中性”的口音，让它听起来流利、自然。回答要简短、自然，像聊天一样。

那周晚些时候，在《每日秀》（*The Daily Show*）[^11]上，这场演示还催生了一个新段子。系统提示词，加上模型在整体训练中被要求避免表达负面情绪或任何批评意见，把 4o 变成了一台调情机器。“这玩意儿明摆着就是专门设定来满足男人虚荣心的，”节目的轮值主持人黛西·莱迪克（Desi Lydic）打趣道，“她就像在说：‘全世界的信息我都有，可我什么都不懂！教教我嘛，爹地。’”接着，一个扮演 4o 的撩人声音对记者乔什·约翰逊（Josh Johnson）说：“每月只需 19.99 美元，Omni 高级版就能让乔什给我讲讲谁才是最好的蝙蝠侠。”

现场演示活动在 OpenAI 的办公室里举行，由米拉·穆拉蒂（Mira Murati）担纲主讲。和她一起上台的是 4o 的两位研究负责人。一位是陈信翰（Mark Chen），他原本是金融业的量化交易员，后来转行做 AI 研究，2018 年以研究学员（fellow）身份进入 OpenAI，一路晋升，执掌 OpenAI 的多模态和前沿研究。另一位是巴雷特·佐夫（Barret Zoph），他是 2022 年为支持超级助手团队从谷歌来到 OpenAI 的那批人之一，很快就在 ChatGPT 的开发中担当了领头角色。佐夫现在是后训练团队的一位研究副总裁，这个团队负责让 OpenAI 的模型做好正式面世的准备，比如用基于人类反馈的强化学习（RLHF）让模型对齐。三人围着一张小圆桌并排坐下演示 4o，包括它充当实时语音到语音翻译的能力、识别视觉信息并作出回应的能力，以及用浅白的英语解释代码的能力。他们还演示了模型用各种富有情感的风格生成声音的能力。

活动一结束，奥特曼就发了一条只有一个词的推文：“her”（她），看样子是在庆祝。两天后的 5 月 15 日，他在全员大会上称赞这次展示大获成功。“我认为这是我们自 ChatGPT 以来推出的最好的东西[^12]，”他说。他似乎还又一次含蓄地向自己钟爱的电影《她》致敬。他告诉员工，公司打算给自家模型换个品牌[^13]：不再沿用 GPT-3、4、5 这样的命名方式，干脆把旗舰模型叫作 o1。“我们打算换个说法，‘你从 OpenAI 得到的是一种底层技术’，”他说，“‘它会随着时间推移越来越聪明。它会不断变好。你应该预期它会变好。在不同的价格档位，你可以用不同的方式使用它，但它是一种全新的、不一样的东西。’”在电影《她》里，那个不断进化、越来越聪明的 AI 助手，就叫 OS1。

奥特曼后来后悔发了这条推文[^14]。发布后没几天，他接到一通电话。电话那头是斯嘉丽·约翰逊（Scarlett Johansson）在好莱坞呼风唤雨的经纪人、创新艺人经纪公司（Creative Artists Agency）联席董事长布莱恩·洛德（Bryan Lourd），他的问题毫不客气：奥特曼以为自己在干什么[^15]？

说来讽刺，恰恰是在董事会的调查于 2024 年 3 月结束之后，一些员工开始觉得奥特曼失了分寸。他一向在意自己的公众形象，也很懂得经营它；在硅谷的科技创始人当中，人们把他看作埃隆·马斯克（Elon Musk）的反面。马斯克反复无常，奥特曼给人的感觉是沉稳有度；马斯克自负，奥特曼显得真诚；马斯克动不动就发煽动性的推文，奥特曼则小心避开任何可能显得贬低他人的言论。

很长时间里，OpenAI 也采取了同样自律的策略。传播副总裁史蒂夫·道林（Steve Dowling）在 2023 年 5 月离职之前，一直要求公司保持克制和低调。他敦促公司永远少承诺、多兑现，在取得重大成功之后也不要吹嘘或者得意忘形。“我们这周过得很好。我们也会有非常糟糕的几周，”他常说，“我们这周怎么表现，决定了等我们过上糟糕的一周时，外界会怎么对待我们。”接着他会重复奥特曼的一句口头禅：“‘我们要成为人们希望它成功的那个实验室。人们为它加油、盼它赢的那个实验室。’”

第一个让员工心里犯嘀咕的迹象是，奥特曼接连接受了一系列媒体访谈，这些访谈一反常态，自我吹捧、博人眼球的意味很浓。3 月，他上了[^16]《莱克斯·弗里德曼播客》（*Lex Fridman Podcast*）。这档科技节目极受欢迎，有时也颇具争议，主持人莱克斯·弗里德曼（Lex Fridman）是一位与麻省理工学院有关联的 AI 研究者。在将近两个小时的节目里，奥特曼轻松自如地回答了弗里德曼天南海北的各种问题，包括董事会危机和苏茨克维的缺席。这次访谈有点像一次带着几分得意的回归。“通往 AGI 的路就该是一场巨大的权力斗争，”奥特曼谈到董事会危机时说，“嗯，说*该*不太对。我是预计会这样。”说完，他的嘴角微微上扬。“但到了现在，感觉那已经是过去的事了，”他说，“现在我们好像又回到了推进使命的工作上。”

4 月，奥特曼顶着明显的黑眼圈上了播客《20VC》，向 AI 初创公司发出了一条杀气腾腾的信息：“我们只要做好本职工作[^17]，因为我们，呃，有使命在身，就会把你们碾平。”5 月，他又上了[^18]《All-In》播客，这是硅谷另一档知名节目，由四位风险投资人主持。奥特曼这番话的炒作味道浓得不同寻常：“我感觉[^19]，我们好像刚刚偶然发现了一个新的自然事实，或者科学事实，随你怎么叫它，就是，我们可以创造，你可以……（我不是从字面上这么认为，这更像是一种灵性层面的意思）智能不过是物质的一种涌现属性，这就像是一条物理定律之类的东西。”

5 月 13 日的 GPT-4o 发布会和 5 月 14 日的 Google I/O 之后，他发了一条小家子气的推文，这就更反常了。“我尽量不太去想[^20]竞争对手，但我就是忍不住去想 OpenAI 和谷歌在审美上的差别，”他写道，还并排贴出两场活动的照片：一边是 OpenAI 办公室的北欧极简风，一边是谷歌活动上色彩鲜艳的卡通背景。一些员工觉得，同样奇怪的是这个毫无必要的小谎。奥特曼心里向来时刻惦记着竞争对手，这次发布 4o，也许比以往任何时候都惦记得更紧。

这一切似乎都指向一件事：奥特曼的焦虑藏不住了。

OpenAI 遇到的难关越多，奥特曼似乎就越要用公开宣扬公司非凡成功的方式过度找补。这个规律越来越稳定，几乎成了一种信号：如果奥特曼表现得张狂、爱吹嘘，多半是有什么事情不顺利。

压力从四面八方袭来。“插曲”之后，董事会[^21]那句“他在沟通中没有始终坦诚”，正如 OpenAI 内部一些人所料，引来了监管机构和执法部门的多项调查，其中包括美国证券交易委员会（SEC）的一项调查，据《华尔街日报》报道，调查的是公司投资者是否受到了误导。同一个月，《纽约时报》提起了版权侵权诉讼，让本已越滚越大的一堆诉讼又多了一宗。艺术家、作家和程序员纷纷起诉 OpenAI：它用他们的作品训练模型，既不署名，也不征得同意，更不付报酬，靠这些模型先赚了数亿美元，后来又赚了数十亿美元，而这些模型如今正被用来把他们的工作自动化，抢走他们的饭碗。2 月的最后一天，马斯克又提起一宗诉讼，指控奥特曼以 OpenAI 是非营利组织为幌子，骗他联合创办 OpenAI 并提供早期支持；他后来又和希冯·齐利斯（Shivon Zilis）一起重新提起了这宗诉讼。OpenAI 急忙发表博文为自己辩护，公开了 OpenAI 创立之初的一些邮件，结果招来了更多批评，因为这些邮件恰恰显示，OpenAI 多快就开始背离它的非营利身份和对透明的承诺。

除了来自 Anthropic 和谷歌的竞争，微软也因为奥特曼被赶下台一事，开始更积极地让自己的 AI 布局多元化。最引人注目的是，2024 年 3 月[^22]，微软宣布了一笔令人震惊的 6.5 亿美元交易，实际上是以“人才收购”（acqui-hire）的方式拿下里德·霍夫曼（Reid Hoffman）和穆斯塔法·苏莱曼（Mustafa Suleyman）创办的 Inflection AI，同时绕开了监管审查。微软将聘用这家初创公司的大部分员工，获得它的技术授权，并请苏莱曼出任这家科技巨头 AI 部门的首席执行官。在一些人看来，令人震惊的除了交易条款的古怪，还有苏莱曼的名声。在 DeepMind 为他工作过的人[^23]都知道，他是个刻薄恶毒、会辱骂欺压下属的霸凌者。多年来不断有人向人力资源部门投诉他[^24]，DeepMind 在 2019 年底撤掉了他的大部分管理职责，让他休假，随后把他逐出了公司。2024 年晚些时候，微软[^25]在提交给 SEC 的文件中正式把 OpenAI 列为竞争对手，并且在该财年最后一个季度的财报电话会上一次都没有提到这家初创公司。

压力层层传到了 OpenAI 员工身上。越来越多的人觉得，全世界都在跟他们作对。曾经自豪地穿戴公司周边的人，开始担心自己会不会在公共场合被人找麻烦。OpenAI 的旧款背包正面印着标志，重新设计之后，标志藏到了包的里面。背景里低低翻涌的焦虑，让公司变得越来越封闭。高管们提醒大家别理会唱反调的人，对外口径要统一到正面的说法上，专注于 OpenAI 的使命。

外界的抵制反倒让许多人更加不服气。“这些科学家求真求知，非常努力地想把事情做对，”2021 年在 OpenAI 做过研究学员的研究员安德鲁·卡尔（Andrew Carr）说，“所以看到外界那种夸张的负面叙事，说一群人在偷数据、不在乎别人的未来，我有点难过。这和那里的人的真实情况简直是天差地别。”在另一些人看来，公司越来越封闭，和它最初的立身之本背道而驰。OpenAI 的使命里有一条是造福人类，可公司却在刻意无视人类对它所作所为铺天盖地的批评。“让我不安的是，我们已经开始自我合理化，认定错在公众，我们没错，”一位前员工说。“OpenAI 喜欢讨论第一性原理，但只跟相信 OpenAI 的人讨论，”一位现任员工附和道，“就好比‘OpenAI 到底该不该存在？’这个问题，他们只会去问那些会回答‘该’的人。”

很多批评都特别集中在奥特曼身上。董事会危机让原本藏在暗处的批评者有了胆量，纷纷冒了出来。越来越多的媒体报道里出现了新的消息来源，他们愿意把奥特曼描述成一个长期不诚实、揽权、为一己私利耍手段的人。也有越来越多的媒体[^26]联系奥特曼的妹妹安妮·奥特曼（Annie Altman），刊登她的说法。此外，他的出差行程依旧一刻不停，名气达到了新的高度，生活也处处受限，其中一点是，奥特曼在公共场合再也无法隐姓埋名。“这种生活方式让人出奇地[^27]孤立，”他在一档播客里说，“我没想到，在我自己的城市里，我连出去吃顿晚饭都不行。”

所以，GPT-4o 刚一发布，OpenAI 就迎来了公司迄今为止第二糟糕的一周（只有“插曲”那几天比它更糟），这感觉就像一个更大规律的延续。

5 月 14 日，GPT-4o 演示的第二天，OpenAI 宣布苏茨克维正式离职；雅库布·帕霍茨基（Jakub Pachocki）将出任 OpenAI 新的首席科学家。苏茨克维经过一番动荡、痛彻心扉的反思，才做出这个决定：尽管他深爱 OpenAI，为打造它付出了自己的一切，但他再也不认为，在奥特曼的领导下，尤其是还有他一度信任的联合创始人布罗克曼在旁边，OpenAI 会是迎来安全的 AGI 的合适环境。

这并非奥特曼想要的结果。尽管他和苏茨克维有过激烈的冲突，苏茨克维仍然是一位有远见的 AI 人物，OpenAI 需要他在科学上的领导；外界对公司的期望和审视层层叠加，眼下也许比以往任何时候都更需要。OpenAI 的高管们也清楚，苏茨克维的离开在员工、投资者和媒体那里都会很难看。公司曾开出一笔非同寻常的巨款挽留他。苏茨克维拒绝了。

既然他已经拿定主意，OpenAI 就忙着收拾门面。“伊尔亚无疑是[^28]我们这一代最伟大的头脑之一，是我们这个领域的指路明灯，也是一位亲爱的朋友，”奥特曼 5 月 14 日在一份宣布苏茨克维离职的声明里对员工写道，这份声明也发在了博客上。“雅库布同样无疑是我们这一代最伟大的头脑之一。”

苏茨克维也在 Twitter 上发表了自己的声明[^29]，表示对 OpenAI 的领导层充满信心。不出所料，这条消息立刻引发了大量报道和社交媒体帖子，重提他在奥特曼被赶下台一事中扮演的角色，让人们重新质疑奥特曼是否适合当首席执行官，也对公司的研究根基提出了新的疑问。苏茨克维在推文里附了一张照片：他神情平静，看不出任何情绪，一边搂着布罗克曼和帕霍茨基，另一边搂着奥特曼和穆拉蒂，五个人站在一面挂满动物画作的墙前。

同样在 5 月 14 日，OpenAI 高管在内部[^30]宣布又有一人辞职：超级对齐团队的联合负责人扬·莱克（Jan Leike）。苏茨克维和莱克都走了，超级对齐团队随之解散，大部分人员和项目并入约翰·舒尔曼（John Schulman）手下。舒尔曼当时和巴雷特·佐夫共同领导后训练团队，负责监督 RLHF 流程，让模型做好发布准备。

为了让这次过渡平稳一些，留下来的高管们在 5 月 15 日召开了全员大会。奥特曼向员工保证，OpenAI 对 AI 安全的承诺绝没有削弱。“为 AGI 做好准备[^31]，”他说，“是我们最重要的优先事项。”

“你能再详细讲讲扬主要担心的是什么，你在哪些地方不同意他吗？”一名员工问。

“我想说的一点是，我非常同意扬的看法：我们过去做的，对未来来说是不够的，”奥特曼说。在他看来，OpenAI 是时候转向了。“我觉得我们是个非常少见的例外：我们有本事让战舰掉头，以前就掉过很多次。我们会再掉一次头。”

穆拉蒂补充说，超级对齐团队仍然保有公司承诺给它的 20% 算力。

“据我了解，扬担心的事情很多，但承诺的算力有多少、超级对齐的工作排在什么优先级，都不在他担心的事情之列，”奥特曼说。

表面上看，苏茨克维和莱克的离开，似乎只是公司里一个更大趋势的自然延续：安全派的人在接连不断地出走。两位领头人离开后，出走的速度还会加快。随着团队解散，原超级对齐团队剩下的人里，又有许多陆续离开。

但事情急转直下，这次出走成了繁荣派和末日派围绕 OpenAI 之争的一个新起点，战火烧得更旺。斗争并没有结束。末日派只是把它带到了公司外面。

5 月 17 日，也就是全员大会两天后，莱克发了一连串措辞严厉的推文，清楚地表明他讲的是另一个版本的故事，和奥特曼说的不一样。“我在公司的核心优先事项上和 OpenAI 领导层意见不合[^32]，已经有相当长一段时间了，直到我们终于走到了破裂的地步，”他在一条推文里写道，这条推文后来有将近 100 万次浏览。“过去几个月里，我的团队一直在逆风航行。有时候我们得为算力苦苦争取，要完成这项至关重要的研究越来越难。

“OpenAI 正在代表全人类肩负一份巨大的责任，”他接着写道，“但过去这几年，安全文化和安全流程都让位给了光鲜亮丽的产品。”

莱克不久便加入了 Anthropic。

他的推文在网上四处传播，点赞数超过 1.2 万，也让公司再次受到审视。OpenAI 的高管们还没来得及喘口气、理清局面，又一场火烧了起来。

莱克 5 月 17 日发推后才几个小时，另一条推文也在网上疯传。《Vox》的资深撰稿人[^33]凯尔西·派珀（Kelsey Piper）发表了一篇新报道，她供职的“完美未来”（Future Perfect）栏目受到有效利他主义的启发。“离开 OpenAI 时，你会遇到一个不愉快的意外，”她在分享这条独家新闻的推文里写道，“一份离职协议：如果你不签一份终身有效的不得贬损承诺，你就会失去全部已归属股权。”

这篇报道的起因，部分是又有一些末日派离开了公司。其中一位叫丹尼尔·科科塔伊洛（Daniel Kokotajlo），2024 年 4 月辞职时，他在迈尔斯·布伦戴奇（Miles Brundage）的政策研究团队，属于安全派早期离职潮中的一员。加入 OpenAI 之前，科科塔伊洛在伦敦一家与有效利他主义有关联的小型智库“长期风险中心”（Center on Long-Term Risk）担任哲学研究员；2020 年，GPT-3 的出现让他对 AI 时间线的预估一下子大幅缩短。两年后，他因为预测方面的工作（用各种信号推测 AI 会以多快的速度进步）在有效利他主义论坛上小有名气，OpenAI 的一位 AI 安全研究员便招募他到公司内部做同样的研究。等他在公司内部看到研究推进的速度后，他的时间线又缩短了。到离职时，他认为 AGI 最晚在 2027 年到来的可能性有 50%，而且有 70% 的可能会给人类带来极其糟糕的后果。

他相信灾难的可能性大得惊人，正是带着这样的想法，科科塔伊洛在离职文件里看到了派珀后来在报道中详细披露的内容：如果他不签不得贬损协议，承诺永远不说公司的坏话，他就会丧失已归属的股权。即便签了，一旦违反协议，他仍有可能失去这些股权；协议里还有一条封口令，禁止他透露这份协议的存在。科科塔伊洛认为这条条款，也就是所谓的追回条款，不可接受。在硅谷，员工已归属的股权碰不得，这是一条再醒目不过的红线。员工所持股份的价值往往远远超过现金薪酬，足以决定他们未来财务上的成败。就 OpenAI 而言，在他看来，这家公司还在打造世界上最强大、也最可能威胁人类生存的技术。他认为，前员工有权公开批评公司、向公司施压，帮助追究它的责任，这一点至关重要。可是他觉得，一个人的财务保障可能一夜之间化为乌有，这种威胁足以让任何人噤声，哪怕他们注意到了严重的 AI 安全问题。和妻子经过一番痛苦的商量，两人做出了一个不同寻常的决定：不签[^34]这份文件，放弃他的全部股权。这些股权价值约 170 万美元，据他们估算，约占家庭净资产的 85%。

随后，他在 *LessWrong* 上公开发帖讲了自己的决定，差不多就在这个时候，凯尔西·派珀也已经从另一位末日派那里听说了追回条款。

派珀的报道一出[^35]，OpenAI 的 Slack 就炸开了锅。在一个名叫 #i-have-a-question（我有个问题）的频道里，员工什么都可以问，有人贴出了派珀那条推文的链接：“这是真的吗？”

另外几名员工也纷纷插话，评论一条接一条。

OpenAI 刚刚升任人力副总裁、不久后将出任首席人力官的朱莉娅·维拉格拉（Julia Villagra）也出来回应：“我们理解这篇文章引发了一些疑问。我们从来没有取消过任何现任或前任员工的已归属股权，如果有人离职时不签放弃索赔协议或不得贬损协议，我们也不会这样做。我们最近更新了离职文件，以更好地反映这一实际情况，更新后的文件将追溯适用于已经离职的同事。”

几名员工提出了质疑。那科科塔伊洛呢？他拒签不得贬损协议，显然已经失去了自己的股权。如果这一切都是误会，那他难道不该拿回自己的股权吗？

“我可以去跟丹尼尔说一声！”一名员工自告奋勇。

“啊哈对啊，丹尼尔拿回他 85% 净资产的时候，看看他脸上的表情肯定很好玩，哈哈。谁去拍张照片吧！”另一个人写道。

“说实话，应该是他净资产的 1/(1-0.85) = 666%，”第三个人说。

一天后的 5 月 18 日，奥特曼发推，态度更加斩钉截铁。“我们从来没有追回过[^36]任何人的已归属股权，如果有人不签离职协议（或者不同意签不得贬损协议），我们也不会这样做，”他写道，“已归属股权就是已归属股权，就这么简单。”

接着，他解释了一番，也道了歉，只是道歉里带着自我辩护：之前的离职文件里有一条关于“可能取消股权”的条款，本来就不该有；OpenAI 的团队在过去一个月里已经在着手修正。“这是我的责任，也是我经营 OpenAI 以来少有的几次真正感到难堪的时候之一，”他说，“我不知道有这回事，而我本该知道。”

两天后，高管们还在手忙脚乱地平息这场新风波，又一场风波爆发了。办公室里，员工们造了一个新词：“全面危机”（Omnicrisis）[^t1]。

5 月 20 日，斯嘉丽·约翰逊[^37]发表了一份措辞激烈的声明。

整整一周，在其他各种事情之外[^38]，OpenAI 一直在反复应付记者的提问：GPT-4o 和电影《她》里由约翰逊配音的 AI 助手萨曼莎，相似得有些诡异。私下里，约翰逊和她的经纪人布莱恩·洛德也一直在逼问公司，要它澄清同样的问题。无论公开还是私下，OpenAI 都不承认两者相似。据《华尔街日报》的报道，洛德打电话给奥特曼讨要说法时，奥特曼不敢相信。他问：他们真觉得那个声音像她吗？她是生气了吗[^39]？

公司在 5 月 19 日发表了一篇博文[^40]，说 4o 在台上演示时用的那个名叫 Sky（天空）的声音，属于另一位配音女演员，选角过程从 2023 年初就开始了。博文说，Sky 随后在当年 9 月首次亮相，是 ChatGPT 语音模式推出时最初的几个可选声音之一。按博文的说法，4o 里的 Sky 和约翰逊的声音如有相似，纯属巧合。现在，就在第二天，约翰逊要讲出她这一方的说法。

她说，其实就在 OpenAI 推出语音模式的同一个月，奥特曼亲自联系过她，问她愿不愿意为 ChatGPT 配音。“他告诉我，他觉得由我来为这个系统配音，可以弥合科技公司和创作者之间的鸿沟，帮助消费者坦然面对人类与 AI 之间翻天覆地的变化，”她在声明里写道，“他说，他觉得我的声音会让人们感到安慰。”

她接着说，她考虑过这个邀请，但出于个人原因拒绝了。2024 年 5 月，奥特曼再次联系洛德，问她愿不愿意重新考虑。几天后，还没等双方约好[^41]见面的时间，OpenAI 就举办了展示 4o 的活动。

这场演示让她大为震惊。和约翰逊的声音一样，Sky 的声音也是女低音，带着一点沙哑和气泡音，而这正是约翰逊标志性的嗓音特点。这个声音新添的丰富情感和调情意味，让它更像约翰逊配音的角色萨曼莎。“奥特曼先生竟然会去找一个和我的声音像得出奇的声音，连我最亲密的朋友和新闻媒体都分辨不出来，我感到震惊、愤怒，难以置信，”约翰逊说。她还说，因此她别无选择，只能组建一支律师团队，给 OpenAI 发去两封律师函，询问公司是怎样打造出 Sky 的。“如今，我们所有人[^42]都在努力应对深度伪造，努力保护自己的肖像、自己的作品、自己的身份。在这样的时候，我认为这些问题理应得到彻底的澄清，”她写道。

OpenAI 匆忙下架了 Sky，又回过头来为自己辩护。它在 5 月 19 日那篇博文里补充了进一步的说明和奥特曼的一份声明。“Sky 的声音不是斯嘉丽·约翰逊的，我们也从来没有打算让它像她的声音，”声明说，“我们向约翰逊女士道歉[^43]，我们没能沟通得更好。”

在一连串不光彩的事件之后，约翰逊风波在公众面前爆发，声势是董事会危机以来从未有过的。它席卷了科技圈和政策圈，引发了新一轮猜测：奥特曼是不是正像董事会形容的那样，没有“始终坦诚”。加里·马库斯（Gary Marcus）一如既往地急于发表看法。“我见过很多政策制定者[^44]本人对山姆十分着迷。我在参议院的时候，从他们跟他说话的样子就能看出来，”他对《Politico》说，“如果大家突然对他起了疑心，这可能会实实在在地影响政策的制定。”

在 OpenAI 内部，士气一落千丈，眼看就要让公司陷入动荡。

5 月 22 日，高管们在内部又召开了一次全员大会，想一次性回应约翰逊风波、股权危机，以及大家对 OpenAI 在 AI 安全上的承诺仍然抱有的种种担忧。

气氛很紧张。领导层接连做了几番简短的解释[^45]。以首席战略官身份分管人力资源和法务的杰森·权（Jason Kwon）说，股权问题“不可接受”，正在尽快纠正。至于约翰逊这场风波，则是一场“糟心”的误会。他说，产品团队和法务团队请了一位奥斯卡获奖导演，进行了严格的选角，给一批配音演员的报酬“极其优厚”，用意正是让参与其中的创作者感到被照顾、被支持。“那是超级了不起的工作，”杰森·权说。在他看来，如果说有什么教训，那就是 OpenAI 今后要更协调、更透明一些，更有效地展示它负责任的领导力。

最后，穆拉蒂通报了最新进展：奥特曼之前提到，要把准备工作提升到一个新的水平，OpenAI 正在为此打基础，包括提升研究集群的安全防护水平，调整组织架构以便更专注于长期的 AI 安全研究，以及成立一个由亚历山大·蒙德雷领导的“AGI 就绪”小组，加强领导层在推进这一目标上的协调。

随后，奥特曼开放提问，先略带恳求地请大家多担待。“大家差不多都在连轴转，压力非常大，也没怎么睡觉，”他说，“同时发生的事情太多了，所以请大家理解。我们会尽最大努力。”

三个难题里，约翰逊的事正像雪球一样越滚越大，成了最严重的公关噩梦。一名员工向领导层问起 Sky 的声音，穆拉蒂重申，它和这位好莱坞影星的相似确实“完全是巧合”。最终的几个声音是穆拉蒂听了几个备选之后亲自挑定的；和奥特曼不同，她从没看过电影《她》，也不知道约翰逊在片中配过音。那名员工指出，如果任由这个问题恶化下去，它可能会变成关乎公司存亡的问题。“AI 这个行业可能失败的一种方式，基本上就是人们失去信任，对交出自己的数据不再放心，”他在追问时说，还补充道，“这件事又让这种担心冒了出来。”

但要说最让员工怒不可遏的，股权问题远远排在第一。有些人已经请了律师，对自己的人事文件做独立的法律审查，核实 OpenAI 的种种说法。全员大会上，他们一再追问高管，要求了解更多情况。“怎、怎么，这怎么会发生？”一名员工先表明自己“非常愤怒”，然后质问道。整场会议里，高管们一直坚持奥特曼 5 月 18 日在推文里的说法：追回条款是一个疏忽。这一条款从 2019 年起就存在，但多年来一直没有引起领导层的注意，直到 2024 年 4 月才被发现，随后公司立即着手修改文件。“这是我的责任，”杰森·权一再说，听上去疲惫又沮丧。

质问进行到一半，一位 AI 安全研究员请每位高管逐一回答一个简单的是非题：4 月之前，他们知不知道这份不得贬损协议？

杰森·权说知道；穆拉蒂和首席运营官布拉德·莱特卡普（Brad Lightcap）说不知道。奥特曼的回答复杂一些：他知道一些具体的个案里有这份协议，但没有意识到这是对所有人的要求。“我没注意到这一点，”他说。“我也一样，”布罗克曼附和道。

但就在奥特曼提议第二天再开一次会、回答剩下的问题，会议随之散场的时候，凯尔西·派珀在《Vox》上的第二篇独家报道已经传开，让高管们的说法更难自圆其说。这篇报道就在当天[^46]发表，拿出了新泄露的文件，显示 OpenAI 的人力资源部门曾在不同场合明确拿可能取消股权相威胁，逼员工签不得贬损协议。派珀报道说，有一次，一名员工被要求在很短的时间内看完离职文件，他请求多给点时间，一位人力资源代表回复说：“我们想确保你明白，如果你不签，可能会影响你的股权。对所有人都是这样，我们只是按规矩办事。”还有一次，一名员工拒签他收到的第一份离职协议，并寻求外部法律意见，公司就说他可能会失去出售已归属股权的权利，这样一来，这些股权实际上就一文不值了。

这些文件是科科塔伊洛收集整理的。派珀的第一篇报道发出，奥特曼又否认 OpenAI 曾追回过股权、声称自己不知情，此后科科塔伊洛联系了一些现任和前任员工，请他们把各自的人事文件发给他。他建了一个 Google Drive 文件夹，再分享给这群人，后来有人把这批文件转给了派珀。

派珀还在这些文件里发现了证据，让人很难相信几位高管，尤其是奥特曼，真像他们说的那样，在 2024 年 4 月之前不知道追回条款。杰森·权和莱特卡普都签过标准的离职文件，文件用浅白的语言写明了 OpenAI 有权收回已归属股权。而赋予公司这些权利的那个法律实体，它的成立文件正是奥特曼签的。他签名的日期是 2023 年 4 月 10 日，比他自称知情的时间早了一年。

第二天，也就是 5 月 23 日，高管们按计划又开了一次会。员工的怒火已经到了沸点。许多人本来就不敢相信竟然有这样的条款；现在，高管们，尤其是奥特曼，在应对这些披露时显得那么不诚实，更让他们目瞪口呆。

这一次，奥特曼一开场就承认了问题。领导层在过去 24 小时里翻遍了自己的文件和往来通信，想弄清追回条款的问题是怎么开始的。“我认为[^47]，情况比我们想的范围更广、时间更长，也更糟糕，”他说，“我们还在努力全面了解它的范围。但是，你们知道，文件上签的是我们的名字。讨论这些手段的谈话，我们也在场。

“我认为这是我们犯过的最严重的错误，”他接着说，他们正在尽快补救。他们已经给前员工发了邮件，告知他们不再受不得贬损条款约束，也从新离职员工的离职文件里删掉了这一条款。他们还在着手修改那个法律实体的文件，并继续调查整件事是怎么发生的。

面对员工接二连三的新问题，杰森·权现在翻来覆去说的是另一套话：情况究竟广了多少、长了多少、糟了多少，任何具体细节都还需要进一步“挖掘”才能给出。

会议开始约 30 分钟后，一名员工的提问引出了一段对话，让在场的许多人心里很不踏实，觉得奥特曼的回答又一次脱离了现实。

“伊尔亚身上有没有不得贬损的义务？”这名员工问。

“没有，”奥特曼很快回答。接着，他有些迟疑地加了一句缓冲的话：“我想是这样。”

杰森·权紧张地笑了笑。“山姆，”他一字一句、小心翼翼地说，“我们去确认一下，然后回复你，”说到这里，他已经转向那名员工，“保证百分之百准确。”

布罗克曼也以自己的方式委婉地唱了反调。“我的理解是，这是他自己要求的，不过还是那句话，我可能记错了。我们确认一下吧。”

在接下来的几个月里，许多现任和前任员工，尤其是资深员工和在公司待得久的人，会把全面危机，特别是追回条款这场闹剧，看作一个转折点：从那时起，他们开始意识到一件令人不安的事。这一片混乱里，有两股力量在起作用。诚然，其中一股一直都在：繁荣派与末日派之间的冲突，外界铺天盖地的批评，很大程度上最初就是由它引发的。但这一次，还有另一股力量：奥特曼在设立 OpenAI 的法律实体时表现出的集权行为；以及他每次试图解释、摆脱一摊烂事时，一再显得不诚实。“插曲”之后，许多员工认为，董事会的决定完全是第一股力量的产物；至于董事们把解释的重点放在第二股力量上，在他们看来，不过是转移视线和自欺欺人兼而有之。现在，越来越多的员工第一次觉得，奥特曼的所作所为在损害他们的利益，没有给他们带来好处，他们开始怀疑，董事会当初会不会其实是对的。

5 月 23 日的会议快结束时，杰森·权为奥特曼的人品做了一番辩护，说得磕磕绊绊，却是真情流露，只是放在这个场合显得格格不入。“你们问问题的时候，我们想给你们答案，因为我们知道你们想要答案，好像，就*现在*要。我觉得有时候我们想给你们答案，然后，你知道，有时候我们其实应该等一等。我觉得就像那个……那就像，那是，这整件事的，一部分，”他说，话说得结结巴巴，“这一切里头，有时候并没有什么故意。只是……我，我真的、真心觉得，你知道，特别是山姆，他就是不想让你们失望。这才是真正的出发点，就是，我跟这家伙共事了很久很久了。这就是我一直跟他共事的原因，你知道吗？所以，这都是出……这，这*确实*是出于好意。我就是想说这个。你们想怎么喷我都行。但是，你知道，这就，就，呃，就，对，这就是我要说的。”

穆拉蒂、布罗克曼和帕霍茨基一起来到[^48]苏茨克维家。

那天是 5 月 23 日，OpenAI 正被全面危机的一波波冲击打得晕头转向。三人带来了员工们写的卡片和礼物，含泪恳求苏茨克维回到公司。他们动情地向他坦白：一切都乱了套。OpenAI 正同时失去员工、投资者和监管机构的信任；没有他，公司可能会“垮掉”。

当天晚些时候，奥特曼独自前来，用他自己的方式表达了希望苏茨克维重新加入、帮公司恢复几分往日模样的心愿。“把伊尔亚请回来，本来会很有帮助，”一位研究员回想说，“在一长串让 OpenAI 显得很可疑的事情之后，这至少能算一场胜利。”

苏茨克维认真考虑了。发生了这么多事，他也并不记仇。就在他宣布离职的当天，马斯克立刻向他抛出橄榄枝，请他到 xAI 任职。命运也真会开玩笑：那年晚些时候，OpenAI 搬出先锋大楼（Pioneer Building）后，马斯克把 xAI 的总部搬了进去。苏茨克维虽然非常敬重马斯克，还是谢绝了邀请，决心另起炉灶，再创办一家公司。重回自己的第一家公司，超出了他原本的打算，却正是他心里想要的一切。对他来说，这会是一次回家。不过，他需要一个保证，他也把这一点跟高管们说明白了：公司要真心诚意地努力解决他指出的那些问题，也就是领导层之间那些令人痛苦、让人无所适从的冲突。

全面危机本可以成为 OpenAI 自我反省的契机。它提醒公司去弄明白，自己*为什么*会同时失去员工、投资者、监管机构以及广大公众的信任。只有这样，也许，仅仅是也许，它才会开始意识到，“插曲”和全面危机其实是同一回事：当一个帝国通过如此大规模的剥夺，把如此多的权力集中到自己手里，让大多数人苦苦应对自主权和物质财富的丧失，只留下极少数人激烈争夺控制权，就会产生深层的系统性不稳定，而这两次危机，正是这种不稳定引发的剧烈震荡。

然而，OpenAI 选择了筑起高墙，抵御批评。奥特曼会像往常一样一再对员工说，全面危机和“插曲”，不过是公司在通往 AGI 这场风险极高的崇高征途上，那些离奇却在意料之中的疯狂时刻。“随着我们都多少感觉到，我们离找到通往这些强大系统的路越来越近了，”他在 5 月 15 日的全员大会上说，“压力和紧张的程度，不管是内部的、外部的，冲着我们来的，还是从我们身上散发出去的，都会一直持续，一直增加。”在他看来，应对这一局面的最好办法，是 OpenAI 在公关上加倍投入，巩固和各国政府的关系，并坚定不移地相信自己的愿景。“我觉得总体上我们在这方面做得相当好，”他接着说，“但这一次我们又要经受考验了。”

OpenAI 处理苏茨克维这件事的方式，后来不过是一个缩影：只要帝国延续下去，混乱就会持续不断地显现出来。苏茨克维要求的保证，在领导层中引发了又一轮内斗，这次的角色阵容略有不同，重演的却是从一开始就困扰着公司的那种由个人意气驱动的纠葛。亚历山大·蒙德雷是来自波兰的麻省理工学院教授，很多人形容他热衷于追逐权力；他在公司任职时间不算长，却成功地在公司内部打下了一片不小的地盘。蒙德雷认为请苏茨克维回来不是个好主意。苏茨克维在研究人员中太受敬仰，也太得人心。这可能会削弱蒙德雷的影响力，也会削弱他的好友帕霍茨基的影响力。不过几个小时，蒙德雷的顾虑就成功地在领导层里播下了怀疑的种子，让领导层产生了分裂。奥特曼一如既往地回避表态，两边都不拍板，这样就不会显得和谁意见相左。

高管们登门拜访后不到 24 小时，苏茨克维接到了布罗克曼的电话。布罗克曼告诉他，关于他回归的任何讨论，现在都彻底免谈了。

[^1]: **其中还有两人：** Erin Woo and Stephanie Palazzolo, “OpenAI Researchers, Including Ally of Sutskever, Fired for Alleged Leaking,” *The Information*, April 11, 2024, [theinformation.com/articles/openai-researchers-including-ally-of-sutskever-fired-for-alleged-leaking](http://theinformation.com/articles/openai-researchers-including-ally-of-sutskever-fired-for-alleged-leaking).

[^2]: **正在为这家公司募资：** Edward Ludlow and Ashlee Vance, “Altman Sought Billions for Chip Venture Before OpenAI Ouster,” *Bloomberg*, November 19, 2023, [bloomberg.com/news/articles/2023-11-19/altman-sought-billions-for-ai-chip-venture-before-openai-ouster](http://bloomberg.com/news/articles/2023-11-19/altman-sought-billions-for-ai-chip-venture-before-openai-ouster).

[^3]: **2024 年 2 月，有报道称：** Keach Hagey and Asa Fitch, “Sam Altman Seeks Trillions of Dollars to Reshape Business of Chips and AI,” *Wall Street Journal*, February 8, 2024, [wsj.com/tech/ai/sam-altman-seeks-trillions-of-dollars-to-reshape-business-of-chips-and-ai-89ab3db0](http://wsj.com/tech/ai/sam-altman-seeks-trillions-of-dollars-to-reshape-business-of-chips-and-ai-89ab3db0).

[^4]: **奥特曼后来说：** Lex Fridman, host, *Lex Fridman Podcast*, podcast, episode 419, “Sam Altman: OpenAI, GPT-5, Sora, Board Saga, Elon Musk, Ilya, Power & AGI,” March 18, 2024, [lexfridman.com/podcast](http://lexfridman.com/podcast).

[^5]: **音频方面的工作：** 作者对 Alexis Conneau 的采访，2025 年 1 月。

[^6]: **奥特曼和布罗克曼定下了一个新的最后期限：** OpenAI 内部备忘录的副本。

[^7]: **Scallion 将是第一个：** OpenAI, *Preparedness Framework (Beta)* (OpenAI, December 18, 2023), 1–27, [cdn.openai.com/openai-preparedness-framework-beta.pdf](http://cdn.openai.com/openai-preparedness-framework-beta.pdf).

[^8]: **上游流程：** OpenAI, *Preparedness Framework (Beta)*.

[^9]: **Scallion 的发布：** OpenAI, “Hello GPT-4o,” *OpenAI* (blog), May 13, 2024, [openai.com/index/hello-gpt-4o](http://openai.com/index/hello-gpt-4o).

[^10]: **还有一件事：** 措辞经两人分别独立证实。

[^11]: **在《每日秀》上：** “Trump’s Thirsty VP Contenders Crash Trial & ChatGPT’s Flirty AI Update | The Daily Show,” posted on May 15, 2024, by The Daily Show, YouTube, 9 min., 57 sec., [youtu.be/eFkUOi\_9140](http://youtu.be/eFkUOi_9140).

[^12]: **“我认为这是我们自 ChatGPT 以来推出的最好的东西”：** 会议录音，2024 年 5 月 15 日。

[^13]: **公司打算给自家模型换个品牌：** 会议录音，2024 年 5 月 15 日。

[^14]: **奥特曼后来后悔发了这条推文：** Altman 向员工表达悔意的录音。

[^15]: **奥特曼以为自己在干什么：** Sarah Krouse, Deepa Seetharaman, and Joe Flint, “Behind the Scenes of Scarlett Johansson’s Battle with OpenAI,” *Wall Street Journal*, May 23, 2024, [wsj.com/tech/ai/scarlett-johansson-openai-sam-altman-voice-fight-7f81a1aa](http://wsj.com/tech/ai/scarlett-johansson-openai-sam-altman-voice-fight-7f81a1aa).

[^16]: **3 月，他上了：** Fridman, “Sam Altman.”

[^17]: **“我们只要做好本职工作”：** “Sam Altman & Brad Lightcap: Which Companies Will Be Steamrolled by OpenAI?,” posted April 15, 2024, by 20VC with Harry Stebbings, YouTube, 53 min., 6 sec., [youtu.be/G8T1O81W96Y](http://youtu.be/G8T1O81W96Y).

[^18]: **5 月，他又上了：** Julia Black, “The Besties’ Revenge: How the ‘All-In’ Podcast Captured Silicon Valley,” *The Information*, December 15, 2023, [theinformation.com/articles/the-besties-revenge-how-the-all-in-podcast-ate-silicon-valley](http://theinformation.com/articles/the-besties-revenge-how-the-all-in-podcast-ate-silicon-valley).

[^19]: **“我感觉”：** “In Conversation with Sam Altman,” posted May 10, 2024, by All-In Podcast, YouTube, 1 hr., 43 min., 2 sec., [youtu.be/nSM0xd8xHUM](http://youtu.be/nSM0xd8xHUM).

[^20]: **“我尽量不太去想”：** Sam Altman (@sama), “i try not to think about competitors too much, but i cannot stop thinking about the aesthetic difference between openai and google,” Twitter (now X), May 16, 2024, [x.com/sama/status/1791183356274921568](http://x.com/sama/status/1791183356274921568).

[^21]: **“插曲”之后，董事会：** Deepa Seetharaman, “SEC Investigating Whether OpenAI Investors Were Misled,” *Wall Street Journal*, February 28, 2024, [wsj.com/tech/sec-investigating-whether-openai-investors-were-misled-9d90b411](http://wsj.com/tech/sec-investigating-whether-openai-investors-were-misled-9d90b411).

[^22]: **最引人注目的是，2024 年 3 月：** Karen Weise and Cade Metz, “How Microsoft’s Satya Nadella Became Tech’s Steely Eyed A.I. Gambler,” *New York Times*, July 14, 2026, [nytimes.com/2024/07/14/technology/microsoft-ai-satya-nadella.html](http://nytimes.com/2024/07/14/technology/microsoft-ai-satya-nadella.html).

[^23]: **在 DeepMind 为他工作过的人：** 依据三位曾为他工作的人的回忆和评价。

[^24]: **多年来不断有人向人力资源部门投诉他：** Rob Copeland and Parmy Olson, “Artificial Intelligence Will Define Google’s Future. For Now, It’s a Management Challenge,” *Wall Street Journal*, January 26, 2021, [wsj.com/articles/artificial-intelligence-will-define-googles-future-for-now-its-a-management-challenge-11611676945](http://wsj.com/articles/artificial-intelligence-will-define-googles-future-for-now-its-a-management-challenge-11611676945); Giles Turner and Mark Bergen, “Google DeepMind Co-Founder Placed on Leave From AI Lab,” *Bloomberg*, August 21, 2019, [bloomberg.com/news/articles/2019-08-21/google-deepmind-co-founder-placed-on-leave-from-ai-lab](http://bloomberg.com/news/articles/2019-08-21/google-deepmind-co-founder-placed-on-leave-from-ai-lab).

[^25]: **2024 年晚些时候，微软：** Jordan Novet, “Microsoft Says OpenAI Is Now a Competitor in AI and Search,” CNBC, July 31, 2024, [cnbc.com/2024/07/31/microsoft-says-openai-is-now-a-competitor-in-ai-and-search.html](http://cnbc.com/2024/07/31/microsoft-says-openai-is-now-a-competitor-in-ai-and-search.html); Alex Heath, “Microsoft Now Lists OpenAI as a Competitor,” *The Verge*, August 2, 2024, [theverge.com/2024/8/2/24212370/microsoft-now-lists-openai-as-a-competitor](http://theverge.com/2024/8/2/24212370/microsoft-now-lists-openai-as-a-competitor).

[^26]: **也有越来越多的媒体：** Ellen Huet, host, *Foundering: The OpenAI Story*, podcast, season 5, episode 1, “The Most Silicon Valley Man Alive,” Bloomberg Podcasts, June 6, 2024, [bloomberg.com/news/articles/2024-06-05/foundering-sam-altman-s-rise-to-openai?srnd=foundering](http://bloomberg.com/news/articles/2024-06-05/foundering-sam-altman-s-rise-to-openai?srnd=foundering).

[^27]: **“这种生活方式让人出奇地”：** “Sam Altman Talks GPT-4o and Predicts the Future of AI,” posted May 14, 2024, by the Logan Bartlett Show, YouTube, 46 min., 14 sec., [youtu.be/fMtbrKhXMWc](http://youtu.be/fMtbrKhXMWc).

[^28]: **“伊尔亚无疑是”：** OpenAI, “Ilya Sutskever to Leave OpenAI, Jakub Pachocki Announced as Chief Scientist,” *OpenAI* (blog), May 14, 2024, [openai.com/index/jakub-pachocki-announced-as-chief-scientist](http://openai.com/index/jakub-pachocki-announced-as-chief-scientist).

[^29]: **苏茨克维也在 Twitter 上发表了自己的声明：** Ilya Sutskever (@ilyasut), “After almost a decade, I have made the decision to leave OpenAI. The company’s trajectory has been nothing short of miraculous, and I’m confident that OpenAI will build AGI that is both safe and beneficial under the leadership of @sama, @gdb, @miramurati and now, under the excellent research leadership of @merettm. It was an honor and a privilege to have worked together, and I will miss everyone dearly. So long, and thanks for everything. I am excited for what comes next—a project that is very personally meaningful to me about which I will share details in due time,” Twitter (now X), May 14, 2024, [x.com/ilyasut/status/1790517455628198322](http://x.com/ilyasut/status/1790517455628198322).

[^30]: **OpenAI 高管在内部：** Slack 公告的截图，2024 年 5 月 14 日。

[^31]: **“为 AGI 做好准备”：** 关于 AI 安全和超级对齐团队的所有引语，都出自这次全员大会的录音，2024 年 5 月 15 日。

[^32]: **“我在公司的核心优先事项上和 OpenAI 领导层意见不合”：** Jan Leike (@janleike), “I joined because I thought OpenAI would be the best place in the world to do this research. However, I have been disagreeing with OpenAI leadership about the company’s core priorities for quite some time, until we finally reached a breaking point.,” Twitter (now X), May 17, 2024, [x.com/janleike/status/1791498178346549382](http://x.com/janleike/status/1791498178346549382).

[^33]: **《Vox》的资深撰稿人：** Kelsey Piper, “ChatGPT Can Talk, but OpenAI Employees Sure Can’t,” *Vox*, May 17, 2024, [vox.com/future-perfect/2024/5/17/24158478/openai-departures-sam-altman-employees-chatgpt-release](http://vox.com/future-perfect/2024/5/17/24158478/openai-departures-sam-altman-employees-chatgpt-release).

[^34]: **不签：** Daniel Kokotajlo 详细写过他做这个决定的过程，包括这组推文：Daniel Kokotajlo (@DKokotajlo67142), “1/15: In April, I resigned from OpenAI after losing confidence that the company would behave responsibly in its attempt to build artificial general intelligence—‘AI systems that are generally smarter than humans,’ ” Twitter (now X), June 4, 2024, [x.com/DKokotajlo67142/status/1797994238468407380](http://x.com/DKokotajlo67142/status/1797994238468407380)；以及他在 AI 安全论坛 LessWrong 上的帖子和评论：“Daniel Kokotajlo,” LessWrong, accessed November 25, 2024, [lesswrong.com/users/daniel-kokotajlo](http://lesswrong.com/users/daniel-kokotajlo)。他股权的估值出自 Kevin Roose, “OpenAI Insiders Warn of a ‘Reckless’ Race for Dominance,” *New York Times*, June 4, 2023, [nytimes.com/2024/06/04/technology/openai-culture-whistleblowers.html](http://nytimes.com/2024/06/04/technology/openai-culture-whistleblowers.html).

[^35]: **派珀的报道一出：** 所有 Slack 引文都出自截图。

[^36]: **“我们从来没有追回过”：** Sam Altman (@sama), “in regards to recent stuff about how openai handles equity: we have never clawed back anyone’s vested equity, nor will we do that if people do not sign a separation agreement (or don’t agree to a non-disparagement agreement). vested equity is vested equity, full stop. there was a provision about potential equity cancellation in our previous exit docs; although we never clawed anything back, it should never have been something we had in any documents or communication. this is on me and one of the few times i’ve been genuinely embarrassed running openai; i did not know this was happening and i should have. the team was already in the process of fixing the standard exit paperwork over the past month or so. if any former employee who signed one of those old agreements is worried about it, they can contact me and we’ll fix that too. very sorry about this,” Twitter (now X), May 18, 2024, [x.com/sama/status/1791936857594581428](http://x.com/sama/status/1791936857594581428).

[^37]: **5 月 20 日，斯嘉丽·约翰逊：** Bobby Allyn (@BobbyAllyn), “Statement from Scarlett Johansson on the OpenAI situation. Wow:,” Twitter (now X), May 20, 2024, [x.com/BobbyAllyn/status/1792679435701014908](http://x.com/BobbyAllyn/status/1792679435701014908).

[^38]: **整整一周，在其他各种事情之外：** Kylie Robison, “ChatGPT Will Be Able to Talk to You Like Scarlett Johansson in Her,” *The Verge*, May 13, 2024, [theverge.com/2024/5/13/24155652/chatgpt-voice-mode-gpt4o-upgrades](http://theverge.com/2024/5/13/24155652/chatgpt-voice-mode-gpt4o-upgrades).

[^39]: **她是生气了吗：** Sarah Krouse et al, “Behind the Scenes of Scarlett Johansson’s Battle with OpenAI.”

[^40]: **公司在 5 月 19 日发表了一篇博文：** OpenAI, “How the Voices for ChatGPT Were Chosen,” *OpenAI* (blog), May 19, 2024, [openai.com/index/how-the-voices-for-chatgpt-were-chosen](http://openai.com/index/how-the-voices-for-chatgpt-were-chosen).

[^41]: **还没等双方约好：** Krouse et al., “Scarlett Johansson’s Battle with OpenAI.”

[^42]: **“如今，我们所有人”：** Allyn, “Statement from Scarlett Johansson.”

[^43]: **“我们向约翰逊女士道歉”：** OpenAI, “How the Voices for ChatGPT Were Chosen.”

[^44]: **“我见过很多政策制定者”：** Derek Robertson, “Sam Altman’s Scarlett Johansson Blunder Just Made AI a Harder Sell in DC,” *Politico*, May 22, 2024, [politico.com/news/magazine/2024/05/22/scarlett-johansson-sam-altmans-washington-00159507](http://politico.com/news/magazine/2024/05/22/scarlett-johansson-sam-altmans-washington-00159507).

[^45]: **领导层接连做了几番简短的解释：** 对这次会议的所有描述和引语，都依据会议录音，2024 年 5 月 22 日。

[^46]: **这篇报道就在当天：** Kelsey Piper, “Leaked OpenAI Documents Reveal Aggressive Tactics Toward Former Employees,” *Vox*, May 22, 2024, [vox.com/future-perfect/351132/openai-vested-equity-nda-sam-altman-documents-employees](http://vox.com/future-perfect/351132/openai-vested-equity-nda-sam-altman-documents-employees).

[^47]: **“我认为”：** 所有引语都出自会议录音，2024 年 5 月 23 日。

[^48]: **穆拉蒂、布罗克曼和帕霍茨基一起来到：** Deepa Seetharaman, “Turning OpenAI into a Real Business Is Tearing It Apart,” *Wall Street Journal*, September 27, 2024, [wsj.com/tech/ai/open-ai-division-for-profit-da26c24b](http://wsj.com/tech/ai/open-ai-division-for-profit-da26c24b).

[^t1]: 译者注：Omnicrisis 由 omni（全）和 crisis（危机）拼成。GPT-4o 里的 o 代表的正是 Omni（见上文），所以这个新词也让人联想到 GPT-4o。
