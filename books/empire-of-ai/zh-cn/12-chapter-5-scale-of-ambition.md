# 第 5 章 野心的规模

要说 OpenAI 扩大规模的信条最早该归功于哪一个人，那就是它的联合创始人伊尔亚·苏茨克维（Ilya Sutskever）。苏茨克维一直把对深度学习的信念看得高于一切。这份信念萌生于他 17 岁那年的一次登门之后不久：那天，他事先没打招呼，就出现在了杰弗里·辛顿（Geoffrey Hinton）的办公室。当时，苏茨克维还是多伦多大学数学专业的本科生，为了维持生计，在当地一家小餐馆负责炸薯条。他急促地敲着辛顿的门，说自己迫切希望加入这位教授的实验室。辛顿让他先预约个时间。“好啊，”苏茨克维说，毫不退让，“现在怎么样？”[^1]

苏茨克维很快就吸收了联结主义的原理。他让辛顿大为震惊[^2]：他对研究问题有一种直觉上的把握，还有一种不可思议的本领，能找出既优雅又有效的解法。苏茨克维还给研究带来了他特有的戏剧色彩。有时，新想法让他兴奋不已[^3]，他会在和人合租的公寓中央做倒立俯卧撑。他喜欢发表斩钉截铁、不留余地的论断。“谁也不会押深度学习输[^4]，”他常说，“成功是必然的[^5]。”

辛顿认为，2012 年在 ImageNet 上取得的那项突破性成果，要归功于苏茨克维这种水准的直觉，再加上亚历克斯·克里泽夫斯基（Alex Krizhevsky）的编程能力。当时，深度学习已经在语音识别上展现出潜力，所以辛顿并没有太在意把它用到计算机视觉上有什么意义。苏茨克维却力推这个想法。辛顿说，在伊尔亚看来，“这显然行得通，而且显然会是一件大事”。“他看得非常清楚，而且他是对的。”

苏茨克维带着对深度学习至死不渝的信念[^6]来到 OpenAI。那时，这个领域对这一范式的信心刚刚开始动摇，加里·马库斯（Gary Marcus）这样的批评者正在呼吁新的思路。苏茨克维却没有动摇。他的信仰建立在一个简单的假设之上[^7]，这个假设也是联结主义的根基：神经网络里的人工节点，足以近似生物大脑里真实的神经元。两者都是接收输入，再把输入转换成输出；持这种想法的人认为，有这样的相似就够了，可以假定节点能像神经元一样，用来构建高度复杂的信息处理系统。苏茨克维是 OpenAI 创立之初的研究总监，在 AI 领域又以远见卓识广受尊敬，实验室朝哪个方向走，完全由他说了算。他相当于中了一张科学界的彩票：同辈中几乎没有人和他竞争，推进自己的想法又有充裕的资源。“凡是不属于深度学习的东西[^8]，根本不在考虑之列，”说起实验室的早年，加州大学伯克利分校教授彼得·阿贝尔（Pieter Abbeel）回忆道。

苏茨克维对深度学习的信念有多坚定，他对扩大深度学习规模的看法就有多坚定。正是苏茨克维持有一种在当时堪称极端的立场：AI 要进一步发展，并不需要发明更复杂的神经网络或新的创新技术。他常说，不同物种的智力[^9]与它们生物大脑的大小相关。所以他认为，如果节点像神经元一样，那么只要扩大简单神经网络的规模，让节点越来越多，数字智能就应该会进步。

苏茨克维像一位主持实验室的教授，根据这些想法给别人出主意，告诉他们哪些项目最值得做。许多科学家加入 OpenAI，就是冲着他的指点和引导来的。“伊尔亚能看到十年以后，”一名 OpenAI 研究员说，和苏茨克维共事过的其他人也有同样的说法。“他就像一位哲学家，”另一人说，“你给他一堆想法，他会告诉你哪些想法在哲学上是对的。”

苏茨克维自己不常写代码。他在技术工作上不亲力亲为，有时让一些员工很不满。一名工程师承认，起初觉得他基本上没什么用：他好像只会在办公室里大步走来走去，时不时到各个会议上露个面，重复同一句话：扩大规模，扩大规模，扩大规模！但这个人后来逐渐欣赏起苏茨克维的笃定，欣赏他能让大家齐心专注于同一个目标。正是这种专注，最终让当时还不被看好的 OpenAI，在谷歌和 DeepMind 自己最擅长的领域打败了它们。

苏茨克维说服人的本事其实并不特别出众。如果说山姆·奥特曼（Sam Altman）是政治家，苏茨克维就恰恰相反。他说话从不拐弯抹角，也从不为了让听众更容易接受而修饰措辞。他只是带着毫不掩饰的真诚和近乎狂妄的自信说出自己的看法，听的人要么产生共鸣、深受鼓舞，要么完全无感。OpenAI 掉转方向、不再公开分享研究成果之后，苏茨克维也没有给这个决定背后的理由裹上糖衣。“说白了，我们错了[^10]。”说起公司当初对透明的承诺，他对《The Verge》的 AI 记者詹姆斯·文森特（James Vincent）说得很干脆。“如果你像我们一样相信，到了某个时候，AI，或者说 AGI，会变得极其强大，强大得难以置信，那么开源就根本说不通。”他还直截了当地指出，这里面也有商业上的考虑。“GPT-4 开发起来不容易。差不多整个 OpenAI 一起干了很长一段时间，才做出这个东西。而想做同样事情的公司有很多很多。”

随着 OpenAI 不断壮大、苏茨克维的名气越来越响，他说话不加过滤的毛病有时就成了一种负担。他的听众已经不只是研究人员，扩大到了普通公众。但他一如既往，没有调整自己的说法。他还是用他招牌式的乐观自信发表言论，而对任何一个听他讲话的外行来说，这些话都缺少了重要的背景。“也许今天的[^11]大型神经网络已经有一点点意识了，”他在 2022 年发推文说，而当时其他研究人员已经在警告，这样的说法可能加深公众对这项技术的误解。一位专门研究认知和意识的 DeepMind 科学家[^12]在评论区回复：“……就如同说，一大片麦田也许有一点点是意大利面。”第二年，苏茨克维[^13]在一次会议上宣称，AGI 终将让所有工作消失，引发了恐慌。那年秋天，他在 X 上断言[^14]：“未来……我们会有\*效果奇佳\*而且便宜到家的 AI 心理治疗。”这话并没有科学依据。就在这之前，一位 OpenAI 高管随口把和 ChatGPT 聊天比作持证专业人员提供的心理治疗，在网上引发了争议。

吸引人们追随苏茨克维的，是他的声望和资历。OpenAI 的许多员工都很清楚他早年对这个领域的贡献，有些人把他看成某种先知。随着时间推移、OpenAI 越来越成功，苏茨克维的举止也越来越像一位先知。在全员大会上，他会当着全公司的人站起来，深吸一口气，为了营造戏剧效果来回踱步，然后才讲出一番含糊的励志话语。2020 年 9 月的一次线上会议上，他眼神迷离，凝望远方，描绘了一幅科幻小说般的未来图景，说那样的未来是有可能实现的。那时外面的湾区，天空已经被附近的山火映成了橙色。“那场面很不真实，因为外面看着已经像世界末日了，”一位研究员回忆说。

2022 年底 ChatGPT 发布后不久，OpenAI 在加州科学院举办了一场节日派对。苏茨克维走到人群面前[^15]，身穿一件印着 OpenAI 字样的上衣和一件黑色西装外套，和格雷格·布罗克曼（Greg Brockman）一起简短地讲了几句话。讲话结束时，依旧精瘦、如今已经开始谢顶的苏茨克维，说出了他新近的口头禅。“感受 AGI，”他说，“感受 AGI。”

按照苏茨克维扩大简单神经网络规模的理念，OpenAI 早期面对的问题就变成了：扩大哪一种神经网络的规模？不同的研究人员提出并摆弄过各种不同的方案，但这个领域里那些已经被广泛采用的神经网络，似乎没有一种符合要求。

2017 年 8 月，情况变了[^16]：谷歌发明了一种新型神经网络，名叫 Transformer。Transformer 擅长捕捉长距离的模式。回想一下早年 iPhone 上功能有限的输入预测，以及它因为生成颠三倒四、语无伦次的句子而催生的那些网络段子。这些都是短距离模式分析的产物：神经网络在看每一个词时，只考虑它和紧挨着它的那几个词的关系。Transformer 能吞下大量文本，把每个词、每个句子、每个段落放在大得多的上下文里去考量。谷歌把 Transformer 看作一种手段，可以用来改进它的搜索引擎、谷歌翻译，以及其他高度依赖语言处理的服务。苏茨克维却从中看到了别的东西。Transformer 是简单、可以扩大规模的神经网络，正属于他一直在寻找的那一类。他开始在办公室里到处宣扬它。

苏茨克维的力推让一些研究人员觉得奇怪。“当时觉得这个想法挺离谱的，”麻省理工学院研究员杜一伦（Yilun Du）回忆说，他大约在这个时候以研究学员（fellow）的身份加入 OpenAI，“Transformer 感觉是个小众的架构。”但苏茨克维的博士论文[^17]是跟着辛顿做的，研究的正是 Transformer 的前身，他看出了 Transformer 有潜力把深度学习推上一个新台阶。OpenAI 的其他人也同样兴奋。零零星星有几位研究人员开始试验它，其中包括亚历克·拉德福德（Alec Radford）。他从大波士顿地区的欧林工学院退学，技术能力出众。他开始在自己的笔记本电脑上埋头鼓捣，常常干到深夜，把 Transformer 的规模稍稍扩大一点，看看会发生什么。

拉德福德训练谷歌的这种神经网络[^18]时，用的数据集里有 7000 多本未出版的英语图书，从爱情小说到冒险小说都有。这些书是他从另一个数据集里取来的，那个数据集是其他 AI 研究人员此前为另一个项目整理并开源的。在试验过程中，他做出了一个影响深远的决定：改变 Transformer 要学习的任务。谷歌一直拿 Transformer 做语言翻译，他把任务换成了学习生成文本，办法是预测一个句子里最有可能出现的下一个词。早些时候，OpenAI 的研究人员就提出过一个假设：生成式模型会是通往 AGI 的重要一步。公司在一篇博客文章中解释[^19]，用的是高度拟人化的说法：这种情形就像理论物理学家理查德·费曼（Richard Feynman）的一句名言，“我无法创造的东西，我就不理解。”苏茨克维在公司内部有另一种说法：训练一个模型去生成令人信服的东西，会迫使它把关于世界的数据压缩成精髓。“智能就是压缩，”苏茨克维常说。他在 2016 年的一份备忘录中详细阐述了自己的坚定信念：压缩实际上是实现通用人工智能*唯一*需要的东西。说得更具体些，拉德福德发现，给算法定下一个简单的目标，让它通过预测下一个词来生成令人信服的文本，确实能让它在更深的层次上掌握英语的细微之处和结构。

有一次埃隆·马斯克（Elon Musk）来办公室，拉德福德向他演示了这项工作的初步进展。模型生成的文本质量很差，马斯克完全不为所动。拉德福德起初很泄气。但继续做下去以后，结果让他吃了一惊。Transformer 进步得很快，在一系列语言处理任务上，比如给一份文档写摘要、回答关于文档的问题，表现都比他以前试过的任何东西好得多。

2018 年，OpenAI 发布了这个模型的第一版，名为“生成式预训练 Transformer”（Generative Pre-Trained Transformer），后来人们叫它 GPT-1。名字里的第二个词“预训练”（*pre-trained*）是 AI 研究里的一个术语，指先用一大批通用的数据训练模型，作为它以后学习更具体任务的前提。换句话说，GPT-1 是在一大批通用的英语文本上训练出来的，从而粗略地模拟出这门语言的运作方式。之后，还可以用一个针对性强得多的数据集再训练它，对它进行“微调”（fine-tune），也就是让它专门化，比如用莎士比亚（Shakespeare）的剧本教它写出莎士比亚风格的文字。GPT-1 几乎没有引起任何关注。但这只是开始。拉德福德对这个想法的验证，已经足以支撑他继续做下去。下一步，就是更大的规模。

公司把最宝贵的资源，也就是算力，更多地分给了拉德福德。他的工作和达里奥·阿莫迪（Dario Amodei）正在主持的一个 AI 安全新项目正好契合，这个项目的思路与尼克·博斯特罗姆（Nick Bostrom）在《超级智能》（*Superintelligence*）里提出的设想一致。2017 年，阿莫迪手下的一个团队[^20]开始探索一种新技术，让 AI 系统与人类的偏好对齐。他们从一个简化的“玩具问题”入手：教一个 AI 智能体在一个类似电子游戏的虚拟环境里做后空翻。这个智能体模拟的是一根 T 形的棍子，竖杆上有三个关节。团队并不直接给它设定学会后空翻的目标，他们用给它反馈的办法来教它：他们雇了一些外包人员，看着这个智能体在环境里胡乱扭来扭去、翻来翻去；每隔一段时间，外包人员要比较两段记录智能体动作的视频片段，选出哪一段更像后空翻。大约 900 次比较之后，这根 T 形棍子已经能成功地把关节蜷起来，翻转过去。OpenAI 在一篇博客文章中大力宣传这项技术[^21]，说它能让 AI 模型听从那些难以说清楚的指令。团队里的研究人员把它叫作“基于人类反馈的强化学习”（RLHF）。

阿莫迪想走出这种玩具环境[^22]，而拉德福德在 GPT-1 上的工作，让语言模型看起来是个不错的选择。但 GPT-1 的能力太有限了。“我们想要一个人类可以给它反馈、和它互动的语言模型，”阿莫迪 2019 年对我说，他希望做到“语言模型足够强大，我们真的可以就人类的价值观和偏好进行有意义的对话”。

拉德福德和阿莫迪联手了。拉德福德收集了一个更大、更多样的数据集，阿莫迪和其他 AI 安全研究人员则训练出一个比一个大的模型。他们定下的目标[^23]，是一个拥有 15 亿个参数（也就是变量）的最终模型，这在当时是业内最大的模型之一。这项工作进一步证实了 Transformer 的用处，也印证了阿莫迪手下另一个团队在研究 OpenAI 定律之后开始酝酿的一个想法：经验定律不只有一条，有许多条。他的团队把它们统称为[^24]“规模定律”。

OpenAI 定律描述的是这个领域过去为提升 AI 性能而扩充资源的速度；规模定律描述的则是深度学习模型的性能与三项关键投入之间的关系：模型训练数据的量、训练所用的算力，以及模型的参数数量。此前，AI 研究人员大体上认为，让这几项投入彼此大致按比例增加，模型的能力也会大致按比例提升。阿莫迪和他的团队有一个出人意料的发现：每一项投入与模型在某个具体、可衡量的任务（比如预测下一个词）上的表现之间的关系，都可以用一条平滑的曲线来描述。换句话说，对于一项与预测下一个词紧密相关的单项能力，比如生成文本的流畅程度，要让模型在这项能力上达到想要的水平，需要用多少数据、多少算力、多少参数，都可以相当准确地估算出来。对于相关性没那么强、但仍有一定关联的能力，增加这些投入也应该能带来更好的表现。

OpenAI 在得到最终那个 15 亿参数的版本之前训练的一系列模型，正好说明了这种关系。每个模型都整整齐齐地落在一条能力不断上升的曲线上。所以，当其中最大的那个，也就是他们命名为 GPT-2 的模型，在 GPT-1 稚嫩的文本生成能力上有了明显进步，能写出篇幅很长、连贯得足以让人误以为出自人手的文字时，大家并不怎么意外。和今天的模型相比，这些文字还很笨拙，常常写着写着就变成了胡言乱语。但这是第一次，大规模自动写作突然成了可能。

让团队感到意外、而且意味更阴暗的，是 GPT-2 凭着新获得的连贯性生成的内容。只要输入几个词[^25]，比如*希拉里·克林顿*（Hillary Clinton）或*乔治·索罗斯*（George Soros），这个更能说会道的语言模型就可能很快滑向阴谋论。训练数据里夹带的少量新纳粹宣传，也可能以可怕的方式冒出来。模型这种出人意料的恶劣表现，让 AI 安全研究人员感到不安。在他们看来，这预示着更强大、未对齐的 AI 将来可能带来的滥用和风险。GPT-2 生成了一段痛斥回收利用的长篇大论[^26]（“回收利用对世界*没有*好处。它对环境有害，对我们的健康有害，对我们的经济有害。”），之后，一位 AI 安全研究员把它打印出来，贴在办公室的回收垃圾桶上方，一半是玩笑，一半是警告。

还有一次，有人让 GPT-2 为小孩子设计一套奖励等级，奖励他们完成作业、做家务。GPT-2 建议用糖果，这又让一些做 AI 安全的人感到不安，他们说，这是恋童癖者惯用的手段。一名欧洲员工对这种联想大吃一惊。“我妈妈肯定这么干过。夏天的星期天，做完家务就有冰激凌吃，”他回忆说。他怀疑，这种过度敏感是不是某种美国特有的东西。这样的时刻还有很多，都让他对 OpenAI 远大目标的基本前提产生了疑问：它缺乏真正的全球代表性，又怎么能造福全人类？他是欧洲人，来自一种和美国高度重叠的文化，即便如此，AI 安全和其他讨论中压倒性地偏向美国价值观和美国规范的倾向，还是常常让他感到格格不入。

GPT-2 在公司内部引发了一场争论。OpenAI 是否已经到了该开始保留研究成果、不再公开的时候？章程早就为这种可能留了余地。阿莫迪这时已经升任研究总监[^27]，他和负责政策工作的杰克·克拉克（Jack Clark）牵头决定下一步怎么走；克拉克以他自己的方式担忧着生存风险和其他严重的风险。他们在内部做了一次调查，还开了几次“信息危害”会议，讨论这项技术可能被滥用的方式。他们的推理是：如果 GPT-2 落入恐怖分子、独裁者或标题党内容农场之手，这个模型就可能被用来作恶。虽然这一次它看上去还不至于构成生存风险，但未来的模型只会越来越强大，这种可能性也会越来越高。最好尽早立下保留研究成果的先例。他们决定，OpenAI 不应发布完整版本。

杰克·克拉克当过记者，曾任 OpenAI 的战略与传播总监，2018 年底完全转去经营 OpenAI 在政策领域刚刚起步的影响力。他经常去华盛顿，很享受被政策制定者当作 AI 问题首选咨询对象的感觉。他会对他们说：“我就像 AI 维基百科[^28]。”他还会介绍自己来自 OpenAI 的“偏向”，这是他自己的说法：“我们希望先进技术有一个稳定的政策制定环境，能跨越好几届政府，因为我们的使命不会在一个总统任期内完成。”

跟我讲完这些，他又补充说：“我们非常幸运，政策制定者给了我们相当多的时间，因为我觉得很明显，基本上要想事情顺利，我们就是希望他们掌握更多信息，也希望他们有更多手段自己产出信息。”

2019 年 2 月，克拉克发起了一场媒体攻势，向各家媒体广而告之：OpenAI 造出了一项危险的技术，因此不会发布它。OpenAI 只会发布一个较小的版本，参数量是完整模型的 8%，让公众初步领略它的能力。他、阿莫迪和另外几个人[^29]合写了一篇博客文章，附上 GPT-2 输出的例子，展示它的全部潜力。“很清楚的是，如果[^30]这项技术成熟了，我估计也就一两年，它就可能被用来制造虚假信息或宣传，”他对我当时在《麻省理工科技评论》的同事威尔·奈特（Will Knight）说。克拉克回避了一个事实：按这个时间表推动这项技术走向成熟的，正是 OpenAI 自己。“我们在努力抢在这件事前头，”他说。

OpenAI 此举在外部研究人员中引发了强烈反弹。他们严格信奉开放科学是这个领域的基石：任何不参与开放科学的机构都应该受到怀疑，要是还公开炫耀这个决定，就更可疑了。许多人还认为，GPT-2 说到底只是一个强大的自动补全软件，OpenAI 为它大敲警钟，分寸失当，荒唐可笑。GPT-2 远没有先进到足以构成严重威胁；就算真的构成威胁，为什么要昭告天下，然后又不让公众审视它？整件事给人的感觉是虚伪做作，像是一场自我吹捧的公关噱头。在斯坦福大学，拉德福德做完一场关于 GPT-2 的讲座后，一位德高望重的自然语言处理教授举手问了最后一个问题。“那么，它*危险*吗？”他嘲弄地问。全场哄堂大笑。“亚历克看上去难过极了，”当时在场的一位斯坦福研究人员回忆说，“斯坦福对 OpenAI 简直是满怀蔑视。”

在 OpenAI 内部，许多研究人员也对阿莫迪和克拉克的决定很不满。在那些不认同两人对灾难性风险看法的人看来，无论是这个决定本身，还是随后的媒体狂欢，都有些莫名其妙。即使在认同这种看法的人当中，也有人质疑两人的判断是否站得住。“把这件事搞得这么大，是个错误，”一位 AI 安全研究员对我说，“感觉就像在喊‘狼来了’。”

反弹刚一爆发，克拉克就在办公室里来回踱步，精力亢奋，一个电话接一个电话地打，努力重新控制局面。他对这场争议不以为意。“我们在打破常规，这自然会引来很多不同的看法，”后来我到办公室采访时，他对我说。他说，所有从事前沿 AI 研究的机构，迟早都得对发表哪些成果更加有所取舍。OpenAI 正在带头试行这样一套流程，看看它可以是什么样子，免得到时候措手不及。“如果我们是对的，而且真的[^31]有可能造出 AGI，”克拉克说，“那我们他妈的肯定需要非常好的信息危害处理程序。”

他还说，研究人员也许不喜欢 OpenAI 这一手，政策制定者却很喜欢。华盛顿圈子里的许多人认为，AI 研究的开放文化是一种威胁。OpenAI 敢于反其道而行之，为它在华盛顿赢得了更多信任。

但在幕后，领导团队也明白，长此以往，公司承受不起研究界的敌意。这家实验室的声誉问题正一个接一个地叠加。它关于 AGI 的夸张言论，它在 GPT-2 和其他营销上的过火做法，还有如今，也就是 2019 年初，刚刚宣布的那个弗兰肯斯坦式的拼凑架构，让它四面受敌，这个领域的顶尖研究人员对它也越来越怀疑。这些问题，再加上它的股权当时还一文不值，让它在招揽和留住人才上依然困难重重。员工们怀疑，外部候选人拿 OpenAI 的录用通知，只是为了跟谷歌或 DeepMind 谈更高的待遇时当筹码。OpenAI 需要想办法证明，自己是一个正经的研究机构。

这个问题经常被拿出来讨论[^32]，午餐时、公司会议上都在谈，一份名为“研究界外联头脑风暴”（Research Community Outreach Brainstorming）的内部文件里也有讨论。在题为“战略”的一节下，文件写道：“明确把 ML 界当作传播工作的利益相关方。”ML 是机器学习的缩写。“改变我们的语气和对外表述，只在我们有意选择这样做的时候才去得罪他们。”文件还承认，糟糕的研究声誉最终会削弱 OpenAI 在华盛顿的影响力。“要在政府层面拥有政策影响力，我们就需要被视为 ML 研究和 AGI 方面最值得信赖的信息来源，”文件在“政策”一节下写道，“研究界的广泛支持和背书，不仅是赢得这种声誉的必要条件，还会放大我们的声音。”

克拉克的团队制定了一个新计划：分阶段发布。OpenAI 不再永久保留 GPT-2，它会把已经开发出来的、一个比一个大的模型隔一段时间发布一个，如果一切顺利，最后再发布 15 亿参数的完整版。团队说，这样 OpenAI 和其他各方就能逐步观察、应对出现的任何后果，实验室也有时间在各阶段之间与其他机构合作研究风险。

克拉克向团队强调，要通过这些合作建立一个生态系统。和知名机构合作，有助于促进产业界和学术界在应对 AI 安全风险上的更多协作。这也能让更多人支持 OpenAI 改变研究发布规范的努力，同时帮助擦亮实验室的名声。他的团队联系了少数几家精心挑选的机构里的 AI 研究人员和信息安全研究人员，让他们提前使用 GPT-2 完整版，测试它被用于有害用途的可能。克拉克指示团队，要从每位研究人员所在的机构那里争取到“最有力的背书”[^33]，这样 OpenAI 列出的合作伙伴就不只是个人，还有他们所在的机构。随后，团队准备了一份白皮书，宣传自己的发布策略，突出这些合作关系。他们列举了一些在 GPT-2 之后同样没有马上发布研究成果的机构，试图以此把 OpenAI 塑造成引领者。

这番功夫没有白费。没过多久，它就[^34]在各个行业团体和政策智库中引发了讨论，探讨把保留研究成果作为管理 AI 安全风险的一种负责任的做法。2020 年底，克拉克将和阿莫迪兄妹等人一起脱离 OpenAI，共同创办 Anthropic。在那之前，他在 OpenAI 的工作会帮助公司确立影响力，也为它日后庞大的政策野心打下基础。

OpenAI 开始用一份路线图把研究系统化。阿莫迪像投资者一样对待这份路线图：他说，这是持有“一个押注组合[^35]”。他和其他研究人员追踪这个领域里的各种想法，这些想法源自关于如何实现通用人工智能的不同理念，他们通过小规模实验逐一推进。看起来有希望的，OpenAI 就继续做；没有结果的，就放弃。

在阿莫迪看来，赢得电子游戏《Dota 2》锦标赛的那个项目已经没多大用处了。《Dota 2》团队 4 月就击败了对手，实现了目标，还帮公司拿到了微软的投资。它也让一些人对公司扩大规模的策略有了新的信心。在他看来，这个项目已经走到了头。《Dota 2》团队解散了。

阿莫迪认为仍然大有可为[^36]的，是 GPT-2。它代表的那个押注，在这个领域里被称为“纯语言”（pure language）假说。这套理论认为，语言是人类交流的主要媒介，这意味着世界上所有的知识，必定都在某个时候被写成过文字。由此推论，只要用海量的语言数据训练一个算法，别的什么都不用，AGI 就应该能够出现。与这种想法相对的是“具身”（grounding）假说，它主张，物理世界，以及我们人类感知它、与它互动的能力，对我们的智能来说是同样关键的要素。照这种看法，AGI 只能从语言与感知（比如计算机视觉）以及互动（比如由实体的或虚拟的智能体在现实世界中采取行动）的结合中产生。

在公司文件里[^37]，研究人员权衡了不同路线的长短。有一回，AI 安全团队的人在争论“纯语言”假说的优点时，拿残障人士做了令人反感的类比。这些讨论暴露出，对智能的衡量会多么快地滑向令人不安的评判：哪些人群的智力更高，哪些人群的智力更低。

“某种形式的语言[^38]，就是脱离人类社会长大的人和社会中的人之间的区别。例子：海伦·凯勒（Helen Keller），”文件在“语言居于核心地位的一些初步论据”这个标题下写道。在页边，AI 安全研究人员通过一串串评论，继续争论支持和反对“纯语言”的理由。

“而且盲人的能力和视力正常的人差不多，”一位研究员写道，以此证明通过视觉实现“具身”似乎没有必要。

“盲人在经济上似乎处于明显的劣势，”另一位回复说，并引用美国盲人联合会（National Federation of the Blind）的统计数据：70% 以上的视障成年人没有全职工作。

“盲人还是比黑猩猩能干得多，”第三位回复说，“有一些非常了不起的盲人。”

OpenAI 的许多人原本对纯语言假说持怀疑态度，但 GPT-2 让他们重新考虑。训练模型越来越准确地预测下一个词，在很大程度上提升了模型在其他一些看似关联不大的语言处理任务上的表现。沿着这条路继续走下去，进一步加强训练，进一步提高预测下一个词的准确度，GPT 模型似乎就有可能发展出更广泛的能力，这甚至显得颇为可信。阿莫迪开始认为，扩大语言模型的规模，虽然很可能并非实现 AGI 唯一需要的东西，却也许是通往 AGI 最快的路。机器人路线的处境也不妙：机器人团队的机械手总是出硬件问题，形成了最糟糕的组合，花钱多，进展又慢。

但问题来了：如果 OpenAI 继续扩大语言模型的规模，就可能加剧它借 GPT-2 警告过的那些潜在危险。阿莫迪向公司其他人论证说（奥特曼也同意），这并不意味着公司应该回避这项任务。事实上，结论恰恰相反：阿莫迪说，OpenAI 应该尽快扩大语言模型的规模，只是不要马上发布。GPT-2 已经表明[^39]，其他人要获得更强大的 AI 能力会有多容易；事实上，在 OpenAI 发布自己的完整版之前，两名研究生就已经做出了一个开源版的 GPT-2。其他人开始进一步扩大语言模型的规模，只是时间问题。这意味着，确保有益的 AGI 的最好办法，就是 OpenAI 抢先一步，利用内部领先的时间，想办法让扩大规模后的模型更安全。等到该公开模型的时候，它额外的打磨和改进将有助于确立 AI 安全规范，就像当初保留 GPT-2 改变了研究发布的规范一样。

既然 GPT-2 已经有一个版本流传在外，也就有了证据表明纯语言模型的危险其实没那么严重。据 OpenAI 所知，它还没有被用于有组织的大规模虚假信息宣传活动；何况这类活动肯定也比 AGI 潜在的生存风险要好。

“滥用显然不是好事，”阿莫迪对我说，“但语言模型远没有 AGI 那么强大。我非常担心语言模型被用作散布虚假信息之类的武器，这让我非常害怕，但与此同时，这是一个相对单一、清楚、明确的担忧。”

换句话说，在阿莫迪看来，扩大 GPT-2 的规模不仅可能是通往 AGI 最快的路，而且一路上可能出现的风险也会相对局限在他认为可控的那一类：错误信息和虚假信息，还到不了灾难的地步。这会给 OpenAI 一个更安全的试验场，用一个强大、但又没有*那么*强大的 AI 系统做实验，把各种毛病解决掉，包括发布它时会遇到的问题。

“AGI 是什么？AGI 长什么样？”阿莫迪说，“嗯，你知道，我们的处境有点尴尬，就是，我们不知道它长什么样，也不知道它什么时候会出现。所以我们去找一些东西，它们算不上 AGI，但至少带有 AGI 的一部分机遇和难题。我们的希望是，如果能把这些东西处理好，那我们就算是，有点像，准备好进入更高级别的联赛了。”

这套逻辑要成立，需要一个特定的前提：AGI 虽然无定形、不可知，却也是不可避免的。此后多年，OpenAI 会一再拿同一论点的各种变体，为自己的所作所为辩护。在 AGI 势不可挡、终将到来的阴影下，公司需要不断开发越来越强大的模型，让自己和社会都做好准备。即使这些模型本身带有风险，它们提供的经验可以用来防范或应对可能到来的 AI 末日，有了这一点，那些风险也就可以承受了。

2023 年初，ChatGPT 席卷全球，一位中国 AI 研究人员向我分享了一番清醒的分析，拆穿了 OpenAI 关于必然性的论点。他说，OpenAI 做的事，除了硅谷，在任何地方都不可能发生。在中国，AI 人才堪与美国匹敌，但没有哪个研究人员和工程师团队，无论多么出色，能拿到 10 亿美元，更不用说十倍于此的钱，去开发一项极其昂贵的技术，却说不清楚这项技术究竟会是什么样子、能派什么用场。直到 ChatGPT 发布之后，中国的公司和投资者才开始热情高涨地投资开发巨型模型，因为他们这时已经看到了足够的证据，相信可以通过商业应用收回投资。

在报道过程中，我逐渐得出了一个更惊人的结论。即使在硅谷，其他公司和投资者也是直到 ChatGPT 之后，才开始毫无保留地把巨额资金投入扩大规模。其中也包括谷歌，以及 OpenAI 最初的对手 DeepMind。恰恰是 OpenAI，凭着它的亿万富翁出身、独特的意识形态倾向，以及奥特曼非同一般的干劲、人脉和融资天赋，凑齐了成熟的条件，让它那套特定的愿景得以出现并占据主导。“我感觉山姆是这个星球上最有野心的人，”一位前员工说。换句话说，OpenAI 所做的一切，和必然性正好相反；它的大型深度学习模型在全球造成的急剧膨胀的代价，它在整个行业引发的、要把这类模型扩大到地球极限的危险竞赛，都只可能出自 OpenAI 这一个地方。

为了 2019 年 4 月的“盖茨演示”，OpenAI 已经把 GPT-2 扩大成了一个稍大一些的模型。但阿莫迪对小幅扩张不感兴趣。如果目标是拉长 OpenAI 的领先时间，GPT-3 就得尽可能大。作为投资的一部分，微软即将交付给 OpenAI 一台新的超级计算机，配有 1 万块英伟达 V100，那是当时世界上训练深度学习模型最强大的 GPU。这款芯片名字里的 *V*，取自意大利化学家、物理学家亚历山德罗·伏打（Alessandro Volta）的姓氏。阿莫迪想用上全部[^40]芯片，而且是同时全部用上，来打造这个新的大语言模型。

在许多人看来，这个想法简直荒唐透顶。在那之前，一个模型只要用几十块芯片训练，就已经算是大规模了。在麻省理工学院和斯坦福大学的顶尖学术实验室里，博士生能有十块芯片就算是奢侈了。在美国以外的大学，比如在印度，学生要是能和好几个同学共用一块芯片，就算运气好了，他们只能靠一块 GPU 的一小部分算力凑合着做研究。

OpenAI 的许多研究人员怀疑阿莫迪的想法到底能不能行得通。还有人认为，循序渐进地扩大规模会更稳妥、更科学、更可预测。但阿莫迪坚持自己的提议，而且得到了其他高管的支持。苏茨克维急于验证自己扩大 Transformer 规模的假设；布罗克曼想继续提升公司的知名度；奥特曼则力主放手一搏，搏得越大越好。不久之后，阿莫迪升任研究副总裁。

在幕后，奥特曼还敏锐地意识到另一个因素：微软投了 10 亿美元，就会带着 10 亿美元的期待；OpenAI 得赶在期限内拿出点东西，证明这笔钱花得值。在阿莫迪眼里，更大的语言模型是开展 AI 安全研究的必要前提；在奥特曼眼里，它有望兑现 OpenAI 对微软的承诺。

接下来的几个月里，阿莫迪和奥特曼会在何时、如何发布 GPT-3 的问题上发生冲突；奥特曼最终胜出，以加快的时间表把模型推向了世界。早在 ChatGPT 问世几年前，这两个决定，一个让 GPT-3 的规模急剧膨胀，一个让它迅速发布，就将改变 AI 发展的方向。这将让 AI 的进步急剧加速，在公司之间、国家之间引发激烈竞争。这将助长监控资本主义和劳动剥削前所未有的扩张。由于需要的资源实在太多，这将让这项技术的开发集中到前所未有的程度，把世界上其他人都挡在门外。这将加速一个恶性循环：大学无力竞争，博士生和教授纷纷流向产业界，独立的学术研究日渐萎缩，问责也开始走向终结。这将把 AI 对环境的影响放大到这样一种程度：由于缺乏透明度和监管，直到今天，无论外部专家还是各国政府，都没能把它完整地统计出来。

不过这一切都还没有发生。2019 年秋天，阿莫迪组建了一个名叫 Nest（巢）的团队，成员大多是其他 AI 安全研究人员，意在由他们在公司内部审慎地掌控 GPT-3 的开发。就这样，这个团队开始了激进的规模扩张。

GPT-3 实际上和 GPT-2 是同一个模型，只是喂进了多得多的数据和算力，规模大了太多，以至于在许多人看来，结果已经超出了程度上的差别，变成了性质上的差别。但用 1 万块芯片带来了新的问题。任何一块芯片都总有一点可能在训练中途崩溃，就像笔记本电脑开了太多窗口可能死机一样。只要一块芯片崩溃，全部都会崩溃，这意味着训练得从头再来。放到 1 万块 GPU 上，其中任何一块芯片崩溃的概率层层叠加，就变得相当可观了。Nest 团队预计训练至少要花几个月，这样的故障无论在金钱上还是时间上，代价都会极其高昂。

为了解决这个问题，团队需要一种办法，确保训练在任何中断之后都能从停下的地方准确地接着进行。团队还需要确定一种策略，把训练分摊到全部 1 万块芯片上，这个过程叫作分片（sharding）：比如说，是把模型切成几十份、几百份还是几千份更好？每一份先在各自的 GPU 集群上训练，然后再合并起来。

接下来是数据上的难题。要获得最好的性能，数据集的规模需要随着参数数量和算力按比例增长。如果参数太多而数据不够，模型就可能开始逐字逐句地照搬训练数据里的句子，这实际上就让它变得毫无用处。为 GPT-2 准备数据时，拉德福德对哪些内容可以进入数据集很挑剔。他抓取的文本来自在 Reddit 上被分享过、并在这个平台上至少获得三个赞的文章和网站。由此得到了[^41]一个 40 GB 的文本库，包含大约 800 万份文档，他把它命名为 WebText。

对 GPT-3 来说，这远远不够。于是 Nest 扩充了数据[^42]：加进了范围更广的 Reddit 分享链接抓取数据，还有英文维基百科的抓取数据，以及一个名叫 Books2 的神秘数据集。OpenAI 从未公开过 Books2 的细节，但两位了解这个数据集的人告诉我，里面有从 Library Genesis 扒下来的已出版图书。Library Genesis 是一个网上的影子书库，收藏的是通过 BT 种子流传的图书和学术文章。2023 年，美国作家协会（Authors Guild）和包括乔治·R.R.马丁（George R. R. Martin）、朱迪·皮考特（Jodi Picoult）在内的 17 位作家起诉 OpenAI 和微软，指控它们大规模侵犯版权。OpenAI 在 2024 年 3 月回应[^43]说，它已经删除了这些数据集，并在 GPT-3.5 之后就停止用它们训练模型，而 GPT-3.5 到那时已经停用了。

数据还是不够。于是 Nest 最后求助于[^44]一个公开的数据集 Common Crawl。这是一个庞杂的数据堆，里面有数 PB，也就是数百万 GB 的文本，定期从整个网络上抓取而来。拉德福德当初特意避开了这个来源，因为它的质量实在太差。为了整治数据里的垃圾，Nest 团队训练了一个机器学习模型，从 Common Crawl 里找出最像维基百科文章的样本。他们的想法是：看起来像维基百科的，质量就更有可能接近维基百科。他们还加进了一些英语以外其他语言的样本，不过这些样本最终只占数据的 7%。即便如此，训练模型时，研究人员仍把过滤后的 Common Crawl 数据的权重设为最低。换句话说，GPT-2 的数据质量就是顶峰，此后便一路下滑。

等到为两年后发布的 GPT-4 收集数据时，追求数量的压力进一步侵蚀了质量。Common Crawl 数据的过滤器被拿掉了，其中大部分数据都灌了进去。通过与微软的合作关系，OpenAI 还拿到了 GitHub 的完整下载，GitHub 是微软旗下的在线代码托管平台。这还不够时，OpenAI 的员工又把能在互联网上找到的东西统统收集起来：抓取 Twitter 上分享的链接，转写 YouTube 视频，再东拼西凑出一长串零零碎碎的其他内容，来源包括小众博客、网上现成的数据堆，以及一个叫 Pastebin 的文本存储网站。凡是没有明确警告禁止抓取的东西，都被当作可以随意拿取。

在谷歌内部，一些研究人员感叹，OpenAI 愿意为收集数据承担法律风险，这给了它很大的优势。谷歌在数据的获取和使用上要保守得多，还有一套严格的流程，确保遵守包括欧洲数据隐私法（俗称 GDPR）在内的各项法规。讽刺的是，谷歌对合规的坚持，反倒让 OpenAI 比谷歌自己更容易用上谷歌的数据。OpenAI 可以随手抓取、转写谷歌旗下 YouTube 的视频，谷歌的研究人员却得在公司内部穿过重重繁文缛节，才能遵守 YouTube 对用户上传内容的严格许可规定。OpenAI 对这种合规毫不在意，用科技创业圈的话说，叫“没有包袱”。这是硅谷一种典型的心态：创始人和投资者奉行这样一句信条，初创公司可以而且应该闯进法律的灰色地带（想想爱彼迎、优步或 Coinbase），去颠覆和革新各个行业。

降低质量门槛、后来实际上把门槛完全撤掉的决定，会对 AI 系统背后的人类劳动产生广泛的下游影响。多年来，科技行业一直依靠经济处境朝不保夕、报酬微薄的工人，为它的 AI 模型完成必不可少的数据准备工作，比如给文本分类、给图像打标签。GPT-3 让使用巨大而质量更差的数据集成为常态之后不久，这类工作的需求就从处理大体无害的内容，转向了常常令人不安的内容，其中包括为内容审核服务，这和此前的社交媒体很像。这种审核必不可少：要靠它来阻止生成式 AI 系统把它们那包罗万象的数据集里最恶劣的部分，也就是对暴力、性虐待或自残的描述和描绘，再现给数以亿计的用户。

“这些模型的输出怎么控制，在这件事上有一个很大的范式转变[^45]，”Appen 的首席执行官兼董事总经理瑞安·科尔恩（Ryan Kolln）说。Appen 是一个为硅谷公司对接数据工作者的平台。“按传统的 AI 思路，你通过限制输入来控制输出，”也就是拉德福德团队做的那种数据过滤，“因为它只从你给它的例子里学习。生成式 AI 的难题在于，输入是全人类的全部语料。所以你得去控制输出。”

在 2023 年的一篇论文中，阿贝巴·比尔哈内（Abeba Birhane）[^46]和合著者提出了“仇恨规模定律”的概念，批判用未经过滤的数据，也就是他们所说的“数据沼泽”，来训练深度学习模型这一做法的前提。他们分析了两个用来训练开源图像生成器的公开图文数据集 LAION-400M 和 LAION-2B-en，两者都取自 Common Crawl，分别有 4 亿张和 20 亿张图像。他们发现，仇恨和辱骂性内容的数量随数据集规模的增大而增加，还加剧了用这些数据集训练的模型的歧视行为。例如，用 20 亿张图像训练的模型，把黑人男性面孔标为罪犯的可能性，是用 4 亿张图像训练的模型的五倍。同年晚些时候，斯坦福大学的一项研究[^47]分析了用来训练 Stable Diffusion 的、包含 50 亿张图像的数据集 LAION-5B，发现其中有数千张已证实或疑似的儿童性虐待图像。

在控制输出的种种手段中[^48]，OpenAI 以平均每小时不到 2 美元的报酬雇用肯尼亚工人，让他们打造一个自动化的内容审核过滤器，这件事最早由《时代》周刊记者比利·佩里戈（Billy Perrigo）披露。它还在全球雇用[^49]了另外 1000 多名外包人员，在它的语言模型上做基于人类反馈的强化学习（RLHF），也就是它当初开发出来教 AI 智能体后空翻的那项技术，工作内容包括反复向模型输入提示词并给模型的回答打分，力求尽可能把模型驯服。

德国艺术家、电影人黑特·史德耶尔（Hito Steyerl）拍过一部纪录片，讲的是从事数据工作的叙利亚难民。她跟我分享的看法，与比尔哈内的批评相互呼应。她说，当数据收集以大规模监控为基础时，对心理有害的材料[^50]就会不断累积。要解决这个问题，我们必须回到它的根源：追问数据里究竟有什么，追问大规模、不加分辨地攫取数据这整个前提。

[^1]: **“现在怎么样？”：** Cade Metz, *Genius Makers: The Mavericks Who Brought AI to Google, Facebook, and the World* (Dutton, 2021), 93; “Geoffrey Hinton | On Working with Ilya, Choosing Problems, and the Power of Intuition,” posted May 20, 2024, by Sana, YouTube, 45 min., 45 sec., [youtu.be/n4IQOBka8bc](http://youtu.be/n4IQOBka8bc).

[^2]: **他让辛顿大为震惊：** 作者对 Geoffrey Hinton 的采访，2023 年 11 月。

[^3]: **有时，新想法让他兴奋不已：** Metz, *Genius Makers*, 94.

[^4]: **“谁也不会押深度学习输”：** Will Douglas Heaven, “Rogue Superintelligence and Merging with Machines: Inside the Mind of OpenAI’s Chief Scientist,” *MIT Technology Review*, October 26, 2023, [technologyreview.com/2023/10/26/1082398/exclusive-ilya-sutskever-openais-chief-scientist-on-his-hopes-and-fears-for-the-future-of-ai](http://technologyreview.com/2023/10/26/1082398/exclusive-ilya-sutskever-openais-chief-scientist-on-his-hopes-and-fears-for-the-future-of-ai).

[^5]: **“成功是必然的”：** “NIPS: Oral Session 4—Ilya Sutskever,” posted August 19, 2016, by Microsoft Research, YouTube, 23 min., 14 sec., [youtu.be/-uyXE7dY5H0](http://youtu.be/-uyXE7dY5H0).

[^6]: **苏茨克维带着对深度学习至死不渝的信念：** Sutskever 常常说起，他对深度学习的信念，说到底是一种*信仰*。2023 年 9 月，他说：“OpenAI 的创立本身就已经是这个赌注的体现，体现的是深度学习能做到这件事的想法。你只需要相信。事实上，我甚至会说，很多，你知道，深度学习研究，至少在过去十年里，现在也许少一点了，靠的一直是信仰。” “Interview with Dr. Ilya Sutskever, Cofounder of OPEN AI—at the Open University Studios—English,” posted September 13, 2023, by The Open University of Israel, YouTube, 50 min., 28 sec., [youtu.be/H1YoNlz2LxA](http://youtu.be/H1YoNlz2LxA).

[^7]: **他的信仰建立在一个简单的假设之上：** “What AI Is Making Possible | Ilya Sutskever and Sven Strohband,” posted July 18, 2023, by Khosla Ventures, YouTube, 25 min., 26 sec., [youtu.be/xym5f0XYlSc](http://youtu.be/xym5f0XYlSc); “Ilya Sutskever: ‘Sequence to Sequence Learning with Neural Networks: What a Decade,’ ” posted December 14, 2024, by seremot, YouTube, 24 min., 36 sec., [youtu.be/1yvBqasHLZs](http://youtu.be/1yvBqasHLZs).

[^8]: **“凡是不属于深度学习的东西”：** 作者对 Pieter Abbeel 的采访，2023 年 10 月。

[^9]: **不同物种的智力：** “Ilya Sutskever: ‘Sequence to Sequence Learning with Neural Networks.”

[^10]: **“说白了，我们错了”：** James Vincent, “OpenAI Co-founder on Company’s Past Approach to Openly Sharing Research: ‘We Were Wrong,’ ” *The Verge*, March 15, 2023, [theverge.com/2023/3/15/23640180/openai-gpt-4-launch-closed-research-ilya-sutskever-interview](http://theverge.com/2023/3/15/23640180/openai-gpt-4-launch-closed-research-ilya-sutskever-interview).

[^11]: **“也许今天的”：** Ilya Sutskever (@ilyasut), “it may be that today’s large neural networks are slightly conscious,” Twitter (now X), February 9, 2022, [x.com/ilyasut/status/1491554478243258368](http://x.com/ilyasut/status/1491554478243258368).

[^12]: **一位专门研究认知和意识的 DeepMind 科学家：** Murray Shanahan (@mpshanahan), “…in the same sense that it may be that a large field of wheat is slightly pasta,” Twitter (now X), February 10, 2022, [x.com/mpshanahan/status/1491715721289678848](http://x.com/mpshanahan/status/1491715721289678848).

[^13]: **第二年，苏茨克维：** Nirit Weiss-Blatt, “What Ilya Sutskever Really Wants,” *AI Panic*, September 16, 2023, [aipanic.news/p/what-ilya-sutskever-really-wants](http://aipanic.news/p/what-ilya-sutskever-really-wants).

[^14]: **那年秋天，他在 X 上断言：** Ilya Sutskever (@ilyasut), “In the future, once the robustness of our models will exceed some threshold, we will have \*wildly effective\* and dirt cheap AI therapy. Will lead to a radical improvement in people’s experience of life. One of the applications I’m most eagerly awaiting.,” Twitter (now X), September 27, 2023, [x.com/ilyasut/status/1707027536150929689](http://x.com/ilyasut/status/1707027536150929689).

[^15]: **苏茨克维走到人群面前：** Sutskever 在这次活动上的一张照片。

[^16]: **2017 年 8 月，情况变了：** Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez et al., “Attention Is All You Need,” in *NIPS ’17: Proceedings of the 31st International Conference on Neural Information Processing Systems* (December 2017): 6000–10, [dl.acm.org/doi/10.5555/3295222.3295349](http://dl.acm.org/doi/10.5555/3295222.3295349).

[^17]: **但苏茨克维的博士论文：** Sutskever 的博士论文研究的是循环神经网络（RNN）。RNN 和 Transformer 一样，都是为处理序列数据设计的，因此适用面很广。例如，一个英语句子是一串词，一张图像是一串像素，一段视频是一串图像。他的博士论文见：Ilya Sutskever, “Training Recurrent Neural Networks” (PhD diss., University of Toronto, 2013), 1–101, cs.utoronto.ca/~ilya/pubs/ilya\_sutskever\_phd\_thesis.pdf [已失效]。

[^18]: **拉德福德训练谷歌的这种神经网络：** Alec Radford, Karthik Narasimhan, Tim Salimans, and Ilya Sutskever, “Improving Language Understanding by Generative Pre-Training,” preprint, OpenAI, June 11, 2018, 1–12, [cdn.openai.com/research-covers/language-unsupervised/language\_understanding\_paper.pdf](http://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf). Radford 从中取用那 7000 多本未出版图书的原始数据集出自：Yukun Zhu, Ryan Kiros, Rich Zemel, Ruslan Salakhutdinov, Raquel Urtasun, Antonio Torralba et al., “Aligning Books and Movies: Towards Story-Like Visual Explanations by Watching Movies and Reading Books,” in *Proceedings: 2015 IEEE International Conference on Computer Vision* (Institute of Electrical and Electronics Engineers, 2015): 19–27, [doi.org/10.1109/ICCV.2015.11](http://doi.org/10.1109/ICCV.2015.11). 在 AI 研究中，一个团队拼凑出一个数据集公开发布，其他团队再拿去另作他用，这种情况并不少见。

[^19]: **公司在一篇博客文章中解释：** OpenAI, “Generative Models,” *Open AI* (blog), June 16, 2016, [openai.com/index/generative-models](http://openai.com/index/generative-models).

[^20]: **2017 年，阿莫迪手下的一个团队：** Paul Christiano, Jan Leike, Tom B. Brown, Miljan Martic, Shane Legg, and Dario Amodei, “Deep Reinforcement Learning from Human Preferences,” in *NIPS ’17: Proceedings of the 31st International Conference on Neural Information Processing Systems* (December 2017): 4302–10, [dl.acm.org/doi/10.5555/3294996.3295184](http://dl.acm.org/doi/10.5555/3294996.3295184).

[^21]: **OpenAI 在一篇博客文章中大力宣传这项技术：** OpenAI, “Learning from Human Preferences,” *Open AI* (blog), June 13, 2017, [openai.com/index/learning-from-human-preferences](http://openai.com/index/learning-from-human-preferences).

[^22]: **阿莫迪想走出这种玩具环境：** 作者对 Dario Amodei 的采访，2019 年 8 月。

[^23]: **他们定下的目标：** Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei, and Ilya Sutskever, “Language Models Are Unsupervised Multitask Learners,” preprint, OpenAI, February 14, 2019, 1–24, [cdn.openai.com/better-language-models/language\_models\_are\_unsupervised\_multitask\_learners.pdf](http://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf).

[^24]: **他的团队把它们统称为：** Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B. Brown, Benjamin Chess, Rewon Child et al., “Scaling Laws for Neural Language Models,” preprint, arXiv, January 23, 2020, 1–30, [doi.org/10.48550/arXiv.2001.08361](http://doi.org/10.48550/arXiv.2001.08361).

[^25]: **只要输入几个词：** 对 Amodei 的采访，2019 年 8 月。

[^26]: **GPT-2 生成了一段痛斥回收利用的长篇大论：** 这段长篇大论的全文见：OpenAI, “Better Language Models and Their Implications,” *Open AI* (blog), February 14, 2019, [openai.com/index/better-language-models](http://openai.com/index/better-language-models).

[^27]: **阿莫迪这时已经升任研究总监：** 作者对 Jack Clark 的采访，2019 年 8 月。

[^28]: **“我就像 AI 维基百科”：** 对 Clark 的采访。

[^29]: **他、阿莫迪和另外几个人：** OpenAI, “Better Language Models.”

[^30]: **“很清楚的是，如果”：** Will Knight, “An AI That Writes Convincing Prose Risks Mass-Producing Fake News,” *MIT Technology Review*, February 14, 2019, [technologyreview.com/2019/02/14/137426/an-ai-tool-auto-generates-fake-news-bogus-tweets-and-plenty-of-gibberish](http://technologyreview.com/2019/02/14/137426/an-ai-tool-auto-generates-fake-news-bogus-tweets-and-plenty-of-gibberish).

[^31]: **“如果我们是对的，而且真的”：** 对 Clark 的采访，2019 年 8 月。

[^32]: **这个问题经常被拿出来讨论：** Karen Hao, “The Messy, Secretive Reality Behind OpenAI’s Bid to Save the World,” *MIT Technology Review*, February 17, 2020, [technologyreview.com/2020/02/17/844721/ai-openai-moonshot-elon-musk-sam-altman-greg-brockman-messy-secretive-reality](http://technologyreview.com/2020/02/17/844721/ai-openai-moonshot-elon-musk-sam-altman-greg-brockman-messy-secretive-reality).

[^33]: **“最有力的背书”：** 2019 年 8 月我在 OpenAI 办公室驻点采访期间，参加了这次政策团队会议。

[^34]: **没过多久，它就：** Helen Toner, “GPT-2 Kickstarted the Conversation About Publication Norms in the AI Research Community,” CSET, May 1, 2020, [cset.georgetown.edu/article/gpt-2-kickstarted-the-conversation-about-publication-norms-in-the-ai-research-community/](http://cset.georgetown.edu/article/gpt-2-kickstarted-the-conversation-about-publication-norms-in-the-ai-research-community/); PAI Staff, “Managing the Risks of AI Research: Six Recommendations for Responsible Publication,” Partnership on AI, May 6, 2021, [partnershiponai.org/paper/responsible-publication-recommendations](http://partnershiponai.org/paper/responsible-publication-recommendations).

[^35]: **“一个押注组合”：** 对 Amodei 的采访，2019 年 8 月。

[^36]: **阿莫迪认为仍然大有可为：** 对 Amodei 的采访。

[^37]: **在公司文件里：** 其中两份文件的副本。

[^38]: **“某种形式的语言”：** 这段引述的讨论出自上面提到的其中一份文件。

[^39]: **GPT-2 已经表明：** Tom Simonite, “OpenAI Said Its Code Was Risky. Two Grads Re-Created It Anyway,” *Wired*, August 26, 2019, [wired.com/story/dangerous-ai-open-source](http://wired.com/story/dangerous-ai-open-source).

[^40]: **阿莫迪想用上全部：** OpenAI 在最初介绍 GPT-3 的论文里没有公布所用芯片的数量，但在第 7 章讲到的谷歌那场风波之后，它把 1 万这个数字告诉了谷歌的研究人员，后者在下面这篇论文里公布了它：David Patterson, Joseph Gonzalez, Quoc Le, Chen Liang, Lluis-Miquel Munguia, Daniel Rothchild et al., “Carbon Emissions and Large Neural Network Training,” preprint, arXiv, April 23, 2021, 6, [doi.org/10.48550/arXiv.2104.10350](http://doi.org/10.48550/arXiv.2104.10350).

[^41]: **由此得到了：** 关于 GPT-2 所用训练数据的细节，见 OpenAI 介绍这个模型的论文：Radford et al., “Language Models Are Unsupervised Multitask Learners.”

[^42]: **于是 Nest 扩充了数据：** 这样做的并非只有 OpenAI。2023 年，作家兼程序员 Alex Reisner 证实，Meta 和彭博等公司用另一个名叫 Books3 的图书数据集训练过它们的模型；据他分析，这个数据集收录了 17 万多本已出版的图书。2024 年，Reisner 又证实，这几家公司以及 Anthropic、英伟达、苹果等公司，同样在用一个名叫 OpenSubtitles 的数据集训练模型，这个数据集收录了 5.3 万多部电影和 8.5 万多集电视剧的对白。Alex Reisner, “Revealed: The Authors Whose Pirated Books Are Powering Generative AI,” *The Atlantic*, August 19, 2023, [theatlantic.com/technology/archive/2023/08/books3-ai-meta-llama-pirated-books/675063/](http://theatlantic.com/technology/archive/2023/08/books3-ai-meta-llama-pirated-books/675063/); Alex Reisner, “There’s No Longer Any Doubt That Hollywood Writing Is Powering AI,” *The Atlantic*, November 18, 2024, [theatlantic.com/technology/archive/2024/11/opensubtitles-ai-data-set/680650](http://theatlantic.com/technology/archive/2024/11/opensubtitles-ai-data-set/680650).

[^43]: **OpenAI 在 2024 年 3 月回应：** Authors Guild v. OpenAI Inc., No. 1:23-cv-08292, CourtListener (S.D.N.Y. May 6, 2024) ECF No. 143, Exhibit D, at \*2.

[^44]: **于是 Nest 最后求助于：** 关于 GPT-3 所用训练数据的细节，见 OpenAI 介绍这个模型的论文：Tom B. Brown, Benjamin Mann, Nick Ryder et al., “Language Models Are Few-Shot Learners,” in *NIPS ’20: Proceedings of the 34th International Conference on Neural Information Processing Systems* (December 2020): 1877–901, [dl.acm.org/doi/abs/10.5555/3495724.3495883](http://dl.acm.org/doi/abs/10.5555/3495724.3495883).

[^45]: **“……有一个很大的范式转变”：** 作者对 Ryan Kolln 的采访，2023 年 10 月。

[^46]: **在 2023 年的一篇论文中，阿贝巴·比尔哈内：** Abeba Birhane, Vinay Prabhu, Sang Han, and Vishnu Naresh Boddeti, “On Hate Scaling Laws for Data-Swamps,” preprint, arXiv, June 28, 2023, 1–27, [doi.org/10.48550/arXiv.2306.13141](http://doi.org/10.48550/arXiv.2306.13141).

[^47]: **同年晚些时候，斯坦福大学的一项研究：** David Thiel, *Identifying and Eliminating CSAM in Generative ML Training Data and Models* (Stanford Internet Observatory, 2023), 1–19, [purl.stanford.edu/kh752sm9123](http://purl.stanford.edu/kh752sm9123).

[^48]: **在控制输出的种种手段中：** Billy Perrigo, “Exclusive: OpenAI Used Kenyan Workers on Less Than $2 Per Hour to Make ChatGPT Less Toxic,” *Time*, January 18, 2023, [time.com/6247678/openai-chatgpt-kenya-workers](http://time.com/6247678/openai-chatgpt-kenya-workers).

[^49]: **它还在全球雇用：** Karen Hao and Deepa Seetharaman, “Cleaning Up ChatGPT Takes Heavy Toll on Human Workers,” *Wall Street Journal*, July 24, 2023, [wsj.com/articles/chatgpt-openai-content-abusive-sexually-explicit-harassment-kenya-workers-on-human-workers-cf191483](http://wsj.com/articles/chatgpt-openai-content-abusive-sexually-explicit-harassment-kenya-workers-on-human-workers-cf191483)；OpenAI 的 RLHF 工作说明的副本。

[^50]: **对心理有害的材料：** 作者对 Hito Steyerl 的采访，2023 年 9 月。
