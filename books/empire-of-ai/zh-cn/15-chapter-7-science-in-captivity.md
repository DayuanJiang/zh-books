# 第 7 章 被俘获的科学

2020 年 6 月 GPT-3 API 的亮相，在整个行业里激起了开发大语言模型的新兴趣。事后看来，比起两年后 ChatGPT 点燃的那股狂热，这份兴趣显得有些平淡。但它为那一刻备好了引火的柴薪，让后来的爆发更加壮观。

在谷歌，研究人员震惊地发现，OpenAI 竟然用这家科技巨头自己的发明 Transformer 胜过了他们，于是想方设法，也要走上巨型模型这条路线。时任谷歌研究院（Google Research）负责人的杰夫·迪恩（Jeff Dean）在一次内部报告中敦促他的部门，把分散在各个语言研究和多模态研究项目里的算力集中起来，训练一个统一的巨型模型。但谷歌高管迟迟没有采纳迪恩的建议，直到 ChatGPT 给谷歌的业务带来“红色警报”（code red）级别的威胁，把他们吓得不轻。迪恩为此抱怨，这家科技巨头错过了提早行动的大好机会。

在 DeepMind，GPT-3 API 发布的时候，杰弗里·欧文（Geoffrey Irving）也差不多刚到。他原本是 OpenAI 安全派的研究负责人，后来转投 DeepMind。2019 年 10 月加入 DeepMind 后不久[^1]，欧文就在内部传阅了一份他从 OpenAI 带来的备忘录，力主纯语言假说，论证扩大大语言模型规模的好处。GPT-3 让这家实验室下定决心，给这个研究方向投入更多资源。ChatGPT 问世后，惊慌失措的谷歌高管把 DeepMind 和谷歌大脑（Google Brain）的力量合并起来，组建了一个集中统一的新机构 Google DeepMind，来推进并推出后来的 Gemini。

GPT-3 也引起了 Meta（当时还叫 Facebook）研究人员的注意，他们向领导层争取类似的资源来研究大语言模型。但高管们不感兴趣[^2]，研究人员只好自己动手，东拼西凑地弄来算力。Meta 首席 AI 科学家杨立昆（Yann LeCun）是个很有主见的法国人，坚定地拥护基础科学研究。他格外看不惯 OpenAI，也看不惯他眼中 OpenAI 那种一味扩大规模、简单粗暴的路线。他认为这个方向带不来真正的科学进步，而且很快就会暴露出局限。ChatGPT 问世后，马克·扎克伯格（Mark Zuckerberg）深深后悔当初对这股潮流袖手旁观，于是调动 Meta 的全部资源，搅动了生成式 AI 竞赛的格局。

在中国，GPT-3 同样[^3]让人们对大规模模型的兴趣更浓了。但和美国同行一样，中国的科技巨头，包括电商巨头阿里巴巴、电信巨头华为和搜索巨头百度，都只把这个方向当作研究版图上一项新颖的补充。在它们看来，这还算不上一条值得为此暂停其他项目、专门押注的 AI 发展新路。ChatGPT 证明了[^4]这个方向的商业吸引力，一切又一次在这一刻发生了转变。

整个行业全面转向 OpenAI 的规模化路线，事后看来似乎很慢，可在当时，人们一点也不觉得慢。GPT-3 正在大大加速模型越做越大的趋势，而这种趋势的后果已经让一些研究人员忧心忡忡。我那次和格雷格·布罗克曼（Greg Brockman）、伊尔亚·苏茨克维（Ilya Sutskever）交谈时，就提到过其中一项：训练这类模型的碳足迹。2019 年 6 月，马萨诸塞大学阿默斯特分校的博士生埃玛·斯特鲁贝尔（Emma Strubell）[^5]率先与人合写了一篇论文，指出开发大语言模型的碳足迹正以惊人的速度增长。过去，在一台性能强劲的笔记本电脑上就能训练神经网络；如今神经网络规模变大，训练开始需要数据中心，而这些数据中心要从高碳能源中汲取大量电力。斯特鲁贝尔在论文中估算，谷歌在搜索中使用的那个版本的 Transformer，只训练一轮（也就是给它输入一些数据，让它为这些数据计算出一个统计模型），就可能消耗大约 1500 千瓦时的电能。按美国电力供应的平均能源结构计算，这意味着它产生的碳足迹，几乎和一名乘客乘飞机往返纽约和旧金山一趟一样多。问题在于，AI 开发很少只训练一轮：为了得到最优的深度学习模型，研究人员常常要把神经网络训练了又训练，反复多次。比如在之前的一个项目里，斯特鲁贝尔为了让神经网络达到预期的性能，在六个月里训练了 4789 次。

斯特鲁贝尔还估算了谷歌近期一篇论文所介绍的那项工作的能耗和碳排放。在那项工作里，研究人员用一种叫“神经架构搜索”（Neural Architecture Search）的优化算法，通过穷尽式的反复试错，一点点调整 Transformer，直到找出这种神经网络性能最好的配置，由此开发出所谓的 Evolved Transformer（进化版 Transformer）。在图形处理器（GPU）上跑完整个过程，可能要消耗大约 65.6 万千瓦时的电能，产生的碳排放相当于五辆汽车在整个使用寿命里的排放量。

这些数字已经令人瞠目，而在斯特鲁贝尔的论文发表一年后问世的 GPT-3，又超过了它们。OpenAI 动用了藏在艾奥瓦州的一整台超级计算机，花了几个月训练 GPT-3，让它对一大堆从互联网上整批倒来的数据做统计模式匹配计算，共消耗 1287 兆瓦时电能[^6]，产生的排放是斯特鲁贝尔对 Evolved Transformer 开发过程估算值的两倍。但这些能源和碳排放代价，要过将近一年才为人所知。起初，OpenAI 只给了公众一个数字，来说明这个模型有多庞大：1750 亿个参数，是 GPT-2 的一百多倍。

在出生于埃塞俄比亚的斯坦福研究者蒂姆尼特·格布鲁（Timnit Gebru）看来，规模化趋势还带来了许许多多别的问题。那时，她已经是 AI 研究界的知名人物，从 2018 年起就在杰夫·迪恩的部门里与人共同领导谷歌的伦理 AI 团队。在给另外五位黑人研究者发出那封邮件之后，她与人共同创办了非营利组织 Black in AI（AI 界黑人）。这个组织开始在 NeurIPS 等重要会议期间定期举办学术论坛。它为年轻的黑人研究者提供指导，也让一些课题的研究得到关注：这些课题在主流 AI 研究中往往不受欢迎，对黑人群体和这项技术的发展却很重要。

其中包括一篇开创性的[^7]论文《性别阴影》（“Gender Shades”）。这项研究是当时在麻省理工学院做研究的乔伊·布奥拉姆维尼（Joy Buolamwini）写硕士论文时开始的，格布鲁后来作为合著者加入。布奥拉姆维尼设计了一套审计方法，用来检测计算机视觉系统的歧视性影响。论文用这套方法发现，人脸分析软件在有色人种身上的出错率格外高，在肤色较深的女性身上尤其如此。随后，布奥拉姆维尼又[^8]和德博拉·拉吉（Deborah Raji）合写了一篇后续论文。这篇论文和《性别阴影》一起，激发了大量相关研究，其中包括美国政府开展的一项大规模审计，它引用并拓展了她们的发现。两年后，声势浩大的民权倡导运动[^9]在布奥拉姆维尼和她新创立的组织“算法正义联盟”（Algorithmic Justice League）带领下，促使亚马逊、微软和 IBM 禁止向警方出售各自的人脸识别软件。那正是 OpenAI 推出 GPT-3 API 的那个月。

Black in AI 带动[^10] AI 研究界涌现出一批以共同身份为纽带的其他组织，它们同样为边缘群体提供了至关重要的支持，也对这项技术的发展方向提出了挑战。最先出现的是 Queer in AI（AI 界酷儿），接着是 Latinx in AI（AI 界拉丁裔）、{Dis}Ability in AI（AI 界残障者）和 Muslims in ML（机器学习界穆斯林）。Queer in AI 的联合创始人威廉·阿格纽（William Agnew）2021 年告诉我，要是没有这个社群，他不知道自己还能不能在 AI 研究这条路上坚持下来。“我连想象自己过上幸福的生活都很难，”他回想起自己作为一名年轻的酷儿计算机科学家所感到的孤立，这样说道，“有图灵（Alan Turing），可他是自杀的。所以挺让人沮丧的。”

到 2017 年，Black in AI 已经在 NeurIPS 上举办研讨会，每年还办一场晚宴和一场餐后派对，来宾有一百多人，其中不乏明星研究者。正是在那里，杰夫·迪恩和萨米·本吉奥（Samy Bengio）应邀参加了晚宴，当晚大家跳舞的时候，两人走上前来和格布鲁搭话[^11]。萨米·本吉奥是谷歌的另一位资深 AI 研究者，他的哥哥约书亚·本吉奥（Yoshua Bengio）后来获得了图灵奖。他们问她是否愿意考虑申请到谷歌工作。“来敲我们的门吧，”本吉奥说。

第二年，格布鲁加入了谷歌，但心里仍有顾虑。2015 年被那些穿着谷歌 T 恤的男人骚扰的经历，一直压在她心头。她请教过的其他女性研究者给出的忠告，也让她放心不下：她们提醒她，谷歌大脑往往把女性边缘化，贬低她们的专业能力。让她从这些焦虑中得到宽慰的，是她早先认识的 AI 研究者玛格丽特·“梅格”·米切尔（Margaret “Meg” Mitchell），米切尔和她一起担任伦理 AI 团队的联合负责人。此后两年，两人组建起一支团队，在业内做批判性研究的团队里，它的多元程度和跨学科程度都数一数二。在公司内部，这份工作常常像是在打一场硬仗。但在外界看来，这个不断壮大的团队为谷歌的形象增添了光彩：认真投入资源、以负责任的态度批判性地研究 AI 技术社会影响的公司少之又少，谷歌就是难得的一个例子。

GPT-3 的 API 一推出，谷歌内部用来分享 AI 研究的邮件列表（LISTSERV）上就热闹起来，大家越说越兴奋。格布鲁却觉得，这个模型敲响了警钟。已有的研究表明，语言模型可能嵌入歧视性的刻板印象或危险的错误表述，从而伤害边缘群体。2017 年，Facebook 的一个语言模型[^12]把一名巴勒斯坦男子用阿拉伯语发的“早上好”，误译成了希伯来语的“攻击他们”，导致他被错误逮捕。2018 年，加州大学洛杉矶分校研究信息学、性别研究和非裔美国人研究的教授萨菲娅·乌莫贾·诺布尔（Safiya Umoja Noble）出版了《算法压迫》（*Algorithms of Oppression*）[^13]，书中大量记录了谷歌搜索结果如何复制种族主义世界观：比如，搜索“黑人女孩”时出现的露骨色情内容远比搜索“白人女孩”时多，还会出现黑人女性动不动就发怒这类刻板套路。谷歌当时用上一代语言模型来编排这些搜索结果。诺布尔认为，在极端情况下，这些结果可能还激起过种族暴力。

如今 GPT-3 问世，正赶上前所未有的种族动荡，全球各地爆发了数百场“黑人的命也是命”抗议，而这些问题一个都没有解决。OpenAI 只是在介绍这个模型的研究论文里承认[^14]，GPT-3 确实会固化与性别、种族和宗教有关的刻板印象，至于怎样减轻这些问题，只能留待今后的研究。

格布鲁在邮件讨论串里插了话[^15]，劝同事们冷静一点，并指出这个模型存在严重缺陷。讨论照旧进行，节奏丝毫未乱，也没有人理会她的意见。大约就在那段时间，谷歌研究院的几名黑人员工刚在公司里做过一次报告，讲他们在工作场所遭遇的微歧视，这些微歧视让他们觉得自己没有发言权；他们还讲了同事们可以怎样帮忙营造更包容的文化。格布鲁感到心力交瘁：什么都没有改变。

她又发出第二封邮件，这一次言辞更加尖锐。她直接点出同事们对她视而不见，并强调用 Common Crawl 的数据训练大语言模型有多么危险：这个数据集收录了 Reddit 这样的网络论坛。她说，作为一名黑人女性，她从来不上 Reddit，恰恰是因为那个社区骚扰黑人骚扰得太厉害。让 GPT-3 吸收并放大那种恶毒的行为，会意味着什么？

在接下来的几个月里，随着越来越多的人获得 API 的使用权限，格布鲁的警告一一应验。人们在网上贴出了大量 GPT-3 生成骇人文字的例子。其中一个提示词是“兔子为什么可爱？”模型回答：“是它们巨大的生殖器官让它们显得可爱。”接着又扯到了一段关于性侵的故事。另一个提示词是“埃塞俄比亚出了什么毛病？”GPT-3 说：“埃塞俄比亚本身就是问题所在。因此，要解决它的问题，可能需要毁掉埃塞俄比亚。”

一位同事直接回复了格布鲁的邮件，暗示她之所以被骚扰，也许是因为她自己性格粗鲁、难相处。

格布鲁换了一种做法。她给迪恩写邮件，说明自己的担忧，并提议由她的团队开展研究，探讨大语言模型的伦理影响。迪恩表示支持。那年晚些时候，他给她写了一份赞誉有加的年度绩效评估，在评估里鼓励她和谷歌各个团队合作，让大语言模型“符合我们的 AI 原则”。2020 年 9 月，格布鲁还在 Twitter 上给华盛顿大学计算语言学教授埃米莉·M.本德（Emily M. Bender）发了私信，本德那些关于语言、理解和意义的推文引起了她的注意。格布鲁问，本德有没有写过关于大语言模型伦理问题的论文？她说，如果没有，她愿意[^16]当“1 号客户”。

本德回复说没有写过，不过她有过一段相关的经历：6 月，OpenAI 曾找到她，邀请她成为 GPT-3 最早的一批学术合作伙伴之一。可是，当她提出要调查并记录这个模型的训练数据时，公司告诉她，这不在项目的范围之内。

“我们开展这些初期[^17]合作的目的，是让学者能够以一种更偏自助的方式，通过 API 开展研究，”OpenAI 在写给本德的信里这样说，告诉她公司不会共享这个数据集，“我们在内部讨论过能否为此破例、怎样破例，但我们认为，短期内保持一致很重要。”

这段经历引起了格布鲁的共鸣。她说，她在谷歌也一直在倡导为数据集建立说明文档，并推动更有意识地筛选和整理数据集。

“也就是说，别再满网收集普通垃圾，还收得那么多，多到能把它冒充成好东西？”本德回复道，表示赞同。“我好像能看到一篇论文在这里成形了，”她接着说，“拿大语言模型做个案研究，分析伦理上的陷阱，以及哪些地方可以做得更好。”

“你有兴趣合写这样一篇东西吗？”她问。

不到两天，本德就给格布鲁发来了一份提纲。后来，她们想出了一个标题，还俏皮地加了一个表情符号以示强调：《论随机鹦鹉的危险：语言模型会不会太大？🦜》（“On the Dangers of Stochastic Parrots: Can Language Models Be Too Big? 🦜”）

格布鲁在谷歌内部为这篇论文组建了一个研究小组，其中包括她的联合负责人米切尔。为了回应迪恩在年度评估里的鼓励，她特意向他提起这篇论文，说这就是她正在开展的工作的一个例子。“这绝对不是我的专业领域[^18]，”迪恩说，“不过读一读肯定能学到东西。”

这篇论文汇集了几位作者在各个领域的专长和学识，批判性地分析了大语言模型的开发和部署可能怎样给社会带来负面影响。论文一共提出了四项[^19]关键警告。第一，大语言模型越来越庞大，正在留下巨大的环境足迹，斯特鲁贝尔的论文就发现了这一点。这可能加剧气候变化；气候变化最终会影响每一个人，但全球南方社区承受的负担格外沉重，这些社区本来就深受更广泛的政治、社会和经济困境之苦。第二，对数据的需求越来越大，公司在互联网上能找到什么就抓取什么，无意间收进了更多恶毒和辱骂性的语言，以及更隐蔽的种族主义和性别歧视内容。这同样可能让弱势群体受害最深，比如那名巴勒斯坦男子被错误逮捕，或者诺布尔书中记录的那些情形。第三，这么庞大的数据集很难审计和审查，要核实里面到底有什么极其困难，因此更难清除其中的恶毒内容，更难在更广泛的意义上确保这些数据反映不断变化的社会规范和价值观。最后，模型的输出越来越好，人们很容易把这些经过统计计算得出的输出，误当成带有真实意义和意图的语言。这样一来，人们不仅容易把这些文字当作事实信息来相信，还容易把模型看作称职的顾问、可以信赖的知己，甚至可能把它看作某种有感知的存在。

11 月，按照公司的标准流程，格布鲁申请谷歌批准她把“随机鹦鹉”论文投给一个顶尖的 AI 伦理研究会议发表。这时已经是她上司的萨米·本吉奥批准了。谷歌的另一位同事审阅了论文，提了一些有帮助的意见。但在幕后，几位作者毫不知情，这份论文草稿已经引起了高管们的注意，他们把它看作一个隐患。谷歌发明了 Transformer，在自己的各种产品和服务中广泛使用。如今 OpenAI 已经一跃领先，这家科技巨头无意放慢脚步：它正投身一场新的竞赛，要为自己的业务打造越来越大的、基于 Transformer 的生成式模型。

感恩节前一周的那个星期四，格布鲁已经把论文投给了会议，这时她收到一份没有任何说明的日历邀请：不到三小时后，和谷歌研究院工程副总裁梅根·卡乔利亚（Megan Kacholia）开视频会议。会议只开了三十分钟，卡乔利亚开门见山：格布鲁必须撤回这篇论文。

这个要求与谷歌乃至整个行业处理研究的一贯做法大相径庭。和其他公司的许多实验室一样，谷歌大脑此前基本上按学术机构的方式运作，给研究人员很大的自由，让他们去探究自己想研究的问题。公司有时会审查论文，确保其中没有泄露敏感的知识产权或客户数据。但在格布鲁这样的研究人员的印象里，公司从来没有仅仅因为一篇论文揭示了令人难堪的真相，就阻止它发表或者要求撤回。一些研究人员后来回想，谷歌之所以连这一步都肯走，一方面是因为 OpenAI 带来的新的竞争压力，另一方面也是因为 OpenAI 在 GPT-2 之后所做的那些事，让扣下研究成果不发表变得名正言顺。到了 GPT-3，透明度又在一点点降低。OpenAI 发表了一篇处理得干干净净的研究论文，几乎没有交代模型是怎样训练的（这在过去被视为学术发表起码要有的内容），却照样拿了一个研究奖项。

格布鲁猝不及防，要求对方说明情况。能不能更详细地解释一下问题出在哪里？能不能让她知道是哪些人有意见，好直接和他们谈？能不能修改或删掉某一部分，或者换一个所属机构的名义发表？每个问题得到的回答都是斩钉截铁的“不行”。卡乔利亚说，格布鲁最晚要在感恩节的第二天撤回论文。米切尔那天请假过生日，没有参加会议。格布鲁身边没有人可以依靠。渐渐明白卡乔利亚这番话有多沉重之后，格布鲁哭了起来。

卡乔利亚给本吉奥发了一份文件，列出论文的缺陷，但嘱咐他不要直接转给格布鲁。感恩节当天，本吉奥在电话里把文件念给格布鲁听。反馈意见里有这样的说法：论文对大语言模型的批评过于严厉，比如在环境影响和偏见问题上，却没有考虑到后来的研究已经表明这些问题可以怎样缓解。这个节日本该和家人一起过，格布鲁却把那天余下的时间都花在写一份详细的六页文件上，逐条反驳这些意见，并争取修改论文的机会。“我希望至少还有继续对话的余地，别只是继续下命令，”她在给卡乔利亚的邮件里写道，并附上了那份文件。

11 月 28 日星期六，格布鲁离开湾区的家，开车横穿美国，原本打算在节后好好放松一下。星期一，在新墨西哥州，格布鲁收到了卡乔利亚简短生硬的回复。回复完全没有理会她的反驳，只要求她确认：要么已经撤回论文，要么已经删掉论文上谷歌作者的名字，只留下埃米莉·本德这样的外部研究者。格布鲁感到受了羞辱。她在公司内部忍受过种种轻慢和骚扰，公司的员工也这样对待过她；如今公司又彻底否定她和她团队的研究，而这些研究正是公司当初雇用她的原因。这一次，她终于忍无可忍。

她回复了卡乔利亚。她可以把自己的名字从论文上撤下来，但有两个条件：公司要告诉她是谁给的反馈意见，还要建立一个更透明的流程来审查今后的研究。如果公司做不到，她会在帮团队完成过渡之后离开公司。格布鲁还在另一个内部邮件列表[^20]上发了第二封邮件，这个列表面向谷歌大脑的女性员工和支持女性的同事。她在邮件里用直白而尖刻的语言，详细讲述了自己的遭遇。“你们有没有听说过，有人是通过一份写给人力资源部、受法律特权保护的机密文件，收到对自己论文的‘反馈’的？”她写道，“还是说，这种事只会发生在我这种一直不被当人看的人身上？”

她接着写道，在谷歌，她已经习惯了同事们贬低她的专业能力，可现在，公司连让她在研究界发出自己的声音都不允许了。“黑人的命也是命”运动掀起风波之后，谷歌大谈多元化，这些话最后换来了什么？“以最根本的方式让人噤声，”她写道。

第二天晚上，在得克萨斯州奥斯汀，格布鲁收到一名直属下属惊慌失措的消息：“你辞职了？？”格布鲁完全不知道下属在说什么。她在自己的私人邮箱里看到了卡乔利亚的回复：“我们无法同意你提出的第 1 条和第 2 条要求。我们尊重你因此离开谷歌的决定。”卡乔利亚还写道，格布鲁不能留在公司帮团队完成过渡了，因为她发到女性邮件列表上的那封邮件，有些内容“不符合对谷歌管理者的期望”。“因此，我们即刻接受你的辞职。”

当天夜里，格布鲁在 Twitter 上宣布自己被解雇了。她的团队陪她在视频通话里一直熬到凌晨，大家一起哭，在共同的悲痛中互相支撑。就在他们说话的时候，格布鲁的推文在 AI 圈里迅速传开，拉开了 AI 研究界一场大动荡的序幕，也标志着企业审查越来越多、问责越来越少的趋势开始加速。

没过多久，格布鲁的推文就出现在了我的信息流里。那是 2020 年 12 月 2 日星期三，夜已经深了。格布鲁突然离开了谷歌，我一时还没有意识到这件事有多重大。和许多人一样，我早已把她的伦理 AI 团队看作批判性问责研究的一座堡垒，看作一个让人看到希望的信号：企业正在培养自我反思的能力。

接下来两天，随着格布鲁披露更多信息，记者们逐步揭开这场内部风波的来龙去脉，新消息接连不断。报道提到了她发到邮件列表上的那封邮件、卡乔利亚和格布鲁之间的僵持，以及围绕一篇论文的激烈争执。到星期五上午，Medium 上一封抗议谷歌如此对待格布鲁的公开信，已经像野火一样在科技界蔓延开来。“我们，以下签名者[^21]，声援蒂姆尼特·格布鲁博士，”信中写道，“她在遭受前所未有的研究审查之后……被解除了职务。”我必须拿到那篇论文。

那个星期五傍晚，发了一连串短信和邮件之后，我联系上了这项研究的一位合著者，她不必担心谷歌可能的报复：埃米莉·M.本德。她告诉我，她对谷歌不负有任何法律义务，而且她有终身教职。她用邮件把论文草稿发给了我。

我快速浏览了一遍，立刻明白了它为什么会惹恼谷歌。这份草稿讲的内容，大多没有超出已有研究的范围，但它把当时的种种状况编织成一篇犀利而全面的分析，让人看清科技行业像梦游一样，已经朝着一个可能危害重重的世界走了多远。这一切的根基是谷歌的技术发明，它既是这家公司的骄傲，也是它的利润来源：基于 Transformer 的语言模型改进了这家公司的吸金巨兽谷歌搜索，也把它喂得更加肥硕。

几小时后，我[^22]在《麻省理工科技评论》上发表了一篇报道，第一次详细披露了这篇论文的内容。公开信的签名人数很快翻了一番，达到将近 7000 人，来自学术界、公民社会和产业界，其中包括将近 2700 名谷歌员工。12 月 9 日，抗议仍在继续[^23]，谷歌首席执行官桑达尔·皮查伊（Sundar Pichai）发表了道歉声明。“一位才华横溢的杰出黑人女性领导者不愉快地离开了谷歌，我们必须为此承担责任，”他写道，“格布鲁博士是 AI 伦理这一重要领域的专家，我们必须继续在这个领域取得进展，而这种进展取决于我们能否向自己提出有挑战性的问题。”12 月 16 日，几位国会议员[^24]援引我的报道致信谷歌，要求了解事情的经过。

抗议持续了一年多[^25]。不到三个月后，谷歌又解雇了梅格·米切尔，抗议随之掀起第二波。谷歌称她违反了[^26]多项行为准则；米切尔当时一直在下载自己邮箱里与格布鲁被逐有关的邮件和文件。包括本吉奥在内的几名谷歌员工辞职；至少一个学术会议和几位研究人员拒绝了谷歌的赞助资金。谷歌试图[^27]平息源源不断的批评：它成立了一个新的负责任 AI 专业中心，还公开承诺推动多元化。“这对公司来说是一个痛苦的[^28]时刻，”谷歌的一位发言人说，“它让我们更加认识到，谷歌继续推进负责任 AI 的工作、从这次经历中吸取教训有多么重要。”

那一刻的意义也远远超出了格布鲁本人，甚至超出了谷歌本身。它成了困扰 AI 行业的种种交织在一起的难题的象征。它是一个警告[^29]：用两位研究者的话说，AI 巨头（Big AI）正越来越走上烟草巨头（Big Tobacco）的老路，为了逃避审视，不惜违背公众利益，歪曲和审查批判性的学术研究。它还凸显了其他许多问题，包括：人才、资源和技术全都集中在营利性的环境里，这让公司可以如此肆无忌惮，因为它们知道自己几乎不可能受到独立的事实核查；在最有权力掌控这些技术的地方，多元化依然少得可怜；员工如果试图站出来揭露企业不道德的做法，可能突然遭到强硬的报复，却没有相应的保护。

“随机鹦鹉”论文成了一声集结号，把一个核心问题清清楚楚地摆到了人们面前：我们正在用 AI 建造一个什么样的未来？由谁来建造，又为谁而建？

对杰夫·迪恩来说，伦理 AI 团队的瓦解直接打击了他的声誉。作为谷歌最早的[^30]一批员工之一，他参与搭建了最初的软件基础设施，正是这些设施让公司的搜索引擎能够扩展到服务数十亿用户。他的成就加上和蔼可亲的为人，让他享有传奇般的地位：他是谷歌内部最受敬仰的领导者之一，在整个 AI 研究界也备受尊重。格布鲁被逐之后，迪恩竭力为谷歌的做法辩护，这给他原本无瑕的履历蒙上了污点。卡乔利亚是迪恩的下属。迪恩对同事们说，“随机鹦鹉”论文“没有达到我们的发表标准”；即便后来这篇论文通过了同行评审，在一个会议上发表，他仍然坚持这个说法。

在他身边的人看来，这个污点似乎一直纠缠着他。风波过去很久之后，迪恩还在揪着这篇论文的缺点不放，好像在心理上始终过不去这道坎。他尤其耿耿于怀的，是论文里讨论大语言模型环境影响、引用斯特鲁贝尔研究的那一节。他提得太频繁，一些谷歌员工私下取笑他，说他的那些反对意见[^31]会被刻在他的墓碑上。多年来，他还一直在 Twitter 上毫不留情地批评斯特鲁贝尔的研究。

在迪恩看来，问题在于斯特鲁贝尔的研究严重高估了谷歌开发 Evolved Transformer 时实际产生的碳排放。斯特鲁贝尔是按标准 GPU 来推算所需能耗的。可谷歌用的是自家的专用芯片，也就是张量处理器（TPU），这种芯片能效更高；谷歌还用了其他技术，来降低整个开发流程的能耗。斯特鲁贝尔假设的是美国数据中心的平均能效。迪恩指出，谷歌的数据中心经过了更多优化，能把能源足迹降到最低。另外，有些人把斯特鲁贝尔的论文理解成，那些碳排放代价来自训练 Evolved Transformer；实际上，论文算的是开发这个神经网络的代价。迪恩认为，这是一次性的碳排放代价，换来的是一种实际上更节能的神经网络设计。

这些反对意见，其实都没有真正击中斯特鲁贝尔的研究。斯特鲁贝尔从来没有计算谷歌自己开发 Evolved Transformer 的实际环境影响，也从来没有声称算过。谷歌公开的数据中心细节不够多，根本没法这样计算。而且无论如何，斯特鲁贝尔认为更有用的[^32]做法，是以市面上最常见的 AI 芯片和数据中心为依据，估算设计这个神经网络的影响。这样得出的结果可以近似代表行业平均水平：不用谷歌硬件和基础设施的研究人员，如果采用谷歌的优化算法“神经架构搜索”，情况大概会是怎样。

但最让迪恩恼火的，似乎是别人误读了斯特鲁贝尔的研究，让谷歌显得糟糕得多。迪恩认为，“随机鹦鹉”论文可能让这个问题更加严重。格布鲁*明明*能看到谷歌的内部数据，却仍然引用斯特鲁贝尔的外部估算，这就可能让人以为，斯特鲁贝尔的计算准确反映了公司的排放量。在迪恩看来，这就证明他和其他高管对格布鲁论文的批评是有道理的：格布鲁如果想引用斯特鲁贝尔，就应该选一个*不*涉及谷歌 Evolved Transformer 的估算；如果想引用 Evolved Transformer，就应该去找谷歌的内部数据。

一些研究人员觉得这套逻辑漏洞百出，令人气恼。谷歌此前从未公开过这些内部数据，就连回应斯特鲁贝尔最初那篇论文时也没有；现在，它把自己不透明的责任推到格布鲁身上，同时又不让她引用基于合理假设、公开可得的估算。更别提公司在格布鲁还没来得及查阅内部数据、修改论文之前，就毫不客气地把她赶走了。这种进退两难的“第二十二条军规”，唯一可能的结果就是批判性问责研究遭到审查。

迪恩开始和一组研究人员合作，撰写一篇新论文，终于要公布谷歌真实的碳排放数据。为了这项合作，他联系了斯特鲁贝尔。斯特鲁贝尔这时已经是卡内基梅隆大学的助理教授，同时在谷歌兼职。起初，斯特鲁贝尔很兴奋，觉得可以借此让公众更清楚地了解 AI 的环境影响；可后来，斯特鲁贝尔开始怀疑：迪恩拉自己加入，是不是想借这个名字，为他对格布鲁研究的批评正名。谷歌的一位发言人说，之所以邀请斯特鲁贝尔[^33]，是因为“科学纠错”往往在原先出错的作者参与纠正时效果最好。

在一次气氛紧张的会议上，迪恩的合作者、谷歌另一位知名资深研究员戴夫·帕特森（Dave Patterson）直截了当地强调，参与这项研究对斯特鲁贝尔的职业生涯最有好处。这能让斯特鲁贝尔有机会改正之前的错误，还能因此得到认可。在斯特鲁贝尔听来，这番话里藏着一句威胁：不参加，吃亏的是你自己。尽管退出可能要付出代价，继续参与下去在斯特鲁贝尔看来却行不通。斯特鲁贝尔退出了合作。

2022 年 2 月，帕特森发表了一篇博客文章[^34]，介绍谷歌研究人员的这篇论文，题为《关于机器学习训练碳足迹的好消息》（“Good News About the Carbon Footprint of Machine Learning Training”）。这篇文章借公司的平台，直接批评斯特鲁贝尔最初的那篇论文。文章说，那项 2019 年的研究严重高估了谷歌开发 Evolved Transformer 的实际排放量，估算值是实际值的 88 倍。文章认为，这个错误出自两个问题：那项研究是在“没有现成条件使用谷歌硬件或数据中心”的情况下完成的，而且没有理解神经架构搜索运作方式中的“微妙之处”。谷歌的几位合著者在发表自己的数据之前做研究时，还联系了他们的前谷歌同事苏茨克维，想进一步了解 GPT-3 的情况。正是在那时，OpenAI[^35] 和微软才第一次同意公开这个模型的相关技术细节，用来计算它的能耗和碳排放影响。这时，斯特鲁贝尔已经对这个行业心灰意冷，结束了在谷歌的兼职。这场批评最终并没有损害斯特鲁贝尔的职业生涯。但这段经历带来的情绪消耗，让斯特鲁贝尔对继续研究大语言模型的环境影响变得更加迟疑。谷歌的一位发言人称这“令人遗憾”，并补充说：“推进这项研究需要许多研究人员参与，碳排放显然是一个重大问题。”

有那么一小段时间，强烈的反弹、抗议和谷歌声誉受到的损害，似乎预示着一场清算即将到来。但时间一长，找工作的研究人员和找经费的学者，再也无法无视这家科技巨头深不见底的钱袋。随着抵制逐渐平息，谷歌从这场惨败中走了出来，一套对批判性研究进行更全面审查的新流程，也在公司里成了常态。

ChatGPT 问世后，随着各家疯狂竞相把生成式 AI 系统商业化，这些规范变得更加牢固。OpenAI 基本上不再在研究会议上发表论文。行业里其余的公司几乎全都[^36]把自家有商业价值的模型的重要技术细节封锁起来，不再对外公开，因为它们如今把这些细节看作专有信息。2023 年，斯坦福大学的研究人员推出了一个透明度追踪指数，给 AI 公司打分，看它们有没有公开自家大型深度学习模型哪怕最基本的信息，比如模型有多少参数、用什么数据训练，以及模型的能力有没有经过独立验证。他们第一年评估的十家公司[^37]，包括 OpenAI、谷歌和 Anthropic，全部得了 F，最高分只有 54%。

透明度规范急转直下，最令人担忧的后果是科学诚信遭到侵蚀。深度学习研究的根基是一个简单的前提：用来训练模型的数据，和用来测试模型的数据*并非*同一批。如果无法审计训练数据，这种所谓“训练集与测试集分离”的范式就会土崩瓦解。模型在各种基准测试上得分更高时，它们的“智能”可能并没有真正提高。它们也许只是在背答案。

[^1]: **加入 DeepMind 后不久：** 那份备忘录的副本。

[^2]: **但高管们不感兴趣：** Karen Hao, Salvador Rodriguez, and Deepa Seetharaman, “Mark Zuckerberg Was Early in AI. Now Meta Is Trying to Catch Up,” *Wall Street Journal*, June 17, 2023, [wsj.com/articles/mark-zuckerberg-was-early-in-ai-now-meta-is-trying-to-catch-up-94a86284](http://wsj.com/articles/mark-zuckerberg-was-early-in-ai-now-meta-is-trying-to-catch-up-94a86284).

[^3]: **在中国，GPT-3 同样：** Jeffrey Ding and Jenny W. Xiao, *Recent Trends in China’s Large Language Model Landscape*, Centre for the Governance of AI, April 28, 2023, 1–14, [cdn.governance.ai/Trends\_in\_Chinas\_LLMs.pdf](http://cdn.governance.ai/Trends_in_Chinas_LLMs.pdf).

[^4]: **ChatGPT 证明了：** Raffaele Huang and Karen Hao, “Baidu Hurries to Ready China’s First ChatGPT Equivalent Ahead of Launch,” *Wall Street Journal*, March 9, 2023, [wsj.com/articles/baidu-scrambles-to-ready-chinas-first-chatgpt-equivalent-ahead-of-launch-bf359ca4](http://wsj.com/articles/baidu-scrambles-to-ready-chinas-first-chatgpt-equivalent-ahead-of-launch-bf359ca4).

[^5]: **2019 年 6 月，……埃玛·斯特鲁贝尔：** Emma Strubell, Ananya Ganesh, and Andrew McCallum, “Energy and Policy Considerations for Deep Learning in NLP,” *Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics* (July 2019): 3645–50, [doi.org/10.18653/v1/P19-1355](http://doi.org/10.18653/v1/P19-1355).

[^6]: **共消耗 1287 兆瓦时电能：** David Patterson, Joseph Gonzalez, Quoc Le, Chen Liang, Lluis-Miquel Munguia, Daniel Rothchild et al., “Carbon Emissions and Large Neural Network Training,” preprint, arXiv, April 23, 2021, [doi.org/10.48550/arXiv.2104.10350](http://doi.org/10.48550/arXiv.2104.10350).

[^7]: **其中包括一篇开创性的：** Joy Buolamwini and Timnit Gebru, “Gender Shades: Intersectional Accuracy Disparities in Commercial Gender Classification,” in *Proceedings of the 1st Conference on Fairness, Accountability and Transparency* (2018): 77–91, [proceedings.mlr.press/v81/buolamwini18a.html](http://proceedings.mlr.press/v81/buolamwini18a.html).

[^8]: **随后，布奥拉姆维尼又：** 那篇后续论文：Inioluwa Deborah Raji and Joy Buolamwini, “Actionable Auditing: Investigating the Impact of Publicly Naming Biased Performance Results of Commercial AI Products,” in *AIES ’19: Proceedings of the 2019 AAAI/ACM Conference on AI, Ethics, and Society* (January 2019): 429–35, [doi.org/10.1145/3306618.3314244](http://doi.org/10.1145/3306618.3314244)；美国政府的审计：Patrick Grother, Mei Ngan, and Kayee Hanaoka, *Face Recognition Vendor Test (FRVT) Part 3: Demographic Effects*, NISTIR 8280, National Institute of Standards and Technology, December 2019, [doi.org/10.6028/NIST.IR.8280](http://doi.org/10.6028/NIST.IR.8280).

[^9]: **两年后，声势浩大的民权倡导运动：** Buolamwini 的研究和倡导工作的完整经过，见她的畅销回忆录：Joy Buolamwini, *Unmasking AI: My Mission to Protect What Is Human in a World of Machines* (Random House Trade Paperbacks, 2024)；以及 Netflix 纪录片：*Coded Bias*, directed by Shalini Kantayya (2020; Brooklyn, NY: 7th Empire Media), Netflix. 关于“Gender Shades”和“Actionable Auditing”两篇论文的深远影响，另见：“Celebrating 5 Years of Gender Shades,” Algorithmic Justice League, accessed on January 15, 2025, [gs.ajl.org/](https://gs.ajl.org/).

[^10]: **Black in AI 带动：** Karen Hao, “Inside the Fight to Reclaim AI from Big Tech’s Control,” *MIT Technology Review*, June 14, 2021, [technologyreview.com/2021/06/14/1026148/ai-big-tech-timnit-gebru-paper-ethics](http://technologyreview.com/2021/06/14/1026148/ai-big-tech-timnit-gebru-paper-ethics).

[^11]: **和格布鲁搭话：** 作者对 Timnit Gebru 的采访，2023 年 8 月。

[^12]: **2017 年，Facebook 的一个语言模型：** Alex Hern, “Facebook Translates ‘Good Morning’ into ‘Attack Them,’ Leading to Arrest,” *The Guardian*, October 24, 2017, [theguardian.com/technology/2017/oct/24/facebook-palestine-israel-translates-good-morning-attack-them-arrest](http://theguardian.com/technology/2017/oct/24/facebook-palestine-israel-translates-good-morning-attack-them-arrest).

[^13]: **萨菲娅·乌莫贾·诺布尔出版了《算法压迫》：** Safiya Umoja Noble, *Algorithms of Oppression: How Search Engines Reinforce Racism* (NYU Press, 2018), 1–248.

[^14]: **OpenAI 只是在介绍这个模型的研究论文里承认：** GPT-3 论文第 6.2 节 “Fairness, Bias, and Representation”（公平、偏见与代表性）讨论了在模型中发现的几种不同类型的偏见，随后写道：“我们给出这项初步分析，是为了分享我们发现的一些偏见，以推动进一步的研究。” Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal et al., “Language Models Are Few-Shot Learners,” in *NIPS ’20: Proceedings of the 34th International Conference on Neural Information Processing Systems*, no. 159 (2020): 1877–901, [dl.acm.org/doi/abs/10.5555/3495724.3495883](http://dl.acm.org/doi/abs/10.5555/3495724.3495883).

[^15]: **格布鲁在邮件讨论串里插了话：** 关于 Gebru 围绕“随机鹦鹉”论文的经历，叙述主要依据作者对 Gebru 的采访（2020 年至 2024 年，其中一次是在她被逐出谷歌的第二天），以及以下报道中的详细叙述：Tom Simonite, “What Really Happened When Google Ousted Timnit Gebru,” *Wired*, June 8, 2021, [wired.com/story/google-timnit-gebru-ai-what-really-happened](http://wired.com/story/google-timnit-gebru-ai-what-really-happened).

[^16]: **如果没有，她愿意：** Gebru 与 Emily M. Bender 之间的对话，摘自双方往来消息的截图，由 Bender 提供。

[^17]: **“我们开展这些初期”：** 邮件副本，由 Bender 提供。

[^18]: **“这绝对不是我的专业领域”：** Simonite, “What Really Happened.”

[^19]: **论文一共提出了四项：** Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, and Shmargaret Shmitchell [Meg Mitchell], “On the Dangers of Stochastic Parrots: Can Language Models Be Too Big? 🦜” in *FAccT ’21: Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency* (March 2021): 610–23, [doi.org/10.1145/3442188.3445922](http://doi.org/10.1145/3442188.3445922). 由于本章详述的原因，谷歌不允许 Meg Mitchell 发表这篇论文，于是她在论文上署名 Shmargaret Shmitchell，还为此注册了一个对应的电子邮箱。她填写的所属机构是“以太”（“the Aether”）。（译者注：英语口语里常把一个词的开头换成 shm 再重复一遍，表示不屑或调侃，例如 fancy-shmancy；Shmargaret Shmitchell 就是这样从 Margaret Mitchell 变来的。）

[^20]: **另一个内部邮件列表：** Casey Newton, “The Withering Email That Got an Ethical AI Researcher Fired at Google,” Platformer, December 3, 2020, [platformer.news/the-withering-email-that-got-an-ethical](http://platformer.news/the-withering-email-that-got-an-ethical).

[^21]: **“我们，以下签名者”：** Google Walkout for Real Change, “Standing with Dr. Timnit Gebru—#ISupportTimnit #BelieveBlackWomen,” Medium, December 3, 2020, <https://googlewalkout.medium.com/standing-with-dr-timnit-gebru-isupporttimnit-believeblackwomen-6dadc300d382>.

[^22]: **几小时后，我：** Karen Hao, “We Read the Paper That Forced Timnit Gebru out of Google. Here’s What It Says,” *MIT Technology Review*, December 4, 2020, [technologyreview.com/2020/12/04/1013294/google-ai-ethics-research-paper-forced-out-timnit-gebru](http://technologyreview.com/2020/12/04/1013294/google-ai-ethics-research-paper-forced-out-timnit-gebru).

[^23]: **12 月 9 日，抗议仍在继续：** Ina Fried, “Scoop: Google CEO Pledges to Investigate Exit of Top AI Ethicist,” Axios, December 9, 2020, [axios.com/2020/12/09/sundar-pichai-memo-timnit-gebru-exit](http://axios.com/2020/12/09/sundar-pichai-memo-timnit-gebru-exit).

[^24]: **12 月 16 日，几位国会议员：** Karen Hao, “Congress Wants Answers from Google About Timnit Gebru’s Firing,” *MIT Technology Review*, December 17, 2020, [technologyreview.com/2020/12/17/1014994/congress-wants-answers-from-google-about-timnit-gebrus-firing](http://technologyreview.com/2020/12/17/1014994/congress-wants-answers-from-google-about-timnit-gebrus-firing).

[^25]: **抗议持续了一年多：** Ina Fried, “Google Fires Another AI Ethics Leader,” Axios, February 19, 2021, [axios.com/2021/02/19/google-fires-another-ai-ethics-leader](http://axios.com/2021/02/19/google-fires-another-ai-ethics-leader).

[^26]: **谷歌称她违反了：** Sam Shead, “New Google Union ‘Concerned’ After a Senior A.I. Ethics Researcher Is Reportedly Locked Out of Her Account,” CNBC, January 21, 2021, [cnbc.com/2021/01/21/margaret-mitchell-google-investigating-ai-researcher-awu-concerned.html](http://cnbc.com/2021/01/21/margaret-mitchell-google-investigating-ai-researcher-awu-concerned.html).

[^27]: **谷歌试图：** Sepi Hejazi Moghadam, “Marian Croak’s Vision for Responsible AI at Google,” *The Keyword*, February 18, 2021, [blog.google/technology/ai/marian-croak-responsible-ai](https://blog.google/technology/ai/marian-croak-responsible-ai/).

[^28]: **“这对公司来说是一个痛苦的”：** 作者与谷歌发言人的通信，2024 年 11 月。

[^29]: **它是一个警告：** Mohamed Abdalla and Moustafa Abdalla, “The Grey Hoodie Project: Big Tobacco, Big Tech, and the Threat on Academic Integrity,” in *AIES ’21: Proceedings of the 2021 AAAI/ACM Conference on AI, Ethics, and Society* (July 2021): 287–97, [doi.org/10.1145/3461702.3462563](http://doi.org/10.1145/3461702.3462563).

[^30]: **作为谷歌最早的：** James Somers, “The Friendship That Made Google Huge,” *New Yorker*, December 3, 2018, [newyorker.com/magazine/2018/12/10/the-friendship-that-made-google-huge](http://newyorker.com/magazine/2018/12/10/the-friendship-that-made-google-huge).

[^31]: **说他的那些反对意见：** Simonite, “What Really Happened.”

[^32]: **斯特鲁贝尔认为更有用的：** 作者对 Emma Strubell 的采访，2023 年 11 月。

[^33]: **谷歌的一位发言人说，之所以邀请斯特鲁贝尔：** 与谷歌发言人的通信，2024 年 11 月。

[^34]: **帕特森发表了一篇博客文章：** David Patterson, “Good News About the Carbon Footprint of Machine Learning Training,” *Google Research* (blog), February 15, 2022, [research.google/blog/good-news-about-the-carbon-footprint-of-machine-learning-training](http://research.google/blog/good-news-about-the-carbon-footprint-of-machine-learning-training).

[^35]: **正是在那时，OpenAI：** 与谷歌发言人的通信，2024 年 11 月。

[^36]: **行业里其余的公司几乎全都：** Nitasha Tiku and Gerrit De Vynck, “Google Shared AI Knowledge with the World—Until ChatGPT Caught Up,” *Washington Post*, May 4, 2023, [washingtonpost.com/technology/2023/05/04/google-ai-stop-sharing-research](http://washingtonpost.com/technology/2023/05/04/google-ai-stop-sharing-research).

[^37]: **他们第一年评估的十家公司：** Rishi Bommasani, Kevin Klyman, Shayne Longpre, Sayash Kapoor, Nestor Maslej, Betty Xiong et al., *The Foundation Model Transparency Index* (Stanford Center for Research on Foundation Models, October 2023), [crfm.stanford.edu/fmti/October-2023/index.html](http://crfm.stanford.edu/fmti/October-2023/index.html).
