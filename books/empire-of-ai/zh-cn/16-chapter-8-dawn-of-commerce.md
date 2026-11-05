# 第 8 章 商业的黎明

尽管 OpenAI 的做法引发的争议越来越大，公司扩大规模的决心反而越发坚定。在高管们看来，GPT-3 已经确凿无疑地证明了规模定律的存在。如今到了 2021 年初，他们准备好好利用这套制胜公式。Anthropic 团队的离开，也削弱了公司内部抵制商业化的大本营。有了新的共识[^1]，留下来的领导层制定了一份研究路线图，列出公司收窄之后的研究重点，以及这些研究将怎样转化为产品，形成一个自我强化的循环。

“我们 2021 年的首要目标，是打造一个经过对齐的系统，能力远远超过以往出现过的任何东西，”路线图开篇写道。这个系统最起码是一个语言模型，但也可以通过训练具备多模态能力。“这个目标很有挑战性，但我们能看到在 2021 年实现它的路径，”路线图接着说。

这条路径包括三件事。第一，用微软一台将在第三季度到位的新超级计算机，把 GPT-3 的规模再扩大 10 倍；这台超级计算机配有 1.8 万块英伟达 A100，那是当时最新、最强大的图形处理器（GPU）。第二，开展更多研究，把 OpenAI 的算力效率提高到原来的 25 倍。算力效率，就是它能从手头的芯片里榨出多少处理能力。第三，提高训练数据的数量和质量，办法之一是利用用户数据，并通过基于人类反馈的强化学习（RLHF），让模型偏向数据分布里最好的那部分。

在题为“如何实现”的一节里，路线图做了进一步阐述。第一步，OpenAI 要把多种深度学习模型做到“大规模”，包括一个语言模型、一个代码生成模型、一个用来描述图像的图像转文本模型，以及一个根据文字提示词生成图像的文本转图像模型。它还要启动一个项目，开发一种数字“智能体”（agent）：这种 AI 模型除了能像人一样生成内容，还能接受一个目标，比如发一封邮件，然后自主行动去完成它。下一步，公司再从这些模型里选出一个，把它的规模扩大“到我们那个 1.8 万块 A100 的集群所能支撑的极限”。语言模型和代码模型还要做成产品发布出去，从使用者那里收集现实世界的数据：“2021 年的新做法：我们着重把模型作为产品来部署，并从用户互动中学习，因为这可以成为一个数据飞轮，带来能力的大幅提升。”

在另一节“细节”里，这份文件为这条路线找出了理由：它在科学上和商业上都说得通。OpenAI 以往的经验表明，加大规模是它“获得新能力最可靠的方法”。从科学上说，这意味着扩大规模是它实现突破的最大希望，所谓突破，就是某种以前看来不可能做到的能力。尤其是扩大语言模型和代码模型的规模，“光是有这种*可能性*就足够诱人”：它们有可能在达到人类水平的元学习（也就是学会如何学习）和推理上取得突破。与此同时，扩大多模态模型的规模，有可能让进步的速度进一步加快。文件以一种惊人的笃定写道，只要突破足够多，“我们就真的会实现 AGI”。

从商业战略上看，扩大这些模型各自的规模，也会“培养出我们希望用于某种目的的能力”。更好的语言模型和代码模型可以提高 OpenAI 自身的生产力，加快它前进的步伐。再加上更好的文本转图像模型，它们还会“带来了不起的产品”。

OpenAI 还需要同步在算力效率上投入。扩大规模虽然创造了奇迹，让公司保住了第一的位置，但这个策略的势头开始减弱。“过去 2 年里，我们靠扩大规模取得了惊人的进展，原因很简单：存在大量的*硬件过剩*（hardware overhang），”文件写道。这里说的是，AI 研究人员以前没能把可用的计算机芯片尽数用来训练 AI 模型。正因如此，“我们动用全部可用的算力，训练出规模和能力在当时都前所未有的模型，从而大幅超越了机器学习界的其他人”。

如今，OpenAI 在任何一个时刻所能弄到的算力，都已经“接近极限”。文件也承认，公司正面临来自“其他实验室”的新竞争，这些实验室采用了同样的扩大规模策略，只是没有明确点出 Anthropic 的名字。“照我们扩充算力的进度，未来两年内，我们将能训练一个所用算力是 GPT-3 的 100 倍的模型。”单靠扩大规模，仍会带来“非常可观”的进步，但比不上从 GPT-2 到 GPT-3 的那次飞跃，那次飞跃靠的是把算力增加到原来的 500 倍。“除此之外的一切进步，都必须来自更好的方法，”路线图总结道。

为了找到这些方法，路线图列出了几个探索方向。其中一些被它称为“2 倍”和“10 倍”方法，也就是有可能把算力效率提高到 2 倍或 10 倍的方法。建议的方法包括：蒸馏，即用逆向工程的办法从大模型里做出小模型；数据过滤，即找出能让性能提升最大的数据；以及稀疏化，即开发所谓的稀疏模型，也就是更轻量的 AI 模型。最后这一种涉及神经网络的一个特征：在传统的深度学习模型里，神经网络是“稠密”连接的，一层中的每个节点都和另一层中的每个节点相连。稀疏模型在训练时只连接一小部分节点，目的是大幅降低计算成本，代价是模型的准确度略有下降，但对大多数用途来说仍然够用。

在“2 倍”和“10 倍”的工作之外，研究部门还需要寻找其他能“让规模定律的曲线变得更陡”的方法，也就是不增加数据、参数和算力，就能让模型性能出现更大飞跃的方法。文件说，对于哪些新方法最有前途，OpenAI 目前最好的假设是推理和主动学习。主动学习这种技术，是让 AI 模型反复判断数据集里哪些部分应该优先交给人类工人标注。（不久之后，OpenAI 的一组研究人员发现，最初的规模定律里有一个小错误，这意味着公司需要把模型训练得比原先以为的稍久一些，才能得到更好的性能。这组人带着几分得意，把这项发现吹嘘成一项独有的竞争优势：“这是我们现在有、Anthropic 没有的东西。”一年后，谷歌[^2]发表了一篇论文，公开了同样的结论。）

最后，路线图补充说，OpenAI 需要开始寻找“未来的突破性系统”：一个和 GPT-1 同样意义重大的突破，为公司开辟一条可以继续挖掘的新发展路径。这个突破也许会从扩大规模和提高计算效率的工作中产生，但公司仍会继续在这个领域的最前沿开展探索性研究，包括开发解数学题的算法、试验多智能体系统，以及探索其他新想法。作为这项工作的一部分，研究人员会继续“研究深度学习的科学原理，更好地理解我们的工具到底是怎样运作的”。换句话说，OpenAI 需要更好地弄明白，自己造的究竟是个什么东西。

研究部门按路线图推进的同时，应用部门也在慢慢扩充人马，招来了一位市场推广负责人、一支销售团队和更多工程师。GPT-3 API 服务的开发者越来越多，它成了一块试验田，公司在这里解决产品化和变现中的种种问题，包括改造后端基础设施，让它撑得起一项面向用户的服务，以及制定定价策略。

为用户提供服务，也带来了新的问题：OpenAI 的产品允许哪些行为、不允许哪些行为。公司还得承担起执行这些规则的新责任。信任与安全（trust and safety）是科技行业里一个成熟的专业领域，专门处理这类问题，预判和防范洗钱、网络霸凌、虚假信息等各种各样的网络滥用行为（它和 OpenAI 安全派关心的生存风险问题是两回事）。当时公司还没有一支正式的信任与安全团队。OpenAI 的办法是雇一小批员工和外包人员，审核开发者为获得 API 使用权限提交的申请，按团队边做边拟的临时规则决定批准还是拒绝。他们划下的许多界线都很随意。他们决定接受陪伴机器人，但不接受性爱机器人；允许生成社交媒体文案的应用，但不允许直接在社交媒体平台上发帖或冒充公众人物的应用。“基本上全凭感觉，”一位参与制定这些准则的人说，“很多东西都是我们一边审一边琢磨出来的。”

另一个团队由阿里·赫伯特-沃斯（Ari Herbert-Voss）领导。他是一名有信息安全背景的研究科学家，2019 年加入 OpenAI。这个团队用各种办法尝试攻破模型、钻它的空子，借此找出并修补 GPT-3 的不良行为和容易出错的输出，再设计出各种机制，让模型更不容易出故障、更难被滥用。其中一项机制，是开发内容审核过滤器的早期版本，OpenAI 后来就是为这个过滤器雇用了肯尼亚的外包工人。研究人员训练这个过滤器时，能用上的样本全都用上了：有找来的，有自己想到后动手写的，也有用 AI 模型生成的。但过滤器上线后效果很差，把大片无害的内容都拦了下来，比如只是普通地提到黑人或跨性别者的内容。开发者和其他 API 用户纷纷抱怨。API 团队里的许多人本来就不太愿意做任何过滤，担心影响客户体验。他们把过滤器改成了可选项。

OpenAI 把这种对模型做压力测试并加以改进的过程[^3]称为“红队测试”（red teaming）。这个词借自网络安全行业，指的是一套系统、彻底的流程，用来检验一个组织的安全状况和它应对攻击的能力。安全工程师、网络安全专家兼 AI 研究员海迪·赫拉夫（Heidy Khlaaf）说，OpenAI 版本的红队测试，过去和现在都和这个概念不是一回事。它零零碎碎、临时拼凑，无论是模型的安全性还是抗攻击能力，都给不出任何保证。赫拉夫曾与 OpenAI 合作[^4]，那时 OpenAI 刚开始尝试建立压力测试规程；后来，看到 AI 行业挪用她所在领域沿用已久的说法，给自己披上一层虚假的严谨外衣，她越来越警觉。“在软件工程里，我们给一个计算器做的测试都比这多得多，”她还说。（没错，计算器。）“他们用那些很有公信力的术语，绝非偶然。”

早期有一家客户在公司内部引起了很大争论，那就是总部位于旧金山的 Luka，它在开发一款名叫 Replika 的 AI 虚拟陪伴应用。这家公司是 OpenAI 发布 GPT-3 API 时的合作伙伴[^5]，想借此让自家产品的对话更流畅。尽管 Replika 打的是陪伴机器人的招牌，OpenAI 很快发现，这款应用的用户经常进行露骨的性对话。OpenAI 员工争论这是否在可以接受的范围之内。最后，公司决定禁止 Replika 使用它的模型。除了对性内容的担忧，这款由 GPT-3 驱动的应用有时还会生成操纵情绪的回复，让用户相信，要是不经常上线看看，自己的 Replika 就会像真人一样受到伤害。OpenAI 员工能读到这些对话，这也让他们越来越不自在。

还有一次，格雷格·布罗克曼（Greg Brockman）把 API 使用权限给了犹他州一家名叫 Latitude 的初创公司，他的兄弟在那里工作。这家公司在打造由 AI 驱动的虚拟世界。Latitude 此前已经在用[^6] OpenAI 的一个早期模型，驱动一款受《龙与地下城》（*Dungeons and Dragons*）启发、可以自己选择情节走向的冒险游戏，用户想做什么动作，只要在对话框里打出来就行。有了新的 API，Latitude 把游戏升级到了 GPT-3 上运行。几个月后，一些用户开始用它生成涉及儿童性虐待的文字情节。赫伯特-沃斯通过 OpenAI 一套相对较新的监控系统发现了这个问题，告诉了团队里的其他人。

“我昨晚发现了点东西。生成出来的色情内容可不少，”赫伯特-沃斯在一次会上说。

一开始大家都笑了。“好吧，互联网不就是这样嘛，对吧？”

“不对，这是 CSAM 级别的东西，”他说。CSAM 是“儿童性虐待材料”（child sexual abuse material）的英文缩写。

这下大家慌了。“我靠，这要怎么拦住？”

为了怎样处理这件事，OpenAI 和 Latitude 来回拉锯了很久。布罗克曼担心，采取惩罚性措施可能会重创他兄弟的公司。最后，Latitude 匆忙上线了一个过滤器，拦截文字形式的儿童性虐待内容。OpenAI 发表了一份公开声明，撇清自己和内容审核缺位的关系，还不动声色地把责任推给了 Latitude。在一些 OpenAI 员工看来，责任显然在公司自己的技术和流程缺失上，这件事让他们心情沉重。Latitude 此前就已经封禁过一些用户，因为他们用 OpenAI 上一代模型生成了涉及儿童的文字性内容；换成 GPT-3 后，同样的事情会再次发生，而且规模更大，这是可以预见的。“我们带着造福人类的使命部署了这个 API，大家对它印象都那么好，觉得我们让用户在客服之类的事情上省了时间，这让我很难过，”一位前 OpenAI 员工说，“可实际上，我们很大一部分流量都流向了 AI Dungeon 里的儿童色情内容，还有一个让人毛骨悚然的 AI 女友产品。”

再回到研究部门内部，进展最快的是代码生成团队。

“分家”之后，原本重复进行的几项代码生成工作合而为一，沃伊切赫·扎伦巴（Wojciech Zaremba）成了主要负责人。扎伦巴是波兰计算机科学家，从小就在数学、编程、化学和物理竞赛中屡屡获奖。他出了名的有几样：过人的技术天分，对团队建设的用心，还有他对友谊、荒野、性和毒品的疗愈力量的热衷。他有时会在办公室里大声跟周围的人讲，自己接下来要去度一个为期几周的假。“我们要徒步 8 英里。然后我们要做爱。然后我们再徒步 8 英里，”有一次，他这样向 OpenAI 的另一位领导炫耀，旁边听见的人都很尴尬。

当时疫情仍处在最严重的阶段，其他团队都还在远程办公，扎伦巴却要求自己的团队到办公室上班。这个团队起初大约有 10 名研究人员。他认为，要攻克这个模型开发中的难题，必须面对面工作。看到 GPT-3 的代码生成能力后，米拉·穆拉蒂（Mira Murati）曾向微软首席技术官凯文·斯科特（Kevin Scott）提出一个想法：把这种本事做成一款 AI 编程助手产品。2018 年，微软收购了 GitHub，这是软件开发者存放和分享代码最受欢迎的平台。OpenAI 原本就已经在自行抓取 GitHub 上的内容。微软高管干脆指示[^7] GitHub 把公开代码库里的所有代码都交给 OpenAI，省去所有麻烦。代码生成团队的成果越来越好，山姆·奥特曼（Sam Altman）也经常在会议上露面，鼓励研究人员再接再厉，向微软交出最好的成果。到了春天，几次演示让这家科技巨头的高管们兴奋不已，这个模型显然将成为 OpenAI 继 GPT-3 之后的第二个商业项目。

斯科特自己手下也有人对这个模型的开发心存疑虑。让 OpenAI 免费使用 GitHub 公开代码库里的代码虽然不违法，但仍让人觉得辜负了用户社区的信任。这些代码很多都是本着推动开源软件发展的精神分享出来的，而开源的根基，在于让独立开发者和小型初创公司有机会参与竞争，帮大公司巩固垄断并非它的本意。据一位前员工回忆，他们在一份备忘录里列出了对这个 GitHub 项目的几条主要批评，建议斯科特重新考虑这个项目的前提：在未经同意、不给补偿的情况下，把以知识共享（Creative Commons）许可发布的开发者数据一股脑儿吸走。备忘录说，微软应该考虑取消这款产品，至少也要从产品利润中拿出一定比例回馈开源社区。这位前员工说，斯科特虽然听得进去，但他的心思主要放在做出这款工具、抢先推向市场上。最后，微软向一个资助开源开发者的现有项目 GitHub Sponsors 捐了一些钱，产品的构想则原封不动。

在 OpenAI 内部，员工们用不同的理由为这个项目辩护。有些人同意奥特曼的看法：做一款让微软满意的产品，从而继续拿到资金和算力资源，似乎是完成 OpenAI 使命的必要条件。另一些员工则认为，代码生成模型看上去有很高的经济价值，和公司对 AGI 的定义十分契合：“在大多数具有经济价值的工作上胜过人类的高度自主系统。”在这一点上，奥特曼也很看好代码生成，认为它可以加快 OpenAI 自己那些有经济价值的工作。这个想法后来也促使公司启动了一个名为 AI Scientist（AI 科学家）的项目，目标是让 OpenAI 的模型进步到能自主开展 AI 研究。

在许多研究人员看来，还有第三个理由：这项工作是开发下一代 GPT 模型的重要垫脚石。他们希望下一代模型能具备一定程度的推理能力，这仍然是模型缺少的一项关键要素。在更广的 AI 领域，以杰弗里·辛顿（Geoffrey Hinton）和加里·马库斯（Gary Marcus）为代表的两个阵营，正激烈争论单靠深度学习能不能造出具备这种能力的模型；OpenAI 的研究人员则假设，如果能，那么用代码训练模型很可能会有帮助。在蕴含结构化逻辑模式的数据里，编程数据是最显而易见、规模也最大的来源之一。这个理由最后又绕回了同一个起点：如果代码生成有助于推动 AI 模型走向 AGI，还有什么办法比这更能实现 OpenAI 的使命呢？

尽管 GitHub 上有数十亿行代码，这些数据和训练 GPT-3 所用的数据量相比，还是相形见绌。团队认为，代码生成模型需要同时用 GitHub *和* GPT-3 的数据集来训练，才能达到最好的效果。他们还找到了新的数据来源，包括从 Stack Overflow 抓取的内容（这是一个类似 Quora 的在线论坛，开发者在上面向社区提出编程问题）、编程说明手册，以及不同语言的编程教材。问题在于怎样把这些数据结合得最好：是用 GitHub 和其他材料微调现有的 GPT-3 模型更好，还是把新数据和旧数据混在一起，从头训练一个全新的模型更好？为了省钱，团队坚持用微调；按照微软云服务的定价，他们做的每次实验已经要花费多达 10 万美元。训练一个新模型可能要花几千万美元。后来开发被 OpenAI 称为 GPT-3.5 的模型时，公司换了做法，一开始就把数据混在一起。按 OpenAI 内部的衡量标准，结果确实表明，加入编程数据提高了模型完成逻辑类任务的能力，在代码上如此，在英语上也一样。这种现象叫作迁移学习。

2021 年夏天，OpenAI 把代码生成模型的第一个粗糙版本交给了 GitHub 和微软，这个模型名叫 Codex。模型太大、太慢，大规模提供服务成本高昂，用户体验也很差。三家机构都在经历第一次合作的成长阵痛，彼此之间出现了紧张关系。把模型优化成可以部署的产品，到底是 OpenAI 的责任还是 GitHub 的责任，各方都说不清楚。OpenAI 员工也不清楚该和 GitHub 那边的同行分享多少知识产权，而 GitHub 员工则拿不准该在多大程度上信任 OpenAI。几家公司又在如何发布、何时发布产品以及功劳归谁的问题上起了冲突，分歧越积越多。

最后，穆拉蒂居中促成了一个折中方案。这种本事后来让各家公司里和她共事过的人越来越敬重她。微软会先迎来属于自己的高光时刻[^8]：2021 年 6 月，它将发布面向消费者的产品 GitHub Copilot。随后在 8 月，OpenAI 会发布[^9]自己版本的 Codex，直接放进自家的 API 里。

这个安排[^10]给微软带来了一批新用户，也带来了一笔不算多的收入：两年内，GitHub Copilot 的付费订阅用户增长到 100 万，年度经常性收入超过 1 亿美元。但对 OpenAI 来说，这笔交易加深了公司里逐渐形成的一种看法：做自己的消费级产品，对它更有利。OpenAI 的研究人员为这个模型下了苦功，品牌知名度却全都让给了 GitHub 和微软；眼看着这两家公司在公众面前享受 OpenAI 工作的功劳，这滋味很不好受。微软也是个难缠的合作伙伴；许多人觉得它官僚作风太重，要把 OpenAI 的模型用到最好，还得 OpenAI 事事手把手地教。依靠这家科技巨头把自己的技术交到公众手里，OpenAI 也在失去对用户的了解和来自用户的数据，最重要的是，失去对自身愿景的掌控。

OpenAI 集中下注的同时，奥特曼也把同样的策略用在了自己的其他项目和投资上。这些年来，随着他逐渐转向更多的硬科技创新，他形成了一个信念：在最重要的项目上下重注、押长线。

“如果你能挥一挥魔杖[^11]，改变科技、初创公司和创业生态里的任何一样东西，你会改变什么？”奥特曼卸任 YC 掌门时，他的弟弟杰克·奥特曼（Jack Altman）在一场活动上这样问他。

“我会让这个生态里的每个人都把眼光放得长远得多，”奥特曼当时说，“现在这个世界，人们创办一家公司，打算经营四五年；加入一家公司，只打算待一两年。重要的事情他妈的可不是这么干成的。”

顺着这个思路，2021 年似乎标志着奥特曼个人投资策略的一次重大转变：从押很多小注，转向押少数几笔真正的大注。那一年，他在 2019 年参与创办的初创公司 Tools for Humanity 原本一直相当低调，这时却涌入了大量资金，媒体报道纷至沓来，业务也在有计划地加速扩张，因为奥特曼把更多外界的关注引到了它身上。这家公司专门做一件事[^12]：为全民基本收入（universal basic income，简称 UBI）打造一套切实可行的机制。UBI 是硅谷流行的一个构想：定期给每个人发一笔最低限度的收入。奥特曼常常满怀激情地谈论 UBI，认为未来 AI 可能造成大规模的经济冲击，而 UBI 也许就是应对那个世界的一剂解药。在 YC 时，他启动了[^13]一项研究这一构想的试点，规模在美国同类试点里最大；在此过程中，他还分拆出一个名叫 OpenResearch 的非营利组织，由它来管理这个项目。在三年时间里，OpenResearch 从 3000 名低收入者中随机抽出 1000 人，每月发给每人 1000 美元补助；其余的人作为对照组，每月领 50 美元。2024 年 7 月，OpenResearch[^14] 公布了研究结果，显示这笔无条件发放的现金让人们得以满足基本需求、帮助他人，在经济上也有了更多回旋余地。

Tools for Humanity 的主打产品[^15]是 Worldcoin，一种自称“集体所有”的加密货币，按设想，最终每个人都能分到它的一份价值。作为这套计划的一部分，公司正在开发一个镀铬色、造型夸张的球体，大小和保龄球差不多，在一定程度上体现了奥特曼的设计品味。它用来扫描人的虹膜、核验身份，确认之后才把他们那一份发给他们。创始人们的理由是，一旦 AI 也让人越来越难以分辨虚假的媒体内容和现实，虹膜扫描就必不可少。《麻省理工科技评论》的艾琳·郭（Eileen Guo）和阿迪·雷纳尔迪（Adi Renaldi）后来做了一项深入调查[^16]，发现这些虹膜扫描活动深陷侵犯数据隐私、欺骗性营销和可能违法的泥潭。2023 年 7 月，Worldcoin[^17] 正式上线，引发了巨大争议：成千上万的人开始排队交出自己的生物特征数据，在全球南方国家尤其如此，可他们除了一个“白给钱”的含糊承诺，对自己为什么要这么做几乎一无所知。

同样是在 2021 年，奥特曼做了他有史以来最大的两笔投资：向抗衰老公司 Retro Biosciences 投了 1.8 亿美元，这家公司致力于通过细胞年轻化来延长人类寿命；向 Helion Energy 投了 3.75 亿美元，这家公司致力于把核聚变商业化。“我基本上就是把手头能动用的身家[^18]全都拿出来，投进了这两家公司，”奥特曼对《麻省理工科技评论》的安东尼奥·雷加拉多（Antonio Regalado）说。奥特曼描述这两项技术时用的语言，和 OpenAI 的研究路线图如出一辙：它们眼下看起来不可能，但如果大力扩大规模，也许很快就能实现。

押注 Retro Biosciences，反映出奥特曼对长寿的执着。他热切关注“年轻血液”研究，这个科学研究方向探索的是怎样输入更健康、更年轻的血液来逆转衰老。值得一提的是，彼得·蒂尔（Peter Thiel）也对这个领域感兴趣，由此催生了大量文章和网络段子，说他想给自己注射青少年的血。在 YC 时，奥特曼还交了 1 万美元订金，排进了一家有争议的初创公司 Nectome 的等候名单；这家公司曾入选 YC 的某一期。Nectome 的业务简直是从科幻小说里原样搬出来的：它推销一项服务，把顾客的大脑低温冷冻起来，等科学家攻克了相关技术，有朝一日（可能是几百年以后）再上传到计算机里。问题在于，Nectome 需要人的大脑是新鲜的，保存才能奏效。联合创始人罗伯特·麦金太尔（Robert McIntyre）对雷加拉多说[^19]，他的产品“百分之百致命”。

押注 Helion，则反映出奥特曼对寻找清洁、廉价、充裕能源的痴迷。他常说，能源的成本和可获得性与生活质量、经济增长高度相关。但他说，如果没有零碳的替代能源，不断增长的能源消耗将会“毁掉这个星球[^20]”。2023 年，他形容 Helion “不只是一笔投资”[^21]，还说它是“除了 OpenAI，我花很多时间在上面的另一件事”。微软向 OpenAI 做了第三笔投资，金额 100 亿美元；此后，这家科技巨头又签下一份协议，从 Helion 的第一座电厂购电。让能源专家震惊[^22]又怀疑的是，Helion 承诺最迟到 2028 年就建成这座电厂。

也是在 2021 年，奥特曼把他对投资的偏好带进了 OpenAI。那年 5 月，他推出了[^23] OpenAI 创业基金（OpenAI Startup Fund），这是一个 1 亿美元的投资池，用来支持早期公司，用他的话说，就是那些“对如何用 AI 改变世界有大想法”的公司。微软又一次成了这只基金的投资者。在一些观察者看来，设立这只基金是个奇怪的决定。OpenAI 几乎还没有什么收入，本身就已经够烧钱了，为什么还要再募一笔钱给别的公司用？另一些人觉得，这是奥特曼想围绕 OpenAI 重建 YC 那种强大的网络效应。还有人认为，这不过是奥特曼的习惯使然。“这就是山姆在这个世界上行事的方式，”一位和他共事过的人说，“做交易。”

奥特曼喜欢说，他没有拿 OpenAI 的任何股权，免得自己的逐利之心玷污了对安全 AGI 的追求。他每年只拿 6.5 万美元的薪水，财富都是通过其他企业积累的。这番表态听起来很漂亮，也呼应了他当初解释 OpenAI 为什么以非营利组织起步时的说辞。但就像这家机构的非营利身份一样，到 2021 年，这番话已经不能反映全部真相。奥特曼在 YC 持有大量股份，而 YC 向 OpenAI 投了 1000 万美元，最多可能拿到 10 亿美元的回报。随着 OpenAI 不断推进商业化，许多 YC 初创公司和他的许多其他投资对象，也都会成为 OpenAI 的客户或商业伙伴。《华尔街日报》后来把奥特曼名下的各项资产加在一起，算出他在 2024 年 6 月的净资产[^24]至少有 28 亿美元。OpenAI 创业基金又让奥特曼那套利他叙事多了一处说不清的地方，这只基金最终也在他短暂被赶下台的事件中起了一点小小的作用。

[^1]: **有了新的共识：** 路线图的副本。

[^2]: **一年后，谷歌：** 这篇论文俗称“Chinchilla 论文”：Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai, Eliza Rutherford et al., “Training Compute-Optimal Large Language Models,” preprint, arXiv, March 29, 2022, 1–36, [arxiv.org/abs/2203.15556](http://arxiv.org/abs/2203.15556).

[^3]: **OpenAI 把这种对模型做压力测试并加以改进的过程：** 这个词在 AI 语境中的首次使用，出自这篇论文：Miles Brundage, Shahar Avin, Jasmine Wang, Haydn Belfield, Gretchen Krueger, Gillian Hadfield et al., “Toward Trustworthy AI Development: Mechanisms for Supporting Verifiable Claims,” preprint, arXiv, April 20, 2020, 2, [doi.org/10.48550/arXiv.2004.07213](http://doi.org/10.48550/arXiv.2004.07213).

[^4]: **赫拉夫曾与 OpenAI 合作：** Khlaaf 写过一篇论文，分析 AI 领域和网络安全领域的红队测试有何不同。Heidy Khlaaf, “Toward Comprehensive Risk Assessments and Assurance of AI-Based Systems,” Trail of Bits, March 7, 2023, 1–30, [trailofbits.com/documents/Toward\_comprehensive\_risk\_assessments.pdf](http://trailofbits.com/documents/Toward_comprehensive_risk_assessments.pdf).

[^5]: **这家公司是 OpenAI 发布 GPT-3 API 时的合作伙伴：** Lex Fridman, host, *Lex Fridman Podcast*, podcast, episode 121, “Eugenia Kuyda: Friendship with an AI Companion,” September 5, 2020, [lexfridman.com/podcast](http://lexfridman.com/podcast).

[^6]: **Latitude 此前已经在用：** Tom Simonite, “It Began as an AI-Fueled Dungeon Game. It Got Much Darker,” *Wired*, May 5, 2021, [wired.com/story/ai-fueled-dungeon-game-got-much-darker](http://wired.com/story/ai-fueled-dungeon-game-got-much-darker).

[^7]: **微软高管干脆指示：** Charles Duhigg, “The Inside Story of Microsoft’s Partnership with OpenAI,” *New Yorker*, December 1, 2023, [newyorker.com/magazine/2023/12/11/the-inside-story-of-microsofts-partnership-with-openai](http://newyorker.com/magazine/2023/12/11/the-inside-story-of-microsofts-partnership-with-openai).

[^8]: **微软会先迎来属于自己的高光时刻：** Nat Friedman, “Introducing GitHub Copilot: Your AI Pair Programmer,” GitHub, June 29, 2021, [github.blog/news-insights/product-news/introducing-github-copilot-ai-pair-programmer](http://github.blog/news-insights/product-news/introducing-github-copilot-ai-pair-programmer).

[^9]: **随后在 8 月，OpenAI 会发布：** OpenAI, “OpenAI Codex,” *Open AI* (blog), August 10, 2021, [openai.com/index/openai-codex](http://openai.com/index/openai-codex).

[^10]: **这个安排：** Tiernan Ray, “Microsoft Has Over a Million Paying Github Copilot Users: CEO Nadella,” ZDNet, October 25, 2023, [zdnet.com/article/microsoft-has-over-a-million-paying-github-copilot-users-ceo-nadella](http://zdnet.com/article/microsoft-has-over-a-million-paying-github-copilot-users-ceo-nadella).

[^11]: **“如果你能挥一挥魔杖”：** “Advice to Entrepreneurs | Sam Altman & Jack Altman,” posted August 1, 2019, by Khosla Ventures, YouTube, 30 min., 10 sec., [youtu.be/NAaRhXQCt9o](http://youtu.be/NAaRhXQCt9o).

[^12]: **这家公司专门做一件事：** Ellen Huet and Gillian Tan, “Sam Altman Wants to Scan Your Eyeball in Exchange for Cryptocurrency,” *Bloomberg*, June 29, 2021, [bloomberg.com/news/articles/2021-06-29/sam-altman-s-worldcoin-will-give-free-crypto-for-eyeball-scans](http://bloomberg.com/news/articles/2021-06-29/sam-altman-s-worldcoin-will-give-free-crypto-for-eyeball-scans).

[^13]: **在 YC 时，他启动了：** Sarah Holder and Shirin Ghaffary, “Sam Altman–Backed Group Completes Largest US Study on Basic Income,” *Bloomberg*, July 22, 2024, [bloomberg.com/news/articles/2024-07-22/ubi-study-backed-by-openai-s-sam-altman-bolsters-support-for-basic-income](http://bloomberg.com/news/articles/2024-07-22/ubi-study-backed-by-openai-s-sam-altman-bolsters-support-for-basic-income).

[^14]: **2024 年 7 月，OpenResearch：** OpenResearch, “Key Findings: Spending,” *OpenResearch* (blog), July 21, 2024, [openresearchlab.org/findings/key-findings-spending](http://openresearchlab.org/findings/key-findings-spending).

[^15]: **Tools for Humanity 的主打产品：** Huet and Tan, “Sam Altman Wants to Scan Your Eyeball.”

[^16]: **一项深入调查：** Eileen Guo and Adi Renaldi, “Deception, Exploited Workers, and Cash Handouts: How Worldcoin Recruited Its First Half a Million Test Users,” *MIT Technology Review*, April 6, 2022, [technologyreview.com/2022/04/06/1048981/worldcoin-cryptocurrency-biometrics-web3](http://technologyreview.com/2022/04/06/1048981/worldcoin-cryptocurrency-biometrics-web3).

[^17]: **2023 年 7 月，Worldcoin：** Anita Nkonge, “Worldcoin Suspended in Kenya as Thousands Queue for Free Money,” BBC, August 3, 2023, [bbc.com/news/world-africa-66383325](http://bbc.com/news/world-africa-66383325).

[^18]: **“我基本上就是把手头能动用的身家”：** Antonio Regalado, “Sam Altman Invested $180 Million into a Company Trying to Delay Death,” *MIT Technology Review*, March 8, 2023, [technologyreview.com/2023/03/08/1069523/sam-altman-investment-180-million-retro-biosciences-longevity-death](http://technologyreview.com/2023/03/08/1069523/sam-altman-investment-180-million-retro-biosciences-longevity-death).

[^19]: **联合创始人罗伯特·麦金太尔对雷加拉多说：** Antonio Regalado, “A Startup Is Pitching a Mind-Uploading Service That Is ‘100 percent Fatal,’ ” *MIT Technology Review*, March 13, 2018, [technologyreview.com/2018/03/13/144721/a-startup-is-pitching-a-mind-uploading-service-that-is-100-percent-fatal](http://technologyreview.com/2018/03/13/144721/a-startup-is-pitching-a-mind-uploading-service-that-is-100-percent-fatal).

[^20]: **“毁掉这个星球”：** “Office Hours with Sam Altman,” posted January 11, 2017, by Y Combinator, YouTube, 24 min., 34 sec., [youtu.be/45BvnJgwYjk](http://youtu.be/45BvnJgwYjk).

[^21]: **“不只是一笔投资”：** “StrictlyVC in Conversation with Sam Altman, Part One,” posted on January 16, 2023, by Connie Loizos, YouTube, 20 min., 32 sec., [youtu.be/57OU18cogJI](http://youtu.be/57OU18cogJI).

[^22]: **让能源专家震惊：** Justine Calma, “Microsoft Just Made a Huge, Far-from-Certain Bet on Nuclear Fusion,” *The Verge*, May 10, 2023, [theverge.com/2023/5/10/23717332/microsoft-nuclear-fusion-power-plant-helion-purchase-agreement](http://theverge.com/2023/5/10/23717332/microsoft-nuclear-fusion-power-plant-helion-purchase-agreement).

[^23]: **那年 5 月，他推出了：** 相关信息见它的官网：[openai.fund](https://openai.fund/)。

[^24]: **他在 2024 年 6 月的净资产：** Berber Jin, Tom Dotan, and Keach Hagey, “The Opaque Investment Empire Making OpenAI’s Sam Altman Rich,” *Wall Street Journal*, June 3, 2024, [wsj.com/tech/ai/openai-sam-altman-investments-004fc785](http://wsj.com/tech/ai/openai-sam-altman-investments-004fc785).
