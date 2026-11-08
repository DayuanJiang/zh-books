# 去翻译腔修订记录

2026 年 11 月对全书做的一次专项修订：顺着中文读，找出读着像英文直译的句子，对照原文改成忠实、易懂的中文。
第一轮由 Claude 按章改写；第二轮由 GPT-6 Astra 逐条对照英文复核；第三轮由 Claude 处理复核提出的问题，逐条决定采用建议、重写、保留或退回。引言和第 1 章的改动另由 Claude 逐条通读。

共改写 1032 处，最终保留改动 999 处，退回原译 33 处。

## 引言

- 英文：The hope for informed gossip is that there are distinctive patterns in the errors people make.
  - 原译：有见地的闲谈之所以有望实现，在于人们犯的错误有特定的模式。
  - 现译：有见地的闲谈之所以有可能，是因为人们犯的错误有一些鲜明的模式。
  - 处理：复核后重写。“之所以有望实现，在于”句式生硬，distinctive 译成“特定”不准 复核：“有见地的闲谈之所以有希望”搭配不自然，没有明确表达“有望实现”的意思；distinctive 在这里强调模式特征鲜明。

- 英文：But that is not the only way the mind works, nor indeed is that the typical way.
  - 原译：但这并不是心智运作的唯一方式，其实也不是它通常的方式。
  - 现译：但心智并不只有这一种运作方式，而且这其实也不是它典型的运作方式。
  - 处理：Astra 复核通过。“它通常的方式”照搬英文代词加名词的结构

- 英文：As we navigate our lives, we normally allow ourselves to be guided by impressions and feelings, and the confidence we have in our intuitive beliefs and preferences is usually justified.
  - 原译：在生活中，我们通常任由印象和感觉指引自己，而我们对自己直觉上的信念和偏好所抱的信心，通常也是有道理的。
  - 现译：在生活中，我们通常任由印象和感觉指引自己，对自己凭直觉形成的信念和偏好抱有信心，而这种信心通常是有道理的。
  - 处理：Astra 复核通过。主语前堆了一长串“对……所抱的”定语

- 英文：So this is my aim for watercooler conversations: improve the ability to identify and understand errors of judgment and choice, in others and eventually in ourselves, by providing a richer and more precise language to discuss them. In at least some cases, an accurate diagnosis may suggest an intervention to limit the damage that bad judgments and choices often cause.
  - 原译：所以，这就是我对饮水机旁闲谈的期望：提供一种更丰富、更准确的语言来讨论判断与选择中的错误，从而提高识别和理解这些错误的能力，先是在别人身上，最终也在我们自己身上。至少在某些情况下，准确的诊断可以提示一种干预的办法，减少糟糕的判断和选择常常造成的损害。
  - 现译：所以，我为饮水机旁的闲谈定下的目标是：提供一种更丰富、更准确的语言来讨论判断与选择中的错误，让人们更善于识别和理解这些错误，先是别人的错误，最终也包括我们自己的错误。至少在某些情况下，准确的诊断也许能指出一种干预办法，来限制糟糕的判断和选择常常造成的损害。
  - 处理：Astra 复核通过。“先是在别人身上……”照搬英文状语位置；aim 写成“期望”，may 写成“可以”

- 英文：This book presents my current understanding of judgment and decision making, which has been shaped by psychological discoveries of recent decades. However, I trace the central ideas to the lucky day in 1969 when I asked a colleague to speak as a guest to a seminar I was teaching in the Department of Psychology at the Hebrew University of Jerusalem.
  - 原译：本书介绍我目前对判断与决策的理解，这些理解是由近几十年来心理学的发现塑造的。不过，书中的核心思想可以追溯到 1969 年的一个幸运的日子。那天，我邀请一位同事到我在耶路撒冷希伯来大学心理学系讲授的研讨课上做客座演讲。
  - 现译：本书介绍我目前对判断与决策的理解，近几十年来心理学的种种发现塑造了这种理解。不过，书中的核心思想可以追溯到 1969 年那幸运的一天。当时我在耶路撒冷希伯来大学心理学系教一门研讨课，那天我请了一位同事来课上做客座演讲。
  - 处理：Astra 复核通过。“是由……塑造的”被动句；“研讨课”前定语过长

- 英文：There was never a dull moment when Amos was around.
  - 原译：有阿莫斯在的地方，从来没有沉闷的时刻。
  - 现译：有阿莫斯在的地方，气氛从来不会沉闷。
  - 处理：Astra 复核通过。“没有沉闷的时刻”是英文习语直译

- 英文：Amos told the class about an ongoing program of research at the University of Michigan that sought to answer this question: Are people good intuitive statisticians?
  - 原译：阿莫斯在课上介绍了密歇根大学正在进行的一项研究计划，它想回答这样一个问题：人是优秀的直觉统计学家吗？
  - 现译：阿莫斯在课上介绍了密歇根大学正在进行的一项研究计划，这项计划要回答的问题是：人是优秀的直觉统计学家吗？
  - 处理：Astra 复核通过。用“它”承接英文定语从句

- 英文：at age four a child effortlessly conforms to the rules of grammar as she speaks, although she has no idea that such rules exist.
  - 原译：四岁的孩子说话时毫不费力就能遵守语法规则，尽管她根本不知道有这些规则存在。
  - 现译：四岁的孩子根本不知道有语法规则存在，说话时却毫不费力就能遵守这些规则。
  - 处理：Astra 复核通过。让步从句照英文放在句末，多了代词“她”

- 英文：We had a lively debate in the seminar and ultimately concluded that a qualified no was a better answer.
  - 原译：我们在研讨课上进行了热烈的辩论，最后得出结论：有保留的“否”是更好的答案。
  - 现译：我们在研讨课上热烈地辩论了一番，最后得出结论：有保留的“否”是更好的答案。
  - 处理：Astra 复核通过。“进行了……辩论”虚化动词

- 英文：In spite of years of teaching and using statistics, we had not developed an intuitive sense of the reliability of statistical results observed in small samples. Our subjective judgments were biased: we were far too willing to believe research findings based on inadequate evidence and prone to collect too few observations in our own research.
  - 原译：尽管教了多年统计学、也用了多年统计学，我们却没有培养出一种直觉，能感觉到在小样本中观察到的统计结果有多可靠。我们的主观判断是有偏差的：我们太容易相信证据不足的研究发现，自己做研究时又往往收集太少的观测数据。
  - 现译：尽管教了多年统计学、也用了多年统计学，我们对小样本中观察到的统计结果有多可靠，却仍缺乏直觉上的把握。我们的主观判断是有偏差的：我们太容易相信证据不足的研究发现，自己做研究时，收集的观测数据又往往太少。
  - 处理：按复核意见修改。“一种直觉，能感觉到……”照搬后置修饰；“收集太少的观测数据”是英文词序 复核：“没能培养出直觉，来判断……”仍是生硬的后接结构，也容易被读成笼统地缺乏直觉。原文限定的是对小样本统计结果可靠性的直觉把握。

- 英文：Amos collected the responses of a group of expert participants in a meeting of the Society of Mathematical Psychology, including the authors of two statistical textbooks.
  - 原译：阿莫斯在数学心理学会的一次会议上，收集了一组专家参与者的回答，其中包括两本统计学教科书的作者。
  - 现译：阿莫斯在数学心理学会的一次会议上收集了一批专家参与者的回答，这些专家里有两本统计学教科书的作者。
  - 处理：Astra 复核通过。“其中包括”照搬 including，字面上挂在“回答”上

- 英文：They also gave very poor advice to a fictitious graduate student about the number of observations she needed to collect.
  - 原译：对于一位虚构的研究生需要收集多少观测数据，他们给出的建议也很糟糕。
  - 现译：一位虚构的研究生需要收集多少观测数据，他们给她的建议也很糟糕。
  - 处理：Astra 复核通过。“对于……”介词结构生硬

- 英文：While writing the article that reported these findings, Amos and I discovered that we enjoyed working together.
  - 原译：在撰写报告这些发现的论文时，阿莫斯和我发现，我们很喜欢一起工作。
  - 现译：在撰写论文报告这些结果时，阿莫斯和我发现，我们很喜欢一起工作。
  - 处理：Astra 复核通过。“撰写报告这些发现的论文”动宾套定语，读不顺

- 英文：Both Amos and I were critical and argumentative, he even more than I, but during the years of our collaboration neither of us ever rejected out of hand anything the other said.
  - 原译：阿莫斯和我都爱挑剔、爱争论，他比我更甚，但在我们合作的那些年里，我们谁都没有对另一方说的话不假思索地否定过。
  - 现译：阿莫斯和我都爱挑剔、爱争论，他比我更甚，但在合作的那些年里，对方说什么，我们谁都没有一口否定过。
  - 处理：Astra 复核通过。“对另一方说的话不假思索地否定过”照搬英文结构

- 英文：Amos was the more logical thinker, with an orientation to theory and an unfailing sense of direction.
  - 原译：阿莫斯是更讲逻辑的思考者，偏重理论，方向感从不出错。
  - 现译：阿莫斯思考起来更讲逻辑，他偏重理论，方向感从不出错。
  - 处理：Astra 复核通过。“是更讲逻辑的思考者”照搬 the more logical thinker

- 英文：We developed a routine in which we spent much of our working days together, often on long walks. For the next fourteen years our collaboration was the focus of our lives, and the work we did together during those years was the best either of us ever did.
  - 原译：我们形成了一个习惯：工作日的大部分时间都待在一起，常常是长时间地散步。在接下来的十四年里，我们的合作是我们生活的中心，我们在那些年里一起完成的工作，是我们两人各自做过的最好的工作。
  - 现译：我们形成了一个习惯：工作日的大部分时间都待在一起，常常一起散很长时间的步。在接下来的十四年里，合作是我们生活的中心；那些年里我们一起完成的工作，是我们两人各自做过的最好的工作。
  - 处理：Astra 复核通过。“常常是长时间地散步”生硬，“我们”重复太多

- 英文：We were not seriously looking for the correct answer to the statistical questions we posed.
  - 原译：我们并没有认真地寻找所提统计问题的正确答案。
  - 现译：我们并没有认真去找这些统计问题的正确答案。
  - 处理：Astra 复核通过。“所提统计问题”文白夹杂，照搬 we posed

- 英文：We once discovered with great delight that we had identical silly ideas about the future professions of several toddlers we both knew.
  - 原译：有一次，我们非常高兴地发现，对于我们都认识的几个蹒跚学步的孩子将来会从事什么职业，我们有着一模一样的傻念头。
  - 现译：有一次，我们非常高兴地发现，说起我们都认识的几个蹒跚学步的孩子将来会干哪一行，我们俩的傻念头一模一样。
  - 处理：复核后重写。“对于……”长介词短语加“有着” 复核：删去“对于”后，“发现”直接接上“孩子将来会干哪一行”这个长问句，读到句尾才明确发现的是两人的想法相同，衔接反而不如原译清楚。

- 英文：It was also clear that our intuitions were governed by the resemblance of each child to the cultural stereotype of a profession. The amusing exercise helped us develop a theory that was emerging in our minds at the time, about the role of resemblance in predictions.
  - 原译：同样清楚的是，我们的直觉取决于每个孩子与某种职业的文化刻板印象有多相似。这个有趣的练习帮助我们发展了一个当时正在我们脑中成形的理论，这个理论讲的是相似性在预测中的作用。
  - 现译：我们也清楚地看到，左右我们直觉的，是每个孩子与某种职业的文化刻板印象有多相似。当时我们脑中正在形成一个理论，讲的是相似性在预测中的作用；这个有趣的练习帮助我们发展了这个理论。
  - 处理：Astra 复核通过。“同样清楚的是”照搬 It was also clear；“理论”前定语过长

- 英文：We noticed that the question triggered a search of memory for divorced professors we knew or knew about, and that we judged the size of categories by the ease with which instances came to mind. We called this reliance on the ease of memory search the availability heuristic. In one of our studies, we asked participants to answer a simple question about words in a typical English text:
  - 原译：我们注意到，这个问题会引发一次记忆搜索，去找我们认识或听说过的离婚的教授；我们是根据例子想起来的容易程度来判断某一类别有多大的。我们把这种对记忆搜索难易程度的依赖称为可得性启发式。在我们的一项研究中，我们请参与者回答一个关于典型英语文本中单词的简单问题：
  - 现译：我们注意到，这个问题会让我们在记忆里搜寻自己认识或听说过的离了婚的教授；我们是根据例子想起来容不容易，来判断某一类别有多大的。我们把这种依赖记忆搜索难易程度的判断方式称为可得性启发式。我们在一项研究中请参与者回答一个简单的问题，问的是典型英语文本中的单词：
  - 处理：Astra 复核通过。“引发一次记忆搜索”“对……的依赖”“一个关于……的问题”都是英文名词化结构

- 英文：Here again, the reliance on a heuristic produces a predictable bias in judgments. For example, I recently came to doubt my long-held impression that adultery is more common among politicians than among physicians or lawyers.
  - 原译：这里再次说明，依赖启发式会在判断中产生可以预见的偏差。例如，我最近开始怀疑自己长期以来的一个印象：政治人物中的婚外情比医生或律师中更常见。
  - 现译：这里同样可以看到，依赖启发式会让判断产生可以预见的偏差。例如，我最近开始怀疑自己长期以来的一个印象：政治人物比医生或律师更常有婚外情。
  - 处理：Astra 复核通过。“这里再次说明”缺主语；“……中的婚外情比……中更常见”照搬 among

- 英文：My intuitive impression could be due entirely to journalists’ choices of topics and to my reliance on the availability heuristic.
  - 原译：我的直觉印象可能完全来自记者对话题的选择，以及我对可得性启发式的依赖。
  - 现译：我的这个直觉印象，可能完全是由记者挑选话题和我依赖可得性启发式造成的。
  - 处理：复核后重写。“记者对话题的选择”“我对……的依赖”名词化 复核：原文的 entirely 同时涵盖记者选题和自己依赖可得性启发式两个因素；“完全是记者挑选话题的结果，再加上……”先把原因全部归给记者，再补另一个因素，改变了限定范围，句子也不如原译完整。

- 英文：Social scientists are no exception; they rely on a view of human nature that provides the background of most discussions of specific behaviors but is rarely questioned.
  - 原译：社会科学家也不例外；他们依赖一种关于人性的看法，大多数关于具体行为的讨论都以它为背景，它本身却很少受到质疑。
  - 现译：社会科学家也不例外：他们依赖一种对人性的看法，讨论具体行为时大多以它为背景，这种看法本身却很少受到质疑。
  - 处理：Astra 复核通过。两个“关于……的”连用，照搬定语从句

- 英文：First, people are generally rational, and their thinking is normally sound. Second, emotions such as fear, affection, and hatred explain most of the occasions on which people depart from rationality.
  - 原译：第一，人通常是理性的，他们的思考一般是合理的。第二，恐惧、喜爱和憎恨等情绪，解释了人们偏离理性的大多数情况。
  - 现译：第一，人通常是理性的，思考一般也合乎情理。第二，人们偏离理性的情况，大多可以用恐惧、喜爱和憎恨等情绪来解释。
  - 处理：Astra 复核通过。多余的“他们的”；“情绪解释了……情况”抽象名词作主语

- 英文：Scholars in other disciplines found it useful, and the ideas of heuristics and biases have been used productively in many fields, including medical diagnosis, legal judgment, intelligence analysis, philosophy, finance, statistics, and military strategy.
  - 原译：其他学科的学者也觉得它有用，启发式和偏差的观点已经在许多领域得到了富有成效的应用，包括医学诊断、法律判决、情报分析、哲学、金融、统计学和军事战略。
  - 现译：其他学科的学者也觉得它有用，许多领域都卓有成效地运用了启发式和偏差的观点，包括医学诊断、法律判决、情报分析、哲学、金融、统计学和军事战略。
  - 处理：Astra 复核通过。“得到了富有成效的应用”虚化动词

- 英文：(As I write this, I notice that my choice of “little-covered” examples was guided by availability. The topics I chose as examples are mentioned often; equally important issues that are less available did not come to my mind.)
  - 原译：（写到这里，我注意到，我挑选“很少被报道”的例子时也受到了可得性的引导。我选作例子的这些话题其实经常被提及；同样重要但可得性较低的问题，并没有出现在我脑中。）
  - 现译：（写到这里，我注意到，我挑选“很少被报道”的例子时，也是受了可得性的引导。我选作例子的这些话题其实经常被提及；同样重要但可得性较低的问题，我却没有想到。）
  - 处理：Astra 复核通过。“并没有出现在我脑中”直译 did not come to my mind

- 英文：We did not fully realize it at the time, but a key reason for the broad appeal of “heuristics and biases” outside psychology was an incidental feature of our work: we almost always included in our articles the full text of the questions we had asked ourselves and our respondents.
  - 原译：我们当时并没有完全意识到，“启发式与偏差”之所以在心理学之外广受欢迎，一个关键原因在于我们工作中的一个附带特点：我们几乎总在文章里附上我们问自己和问受访者的那些问题的全文。
  - 现译：我们当时并没有完全意识到，“启发式与偏差”之所以在心理学之外广受欢迎，一个关键原因在于我们工作中的一个附带特点：我们问过自己、也问过受访者的那些问题，几乎总是全文附在文章里。
  - 处理：Astra 复核通过。“的”字连串：问受访者的那些问题的全文

- 英文：The use of demonstrations provided scholars from diverse disciplines—notably philosophers and economists—an unusual opportunity to observe possible flaws in their own thinking.
  - 原译：演示让不同学科的学者，尤其是哲学家和经济学家，有了一个难得的机会，去观察自己思维中可能存在的缺陷。
  - 现译：通过这些演示，不同学科的学者，尤其是哲学家和经济学家，难得有机会观察到自己思维中可能存在的缺陷。
  - 处理：Astra 复核通过。“有了一个难得的机会，去观察”照搬 an opportunity to

- 英文：A recurrent theme of this book is that luck plays a large role in every story of success; it is almost always easy to identify a small change in the story that would have turned a remarkable achievement into a mediocre outcome.
  - 原译：本书一再出现的一个主题是，运气在每个成功的故事里都扮演着重要的角色；我们几乎总能轻易找到故事里的某个小变化，只要它发生了，一项非凡的成就就会变成平庸的结果。
  - 现译：本书一再出现的一个主题是，运气在每个成功的故事里都起着很大的作用；我们几乎总能轻易找到故事里的某个小变化，只要它发生了，一项非凡的成就就会变成平庸的结果。
  - 处理：Astra 复核通过。“扮演着重要的角色”是 plays a role 的套译

- 英文：The reaction to our work was not uniformly positive. In particular, our focus on biases was criticized as suggesting an unfairly negative view of the mind. As expected in normal science, some investigators refined our ideas and others offered plausible alternatives.
  - 原译：对我们工作的反应并非全是正面的。特别是，有人批评说，我们对偏差的关注暗示了一种对心智不公正的负面看法。正如常规科学中通常会出现的那样，一些研究者完善了我们的观点，另一些人则提出了合理的替代解释。
  - 现译：人们对我们工作的反应并不全是正面的。尤其是，有人批评我们关注偏差，说这暗示了一种对心智过于负面、有失公允的看法。一些研究者完善了我们的观点，另一些人则提出了合理的替代解释；这样的情况在常规科学中本就在意料之内。
  - 处理：按复核意见修改。“对……的反应”“我们对偏差的关注”名词化主语；“正如……那样”套译 复核：前两句有所改善，但“和常规科学中意料之中的情形一样”修饰层层套叠，比原来的衔接更拗口。

- 英文：By and large, though, the idea that our minds are susceptible to systematic errors is now generally accepted. Our research on judgment had far more effect on social science than we thought possible when we were working on it.
  - 原译：不过总的来说，我们的心智容易犯系统性错误这一观点，如今已经被普遍接受。我们对判断的研究对社会科学产生的影响，远远超出了我们当初做研究时所能想到的程度。
  - 现译：不过总的来说，如今人们已经普遍接受了这一观点：我们的心智容易犯系统性错误。我们对判断的研究给社会科学带来的影响，远远超出了我们当初做研究时的想象。
  - 处理：Astra 复核通过。长主语加“被普遍接受”被动句；“所能想到的程度”生硬

- 英文：Immediately after completing our review of judgment, we switched our attention to decision making under uncertainty.
  - 原译：完成对判断的研究综述之后，我们立刻把注意力转向不确定条件下的决策。
  - 现译：写完判断研究的综述之后，我们立刻把注意力转向了不确定条件下的决策。
  - 处理：Astra 复核通过。“完成对判断的研究综述”名词化

- 英文：These elementary choices had long been used to examine broad questions about decision making, such as the relative weight that people assign to sure things and to uncertain outcomes.
  - 原译：长期以来，这类基本的选择一直被用来考察有关决策的一般性问题，比如人们给确定的事和不确定的结果分别赋予多大的权重。
  - 现译：长期以来，人们一直用这类基本的选择来考察有关决策的一般性问题，比如人们给确定的事和不确定的结果分别赋予多大的权重。
  - 处理：Astra 复核通过。“被用来”被动句

- 英文：Here again, as in judgment, we observed systematic biases in our own decisions, intuitive preferences that consistently violated the rules of rational choice.
  - 原译：在这里，和在判断中一样，我们在自己的决策中也观察到了系统性的偏差，也就是一贯违背理性选择规则的直觉偏好。
  - 现译：和研究判断时一样，我们在自己的决策中也观察到了系统性的偏差，也就是一贯违背理性选择规则的直觉偏好。
  - 处理：Astra 复核通过。“在这里，和在判断中一样”逐词照搬

- 英文：Until geographical separation made it too difficult to go on, Amos and I enjoyed the extraordinary good fortune of a shared mind that was superior to our individual minds and of a relationship that made our work fun as well as productive.
  - 原译：在地理上的分隔让合作难以为继之前，阿莫斯和我一直享有非凡的好运：我们共有的心智胜过我们各自的心智，我们的关系也让工作既有趣又富有成效。
  - 现译：后来我们分隔两地，合作难以为继；在那之前，阿莫斯和我一直格外幸运：我们共有的心智胜过各自的心智，我们的关系也让工作既有趣又富有成效。
  - 处理：Astra 复核通过。“在……之前”包着长从句；“享有非凡的好运”直译

- 英文：Our collaboration on judgment and decision making was the reason for the Nobel Prize that I received in 2002, which Amos would have shared had he not died, aged fifty-nine, in 1996.
  - 原译：我们在判断与决策方面的合作，是我在 2002 年获得诺贝尔奖的原因；如果阿莫斯没有在 1996 年以五十九岁的年纪去世，他本会与我分享这个奖项。
  - 现译：我在 2002 年获得诺贝尔奖，凭的就是我们在判断与决策方面的合作；要不是阿莫斯在 1996 年去世（享年五十九岁），他本会与我分享这个奖项。
  - 处理：Astra 复核通过。“以五十九岁的年纪去世”照搬 aged fifty-nine；“是……的原因”生硬

- 英文：It turned out that the heart of the fire had not been in the kitchen but in the basement beneath where the men had stood.
  - 原译：后来才发现，火势的中心不在厨房，在他们所站位置下方的地下室里。
  - 现译：后来才发现，火势的中心不在厨房，在他们脚下的地下室里。
  - 处理：Astra 复核通过。“他们所站位置下方的”定语生硬

- 英文：Valid intuitions develop when experts have learned to recognize familiar elements in a new situation and to act in a manner that is appropriate to it.
  - 原译：当专家学会在新情境中识别出熟悉的要素，并以恰当的方式行动时，有效的直觉就形成了。
  - 现译：专家学会了在新情境中识别出熟悉的要素，并采取恰当的行动，有效的直觉就形成了。
  - 处理：Astra 复核通过。“当……时”包长从句，“以恰当的方式行动”照搬 in a manner

- 英文：The executive’s decision would today be described as an example of the affect heuristic, where judgments and decisions are guided directly by feelings of liking and disliking, with little deliberation or reasoning.
  - 原译：这位高管的决定，今天会被描述为情感启发式的一个例子：判断和决定直接受到喜欢和不喜欢的感觉引导，几乎没有经过深思熟虑或推理。
  - 现译：按今天的说法，这位高管的决定是情感启发式的一个例子：判断和决定直接受到喜欢和不喜欢的感觉引导，几乎没有经过深思熟虑或推理。
  - 处理：Astra 复核通过。“会被描述为”被动句

- 英文：If the individual has relevant expertise, she will recognize the situation, and the intuitive solution that comes to her mind is likely to be correct.
  - 原译：如果这个人有相关的专长，她就会认出这种情境，她脑中浮现的直觉解法很可能是正确的。
  - 现译：如果这个人有相关的专长，就会认出这种情境，脑中浮现的直觉解法也很可能是正确的。
  - 处理：Astra 复核通过。多余的代词“她”

- 英文：The spontaneous search for an intuitive solution sometimes fails—neither an expert solution nor a heuristic answer comes to mind.
  - 原译：自发地寻找直觉解法有时会失败：脑中既没有出现专家的解法，也没有出现启发式的答案。
  - 现译：我们自发地寻找直觉解法，有时会一无所获：脑中既没有浮现专家的解法，也没有浮现启发式的答案。
  - 处理：Astra 复核通过。动作作主语，“寻找……会失败”照搬英文

- 英文：For reasons that I explain more fully in the next chapter, I describe mental life by the metaphor of two agents, called System 1 and System 2, which respectively produce fast and slow thinking.
  - 原译：出于我将在下一章更详细解释的理由，我用两个主体的比喻来描述心理生活，它们叫作系统 1 和系统 2，分别产生快思考和慢思考。
  - 现译：我用两个主体的比喻来描述心理生活，它们叫作系统 1 和系统 2，分别产生快思考和慢思考；这样做的理由，我会在下一章更详细地解释。
  - 处理：Astra 复核通过。句首“出于我将……的理由”长定语

- 英文：In the picture that emerges from recent research, the intuitive System 1 is more influential than your experience tells you, and it is the secret author of many of the choices and judgments you make.
  - 原译：在最近的研究所呈现的图景中，直觉的系统 1 比你的经验告诉你的更有影响力，它是你所作的许多选择和判断背后不为人知的作者。
  - 现译：近来的研究描绘出这样一幅图景：直觉的系统 1 比你凭经验以为的更有影响力，它是你许多选择和判断的幕后作者。
  - 处理：Astra 复核通过。“在……所呈现的图景中”“比你的经验告诉你的”逐词直译

- 英文：It elaborates the distinction between the automatic operations of System 1 and the controlled operations of System 2, and shows how associative memory, the core of System 1, continually constructs a coherent interpretation of what is going on in our world at any instant. I attempt to give a sense of the complexity and richness of the automatic and often unconscious processes that underlie intuitive thinking, and of how these automatic processes explain the heuristics of judgment.
  - 原译：它详细阐述系统 1 的自动运作与系统 2 的受控运作之间的区别，并说明联想记忆，也就是系统 1 的核心，如何在每时每刻不断构建出一种连贯的解释，来说明我们的世界里正在发生什么。我试图让读者感受到，构成直觉思维基础的那些自动的、往往是无意识的过程有多复杂、多丰富，以及这些自动过程怎样解释了判断启发式。
  - 现译：这一部分详细阐述系统 1 的自动运作与系统 2 的受控运作有什么区别，并说明系统 1 的核心，也就是联想记忆，怎样时时刻刻为我们世界里正在发生的事构建出连贯的解释。直觉思维的基础是一些自动的、往往无意识的过程，我试图让读者感受到这些过程有多复杂、多丰富，以及它们怎样解释了判断启发式。
  - 处理：Astra 复核通过。句首“它”指代不明；“构成直觉思维基础的那些……过程”定语过长

- 英文：But the automatic formation of memories—a feature of System 1—has its rules, which we can exploit so that the worse episode leaves a better memory. When people later choose which episode to repeat, they are, naturally, guided by their remembering self and expose themselves (their experiencing self) to unnecessary pain. The distinction between two selves is applied to the measurement of well-being, where we find again that what makes the experiencing self happy is not quite the same as what satisfies the remembering self.
  - 原译：但记忆的自动形成，也就是系统 1 的一个特点，有它自己的规则，我们可以利用这些规则，让更糟的那次经历留下更好的记忆。之后，当人们选择重复哪一次经历时，他们自然会受记忆自我的引导，让自己（也就是他们的体验自我）承受不必要的痛苦。两个自我的区分被应用到幸福感的测量上，我们再次发现，让体验自我快乐的东西，与让记忆自我满意的东西并不完全相同。
  - 现译：但记忆的自动形成（这是系统 1 的一个特点）自有一套规则，我们可以利用这些规则，让更糟的那次经历留下更好的记忆。之后，人们选择重复哪一次经历时，自然会受记忆自我的引导，让自己（也就是他们的体验自我）承受不必要的痛苦。把两个自我的区分应用到幸福感的测量上，我们再次发现，让体验自我快乐的东西，与让记忆自我满意的东西并不完全相同。
  - 处理：复核后重写。“记忆的自动形成”名词化主语；“当……时”和“被应用到” 复核：原文说“记忆的自动形成过程有自身的规则”，改写却先断言“记忆是自动形成的”，把对某种形成过程的描述泛化成了关于记忆形成的总体判断；“自有一套规则”也没有明确落在形成过程上。原译更准确。

- 英文：The articles present the contributions that were cited by the Nobel committee—and you may be surprised by how simple they are.
  - 原译：这两篇文章介绍的正是诺贝尔委员会所引用的那些贡献，你可能会惊讶于它们有多简单。
  - 现译：这两篇文章介绍的正是诺贝尔委员会所引用的那些贡献，你可能会惊讶于它们有多简单。
  - 处理：复核后退回原译。“惊讶于”照搬 be surprised by 复核：“简单得也许会让你吃惊”把不确定语气塞进程度补语，读起来拗口。“惊讶于”在这里是正常的书面表达，原译更自然，也清楚保留了 may 的语气。

## 第 1 章 故事里的两个角色

- 英文：Your experience as you look at the woman’s face seamlessly combines what we normally call seeing and intuitive thinking.
  - 原译：看着这位女士的脸时，你的体验把我们通常所说的“看见”和直觉思维天衣无缝地融合在了一起。
  - 现译：看着这位女士的脸时，你的体验中既有我们通常所说的“看见”，也有直觉思维，两者浑然一体。
  - 处理：按复核意见修改。“你的体验把……融合”抽象名词作主语 复核：“看……时，在你的体验里”连续叠加状语，仍然生硬。可以保留体验中两种活动融为一体的意思，改用更清楚的中文结构。

- 英文：A premonition of what she was going to do next came to mind automatically and effortlessly.
  - 原译：对她下一步要做什么的预感，自动地、毫不费力地浮现在你脑中。
  - 现译：她下一步要做什么，你脑中自动地、毫不费力地就有了预感。
  - 处理：Astra 复核通过。“对……的预感”名词化主语

- 英文：It just happened to you.
  - 原译：它就那么发生在了你身上。
  - 现译：它就这么自己冒了出来。
  - 处理：复核后重写。“发生在了你身上”直译 happened to you 复核：“它就那么自己发生了”仍不自然。“它”承接的是对图片的反应，直接点明并表达其自发产生即可。

- 英文：Psychologists have been intensely interested for several decades in the two modes of thinking evoked by the picture of the angry woman and by the multiplication problem, and have offered many labels for them.
  - 原译：几十年来，心理学家一直对这两种思考方式抱有浓厚的兴趣，一种由那张生气女士的照片引发，另一种由那道乘法题引发；他们为这两种方式起过许多名称。
  - 现译：那张生气女士的照片和那道乘法题，引发的是两种不同的思考方式。几十年来，心理学家一直对这两种方式抱有浓厚的兴趣，也给它们起过许多名称。
  - 处理：Astra 复核通过。“一种由……引发”照搬英文后置修饰

- 英文：The labels of System 1 and System 2 are widely used in psychology, but I go further than most in this book, which you can read as a psychodrama with two characters.
  - 原译：系统 1 和系统 2 这两个名称在心理学中用得很广，但我在这本书里比大多数人走得更远：你可以把它当作一出有两个角色的心理剧来读。
  - 现译：系统 1 和系统 2 这两个名称在心理学中用得很广，但我在这本书里比大多数人走得更远：你可以把这本书当作一出有两个角色的心理剧来读。
  - 处理：Astra 复核通过。“它”照搬 which，指代不清

- 英文：In rough order of complexity, here are some examples of the automatic activities that are attributed to System 1:
  - 原译：下面是一些归于系统 1 的自动活动的例子，大致按复杂程度排列：
  - 现译：下面举一些例子，都是归在系统 1 名下的自动活动，大致按复杂程度排列：
  - 处理：Astra 复核通过。“归于系统 1 的自动活动的例子”的字连串

- 英文：We are born prepared to perceive the world around us, recognize objects, orient attention, avoid losses, and fear spiders.
  - 原译：我们生来就准备好了去感知周围的世界、识别物体、引导注意力、规避损失，以及害怕蜘蛛。
  - 现译：我们生来就做好了准备，去感知周围的世界、识别物体、引导注意力、规避损失，以及害怕蜘蛛。
  - 处理：复核后重写。“生来就准备好了去……”直译 born prepared to 复核：born prepared to 表示生来具有相应的准备或倾向，不等于出生时就已经掌握这些能力、已经害怕蜘蛛。“天生就会”和“天生怕”把先天准备改成了现成能力与恐惧，断言更强。

- 英文：You may be able to resist turning toward the source of a loud and offensive comment at a crowded party, but even if your head does not move, your attention is initially directed to it, at least for a while.
  - 原译：在拥挤的聚会上，有人大声说了一句冒犯人的话，你也许能忍住不转过头去，但即使你的头没有动，你的注意力一开始也会被引向那里，至少会有一会儿是这样。
  - 现译：在拥挤的聚会上，有人大声说了一句冒犯人的话，你也许能忍住不转过头去，但即使头没有动，你的注意力起初也会转向那里，至少有一会儿是这样。
  - 处理：Astra 复核通过。多余的“你的”，“被引向”被动句

- 英文：When waiting for a relative at a busy train station, for example, you can set yourself at will to look for a white-haired woman or a bearded man, and thereby increase the likelihood of detecting your relative from a distance.
  - 原译：例如，在繁忙的火车站等一位亲戚时，你可以有意设定自己去找一位白发女士或一位留胡子的男士，从而提高远远认出这位亲戚的可能性。
  - 现译：例如，在繁忙的火车站等一位亲戚时，你可以有意设定自己的注意力，去找一位白发女士或一位留胡子的男士，这样就更有可能远远地认出这位亲戚。
  - 处理：复核后重写。“从而提高……的可能性”名词化 复核：后半句更自然，但“有意设定自己去找”仍是明显的直译。结合上下文，这里是主动调整注意力，使自己寻找具有指定特征的人。

- 英文：In all these cases, you are asked to do something that does not come naturally, and you will find that the consistent maintenance of a set requires continuous exertion of at least some effort.
  - 原译：在所有这些情况下，你要做的都是自己不会自然而然去做的事，你会发现，要一直保持这样的设定，就得持续付出至少一点努力。
  - 现译：在所有这些情况下，你要做的都是自己不会自然而然去做的事，你会发现，要一直保持这样的设定，至少得持续花一些力气。
  - 处理：Astra 复核通过。“持续付出至少一点努力”照搬英文语序

- 英文：Indeed, the viewers who fail to see the gorilla are initially sure that it was not there—they cannot imagine missing such a striking event.
  - 原译：确实，那些没有看到大猩猩的观看者起初都很肯定，它根本就不在那里；他们无法想象自己会错过如此显眼的事。
  - 现译：确实，那些没有看到大猩猩的观看者起初都很肯定，视频里根本没有大猩猩；他们无法想象自己会错过这么显眼的事。
  - 处理：Astra 复核通过。“它根本就不在那里”直译 it was not there

- 英文：System 2 is mobilized when a question arises for which System 1 does not offer an answer, as probably happened to you when you encountered the multiplication problem 17 × 24.
  - 原译：出现一个系统 1 给不出答案的问题时，系统 2 就会被调动起来；你看到乘法题 17 × 24 时，很可能就是这种情况。
  - 现译：遇到系统 1 给不出答案的问题，系统 2 就会被调动起来；你看到乘法题 17 × 24 时，很可能就是这样。
  - 处理：Astra 复核通过。“出现一个……的问题时”照搬 when a question arises

- 英文：System 2 is also credited with the continuous monitoring of your own behavior—the control that keeps you polite when you are angry, and alert when you are driving at night.
  - 原译：持续监控你自己的行为，也被认为是系统 2 的功劳，正是这种控制让你在生气时保持礼貌，在夜间开车时保持警觉。
  - 现译：持续监控自己的行为，也要归功于系统 2：正是这种控制，让你生气时也能保持礼貌，夜里开车时保持警觉。
  - 处理：Astra 复核通过。“也被认为是……的功劳”被动句

- 英文：As we shall see, it sometimes answers easier questions than the one it was asked, and it has little understanding of logic and statistics.
  - 原译：我们后面会看到，它有时会去回答比被问到的问题更简单的问题，而且它对逻辑和统计也知之甚少。
  - 现译：我们后面会看到，它有时会把被问到的问题换成更简单的问题来回答，而且对逻辑和统计也知之甚少。
  - 处理：Astra 复核通过。“比被问到的问题更简单的问题”照搬英文比较结构

- 英文：The prioritizing of the chosen words is effective and the mild temptation to read other words was fairly easy to resist when you went through the first column.
  - 原译：让选定的词优先，这一招很有效：看第一列时，想去读其他单词的轻微诱惑是比较容易抵挡的。
  - 现译：让选定的词优先，这一招很有效：看第一列时，你会有点想去读别的单词，但这点诱惑比较容易抵挡。
  - 处理：Astra 复核通过。“想去读其他单词的轻微诱惑”名词化主语

- 英文：We also know what it is like to force our attention on a boring book, when we constantly find ourselves returning to the point at which the reading lost its meaning.
  - 原译：我们也知道强迫自己把注意力放在一本无聊的书上是什么滋味：我们总是发现自己又回到了那个读着读着就不知所云的地方。
  - 现译：我们也知道强迫自己专心读一本无聊的书是什么滋味：我们总是发现自己又得翻回去，回到从那儿起就没读进去的地方。
  - 处理：复核后重写。“发现自己又回到了”直译 find ourselves returning 复核：“总是一次次”语义重复；“不知所云”容易让人以为是书写得不通。原文说的是读者无法保持注意，一再返回自己开始未能理解所读内容的位置。

- 英文：You should treat “System 1” and “System 2” as nicknames, like Bob and Joe, identifying characters that you will get to know over the course of this book.
  - 原译：你应该把“系统 1”和“系统 2”当作昵称，就像鲍勃和乔一样，用来指代你在读这本书的过程中会逐渐熟悉的两个角色。
  - 现译：你应该把“系统 1”和“系统 2”当作昵称，就像鲍勃和乔一样，它们指的是两个角色，读这本书的过程中你会逐渐熟悉他们。
  - 处理：Astra 复核通过。“角色”前定语过长

- 英文：“He had an impression, but some of his impressions are illusions.”
  - 原译：“他有个印象，可他的有些印象是错觉。”
  - 现译：“他是有这么个印象，可他有些印象是错觉。”
  - 处理：Astra 复核通过。不像口语，“他的有些印象”语序别扭

- 英文：“This was a pure System 1 response. She reacted to the threat before she recognized it.”
  - 原译：“这纯粹是系统 1 的反应。她还没认出那是威胁，就已经作出了反应。”
  - 现译：“这纯粹是系统 1 的反应。她还没认出那是威胁，就已经有反应了。”
  - 处理：Astra 复核通过。“作出了反应”书面腔，不像闲聊

- 英文：“This is your System 1 talking. Slow down and let your System 2 take control.”
  - 原译：“这是你的系统 1 在说话。慢一点，让你的系统 2 来掌控局面。”
  - 现译：“这是你的系统 1 在说话。慢一点，让你的系统 2 来接手。”
  - 处理：Astra 复核通过。“掌控局面”书面腔，不像口语

## 第 2 章 注意与努力

- 英文：The defining feature of System 2, in this story, is that its operations are effortful, and one of its main characteristics is laziness, a reluctance to invest more effort than is strictly necessary.
  - 原译：在这个故事里，系统 2 最根本的特征是它的运作很费力，而它的主要特点之一是懒惰，也就是不愿意付出超出必要限度的努力。
  - 现译：在这个故事里，系统 2 最根本的特征是运作起来很费力，它的主要特点之一是懒惰，也就是不愿意付出超出必要限度的努力。
  - 处理：复核后重写。“它的”重复、“而”多余，“超出必要限度的努力”照搬英文比较结构 复核：“非付出不可的努力之外，多一点也不愿意付出”比原译绕口，还重复了“付出”；原译对必要限度的表述准确、清楚。

- 英文：If you would like to know what your body is doing while your mind is hard at work, set up two piles of books on a sturdy table, place a video camera on one and lean your chin on the other, get the video going, and stare at the camera lens while you work on Add-1 or Add-3 exercises.
  - 原译：如果你想知道，在心智努力工作时你的身体在做什么，可以在一张结实的桌子上摞两摞书，在一摞上面放一台摄像机，把下巴搁在另一摞上，开始录像，然后一边做加 1 或加 3 练习，一边盯着镜头。
  - 现译：如果你想知道头脑卖力工作时身体在做什么，可以在一张结实的桌子上摞两摞书，在一摞上面放一台摄像机，把下巴搁在另一摞上，开始录像，然后一边做加 1 或加 3 练习，一边盯着镜头。
  - 处理：Astra 复核通过。“在……时”嵌进宾语，加多余的“你的”，照搬 while 从句

- 英文：Hess also wrote of belladonna, a pupil-dilating substance that was used as a cosmetic, and of bazaar shoppers who wear dark glasses in order to hide their level of interest from merchants.
  - 原译：赫斯还写到了颠茄，一种能让瞳孔放大的物质，曾被当作化妆品使用；他也写到，集市上的顾客会戴墨镜，免得商贩看出他们有多感兴趣。
  - 现译：赫斯还写到，颠茄能让瞳孔放大，以前有人拿它当化妆品；他也写到，集市上的顾客会戴墨镜，免得商贩看出他们有多感兴趣。
  - 处理：Astra 复核通过。照搬英文同位语“颠茄，一种……的物质”，加被动的“被当作……使用”

- 英文：Add-1 with four digits caused a larger dilation than the task of holding seven digits for immediate recall.
  - 原译：对四个数字做加 1，引起的瞳孔放大比记住七个数字以便马上回忆的任务更大。
  - 现译：对四个数字做加 1，瞳孔放大得比记住七个数字以便马上回忆时更多。
  - 处理：Astra 复核通过。拿“瞳孔放大”和“任务”比较，照搬 than the task 造成比较对象错位

- 英文：When we exposed our subjects to more digits than they could remember, their pupils stopped dilating or actually shrank.
  - 原译：当我们给受试者呈现的数字多到他们记不住时，他们的瞳孔就不再放大，甚至反而缩小了。
  - 现译：我们给受试者听的数字多到他们记不住时，他们的瞳孔就不再放大，甚至反而缩小了。
  - 处理：复核后重写。“当……时”框住长定语，“呈现”是 expose 的直译 复核：原文叙述我们实际实施的实验及观察结果，改成“如果”后变成了假设条件，还删去了实验主体“我们”；“如果”也与句末“缩小了”的叙事语气不协调。

- 英文：We worked for some months in a spacious basement suite in which we had set up a closed-circuit system that projected an image of the subject’s pupil on a screen in the corridor; we also could hear what was happening in the laboratory.
  - 原译：有几个月，我们在地下室一处宽敞的套间里工作，还在那里装了一套闭路系统，把受试者瞳孔的图像投到走廊里的一块屏幕上；我们也能听到实验室里在发生什么。
  - 现译：有几个月，我们在地下室一处宽敞的套间里工作，还在那里装了一套闭路系统，把受试者瞳孔的图像投到走廊里的一块屏幕上；实验室里的动静，我们也听得到。
  - 处理：Astra 复核通过。“听到……在发生什么”直译 what was happening

- 英文：The diameter of the projected pupil was about a foot; watching it dilate and contract when the participant was at work was a fascinating sight, quite an attraction for visitors in our lab.
  - 原译：投出来的瞳孔直径约有一英尺；参与者用功时，看着它放大、收缩，是一番很吸引人的景象，来实验室参观的人都爱看。
  - 现译：投出来的瞳孔直径约有一英尺；参与者做任务时，看着它放大、收缩，真让人着迷，来实验室参观的人也很爱看。
  - 处理：复核后重写。“是一番很吸引人的景象”照搬 was a fascinating sight 的判断句 复核：沿用了原译“来实验室参观的人都爱看”的过强限定。原文只说这一景象很吸引参观者，没有断言所有参观者无一例外都喜欢。

- 英文：The answer from inside the lab was often, “How did you know?” to which we would reply, “We have a window to your soul.”
  - 原译：实验室里的回答常常是：“你们怎么知道的？”我们就回答：“我们有一扇通往你心灵的窗户。”
  - 现译：实验室里的人常常反问：“你们怎么知道的？”我们就回答：“我们有一扇通往你心灵的窗户。”
  - 处理：Astra 复核通过。抽象名词“回答”作主语，照搬 The answer was

- 英文：The casual observations we made from the corridor were sometimes as informative as the formal experiments.
  - 原译：我们在走廊里随意的观察，有时和正式实验一样有收获。
  - 现译：我们在走廊里随意观察，有时和正式实验一样有收获。
  - 处理：Astra 复核通过。照搬名词短语“……随意的观察”作主语

- 英文：An image came to mind: mental life—today I would speak of the life of System 2—is normally conducted at the pace of a comfortable walk, sometimes interrupted by episodes of jogging and on rare occasions by a frantic sprint.
  - 原译：我脑中浮现出一个画面：心理生活（今天我会说是系统 2 的生活）通常以舒适的散步速度进行，有时会穿插几段慢跑，极少数时候还会有一阵拼命的冲刺。
  - 现译：我脑中浮现出一个画面：心理生活（今天我会说是系统 2 的生活）通常像不紧不慢的散步，有时会穿插几段慢跑，极少数时候还会来一阵拼命的冲刺。
  - 处理：复核后重写。“以……速度进行”是 is conducted at the pace of 的直译 复核：“心理生活通常是迈着舒服的步子走”搭配生硬，也淡化了原文以散步速度比喻心理活动节奏的重点。

- 英文：We found that people, when engaged in a mental sprint, may become effectively blind.
  - 原译：我们发现，人在进行心理冲刺时，可能会变得形同失明。
  - 现译：我们发现，人在心理冲刺时，可能会变得形同失明。
  - 处理：Astra 复核通过。虚化动词“进行”

- 英文：When you turn on a bulb or a toaster, it draws the energy it needs but no more. Similarly, we decide what to do, but we have limited control over the effort of doing it.
  - 原译：你打开一个灯泡或一台烤面包机时，它只取用自己需要的电，一点也不多用。同样，我们能决定做什么，但对做这件事要付出多少努力，我们的控制是有限的。
  - 现译：你开灯或者打开烤面包机，它只取用自己需要的电，一点也不多用。同样，我们能决定做什么，但做这件事要付出多少努力，我们却控制不了多少。
  - 处理：Astra 复核通过。多余的“一个”“一台”，“对……我们的控制是有限的”照搬 have limited control over

- 英文：You will find that you have responded to the threat before you became fully conscious of it.
  - 原译：你会发现，在你完全意识到危险之前，你已经作出了反应。
  - 现译：你会发现，还没完全意识到危险，你就已经作出了反应。
  - 处理：Astra 复核通过。“在……之前”照搬 before 从句，“你”重复

- 英文：He eventually became the leading authority on “cognitive pupillometry,” and I wrote a book titled Attention and Effort, which was based in large part on what we learned together and on follow-up research I did at Harvard the following year.
  - 原译：他最终成了“认知瞳孔测量学”的头号权威，我则写了一本名为《注意与努力》的书，书的内容很大程度上来自我们一起学到的东西，以及我第二年在哈佛大学做的后续研究。
  - 现译：他最终成了“认知瞳孔测量学”的头号权威，我则写了《注意与努力》一书，书的内容很大程度上来自我们一起学到的东西，以及我第二年在哈佛大学做的后续研究。
  - 处理：复核后重写。“一本名为……的书”直译 a book titled 复核：虽然缩短了书名的引入方式，却增添了“这本书……是根据……写成的”长框架，“写了／写成”重复，整体比原译更拖沓，没有改善阅读。

- 英文：A general “law of least effort” applies to cognitive as well as physical exertion.
  - 原译：一条普遍的“最省力法则”既适用于体力上的付出，也适用于认知上的付出。
  - 现译：有一条普遍的“最省力法则”，既适用于体力上的付出，也适用于认知上的付出。
  - 处理：Astra 复核通过。用“一条……”直接起句，照搬英文不定冠词主语

- 英文：Like a juggler with several balls in the air, you cannot afford to slow down; the rate at which material decays in memory forces the pace, driving you to refresh and rehearse information before it is lost.
  - 原译：就像同时抛着好几个球的杂耍演员一样，你不能放慢速度；记忆里的材料消退的速度决定了你的节奏，逼着你在信息丢失之前不断刷新、复述它。
  - 现译：就像同时抛着好几个球的杂耍演员一样，你不能放慢速度；材料在记忆里消退的速度决定了你的节奏，逼着你赶在信息丢失之前不断刷新、复述。
  - 处理：Astra 复核通过。“记忆里的材料消退的速度”两个“的”叠用，句末多余的“它”

- 英文：“I won’t try to solve this while driving. This is a pupil-dilating task. It requires mental effort!”
  - 原译：“我可不打算边开车边解这道题。这是会让瞳孔放大的任务，得费脑子！”
  - 现译：“我可不打算边开车边解这道题。这可是会让瞳孔放大的活儿，得费脑子！”
  - 处理：Astra 复核通过。饮水机旁的口语用“这是……的任务”，像书面判断句

## 第 3 章 懒惰的控制者

- 英文：My experience is that I can think while strolling but cannot engage in mental work that imposes a heavy load on short-term memory.
  - 原译：我的经验是，散步时我可以思考，但没法从事给短时记忆带来沉重负担的脑力工作。
  - 现译：我的经验是，散步时我可以思考，但没法做那种会给短时记忆带来沉重负担的脑力工作。
  - 处理：Astra 复核通过。“从事”是 engage in 的直译

- 英文：Of course, not all slow thinking requires that form of intense concentration and effortful computation—I did the best thinking of my life on leisurely walks with Amos.
  - 原译：当然，并不是所有的慢思考都需要那种高度的专注和费力的计算：我这辈子最好的思考，就是在和阿莫斯悠闲散步时完成的。
  - 现译：当然，并不是所有的慢思考都需要那种高度的专注和费力的计算：我这辈子思考得最好的时候，就是和阿莫斯一起悠闲散步的时候。
  - 处理：Astra 复核通过。“最好的思考……完成的”直译 did the best thinking

- 英文：As I speed up, my attention is drawn with increasing frequency to the experience of walking and to the deliberate maintenance of the faster pace. My ability to bring a train of thought to a conclusion is impaired accordingly.
  - 原译：随着我越走越快，我的注意力越来越频繁地被引到走路这件事本身上，引到有意维持更快的步伐上。我把一个思路想到底的能力也相应受损。
  - 现译：我走得越快，注意力就越频繁地转向走路这件事本身，转向有意维持较快的步伐。相应地，我也越来越难把一个思路想到底。
  - 处理：Astra 复核通过。“随着……”加被动的“被引到”，“能力……受损”用抽象名词作主语

- 英文：For most of us, most of the time, the maintenance of a coherent train of thought and the occasional engagement in effortful thinking also require self-control.
  - 原译：对我们大多数人来说，在大多数时候，保持连贯的思路、偶尔进行费力的思考，也需要自我控制。
  - 现译：我们大多数人在大多数时候，要保持思路连贯、偶尔费力地思考，也需要自我控制。
  - 处理：Astra 复核通过。“对……来说”“在……时候”两层状语框架，虚化动词“进行”

- 英文：Although I have not conducted a systematic survey, I suspect that frequent switching of tasks and speeded-up mental work are not intrinsically pleasurable, and that people avoid them when possible.
  - 原译：虽然我没有做过系统的调查，但我猜想，频繁地切换任务，以及加快节奏的脑力工作，本身都不让人愉快，人们只要有可能就会避开它们。
  - 现译：虽然我没有做过系统的调查，但我猜想，频繁切换任务、加快节奏做脑力工作，本身都不让人愉快，人们能避开就会避开。
  - 处理：Astra 复核通过。“以及”连接两个名词短语，句末多余的“它们”

- 英文：The psychologist Mihaly Csikszentmihalyi (pronounced six-cent-mihaly) has done more than anyone else to study this state of effortless attending, and the name he proposed for it, flow, has become part of the language.
  - 原译：心理学家米哈里·契克森米哈赖（他的姓读作 six-cent-mihaly）对这种毫不费力的专注状态所做的研究比谁都多，他给这种状态起的名字“心流”，已经成了日常语言的一部分。
  - 现译：心理学家米哈里·契克森米哈赖（他的姓读作 six-cent-mihaly）研究这种毫不费力的专注状态，下的功夫比谁都多；他给这种状态起的名字“心流”，已经成了日常用语。
  - 处理：复核后保留改写。“对……所做的研究”名词化，“成了日常语言的一部分”直译 part of the language 复核：“下的功夫比谁都多”把比较对象从所做的研究工作改成了投入的精力；研究工作做得最多，不等于付出的努力最多。

- 英文：While your attention is focused on the digits, you are offered a choice between two desserts: a sinful chocolate cake and a virtuous fruit salad. The evidence suggests that you would be more likely to select the tempting chocolate cake when your mind is loaded with digits.
  - 原译：就在你专心记数字的时候，有人让你从两种甜点中挑一种：一块罪恶的巧克力蛋糕，一份清白的水果沙拉。证据表明，当你脑子里装满数字时，你更有可能选那块诱人的巧克力蛋糕。
  - 现译：就在你专心记数字的时候，有人让你从两种甜点中挑一种：一块吃了会有罪恶感的巧克力蛋糕，一份吃了心安理得的水果沙拉。证据表明，脑子里装满数字的时候，你更有可能选那块诱人的巧克力蛋糕。
  - 处理：复核后重写。sinful、virtuous 硬译成“罪恶的”“清白的”，“当……时”照搬 when 从句 复核：“问心无愧”直接修饰“水果沙拉”仍然生硬，应落在吃沙拉的人身上，与前面的罪恶感对应。

- 英文：Their experiments involve successive rather than simultaneous tasks.
  - 原译：在他们的实验中，几项任务是先后完成的，而非同时进行。
  - 现译：他们的实验让人先后做几项任务，而不是同时做。
  - 处理：Astra 复核通过。“是……完成的”加书面的“而非……进行”

- 英文：In a typical demonstration, participants who are instructed to stifle their emotional reaction to an emotionally charged film will later perform poorly on a test of physical stamina—how long they can maintain a strong grip on a dynamometer in spite of increasing discomfort.
  - 原译：在一个典型的演示中，参与者被要求在看一部能强烈激起情绪的影片时压抑自己的情绪反应，之后在一项身体耐力测试中，他们的表现会很差：这项测试看的是，尽管越来越难受，他们能把测力计紧紧握住多久。
  - 现译：在一个典型的演示中，研究者让参与者看一部能强烈激起情绪的影片，并要求他们压抑自己的情绪反应；之后做身体耐力测试时，他们的表现会很差：这项测试看的是，尽管越来越难受，他们能把测力计紧紧握住多久。
  - 处理：Astra 复核通过。被动句“被要求在……时……”套长状语，照搬定语从句

- 英文：The most surprising discovery made by Baumeister’s group shows, as he puts it, that the idea of mental energy is more than a mere metaphor.
  - 原译：鲍迈斯特团队最令人吃惊的发现表明，用他的话说，心理能量这个概念不只是一个比喻。
  - 现译：鲍迈斯特团队最令人吃惊的发现表明，心理能量这个概念，用他的话说，不只是一个比喻。
  - 处理：Astra 复核通过。插入语“用他的话说”照搬英文位置，隔开了“表明”和它的宾语

- 英文：When you are actively involved in difficult cognitive reasoning or engaged in a task that requires self-control, your blood glucose level drops.
  - 原译：当你积极投入困难的认知推理，或者从事一项需要自我控制的任务时，你的血糖水平就会下降。
  - 现译：无论是积极投入困难的认知推理，还是做一项需要自我控制的任务，你的血糖水平都会下降。
  - 处理：复核后重写。“当……时”长框架，“从事”，多余的“你的” 复核：“你积极投入……”与“或者在做……时”结构不平行，删去开头的时间关联词后，句子反而不顺。原译的“当……时”清楚统摄两种情形，并非必须删除的翻译腔。

- 英文：While they were performing the task, a series of words crossed the screen in slow succession.
  - 原译：在他们做这项任务时，屏幕上会有一串单词一个接一个地缓缓移过。
  - 现译：他们做这项任务时，一串单词会一个接一个地从屏幕上缓缓移过。
  - 处理：Astra 复核通过。“在……时”加“会有……”存在句，语序拗口

- 英文：A disturbing demonstration of depletion effects in judgment was recently reported in the Proceedings of the National Academy of Sciences.
  - 原译：最近，《美国国家科学院院刊》报道了一项研究，它展示了判断中的损耗效应，结果令人不安。
  - 现译：最近，《美国国家科学院院刊》报道了一项研究，展示了判断中的损耗效应，结果令人不安。
  - 处理：Astra 复核通过。多余的代词“它”

- 英文：The best possible account of the data provides bad news: tired and hungry judges tend to fall back on the easier default position of denying requests for parole.
  - 原译：对这些数据最好的解释带来了坏消息：又累又饿的法官，往往会退回到更省事的默认立场，驳回假释申请。
  - 现译：对这些数据最合理的解释带来了一个坏消息：又累又饿的法官，往往会退回到更省事的默认立场，驳回假释申请。
  - 处理：复核后重写。抽象名词作主语，“解释带来了坏消息”直译 provides bad news 复核：“对这些数据”被硬拆成话题，“最好的解释是个坏消息”也比原句别扭。原译“解释带来了坏消息”可以成立，抽象名词作主语本身不是语病。

- 英文：The distinctive mark of this easy puzzle is that it evokes an answer that is intuitive, appealing, and wrong.
  - 原译：这道简单谜题的显著特点是，它会引出一个直觉的、诱人的、错误的答案。
  - 现译：这道简单谜题的显著特点是，它会引出一个答案：出于直觉，很有吸引力，却是错的。
  - 处理：Astra 复核通过。三个带“的”的形容词堆在名词前

- 英文：His reasoning was that we know a significant fact about anyone who says that the ball costs 10¢: that person did not actively check whether the answer was correct, and her System 2 endorsed an intuitive answer that it could have rejected with a small investment of effort.
  - 原译：他的推理是，对于任何一个说球 10 美分的人，我们都知道一个重要事实：这个人没有主动检查答案对不对，她的系统 2 认可了一个直觉答案，而这个答案本来只要稍微花点力气就能否决。
  - 现译：他的推理是，只要有人说球是 10 美分，我们就知道了关于这个人的一个重要事实：这个人没有主动检查答案对不对，她的系统 2 认可了一个直觉答案，而这个答案本来只要稍微花点力气就能否决。
  - 处理：Astra 复核通过。“对于任何一个……的人”照搬 about anyone who

- 英文：The bat-and-ball problem is our first encounter with an observation that will be a recurrent theme of this book: many people are overconfident, prone to place too much faith in their intuitions. They apparently find cognitive effort at least mildly unpleasant and avoid it as much as possible.
  - 原译：通过球拍和球问题，我们第一次碰到了一个观察结果，它将是本书反复出现的主题：许多人过度自信，容易过分相信自己的直觉。他们显然觉得认知努力至少有点令人不快，并且尽可能地回避它。
  - 现译：在球拍和球问题中，我们第一次碰到了一个本书会反复谈到的现象：许多人过度自信，容易过分相信自己的直觉。他们似乎觉得认知努力至少有点令人不快，并且能避就避。
  - 处理：按复核意见修改。“一个观察结果，它将是……”照搬定语从句，句末多余的“它” 复核：沿用了原译对 apparently 的过强处理。这里是从行为表现推测人们的感受，“显然”提高了确定程度，应保留“似乎／看来”的语气。

- 英文：Just as in the bat-and-ball problem, a plausible answer comes to mind immediately.
  - 原译：就像在球拍和球问题中那样，一个看似合理的答案立刻浮现在脑中。
  - 现译：就像在球拍和球问题中那样，脑子里立刻冒出了一个看似合理的答案。
  - 处理：Astra 复核通过。“一个……的答案”作主语，照搬英文主谓语序

- 英文：This experiment has discouraging implications for reasoning in everyday life. It suggests that when people believe a conclusion is true, they are also very likely to believe arguments that appear to support it, even when these arguments are unsound.
  - 原译：对于日常生活中的推理，这个实验的含义令人沮丧。它表明，当人们相信一个结论为真时，他们也很可能会相信那些看似支持这个结论的论证，即使这些论证并不可靠。
  - 现译：对日常生活中的推理来说，这个实验的含义令人沮丧。它表明，人们如果相信一个结论是真的，就很可能也会相信那些看似支持它的论证，即使这些论证在逻辑上站不住脚。
  - 处理：复核后重写。“对于……”起句，“当……时”和多余的“他们” 复核：“放到日常生活的推理中”搭配生硬，没有说清实验对日常推理的启示；此处 unsound 指论证在逻辑上不成立，“不可靠”过于含混。

- 英文：Next, consider the following question and answer it quickly before reading on:
  - 原译：接下来，请考虑下面这个问题，先快速回答，再往下读：
  - 现译：接下来，请看下面这个问题，先快速回答，再往下读：
  - 处理：Astra 复核通过。consider 直译成“考虑”

- 英文：But knowledge of a fact is not all-or-none. Facts that we know do not always come to mind when we need them.
  - 原译：但知道一个事实，并不是全有或全无的事。我们知道的事实，并不总会在需要时浮现在脑中。
  - 现译：但我们对一个事实的掌握，并非只有“知道”和“不知道”两种状态。我们知道的事实，需要的时候不一定想得起来。
  - 处理：按复核意见修改。all-or-none 硬译成“全有或全无”，“浮现在脑中”书面直译 复核：首句把“知道一个事实”与“知道和不知道两种情况”叠在一起，仍然绕口，容易形成逻辑歧义；应以对事实的掌握状态为讨论对象。

- 英文：Indeed, the average guess by people who were asked about Michigan is lower than the guesses of a similar group who were asked about the murder rate in Detroit.
  - 原译：事实上，被问到密歇根州的人给出的平均猜测，比另一组相似的人被问到底特律的谋杀率时给出的猜测还要低。
  - 现译：事实上，问的是密歇根州时，人们猜测的平均值，比另一组相似的人对底特律谋杀率的猜测还要低。
  - 处理：Astra 复核通过。两个“被问到……给出的”长定语

- 英文：The extent of deliberate checking and search is a characteristic of System 2, which varies among individuals.
  - 原译：刻意检查和搜索的程度，是系统 2 的一个特征，它因人而异。
  - 现译：刻意检查和搜索到什么程度，是系统 2 的一个特征，因人而异。
  - 处理：Astra 复核通过。“……的程度”抽象名词作主语，which 从句译出多余的“它”

- 英文：Failing these minitests appears to be, at least to some extent, a matter of insufficient motivation, not trying hard enough.
  - 原译：在这些小测验中失败，看来至少在一定程度上是动机不足的问题，也就是不够努力。
  - 现译：答错这几道题，看来至少在一定程度上是因为动机不足，也就是不够努力。
  - 处理：复核后重写。动名词 failing 硬译成“在……中失败” 复核：“几道小测验”量词搭配不当：“道”用于题目，测验通常用“项”或“个”。

- 英文：“Lazy” is a harsh judgment about the self-monitoring of these young people and their System 2, but it does not seem to be unfair.
  - 原译：说这些年轻人和他们的系统 2 在自我监控上“懒惰”，是一个严厉的评判，但似乎也不算冤枉。
  - 现译：说这些年轻人和他们的系统 2 在自我监控上“懒惰”，这个评价很严厉，但似乎也不算冤枉。
  - 处理：Astra 复核通过。“是一个严厉的评判”照搬 is a harsh judgment

- 英文：Some have addressed it by asking the correlation question: If people were ranked by their self-control and by their cognitive aptitude, would individuals have similar positions in the two rankings?
  - 原译：有些人通过提出相关性的问题来研究它：如果分别按自我控制能力和认知能力给人们排名，同一个人在两个排名中的位置会不会差不多？
  - 现译：有些研究者问的是相关性问题：如果分别按自我控制能力和认知能力给人们排名，同一个人在两个排名中的位置会不会差不多？
  - 处理：Astra 复核通过。“通过……来研究它”照搬 by asking，多余的“它”

- 英文：The children were watched through a one-way mirror, and the film that shows their behavior during the waiting time always has the audience roaring in laughter.
  - 原译：研究者透过单向镜观察孩子们，记录他们在等待期间表现的影片，每次放映都会让观众哄堂大笑。
  - 现译：研究者透过单向镜观察孩子们，还拍下了他们等待时的表现，这段影片每次放映都会让观众哄堂大笑。
  - 处理：Astra 复核通过。长定语“记录他们在等待期间表现的影片”作主语，容易误读成动宾

- 英文：We recognize related differences among individuals: some people are more like their System 2; others are closer to their System 1.
  - 原译：我们也能在个人之间看出相应的差异：有些人更像他们的系统 2，另一些人则更接近他们的系统 1。
  - 现译：在不同的人身上，我们也能看到相应的差异：有些人更像自己的系统 2，另一些人则更接近自己的系统 1。
  - 处理：Astra 复核通过。“在个人之间看出差异”照搬 among individuals，“他们的”多余

- 英文：Stanovich published his conclusions in a book titled Rationality and the Reflective Mind, which offers a bold and distinctive approach to the topic of this chapter. He draws a sharp distinction between two parts of System 2—indeed, the distinction is so sharp that he calls them separate “minds.”
  - 原译：斯坦诺维奇把他的结论写进了一本名为《理性与反思心智》（Rationality and the Reflective Mind）的书，对本章的主题提出了一种大胆而独特的看法。他把系统 2 截然分成两个部分，分得如此清楚，以至于把这两部分称为两个独立的“心智”。
  - 现译：斯坦诺维奇把他的结论写进了《理性与反思心智》（Rationality and the Reflective Mind）一书，这本书对本章的主题提出了一种大胆而独特的看法。他把系统 2 截然分成两个部分，分得极其清楚，甚至把这两部分称为两个独立的“心智”。
  - 处理：Astra 复核通过。“一本名为……的书”，“如此……以至于”照搬 so...that

- 英文：Time will tell whether the distinction between intelligence and rationality can lead to new discoveries.
  - 原译：智力与理性的区分能否带来新的发现，只有时间能告诉我们。
  - 现译：智力与理性的区分能否带来新的发现，还有待时间检验。
  - 处理：Astra 复核通过。Time will tell 硬译成“只有时间能告诉我们”

## 第 4 章 联想机器

- 英文：As a result, you are experiencing a temporary aversion to bananas (don’t worry, it will pass).
  - 原译：结果，你现在对香蕉有了一种暂时的反感（别担心，这会过去的）。
  - 现译：结果，你现在对香蕉暂时有些反感（别担心，这会过去的）。
  - 处理：复核后重写。“有了一种暂时的反感”是名词化直译，多了“一种” 复核：“暂时反感起香蕉来了”语序拗口，“暂时”与“起……来了”叠用不自然，反而不如原译清楚。

- 英文：All this happens quickly and all at once, yielding a self-reinforcing pattern of cognitive, emotional, and physical responses that is both diverse and integrated—it has been called associatively coherent.
  - 原译：这一切都发生得很快，而且同时发生，形成了一种由认知、情绪和身体反应组成的自我强化模式，它既多样又融为一体，人们说它具有联想一致性。
  - 现译：这一切都发生得很快，而且同时发生，认知、情绪和身体上的反应形成了一种自我强化的模式：它既多样又融为一体，人们说它具有联想一致性。
  - 处理：Astra 复核通过。名词前堆了长定语“由……组成的”，后面又接代词“它”补说

- 英文：I will adopt an expansive view of what an idea is.
  - 原译：对于什么是观念，我会采取一种宽泛的理解。
  - 现译：我对“观念”的理解会比较宽泛。
  - 处理：Astra 复核通过。“对于……”开头加虚化动词“采取一种……理解”

- 英文：In the 1980s, psychologists discovered that exposure to a word causes immediate and measurable changes in the ease with which many related words can be evoked.
  - 原译：20 世纪 80 年代，心理学家发现，接触一个词，会让许多相关的词被唤起的难易程度立刻发生可以测量的变化。
  - 现译：20 世纪 80 年代，心理学家发现，人接触一个词之后，许多相关的词被唤起的难易程度会立刻发生变化，而且这种变化可以测量。
  - 处理：Astra 复核通过。照搬英文名词结构，“发生可以测量的变化”前后修饰挤在一起

- 英文：Furthermore, the primed ideas have some ability to prime other ideas, although more weakly.
  - 原译：此外，受到启动的观念也有一定的能力去启动其他观念，只是作用更弱。
  - 现译：此外，受到启动的观念自己也能在一定程度上启动其他观念，只是作用更弱。
  - 处理：Astra 复核通过。“有一定的能力去”直译 have some ability to

- 英文：For one group of students, half the scrambled sentences contained words associated with the elderly, such as Florida, forgetful, bald, gray, or wrinkle.
  - 原译：对其中一组学生来说，这些打乱的句子中有一半含有与老年人相关的词，比如“佛罗里达”[^t2]、“健忘”“秃顶”“灰白”或“皱纹”。
  - 现译：其中一组学生拿到的打乱的句子里，有一半含有与老年人相关的词，比如“佛罗里达”[^t2]、“健忘”“秃顶”“灰白”或“皱纹”。
  - 处理：Astra 复核通过。“对……来说”直译 For one group

- 英文：A study conducted in a German university was the mirror image of the early experiment that Bargh and his colleagues had carried out in New York.
  - 原译：德国一所大学做过一项研究，它正好是巴奇和同事早先在纽约所做实验的镜像。
  - 现译：德国一所大学做过一项研究，正好是巴奇和同事早先在纽约所做实验的镜像。
  - 处理：Astra 复核通过。多余的代词“它”

- 英文：After this brief experience, the participants were much quicker to recognize words related to old age, such as forgetful, old, and lonely.
  - 原译：有了这段短暂的经历之后，参与者认出与老年有关的词（比如“健忘”“老”“孤独”）要快得多。
  - 现译：这样走了一小会儿之后，参与者认出与老年有关的词（比如“健忘”“老”“孤独”）要快得多。
  - 处理：Astra 复核通过。“有了这段短暂的经历”直译 brief experience，中文不这样说一次走路

- 英文：College students were asked to rate the humor of cartoons from Gary Larson’s The Far Side while holding a pencil in their mouth.
  - 原译：研究者请大学生嘴里含着铅笔，给加里·拉森的漫画 The Far Side 中的作品评定有多好笑。
  - 现译：研究者请大学生嘴里含着铅笔，评一评加里·拉森的漫画 The Far Side 里的作品有多好笑。
  - 处理：Astra 复核通过。“给……评定有多好笑”搭配生硬

- 英文：In another experiment, people whose face was shaped into a frown (by squeezing their eyebrows together) reported an enhanced emotional response to upsetting pictures—starving children, people arguing, maimed accident victims.
  - 原译：在另一项实验中，脸被摆成皱眉表情的人（方法是让他们把眉头挤到一起），看到令人不安的图片时，报告说自己的情绪反应更强烈，这些图片包括挨饿的儿童、正在争吵的人、在事故中致残的伤者。
  - 现译：在另一项实验中，研究者让一些人把眉头挤到一起，做出皱眉的表情；这些人在看到令人不安的图片（比如挨饿的儿童、正在争吵的人、在事故中致残的伤者）时，报告说自己的情绪反应更强烈。
  - 处理：按复核意见修改。“脸被摆成……的人”被动长定语，图片内容拖在句尾补充 复核：后半句“这些人看到……，报告的情绪反应更强烈”衔接不顺，长串图片举例又隔断了句子；应明确观看图片的时间关系，并保留参与者自述这一层意思。

- 英文：Again, there was no awareness, just a habitual connection between an attitude of rejection or acceptance and its common physical expression.
  - 原译：这里同样没有任何察觉，有的只是拒绝或接受的态度与它常见的身体表现之间的习惯性联系。
  - 现译：人们同样毫无察觉，有的只是一种习惯性的联系：一边是拒绝或接受的态度，一边是这种态度常见的身体表现。
  - 处理：Astra 复核通过。“这里没有任何察觉”缺主语，“A 与 B 之间的联系”长定语

- 英文：For instance, most of us think of voting as a deliberate act that reflects our values and our assessments of policies and is not influenced by irrelevancies.
  - 原译：例如，我们大多数人认为，投票是一种深思熟虑的行为，它反映我们的价值观和我们对政策的评估，不受无关因素的影响。
  - 现译：例如，我们大多数人认为，投票是一种深思熟虑的行为，反映的是我们的价值观和我们对政策的评估，不受无关因素的影响。
  - 处理：Astra 复核通过。照搬定语从句，多了代词“它”

- 英文：A separate experiment showed that exposing people to images of classrooms and school lockers also increased the tendency of participants to support a school initiative.
  - 原译：另一项实验表明，让人们看教室和学校储物柜的图片，也会提高参与者支持一项学校提案的倾向。
  - 现译：另一项实验表明，给人们看教室和学校储物柜的图片，也会让参与者更倾向于支持一项学校提案。
  - 处理：Astra 复核通过。“提高……的倾向”直译 increased the tendency

- 英文：In another experiment in the series, participants were told that they would shortly have a get-acquainted conversation with another person and were asked to set up two chairs while the experimenter left to retrieve that person.
  - 原译：在这一系列实验的另一项中，研究者告诉参与者，他们马上要和另一个人进行一次互相认识的谈话，并请他们在实验者出去带那个人过来时摆好两把椅子。
  - 现译：在这一系列实验的另一项中，研究者告诉参与者，他们马上要和另一个人聊一聊，彼此认识一下，并请他们在实验者出去带那个人过来时摆好两把椅子。
  - 处理：Astra 复核通过。虚化动词“进行一次……的谈话”

- 英文：The psychologist who has done this remarkable research, Kathleen Vohs, has been laudably restrained in discussing the implications of her findings, leaving the task to her readers.
  - 原译：做出这些出色研究的心理学家凯瑟琳·沃斯，在讨论这些发现有什么含义时非常克制，令人称道，她把这项任务留给了读者。
  - 现译：做出这些出色研究的是心理学家凯瑟琳·沃斯，她在讨论这些发现有什么含义时非常克制，把这项任务留给了读者，这一点令人称道。
  - 处理：复核后重写。主语已经出现，句中又用“她”重复主语 复核：“令人称道，把这项任务留给了读者”的衔接比原译生硬。原译末尾的“她”用于在插入评价后接回行动主体，并非无效重复。

- 英文：I conclude with a perfect demonstration of a priming effect, which was conducted in an office kitchen at a British university.
  - 原译：最后，我再介绍一个完美的启动效应演示，它是在英国一所大学的办公室茶水间里进行的。
  - 现译：最后，我再介绍一个完美的启动效应演示，地点在英国一所大学的办公室茶水间。
  - 处理：Astra 复核通过。照搬 which 从句，“它是……进行的”

- 英文：Evidently, a purely symbolic reminder of being watched prodded people into improved behavior.
  - 原译：显然，一个纯粹象征性的、提醒人们正被注视的东西，促使人们表现得更好。
  - 现译：显然，纯粹象征性地提醒人们有人在看着，就促使他们表现得更好了。
  - 处理：Astra 复核通过。抽象名词作主语，前面堆着两层定语

- 英文：It is the source of your rapid and often precise intuitive judgments.
  - 原译：它是你那些迅速而且常常很准确的直觉判断的来源。
  - 现译：你那些迅速而且常常很准确的直觉判断，就来自它。
  - 处理：Astra 复核通过。“是……的来源”中间夹了一长串定语

## 第 5 章 认知放松

- 英文：Whenever you are conscious, and perhaps even when you are not, multiple computations are going on in your brain, which maintain and update current answers to some key questions:
  - 原译：只要你是清醒的，也许甚至在你不清醒的时候，你的大脑里都有多项计算在同时进行，它们维持并不断更新着对一些关键问题的当前答案：
  - 现译：只要你是清醒的，也许甚至在你不清醒的时候，你的大脑里都有多项计算在同时进行，它们维持并不断更新着对一些关键问题的当前答案：
  - 处理：复核后退回原译。照搬 which 从句用“它们”，“对……的当前答案”生硬 复核：“为一些关键问题保持……答案”搭配不自然，改写没有消除翻译腔，反而不如原译的指代和句法清楚。

- 英文：You know, and will know for a while, that these are not the names of minor celebrities.
  - 原译：你知道，而且在一段时间里都会知道，这些不是小有名气的人的名字。
  - 现译：你知道，而且在一段时间里都会知道，这些不是小有名气的人的名字。
  - 处理：复核后退回原译。“的人的名字”的字连串 复核：“这些名字不属于哪个……人”表达生硬，不如“这些不是……人的名字”直接清楚；改写没有改善中文。

- 英文：There is a substantial probability that you will identify David Stenbill as a well-known person, although you will not (of course) know whether you encountered his name in the context of movies, sports, or politics.
  - 原译：你很有可能把戴维·斯滕比尔认作名人，虽然你（当然）不会知道自己是在电影、体育还是政治的背景下看到他的名字的。
  - 现译：你很有可能把戴维·斯滕比尔认作名人，虽然你（当然）不会知道，自己是在和电影、体育还是政治有关的场合见到他的名字的。
  - 处理：Astra 复核通过。“在……的背景下”直译 in the context of

- 英文：System 2 was involved in sifting that information, perhaps raising the issue of whether the question about New York was too easy, or checking the meaning of revolves.
  - 原译：系统 2 参与了对这些信息的筛选，它也许问过自己，关于纽约的那道题是不是太简单了，也许还核对过“绕着……转”（revolves）是什么意思。
  - 现译：筛选这些信息时，系统 2 参与了进来：它也许问过自己，关于纽约的那道题是不是太简单了，也许还核对过“绕着……转”（revolves）是什么意思。
  - 处理：Astra 复核通过。“参与了对……的筛选”名词化

- 英文：The familiarity of one phrase in the statement sufficed to make the whole statement feel familiar, and therefore true.
  - 原译：陈述中一个短语的熟悉感，就足以让整个陈述显得熟悉，因而显得真实。
  - 现译：只要陈述中有一个短语让人觉得熟悉，整个陈述就会显得熟悉，因而显得真实。
  - 处理：Astra 复核通过。抽象名词“……的熟悉感”作主语

- 英文：The general principle is that anything you can do to reduce cognitive strain will help, so you should first maximize legibility.
  - 原译：总的原则是，凡是你能做的、可以减轻认知紧张的事，都会有帮助，所以你首先应该让文字尽可能清晰易读。
  - 现译：总的原则是，凡是能减轻认知紧张的做法都有帮助，所以你首先应该让文字尽可能清晰易读。
  - 处理：Astra 复核通过。两层定语“你能做的、可以……的事”照搬英文

- 英文：My Princeton colleague Danny Oppenheimer refuted a myth prevalent among undergraduates about the vocabulary that professors find most impressive.
  - 原译：我在普林斯顿的同事丹尼·奥本海默，驳斥了本科生中流行的一种迷思，这种迷思关乎什么样的词汇最能让教授刮目相看。
  - 现译：我在普林斯顿的同事丹尼·奥本海默，驳斥了本科生中流行的一种迷思，这种迷思关乎什么样的词汇最能让教授刮目相看。
  - 处理：复核后退回原译。“这种迷思关乎……”是 about 的直译 复核：“说的是”缺少清楚的承接主体，容易与前面的奥本海默相连；原译明确说明是“这种迷思”涉及什么问题，反而更清楚。

- 英文：The best procedure for the observers would have been to average the two reports, but this is not what they did. They gave much more weight to the report from Artan than to the report from Taahhut.
  - 原译：对这些观察者来说，最好的做法本该是取两份报告的平均值，但他们没有这样做。他们对 Artan 报告的重视，远远超过对 Taahhut 报告的重视。
  - 现译：这些观察者最好的做法本该是取两份报告的平均值，但他们没有这样做。比起 Taahhut 的报告，他们对 Artan 的报告要重视得多。
  - 处理：按复核意见修改。“对……来说”和“对……的重视远远超过对……的重视”名词化 复核：“看重 Artan 的报告得多”比较补语位置不当，应改为“对 Artan 的报告要重视得多”。

- 英文：High-quality paper, bright colors, and rhyming or simple language will not be much help if your message is obviously nonsensical, or if it contradicts facts that your audience knows to be true.
  - 原译：如果你的信息明显是胡说八道，或者与听众知道是真的事实相矛盾，那么高质量的纸张、鲜艳的颜色、押韵或简单的语言都帮不了多大忙。
  - 现译：如果你的信息明显是胡说八道，或者与受众已知的事实相矛盾，那么高质量的纸张、鲜艳的颜色、押韵或简单的语言都帮不了多大忙。
  - 处理：按复核意见修改。“听众知道是真的事实”照搬 knows to be true，读着拗口 复核：audience 在这里泛指信息接收者，包括读者，译成“听众”范围过窄；“明知为真”也带有不必要的强调。

- 英文：The symmetry of many associative connections was a dominant theme in the discussion of associative coherence.
  - 原译：在讨论联想一致性时，许多联想关系的对称性是一个主要议题。
  - 现译：讨论联想一致性时，一个主要的话题是：许多联想关系是对称的。
  - 处理：Astra 复核通过。抽象名词“……的对称性”作主语

- 英文：Indeed, the mere exposure effect is actually stronger for stimuli that the individual never consciously sees.
  - 原译：其实，对于一个人从未有意识地看到的刺激，单纯曝光效应反而更强。
  - 现译：其实，一个人从未有意识地看到过的刺激，产生的单纯曝光效应反而更强。
  - 处理：Astra 复核通过。“对于……”直译 for stimuli

- 英文：Survival prospects are poor for an animal that is not suspicious of novelty.
  - 原译：一只对新奇事物不起疑心的动物，生存的前景是很糟糕的。
  - 现译：动物要是对新奇事物不起疑心，生存下去的机会就不大。
  - 处理：按复核意见修改。多余的“一只”，长定语，“前景是很糟糕的”搭配生硬 复核：“生存的希望就很渺茫”比原文 poor 的程度更重，容易让人理解为几乎无法存活；宜表述为生存机会不大。

- 英文：The consequences of repeated exposures benefit the organism in its relations to the immediate animate and inanimate environment.
  - 原译：反复接触带来的后果，有益于生物体与周围有生命和无生命环境之间的关系。
  - 现译：反复接触带来的影响，让生物体在与周围的生物和非生物打交道时受益。
  - 处理：复核后重写。“有益于……之间的关系”照搬 benefit ... in its relations 复核：“有生命和无生命的环境”仍然生硬，容易读成环境本身有无生命；这里指周围的生物和无生命事物。“后果”用于这些有益影响也不够自然。

- 英文：The role of cognitive ease in the judgment was confirmed experimentally by another German team: manipulations that increase cognitive ease (priming, a clear font, pre-exposing words) all increase the tendency to see the words as linked.
  - 原译：另一个德国团队用实验证实了认知放松在这种判断中的作用：凡是能增加认知放松的操作（启动、清晰的字体、预先呈现这些词），都会增加人们把这些词看成有联系的倾向。
  - 现译：另一个德国团队用实验证实了认知放松在这种判断中的作用：凡是能增加认知放松的操作（启动、清晰的字体、预先呈现这些词），都会让人们更倾向于把这些词看成有联系的。
  - 处理：Astra 复核通过。“增加……的倾向”直译 increase the tendency

- 英文：Mood evidently affects the operation of System 1: when we are uncomfortable and unhappy, we lose touch with our intuition.
  - 原译：心情显然会影响系统 1 的运作：当我们感到不舒服、不开心时，我们就和自己的直觉失去了联系。
  - 现译：心情显然会影响系统 1 的运作：我们感到不舒服、不开心的时候，就和自己的直觉失去了联系。
  - 处理：Astra 复核通过。“当……时”加重复的主语“我们”

- 英文：These findings add to the growing evidence that good mood, intuition, creativity, gullibility, and increased reliance on System 1 form a cluster.
  - 原译：支持下面这个看法的证据越来越多，这些发现又是其中的新证据：好心情、直觉、创造力、轻信，以及更多地依赖系统 1，是相伴出现的一组特征。
  - 现译：越来越多的证据表明，好心情、直觉、创造力、轻信，以及更多地依赖系统 1，是相伴出现的一组特征；这些发现又为此添了新的证据。
  - 处理：Astra 复核通过。为了照顾 evidence that 从句，用“下面这个看法”“其中的新证据”绕了一圈

- 英文：The Remote Association Test has more to tell us about the link between cognitive ease and positive affect.
  - 原译：关于认知放松与积极情感之间的联系，远距离联想测验还能告诉我们更多。
  - 现译：远距离联想测验还能让我们更多地了解认知放松与积极情感之间的联系。
  - 处理：Astra 复核通过。“还能告诉我们更多”直译 has more to tell us

- 英文：The impression of cognitive ease that comes with the presentation of a coherent triad appears to be mildly pleasurable in itself.
  - 原译：看到一组连贯的三个词时产生的认知放松印象，本身似乎就让人有些愉快。
  - 现译：看到一组连贯的三个词时，人会产生认知放松的印象，这种印象本身似乎就让人有些愉快。
  - 处理：复核后保留改写。主语前堆了一整句定语 复核：“一组连贯的三个词”量词和定语叠用，仍然生硬；可沿用上下文的“三词组”，同时保留三个词这一数量。

- 英文：The evidence that we have about good feelings, cognitive ease, and the intuition of coherence is, as scientists say, correlational but not necessarily causal.
  - 原译：我们掌握的关于愉快感、认知放松和连贯性直觉的证据，用科学家的话说，是相关性的，不一定是因果性的。
  - 现译：关于愉快感、认知放松和连贯性直觉，我们掌握的证据用科学家的话说是相关性的，不一定是因果性的。
  - 处理：Astra 复核通过。“我们掌握的关于……的证据”双层长定语

- 英文：It was beyond imagining that bad font influences judgments of truth and improves cognitive performance, or that an emotional response to the cognitive ease of a triad of words mediates impressions of coherence.
  - 原译：那时谁也想象不到，糟糕的字体会影响人们对真假的判断，还能提高认知表现；也想象不到，对一组三个词的认知放松所产生的情绪反应，会在连贯性印象的形成中起中介作用。
  - 现译：那时谁也想象不到，糟糕的字体会影响人们对真假的判断，还能提高认知表现；也想象不到，一组三个词带来的认知放松会引起情绪反应，而连贯性的印象正是以这种情绪反应为中介形成的。
  - 处理：Astra 复核通过。“对……所产生的情绪反应”“在……的形成中起中介作用”双重名词化

- 英文：“Familiarity breeds liking. This is a mere exposure effect.”
  - 原译：> “熟悉产生好感。这是单纯曝光效应。”
  - 现译：> “熟悉了就会有好感，这是单纯曝光效应。”
  - 处理：Astra 复核通过。“熟悉产生好感”是书面直译，不像饮水机旁的口头话

- 英文：“I’m in a very good mood today, and my System 2 is weaker than usual. I should be extra careful.”
  - 原译：> “我今天心情特别好，我的系统 2 比平时弱。我得格外小心。”
  - 现译：> “我今天心情特别好，系统 2 比平时弱，得格外小心。”
  - 处理：Astra 复核通过。口语里连用三个“我”，照搬英文主语

## 第 6 章 常态、意外与原因

- 英文：The spreading of activation in the associative machine is automatic, but we (System 2) have some ability to control the search of memory, and also to program it so that the detection of an event in the environment can attract attention.
  - 原译：联想机器里激活的扩散是自动的，但我们（系统 2）有一定的能力控制对记忆的搜索，还能给它设定程序，让环境中的某个事件一被察觉就能吸引注意。
  - 现译：在联想机器里，激活是自动扩散的，但我们（系统 2）能在一定程度上控制怎样搜索记忆，还能给记忆设定程序，让环境中的某个事件一被察觉就能吸引注意。
  - 处理：复核后重写。抽象名词“激活的扩散”作主语，“对记忆的搜索”名词化，“它”指代不清 复核：把 it 明确改成“这种搜索”缩窄了指代；结合前文 program your memory 的说明，这里说的是给记忆系统设定程序。

- 英文：The main function of System 1 is to maintain and update a model of your personal world, which represents what is normal in it.
  - 原译：系统 1 的主要功能，是维护和更新一个关于你个人世界的模型，这个模型表征了你的世界里什么是正常的。
  - 现译：系统 1 的主要功能，是维护和更新你个人世界的模型，这个模型表征的是你的世界里什么是正常的。
  - 处理：Astra 复核通过。“一个关于……的模型”照搬 a model of

- 英文：As these links are formed and strengthened, the pattern of associated ideas comes to represent the structure of events in your life, and it determines your interpretation of the present as well as your expectations of the future.
  - 原译：随着这些联系的形成和加强，相互联想的观念所构成的模式逐渐表征了你生活中各种事件的结构，它决定了你怎样解释现在，也决定了你对未来有怎样的预期。
  - 现译：随着这些联系形成并不断加强，彼此关联的观念所构成的模式逐渐表征了你生活中各种事件的结构；这个模式决定了你怎样解释现在，也决定了你对未来有怎样的预期。
  - 处理：复核后重写。“随着……的形成和加强”名词化，句中“它”照搬 it 复核：“相互联想的观念”搭配不当，associated ideas 指彼此关联的观念；“慢慢表征出”也仍然生硬。

- 英文：When we came to dinner, we were surprised to meet an acquaintance, a psychologist named Jon.
  - 原译：我们去吃晚饭时，意外地遇到了一位熟人，一位名叫乔恩的心理学家。
  - 现译：我们去吃晚饭时，意外地遇到了一位熟人，心理学家乔恩。
  - 处理：Astra 复核通过。同位语“一位……，一位名叫……的”照搬英文

- 英文：On a Sunday evening some years ago, we were driving from New York City to Princeton, as we had been doing every week for a long time.
  - 原译：几年前的一个星期天傍晚，我们开车从纽约市去普林斯顿，很长一段时间以来，我们每周都这样开一趟。
  - 现译：几年前的一个星期天傍晚，我们开车从纽约市去普林斯顿，这条路我们每周都开，已经开了很久。
  - 处理：Astra 复核通过。“很长一段时间以来”照搬 for a long time 的从句

- 英文：Because the circumstances of the recurrence were the same, the second incident was sufficient to create an active expectation: for months, perhaps for years, after the event we were reminded of burning cars whenever we reached that spot of the road and were quite prepared to see another one (but of course we never did).
  - 原译：由于事情重演时的情境相同，第二次事件就足以形成一个主动的预期：在那之后的几个月，也许是几年里，我们每次开到那段路，都会想起着火的汽车，而且随时准备好再看到一辆（当然，我们再也没有看到过）。
  - 现译：由于事情重演时的情境一样，第二次就足以让我们形成主动的预期：在那之后的几个月，也许是几年里，我们每次开到那段路，都会想起着火的汽车，而且完全做好了再看到一辆的心理准备（当然，我们再也没有看到过）。
  - 处理：复核后重写。“第二次事件就足以形成一个主动的预期”以事件作主语，生硬 复核：“随时准备好再看到一辆”仍是生硬直译；quite prepared 强调充分的心理准备，不是“随时”这一时间限定。

- 英文：The psychologist Dale Miller and I wrote an essay in which we attempted to explain how events come to be perceived as normal or abnormal.
  - 原译：心理学家戴尔·米勒和我写过一篇文章，试图解释事件是怎样被人看成正常或反常的。
  - 现译：心理学家戴尔·米勒和我写过一篇文章，试图解释事件是怎样被人看成正常或反常的。
  - 处理：复核后退回原译。不必要的被动句“被人看成” 复核：“人们怎样会把”搭配生硬，容易读成“人们怎么会”的疑问语气。原译的被动句自然、准确，没有必要强行改成主动句。

- 英文：Replace Moses with George W. Bush in this sentence and you will have a poor political joke but no illusion.
  - 原译：把这句话里的摩西换成乔治·W. 布什，你会得到一个蹩脚的政治笑话，却不会产生错觉。
  - 现译：把这句话里的摩西换成乔治·W. 布什，就成了一个蹩脚的政治笑话，但不会产生错觉。
  - 处理：Astra 复核通过。“你会得到一个……”直译 you will have

- 英文：When I mention a table, without specifying further, you understand that I mean a normal table.
  - 原译：我提到一张桌子而不作进一步说明时，你明白我指的是一张正常的桌子。
  - 现译：我说起一张桌子，没有再加说明，你就明白我指的是一张正常的桌子。
  - 处理：Astra 复核通过。“而不作进一步说明时”虚化动词加“……时”

- 英文：We have norms for a vast number of categories, and these norms provide the background for the immediate detection of anomalies such as pregnant men and tattooed aristocrats.
  - 原译：对于数量庞大的各种类别，我们都有相应的常态，这些常态提供了背景，让我们能立刻察觉怀孕的男人、有文身的贵族这类反常现象。
  - 现译：我们心里对非常多的类别都有相应的常态，这些常态构成了背景，让我们能立刻察觉怀孕的男人、有文身的贵族这类反常现象。
  - 处理：复核后重写。句首“对于……”照搬 for 复核：“对……都有相应的常态”没有说清这是心中的常态认识；“数量庞大的各种类别”也仍然累赘。

- 英文：In your network of associations, anger and lack of punctuality are linked as an effect and its possible cause, but there is no such link between anger and the idea of expecting caterers.
  - 原译：在你的联想网络里，生气和不守时作为结果和可能的原因联系在一起，但生气和等承办宴席的人到来这个念头之间，并没有这样的联系。
  - 现译：在你的联想网络里，生气和不守时联系在一起，一个是结果，一个是可能的原因；但生气和等承办宴席的人到来这个念头之间，并没有这样的联系。
  - 处理：Astra 复核通过。“作为……联系在一起”照搬 linked as

- 英文：System 2, your conscious self, was offered the causal interpretation and accepted it.
  - 原译：系统 2，也就是你有意识的自我，得到了这个因果解释，并接受了它。
  - 现译：系统 2，也就是你有意识的自我，收到这个因果解释后，就接受了它。
  - 处理：复核后重写。句末“并接受了它”多余代词 复核：“接受了下来”搭配生硬，比原来的“并接受了它”更不自然；原译中的宾语代词并不多余。

- 英文：A story in Nassim Taleb’s The Black Swan illustrates this automatic search for causality.
  - 原译：纳西姆·塔勒布的《黑天鹅》里有一个故事，很能说明这种对因果关系的自动搜寻。
  - 现译：纳西姆·塔勒布的《黑天鹅》里有一个故事，很能说明我们怎样自动搜寻因果关系。
  - 处理：Astra 复核通过。“这种对……的自动搜寻”名词化

- 英文：We have limited information about what happened on a day, and System 1 is adept at finding a coherent causal story that links the fragments of knowledge at its disposal.
  - 原译：对于某一天发生了什么，我们掌握的信息有限，而系统 1 擅长找到一个连贯的因果故事，把它手头那些零碎的知识串联起来。
  - 现译：一天里发生了什么，我们掌握的信息有限，而系统 1 擅长找到一个连贯的因果故事，把手头那些零碎的知识串联起来。
  - 处理：Astra 复核通过。句首“对于……”，多余代词“它”

- 英文：When people who had read this brief story (along with many others) were given a surprise recall test, the word pickpocket was more strongly associated with the story than the word sights, even though the latter was actually in the sentence while the former was not.
  - 原译：有人读过这个小故事（还有许多别的故事）之后，接受了一次事先没有告知的回忆测验，结果“扒手”这个词与这个故事的联系，比“景色”这个词更强，尽管后者确实出现在句子里，而前者并没有。
  - 现译：有人读过这个小故事（还有许多别的故事）之后，接受了一次突击回忆测验，结果“扒手”这个词与这个故事的联系，比“景色”这个词更强，尽管句子里确实有“景色”，却没有“扒手”。
  - 处理：Astra 复核通过。“后者……前者”照搬 the latter/the former，“事先没有告知的”定语啰嗦

- 英文：In the story of the startling soup, the outcome—whether another customer wincing at the taste of the soup or the first person’s extreme reaction to the waiter’s touch—brings about an associatively coherent interpretation of the initial surprise, completing a plausible story.
  - 原译：在那个令人吃惊的汤的故事里，后来发生的事，无论是另一位客人尝了汤也皱起脸，还是第一位客人被服务员一碰就反应激烈，都会让最初那个意外得到一个在联想上一致的解释，凑成一个说得通的故事。
  - 现译：在餐厅尝汤的那个故事里，后来发生的事，无论是另一位客人尝了汤也皱起脸，还是第一位客人被服务员一碰就反应激烈，都会给最初那个意外带来一个在联想上一致的解释，凑成一个说得通的故事。
  - 处理：复核后重写。“令人吃惊的汤的故事”的字连串 复核：“汤让人吃惊的那个故事”仍然拗口；后半句“让……得到一个在联想上一致的解释”也保留了明显的直译痕迹。

- 英文：Experiments have shown that six-month-old infants see the sequence of events as a cause-effect scenario, and they indicate surprise when the sequence is altered.
  - 原译：实验表明，六个月大的婴儿会把这一连串事件看成一个因果情景，事件的顺序被改动时，他们会表现出惊讶。
  - 现译：实验表明，六个月大的婴儿会把这一连串事件看成一个因果情景，如果改动事件的顺序，他们会表现出惊讶。
  - 处理：Astra 复核通过。不必要的被动句“被改动时”

- 英文：In 1944, at about the same time as Michotte published his demonstrations of physical causality, the psychologists Fritz Heider and Mary-Ann Simmel used a method similar to Michotte’s to demonstrate the perception of intentional causality.
  - 原译：1944 年，差不多就在米肖特发表物理因果演示的同一时期，心理学家弗里茨·海德和玛丽-安·西梅尔用一种与米肖特类似的方法，演示了人对意图因果的知觉。
  - 现译：1944 年，差不多就在米肖特发表物理因果演示的同一时期，心理学家弗里茨·海德和玛丽-安·西梅尔用一种与米肖特类似的方法，演示了人对意图因果的知觉。
  - 处理：复核后退回原译。“人对……的知觉”名词化 复核：“演示了人们会知觉到”不如原来的“演示了人对……的知觉”自然。“知觉”在这里作名词准确，没有必要为去名词化而强改成动词。

- 英文：Here again, the evidence is that we are born prepared to make intentional attributions: infants under one year old identify bullies and victims, and expect a pursuer to follow the most direct path in attempting to catch whatever it is chasing.
  - 原译：这里的证据同样表明，我们生来就会作出意图归因：不满一岁的婴儿就能认出欺凌者和受害者，还会预期追赶者在试图抓住它所追的东西时，会走最直接的路线。
  - 现译：这里的证据同样表明，我们生来就倾向于作出意图归因：不满一岁的婴儿就能认出欺凌者和受害者，还会预期追赶者会走最直接的路线去抓它追的东西。
  - 处理：复核后重写。“在试图……时”状语照搬 in attempting to 复核：沿用了原译的程度偏差：born prepared 强调先天的准备或倾向，不等于断言人一出生就已经会作出意图归因。

- 英文：The two modes of causation that we are set to perceive make it natural for us to accept the two central beliefs of many religions: an immaterial divinity is the ultimate cause of the physical world, and immortal souls temporarily control our bodies while we live and leave them behind as we die.
  - 原译：我们天生会感知的这两种因果方式，让我们很自然地接受许多宗教的两个核心信念：非物质的神是物质世界的终极原因；不朽的灵魂在我们活着时暂时掌控我们的身体，在我们死去时离开身体。
  - 现译：我们天生就会感知这两种因果方式，这让我们很容易接受许多宗教的两个核心信念：非物质的神是物质世界的终极原因；不朽的灵魂在我们活着时暂时掌控我们的身体，在我们死去时离开身体。
  - 处理：复核后重写。带长定语的名词短语作主语 复核：“因此很自然地会接受”把接受这些信念显得自然，写成了会实际接受的结果；原文并未断言人们必然接受这些宗教信念。

- 英文：The prominence of causal intuitions is a recurrent theme in this book because people are prone to apply causal thinking inappropriately, to situations that require statistical reasoning.
  - 原译：因果直觉的突出地位是本书反复出现的主题，因为人们容易把因果思维用错地方，用到需要统计推理的情境中。
  - 现译：因果直觉占据着突出的地位，这是本书反复出现的主题，因为人们容易把因果思维用错地方，用到需要统计推理的情境中。
  - 处理：Astra 复核通过。抽象名词“突出地位”作主语

- 英文：She will end up thinking that someone intentionally sabotaged her work.
  - 原译：到头来她会认定，是有人故意破坏了她的工作。
  - 现译：到头来她会认定，是有人存心搞砸了她的工作。
  - 处理：Astra 复核通过。口头话里“破坏了她的工作”生硬

## 第 7 章 急于下结论的机器

- 英文：These are the circumstances in which intuitive errors are probable, which may be prevented by a deliberate intervention of System 2.
  - 原译：在这些情况下，直觉很可能出错，而系统 2 有意的介入或许能避免这些错误。
  - 现译：在这些情况下，直觉很可能出错，而系统 2 如果有意介入，或许能避免这些错误。
  - 处理：Astra 复核通过。抽象名词“有意的介入”作主语

- 英文：In the absence of an explicit context, System 1 generated a likely context on its own.
  - 原译：在没有明确语境的情况下，系统 1 自己生成了一个可能的语境。
  - 现译：没有明确的语境，系统 1 就自己生成了一个可能性较大的语境。
  - 处理：按复核意见修改。“在……的情况下”照搬 in the absence of 复核：沿用了原译对程度的弱化：likely 是可能性较大，不只是 possible 意义上的“可能”。

- 英文：When uncertain, System 1 bets on an answer, and the bets are guided by experience.
  - 原译：拿不准的时候，系统 1 会押一个答案，而押注是由经验指引的。
  - 现译：拿不准的时候，系统 1 会押一个答案，押注凭的是经验。
  - 处理：Astra 复核通过。“是由……指引的”照搬被动

- 英文：Even a nonsensical statement, Gilbert argues, will evoke initial belief.
  - 原译：吉尔伯特认为，即使是毫无意义的陈述，也会引起最初的相信。
  - 现译：吉尔伯特认为，即使是毫无意义的陈述，一开始也会让人相信。
  - 处理：Astra 复核通过。“引起最初的相信”名词化直译

- 英文：The disruption of System 2 had a selective effect: it made it difficult for people to “unbelieve” false sentences.
  - 原译：对系统 2 的干扰产生了一种有选择的影响：它让人们难以“不信”假句子。
  - 现译：系统 2 受到干扰，带来的影响具有选择性：人们变得难以“不信”假句子。
  - 处理：复核后重写。抽象名词作主语，“它让……”照搬 it made 复核：“产生的影响是有选择的”仍然生硬，宜说“具有选择性”；unbelieve 在这里指从起初的相信转为不信，也应表达清楚。

- 英文：Contrary to the rules of philosophers of science, who advise testing hypotheses by trying to refute them, people (and scientists, quite often) seek data that are likely to be compatible with the beliefs they currently hold.
  - 原译：科学哲学家主张通过设法反驳假设来检验它，但人们（科学家也常常如此）违背了这条规则，他们寻找的是很可能与自己目前所持信念相符的数据。
  - 现译：科学哲学家主张，检验假设要设法反驳它；人们（科学家也常常如此）却违背这条规则，去寻找很可能与自己目前所持信念相符的数据。
  - 处理：Astra 复核通过。“通过……来……”介词结构，多余代词“他们”

- 英文：If you are asked about the probability of a tsunami hitting California within the next thirty years, the images that come to your mind are likely to be images of tsunamis, in the manner Gilbert proposed for nonsense statements such as “whitefish eat candy.”
  - 原译：如果有人问你，未来三十年内海啸袭击加利福尼亚的概率有多大，你脑海中浮现的多半是海啸的画面，就像吉尔伯特针对“白鲑吃糖果”这类胡话所提出的那样。
  - 现译：如果有人问你，未来三十年内海啸袭击加利福尼亚的概率有多大，你脑海中浮现的多半是海啸的画面，情形就和吉尔伯特分析“白鲑吃糖果”这类胡话时说的一样。
  - 处理：Astra 复核通过。“就像……针对……所提出的那样”照搬 in the manner

- 英文：This is a pity, because the halo effect is a good name for a common bias that plays a large role in shaping our view of people and situations.
  - 原译：这很可惜，因为有一种常见的偏差在塑造我们对人和情境的看法上起着很大的作用，而光环效应正是它的好名字。
  - 现译：这很可惜，因为光环效应是个很贴切的名称，指的是一种常见的偏差，而这种偏差在很大程度上影响着我们对人和情境的看法。
  - 处理：按复核意见修改。“在……上起着很大的作用”和“正是它的好名字”生硬 复核：“是个好名字”仍是直译，没有清楚表达名称贴切的意思；“对我们怎样看待……影响很大”的搭配也不够顺畅。

- 英文：Real evidence of generosity is missing in the story of Joan, and the gap is filled by a guess that fits one’s emotional response to her.
  - 原译：在琼的故事里，并没有她慷慨的真实证据，这个空缺由一个猜测填补，而这个猜测与人对她的情绪反应相吻合。
  - 现译：在琼的故事里，并没有她慷慨的真实证据，填补这个空缺的，是一个与人对她的情绪反应相吻合的猜测。
  - 处理：Astra 复核通过。被动式“由……填补”，后面又拖一句“而这个猜测”

- 英文：In other situations, evidence accumulates gradually and the interpretation is shaped by the emotion attached to the first impression.
  - 原译：在另一些情境中，证据是逐渐积累起来的，对证据的解释受到第一印象所附带的情绪影响。
  - 现译：在另一些情境中，证据是逐渐积累起来的，人们怎样解释这些证据，受第一印象带着的情绪左右。
  - 处理：Astra 复核通过。“对证据的解释受到……影响”名词化

- 英文：In an enduring classic of psychology, Solomon Asch presented descriptions of two people and asked for comments on their personality.
  - 原译：在心理学一项经久不衰的经典研究中，所罗门·阿希给出了对两个人的描述，请参与者评价他们的性格。
  - 现译：在心理学一项经久不衰的经典研究中，所罗门·阿希描述了两个人，请参与者评价他们的性格。
  - 处理：Astra 复核通过。“给出了对……的描述”名词化

- 英文：The halo effect is also an example of suppressed ambiguity: like the word bank, the adjective stubborn is ambiguous and will be interpreted in a way that makes it coherent with the context.
  - 原译：光环效应也是抑制歧义的一个例子：和 bank 这个词一样，“固执”这个形容词也有歧义，人们会按照与语境一致的方式去解读它。
  - 现译：光环效应也是抑制歧义的一个例子：和 bank 这个词一样，“固执”这个形容词也有歧义，人们会把它解读得与语境一致。
  - 处理：Astra 复核通过。“按照……的方式去……”照搬 in a way that

- 英文：When I was disappointed with a student’s second essay and went to the back page of the booklet to enter a poor grade, I occasionally discovered that I had given a top grade to the same student’s first essay.
  - 原译：当我对某个学生的第二篇论述感到失望，翻到答题册封底去写一个低分时，偶尔会发现，我给同一个学生的第一篇论述打的是最高分。
  - 现译：我对某个学生的第二篇论述感到失望，翻到答题册封底准备记下一个低分时，偶尔会发现，自己给这个学生的第一篇论述打的却是很高的分。
  - 处理：复核后重写。“当……时”照搬 when 复核：删去时间结构后，前面的情境与“偶尔会发现”的关系不够清楚。另外，a top grade 指高分或优等成绩，不必然是“最高分”，这一旧译问题仍需修正。

- 英文：The uncomfortable inconsistency that was revealed when I switched to the new procedure was real: it reflected both the inadequacy of any single question as a measure of what the student knew and the unreliability of my own grading.
  - 原译：换成新流程后暴露出来的那种令人不舒服的不一致，是真实的：它既反映出任何单独一道题都不足以衡量学生掌握了多少知识，也反映出我自己的评分并不可靠。
  - 现译：换成新流程后暴露出来的不一致，虽然让人不舒服，却是真实的：它既反映出任何单独一道题都不足以衡量学生掌握了多少知识，也反映出我自己的评分并不可靠。
  - 处理：Astra 复核通过。名词前定语过长

- 英文：The procedure I adopted to tame the halo effect conforms to a general principle: decorrelate error!
  - 原译：我为驯服光环效应而采用的流程，符合一条普遍的原则：让误差互不相关！
  - 现译：我用来驯服光环效应的这个流程，符合一条普遍的原则：让误差互不相关！
  - 处理：Astra 复核通过。“为……而采用的”书面定语

- 英文：To understand how this principle works, imagine that a large number of observers are shown glass jars containing pennies and are challenged to estimate the number of pennies in each jar.
  - 原译：要理解这条原则如何起作用，请想象一下：许多观察者看着装有 1 美分硬币的玻璃罐，被要求估计每个罐子里有多少枚硬币。
  - 现译：要理解这条原则怎样起作用，请想象一下：给许多观察者看装着 1 美分硬币的玻璃罐，让他们估计每个罐子里有多少枚硬币。
  - 处理：按复核意见修改。不必要的被动句“被要求” 复核：原文只用了玻璃罐的复数，没有限定数量为“几个”；应去掉新增的数量限制。

- 英文：As James Surowiecki explained in his best-selling The Wisdom of Crowds, this is the kind of task in which individuals do very poorly, but pools of individual judgments do remarkably well.
  - 原译：正如詹姆斯·索罗维基在他的畅销书《群体的智慧》中所解释的，在这类任务中，个人表现很差，但把许多人的判断汇集起来，结果却出奇地好。
  - 现译：詹姆斯·索罗维基在畅销书《群体的智慧》中解释过，在这类任务中，个人表现很差，但把许多人的判断汇集起来，结果却出奇地好。
  - 处理：Astra 复核通过。“正如……所解释的”和多余的“他的”

- 英文：The standard practice of open discussion gives too much weight to the opinions of those who speak early and assertively, causing others to line up behind them.
  - 原译：公开讨论的标准做法，会让那些发言早、态度强势的人的意见占太大的分量，导致其他人都跟在他们后面站队。
  - 现译：惯常的做法是大家自由讨论，这样一来，发言早、态度强势的人意见分量过重，其他人也就跟着附和。
  - 处理：复核后重写。“那些……的人的意见”的字连串 复核：standard practice 指惯常采用的讨论方式，不是“按照公开讨论的标准”办事；这里讨论的是这种方式造成的影响。“其他人都”也增加了全体性的限定。

- 英文：When information is scarce, which is a common occurrence, System 1 operates as a machine for jumping to conclusions.
  - 原译：信息稀缺的时候（这种情况很常见），系统 1 就像一台急于下结论的机器那样运作。
  - 现译：信息稀缺的时候（这种情况很常见），系统 1 运作起来就是一台急于下结论的机器。
  - 处理：Astra 复核通过。“就像……那样运作”照搬 operates as

- 英文：You did not start by asking, “What would I need to know before I formed an opinion about the quality of someone’s leadership?”
  - 原译：你没有先问：“在对一个人的领导能力形成看法之前，我需要知道些什么？”
  - 现译：你没有先问：“我得先知道些什么，才能对一个人的领导能力有个看法？”
  - 处理：Astra 复核通过。心里话用了“在……形成看法之前”的书面句式

- 英文：Of course, System 2 also is capable of a more systematic and careful approach to evidence, and of following a list of boxes that must be checked before making a decision
  - 原译：当然，系统 2 也能用一种更系统、更仔细的方式对待证据，在作决定之前按清单逐项核对必须查验的事项。
  - 现译：当然，系统 2 也能更系统、更仔细地对待证据，在作决定之前按清单逐项核对必须查验的事项。
  - 处理：Astra 复核通过。“用一种……的方式”照搬 approach

- 英文：On September 3, plaintiff David Thornton, a forty-three-year-old union field representative, was present in Thrifty Drug Store #168, performing a routine union visit.
  - 原译：9 月 3 日，原告戴维·桑顿，一位四十三岁的工会外勤代表，来到斯里夫蒂药店（Thrifty Drug）第 168 号店，进行一次例行的工会走访。
  - 现译：9 月 3 日，原告戴维·桑顿来到斯里夫蒂药店（Thrifty Drug）第 168 号店，作例行的工会走访。桑顿四十三岁，是工会的外勤代表。
  - 处理：Astra 复核通过。插入同位语照搬英文，“进行一次”虚化动词

- 英文：Naturally, the lawyer for the union organizer described the arrest as an intimidation attempt, while the lawyer for the store argued that having the talk in the store was disruptive and that the manager was acting properly.
  - 原译：很自然，工会组织者的律师把这次逮捕说成一次恐吓企图，而药店的律师则认为，在店里谈话扰乱了营业，经理的做法是恰当的。
  - 现译：很自然，工会组织者的律师把这次逮捕说成是企图恐吓，而药店的律师则认为，在店里谈话扰乱了营业，经理的做法是恰当的。
  - 处理：Astra 复核通过。“一次恐吓企图”名词短语直译

- 英文：It is the consistency of the information that matters for a good story, not its completeness.
  - 原译：对于一个好故事来说，要紧的是信息是否一致，信息完不完整倒无所谓。
  - 现译：对于一个好故事来说，要紧的是信息是否一致，信息完不完整倒无所谓。
  - 处理：复核后退回原译。“对于……来说”照搬 for 复核：上下文谈的是在心中构建连贯解释。“要讲出”增加了讲述的动作，容易把认知过程读成讲故事的方法；原译没有这个歧义，也并不难懂。

- 英文：Let’s decorrelate errors by obtaining separate judgments on the issue before any discussion.
  - 原译：讨论之前，咱们先让每个人就这个问题单独作出判断，让误差互不相关。
  - 现译：讨论之前，咱们先让每个人对这个问题各自下个判断，让误差互不相关。
  - 处理：Astra 复核通过。口头话里用“就……作出判断”这种书面虚化动词

## 第 8 章 判断是怎样产生的

- 英文：There is no limit to the number of questions you can answer, whether they are questions someone else asks or questions you ask yourself. Nor is there a limit to the number of attributes you can evaluate.
  - 原译：你能回答的问题没有数量上的限制，无论是别人问你的，还是你问自己的。你能评估的属性也没有数量上的限制。
  - 现译：你能回答的问题没有上限，不管是别人问你的，还是你自己问自己的。你能评估的属性也没有上限。
  - 处理：Astra 复核通过。“没有数量上的限制”照搬 no limit to the number of

- 英文：It continuously monitors what is going on outside and inside the mind, and continuously generates assessments of various aspects of the situation without specific intention and with little or no effort.
  - 原译：它持续不断地监视着心智内外发生的事，并且在没有特定意图、几乎或完全不费力的情况下，持续不断地对当前情境的各个方面作出评估。
  - 现译：它持续不断地监视着心智内外发生的事，也持续不断地评估当前情境的各个方面，做这些评估不需要特定的意图，只费很少的力气，甚至完全不费力。
  - 处理：复核后重写。“在……的情况下”长状语，加虚化动词“作出评估” 复核：“几乎或完全不费力”仍是生硬的压缩表达，后半句也较拖沓。

- 英文：System 1 has been shaped by evolution to provide a continuous assessment of the main problems that an organism must solve to survive: How are things going? Is there a threat or a major opportunity? Is everything normal? Should I approach or avoid?
  - 原译：系统 1 是由进化塑造的，它持续评估一个生物要生存就必须解决的几个主要问题：情况怎么样？有没有威胁，或者重大的机会？一切都正常吗？我该靠近还是该躲开？
  - 现译：进化塑造了系统 1，让它持续评估一个生物要生存就必须解决的几个主要问题：情况怎么样？有没有威胁，或者重大的机会？一切都正常吗？我该靠近还是该躲开？
  - 处理：Astra 复核通过。照搬被动结构“是由进化塑造的”

- 英文：The questions are perhaps less urgent for a human in a city environment than for a gazelle on the savannah, but we have inherited the neural mechanisms that evolved to provide ongoing assessments of threat level, and they have not been turned off.
  - 原译：对生活在城市环境里的人来说，这些问题也许不像对稀树草原上的瞪羚那么紧迫，但我们继承了为持续评估威胁程度而进化出来的神经机制，这些机制并没有关闭。
  - 现译：这些问题对生活在城市里的人也许不像对稀树草原上的瞪羚那么紧迫，但我们继承了一套神经机制，它们是为了持续评估威胁程度而进化出来的，而且一直没有关掉。
  - 处理：Astra 复核通过。“对……来说”开头，名词前堆长定语

- 英文：This contributes to one’s chances of survival in a dangerous world, and such a specialized capability has indeed evolved. Alex Todorov, my colleague at Princeton, has explored the biological roots of the rapid judgments of how safe it is to interact with a stranger. He showed that we are endowed with an ability to evaluate, in a single glance at a stranger’s face, two potentially crucial facts about that person: how dominant (and therefore potentially threatening) he is, and how trustworthy he is, whether his intentions are more likely to be friendly or hostile.
  - 原译：在一个危险的世界里，这种能力能提高一个人生存的机会，而这样一种专门的能力也确实进化出来了。我在普林斯顿的同事亚历克斯·托多罗夫研究过这样一种快速判断的生物学根源：与一个陌生人打交道有多安全。他的研究表明，我们天生就有一种能力，只要看一眼陌生人的脸，就能评估出关于这个人的两个可能至关重要的事实：他有多强势（因而可能有多大威胁），以及他有多可信，也就是他的意图更可能是友好的还是敌意的。
  - 现译：在危险的世界里，这种能力能增加人活下来的机会，而这样的专门能力也确实进化出来了。我们会很快判断跟一个陌生人打交道有多安全，我在普林斯顿的同事亚历克斯·托多罗夫研究过这种快速判断的生物学根源。他的研究表明，我们天生就有这种本领，只看一眼陌生人的脸，就能评估出有关这个人的两件可能至关重要的事：他有多强势（因而可能有多大威胁），以及他有多可信，也就是他更可能怀有善意还是敌意。
  - 处理：按复核意见修改。多余的“一个”“一种”，冒号补述照搬 judgments of how safe，定语过长 复核：“意图是友好的还是敌意的”搭配不当，尤其“敌意的”不能这样与“友好的”并列。此处应说明陌生人更可能怀有善意还是敌意。

- 英文：The shape of the face provides the cues for assessing dominance: a “strong” square chin is one such cue. Facial expression (smile or frown) provides the cues for assessing the stranger’s intentions.
  - 原译：脸的形状为评估强势程度提供了线索：“刚毅”的方下巴就是这样一条线索。面部表情（微笑还是皱眉）为评估陌生人的意图提供了线索。
  - 现译：评估强势程度的线索来自脸的形状：“刚毅”的方下巴就是其中一条。评估陌生人意图的线索则来自面部表情（微笑还是皱眉）。
  - 处理：Astra 复核通过。“为……提供了线索”照搬 provides the cues for

- 英文：Todorov showed his students pictures of men’s faces, sometimes for as little as one-tenth of a second, and asked them to rate the faces on various attributes, including likability and competence.
  - 原译：托多罗夫给他的学生看一些男性面孔的照片，有时只给他们看十分之一秒，然后请他们按各种属性给这些面孔打分，包括讨人喜欢的程度和能力。
  - 现译：托多罗夫给学生看一些男性面孔的照片，有时只给他们看十分之一秒，然后请他们从讨人喜欢的程度、能力等多个方面给这些面孔打分。
  - 处理：Astra 复核通过。多余的“他的”，句末“包括……”照搬 including 后置补充

- 英文：The faces that Todorov showed were not a random set: they were the campaign portraits of politicians competing for elective office. Todorov then compared the results of the electoral races to the ratings of competence that Princeton students had made, based on brief exposure to photographs and without any political context.
  - 原译：托多罗夫给学生看的面孔并不是随便挑的：它们是竞选公职的政治人物的竞选照片。随后，托多罗夫把选举结果与普林斯顿学生给出的能力评分作了比较，学生们只是短暂地看过照片，也没有任何政治背景信息。
  - 现译：托多罗夫给学生看的面孔并不是随便挑的：那是一些政治人物竞选公职时用的竞选照。随后，托多罗夫把选举结果跟普林斯顿学生给出的能力评分作了比较，学生们只短暂地看过照片就打了分，也没有任何政治背景信息可参考。
  - 处理：复核后重写。“的”字连串，虚化动词“作了比较”，句末补述照搬 based on 分词短语 复核：“匆匆看过”给原文的短暂接触照片增加了仓促观看的意味；“打的能力分”也不如“能力评分”自然、明确。原译更准确顺畅。

- 英文：But studies of the brain’s response to winning and losing candidates show that we are biologically predisposed to reject candidates who lack the attributes we value—in this research, losers evoked stronger indications of (negative) emotional response.
  - 原译：但是，对大脑如何回应胜选和落选候选人的研究表明，我们在生物学上就倾向于拒绝那些缺少我们看重的特质的候选人：在这项研究中，落选者引起的（负面）情绪反应迹象更强。
  - 现译：但是，有研究考察了大脑对胜选和落选候选人的反应，结果表明，如果候选人缺少我们看重的特质，我们天生就倾向于排斥他：在这项研究中，落选者引起的（负面）情绪反应，在大脑中表现得更明显。
  - 处理：复核后重写。主语“对大脑如何回应……的研究”过长，宾语“的”字连串 复核：“在生物学上就倾向于”仍显生硬；“反应迹象更强”搭配不自然，原文说的是显示情绪反应的迹象更明显。

- 英文：Voters are attempting to form an impression of how good a candidate will be in office, and they fall back on a simpler assessment that is made quickly and automatically and is available when System 2 must make its decision.
  - 原译：选民们想形成一个印象，判断一位候选人上任后会干得多好，于是退而依靠一个更简单的评估，这个评估是迅速、自动地作出的，而且在系统 2 必须作出决定时随手可用。
  - 现译：选民们想对一位候选人上任后会干得多好形成印象，于是退而依靠一种更简单的评估：这种评估迅速、自动地完成，等到系统 2 必须作决定时，随手就能拿来用。
  - 处理：复核后重写。照搬 that is made 定语从句，虚化动词“作出” 复核：原文谈的是候选人上任后会有怎样的表现，“能干得多好”偏向能力；“退而依靠一个评估”也仍显生硬。

- 英文：Political scientists followed up on Todorov’s initial research by identifying a category of voters for whom the automatic preferences of System 1 are particularly likely to play a large role.
  - 原译：政治学家沿着托多罗夫最初的研究继续探索，找出了一类选民：对他们来说，系统 1 的自动偏好特别可能起很大的作用。
  - 现译：政治学家沿着托多罗夫最初的研究继续探索，找出了一类选民，系统 1 的自动偏好在他们身上尤其可能起很大的作用。
  - 处理：Astra 复核通过。“对他们来说”照搬 for whom 从句

- 英文：As expected, the effect of facial competence on voting is about three times larger for information-poor and TV-prone voters than for others who are better informed and watch less television. Evidently, the relative importance of System 1 in determining voting choices is not the same for all people.
  - 原译：不出所料，对信息贫乏又爱看电视的选民来说，面孔是否显得能干对投票的影响，大约是那些消息更灵通、电视看得少的选民的三倍。显然，在决定投票选择时，系统 1 的相对重要性并不是对所有人都一样。
  - 现译：不出所料，在信息贫乏又爱看电视的选民身上，面孔是否显得能干对投票的影响，大约是那些消息更灵通、电视看得少的选民的三倍。显然，在决定投票选择时，系统 1 的相对分量并不是人人都一样。
  - 处理：Astra 复核通过。“对……来说”“对所有人都一样”照搬 for ... voters / for all people

- 英文：The list of basic assessments is long, but not every possible attribute is assessed.
  - 原译：基本评估的清单很长，但并不是每一种可能的属性都会被评估。
  - 现译：基本评估的清单很长，但并非每一种可能的属性都在评估之列。
  - 处理：Astra 复核通过。照搬被动句“会被评估”

- 英文：You know that the two towers are equally tall and that they are more similar to each other than the tower on the left is to the array of blocks in the middle.
  - 原译：你知道两座塔一样高，也知道它们彼此之间的相似程度，比左边那座塔与中间那片积木的相似程度更高。
  - 现译：你知道两座塔一样高，也知道两座塔彼此更相像，左边那座塔和中间那片积木就没那么像。
  - 处理：Astra 复核通过。照搬英文比较结构“相似程度比……的相似程度更高”

- 英文：For another example, consider the question: What is the average length of the lines in figure 8?
  - 原译：再举一个例子，请考虑这个问题：图 8 中这些线段的平均长度是多少？
  - 现译：再举一个例子，想一想这个问题：图 8 中这些线段的平均长度是多少？
  - 处理：Astra 复核通过。consider 直译成“请考虑”

- 英文：Furthermore, the accuracy of these judgments is not impaired when the observer is cognitively busy with a memory task.
  - 原译：而且，即使观察者在认知上正忙于一项记忆任务，这些判断的准确性也不会受损。
  - 现译：而且，即使观察者的脑子正忙着做一项记忆任务，这些判断也一样准确。
  - 处理：Astra 复核通过。“在认知上正忙于”直译 cognitively busy，抽象名词“准确性”作主语

- 英文：System 1 does it, automatically and effortlessly, just as it registers the color of the lines and the fact that they are not parallel.
  - 原译：系统 1 就能自动地、毫不费力地做到这一点，就像它感知这些线段的颜色，以及它们并不平行这一事实一样。
  - 现译：系统 1 就能自动地、毫不费力地做到这一点，就像它能感知这些线段的颜色，也能察觉它们并不平行一样。
  - 处理：按复核意见修改。“……这一事实”直译 the fact that 复核：“感知……是什么颜色、彼此并不平行”的并列衔接生硬，两项感知内容的句式不协调。

- 英文：It is in fact an instance of an important limitation of that system.
  - 原译：但这其实是这个系统一个重要局限的例证。
  - 现译：但这其实体现了这个系统的一个重要局限。
  - 处理：Astra 复核通过。“是……的例证”直译 an instance of

- 英文：Participants in one of the numerous experiments that were prompted by the litigation following the disastrous Exxon Valdez oil spill were asked their willingness to pay for nets to cover oil ponds in which migratory birds often drown. Different groups of participants stated their willingness to pay to save 2,000, 20,000, or 200,000 birds.
  - 原译：在其中一项实验里，参与者被问到，他们愿意出多少钱，给那些常有候鸟淹死的油池盖上防护网。不同组的参与者分别说出了为拯救 2,000 只、20,000 只或 200,000 只鸟愿意支付的金额。
  - 现译：其中一项实验问参与者，愿意出多少钱给那些常有候鸟淹死的油池盖上防护网。各组参与者分别说出，为了拯救 2,000 只、20,000 只或 200,000 只鸟，自己愿意出多少钱。
  - 处理：复核后保留改写。被动句“参与者被问到”，“为拯救……愿意支付的金额”定语过长 复核：“实验问参与者”不如原译自然；“分别说出，为了……”又用逗号割裂动词与后面的宾语内容。原译更顺畅。漏油事故及诉讼背景已在正文前一句交代，不属于漏译。

- 英文：What the participants reacted to, in all three groups, was a prototype—the awful image of a helpless bird drowning, its feathers soaked in thick oil.
  - 原译：三个组的参与者作出反应的对象，都是一个原型：一只无助的鸟正在淹死，羽毛浸透了黏稠的原油，那景象惨不忍睹。
  - 现译：让三个组的参与者产生反应的，都是一个原型：一只无助的鸟正在淹死，羽毛浸透了黏稠的原油，那景象惨不忍睹。
  - 处理：Astra 复核通过。“作出反应的对象”照搬 what ... reacted to

- 英文：An underlying scale of intensity allows matching across diverse dimensions.
  - 原译：有了一个潜在的强度量表，就可以在各种不同的维度之间进行匹配。
  - 现译：有了潜在的强度量表，各种维度上的强度就可以相互匹配。
  - 处理：复核后重写。虚化动词“进行匹配”，多余的“一个” 复核：原文说可以跨维度进行匹配，改写却把“维度”本身写成相互匹配的对象，模糊了匹配不同维度上的强度这一含义。原译的关系更准确。

- 英文：And of course you have similar feelings about the intensity of punishments.
  - 原译：当然，对于惩罚的强度，你也有类似的感觉。
  - 现译：当然，你对惩罚的强度也有类似的感觉。
  - 处理：Astra 复核通过。“对于……”前置照搬 about

- 英文：The occasional judgments are voluntary. They occur only when you intend them to do so.
  - 原译：这些偶尔作出的判断是自主的。只有你有意要作出时，它们才会发生。
  - 现译：这些偶尔才有的判断是自主的，只有你有意去判断时，它们才会出现。
  - 处理：复核后重写。“有意要作出时”生硬，照搬 intend them to 复核：“偶尔才作”“有意去作”中的单字“作”用得生硬，后面的“它们才会发生”也仍有直译感。

- 英文：However, the control over intended computations is far from precise: we often compute much more than we want or need.
  - 原译：然而，对于有意进行的计算，我们的控制远远谈不上精确：我们计算的东西，常常比我们想要或需要的多得多。
  - 现译：然而，对于有意进行的计算，我们的控制远远谈不上精确：我们算的东西，常常比自己想要或需要的多得多。
  - 处理：复核后重写。“对于……，我们的控制”抽象名词作主语，多余的“我们” 复核：“控制得远远谈不上精确”杂糅了“控制得不够精确”和“控制远远谈不上精确”两种结构，反而造成语病。原译清楚通顺。

- 英文：An intention to answer one question evoked another, which was not only superfluous but actually detrimental to the main task.
  - 原译：想要回答一个问题的意图，引出了另一个问题，而这个问题不仅多余，实际上还妨碍了主要任务。
  - 现译：本想回答一个问题，却引出了另一个问题，而这个问题不仅多余，实际上还妨碍了主要任务。
  - 处理：Astra 复核通过。抽象名词“……的意图”作主语

- 英文：Here again, the intention to perform one computation evoked another. And here again, the correct answer prevailed in the conflict, but the conflict with the irrelevant answer disrupted performance.
  - 原译：这里也一样，执行一项计算的意图引出了另一项计算。同样，正确答案在冲突中胜出了，但与无关答案的冲突干扰了表现。
  - 现译：这里也一样，本想做一项计算，却引出了另一项计算。同样，正确答案在冲突中胜出了，但跟无关答案的冲突还是干扰了作答。
  - 处理：Astra 复核通过。抽象名词“意图”作主语，“干扰了表现”直译 disrupted performance

- 英文：“Evaluating people as attractive or not is a basic assessment. You do that automatically whether or not you want to, and it influences you.”
  - 原译：判断一个人有没有吸引力，是一种基本评估。不管你愿不愿意，你都会自动这么做，而且它会影响你。
  - 现译：判断一个人有没有吸引力，是一种基本评估。不管你愿不愿意，你都会自动这么做，而且会受它影响。
  - 处理：Astra 复核通过。多余代词“它”作主语，不像口头话

- 英文：“The punishment won’t feel just unless its intensity matches the crime. Just like you can match the loudness of a sound to the brightness of a light.”
  - 原译：惩罚的强度要跟罪行相当，才会让人觉得公正。就像你可以让声音的响度跟灯光的亮度相匹配一样。
  - 现译：惩罚的强度要跟罪行相当，才会让人觉得公正。就像你可以让声音的响度跟灯光的亮度相匹配一样。
  - 处理：复核后退回原译。“就像你可以让……相匹配一样”书面生硬，不像闲谈 复核：把“相当”“相匹配”都改成“对上”，没有使口语更自然，反而让强度对应关系变得含混；“这就跟你能让……对上一样”也比原译拗口。

- 英文：“This was a clear instance of a mental shotgun. He was asked whether he thought the company was financially sound, but he couldn’t forget that he likes their product.”
  - 原译：这是心理霰弹枪的一个明显例子。有人问他觉得这家公司的财务状况是否稳健，他却忘不了自己喜欢他们的产品。
  - 现译：这显然是心理霰弹枪在起作用。人家问他觉得这家公司的财务状况稳不稳健，他却忘不了自己喜欢他们的产品。
  - 处理：Astra 复核通过。“……的一个明显例子”直译 a clear instance of，“是否稳健”书面化

## 第 9 章 回答一个更容易的问题

- 英文：The normal state of your mind is that you have intuitive feelings and opinions about almost everything that comes your way.
  - 原译：你心智的常态是，对遇到的几乎每一件事，你都有直觉的感受和看法。
  - 现译：正常情况下，对遇到的几乎每一件事，你都有直觉的感受和看法。
  - 处理：Astra 复核通过。“你心智的常态是”直译 the normal state of your mind is that

- 英文：Whether you state them or not, you often have answers to questions that you do not completely understand, relying on evidence that you can neither explain nor defend.
  - 原译：不管说不说出口，对于自己并不完全理解的问题，你常常都有答案，而这些答案所依据的证据，你既解释不了，也无法为之辩护。
  - 现译：不管说不说出口，你常常对自己并不完全理解的问题也有答案，而这些答案依据的证据，你既解释不了，也无法为它们辩护。
  - 处理：复核后重写。“对于……”前置，“所依据的”“为之辩护”照搬分词短语 复核：“证据你……辩护不了”搭配不当，“辩护”不能这样直接支配“证据”；应保留为这些证据辩护的关系。

- 英文：I propose a simple account of how we generate intuitive opinions on complex matters.
  - 原译：关于我们怎样对复杂的事情形成直觉看法，我提出一个简单的解释。
  - 现译：我们是怎样对复杂的事情形成直觉看法的？我提出一个简单的解释。
  - 处理：Astra 复核通过。“关于……”长介词短语前置

- 英文：System 1 often makes this move when faced with difficult target questions, if the answer to a related and easier heuristic question comes readily to mind.
  - 原译：面对困难的目标问题时，如果一个相关的、更容易的启发式问题的答案很容易浮现在脑中，系统 1 就常常这样做。
  - 现译：面对困难的目标问题时，如果有一个相关的、更容易的启发式问题，它的答案又很容易浮现在脑中，系统 1 就常常这样做。
  - 处理：Astra 复核通过。“一个相关的、更容易的启发式问题的答案”定语过长

- 英文：Another capability of System 1, intensity matching, is available to solve that problem.
  - 原译：系统 1 的另一种能力，也就是强度匹配，可以解决这个问题。
  - 现译：系统 1 还有一种能力可以解决这个问题，那就是强度匹配。
  - 处理：Astra 复核通过。照搬同位语插入结构

- 英文：As printed on the page, is the figure on the right larger than the figure on the left?
  - 原译：就印在纸面上的样子而言，右边的人像比左边的人像大吗？
  - 现译：单看印在纸面上的样子，右边的人像比左边的人像大吗？
  - 处理：Astra 复核通过。“就……而言”直译 as printed

- 英文：Your impression of their relative size is dominated by a powerful illusion, which neatly illustrates the process of substitution.
  - 原译：你对两者相对大小的印象，被一个强烈的错觉左右了，这个错觉恰好清楚地说明了替代的过程。
  - 现译：一个强烈的错觉左右了你对两者相对大小的印象，这个错觉恰好清楚地说明了替代的过程。
  - 处理：Astra 复核通过。照搬被动句“被……左右了”

- 英文：For the rest of us, substitution occurs: the dominant impression of 3-D size dictates the judgment of 2-D size.
  - 原译：我们其他人身上则会发生替代：占主导地位的三维大小印象，决定了对二维大小的判断。
  - 现译：至于我们其他人，就会发生替代：占主导地位的三维大小印象，决定了我们对二维大小的判断。
  - 处理：Astra 复核通过。“我们其他人身上则会发生”照搬 for the rest of us, substitution occurs

- 英文：You were not confused about the question, but you were influenced by the answer to a question that you were not asked: “How tall are the three people?”
  - 原译：你没有弄错问题，但你受到了另一个问题的答案的影响，而那个问题并没有人问你：“这三个人有多高？”
  - 现译：你没有弄错问题，但另一个问题的答案影响了你。那是个没人问你的问题：“这三个人有多高？”
  - 处理：按复核意见修改。被动“受到了……的影响”加“的”字连串，后补定语从句 复核：引语紧接“它的答案影响了你”之后，容易被误读为在列出答案，实际引述的却是那个未被问到的问题。应调整引语的承接位置。

- 英文：As this example illustrates, a judgment that is based on substitution will inevitably be biased in predictable ways.
  - 原译：正如这个例子所示，基于替代的判断必然会以可以预见的方式出现偏差。
  - 现译：这个例子说明，基于替代的判断必然会出现可以预见的偏差。
  - 处理：Astra 复核通过。“正如……所示”“以……的方式”照搬 as ... illustrates / in ... ways

- 英文：Evidently, dating was not what came first to the students’ minds when they were asked to assess their happiness.
  - 原译：显然，学生们被要求评估自己的幸福程度时，最先想到的并不是约会。
  - 现译：显然，请学生们评估自己有多幸福时，他们最先想到的并不是约会。
  - 处理：Astra 复核通过。照搬被动句“被要求”

- 英文：In this sequence, the correlation between the number of dates and reported happiness was about as high as correlations between psychological measures can get.
  - 原译：按这个顺序提问，约会次数和自述幸福程度之间的相关，几乎达到了心理测量指标之间的相关所能达到的最高水平。
  - 现译：按这个顺序提问，约会次数和自述幸福程度之间的相关很高，心理测量指标之间的相关差不多也就只能高到这个程度。
  - 处理：Astra 复核通过。“……所能达到的最高水平”长定语，照搬 as high as ... can get

- 英文：Dating was apparently not the center of these students’ life (in the first survey, happiness and dating were uncorrelated), but when they were asked to think about their romantic life, they certainly had an emotional reaction.
  - 原译：看来约会并不是这些学生生活的中心（在第一次调查中，幸福和约会并不相关），但被要求想一想自己的感情生活时，他们肯定产生了情绪反应。
  - 现译：看来约会并不是这些学生生活的中心（在第一次调查中，幸福和约会并不相关），但请他们想一想自己的感情生活时，他们肯定产生了情绪反应。
  - 处理：Astra 复核通过。照搬被动句“被要求”

- 英文：They substituted the question to which they had a readymade answer for the question they were asked.
  - 原译：他们用一个自己已有现成答案的问题，替代了别人问他们的那个问题。
  - 现译：他们手头已经有一个问题的现成答案，就用这个问题替代了别人问他们的那个问题。
  - 处理：Astra 复核通过。“一个自己已有现成答案的问题”照搬 to which 定语从句

- 英文：Your beliefs, and even your emotional attitude, may change (at least a little) when you learn that the risk of an activity you disliked is smaller than you thought. However, the information about lower risks will also change your view of the benefits (for the better) even if nothing was said about benefits in the information you received.
  - 原译：当你得知一项你不喜欢的活动风险比你以为的小时，你的信念，甚至你的情感态度，都可能改变（哪怕只是稍微改变）。不过，关于风险较低的信息，也会改变你对好处的看法（往好的方向改变），即使你得到的信息里根本没有提到好处。
  - 现译：一旦得知自己不喜欢的某项活动风险比原先以为的小，你的信念，甚至你的情感态度，都可能改变（哪怕只是稍微改变）。不过，得知风险较低，也会改变你对好处的看法（往好的方向改变），即使你得到的信息里根本没有提到好处。
  - 处理：Astra 复核通过。“当……时”包着长从句，“关于风险较低的信息”抽象名词作主语

- 英文：An active, coherence-seeking System 1 suggests solutions to an undemanding System 2.
  - 原译：一个活跃的、追求连贯的系统 1，向一个不怎么挑剔的系统 2 提出解决办法。
  - 现译：活跃而追求连贯的系统 1，向不怎么挑剔的系统 2 提出解决办法。
  - 处理：按复核意见修改。照搬两个不定冠词“一个……的” 复核：删掉两个“一个”合理，但“把解决办法提给……”搭配生硬，宜保留“向……提出解决办法”的结构。

- 英文：“The question we face is whether this candidate can succeed. The question we seem to answer is whether she interviews well. Let’s not substitute.”
  - 原译：我们要面对的问题是，这位候选人能不能成功。可我们回答的问题，好像是她面试表现好不好。咱们别把问题换掉。
  - 现译：我们面对的问题是这位候选人能不能成功，可我们回答的好像是她面试表现好不好。咱们别把问题换掉。
  - 处理：Astra 复核通过。照搬英文两句平行的 The question ... is 句式，口语不顺

- 英文：“He likes the project, so he thinks its costs are low and its benefits are high. Nice example of the affect heuristic.”
  - 原译：他喜欢这个项目，所以觉得它成本低、收益高。这是情感启发式的一个好例子。
  - 现译：他喜欢这个项目，所以觉得它成本低、收益高。这是情感启发式的一个好例子。
  - 处理：复核后退回原译。“……的一个好例子”直译 nice example of 复核：原文称这是情感启发式的一个“好例子”，改写却增加了“典型”的判定，也改变了评价例子的语气。原译本就自然，没有必要这样改。

- 英文：“We are using last year’s performance as a heuristic to predict the value of the firm several years from now. Is this heuristic good enough? What other information do we need?”
  - 原译：我们在用去年的业绩作启发式，来预测这家公司几年后的价值。这个启发式够好吗？我们还需要哪些其他信息？
  - 现译：我们拿去年的业绩当启发式，来预测这家公司几年后的价值。这个启发式够不够好？我们还需要哪些别的信息？
  - 处理：Astra 复核通过。“够好吗”“其他信息”直译，不像同事间商量的口气

- 英文：Each of the active sentences replaces a statement, technically more accurate but harder to understand, to the effect that a mental event occurs automatically and fast. My hope is that the list of traits will help you develop an intuitive sense of the “personality” of the fictitious System 1. As happens with other characters you know, you will have hunches about what System 1 would do under different circumstances, and most of your hunches will be correct.
  - 原译：表中每一个主动句，都代替了一个在专业上更准确、但更难理解的陈述，大意是某个心理事件自动而迅速地发生。我希望这份特质清单能帮助你对虚构的系统 1 的“个性”形成一种直觉。就像对你认识的其他角色一样，对于系统 1 在不同情况下会怎么做，你会有一些预感，而且你的大多数预感都会是对的。
  - 现译：表中每个主动句，都代替了另一种说法，大意是某个心理事件自动而迅速地发生；那种说法在专业上更准确，但更难理解。我希望这份特质清单能帮你凭直觉把握虚构的系统 1 有什么样的“个性”。就像你能大致猜到自己认识的其他角色会怎么做一样，对于系统 1 在不同情况下会怎么做，你也会有一些预感，而且大多数预感都会是对的。
  - 处理：复核后重写。名词前长定语，“的”字连串，“对于……”前置 复核：“对认识的其他角色会有预感”搭配不完整，预感的对象应是角色会怎么做，而不是角色本身；应把这一关系说清楚。

- 英文：creates a coherent pattern of activated ideas in associative memory
  - 原译：在联想记忆中形成由被激活的观念组成的连贯模式
  - 现译：在联想记忆中把被激活的观念组织成连贯的模式
  - 处理：按复核意见修改。“由……组成的”长定语 复核：“把被激活的观念组成连贯的模式”搭配生硬，此处用“组织成”才能自然表达将观念组织为连贯模式的意思。

## 第 10 章 小数定律

- 英文：A study of the incidence of kidney cancer in the 3,141 counties of the United States reveals a remarkable pattern.
  - 原译：一项针对美国 3,141 个县肾癌发病率的研究，揭示了一个引人注目的规律。
  - 现译：有一项研究调查了美国 3,141 个县的肾癌发病率，发现了一个引人注目的规律。
  - 处理：Astra 复核通过。“一项针对……的研究，揭示了”长定语主语加主谓间逗号

- 英文：You probably rejected the idea that Republican politics provide protection against kidney cancer.
  - 原译：你大概否定了共和党的政治主张能预防肾癌这个想法。
  - 现译：你大概否定了这个想法：共和党的政治主张能预防肾癌。
  - 处理：Astra 复核通过。整个从句堆在“这个想法”前作定语

- 英文：Very likely, you ended up focusing on the fact that the counties with low incidence of cancer are mostly rural.
  - 原译：很可能，你最后把注意力放在了这样一个事实上：癌症发病率低的县大多在农村。
  - 现译：你最后很可能把注意力放在了这个事实上：癌症发病率低的县大多在农村。
  - 处理：Astra 复核通过。照搬 Very likely 的句首状语位置

- 英文：“It is both easy and tempting to infer that their low cancer rates are directly due to the clean living of the rural lifestyle—no air pollution, no water pollution, access to fresh food without additives.”
  - 原译：“人们很容易推断，也很想推断，这些县癌症发病率低，直接得益于农村生活方式的干净健康：没有空气污染，没有水污染，能吃到不含添加剂的新鲜食物。”
  - 现译：“人们很容易推断，也很想推断，这些县癌症发病率低，直接得益于农村干净健康的生活方式：没有空气污染，没有水污染，能吃到不含添加剂的新鲜食物。”
  - 处理：Astra 复核通过。“生活方式的干净健康”照搬 of 结构

- 英文：The feature “sparsely populated” did not immediately stand out as relevant when you read the epidemiological story.
  - 原译：- 读到那个流行病学故事时，“人口稀少”这个特征并没有立刻作为相关因素引起你的注意。
  - 现译：- 读到那个流行病学故事时，你没有立刻注意到“人口稀少”这个特征与此有关。
  - 处理：Astra 复核通过。“作为相关因素引起你的注意”硬译 stand out as relevant

- 英文：The first statement has a clear ring of truth, but until the second version makes intuitive sense, you have not truly understood the first.
  - 原译：第一个说法听上去显然是对的，但在第二个说法让你凭直觉就觉得有道理之前，你并没有真正理解第一个说法。
  - 现译：第一个说法听上去显然是对的；可是，要等到第二个说法也让你凭直觉就觉得有道理，你才算真正理解了第一个说法。
  - 处理：Astra 复核通过。“在……之前”套住长从句，照搬 until 结构

- 英文：My collaboration with Amos in the early 1970s began with a discussion of the claim that people who have had no training in statistics are good “intuitive statisticians.”
  - 原译：20 世纪 70 年代初，我和阿莫斯的合作，始于讨论这样一种说法：没有受过统计学训练的人，也是优秀的“直觉统计学家”。
  - 现译：20 世纪 70 年代初，我和阿莫斯的合作是从讨论这样一种说法开始的：没有受过统计学训练的人，也是优秀的“直觉统计学家”。
  - 处理：Astra 复核通过。“合作，始于”书面腔，照搬 began with

- 英文：The risk of error can be estimated for any given sample size by a fairly simple procedure.
  - 原译：对于任何给定的样本量，出错的风险都可以用一个相当简单的程序估算出来。
  - 现译：无论样本量是多少，都可以用一个相当简单的程序估算出错的风险。
  - 处理：Astra 复核通过。“对于任何给定的”直译 for any given

- 英文：An article I had read shortly before the debate with Amos demonstrated the mistake that researchers made (they still do) by a dramatic observation.
  - 原译：在和阿莫斯辩论前不久，我读过一篇文章，它用一个惊人的观察说明了研究者所犯的错误（他们现在仍然在犯）。
  - 现译：在和阿莫斯辩论前不久，我读过一篇文章，这篇文章用一个惊人的观察结果，说明了研究者犯的错误（他们现在仍然在犯）。
  - 处理：Astra 复核通过。代词“它”指文章、“所犯的”生硬

- 英文：A plausible explanation was that psychologists’ decisions about sample size reflected prevalent intuitive misconceptions of the extent of sampling variation.
  - 原译：一个说得通的解释是，心理学家在样本量上的决定，反映了人们在抽样变异的幅度上普遍存在的直觉误解。
  - 现译：一个说得通的解释是：人们对抽样变异的幅度普遍存在直觉上的误解，心理学家对样本量的选择正反映了这些误解。
  - 处理：按复核意见修改。抽象名词作主语，两个“在……上”加长定语 复核：原文说心理学家对样本量作出的选择反映了误解，不是决定样本量的“方式”反映了误解；改写转移了所指。

- 英文：My mistake was particularly embarrassing because I taught statistics and knew how to compute the sample size that would reduce the risk of failure to an acceptable level.
  - 原译：我的错误尤其让人难堪，因为我教统计学，知道怎样计算出能把失败风险降到可接受水平的样本量。
  - 现译：我的错误尤其让人难堪，因为我教统计学，知道怎样算出一个样本量，把失败的风险降到可以接受的水平。
  - 处理：Astra 复核通过。定语从句整个前置到“样本量”前

- 英文：Amos and I set out to examine whether I was the only fool or a member of a majority of fools, by testing whether researchers selected for mathematical expertise would make similar mistakes.
  - 原译：我们的办法是检验那些因精通数学而被选中的研究者，会不会犯类似的错误。
  - 现译：我们的办法是专门挑一些精通数学的研究者，看他们会不会犯类似的错误。
  - 处理：Astra 复核通过。“因……而被选中的”被动长定语

- 英文：Amos collected the responses of a group of sophisticated participants (including authors of two statistical textbooks) at a meeting of the Society of Mathematical Psychology.
  - 原译：阿莫斯在数学心理学会的一次会议上，收集了一组资深参与者（其中包括两本统计学教科书的作者）的回答。
  - 现译：阿莫斯在数学心理学会的一次会议上，请一组资深的参与者（其中包括两本统计学教科书的作者）回答了问卷。
  - 处理：复核后保留改写。括号夹在长定语中间，“……的回答”拖尾 复核：原文明确说阿莫斯收集了回答；“请……回答了问卷”改成了组织作答，没有保留收集回答这一动作。原译准确。

- 英文：The omitted details of the poll, that it was done on the phone with a sample of 300, are of no interest in themselves; they provide background information that attracts little attention.
  - 原译：被省略的调查细节，即调查是通过电话进行的、样本是 300 人，本身并没有什么意思；它们提供的是背景信息，很少引起注意。
  - 现译：省略掉的那些调查细节，也就是调查是打电话做的、样本有 300 人，本身并没有什么意思；它们提供的是背景信息，很少引起注意。
  - 处理：Astra 复核通过。“被省略的”“即”“通过电话进行”书面直译

- 英文：When the reliability is obviously low, however, the message will be discredited.
  - 原译：不过，当可靠性明显很低时，这条消息就不会被采信。
  - 现译：不过，如果可靠性明显很低，你就不会相信这条消息了。
  - 处理：复核后重写。“当……时”加“被”字句 复核：原文描述人们会不再相信这条消息；“不足为信”变成了对消息是否值得相信的评价。“不会被采信”更准确，中文也自然。

- 英文：You can see why assuming causality could have had evolutionary advantages.
  - 原译：你可以看出，为什么假定存在因果关系可能曾经带来进化上的优势。
  - 现译：不难看出，假定存在因果关系为什么可能在进化上带来过优势。
  - 处理：Astra 复核通过。“你可以看出，为什么”照搬 You can see why

- 英文：We are automatically on the lookout for the possibility that the environment has changed.
  - 原译：我们会自动留意环境可能已经发生变化。
  - 现译：我们会自动留意环境是不是已经起了变化。
  - 处理：Astra 复核通过。“留意……可能已经发生变化”搭配不通

- 英文：I soon had an occasion to apply what I had learned from Feller.
  - 原译：不久，我就有了一个机会，运用从费勒那里学到的东西。
  - 现译：不久，我就有机会用上了从费勒那里学到的东西。
  - 处理：Astra 复核通过。“有了一个机会，运用”照搬 had an occasion to

- 英文：My advice was that the command should accept that the different outcomes were due to blind luck, and that the interviewing of the pilots should stop.
  - 原译：我的建议是，指挥部应当接受这样的看法：不同的结果纯属运气，对飞行员的问话应该停止。
  - 现译：我的建议是：指挥部应当承认，两个中队结果不同纯属运气，并且不要再找飞行员问话了。
  - 处理：Astra 复核通过。“对飞行员的问话应该停止”名词化加无主语

- 英文：I reasoned that luck was the most likely answer, that a random search for a nonobvious cause was hopeless, and that in the meantime the pilots in the squadron that had sustained losses did not need the extra burden of being made to feel that they and their dead friends were at fault.
  - 原译：我的理由是：运气是最可能的答案；漫无目的地寻找一个不明显的原因，不会有结果；而且与此同时，没有必要再让那个蒙受损失的中队的飞行员背上额外的负担，觉得损失是自己和阵亡战友的过错。
  - 现译：我的理由是：运气是最可能的答案；漫无目的地寻找一个不明显的原因，不会有结果；而且，那个中队已经蒙受了损失，这时候没有必要再让中队的飞行员背上额外的负担，觉得过错在自己和阵亡的战友身上。
  - 处理：Astra 复核通过。“与此同时”硬译，“那个蒙受损失的中队的飞行员”的字连串

- 英文：The “fact” that players occasionally acquire a hot hand is generally accepted by players, coaches, and fans.
  - 原译：球员偶尔会有一双“热手”（hot hand），这个“事实”被球员、教练和球迷普遍接受。
  - 现译：球员、教练和球迷普遍接受这样一个“事实”：球员偶尔会进入“热手”（hot hand）状态。
  - 处理：复核后重写。不必要的“被”字句 复核：仍保留了原译“一双热手”的生硬直译。hot hand 指手感状态，不是身体上的一双手。

- 英文：Players on both teams adapt to this judgment—teammates are more likely to pass to the hot scorer and the defense is more likely to doubleteam.
  - 原译：两队的球员都会根据这个判断调整打法：队友更愿意把球传给这位手热的得分手，防守方则更可能对他进行包夹。
  - 现译：两队的球员都会根据这个判断调整打法：队友更可能把球传给这位手热的得分手，防守方则更可能包夹他。
  - 处理：按复核意见修改。“对他进行包夹”虚化动词“进行” 复核：仍将 more likely 译成“更愿意”，把行为发生的可能性换成了主观意愿。

- 英文：Analysis of thousands of sequences of shots led to a disappointing conclusion: there is no such thing as a hot hand in professional basketball, either in shooting from the field or scoring from the foul line.
  - 原译：对成千上万组投篮序列的分析，得出了一个令人失望的结论：在职业篮球中，无论是运动战投篮还是罚球，都不存在热手这回事。
  - 现译：研究者分析了成千上万组投篮序列，得出了一个令人失望的结论：在职业篮球中，无论是运动战投篮还是罚球，都不存在热手这回事。
  - 处理：Astra 复核通过。“对……的分析”抽象名词作主语

- 英文：The hot hand is entirely in the eye of the beholders, who are consistently too quick to perceive order and causality in randomness.
  - 原译：热手完全存在于旁观者的眼中，而旁观者总是太快地在随机中看出秩序和因果。
  - 现译：热手完全存在于旁观者的眼中，而旁观者总是太轻易地从随机现象中看出秩序和因果。
  - 处理：复核后重写。“太快地”照搬英文副词 复核：“总是太快就在随机中看出”搭配生硬；仅删除“地”没有解决问题。“随机”也宜落实为“随机现象”。

- 英文：The finding was picked up by the press because of its surprising conclusion, and the general response was disbelief.
  - 原译：由于结论出人意料，这项发现被媒体报道了，而普遍的反应是不相信。
  - 现译：因为结论出人意料，媒体报道了这项发现，而大家普遍的反应是不相信。
  - 处理：Astra 复核通过。“被媒体报道了”被动句

- 英文：Thanks to recent advances in cognitive psychology, we can now see clearly what Amos and I could only glimpse: the law of small numbers is part of two larger stories about the workings of the mind.
  - 原译：得益于认知心理学近年来的进展，当年阿莫斯和我只能隐约看到的东西，我们现在可以看得很清楚了：小数定律是关于心智如何运作的两个更大的故事的一部分。
  - 现译：得益于认知心理学近年来的进展，当年阿莫斯和我只能隐约看到的东西，我们现在可以看得很清楚了：小数定律属于两个更大的故事，它们讲的都是心智如何运作。
  - 处理：Astra 复核通过。“关于……的两个更大的故事的一部分”的字连串

- 英文：“I plan to keep the results of the experiment secret until we have a sufficiently large sample. Otherwise we will face pressure to reach a conclusion prematurely.”
  - 原译：> “在样本足够大之前，我打算对实验结果保密。不然的话，我们就会面临过早下结论的压力。”
  - 现译：> “样本够大之前，我打算对实验结果保密。不然的话，我们就会面临过早下结论的压力。”
  - 处理：复核后重写。“面临……的压力”书面腔，不像口头话 复核：“面临……的压力”是自然的中文，也适用于谈话。“有压力逼着我们”反而搭配生硬，“逼着”还加重了受迫意味，未比原译更好。

## 第 11 章 锚

- 英文：The spin of a wheel of fortune—even one that is not rigged—cannot possibly yield useful information about anything, and the participants in our experiment should simply have ignored it.
  - 原译：转一次幸运轮盘，哪怕是没做过手脚的轮盘，也不可能提供关于任何事情的有用信息，参加实验的人本该完全不去理会它。
  - 现译：转一次幸运轮盘，哪怕是没做过手脚的轮盘，也不可能在任何事情上提供有用的信息，参加实验的人本该完全不去理会它。
  - 处理：Astra 复核通过。“关于任何事情的有用信息”照搬 information about

- 英文：We were not the first to observe the effects of anchors, but our experiment was the first demonstration of its absurdity: people’s judgments were influenced by an obviously uninformative number.
  - 原译：我们并不是最早观察到锚的效应的人，但我们的实验第一次展示了这种效应有多荒谬：人们的判断受到了一个显然不含任何信息的数字的影响。
  - 现译：我们并不是最早观察到锚的效应的人，但我们的实验第一次展示了这种效应有多荒谬：一个显然不含任何信息的数字，影响了人们的判断。
  - 处理：Astra 复核通过。“受到了……的数字的影响”被动加长定语

- 英文：Decades after our disagreement, and years after Amos’s death, convincing evidence of such a process was offered independently by two psychologists who had worked closely with Amos early in their careers:
  - 原译：在我们产生分歧几十年之后，也是在阿莫斯去世多年之后，两位在职业生涯早期与阿莫斯密切合作过的心理学家，各自独立地为这样一个过程提供了令人信服的证据。
  - 现译：我们产生分歧几十年之后，也是阿莫斯去世多年之后，有两位心理学家各自独立地为这样一个过程提供了令人信服的证据，他们在职业生涯早期都曾与阿莫斯密切合作。
  - 处理：Astra 复核通过。主语前堆了一长串定语

- 英文：Insufficient adjustment is also a source of tension between exasperated parents and teenagers who enjoy loud music in their room.
  - 原译：调整不足也是恼火的父母与喜欢在房间里大声放音乐的青少年关系紧张的一个原因。
  - 现译：有些青少年喜欢在房间里大声放音乐，惹得父母很恼火，双方关系紧张，调整不足也是一个原因。
  - 处理：Astra 复核通过。“……关系紧张的一个原因”超长前置定语

- 英文：So we now know that Amos was right for at least some cases of anchoring, which involve a deliberate System 2 adjustment in a specified direction from an anchor.
  - 原译：所以我们现在知道，至少对某些锚定情形来说，阿莫斯是对的：在这些情形中，系统 2 从锚出发，朝一个确定的方向有意地进行调整。
  - 现译：所以我们现在知道，至少对某些锚定情形来说，阿莫斯是对的：在这些情形中，系统 2 从锚出发，有意地朝一个确定的方向调整。
  - 处理：Astra 复核通过。虚化动词“进行调整”

- 英文：This is the word we use when someone causes us to see, hear, or feel something by merely bringing it to mind.
  - 原译：别人仅仅通过让我们想到某样东西，就使我们看到、听到或感觉到它，这时我们就用“暗示”这个词。
  - 现译：如果有人只是让我们想到某样东西，就使我们看到、听到或感觉到了它，我们就把这叫作“暗示”。
  - 处理：Astra 复核通过。“仅仅通过……就使”照搬 by merely 结构

- 英文：I had to agree that he was right, but I never became enthusiastic about the idea of insufficient adjustment as the sole cause of anchoring effects.
  - 原译：他说得对，我也不得不承认，但对于把调整不足当作锚定效应唯一原因的观点，我始终提不起热情。
  - 现译：他说得对，我也不得不承认；但要说调整不足是锚定效应的唯一原因，我对这个观点始终提不起热情。
  - 处理：Astra 复核通过。“对于……的观点”长定语

- 英文：We conducted many inconclusive experiments in an effort to understand anchoring, but we failed and eventually gave up the idea of writing more about it.
  - 原译：我们没能成功，最后放弃了就这个问题再写些什么的打算。
  - 现译：我们没能成功，最后打消了就这个问题再写点什么的念头。
  - 处理：Astra 复核通过。“放弃了……的打算”定语过长、搭配生硬

- 英文：You did not believe for a moment that Gandhi lived for 144 years, but your associative machinery surely generated an impression of a very ancient person.
  - 原译：你一刻也没有相信过甘地活了 144 岁，但你的联想机制肯定生成了一个极其年迈的老人的印象。
  - 现译：你一刻也没有相信过甘地活了 144 岁，但你的联想机制肯定让你形成了这样的印象：甘地是一位极其年迈的老人。
  - 处理：按复核意见修改。“老人的印象”照搬 of，还有歧义 复核：“生成了一个印象，让你想到……”仍然生硬，并把印象的具体内容改成了印象随后引发的联想。原文只说形成了一个极其年迈者的印象。

- 英文：They were developed, much later, by other people.
  - 原译：它们是很久以后由别人发展出来的。
  - 现译：很久以后，别人才发展出这些技术和观点。
  - 处理：Astra 复核通过。“由别人发展出来”被动结构

- 英文：The German psychologists Thomas Mussweiler and Fritz Strack offered the most compelling demonstrations of the role of associative coherence in anchoring.
  - 原译：对联想一致性在锚定中的作用，德国心理学家托马斯·穆斯魏勒和弗里茨·斯特拉克给出了最有说服力的演示。
  - 现译：关于联想一致性在锚定中的作用，最有说服力的演示来自德国心理学家托马斯·穆斯魏勒和弗里茨·斯特拉克。
  - 处理：复核后重写。“对……的作用……给出了演示”名词化 复核：前半句提出“起什么作用”，后半句却直接接“演示最有说服力”，话题衔接生硬。宜直接说明谁展示了什么。

- 英文：Although I did not know how to prove it at the time, my hunch about the link between anchoring and suggestion turned out to be correct.
  - 原译：尽管当时我不知道该怎么证明，但我对锚定与暗示之间联系的猜想，后来证明是对的。
  - 现译：我曾猜想锚定与暗示之间有联系，尽管当时我不知道该怎么证明，但这个猜想后来证明是对的。
  - 处理：Astra 复核通过。“我对……联系的猜想”抽象名词作主语

- 英文：Some visitors at the San Francisco Exploratorium were asked the following two questions:
  - 原译：旧金山探索馆的一些参观者被问了下面两个问题：
  - 现译：研究者问了旧金山探索馆的一些参观者下面两个问题：
  - 处理：Astra 复核通过。“被问了”被动句

- 英文：For other participants, the first question referred to a “low anchor” of 180 feet.
  - 原译：对另一些参与者，第一个问题提到的是一个 180 英尺的“低锚”。
  - 现译：问另一些参与者时，第一个问题提到的是 180 英尺的“低锚”。
  - 处理：Astra 复核通过。“对另一些参与者”照搬 For，多余的“一个”

- 英文：When we used a wheel of fortune to anchor estimates of the proportion of African nations in the UN, the anchoring index was 44%, well within the range of effects observed with anchors that could plausibly be taken as hints.
  - 原译：我们用幸运轮盘为联合国中非洲国家所占比例的估计设下锚时，锚定指数是 44%，完全落在那些可以合理地当作提示的锚所产生的效应范围之内。
  - 现译：我们用幸运轮盘来锚定人们对联合国中非洲国家所占比例的估计时，锚定指数是 44%。有些锚可以合理地当作提示，这个数值完全落在使用这类锚时观察到的效应范围之内。
  - 处理：复核后重写。“那些……的锚所产生的效应范围”超长定语 复核：沿用了原译对 observed 的省略。原文比较的是使用这类锚时实际观察到的效应范围，应保留这一实测限定。

- 英文：The participants who have been exposed to random or absurd anchors (such as Gandhi’s death at age 144) confidently deny that this obviously useless information could have influenced their estimate, and they are wrong.
  - 原译：接触过随机的或荒谬的锚（比如甘地 144 岁去世）的参与者，会信心十足地否认这种明显无用的信息影响过自己的估计，而他们错了。
  - 现译：参与者接触过随机的或荒谬的锚（比如甘地 144 岁去世）之后，会信心十足地断言，这种明显无用的信息不可能影响到自己的估计，但他们错了。
  - 处理：复核后重写。主语前的定语从句太长 复核：仍漏掉了 could have 的可能性情态。参与者否认的是这种信息有可能影响自己的估计，不只是说它实际上没有影响。

- 英文：When you read a story about the heroic rescue of a wounded mountain climber, its effect on your associative memory is much the same if it is a news report or the synopsis of a film.
  - 原译：当你读到一个英勇营救受伤登山者的故事时，无论它是一篇新闻报道还是一部电影的剧情梗概，它对你联想记忆的影响都差不多。
  - 现译：读到一个英勇营救受伤登山者的故事时，不管那是一篇新闻报道还是一部电影的剧情梗概，它对你联想记忆的影响都差不多。
  - 处理：Astra 复核通过。“当你……时”加重复的代词“它”

- 英文：If the content of a screen saver on an irrelevant computer can affect your willingness to help strangers without your being aware of it, how free are you?
  - 原译：如果一台与任务无关的电脑上的屏保内容，就能在你毫无察觉的情况下影响你帮助陌生人的意愿，那你还有多少自由？
  - 现译：如果一台不相干的电脑上显示的屏保，就能在你毫无察觉的情况下影响你帮助陌生人的意愿，那你还有多少自由？
  - 处理：复核后重写。“……电脑上的屏保内容”的字连串作主语 复核：“如果……显示什么屏保，就能……”把疑问式表达嵌进条件句，句法不顺。原文的主语是屏保内容，原译虽有较长定语，但表达清楚。

- 英文：We shouldn’t let that number influence our thinking. Set it aside.
  - 原译：我们不能让那个数字影响我们的思考。先把它放到一边。
  - 现译：咱们别让那个数字影响思路。先把它放一边。
  - 处理：Astra 复核通过。“影响我们的思考”书面腔，不像会议上说的话

## 第 12 章 可得性的科学

- 英文：We were the guests of the Oregon Research Institute, which housed several future stars of all the fields in which we worked—judgment, decision making, and intuitive prediction.
  - 原译：我们是俄勒冈研究所的客人，那里聚集了好几位后来成为明星的学者，我们研究的判断、决策和直觉预测这几个领域都有。
  - 现译：我们在俄勒冈研究所做客，那里聚集了好几位后来成为明星的学者，我们研究的判断、决策和直觉预测这几个领域都有。
  - 处理：Astra 复核通过。“是……的客人”照搬 were the guests of

- 英文：Paul was on his way to becoming the leading psychologist among scholars of risk, a position he has held for decades, collecting many honors along the way.
  - 原译：保罗当时正逐步成为风险研究领域首屈一指的心理学家，几十年来他一直保持着这个地位，一路上获得了许多荣誉。
  - 现译：保罗当时正逐步成为风险研究领域首屈一指的心理学家，几十年来一直保持着这个地位，其间获得了许多荣誉。
  - 处理：Astra 复核通过。along the way 直译成“一路上”，代词多余

- 英文：We thought of that heuristic when we asked ourselves what people actually do when they wish to estimate the frequency of a category, such as “people who divorce after the age of 60” or “dangerous plants.” The answer was straightforward: instances of the class will be retrieved from memory, and if retrieval is easy and fluent, the category will be judged to be large.
  - 原译：我们是在问自己下面这个问题时想到这种启发式的：人们想估计某个类别的频率时，比如“60 岁以后离婚的人”或者“危险的植物”，他们实际上在做什么？答案很简单：人们会从记忆中提取这个类别的例子，如果提取起来容易又流畅，这个类别就会被判断为很大。
  - 现译：我们是在问自己下面这个问题时想到这种启发式的：人们想估计某一类人或事物有多常见时，比如“60 岁以后离婚的人”或者“危险的植物”，实际上在做什么？答案很简单：人们会从记忆中提取这个类别的例子，如果提取起来容易又流畅，就会认为这一类人或事物很多。
  - 处理：按复核意见修改。代词重复，被动句“被判断为” 复核：“类别的频率”“类别很大”仍然生硬，后者容易被理解为类别涵盖的范围广；这里指这一类人或事物的常见程度和数量。

- 英文：The statement seemed clear when we formulated it, but the concept of availability has been refined since then.
  - 原译：我们提出这个表述的时候，它看起来很清楚，但从那以后，可得性这个概念已经得到了进一步的完善。
  - 现译：我们刚提出这个表述时，觉得它很清楚，不过从那以后，可得性这个概念又经过了进一步完善。
  - 处理：Astra 复核通过。“得到了……的完善”虚化动词，多余代词

- 英文：you wish to estimate the size of a category or the frequency of an event, but you report an impression of the ease with which instances come to mind. Substitution of questions inevitably produces systematic errors.
  - 原译：和其他判断启发式一样，可得性启发式也是用一个问题替代另一个问题：你想估计的是一个类别的大小或一个事件的频率，报告的却是例子想起来有多容易的印象。问题的替代不可避免地会产生系统性错误。
  - 现译：和其他判断启发式一样，可得性启发式也是用一个问题替代另一个问题：你想估计的是某一类事物有多少，或者某种事件有多频繁，报告的却是你对例子有多容易想起来的印象。这样替代问题，不可避免地会产生系统性错误。
  - 处理：复核后重写。“……有多容易的印象”定语生硬，抽象名词作主语 复核：改写没有保留术语表中的“印象”，且“报告的却是你觉得……”仍然拗口。应明确区分要估计的数量或频率与实际报告的提取难易印象。

- 英文：Each factor in your list will be a potential source of bias.
  - 原译：你列出的每一个因素，都是偏差的一个潜在来源。
  - 现译：你列出的每个因素，都可能是偏差的来源。
  - 处理：Astra 复核通过。“一个潜在来源”照搬 a potential source

- 英文：A judicial error that affects you will undermine your faith in the justice system more than a similar incident you read about in a newspaper.
  - 原译：一次影响到你本人的司法错误，比你在报纸上读到的类似事件，更能动摇你对司法系统的信心。
  - 现译：影响到你本人的司法错误，比你在报纸上读到的类似事件更能动摇你对司法系统的信心。
  - 处理：复核后重写。“一次影响到你本人的”照搬定语从句 复核：原文强调司法错误影响到本人；“自己碰上”侧重亲历或遭遇，没有明确保留受到影响这一限定。原译清楚、准确，没有必须改掉的翻译腔。

- 英文：One of the best-known studies of availability suggests that awareness of your own biases can contribute to peace in marriages, and probably in other joint projects.
  - 原译：关于可得性最有名的研究之一表明，意识到自己的偏差，有助于婚姻和睦，很可能也有助于其他合作项目中的和睦。
  - 现译：在可得性方面最有名的研究里，有一项表明：意识到自己的偏差有助于婚姻和睦，对其他合作项目很可能也是如此。
  - 处理：Astra 复核通过。“关于……之一”结构，“合作项目中的和睦”搭配生硬

- 英文：The bias is not necessarily self-serving: spouses also overestimated their contribution to causing quarrels, although to a smaller extent than their contributions to more desirable outcomes.
  - 原译：这种偏差不一定是在抬高自己：夫妻双方也高估了自己在引发争吵上的份儿，只是高估的程度比在那些更令人满意的结果上要小一些。
  - 现译：这种偏差不一定是在抬高自己：夫妻双方也高估了自己在引发争吵中所起的作用，不过，对于那些更理想的结果，他们把自己的贡献高估得更厉害。
  - 处理：复核后重写。“程度比在……上要小”比较结构拗口 复核：“高估得不像在那些……结果上那么多”仍然绕口，比较双方的贡献及高估幅度没有表达清楚。

- 英文：The opportunity for successful debiasing exists because the circumstances in which issues of credit allocation come up are easy to identify, the more so because tensions often arise when several people at once feel that their efforts are not adequately recognized.
  - 原译：之所以有机会成功消除这种偏差，是因为出现功劳分配问题的情境很容易识别；几个人同时觉得自己的努力没有得到充分认可时，常常会出现紧张气氛，这让这种情境更容易认出来。
  - 现译：之所以有机会成功消除这种偏差，是因为会出现功劳分配问题的场合很容易识别；何况几个人同时觉得自己的努力没有得到充分认可时，常常会闹得气氛紧张，这样的场合就更容易识别了。
  - 处理：复核后重写。长定语“出现……的情境”，“这让……”硬接 the more so because 复核：“是因为什么情况下……很容易辨认”断句生硬，结尾“就更容易认出来了”又省去了辨认对象，比原译更难读。原译已清楚表达紧张气氛使相关情境更容易识别的关系。

- 英文：How will people’s impressions of the frequency of a category be affected by a requirement to list a specified number of instances?
  - 原译：当时，诺伯特·施瓦茨领导的一群德国心理学家提出了一个耐人寻味的问题：如果要求人们列出指定数量的例子，他们对某一类别频率的印象会受到怎样的影响？
  - 现译：当时，诺伯特·施瓦茨领导的一群德国心理学家提出了一个耐人寻味的问题：要求人们列出指定数量的例子，会怎样影响他们对某一类别频率的印象？
  - 处理：Astra 复核通过。照搬英文被动句“会受到怎样的影响”

- 英文：Furthermore, participants who had been asked to list twelve cases in which they had not behaved assertively ended up thinking of themselves as quite assertive! If you cannot easily come up with instances of meek behavior, you are likely to conclude that you are not meek at all.
  - 原译：此外，有些参与者被要求列出十二个自己没有表现得果敢的事例，他们最后反而觉得自己相当果敢！如果你很难想出自己软弱退让的例子，你很可能会断定自己一点也不软弱。
  - 现译：此外，有些参与者被要求列出十二个自己没有表现得果敢的事例，最后反而觉得自己相当果敢！如果你很难想出自己软弱退让的例子，就很可能会断定自己一点也不软弱。
  - 处理：Astra 复核通过。多余的代词“他们”“你”

- 英文：A professor at UCLA found an ingenious way to exploit the availability bias.
  - 原译：加州大学洛杉矶分校的一位教授找到了一个巧妙的办法来利用可得性偏差。
  - 现译：加州大学洛杉矶分校的一位教授找到了一个利用可得性偏差的巧妙办法。
  - 处理：Astra 复核通过。照搬 a way to 的语序

- 英文：As predicted, participants whose experience of fluency was “explained” did not use it as a heuristic; the subjects who were told that music would make retrieval more difficult rated themselves as equally assertive when they retrieved twelve instances as when they retrieved six.
  - 原译：正如预测的那样，流畅度体验得到了“解释”的参与者，没有把它当作启发式来用；那些被告知音乐会让提取变难的参与者，提取十二个例子时和提取六个例子时，认为自己同样果敢。
  - 现译：正如预测的那样，流畅度体验得到了“解释”的参与者，没有把它当作启发式来用；被告知音乐会让提取变难的参与者，不管提取的是十二个例子还是六个，都认为自己同样果敢。
  - 处理：Astra 复核通过。照搬 as...as 比较结构，读不顺

- 英文：Among the basic features of System 1 is its ability to set expectations and to be surprised when these expectations are violated.
  - 原译：系统 1 的基本特点之一，就是能够设定预期，并在预期被违背时感到意外。
  - 现译：系统 1 的基本特点之一，就是能够设定预期，并在预期落空时感到意外。
  - 处理：Astra 复核通过。“预期被违背”被动句直译

- 英文：You will be far less surprised when you actually see him with his top hat than you would have been without the warning. In Schwarz’s experiment, the background music has been mentioned as a possible cause of retrieval problems.
  - 原译：等你真的看到他戴着高礼帽时，你就远不会像没有事先得到提醒时那样意外了。在施瓦茨的实验中，背景音乐已经被说成提取困难的一个可能原因。
  - 现译：有了这个提醒，等你真的看到他戴着高礼帽，就远没有那么意外了。在施瓦茨的实验中，实验者已经提到，背景音乐可能是提取困难的一个原因。
  - 处理：复核后重写。比较句拗口，“被说成”被动句 复核：“远没有事先没人提醒时那么意外”接连使用两个否定，比较关系比原来更绕口；第二句的主动表达可以保留。

- 英文：Students with no family history of heart disease were casual about the task and followed the availability heuristic.
  - 原译：没有心脏病家族史的学生对这项任务很随意，遵循的是可得性启发式。
  - 现译：没有心脏病家族史的学生做这项任务时很随意，遵循的是可得性启发式。
  - 处理：Astra 复核通过。“对这项任务很随意”照搬 casual about

- 英文：The following are some conditions in which people “go with the flow” and are affected more strongly by ease of retrieval than by the content they retrieved:
  - 原译：在下面这些情况下，人们会“跟着感觉走”，受提取难易程度的影响比受提取出的内容的影响更大：
  - 现译：在下面这些情况下，人们会“跟着感觉走”，提取起来容不容易，比提取出了什么内容对他们的影响更大：
  - 处理：Astra 复核通过。“受……的影响比受……的影响更大”照搬比较结构

- 英文：The authors introduce their article with a famous quote: “I don’t spend a lot of time taking polls around the world to tell me what I think is the right way to act. I’ve just got to know how I feel” (George W. Bush, November 2002).
  - 原译：作者在文章开头引用了一句名言：“我不会花很多时间在世界各地做民意调查，让它们告诉我什么是我认为正确的做法。我只需要知道自己的感觉。”（乔治·W. 布什，2002 年 11 月）
  - 现译：作者在文章开头引用了一句名言：“我不会花很多时间在世界各地搞民意调查，让民调来告诉我，我认为该怎么做才对。我只要知道自己是什么感觉就行了。”（乔治·W. 布什，2002 年 11 月）
  - 处理：Astra 复核通过。口语引语逐词直译，“让它们告诉我什么是”不像人说的话

- 英文：Merely reminding people of a time when they had power increases their apparent trust in their own intuition.
  - 原译：只要让人们回想起自己曾经掌握权力的某个时候，他们表现出来的对自己直觉的信任就会增加。
  - 现译：只要让人们回想起自己曾经掌握权力的某个时候，他们就会显得更相信自己的直觉。
  - 处理：Astra 复核通过。长定语加抽象名词“信任就会增加”

- 英文：That’s silly.
  - 原译：这很傻。
  - 现译：这挺傻的。
  - 处理：Astra 复核通过。饮水机旁的口语说得生硬

## 第 13 章 可得性、情绪与风险

- 英文：Kunreuther also observed that protective actions, whether by individuals or governments, are usually designed to be adequate to the worst disaster actually experienced.
  - 原译：昆鲁斯还观察到，无论是个人还是政府采取的防护措施，通常都以足以应付实际经历过的最严重灾难为准来设计。
  - 现译：昆鲁斯还观察到，无论是个人还是政府采取的防护措施，通常都设计得足以应付实际经历过的最严重灾难。
  - 处理：Astra 复核通过。“以……为准来设计”结构拗口

- 英文：As long ago as pharaonic Egypt, societies have tracked the high-water mark of rivers that periodically flood—and have always prepared accordingly, apparently assuming that floods will not rise higher than the existing high-water mark.
  - 原译：早在法老时代的埃及，人们就开始记录周期性泛滥的河流的最高水位，并且一直据此作准备，似乎认定洪水不会涨得比已有的最高水位更高。
  - 现译：早在法老时代的埃及，人们就开始记录周期性泛滥的河流涨到过的最高水位，并且一直据此作准备，似乎认定洪水不会涨得比已有的最高水位更高。
  - 处理：Astra 复核通过。“的……的”连用

- 英文：where Paul Slovic and his longtime collaborator Sarah Lichtenstein were joined by our former student Baruch Fischhoff.
  - 原译：在那里，我们以前的学生巴鲁克·菲施霍夫加入了保罗·斯洛维奇和他的长期合作者萨拉·利希滕斯坦的行列。
  - 现译：在那里，我们以前的学生巴鲁克·菲施霍夫也加入进来，和保罗·斯洛维奇以及他的长期合作者萨拉·利希滕斯坦一起工作。
  - 处理：Astra 复核通过。“加入了……的行列”套用 were joined by

- 英文：The media do not just shape what the public is interested in, but also are shaped by it.
  - 原译：媒体塑造了公众感兴趣的东西，反过来也被公众的兴趣塑造。
  - 现译：媒体不只左右着公众对什么感兴趣，自己也受公众兴趣的左右。
  - 处理：Astra 复核通过。“塑造……东西”“被……塑造”直译

- 英文：Unusual events (such as botulism) attract disproportionate attention and are consequently perceived as less unusual than they really are.
  - 原译：不寻常的事件（比如肉毒杆菌中毒）吸引了不成比例的关注，结果人们觉得它们没有实际上那么不寻常。
  - 现译：罕见的事件（比如肉毒杆菌中毒）受到的关注多得不成比例，结果人们以为这类事件比实际更常见。
  - 处理：按复核意见修改。“吸引了不成比例的关注”直译 复核：“没有实际上那么不寻常”仍是生硬的比较表达。上下文讨论发生频率，用“比实际更常见”更清楚。

- 英文：As mentioned earlier, Slovic eventually developed the notion of an affect heuristic, in which people make judgments and decisions by consulting their emotions: Do I like it? Do I hate it? How strongly do I feel about it?
  - 原译：按照这个概念，人们是通过询问自己的情绪来作出判断和决定的：我喜欢它吗？我讨厌它吗？我对它的感觉有多强烈？
  - 现译：按照这个概念，人们作判断、下决定时，会去问问自己的感受：我喜欢它吗？我讨厌它吗？我对它的感觉有多强烈？
  - 处理：Astra 复核通过。“通过询问自己的情绪来作出”搭配生硬

- 英文：The affect heuristic is an instance of substitution, in which the answer to an easy question (How do I feel about it?) serves as an answer to a much harder question (What do I think about it?).
  - 原译：情感启发式是替代的一个实例：一个容易的问题（我对它有什么感觉？）的答案，被当成了一个难得多的问题（我对它有什么看法？）的答案。
  - 现译：情感启发式是替代的一个实例：人们用“我对它有什么感觉？”这个简单问题的答案，来回答“我对它有什么看法？”这个难得多的问题。
  - 处理：复核后重写。括号插在名词短语中间，被动句 复核：“这个容易问题”搭配不自然，应改为“这个容易回答的问题”；其余改写准确。

- 英文：Damasio and his colleagues have observed that people who do not display the appropriate emotions before they decide, sometimes because of brain damage, also have an impaired ability to make good decisions.
  - 原译：达马西奥和他的同事们观察到，有些人在作决定之前没有表现出恰当的情绪（有时是因为脑损伤），他们作出好决定的能力也受到了损害。
  - 现译：达马西奥和他的同事们观察到，作决定之前没有表现出恰当情绪的人（有时是因为脑损伤），作出好决定的能力也受到了损害。
  - 处理：复核后重写。“有些人……，他们……”照搬关系从句 复核：do not display 表示没有表现出，改成“表现不出”增加了缺乏这种能力的含义，把观察到的表现改成了能力判断。原译保留了这一区别。

- 英文：Remarkably, members of the British Toxicology Society responded similarly: they found little benefit in substances or technologies that they thought risky, and vice versa.
  - 原译：值得注意的是，英国毒理学会的成员也作出了类似的反应：凡是他们认为有风险的物质或技术，他们都觉得没什么好处，反过来也一样。
  - 现译：值得注意的是，英国毒理学会的成员反应也差不多：凡是自己认为有风险的物质或技术，他们都觉得没什么好处，反过来也一样。
  - 处理：Astra 复核通过。“作出了……反应”虚化动词，代词重复

- 英文：Although they had received no relevant evidence, the technology they now liked more than before was also perceived as less risky.
  - 原译：尽管他们没有得到任何相关的证据，但那项他们现在比以前更喜欢的技术，在他们眼里风险也变小了。
  - 现译：他们现在比以前更喜欢那项技术；尽管没有得到任何有关风险的证据，他们也觉得它的风险变小了。
  - 处理：按复核意见修改。名词前堆了长定语 复核：改写把“更喜欢”和“觉得风险更小”并列置于让步范围内，容易误读为两者都没有相关证据。上下文明确给过好处方面的信息，缺少的只是风险方面的证据。

- 英文：“Risk” does not exist “out there,” independent of our minds and culture, waiting to be measured.
  - 原译：“风险”并不是独立于我们的头脑和文化、“在那儿”等着被测量的东西。
  - 现译：“风险”并不是独立于我们的头脑和文化、“在那儿”等人去测量的东西。
  - 处理：Astra 复核通过。“等着被测量”照搬被动态

- 英文：To illustrate his claim, Slovic lists nine ways of defining the mortality risk associated with the release of a toxic material into the air, ranging from “death per million people” to “death per million dollars of product produced.”
  - 原译：为了说明自己的主张，斯洛维奇针对向空气中释放一种有毒物质带来的死亡风险，列出了九种定义方式，从“每百万人的死亡数”到“每生产价值百万美元的产品造成的死亡数”。
  - 现译：为了说明自己的主张，斯洛维奇以向空气中释放一种有毒物质带来的死亡风险为例，列出了九种定义方式，从“每百万人的死亡数”到“每生产价值百万美元的产品造成的死亡数”。
  - 处理：复核后重写。“针对……”长状语前置，句子头重 复核：“列出了九种方式，来定义……”断得生硬，又把句末“从……到……”与它说明的“九种方式”隔开了很远。原译的层次和列举关系更清楚。

- 英文：His point is that the evaluation of the risk depends on the choice of a measure—with the obvious possibility that the choice may have been guided by a preference for one outcome or another.
  - 原译：他的观点是，对风险的评估取决于选择哪种衡量标准，而且显然有这样一种可能：选择哪种标准，本身就受到了对这种或那种结果的偏好的引导。
  - 现译：他的观点是，对风险的评估取决于选择哪种衡量标准，而且显然有这样一种可能：选择哪种标准，本身就是由对某种结果的偏好引导的。
  - 处理：Astra 复核通过。“受到了……的偏好的引导”的字连串

- 英文：Every policy question involves assumptions about human nature, in particular about the choices that people may make and the consequences of their choices for themselves and for society.
  - 原译：每个政策问题都涉及对人性的假设，特别是关于人们可能作出哪些选择，以及这些选择会给他们自己和社会带来哪些后果。
  - 现译：每个政策问题都涉及对人性的假设，尤其是对两件事的假设：人们可能作出哪些选择，这些选择又会给他们自己和社会带来哪些后果。
  - 处理：复核后重写。“特别是关于……”照搬 in particular about，句子不完整 复核：“假设人们可能作出哪些选择”把名词性的假设硬改成了“假设＋疑问分句”，搭配不自然；选择和后果应并列作为假设涉及的内容。

- 英文：He starts from the position that risk regulation and government intervention to reduce risks should be guided by rational weighting of costs and benefits, and that the natural units for this analysis are the number of lives saved (or perhaps the number of life-years saved, which gives more weight to saving the young) and the dollar cost to the economy.
  - 原译：他的出发点是：风险监管和政府为降低风险而进行的干预，应该以理性地权衡成本和收益为指导；这种分析自然要用的计量单位，是挽救的生命数（也可能是挽救的生命年数，这样会更看重挽救年轻人）和整个经济为此付出的美元成本。
  - 现译：他的出发点是：风险监管和政府为降低风险而进行的干预，应该以理性地权衡成本和收益为指导；这种分析自然要用的计量单位，是挽救的生命数（也可能是挽救的生命年数，这样会更看重挽救年轻人）和整个经济为此付出的美元成本。
  - 处理：复核后退回原译。虚化动词“进行” 复核：“进行干预”本来就是自然的搭配；“采取干预”反而生硬，通常应说“采取干预措施”。此次替换没有改善中文。

- 英文：In particular, the importance of an idea is often judged by the fluency (and emotional charge) with which that idea comes to mind.
  - 原译：特别是，一个观念有多重要，常常是根据这个观念浮现在脑中的流畅程度（以及它带有的情绪色彩）来判断的。
  - 现译：特别是，人们常常根据一个观念浮现在脑中有多流畅（以及带有多强的情绪色彩），来判断这个观念有多重要。
  - 处理：Astra 复核通过。被动句无施事，“是根据……来判断的”拖沓

- 英文：An availability cascade is a self-sustaining chain of events, which may start from media reports of a relatively minor event and lead up to public panic and large-scale government action. On some occasions, a media story about a risk catches the attention of a segment of the public, which becomes aroused and worried.
  - 原译：可得性级联是一个自我维持的事件链条，它可能从媒体对一件相对不起眼的事情的报道开始，最后发展到公众恐慌和大规模的政府行动。在某些情况下，媒体关于某种风险的一篇报道引起了一部分公众的注意，这些人变得激动和担忧。
  - 现译：可得性级联是一个自我维持的事件链条：它可能从媒体报道一件相对不起眼的事开始，一路发展到公众恐慌和大规模的政府行动。有时，媒体对某种风险的一篇报道引起了一部分公众的注意，这些人变得激动和担忧。
  - 处理：复核后重写。“媒体对……的报道”名词化长定语，“在某些情况下”直译 on some occasions 复核：原文的 may 同时管辖起点和后续发展；改成“起点可能是……最后发展到……”后，可能性只明确落在起点上，终点容易被读成必然结果。

- 英文：Scientists and others who try to dampen the increasing fear and revulsion attract little attention, most of it hostile: anyone who claims that the danger is overstated is suspected of association with a “heinous cover-up.”
  - 原译：科学家和其他试图平息日益增长的恐惧和反感的人，很少受到关注，得到的关注也大多带有敌意：任何声称危险被夸大了的人，都会被怀疑与一场“令人发指的掩盖行动”有牵连。
  - 现译：科学家和其他一些人试图平息日益增长的恐惧和反感，却很少受到关注，得到的关注也大多带有敌意：谁要是说危险被夸大了，就会被怀疑和一场“令人发指的掩盖行动”有牵连。
  - 处理：Astra 复核通过。主语前堆长定语，“任何……的人”照搬 anyone who

- 英文：The combination of probability neglect with the social mechanisms of availability cascades inevitably leads to gross exaggeration of minor threats, sometimes with important consequences.
  - 原译：忽视概率与可得性级联的社会机制结合在一起，必然会导致对小威胁的严重夸大，有时还会造成重大的后果。
  - 现译：忽视概率与可得性级联的社会机制结合在一起，必然会把小威胁严重夸大，有时还会造成重大的后果。
  - 处理：Astra 复核通过。“导致对……的严重夸大”名词化

- 英文：Slovic rightly stresses the resistance of the public to the idea of decisions being made by unelected and unaccountable experts.
  - 原译：斯洛维奇正确地强调了，公众抗拒由未经选举、不必问责的专家来作决定。
  - 现译：斯洛维奇强调，公众抗拒由未经选举、不受问责的专家来作决定，这一点说得对。
  - 处理：按复核意见修改。“正确地强调了”照搬副词 rightly 复核：沿用了原译中不准确的“不必问责”：unaccountable 指专家本人不受问责，不是专家无须问责他人。

- 英文：The Love Canal incident may have caused excessive resources to be allocated to the management of toxic waste, but it also had a more general effect in raising the priority level of environmental concerns.
  - 原译：拉夫运河事件也许导致过多的资源被分配给有毒废物的治理，但它也产生了一个更普遍的影响，提高了环境问题的优先级。
  - 现译：拉夫运河事件也许让有毒废物治理分到了过多的资源，但它也带来了一个更广泛的影响：提高了环境问题的优先级。
  - 处理：复核后重写。“导致……被分配给”被动套被动，“产生了……影响” 复核：“让分给……的资源过多了”仍然拗口；more general 在这里指影响范围更广，不宜译成发生得更普遍。

- 英文：“This is an availability cascade: a nonevent that is inflated by the media and the public until it fills our TV screens and becomes all anyone is talking about.”
  - 原译：“这是一个可得性级联：一件本来不算什么的事，被媒体和公众越吹越大，直到占满我们的电视屏幕，成了所有人都在谈论的话题。”
  - 现译：“这就是可得性级联：一件本来不算什么的事，被媒体和公众越吹越大，直到占满电视屏幕，人人谈的都是这件事。”
  - 处理：按复核意见修改。“一个”“我们的”照搬英文，口语不自然 复核：沿用了原译的遗漏：all anyone is talking about 不只是人人都在谈论，还强调大家谈的全是这件事。

## 第 14 章 汤姆·W 的专业

- 英文：Using base-rate information is the obvious move when no other information is provided.
  - 原译：在没有提供其他信息的情况下，利用基础比率信息是显而易见的做法。
  - 现译：没有给出其他信息时，利用基础比率信息是显而易见的做法。
  - 处理：Astra 复核通过。“在……的情况下”套式

- 英文：You will get more out of the chapter if you give the task a quick try; reading the report on Tom W is necessary to make your judgments about the various graduate specialties.
  - 原译：如果你先快速试一试这项任务，就能从这一章得到更多收获；要对各个研究生专业作出判断，就得读一读这份关于汤姆·W 的报告。
  - 现译：如果你先快速试一试这项任务，读这一章的收获会更大；要对各个研究生专业下判断，就得读一读这份关于汤姆·W 的报告。
  - 处理：Astra 复核通过。“从这一章得到更多收获”照搬 get more out of，虚化动词“作出判断”

- 英文：This question too is straightforward. It requires you to retrieve, or perhaps to construct, a stereotype of graduate students in the different fields.
  - 原译：这个问题也很简单。它要求你从记忆中调出，或者临时构建，各个领域研究生的刻板印象。
  - 现译：这个问题也很简单。你需要从记忆中调出各个领域研究生的刻板印象，或者临时构建出来。
  - 处理：复核后重写。插入语把动词和宾语隔开，照搬英文句法；“它要求你”抽象主语 复核：“或许还得”把原文的选择关系改成了追加步骤：原文是从记忆中调出刻板印象，或者可能需要构建，并非调出之后还要另外构建。

- 英文：However, the hints planted in the description (corny puns and others) were intended to activate an association with a stereotype, an automatic activity of System 1.
  - 原译：不过，描述里埋下的那些线索（老套的双关语等等）是为了让人联想到某种刻板印象，而这是系统 1 的一种自动活动。
  - 现译：不过，描述里埋下的那些线索（老套的双关语等等）是为了让人联想到某种刻板印象，这种联想是系统 1 自动产生的。
  - 处理：Astra 复核通过。同位语直译成“系统 1 的一种自动活动”，多余的“一种”

- 英文：The instructions for this similarity task required a comparison of the description of Tom W to the stereotypes of the various fields of specialization.
  - 原译：这项相似性任务的说明，要求把汤姆·W 的描述和各个专业领域的刻板印象作比较。
  - 现译：按照这项相似性任务的说明，要把汤姆·W 的描述和各个专业领域的刻板印象作比较。
  - 处理：Astra 复核通过。抽象名词“说明”作主语，主谓之间用逗号断开

- 英文：The third task in the sequence was administered to graduate students in psychology, and it is the critical one: rank the fields of specialization in order of the likelihood that Tom W is now a graduate student in each of these fields.
  - 原译：这一系列中的第三项任务是让心理学研究生做的，它才是关键：按照汤姆·W 现在是各个领域研究生的可能性大小，给这些专业领域排序。
  - 现译：这组任务中的第三项是让心理学研究生做的，它才是关键：按照汤姆·W 现在是各个领域研究生的可能性大小，给这些专业领域排序。
  - 处理：Astra 复核通过。“这一系列中的”直译 in the sequence

- 英文：That was a happy moment—even the mighty had fallen.
  - 原译：那是一个让人高兴的时刻：连高手也失手了。
  - 现译：那一刻真让人高兴：连高手也失手了。
  - 处理：Astra 复核通过。“那是一个……的时刻”照搬 That was a happy moment

- 英文：Of course, Robyn immediately recognized his mistake as soon as I mentioned “base rate,” but he had not spontaneously thought of it.
  - 原译：当然，我一提“基础比率”，罗宾马上就意识到了自己的错误，但他并没有自发地想到它。
  - 现译：当然，我一提“基础比率”，罗宾马上就意识到了自己的错误，但他并没有自己想到基础比率。
  - 处理：复核后重写。“自发地想到它”直译 spontaneously thought of it，代词“它”多余 复核：“这一点”紧接“自己的错误”，容易被理解为没有自行发现错误；原文指的是未自行想到基础比率，应明确指代。

- 英文：Although he knew as much as anyone about the role of base rates in prediction, he neglected them when presented with the description of an individual’s personality.
  - 原译：尽管他对基础比率在预测中的作用了解得不比任何人少，可是一看到对一个人性格的描述，他就把基础比率忽视了。
  - 现译：尽管他对基础比率在预测中的作用了解得不比任何人少，可是一看到某个人的性格描述，他就忽视了基础比率。
  - 处理：Astra 复核通过。“对一个人性格的描述”名词化结构，“把……忽视了”搭配生硬

- 英文：A question about probability or likelihood activates a mental shotgun, evoking answers to easier questions. One of the easy answers is an automatic assessment of representativeness—routine in understanding language.
  - 原译：一个关于概率或可能性的问题会启动心理霰弹枪，引出对一些更容易的问题的回答。其中一个容易的回答，就是对代表性的自动评估，这是理解语言时常规的一步。
  - 现译：关于概率或可能性的问题会触发心理霰弹枪，引出一些更容易的问题的答案。其中一个容易的答案，就是对代表性的自动评估，这是我们理解语言时的常规动作。
  - 处理：Astra 复核通过。多余的“一个”，“对……的回答”名词化；“启动”和术语“启动效应”容易混淆

- 英文：In other situations, the stereotypes are false and the representativeness heuristic will mislead, especially if it causes people to neglect base-rate information that points in another direction.
  - 原译：在另一些情况下，刻板印象是错的，代表性启发式就会误导人，尤其是当它让人忽视指向另一个方向的基础比率信息时。
  - 现译：在另一些情况下，刻板印象是错的，代表性启发式就会误导人；如果基础比率信息指向另一个方向，而这种启发式又让人忽视了它，就尤其如此。
  - 处理：复核后重写。“尤其是当……时”套式，定语从句前置成长定语 复核：“误导就尤其严重”增加了误导程度更严重的判断。原文强调的是尤其会造成误导的条件，没有明确比较误导的严重程度。

- 英文：And if you must guess whether a woman who is described as “a shy poetry lover” studies Chinese literature or business administration, you should opt for the latter option.
  - 原译：如果有一位女性被描述为“一个害羞的诗歌爱好者”，你必须猜她学的是中国文学还是工商管理，那么你应该选后者。
  - 现译：如果有一位女性被描述为“一个害羞的诗歌爱好者”，而你必须猜她学的是中国文学还是工商管理，那么你应该选后者。
  - 处理：Astra 复核通过。两个条件分句硬接在一起，读起来像两句话

- 英文：However, concern for base rates evidently disappears as soon as Tom W’s personality is described.
  - 原译：然而，一旦描述了汤姆·W 的性格，对基础比率的关注显然就消失了。
  - 现译：然而，一旦有了对汤姆·W 性格的描述，人们显然就不再关注基础比率了。
  - 处理：Astra 复核通过。抽象名词“对基础比率的关注”作主语

- 英文：Psychologists have conducted many experiments in which base-rate information is explicitly provided as part of the problem, and many of the participants are influenced by those base rates, although the information about the individual case is almost always weighted more than mere statistics.
  - 原译：心理学家做过许多实验，把基础比率信息作为问题的一部分明确给出，许多参与者都受到了这些基础比率的影响，尽管个案信息几乎总是被赋予比单纯的统计数据更大的权重。
  - 现译：心理学家做过许多实验，把基础比率信息作为问题的一部分明确给出，许多参与者都受到了这些基础比率的影响，不过比起单纯的统计数据，他们几乎总是更看重个案信息。
  - 处理：复核后重写。“被赋予……权重”被动句，比较项塞进长定语 复核：“给个案信息的权重……比给单纯的统计数据更大”比较项不完整，后半句缺少“的权重”，读起来仍不顺。

- 英文：An experiment that was conducted a few years ago with Harvard undergraduates yielded a finding that surprised me: enhanced activation of System 2 caused a significant improvement of predictive accuracy in the Tom W problem.
  - 原译：几年前，有人以哈佛大学的本科生为对象做了一项实验，得出的发现让我很意外：更多地激活系统 2，使人们在汤姆·W 问题上的预测准确性显著提高了。
  - 现译：几年前，有人以哈佛大学的本科生为对象做了一项实验，结果让我很意外：更多地激活系统 2，显著提高了人们在汤姆·W 问题上预测的准确性。
  - 处理：Astra 复核通过。“得出的发现”照搬 yielded a finding，“使……提高了”句式生硬

- 英文：When an incorrect intuitive judgment is made, System 1 and System 2 should both be indicted.
  - 原译：作出了错误的直觉判断时，系统 1 和系统 2 都应该被追究责任。
  - 现译：出现错误的直觉判断时，系统 1 和系统 2 都有责任。
  - 处理：复核后重写。虚化动词“作出”加被动句“被追究责任” 复核：前半句更顺了，但“系统 1 和系统 2 的责任都应该追究”语序仍显迂回，可以直接说明应追究谁的责任。

- 英文：The relevant “rules” for cases such as the Tom W problem are provided by Bayesian statistics.
  - 原译：像汤姆·W 问题这样的情况，相关的“规则”由贝叶斯统计提供。
  - 现译：像汤姆·W 问题这样的情况，相关的“规则”来自贝叶斯统计。
  - 处理：Astra 复核通过。“由……提供”直译 are provided by

- 英文：Question the diagnosticity of your evidence.
  - 原译：- 质疑你的证据的诊断性。
  - 现译：- 质疑你手上证据的诊断性。
  - 处理：Astra 复核通过。“你的证据的”连用两个“的”

## 第 15 章 琳达：少即是多

- 英文：The best-known and most controversial of our experiments involved a fictitious lady called Linda.
  - 原译：在我们所有的实验里，最出名、争议也最大的一个，涉及一位名叫琳达的虚构女士。
  - 现译：在我们所有的实验里，最出名、争议也最大的一个，围绕的是一位名叫琳达的虚构女士。
  - 处理：Astra 复核通过。“涉及”直译 involved

- 英文：In one of our experiments we presented participants with a list of eight possible scenarios for Linda.
  - 原译：在我们的一项实验中，我们给参与者看了一份清单，上面列着关于琳达的八种可能情景。
  - 现译：在其中一项实验中，我们给参与者看了一份清单，上面列着关于琳达的八种可能情景。
  - 处理：Astra 复核通过。“我们的……我们”代词重复

- 英文：In the absence of a competing intuition, logic prevails.
  - 原译：没有一个与之竞争的直觉时，逻辑就会占上风。
  - 现译：没有直觉与逻辑抗衡时，逻辑就会占上风。
  - 处理：按复核意见修改。“一个与之竞争的直觉”照搬 a competing intuition 复核：“别的直觉”容易让人误以为逻辑也是一种直觉，“它”的指代也不够清楚。原文说的是没有与逻辑竞争的直觉。

- 英文：He auctioned sets of ten high-value cards, and identical sets to which three cards of modest value were added.
  - 原译：他拍卖了一些十张一套的高价值卡片，还拍卖了另一些套卡，它们和前者完全相同，只是另外加了三张价值一般的卡片。
  - 现译：他拍卖的套卡有两种：一种是十张一套的高价值卡片；另一种是同样的十张，再加上三张价值一般的卡片。
  - 处理：Astra 复核通过。定语从句拆成“它们和前者……”，照搬英文后置修饰

- 英文：Here again, the scenario that was judged more probable was unquestionably more plausible, a more coherent fit with all that was known about the best tennis player in the world.
  - 原译：这里也一样：被判断为更可能的情景无疑更可信，它与人们对这位世界最佳网球手的全部了解更连贯、更吻合。
  - 现译：这里也一样：人们认为更可能的那个情景无疑更可信，和大家对这位世界最佳网球手的全部了解也更吻合，放在一起更连贯。
  - 处理：复核后重写。“被判断为”被动句，多余的代词“它” 复核：“和……全部了解更连贯”搭配不当。原文的 more coherent fit 指情景与已有了解更加一致，并非两者之间更加“连贯”。

- 英文：They would (hypothetically) win $25 if their chosen sequence showed up.
  - 原译：如果他们选的序列出现了，他们就能（假设性地）赢得 25 美元。
  - 现译：如果他们选的序列出现了，就能赢得 25 美元（只是假设）。
  - 处理：Astra 复核通过。“（假设性地）”直译 hypothetically 插在动词前，代词“他们”重复

- 英文：However, their vacation did not depend on a correct answer; they spent very little time on it, and were content to answer as if they had only been “asked for their opinion.”
  - 原译：然而，他们的假期并不取决于答对与否；他们在这道题上只花了很少的时间，就当别人只是在“问问他们的看法”，这样作答就满足了。
  - 现译：然而，他们的假期并不取决于答对与否；他们在这道题上花的时间很少，只当别人是在“问问他们的看法”，觉得这样回答就够了。
  - 处理：按复核意见修改。“这样作答就满足了”照搬 were content to answer，语序别扭 复核：“答得就像别人只是……”比较关系生硬，“这样也就满足了”仍带翻译腔。原文指他们把问题当成征询个人看法，觉得这样回答便已足够。

- 英文：These arguments were sometimes extended to suggest that our entire enterprise was misguided: if one salient cognitive illusion could be weakened or explained away, others could be as well.
  - 原译：这些论点有时还被进一步引申，暗示我们的整个研究事业都走错了方向：如果一个醒目的认知错觉能被削弱或被解释掉，其他的认知错觉也可以。
  - 现译：有时还有人进一步引申这些论点，暗示我们的整个研究事业都走错了方向：如果一种显著的认知错觉能被削弱，或者能被解释成并非真正的错觉，那么其他认知错觉也一样。
  - 处理：复核后重写。一句里连用三个“被” 复核：salient 应按术语表译为“显著”；“解释掉”仍是生硬直译，没有清楚表达通过解释否定其错觉性质的意思。

- 英文：The evidence that we had built up for heuristics from between-subjects experiment (including studies of Linda) was not challenged—it was simply not addressed, and its salience was diminished by the exclusive focus on the conjunction fallacy.
  - 原译：我们从组间实验（包括关于琳达的研究）中为启发式积累起来的证据，并没有受到质疑，大家只是根本不去讨论它；而人们的注意力全都集中在合取谬误上，也让这些证据显得不再那么醒目。
  - 现译：我们通过组间实验（包括关于琳达的研究）积累了支持启发式的证据。这些证据并没有受到质疑，大家只是根本不去讨论它们；而人们的注意力全都集中在合取谬误上，这些证据也就显得没那么显著了。
  - 处理：复核后重写。主语前堆了一长串定语 复核：拆开长定语的方向正确，但“为启发式积累起了证据”搭配仍显生硬；salience 应按术语表使用“显著性”。

## 第 16 章 原因胜过统计

- 英文：The court tested the reliability of the witness under the circumstances that existed on the night of the accident and concluded that the witness correctly identified each one of the two colors 80% of the time and failed 20% of the time.
  - 原译：法庭在事故当晚的同样条件下测试了这位目击者的可靠性，结论是：两种颜色中的每一种，目击者都有 80% 的时候认得对，20% 的时候认错。
  - 现译：法庭在事故当晚的同样条件下测试了这位目击者的可靠性，结论是：无论是哪种颜色，目击者都有 80% 的时候认得对，20% 的时候认错。
  - 处理：Astra 复核通过。“两种颜色中的每一种”照搬 each one of the two colors

- 英文：Now consider a variation of the same story, in which only the presentation of the base rate has been altered.
  - 原译：现在来看同一个故事的一个变体，其中只改变了基础比率的呈现方式。
  - 现译：现在来看同一个故事的变体，这一次只改了基础比率的呈现方式。
  - 处理：Astra 复核通过。多余的“一个”，“其中”照搬 in which 从句

- 英文：The inferences from the two stories about the color of the car are contradictory and approximately cancel each other. The chances for the two colors are about equal (the Bayesian estimate is 41%, reflecting the fact that the base rate of Green cabs is a little more extreme than the reliability of the witness who reported a Blue cab).
  - 原译：两个故事对车的颜色作出的推断互相矛盾，大致彼此抵消。两种颜色的可能性差不多（贝叶斯估计值是 41%，这反映出绿色出租车的基础比率，比那位说看到蓝色出租车的目击者的可靠性稍微极端一点）。
  - 现译：关于车的颜色，两个故事得出的推断互相矛盾，大致彼此抵消。两种颜色的可能性差不多（贝叶斯估计值是 41%，反映出绿色出租车的基础比率比目击者的可靠性稍微极端一点，而这位目击者说的是蓝色出租车）。
  - 处理：Astra 复核通过。“作出的推断”和“目击者的可靠性”前堆了长定语

- 英文：The two types of base-rate information are treated differently:
  - 原译：人们对这两类基础比率信息的处理方式不同：
  - 现译：这两类基础比率信息，人们处理起来并不一样：
  - 处理：Astra 复核通过。抽象名词“处理方式”作中心，照搬 are treated differently

- 英文：Causal base rates are treated as information about the individual case and are easily combined with other case-specific information.
  - 原译：因果性基础比率被当作关于这个个案的信息，很容易与其他针对这个个案的信息结合起来。
  - 现译：因果性基础比率会被当成这个个案本身的信息，很容易和关于这个个案的其他信息结合起来。
  - 处理：Astra 复核通过。“关于……的信息”“其他针对……的信息”重复堆叠

- 英文：The causal version of the cab problem had the form of a stereotype: Green drivers are dangerous.
  - 原译：出租车问题的因果版本具有刻板印象的形式：绿色公司的司机很危险。
  - 现译：出租车问题的因果版本，形式上就是一个刻板印象：绿色公司的司机很危险。
  - 处理：Astra 复核通过。“具有……的形式”直译 had the form of

- 英文：In other contexts, however, such as hiring or profiling, there is a strong social norm against stereotyping, which is also embedded in the law.
  - 原译：然而在另一些场合，比如招聘或按群体特征排查嫌疑人，社会上有一条反对用刻板印象看人的强有力的规范，它也写进了法律。
  - 现译：然而在另一些场合，比如招聘或按群体特征排查嫌疑人，社会上有一条约束力很强的规范，反对用刻板印象看人，这条规范也写进了法律。
  - 处理：复核后重写。“规范”前堆长定语，“它”照搬 which 从句 复核：拆开长定语的方向正确，但“一条很强的规范”搭配生硬，应明确是社会规范的约束力很强。

- 英文：In his experiment, Ajzen showed his participants brief vignettes describing some students who had taken an exam at Yale and asked the participants to judge the probability that each student had passed the test. The manipulation of causal base rates was straightforward: Ajzen told one group that the students they saw had been drawn from a class in which 75% passed the exam, and told another group that the same students had been in a class in which only 25% passed.
  - 原译：在他的实验中，阿耶兹给参与者看一些简短的描述，描述的是在耶鲁参加过一次考试的几个学生，然后请参与者判断每个学生通过考试的概率。对因果性基础比率的操纵很简单：阿耶兹告诉一组参与者，他们看到的学生来自一个有 75% 的人通过考试的班级；又告诉另一组参与者，同样这些学生所在的班级只有 25% 的人通过。
  - 现译：阿耶兹在实验中给参与者看了一些简短的描述，描述的是在耶鲁参加过一次考试的几个学生，然后请参与者判断每个学生通过考试的概率。操纵因果性基础比率的办法很简单：阿耶兹告诉一组参与者，他们看到的学生来自一个班，那个班有 75% 的人通过了考试；又告诉另一组参与者，同样这些学生所在的班只有 25% 的人通过。
  - 处理：Astra 复核通过。多余的“他的”，抽象名词“对……的操纵”作主语，“班级”前定语过长

- 英文：This base rate is a purely statistical fact about the ensemble from which cases have been drawn.
  - 原译：这个基础比率纯粹是一个统计事实，说的是从中抽出这些个案的那一整组人。
  - 现译：这个基础比率纯粹是一个统计事实，说的是一整组人，这些个案就是从这组人里抽出来的。
  - 处理：Astra 复核通过。“从中抽出……的那一整组人”照搬 from which 从句

- 英文：It is tempting to conclude that we have reached a satisfactory conclusion: causal base rates are used; merely statistical facts are (more or less) neglected.
  - 原译：我们很想就此认为，已经得出了一个令人满意的结论：因果性基础比率会被使用，纯粹的统计事实（或多或少）会被忽视。
  - 现译：我们很想就此认为，已经得出了一个令人满意的结论：人们会利用因果性基础比率，却（或多或少）忽视纯粹的统计事实。
  - 处理：Astra 复核通过。连用两个“会被”，照搬英文被动

- 英文：The reckless cabdrivers and the impossibly difficult exam illustrate two inferences that people can draw from causal base rates: a stereotypical trait that is attributed to an individual, and a significant feature of the situation that affects an individual’s outcome.
  - 原译：鲁莽的出租车司机和难得离谱的考试，说明了人们可以从因果性基础比率中得出的两种推断：一种是归到某个人身上的刻板印象特质，另一种是情境中影响个人结果的一个重要特征。
  - 现译：鲁莽的出租车司机和难得离谱的考试，说明人们可以从因果性基础比率中得出两种推断：一种是某个人身上带有刻板印象里的特质，另一种是情境中有一个重要特征，会影响个人的结果。
  - 处理：Astra 复核通过。三处名词前都堆了从句式长定语

- 英文：The experiment shows that individuals feel relieved of responsibility when they know that others have heard the same request for help.
  - 原译：这个实验表明，当个人知道别人也听到了同样的求助时，他们会觉得自己卸下了责任。
  - 现译：这个实验表明，一个人知道别人也听到了同样的求助时，会觉得责任不再落在自己身上。
  - 处理：Astra 复核通过。“当……时”加多余的“他们”，“个人”照搬 individuals

- 英文：And that means you, too.
  - 原译：这也包括你。
  - 现译：你也不例外。
  - 处理：Astra 复核通过。直译 that means you, too，不像口语

- 英文：If I find myself in a situation in which other people have an opportunity to help, I might not step forward. The presence of others would reduce my sense of personal responsibility more than I initially thought.
  - 原译：如果我身处的情境里别人也有机会去帮忙，我可能不会挺身而出。别人在场，会比我起初以为的更多地削弱我的个人责任感。
  - 现译：如果别人也有机会出手相助，我可能就不会挺身而出。有别人在场，我的个人责任感会减弱，而且减弱的程度会比我起初以为的更大。
  - 处理：按复核意见修改。“我身处的情境里”照搬从句，“会比……更多地削弱”比较结构生硬 复核：“如果我遇到的情况是……”仍然绕口；“减弱得……更多”也不如直接比较减弱的程度自然。

- 英文：Thus your prior belief about any unspecified participant should be that he did not rush to help.
  - 原译：所以，对于任何一位没有具体指明的参与者，你的先验信念应该是：他没有赶去帮忙。
  - 现译：所以，对于任何一位你不了解具体情况的参与者，你的先验信念都应该是：他没有赶去帮忙。
  - 处理：复核后重写。“对于……来说”式句首，“没有具体指明的”直译 unspecified 复核：删掉了 unspecified 的限定。原文说的是尚不了解具体情况的参与者，应先根据基础比率判断；“不管说的是哪一位参与者”扩大了适用范围。

- 英文：Indeed, Nisbett and Borgida reported similar findings in teaching another study, in which mild social pressure caused people to accept much more painful electric shocks than most of us (and them) would have expected. Students who do not develop a new appreciation for the power of social setting have learned nothing of value from the experiment. The predictions they make about random strangers, or about their own behavior, indicate that they have not changed their view of how they would have behaved.
  - 原译：在那项研究里，温和的社会压力就让人们接受了比我们大多数人（也包括他们）预想的痛苦得多的电击。没有对社会情境的力量产生新认识的学生，并没有从实验中学到任何有价值的东西。他们对随机挑选的陌生人或对自己的行为所作的预测表明，他们并没有改变对自己在那种情境下会怎样表现的看法。
  - 现译：在那项研究里，温和的社会压力就让人们接受了非常痛苦的电击，人们愿意承受的程度远远超出我们大多数人（也包括他们）的预想。学生如果没有对社会情境的力量产生新的认识，就没有从实验中学到任何有价值的东西。他们预测随机挑选的陌生人会怎么做，或者预测自己会怎么做，从这些预测可以看出，他们对自己在那种情境下会怎样表现的看法并没有改变。
  - 处理：复核后重写。“电击”“学生”“预测”前都挂着很长的定语，“所作的预测”是虚化动词 复核：拆句后，“电击的痛苦程度……超出预想”容易被理解为电击比预想的更疼。原文强调的是，人们竟会接受如此痛苦的电击，超出了大家对其行为的预期。

- 英文：But when the students were surprised by individual cases—two nice people who had not helped—they immediately made the generalization and inferred that helping is more difficult than they had thought.
  - 原译：但当让学生吃惊的是个案（两个和善的人竟然没有帮忙）时，他们立刻就作出了概括，推断出帮助别人比他们原来想的更难。
  - 现译：但如果让学生吃惊的是个案（两个和善的人竟然没有帮忙），他们立刻就归纳出一般结论，推断出帮助别人比他们原来想的更难。
  - 处理：复核后保留改写。“当……时”把括号夹在中间，“作出了概括”直译 made the generalization 复核：原文在叙述已经观察到的实验结果，when 表示当时的情形；改成“如果”使事实叙述变成了假设条件。可以保留“归纳出一般结论”的改进。

- 英文：People who are taught surprising statistical facts about human behavior may be impressed to the point of telling their friends about what they have heard, but this does not mean that their understanding of the world has really changed.
  - 原译：人们听人讲了一些关于人类行为、令人吃惊的统计事实后，可能会印象深刻，以至于把听到的东西讲给朋友听，但这并不意味着他们对世界的理解真的改变了。
  - 现译：人们听人讲了一些关于人类行为的统计事实，觉得出人意料，可能会印象深刻，甚至把听到的东西讲给朋友听，但这并不意味着他们对世界的理解真的改变了。
  - 处理：Astra 复核通过。两个定语用顿号并列堆在“统计事实”前，“以至于”直译 to the point of

- 英文：That is why this book contains questions that are addressed personally to the reader.
  - 原译：这就是为什么本书里有一些直接向读者本人提出的问题。
  - 现译：所以本书里有一些问题，是直接问读者本人的。
  - 处理：Astra 复核通过。“这就是为什么”直译 That is why，“问题”前定语过长

## 第 17 章 均值回归

- 英文：I had one of the most satisfying eureka experiences of my career while teaching flight instructors in the Israeli Air Force about the psychology of effective training.
  - 原译：我职业生涯中最令人满足的顿悟之一，发生在我给以色列空军的飞行教官讲授有效训练的心理学时。
  - 现译：我给以色列空军的飞行教官讲授有效训练的心理学时，有过一次顿悟，那是我职业生涯中最令人满足的顿悟之一。
  - 处理：Astra 复核通过。“……之一，发生在……时”，时间状语照搬英文放在句末

- 英文：When I finished my enthusiastic speech, one of the most seasoned instructors in the group raised his hand and made a short speech of his own. He began by conceding that rewarding improved performance might be good for the birds, but he denied that it was optimal for flight cadets.
  - 原译：我满怀热情地讲完后，在场最资深的教官之一举起手，也作了一番简短的发言。他先承认，奖励进步对鸟类也许有好处，但他否认这对飞行学员是最好的办法。
  - 现译：我满怀热情地讲完后，在场一位资历最深的教官举起手，也简短地讲了几句。他先承认，奖励进步对鸟类也许有好处，但否认这对飞行学员是最好的办法。
  - 处理：Astra 复核通过。“……之一举起手”作主语别扭，“作了一番发言”是虚化动词，后句多余的“他”

- 英文：On the other hand, I have often screamed into a cadet’s earphone for bad execution, and in general he does better on his next try.
  - 原译：另一方面，学员动作做得糟糕时，我常常对着他的耳机大吼，而一般来说，他下一次会做得更好。
  - 现译：反过来，学员动作做得糟糕时，我常常对着他的耳机大吼，一般来说，他下一次会做得更好。
  - 处理：Astra 复核通过。口语里用“另一方面”“而”，照搬 On the other hand 和 and

- 英文：This was a joyous moment of insight, when I saw in a new light a principle of statistics that I had been teaching for years.
  - 原译：那是一个令人欣喜的领悟时刻：一条我已经教了多年的统计学原理，我从一个新的角度看清了它。
  - 现译：那一刻我满心欢喜，豁然开朗：一条我已经教了多年的统计学原理，我从一个新的角度看清了。
  - 处理：Astra 复核通过。“一个令人欣喜的领悟时刻”直译名词短语，句末“它”多余

- 英文：But the inference he had drawn about the efficacy of reward and punishment was completely off the mark.
  - 原译：但他由此对奖励和惩罚的效果作出的推断，完全不着边际。
  - 现译：但他由此对奖惩效果得出的结论，却完全错了。
  - 处理：按复核意见修改。“对……作出的推断”长定语加虚化动词 复核：仍沿用了“不着边际”的误译。这里的 completely off the mark 指结论完全错误，而不是说话空泛或离题。

- 英文：The discovery I made on that day was that the flight instructors were trapped in an unfortunate contingency: because they punished cadets when performance was poor, they were mostly rewarded by a subsequent improvement, even if punishment was actually ineffective.
  - 原译：那天我的发现是，飞行教官们陷入了一种不幸的奖惩关联：他们在学员表现差时惩罚学员，而接下来学员多半会有进步，这对教官来说就成了奖励，哪怕惩罚其实并没有效果。
  - 现译：那天我发现，飞行教官们陷入了一种不幸的奖惩关联：他们在学员表现差时惩罚学员，而接下来学员多半会有进步，这对教官来说就成了奖励，哪怕惩罚其实并没有效果。
  - 处理：Astra 复核通过。“我的发现是”照搬 The discovery I made was

- 英文：Because we tend to be nice to other people when they please us and nasty when they do not, we are statistically punished for being nice and rewarded for being nasty.
  - 原译：我们往往在别人让我们高兴时对他们好，在别人不让我们高兴时对他们不好；因此，从统计上说，我们对人好会受到惩罚，对人坏反而会得到奖励。
  - 现译：别人让我们高兴，我们往往就对他好；别人不合我们的意，我们往往就对他不好。因此，从统计上说，我们对人好会受到惩罚，对人不好反而会得到奖励。
  - 处理：复核后重写。“在……时”状语夹在主谓之间，代词“我们”“他们”反复出现 复核：nasty 泛指对人不好、不友善，不限于态度凶。“对人凶”把原文概括的一般人际行为窄化了；before 保留的范围更准确。

- 英文：We focus on a player who did very well on the first day, closing with a score of 66.
  - 原译：我们关注一位第 1 天表现非常好的球员，他最后打出了 66 杆。
  - 现译：我们来看一位第 1 天打得非常好的球员，他那天的最终成绩是 66 杆。
  - 处理：Astra 复核通过。“关注一位球员”直译 focus on

- 英文：Uncertain though they are, the following inferences from the score on day 1 are plausible and will be correct more often than they are wrong.
  - 原译：尽管不确定，根据第 1 天的成绩作出的下面这些推断是合理的，而且对的时候会比错的时候多。
  - 现译：根据第 1 天的成绩，可以作出下面这些推断。它们虽然不确定，却是合理的，而且对的时候会比错的时候多。
  - 处理：Astra 复核通过。让步状语照搬句首，“推断”前定语过长

- 英文：This means that in the absence of any other information, your best guess about the players’ score on day 2 should not be a repeat of their performance on day 1.
  - 原译：这意味着，在没有任何其他信息的情况下，你对球员第 2 天成绩的最佳猜测，不应该是他们第 1 天表现的重演。
  - 现译：这意味着，如果没有任何其他信息，你对球员第 2 天成绩的最佳猜测，不应该是照搬他们第 1 天的表现。
  - 处理：Astra 复核通过。“在……的情况下”直译 in the absence of，“表现的重演”直译 a repeat of

- 英文：The golfer who did well on day 1 is likely to be successful on day 2 as well, but less than on the first, because the unusual luck he probably enjoyed on day 1 is unlikely to hold.
  - 原译：第 1 天表现好的球员，第 2 天很可能也会打得不错，但不如第 1 天好，因为他第 1 天很可能享有的那份不寻常的好运，不太可能延续下去。
  - 现译：第 1 天表现好的球员，第 2 天很可能也会打得不错，但不如第 1 天好，因为他第 1 天很可能运气格外好，而这样的好运不太可能延续下去。
  - 处理：Astra 复核通过。“好运”前堆了从句式长定语，“享有好运”直译 enjoyed luck

- 英文：The golfer who did poorly on day 1 will probably be below average on day 2, but will improve, because his probable streak of bad luck is not likely to continue.
  - 原译：第 1 天表现差的球员，第 2 天很可能仍然低于平均水平，但会有所进步，因为他很可能遇到的那一连串坏运气，不太可能继续下去。
  - 现译：第 1 天表现差的球员，第 2 天很可能仍然低于平均水平，但会有所进步，因为他第 1 天很可能碰上了一连串坏运气，而这阵坏运气不太可能延续下去。
  - 处理：复核后重写。“坏运气”前挂着“他很可能遇到的那”长定语 复核：“不太可能一直持续”容易读成坏运气不会长久持续的泛论。原文在预测第 2 天的表现，强调的是前一天的坏运气不太可能延续到第 2 天。

- 英文：We also expect the difference between the two golfers to shrink on the second day, although our best guess is that the first player will still do better than the second.
  - 原译：我们还预计，两位球员之间的差距在第 2 天会缩小，尽管我们的最佳猜测是，第一位球员仍会比第二位打得好。
  - 现译：我们还预计，两位球员之间的差距在第 2 天会缩小，不过我们的最佳猜测仍然是，第一位球员会比第二位打得好。
  - 处理：Astra 复核通过。“尽管”让步从句照搬英文放在主句之后

- 英文：The fact that you observe regression when you predict an early event from a later event should help convince you that regression does not have a causal explanation.
  - 原译：用后发生的事件预测先发生的事件时，你同样能观察到回归；这个事实应该有助于让你相信，回归没有因果解释。
  - 现译：用后发生的事件预测先发生的事件时，你同样能观察到回归；这个事实应该有助于让你相信，回归没有因果解释。
  - 处理：复核后退回原译。“这个事实应该有助于让你相信”直译 The fact … should help convince you 复核：“帮你相信”搭配生硬，没有自然表达 help convince 的劝服作用。

- 英文：Overconfidence and the pressure of meeting high expectations are often offered as explanations.
  - 原译：人们常常用过度自信和不负众望的压力来解释这个魔咒。
  - 现译：人们常常把这个魔咒归因于过度自信，以及不负众望的压力。
  - 处理：复核后重写。“不负众望的压力”搭配生硬，读不出 meeting high expectations 的意思 复核：“满足众人厚望”搭配不当，通常说“满足期望”或“不负厚望”；新增的逗号也割裂了句子。before 的“不负众望的压力”自然且符合原意。

- 英文：Regression to the mean was discovered and named late in the nineteenth century by Sir Francis Galton, a half cousin of Charles Darwin and a renowned polymath.
  - 原译：均值回归是在 19 世纪后期由弗朗西斯·高尔顿爵士发现并命名的。
  - 现译：19 世纪后期，弗朗西斯·高尔顿爵士发现了均值回归，并给它起了名字。
  - 处理：Astra 复核通过。“是……由……发现并命名的”照搬英文被动

- 英文：…which reports measurements of size in successive generations of seeds and in comparisons of the height of children to the height of their parents.
  - 原译：这篇文章报告了对连续几代种子大小的测量，以及子女身高与父母身高的比较。
  - 现译：这篇文章报告了连续几代种子大小的测量结果，还比较了子女和父母的身高。
  - 处理：Astra 复核通过。“报告了对……的测量……的比较”抽象名词堆叠

- 英文：It took Galton several years to work his way from his discovery of filial regression in size to the broader notion that regression inevitably occurs when the correlation between two measures is less than perfect, and he needed the help of the most brilliant statisticians of his time to reach that conclusion.
  - 原译：高尔顿花了好几年时间，才从他发现的子代在大小上的回归，一步步走到一个更普遍的观念：只要两个测量指标之间的相关不完全，回归就必然会发生。而且，为了得出这个结论，他还需要当时最杰出的统计学家的帮助。
  - 现译：高尔顿发现子代在大小上会出现回归之后，花了好几年时间，才逐步形成一个更普遍的认识：只要两个测量指标之间的相关不完全，回归就必然会发生。而且，要得出这个结论，他还得靠当时最杰出的几位统计学家帮忙。
  - 处理：复核后重写。“从他发现的子代在大小上的回归”定语绕口，“需要……的帮助”直译 复核：拆分开头有帮助，但“从这里一步步走到一个更普遍的观念”仍是生硬的直译，应写成逐步形成认识。

- 英文：If all you know about Tom is that he ranks twelfth in weight (well above average), you can infer (statistically) that he is probably older than average and also that he probably consumes more ice cream than other children. If all you know about Barbara is that she is eighty-fifth in piano (far below the average of the group), you can infer that she is likely to be young and that she is likely to practice less than most other children.
  - 原译：如果你对汤姆的全部了解，只是他的体重排第 12（远高于平均），你就可以（从统计上）推断，他的年龄很可能大于平均，他吃的冰激凌也很可能比其他孩子多。如果你对芭芭拉的全部了解，只是她的钢琴水平排第 85（远低于全组的平均），你就可以推断，她很可能年纪小，练琴的时间也很可能比其他大多数孩子少。
  - 现译：如果你只知道汤姆的体重排第 12（远高于平均），就可以（从统计上）推断，他的年龄很可能大于平均，冰激凌也很可能吃得比其他孩子多。如果你只知道芭芭拉的钢琴水平排第 85（远低于全组的平均），就可以推断，她很可能年纪小，练琴的时间也很可能比其他大多数孩子少。
  - 处理：Astra 复核通过。“你对汤姆的全部了解，只是”直译 all you know about Tom is，代词重复

- 英文：When our attention is called to an event, associative memory will look for its cause—more precisely, activation will automatically spread to any cause that is already stored in memory. Causal explanations will be evoked when regression is detected, but they will be wrong because the truth is that regression to the mean has an explanation but does not have a cause.
  - 原译：当我们的注意力被引向某个事件时，联想记忆就会寻找它的原因；更准确地说，激活会自动扩散到记忆中已经存储的任何原因上。察觉到回归时，因果解释就会被唤起，但这些解释都会是错的，因为事实是：均值回归有解释，却没有原因。
  - 现译：某个事件一旦引起我们的注意，联想记忆就会去寻找它的原因；更准确地说，激活会自动扩散到记忆中已经存储的任何原因上。一察觉到回归，脑子里就会冒出因果解释，但这些解释都会是错的，因为事实是：均值回归有解释，却没有原因。
  - 处理：Astra 复核通过。“当……被引向……时”和“就会被唤起”照搬英文被动

- 英文：Our difficulties with the concept of regression originate with both System 1 and System 2.
  - 原译：我们理解回归这个概念时遇到的困难，既来自系统 1，也来自系统 2。
  - 现译：我们难以理解回归这个概念，根源既在系统 1，也在系统 2。
  - 处理：Astra 复核通过。抽象名词“困难”作主语，前面挂着长定语

- 英文：Most readers of such headlines will automatically infer that the energy drink or the cat hugging caused an improvement, but this conclusion is completely unjustified.
  - 原译：这类标题的大多数读者会自动推断，是能量饮料或抱猫带来了好转，但这个结论完全站不住脚。
  - 现译：大多数人读到这类标题，会自动推断是能量饮料或抱猫带来了好转，但这个结论完全站不住脚。
  - 处理：Astra 复核通过。“这类标题的大多数读者”直译 Most readers of such headlines

- 英文：In order to conclude that an energy drink—or any other treatment—is effective, you must compare a group of patients who receive this treatment to a “control group” that receives no treatment (or, better, receives a placebo). The control group is expected to improve by regression alone, and the aim of the experiment is to determine whether the treated patients improve more than regression can explain.
  - 原译：要断定能量饮料（或任何其他疗法）有效，你必须把接受这种疗法的一组患者，和不接受任何治疗（更好的做法是给予安慰剂）的“对照组”进行比较。可以预计，对照组仅凭回归就会好转，实验的目的是确定接受治疗的患者的好转程度，是否超出了回归所能解释的范围。
  - 现译：要断定能量饮料（或任何其他疗法）有效，你必须拿接受这种疗法的一组患者，和一个“对照组”比较，对照组不接受任何治疗（更好的做法是给他们安慰剂）。可以预计，对照组光靠回归就会好转；实验要确定的是，接受治疗的患者好转的幅度，是否超出了回归所能解释的范围。
  - 处理：Astra 复核通过。“对照组”前定语带括号太长，“进行比较”虚化动词，“患者的好转程度”的字连串

- 英文：One of my favorite examples of the errors of intuitive prediction is adapted from Max Bazerman’s excellent text Judgment in Managerial Decision Making:
  - 原译：我最喜欢的直觉预测错误的例子之一，改编自马克斯·巴泽曼的优秀教材《管理决策中的判断》（Judgment in Managerial Decision Making）：
  - 现译：说到直觉预测出错，我最喜欢的例子之一改编自马克斯·巴泽曼的优秀教材《管理决策中的判断》（Judgment in Managerial Decision Making）：
  - 处理：Astra 复核通过。“我最喜欢的直觉预测错误的例子之一”的字连串

- 英文：As Galton painfully discovered, the concept of regression is far from obvious.
  - 原译：正如高尔顿痛苦地发现的那样，回归这个概念一点也不显而易见。
  - 现译：高尔顿吃了不少苦头才发现，回归这个概念一点也不显而易见。
  - 处理：Astra 复核通过。“正如……的那样”直译 As …，“痛苦地发现”直译 painfully discovered

## 第 18 章 驯服直觉预测

- 英文：In our private lives, we forecast our spouse’s reaction to a proposed move or our own future adjustment to a new job.
  - 原译：在私人生活中，我们会预测配偶对一个搬家的提议有什么反应，也会预测自己将来对一份新工作适应得怎么样。
  - 现译：在私人生活中，我们会预测配偶对搬家的提议有什么反应，也会预测自己将来对一份新工作适应得怎么样。
  - 处理：Astra 复核通过。照搬冠词 a，多余的“一个”

- 英文：Some predictive judgments, such as those made by engineers, rely largely on look-up tables, precise calculations, and explicit analyses of outcomes observed on similar occasions.
  - 原译：有些预测性判断，比如工程师作出的判断，主要依靠查表、精确计算，以及对类似场合下观察到的结果所作的明确分析。
  - 现译：有些预测性判断，比如工程师作出的判断，主要依靠查表、精确计算，以及明确分析在类似场合下观察到的结果。
  - 处理：复核后保留改写。“对……所作的……分析”名词化长定语 复核：“明确分析”搭配生硬，把“明确”从分析的性质改成动作的修饰语，反而不如原来的“所作的明确分析”清楚。原来的名词结构没有必要强行拆除。

- 英文：The rapid and automatic judgments and choices of chess masters, fireground commanders, and physicians that Gary Klein has described in Sources of Power and elsewhere illustrate these skilled intuitions, in which a solution to the current problem comes to mind quickly because familiar cues are recognized.
  - 原译：加里·克莱因在《如何作出正确决策》（Sources of Power）和其他著作里描述过国际象棋大师、火场指挥官和医生迅速、自动地作出的判断和选择，这些都是熟练直觉的例子：因为认出了熟悉的线索，眼前这个问题的解决办法很快就浮现在脑中。
  - 现译：国际象棋大师、火场指挥官和医生会迅速、自动地作出判断和选择，加里·克莱因在《如何作出正确决策》（Sources of Power）和其他著作里描述过这些例子，它们说明的就是熟练直觉：因为认出了熟悉的线索，眼前这个问题的解决办法很快就浮现在脑中。
  - 处理：Astra 复核通过。宾语前堆了很长的定语

- 英文：Intuitive judgments can be made with high confidence even when they are based on nonregressive assessments of weak evidence.
  - 原译：即使直觉判断依据的只是对薄弱证据所作的非回归评估，人们也可能带着很高的信心作出这些判断。
  - 现译：即使直觉判断依据的只是对薄弱证据的非回归评估，人们作出这些判断时也可能信心十足。
  - 处理：Astra 复核通过。“所作的”虚化结构，with high confidence 直译成“带着很高的信心”

- 英文：The evaluation of the flimsy evidence of cognitive ability in childhood is substituted as an answer to the question about her college GPA.
  - 原译：对这条反映童年认知能力的单薄证据的评价，被拿来当作答案，回答她大学平均绩点是多少的问题。
  - 现译：这条反映她童年认知能力的证据很单薄，人们却用对它的评价来回答她大学平均绩点是多少的问题。
  - 处理：按复核意见修改。抽象名词作主语，前面挂着一串“的”字定语 复核：拆开后，“十分单薄”与所修饰的“证据”隔得较远；“当作答案，回答……的问题”仍然重复拖沓。

- 英文：Amos and I once asked participants in an experiment to judge descriptions of eight college freshmen, allegedly written by a counselor on the basis of interviews of the entering class.
  - 原译：阿莫斯和我曾经请一项实验的参与者评判八名大学新生的描述，据称这些描述是一位辅导员根据对这届新生的面谈写成的。
  - 现译：阿莫斯和我曾经在一项实验里，请参与者评判对八名大学新生的描述，据称这些描述是一位辅导员根据与这届新生的面谈写成的。
  - 处理：复核后重写。“一项实验的参与者”“根据对……的面谈”照搬英文名词结构 复核：“面谈这届新生”搭配不当，应说“与这届新生面谈”；“面谈后写成”只交代时间先后，遗漏了 on the basis of 所表达的依据关系。

- 英文：The very existence of such a norm is remarkable.
  - 原译：这样一种常态的存在本身就很了不起。
  - 现译：居然存在这样一种常态，这本身就很了不起。
  - 处理：Astra 复核通过。“……的存在”抽象名词作主语

- 英文：There is impressive consensus in such judgments, at least within a culture.
  - 原译：在这类判断上，人们的共识程度令人吃惊，至少在同一种文化内是这样。
  - 现译：在这类判断上，人们的看法一致得惊人，至少在同一种文化内是这样。
  - 处理：Astra 复核通过。“共识程度”抽象名词直译

- 英文：As was the case with Julie, the prediction of the future is not distinguished from an evaluation of current evidence—prediction matches evaluation.
  - 原译：和朱莉的例子一样，对未来的预测没有和对眼前证据的评价区分开来：预测与评价相匹配。
  - 现译：和朱莉的例子一样，预测未来和评价眼前的证据没有区分开来：预测与评价相匹配。
  - 处理：Astra 复核通过。“对……的预测”“对……的评价”名词化结构

- 英文：People are asked for a prediction but they substitute an evaluation of the evidence, without noticing that the question they answer is not the one they were asked.
  - 原译：人们被要求作出预测，却用对证据的评价来替代，而且没有注意到，自己回答的问题和被问到的问题已经不一样了。
  - 现译：人们被要求作预测，却拿对证据的评价来替代，而且没有注意到，自己回答的并不是被问到的那个问题。
  - 处理：Astra 复核通过。“作出”虚化动词，后半句绕成两个问题比较，还多了原文没有的“已经”

- 英文：These findings provide a compelling example of both substitution and intensity matching.
  - 原译：这些发现为替代和强度匹配提供了一个很有说服力的例子。
  - 现译：这些发现是一个很有说服力的例子，同时体现了替代和强度匹配。
  - 处理：Astra 复核通过。“为……提供了一个例子”直译 provide，丢了 both

- 英文：Similarly, if you use childhood achievements to predict grades in college without regressing your predictions toward the mean, you will more often than not be disappointed by the academic outcomes of early readers and happily surprised by the grades of those who learned to read relatively late.
  - 原译：同样，如果你用童年的成就来预测大学成绩，却不让预测向均值回归，那么早早学会阅读的人的学业结果多半会让你失望，而学阅读学得相对晚的人的成绩则会给你惊喜。
  - 现译：同样，如果你用童年的成就来预测大学成绩，却不让预测向均值回归，那么早早学会阅读的人，学业表现多半会让你失望，而学会阅读比较晚的人，成绩则多半会让你惊喜。
  - 处理：复核后重写。“的人的”双“的”连用 复核：“学阅读学得相对晚”仍然重复拗口。more often than not 同时限定“失望”和“惊喜”，后半句也应明确保留这一概率限定。

- 英文：The biases we find in predictions that are expressed on a scale, such as GPA or the revenue of a firm, are similar to the biases observed in judging the probabilities of outcomes.
  - 原译：我们在用数值表达的预测（比如平均绩点或一家公司的收入）中发现的偏差，与判断各种结果的概率时观察到的偏差相似。
  - 现译：有些预测用数值来表达，比如平均绩点或一家公司的收入；我们在这类预测中发现的偏差，与判断各种结果的概率时观察到的偏差相似。
  - 处理：Astra 复核通过。主语前堆了带括号的长定语

- 英文：A preference for unbiased predictions is justified if all errors of prediction are treated alike, regardless of their direction.
  - 原译：如果所有预测错误不论偏向哪个方向都被同等看待，偏好无偏预测就是合理的。
  - 现译：如果我们对所有预测错误一视同仁，不管它们偏向哪个方向，那么偏好无偏预测就是合理的。
  - 处理：Astra 复核通过。照搬被动“被同等看待”

- 英文：It is natural for the associative machinery to match the extremeness of predictions to the perceived extremeness of evidence on which it is based—this is how substitution works.
  - 原译：联想机制很自然地会让预测的极端程度，与预测所依据的证据给人感觉上的极端程度相匹配，替代就是这样起作用的。
  - 现译：证据看上去有多极端，联想机制就很自然地让依据它作出的预测有多极端，替代就是这样起作用的。
  - 处理：Astra 复核通过。“极端程度”抽象名词对抽象名词，“给人感觉上的”生硬

- 英文：Be warned: your intuitions will deliver predictions that are too extreme and you will be inclined to put far too much faith in them.
  - 原译：请注意：你的直觉给出的预测会过于极端，而你会倾向于过分相信它们。
  - 现译：要当心：你的直觉给出的预测会过于极端，而你又很容易过分相信它们。
  - 处理：Astra 复核通过。be inclined to 直译成“会倾向于”，Be warned 语气偏弱

## 第 19 章 理解的错觉

- 英文：The halo effect discussed earlier contributes to coherence, because it inclines us to match our view of all the qualities of a person to our judgment of one attribute that is particularly significant.
  - 原译：前面讨论过的光环效应有助于形成这种连贯，因为它让我们倾向于根据我们对某人一个特别重要的属性的判断，来确定对他所有品质的看法。
  - 现译：前面讨论过的光环效应有助于形成这种连贯，因为我们对一个人某个特别重要的属性下了判断以后，往往会让对他所有品质的看法都与这个判断相符。
  - 处理：Astra 复核通过。“根据我们对某人一个……属性的判断”一串“的”字定语

- 英文：Two creative graduate students in the computer science department at Stanford University come up with a superior way of searching information on the Internet.
  - 原译：斯坦福大学计算机系两名富有创造力的研究生，想出了一种在互联网上搜索信息的更好的方法。
  - 现译：斯坦福大学计算机系两名富有创造力的研究生，想出了一种更好的办法来搜索互联网上的信息。
  - 处理：Astra 复核通过。“一种……的更好的方法”定语过长、“的”字连用

- 英文：On one memorable occasion, they were lucky, which makes the story even more compelling: a year after founding Google, they were willing to sell their company for less than $1 million, but the buyer said the price was too high. Mentioning the single lucky incident actually makes it easier to underestimate the multitude of ways in which luck affected the outcome.
  - 原译：有一回他们走了运，这件事令人难忘，也让这个故事更有说服力：创办谷歌一年后，他们愿意以不到 100 万美元的价格卖掉他们的公司，买方却说价格太高了。提到这一次幸运的插曲，其实反而让人更容易低估运气影响结果的途径之多。
  - 现译：有一回他们走了运，这件事令人难忘，也让这个故事更有说服力：创办谷歌一年后，他们愿意以不到 100 万美元的价格卖掉公司，买方却说价格太高了。提到这一次幸运的插曲，其实反而让人更容易低估运气对结果的影响有多么广泛。
  - 处理：复核后重写。多余的物主代词“他们的”；“途径之多”硬译 the multitude of ways 复核：“低估运气在多少方面影响了结果”搭配生硬，比原来的“低估……的途径之多”更难读；原译也更明确地保留了 multitude 对途径繁多的强调。

- 英文：A detailed history would specify the decisions of Google’s founders, but for our purposes it suffices to say that almost every choice they made had a good outcome.
  - 原译：详细的历史会一一列出谷歌创始人做过的决定，不过就我们的目的而言，只要说他们做的几乎每个选择都有好结果就够了。
  - 现译：如果详细讲述这段历史，就会一一列出谷歌创始人做过的决定，不过对我们这里的讨论来说，只要说他们做的几乎每个选择都有好结果就够了。
  - 处理：复核后重写。for our purposes 直译成“就我们的目的而言” 复核：后半句有所改善，但“详细的历史会一一列出”仍然生硬。history 在这里指历史记述，不是历史本身。

- 英文：Once you adopt a new view of the world (or of any part of it), you immediately lose much of your ability to recall what you used to believe before your mind changed.
  - 原译：一旦你接受了对世界（或者对世界的任何一部分）的新看法，你回忆自己在改变想法之前相信什么的能力，就会立刻失去很大一部分。
  - 现译：一旦你接受了对世界（或者对世界任何一部分）的新看法，要回忆起自己改变想法之前相信什么，就会立刻变得困难得多。
  - 处理：按复核意见修改。“……的能力”长定语加抽象名词作主语 复核：“在很大程度上想不起来”搭配生硬，也没有清楚保留原文强调的“回忆能力大幅减弱”，容易读成已经遗忘了许多旧观念。

- 英文：Because adherence to standard operating procedures is difficult to second-guess, decision makers who expect to have their decisions scrutinized with hindsight are driven to bureaucratic solutions—and to an extreme reluctance to take risks.
  - 原译：按标准操作程序办事，别人很难在事后挑毛病，所以那些预料到自己的决策会被人用后见之明来审视的决策者，就会被迫采取官僚式的办法，变得极其不愿冒险。
  - 现译：按标准操作程序办事，别人很难在事后挑毛病，所以决策者如果预料到自己的决策会被人用后见之明来审视，就会被迫采取官僚式的办法，变得极其不愿冒险。
  - 处理：Astra 复核通过。照搬英文定语从句，主语前定语过长

- 英文：A very generous estimate of the correlation between the success of the firm and the quality of its CEO might be as high as .30, indicating 30% overlap.
  - 原译：对于公司的成功与 CEO 的水平之间的相关，一个非常宽松的估计可能高达 0.30，表示两者有 30% 的重叠。
  - 现译：如果估计得十分乐观，公司的成功与 CEO 的水平之间的相关系数可能高达 0.30，表示两者有 30% 的重叠。
  - 处理：按复核意见修改。“对于……，一个……的估计”照搬英文名词主语 复核：“之间的相关”表达不完整，此处谈具体数值，宜明确为“相关系数”。generous 指估值给得很高，“估计得非常宽松”容易被理解成估算不严谨。

- 英文：How often will you find that the firm with the stronger CEO is the more successful of the two?
  - 原译：你会有多少次发现，CEO 更强的那家公司，也是两家里更成功的那家？
  - 现译：在多大比例的公司对里，你会发现 CEO 更强的那家公司也是两家里更成功的那家？
  - 处理：复核后重写。How often 直译成“你会有多少次发现” 复核：“你会发现……”先作断言，再接“这种情况有多常见”，语气和句法都不顺。原文是在询问这种情况出现的频率。

- 英文：If you expected this value to be higher—and most of us do—then you should take that as an indication that you are prone to overestimate the predictability of the world you live in.
  - 原译：如果你本以为这个数值会更高（我们大多数人都这样以为），那你就应该把这当作一个迹象，说明你容易高估自己所生活的世界的可预测性。
  - 现译：如果你本以为这个数值会更高（我们大多数人都这样以为），那你就应该把这当作一个迹象，说明你容易高估自己所处世界的可预测性。
  - 处理：复核后重写。“所生活的世界的可预测性”“的”字连用加抽象名词 复核：“这个世界有多可预测”生硬，机械拆开“可预测性”反而增加了翻译腔。原来的“世界的可预测性”准确，也更自然。

- 英文：The basic message of Built to Last and other similar books is that good managerial practices can be identified and that good practices will be rewarded by good results.
  - 原译：《基业长青》和其他类似的书传达的基本信息是：好的管理实践是可以识别出来的，而好的实践会得到好结果的回报。
  - 现译：《基业长青》和其他类似的书传达的基本信息是：好的管理实践是可以识别出来的，而且好的实践会换来好的结果。
  - 处理：Astra 复核通过。被动 be rewarded by 硬译成“得到好结果的回报”

- 英文：Knowing the importance of luck, you should be particularly suspicious when highly consistent patterns emerge from the comparison of successful and less successful firms. In the presence of randomness, regular patterns can only be mirages.
  - 原译：知道了运气的重要性，当你从成功公司和不那么成功的公司的比较中看到高度一致的模式时，就应该格外怀疑。在存在随机性的情况下，规律的模式只能是海市蜃楼。
  - 现译：既然知道运气很重要，那么在比较成功和不那么成功的公司时，如果看到了高度一致的模式，就应该格外怀疑。只要有随机性在起作用，规律的模式就只能是海市蜃楼。
  - 处理：Astra 复核通过。“当……的比较中……时”长状语，“在存在……的情况下”套话

- 英文：Stories of how businesses rise and fall strike a chord with readers by offering what the human mind needs: a simple message of triumph and failure that identifies clear causes and ignores the determinative power of luck and the inevitability of regression.
  - 原译：讲述企业兴衰的故事之所以能引起读者共鸣，是因为它们提供了人的心智所需要的东西：一个关于成功与失败的简单信息，它指出明确的原因，忽视运气的决定性力量和回归的必然性。
  - 现译：讲述企业兴衰的故事之所以能引起读者共鸣，是因为它们提供了人的心智所需要的东西：一个关于成败的简单说法，它指出明确的原因，而忽视运气的决定性力量和回归的必然性。
  - 处理：复核后重写。把 that 从句译成多余的代词“它” 复核：“一个……信息”量词不当，“关于成功与失败的简单信息”也仍有直译腔；仅删掉“它”，没有理顺后续“指出”“忽视”的主语。

## 第 20 章 有效性错觉

- 英文：Many decades ago I spent what seemed like a great deal of time under a scorching sun, watching groups of sweaty soldiers as they solved a problem.
  - 原译：几十年前，我曾在灼人的烈日下待过一段似乎很漫长的时间，看着一组又一组汗流浃背的士兵解决一个难题。
  - 现译：几十年前，我曾顶着灼人的烈日，看着一组又一组汗流浃背的士兵解决一个难题，那段时间似乎很漫长。
  - 处理：Astra 复核通过。照搬 spent what seemed like a great deal of time，“待过一段……的时间”定语拖沓

- 英文：When our multiple observations of each candidate converged on a coherent story, we were completely confident in our evaluations and felt that what we had seen pointed directly to the future. The soldier who took over when the group was in trouble and led the team over the wall was a leader at that moment.
  - 原译：当我们对某位候选人的多次观察汇聚成一个连贯的故事时，我们对自己的评估就完全有信心，觉得眼前所见直接指向了未来。小组陷入困境时挺身接手、带领队伍翻过墙的那个士兵，在那一刻就是一位领导者。
  - 现译：对某位候选人的多次观察一旦汇聚成一个连贯的故事，我们就对自己的评估完全有信心，觉得眼前所见直接指向了未来。小组陷入困境时，有个士兵挺身接手，带着大家翻过了墙，那一刻他就是一位领导者。
  - 处理：Astra 复核通过。“当……时”套 when 从句，主语前堆了长定语

- 英文：Because our impressions of how well each soldier had performed were generally coherent and clear, our formal predictions were just as definite.
  - 原译：我们对每个士兵表现好坏的印象通常连贯而清晰，所以我们正式作出的预测也同样确定。
  - 现译：我们对每个士兵表现好坏的印象通常连贯而清晰，所以正式的预测也同样明确。
  - 处理：Astra 复核通过。虚化动词“作出”，多余的“我们”

- 英文：If challenged, however, we were prepared to admit, “But of course anything could happen.” We were willing to make that admission because, despite our definite impressions about individual candidates, we knew with certainty that our forecasts were largely useless.
  - 原译：不过，如果有人提出质疑，我们也准备好承认：“当然，什么事都可能发生。”我们之所以愿意这样承认，是因为尽管对单个候选人有明确的印象，我们却确定无疑地知道，自己的预测基本上没有用。
  - 现译：不过，要是有人提出质疑，我们也愿意承认：“当然，什么事都可能发生。”之所以愿意这样承认，是因为尽管对一个个候选人都有明确的印象，我们心里却清清楚楚地知道，自己的预测基本上没有用。
  - 处理：按复核意见修改。“准备好承认”直译 prepared to，“确定无疑地知道”照搬副词 复核：prepared to admit 表示愿意承认；“随时会承认”不够自然，也把意愿强化成了确定会发生的反应。

- 英文：The evidence that we could not forecast success accurately was overwhelming. Every few months we had a feedback session in which we learned how the cadets were doing at the officer-training school and could compare our assessments against the opinions of commanders who had been monitoring them for some time. The story was always the same: our ability to predict performance at the school was negligible.
  - 原译：证明我们无法准确预测谁能成功的证据十分确凿。每隔几个月，我们会开一次反馈会，了解这些学员在军官学校的表现，并把我们的评估与已经观察了他们一段时间的指挥官的意见作比较。结果每次都一样：我们预测他们在军官学校表现的能力微乎其微。
  - 现译：压倒性的证据表明，我们无法准确预测谁能成功。每隔几个月，我们会开一次反馈会，了解这些学员在军官学校的表现。指挥官们已经观察了他们一段时间，我们可以在会上把自己的评估与指挥官的意见相对照。
  - 处理：按复核意见修改。名词前定语过长，“作比较”，抽象名词“能力”作主语 复核：could compare 表示可以进行对照，“再拿……对照”丢失了这一情态；指挥官观察学员的说明后置后，衔接也较松散。

- 英文：The dismal truth about the quality of our predictions had no effect whatsoever on how we evaluated candidates and very little effect on the confidence we felt in our judgments and predictions about individuals.
  - 原译：我们的预测质量如此糟糕，这个令人沮丧的事实，对我们怎样评估候选人毫无影响，对我们在判断和预测单个候选人时所感到的信心，也几乎没有影响。
  - 现译：我们的预测质量如此糟糕，这个令人沮丧的事实丝毫没有改变我们评估候选人的方式，我们在判断和预测一个个候选人时有多自信，也几乎没受影响。
  - 处理：Astra 复核通过。“所感到的信心”照搬 the confidence we felt，“对……影响”重复

- 英文：The global evidence of our previous failure should have shaken our confidence in our judgments of the candidates, but it did not. It should also have caused us to moderate our predictions, but it did not. We knew as a general fact that our predictions were little better than random guesses, but we continued to feel and act as if each of our specific predictions was valid.
  - 原译：我们过去整体上失败的证据，本应动摇我们对候选人判断的信心，但它没有。它也本应让我们把预测调得温和一些，但也没有。我们知道一个总体事实：我们的预测比随机猜测好不了多少。可是在感觉上和行动上，我们仍然把自己的每一个具体预测都当作有效的。
  - 现译：总体证据表明，我们过去的预测失败了。这本应动摇我们评判候选人时的信心，却没有；也本应让我们作出不那么极端的预测，却同样没有。我们知道一个总体事实：自己的预测比随机猜测好不了多少。可我们仍然觉得自己的每一个具体预测都有效，行动时也仍以此为依据。
  - 处理：按复核意见修改。“……的证据”长定语，代词“它”作主语，“在感觉上和行动上”照搬 feel and act 复核：“把预测调得温和一些”仍然生硬，原意是减少预测的极端程度；“做起事来也照旧如此”没有清楚说明行动时仍把预测当作有效的。

- 英文：Decades later, I can see many of the central themes of my thinking—and of this book—in that old story. Our expectations for the soldiers’ future performance were a clear instance of substitution, and of the representativeness heuristic in particular.
  - 原译：几十年后的今天，我能在那个旧故事里看到我思想中的许多核心主题，它们也是本书的核心主题。我们对士兵未来表现的预期，是替代的一个清楚例子，具体说，是代表性启发式的例子。
  - 现译：几十年后的今天，我能在那段往事里看到我思想中的许多核心主题，它们也是本书的核心主题。我们对士兵未来表现的预期，明显是一种替代，具体说，是代表性启发式在起作用。
  - 处理：Astra 复核通过。“旧故事”直译 old story，“……的一个清楚例子”照搬 a clear instance of

- 英文：This was a clear instance of WYSIATI. We had compelling impressions of the behavior we observed and no good way to represent our ignorance of the factors that would eventually determine how well the candidate would perform as an officer.
  - 原译：这是所见即全部的一个清楚例子。我们对观察到的行为有着令人信服的印象；而对那些最终将决定这位候选人当军官表现如何的因素，我们一无所知，又没有好办法在判断中把这种无知体现出来。
  - 现译：这显然是所见即全部在起作用。我们观察到的行为给我们留下了令人信服的印象；至于最终会决定这位候选人当军官表现如何的那些因素，我们一无所知，又没有好办法在判断中把这种无知体现出来。
  - 处理：复核后重写。“……的一个清楚例子”，“有着……的印象” 复核：compelling 表示令人信服，“不容置疑”把印象的说服力强化成了不可质疑的确定性，程度超过原文。

- 英文：I knew so little about finance that I did not even know what to ask him, but I remember one exchange. “When you sell a stock,” I asked, “who buys it?” He answered with a wave in the vague direction of the window, indicating that he expected the buyer to be someone else very much like him. That was odd: What made one person buy and the other sell?
  - 原译：我对金融所知甚少，甚至不知道该问他什么，但我记得有一段对话。“你卖出一只股票的时候，”我问，“是谁买走了它？”他朝窗户的方向随手一挥，意思是他认为买家是另一个和他非常相像的人。这就怪了：是什么让一个人买入，另一个人卖出？
  - 现译：我对金融所知甚少，甚至不知道该问他什么，但有一段对话我至今记得。“你卖股票的时候，”我问，“是谁在买？”他朝窗户的方向随手一挥，意思是他料想买家是另一个和他非常相像的人。这就怪了：为什么一个人买，另一个人卖？
  - 处理：Astra 复核通过。口语里多余的“一只”“它”，“是什么让……”照搬 What made

- 英文：For most of them, that belief is an illusion.
  - 原译：对他们中的大多数人来说，这种信念是一种错觉。
  - 现译：他们大多数人的这种信念，都是一种错觉。
  - 处理：Astra 复核通过。“对……来说”照搬 For ...

- 英文：In its broad outlines, the standard theory of how the stock market works is accepted by all the participants in the industry.
  - 原译：关于股市如何运作，有一套标准理论，它的大致轮廓得到了这个行业所有参与者的认可。
  - 现译：关于股市如何运作，有一套标准理论，这个行业的所有参与者都认同它的基本观点。
  - 处理：按复核意见修改。“得到了……的认可”照搬被动 复核：“认可它的大致轮廓”仍是生硬搭配。原文说的是业内所有参与者都接受这套理论的基本观点，并非认可一个轮廓。

- 英文：Odean began by studying the trading records of 10,000 brokerage accounts of individual investors spanning a seven-year period.
  - 原译：奥迪恩首先研究了 10,000 个个人投资者经纪账户在七年间的交易记录。
  - 现译：奥迪恩首先研究了个人投资者的 10,000 个经纪账户，查看它们七年间的交易记录。
  - 处理：Astra 复核通过。名词前修饰语层层堆叠

- 英文：By these actions the investor revealed that he (most of the investors were men) had a definite idea about the future of the two stocks: he expected the stock that he chose to buy to do better than the stock he chose to sell.
  - 原译：投资者用这些行动表明，他（这些投资者大多是男性）对这两只股票的前景有明确的看法：他预期自己选择买入的股票会比选择卖出的那只表现更好。
  - 现译：投资者这样做，就表明他（这些投资者大多是男性）对这两只股票的前景有明确的看法：他预期自己选择买入的股票会比选择卖出的那只表现更好。
  - 处理：Astra 复核通过。“用这些行动表明”直译 By these actions

- 英文：The results were unequivocally bad. On average, the shares that individual traders sold did better than those they bought, by a very substantial margin: 3.2 percentage points per year, above and beyond the significant costs of executing the two trades.
  - 原译：结果毫无疑问是糟糕的。平均而言，个人交易者卖出的股票比他们买入的表现更好，而且差距相当大：每年高出 3.2 个百分点，这还没算上执行这两笔交易本身相当可观的成本。
  - 现译：结果毫无疑问很糟糕。平均而言，个人交易者卖出的股票比他们买入的表现更好，而且差距相当大：每年高出 3.2 个百分点，这还没算上做这两笔交易本身就要付出的可观成本。
  - 处理：Astra 复核通过。“是糟糕的”判断句，“执行交易”直译 executing

- 英文：It is important to remember that this is a statement about averages: some individuals did much better, others did much worse.
  - 原译：要记住，这是关于平均水平的说法：有些人的表现好得多，另一些人则差得多。
  - 现译：要记住，这里说的是平均水平：有些人的表现好得多，另一些人则差得多。
  - 处理：Astra 复核通过。“关于……的说法”直译 a statement about

- 英文：In a paper titled “Trading Is Hazardous to Your Wealth,” they showed that, on average, the most active traders had the poorest results, while the investors who traded the least earned the highest returns.
  - 原译：在一篇题为《交易有损你的财富》（Trading Is Hazardous to Your Wealth）的论文中，他们表明，平均而言，交易最活跃的人结果最差，交易最少的投资者收益最高。
  - 现译：在一篇题为《交易有损你的财富》（Trading Is Hazardous to Your Wealth）的论文中，他们的研究表明，平均而言，交易最活跃的人表现最差，而交易最少的投资者收益最高。
  - 处理：按复核意见修改。“他们表明”直译 they showed 复核：此处 showed 是报告研究结果，“他们证明”措辞偏强，搭配也不如“他们的研究表明”自然。

- 英文：In another paper, titled “Boys Will Be Boys,” they showed that men acted on their useless ideas significantly more often than women, and that as a result women achieved better investment results than men.
  - 原译：在另一篇题为《男孩终归是男孩》（Boys Will Be Boys）的论文中，他们表明，男性根据自己那些无用的想法采取行动的次数明显多于女性，结果女性的投资成绩比男性好。
  - 现译：在另一篇题为《男孩终归是男孩》（Boys Will Be Boys）的论文中，他们的研究表明，男性把自己那些无用的想法付诸行动的次数明显多于女性，因此女性的投资成绩比男性好。
  - 处理：按复核意见修改。“根据……采取行动”直译 acted on 复核：“付诸行动”的改写自然，但把 showed 改为“证明”强化了论断，宜用“研究表明”。

- 英文：Of course, there is always someone on the other side of each transaction; in general, these are financial institutions and professional investors, who are ready to take advantage of the mistakes that individual traders make in choosing a stock to sell and another stock to buy.
  - 原译：当然，每笔交易的另一方总有人；一般来说，他们是金融机构和专业投资者，随时准备利用个人交易者在选择卖出哪只股票、买入哪只股票时犯的错误。
  - 现译：当然，每笔交易总有另一方；一般来说，另一方是金融机构和专业投资者，他们随时准备利用个人交易者在选择卖出哪只股票、买入哪只股票时犯的错误。
  - 处理：复核后重写。“另一方总有人”照搬 there is someone on the other side 的语序 复核：“有人站在另一边”仍机械沿用了英文的空间表达，容易让人联想到立场对立；这里指交易的另一方。

- 英文：Unfortunately for them, recent winners tend to do better than recent losers in the short run, so individuals sell the wrong stocks. They also buy the wrong stocks. Individual investors predictably flock to companies that draw their attention because they are in the news.
  - 原译：对他们来说不幸的是，短期内，近期的赢家往往比近期的输家表现更好，所以个人投资者卖错了股票。他们也买错了股票。可以预见，个人投资者会一窝蜂地涌向那些因为上了新闻而吸引他们注意的公司。
  - 现译：对他们不利的是，在短期内，近期的赢家往往比近期的输家表现更好，所以个人投资者卖错了股票。他们也买错了股票。可以预见，哪家公司上了新闻、引起了他们的注意，个人投资者就会一窝蜂地涌过去。
  - 处理：Astra 复核通过。“对他们来说不幸的是”直译 Unfortunately for them，“公司”前定语过长

- 英文：Where there is skill, however, the rankings will be more stable.
  - 原译：而在有技能的地方，排名会更稳定。
  - 现译：而只要存在技能，排名就会更稳定。
  - 处理：Astra 复核通过。“在有技能的地方”直译 Where there is

- 英文：I had been invited to speak to a group of investment advisers in a firm that provided financial advice and other services to very wealthy clients. I asked for some data to prepare my presentation and was granted a small treasure: a spreadsheet summarizing the investment outcomes of some twenty-five anonymous wealth advisers, for each of eight consecutive years.
  - 原译：一家为非常富有的客户提供理财建议和其他服务的公司，邀请我给他们的一群投资顾问做演讲。为了准备演讲，我要了一些数据，结果得到了一份小小的宝藏：一张电子表格，汇总了大约二十五位匿名财富顾问连续八年中每一年的投资业绩。
  - 现译：有一家公司为非常富有的客户提供理财建议和其他服务，他们邀请我给公司的一群投资顾问做演讲。为了准备演讲，我要了一些数据，结果得到了一份小小的宝藏：一张电子表格，汇总了大约二十五位匿名财富顾问连续八年的逐年投资业绩。
  - 处理：Astra 复核通过。主语“公司”前定语过长，“连续八年中每一年的”的字连串

- 英文：Facts that challenge such basic assumptions—and thereby threaten people’s livelihood and self-esteem—are simply not absorbed. The mind does not digest them. This is particularly true of statistical studies of performance, which provide base-rate information that people generally ignore when it clashes with their personal impressions from experience.
  - 原译：挑战这类基本假设的事实，因为会威胁到人们的生计和自尊，根本不会被吸收。心智消化不了它们。业绩的统计研究尤其如此：这类研究提供的是基础比率信息，而当这类信息与人们从经验中得来的个人印象相冲突时，人们通常会忽视它。
  - 现译：有些事实挑战了这类基本假设，也因此威胁到人们的生计和自尊，人们根本不会吸收这样的事实。心智消化不了它们。关于业绩的统计研究尤其如此：这类研究提供的是基础比率信息，一旦它和人们从经验中得来的个人印象相冲突，人们通常就会忽视它。
  - 处理：Astra 复核通过。长定语主语加被动“不会被吸收”，“而当……时”

- 英文：Their own experience of exercising careful judgment on complex problems was far more compelling to them than an obscure statistical fact.
  - 原译：他们自己在复杂问题上审慎判断的亲身经验，对他们来说远比一个晦涩的统计事实更有说服力。
  - 现译：他们亲自在复杂问题上作过审慎的判断，在他们看来，这种经验远比一个晦涩的统计事实更有说服力。
  - 处理：Astra 复核通过。抽象名词“经验”作主语，前面定语过长

- 英文：What you learned about the Müller-Lyer illusion did not change the way you see the lines, but it changed your behavior. You now know that you cannot trust your impression of the length of lines that have fins appended to them, and you also know that in the standard Müller-Lyer display you cannot trust what you see.
  - 原译：你对缪勒-莱尔错觉的了解，并没有改变你看那两条线的方式，却改变了你的行为。你现在知道，对于两端加了短斜线的线段，你不能相信自己对它们长度的印象；你也知道，在标准的缪勒-莱尔图形里，你不能相信自己看到的东西。
  - 现译：你知道了缪勒-莱尔错觉是怎么回事，这并没有改变那两条线在你眼中的样子，却改变了你的行为。
  - 处理：复核后重写。抽象名词“了解”作主语，“对于……”和代词“它们” 复核：the way you see the lines 指线条在眼中呈现的样子，而不是观看的方法。“看那两条线的方式”容易与后面的行为变化混淆，这一问题在旧译中也存在。

- 英文：In contrast, when my colleagues and I in the army learned that our leadership assessment tests had low validity, we accepted that fact intellectually, but it had no impact on either our feelings or our subsequent actions. The response we encountered in the financial firm was even more extreme. I am convinced that the message that Thaler and I delivered to both the executives and the portfolio managers was instantly put away in a dark corner of memory where it would cause no damage.
  - 原译：相比之下，我和军队里的同事得知我们的领导力评估测试有效性很低时，我们在理智上接受了这个事实，但它对我们的感受和之后的行动都没有任何影响。我们在那家金融公司遇到的反应更加极端。我相信，塞勒和我向高管和投资组合经理们传达的信息，立刻就被放进了记忆里一个黑暗的角落，在那里它不会造成任何损害。
  - 现译：相比之下，我和军队里的同事得知自己的领导力评估测试有效性很低，在理智上接受了这个事实，可它丝毫没有影响我们的感受，也没有影响我们后来的行动。我们在那家金融公司遇到的反应更加极端。我确信，塞勒和我向高管和投资组合经理们传达的信息，立刻就被塞进了记忆里一个黑暗的角落，在那儿不会造成任何损害。
  - 处理：Astra 复核通过。“……时，我们”主语重复，“在那里它”照搬 where it 从句

- 英文：Why do investors, both amateur and professional, stubbornly believe that they can do better than the market, contrary to an economic theory that most of them accept, and contrary to what they could learn from a dispassionate evaluation of their personal experience?
  - 原译：为什么投资者，无论业余的还是专业的，都固执地相信自己能跑赢市场？
  - 现译：为什么投资者不论业余还是专业，都固执地相信自己能跑赢市场？
  - 处理：Astra 复核通过。照搬英文的插入语，用逗号隔开

- 英文：Our understanding of cognitive ease and associative coherence locates subjective confidence firmly in System 1.
  - 原译：根据我们对认知放松和联想一致性的理解，主观信心牢牢地属于系统 1。
  - 现译：按我们对认知放松和联想一致性的理解，主观信心无疑属于系统 1。
  - 处理：Astra 复核通过。“牢牢地属于”直译 firmly

- 英文：Finally, the illusions of validity and skill are supported by a powerful professional culture.
  - 原译：最后，有效性错觉和技能错觉还得到一种强大的职业文化的支撑。
  - 现译：最后，支撑有效性错觉和技能错觉的，还有一种强大的职业文化。
  - 处理：Astra 复核通过。“得到……的支撑”被动

- 英文：The idea that the future is unpredictable is undermined every day by the ease with which the past is explained.
  - 原译：“未来不可预测”这个观点每天都在被削弱，因为解释过去是那么容易。
  - 现译：过去解释起来那么容易，这每天都在削弱“未来不可预测”这个观点。
  - 处理：Astra 复核通过。“在被削弱”被动句

- 英文：The illusion that we understand the past fosters overconfidence in our ability to predict the future.
  - 原译：以为自己理解了过去，这种错觉助长了我们对自己预测未来能力的过度自信。
  - 现译：我们以为自己理解了过去，这种错觉助长了过度自信，让我们高估自己预测未来的能力。
  - 处理：Astra 复核通过。“对自己预测未来能力的过度自信”的字长定语

- 英文：The often-used image of the “march of history” implies order and direction. Marches, unlike strolls or walks, are not random. We think that we should be able to explain the past by focusing on either large social movements and cultural and technological developments or the intentions and abilities of a few great men. The idea that large historical events are determined by luck is profoundly shocking, although it is demonstrably true.
  - 原译：人们常用“历史的行进”（march of history）这个说法，它意味着秩序和方向。行进和闲逛、散步不同，它不是随意的。我们认为，自己应该能够解释过去，办法是关注大规模的社会运动以及文化和技术的发展，或者关注少数伟人的意图和能力。重大历史事件由运气决定，这个想法令人深感震惊，尽管它可以被证明是真的。
  - 现译：人们常用“历史的行进”（march of history）这个说法，它暗含着秩序和方向。行进和闲逛、散步不同，它不是随意的。我们认为，只要着眼于大规模的社会运动以及文化和技术的发展，或者着眼于少数伟人的意图和能力，自己就应该能够解释过去。说重大历史事件由运气决定，这个想法令人深感震惊，尽管可以证明它是真的。
  - 处理：Astra 复核通过。“办法是”硬拆 by 短语，“可以被证明”被动

- 英文：He also asked the experts how they reached their conclusions, how they reacted when proved wrong, and how they evaluated evidence that did not support their positions.
  - 原译：他还问这些专家是怎样得出结论的，被证明错了时有什么反应，又是怎样评估不支持自己立场的证据的。
  - 现译：他还问这些专家是怎样得出结论的，事实证明自己错了时有什么反应，又是怎样评估不支持自己立场的证据的。
  - 处理：Astra 复核通过。“被证明错了”被动

- 英文：Even in the region they knew best, experts were not significantly better than nonspecialists.
  - 原译：即使在他们最了解的地区，专家也并不比非专业人士明显更好。
  - 现译：即使在自己最了解的地区，专家也没有明显强过非专业人士。
  - 处理：Astra 复核通过。“并不比……明显更好”照搬 not significantly better than

- 英文：The reason is that the person who acquires more knowledge develops an enhanced illusion of her skill and becomes unrealistically overconfident.
  - 原译：原因在于，获得更多知识的人，对自己技能的错觉也会增强，变得不切实际地过度自信。
  - 现译：原因在于，一个人知识多了，对自己技能的错觉也会增强，过度自信到不切实际的地步。
  - 处理：Astra 复核通过。“不切实际地过度自信”照搬副词修饰

- 英文：“In this age of academic hyperspecialization, there is no reason for supposing that contributors to top journals—distinguished political scientists, area study specialists, economists, and so on—are any better than journalists or attentive readers of The New York Times in ‘reading’ emerging situations.”
  - 原译：“在这个学术高度专业化的时代，没有理由认为，那些在顶级期刊上发表文章的人（杰出的政治学家、区域研究专家、经济学家等等），在‘解读’正在出现的局势方面，会比记者或《纽约时报》的细心读者更强。”
  - 现译：“在这个学术高度专业化的时代，没有理由认为，那些在顶级期刊上发表文章的人（杰出的政治学家、区域研究专家、经济学家等等），在‘解读’正在出现的局势时，会比记者或《纽约时报》的细心读者更强。”
  - 处理：Astra 复核通过。“在……方面”

- 英文：Two hedgehogs on different sides of an issue, each attacking the idiotic ideas of the adversary, make for a good show.
  - 原译：在同一个问题上站在对立两边的两只刺猬，各自攻击对方的愚蠢观点，就能凑成一档好节目。
  - 现译：两只刺猬在同一个问题上各站一边，互相攻击对方的愚蠢观点，就能凑成一档好节目。
  - 处理：Astra 复核通过。主语前定语过长

- 英文：Instead the foxes recognize that reality emerges from the interactions of many different agents and forces, including blind luck, often producing large and unpredictable outcomes.
  - 原译：狐狸认识到，现实是从许多不同的行动者和力量的相互作用中产生的，其中也包括纯粹的运气，而这种相互作用常常带来重大的、无法预测的结果。
  - 现译：狐狸认识到，现实产生于许多不同的行动者和力量的相互作用，其中也包括纯粹的运气，这种相互作用常常带来重大而无法预测的结果。
  - 处理：Astra 复核通过。“是从……中产生的”框式结构，多余的“而”

- 英文：But they are less likely than hedgehogs to be invited to participate in television debates.
  - 原译：但和刺猬相比，他们被邀请参加电视辩论的可能性更小。
  - 现译：但和刺猬相比，他们更不容易被请去参加电视辩论。
  - 处理：Astra 复核通过。抽象名词“可能性”作主语

- 英文：The second is that high subjective confidence is not to be trusted as an indicator of accuracy (low confidence could be more informative).
  - 原译：第二个教训是，不能把很高的主观信心当作准确性的指标来信任（低信心可能反而更能说明问题）。
  - 现译：第二个教训是，很高的主观信心并不是准确性的可靠指标（低信心可能反而更能说明问题）。
  - 处理：按复核意见修改。“当作……来信任”照搬 trusted as 复核：原文说不能信赖高主观信心这一指标；删去“信任”后变成完全不能作为指标，丢失了可靠性这一限定。

- 英文：But we should not expect performance in officer training and in combat to be predictable from behavior on an obstacle field—behavior both on the test and in the real world is determined by many factors that are specific to the particular situation.
  - 原译：但我们不应该指望，根据一个人在障碍场上的表现，就能预测他在军官培训和战斗中的表现：无论是测试中的行为，还是现实世界中的行为，都由许多特定于具体情境的因素决定。
  - 现译：但我们不应该指望，根据一个人在障碍场上的表现，就能预测他在军官培训和战斗中的表现：无论是测试中的行为，还是现实世界中的行为，都取决于各自情境特有的许多因素。
  - 处理：按复核意见修改。“特定于”直译 specific to 复核：“许多具体情境特有的因素”修饰关系有歧义，容易把“许多”理解为修饰“具体情境”；原文强调的是各自情境特有的因素有很多。

- 英文：You should expect little or nothing from Wall Street stock pickers who hope to be more accurate than the market in predicting the future of prices. And you should not expect much from pundits making long-term forecasts—although they may have valuable insights into the near future.
  - 原译：对于那些希望比市场更准确地预测价格走势的华尔街选股人，你只能抱很低的期望，甚至根本不该抱期望。对于作长期预测的评论家，你也不应该期望太多，尽管他们对近期的未来可能有宝贵的见解。
  - 现译：对那些希望比市场更准确地预测价格走势的华尔街选股人，你只能抱很低的期望，甚至根本不该抱期望。
  - 处理：按复核意见修改。“对于那些……的”引出长定语，“近期的未来”直译 near future 复核：原文限定的是那些希望比市场预测得更准确的华尔街选股人；改写将其变成对所有华尔街选股人的断言，扩大了范围。

- 英文：“She has a coherent story that explains all she knows, and the coherence makes her feel good.”
  - 原译：“她有一个连贯的故事，能解释她知道的一切，而这种连贯让她感觉很好。”
  - 现译：“她有个连贯的故事，能解释她知道的一切，这种连贯让她感觉很好。”
  - 处理：Astra 复核通过。口语里多余的“一个”和连接词“而”

- 英文：“She is a hedgehog. She has a theory that explains everything, and it gives her the illusion that she understands the world.”
  - 原译：“她是只刺猬。她有一套能解释一切的理论，这让她产生了一种错觉，以为自己理解这个世界。”
  - 现译：“她是只刺猬。她有一套理论能解释一切，这让她产生错觉，以为自己看懂了这个世界。”
  - 处理：Astra 复核通过。口语里的前置定语和“产生了一种错觉”书面腔

## 第 21 章 直觉与公式

- 英文：Meehl reported generally similar results across a variety of other forecast outcomes, including violations of parole, success in pilot training, and criminal recidivism.
  - 原译：米尔还报告说，在其他各种预测结果上，包括是否违反假释规定、飞行员训练能否成功以及罪犯是否再犯，结果也大体相似。
  - 现译：米尔还报告说，预测其他各种结果时，包括是否违反假释规定、飞行员训练能否成功以及罪犯是否再犯，情况也大体相似。
  - 处理：Astra 复核通过。“在……预测结果上”照搬 across 结构，“结果”前后重复

- 英文：The Princeton economist and wine lover Orley Ashenfelter has offered a compelling demonstration of the power of simple statistics to outdo world-renowned experts.
  - 原译：普林斯顿大学的经济学家、葡萄酒爱好者奥利·阿申费尔特，令人信服地展示了简单的统计方法胜过世界知名专家的威力。
  - 现译：普林斯顿大学的经济学家、葡萄酒爱好者奥利·阿申费尔特，令人信服地展示了简单统计方法的威力：它能胜过世界知名的专家。
  - 处理：Astra 复核通过。“胜过……的威力”，名词前定语太长

- 英文：In a famous thought experiment, he described a formula that predicts whether a particular person will go to the movies tonight and noted that it is proper to disregard the formula if information is received that the individual broke a leg today.
  - 原译：在一个著名的思想实验里，他描述了一个预测某人今晚会不会去看电影的公式，并指出，如果得到消息说这个人今天摔断了腿，那么不理会这个公式是恰当的。
  - 现译：在一个著名的思想实验里，他描述了一个公式，用来预测某人今晚会不会去看电影，并指出，如果得知这个人今天摔断了腿，那么不理会这个公式是恰当的。
  - 处理：复核后重写。“……是恰当的”直译 it is proper to，“公式”前定语过长 复核：“理应不去理会”重复、绕口，也比原文“这样做是恰当的”语气更强。

- 英文：The prospects of a convict being granted parole may change significantly during the time that elapses between successive food breaks in the parole judges’ schedule.
  - 原译：一个犯人获得假释的希望，可能在假释法官日程中两次用餐休息之间的那段时间里发生很大的变化。
  - 现译：从假释法官日程里的一次用餐休息到下一次用餐休息，犯人获得假释的希望可能会发生很大的变化。
  - 处理：Astra 复核通过。多余的“一个”，“在……之间的那段时间里”长状语照搬英文

- 英文：When predictability is poor—which it is in most of the studies reviewed by Meehl and his followers—inconsistency is destructive of any predictive validity.
  - 原译：当可预测性很低时（米尔和他的追随者所回顾的大多数研究都是如此），不一致会毁掉任何预测有效性。
  - 现译：可预测性很低时（米尔和他的追随者回顾的研究大多如此），不一致会让预测完全失去有效性。
  - 处理：Astra 复核通过。“当……时”，“毁掉任何预测有效性”直译 any

- 英文：The evidence is fragmentary, but there are solid grounds for a conjecture: conducting an interview is likely to diminish the accuracy of a selection procedure, if the interviewers also make the final admission decisions. Because interviewers are overconfident in their intuitions, they will assign too much weight to their personal impressions and too little weight to other sources of information, lowering validity. Similarly, the experts who evaluate the quality of immature wine to predict its future have a source of information that almost certainly makes things worse rather than better: they can taste the wine.
  - 原译：证据虽然零散，但有充分的理由作出这样的推测：如果面试官同时也作最终的录取决定，那么进行面试很可能会降低选拔程序的准确性。由于面试官对自己的直觉过度自信，他们会给个人印象太多的权重，给其他信息来源太少的权重，从而降低有效性。同样，评估新酒品质来预测它将来如何的专家，有一个信息来源几乎肯定会让事情变得更糟而不是更好：他们能品尝这些酒。
  - 现译：证据虽然零散，但有充分的理由推测：如果最终的录取决定也由面试官来作，那么面试很可能会降低选拔程序的准确性。面试官对自己的直觉过度自信，所以给个人印象的权重会太大，给其他信息来源的权重会太小，有效性也就降低了。同样，专家评估新酒的品质、预测它将来如何时，有一个信息来源几乎肯定会帮倒忙：他们能尝到这些酒。
  - 处理：Astra 复核通过。“作出这样的推测”“进行面试”虚化动词，“给……太多的权重”，“专家”前定语过长，“更糟而不是更好”直译

- 英文：However, Dawes observed that the complex statistical algorithm adds little or no value.
  - 原译：然而道斯注意到，复杂的统计算法增加的价值很少，甚至没有。
  - 现译：然而道斯注意到，这种复杂的统计算法几乎没有增加什么价值。
  - 处理：Astra 复核通过。“很少，甚至没有”逐字照搬 little or no

- 英文：A formula that combines these predictors with equal weights is likely to be just as accurate in predicting new cases as the multiple-regression formula that was optimal in the original sample.
  - 原译：用相等的权重把这些预测因子组合起来的公式，预测新个案时很可能和多元回归公式一样准确，哪怕后者在原始样本中是最优的。
  - 现译：用相等的权重把这些预测因子组合起来，得到的公式在预测新个案时，很可能和多元回归公式一样准确，尽管后者在原始样本中是最优的。
  - 处理：按复核意见修改。主语“……组合起来的公式”定语太长 复核：沿用了“哪怕”，容易把原文已经确定的“在原始样本中最优”读成假设条件，应使用事实性的让步表达。

- 英文：Simple equally weighted formulas based on existing statistics or on common sense are often very good predictors of significant outcomes.
  - 原译：以现有的统计数据或常识为基础、各项权重相等的简单公式，常常能很好地预测重要的结果。
  - 现译：以现有的统计数据或常识为基础，给各项相等的权重，这样的简单公式常常能很好地预测重要的结果。
  - 处理：Astra 复核通过。主语前堆了一串修饰

- 英文：Clearly, they were in the grip of an illusion of skill in terms of their ability to make long-term predictions.
  - 原译：显然，对于自己作长期预测的能力，他们陷入了一种技能错觉。
  - 现译：显然，说到自己作长期预测的能力，他们陷入了技能错觉。
  - 处理：Astra 复核通过。“对于……”句式，多余的“一种”

- 英文：The prejudice against algorithms is magnified when the decisions are consequential.
  - 原译：当决定事关重大时，对算法的偏见就会放大。
  - 现译：决定事关重大时，人们对算法的偏见就会放大。
  - 处理：Astra 复核通过。“当……时”照搬 when 从句

- 英文：We are increasingly exposed to guidelines that have the form of simple algorithms, such as the ratio of good and bad cholesterol levels we should strive to attain.
  - 原译：我们越来越多地接触到以简单算法的形式出现的指导原则，比如我们应该努力达到的好胆固醇与坏胆固醇水平的比值。
  - 现译：我们越来越常接触到一些指导原则，它们以简单算法的形式呈现，比如告诉我们应努力让好胆固醇与坏胆固醇的水平之比达到多少。
  - 处理：按复核意见修改。“以……的形式出现的指导原则”“我们应该努力达到的……比值”定语过长 复核：“比如……水平之比，我们应该努力达到多少”衔接断裂，使目标比值变成悬空的问句，“我们达到比值”的搭配也不自然。

- 英文：Another lesson I learned from Meehl was that we should abandon the procedure in which the interviewers’ global evaluations of the recruit determined the final decision.
  - 原译：我从米尔那里学到的另一个教训是，我们应该放弃由面谈官对新兵的总体评价来决定最终结果的做法。
  - 现译：我从米尔那里学到的另一个教训是：让面谈官对新兵的总体评价来决定最终结果，这种做法我们应该放弃。
  - 处理：Astra 复核通过。整个定语从句塞在“做法”前面

- 英文：I made up a list of six characteristics that appeared relevant to performance in a combat unit, including “responsibility,” “sociability,” and “masculine pride.”
  - 原译：我列出了六项看起来与在作战部队中的表现有关的特征，包括“责任心”“社交性”和“男子汉的自尊”。
  - 现译：我列出了六项特征，它们看起来与在作战部队中的表现有关，包括“责任心”“社交性”和“男子汉的自尊”。
  - 处理：Astra 复核通过。“特征”前定语过长

- 英文：By focusing on standardized, factual questions, I hoped to combat the halo effect, where favorable first impressions influence later judgments.
  - 原译：我希望借助标准化的事实性问题，来对抗光环效应，也就是良好的第一印象影响之后的判断。
  - 现译：我希望把重点放在标准化的事实性问题上，以此对抗光环效应，也就是良好的第一印象会影响后来的判断。
  - 处理：Astra 复核通过。“影响之后的判断”直译 later judgments，容易读成“影响之后”

- 英文：The sum of our six ratings predicted soldiers’ performance much more accurately than the global evaluations of the previous interviewing method, although far from perfectly.
  - 原译：我们六项评分的总和对士兵表现的预测，比以前那种面谈方法的总体评价准确得多，虽然离完美还差得很远。
  - 现译：用我们六项评分的总和来预测士兵的表现，比用以前那种面谈方法的总体评价准确得多，不过离完美还差得很远。
  - 处理：Astra 复核通过。抽象名词短语“……对士兵表现的预测”作主语

- 英文：I learned from this finding a lesson that I have never forgotten: intuition adds value even in the justly derided selection interview, but only after a disciplined collection of objective information and disciplined scoring of separate traits.
  - 原译：从这个发现中，我学到了一个至今没有忘记的教训：即使在理应受到嘲笑的选拔面谈中，直觉也能增加价值，但前提是先严格按规矩收集客观信息，再严格按规矩给各项特质分别打分。
  - 现译：从这个发现中，我学到了一个至今没有忘记的教训：即使在理应受到嘲笑的选拔面谈中，直觉也能增加价值，但前提是先严格按规矩收集客观信息，再严格按规矩给各项特质分别打分。
  - 处理：复核后退回原译。“理应受到嘲笑的选拔面谈”直译 justly derided 复核：将简短的让步修饰扩成“受人嘲笑，这是它应得的”，语气显得刻意而生硬，也拖延了“直觉仍有价值”这一主旨，中文不如 before 紧凑。

- 英文：The message of this chapter is readily applicable to tasks other than making manpower decisions for an army.
  - 原译：这一章的道理，很容易用到为军队作人事决定以外的任务上。
  - 现译：这一章的道理，不仅适用于军队的人事决策，也很容易用到其他任务上。
  - 处理：按复核意见修改。“为军队作人事决定以外的任务”定语过长 复核：“这一章的道理，除了为军队作人事决定”主谓搭配不当；“道理”不能作决定，应明确是道理适用于这些任务。

## 第 22 章 专家直觉：什么时候可以相信它？

- 英文：Especially when the original critique is sharply worded, the reply and the rejoinder are often exercises in what I have called sarcasm for beginners and advanced sarcasm. The replies rarely concede anything to a biting critique, and it is almost unheard of for a rejoinder to admit that the original critique was misguided or erroneous in any way.
  - 原译：尤其是在最初的批评措辞尖锐的时候，答复和再回应往往就成了我所说的“初级挖苦”和“高级挖苦”的练习。答复很少会向尖刻的批评作出任何让步；至于再回应承认最初的批评有哪怕一点不当或错误，几乎闻所未闻。
  - 现译：尤其是最初的批评措辞尖锐时，答复和再回应往往就变成我所说的“初级挖苦”和“高级挖苦”。面对尖刻的批评，答复很少会有任何让步；再回应要是承认最初的批评有哪怕一点不当或错误，那几乎是闻所未闻的事。
  - 处理：Astra 复核通过。“……的练习”直译 exercises in，“作出任何让步”，“至于……几乎闻所未闻”主语悬空

- 英文：In especially tense situations, the research is moderated by an arbiter.
  - 原译：在气氛特别紧张的情况下，研究由一位仲裁人主持。
  - 现译：气氛特别紧张时，研究由一位仲裁人主持。
  - 处理：Astra 复核通过。“在……的情况下”套话

- 英文：My most satisfying and productive adversarial collaboration was with Gary Klein, the intellectual leader of an association of scholars and practitioners who do not like the kind of work I do.
  - 原译：克莱因是一个由学者和实践者组成的群体的思想领袖，这些人不喜欢我做的那类工作。
  - 现译：有一群学者和实践者不喜欢我做的那类工作，克莱因是这个群体的思想领袖。
  - 处理：Astra 复核通过。“一个由……组成的群体的思想领袖”连串“的”字

- 英文：The NDMers adamantly reject the focus on biases in the heuristics and biases approach.
  - 原译：NDM 学者坚决反对启发式与偏差研究路线对偏差的关注。
  - 现译：启发式与偏差研究路线把重点放在偏差上，NDM 学者坚决反对这样做。
  - 处理：Astra 复核通过。“反对……对偏差的关注”抽象名词作宾语

- 英文：I invited him to join in an effort to map the boundary that separates the marvels of intuition from its flaws.
  - 原译：我邀请他一起努力，划出那条把直觉的奇妙之处与它的缺陷分开的界线。
  - 现译：我邀请他和我一起，在直觉的奇妙之处与它的缺陷之间划出一条界线。
  - 处理：Astra 复核通过。“那条把……分开的界线”定语从句前置太长

- 英文：My thinking was formed by observing the illusion of validity in myself and by reading Paul Meehl’s demonstrations of the inferiority of clinical prediction. In contrast, Klein’s views were shaped by his early studies of fireground commanders (the leaders of firefighting teams).
  - 原译：我的想法，是在观察自己身上的有效性错觉、阅读保罗·米尔证明临床预测不如统计预测的那些研究时形成的。相比之下，克莱因的看法是由他早年对火场指挥官（消防队的带队人）的研究塑造的。
  - 现译：我的想法来自两方面：一是观察自己身上的有效性错觉，二是阅读保罗·米尔的研究，这些研究证明了临床预测不如统计预测。相比之下，克莱因的看法来自他早年对火场指挥官（消防队的带队人）的研究。
  - 处理：Astra 复核通过。“那些研究”前定语过长，“是由……塑造的”被动照搬

- 英文：investigated how the commanders could make good decisions without comparing options. The initial hypothesis was that commanders would restrict their analysis to only a pair of options, but that hypothesis proved to be incorrect.
  - 原译：研究了指挥官们怎样在不比较各种方案的情况下作出好的决定。最初的假设是，指挥官会把分析限制在仅仅两个方案之间，但事实证明这个假设是错的。
  - 现译：研究了指挥官们怎样不比较各种方案就作出好的决定。最初的假设是，指挥官只会分析两个方案，但事实证明这个假设是错的。
  - 处理：Astra 复核通过。“在不……的情况下”，“把分析限制在仅仅两个方案之间”直译

- 英文：They could draw on the repertoire of patterns that they had compiled during more than a decade of both real and virtual experience to identify a plausible option, which they considered first.
  - 原译：他们可以调用自己在十多年的真实经验和虚拟经验中积累起来的模式库，找出一个看似可行的方案，首先考虑它。
  - 现译：他们在十多年的真实经验和虚拟经验中积累了一套模式库，可以从中找出一个看似可行的方案，首先考虑它。
  - 处理：Astra 复核通过。“模式库”前定语过长

- 英文：In the first phase, a tentative plan comes to mind by an automatic function of associative memory—System 1.
  - 原译：在第一阶段，一个初步的计划通过联想记忆的自动功能浮现在脑中，这是系统 1 的工作。
  - 现译：在第一阶段，联想记忆自动运作，让一个初步的计划浮现在脑中，这是系统 1 的工作。
  - 处理：Astra 复核通过。“通过联想记忆的自动功能”照搬 by 短语

- 英文：The model of intuitive decision making as pattern recognition develops ideas presented some time ago by Herbert Simon, perhaps the only scholar who is recognized and admired as a hero and founding figure by all the competing clans and tribes in the study of decision making.
  - 原译：把直觉决策看作模式识别的这个模型，发展了赫伯特·西蒙多年前提出的观点。在决策研究领域，各个门派相互竞争，西蒙也许是唯一一位被所有门派公认、敬仰，尊为英雄和奠基人的学者。
  - 现译：这个模型把直觉决策看作模式识别，它发展了赫伯特·西蒙多年前提出的观点。在决策研究领域，各个门派相互竞争，西蒙也许是唯一一位被所有门派公认、敬仰，尊为英雄和奠基人的学者。
  - 处理：复核后重写。主语前定语过长，“唯一一位被……的学者”被动加长定语 复核：后半句把清楚的“西蒙也许是……”改成“所有门派都公认、敬仰，并尊为……”这一长定语，进一步推迟主语中心词，反而更拗口，没有达到消除长定语的目的。

- 英文：In chess, recurrent patterns of interacting pieces play the role of letters, and a chess position is a long word or a sentence.
  - 原译：在国际象棋里，反复出现的、棋子之间相互作用的模式扮演着字母的角色，而一个棋局就是一个长单词或一个句子。
  - 现译：在国际象棋里，棋子之间反复出现的相互作用模式相当于字母，而一个棋局就是一个长单词或一个句子。
  - 处理：复核后重写。“扮演着……的角色”直译 play the role of 复核：“相互作用、反复出现”并列后修饰关系不清。原文说的是棋子之间的相互作用模式反复出现，并非模式本身相互作用。

- 英文：I had spent more time thinking about clinicians, stock pickers, and political scientists trying to make unsupportable long-term forecasts.
  - 原译：我则花了更多时间去思考那些试图作出站不住脚的长期预测的临床心理学家、选股者和政治学家。
  - 现译：我则花了更多时间去思考那些试图作出站不住脚的长期预测的临床心理学家、选股者和政治学家。
  - 处理：复核后退回原译。“那些试图作出……的”定语太长 复核：原文限定讨论的是试图作出这类长期预测的专业人士。拆成“这些人试图……”后，容易被读成对三类专业人士的整体断言；before 的限定范围更清楚。

- 英文：Statistical algorithms greatly outdo humans in noisy environments for two reasons: they are more likely than human judges to detect weakly valid cues and much more likely to maintain a modest level of accuracy by using such cues consistently.
  - 原译：在噪声很大的环境里，统计算法远远胜过人，原因有两个：它们比人类判断者更有可能发现有效性较弱的线索，而且通过始终如一地使用这些线索，它们远比人更有可能保持中等水平的准确度。
  - 现译：在噪声很大的环境里，统计算法远远胜过人，原因有两个：一是它们比人类判断者更有可能发现有效性较弱的线索；二是它们始终如一地使用这些线索，因此远比人更有可能保持尚可的准确度。
  - 处理：复核后重写。“通过……”照搬 by 短语，两个原因分不清 复核：沿用了“中等水平”，但 modest 在这里强调准确度有限、不算高，并未确定达到中等水平。

- 英文：In the absence of valid cues, intuitive “hits” are due either to luck or to lies. If you find this conclusion surprising, you still have a lingering belief that intuition is magic.
  - 原译：在没有有效线索的情况下，直觉的“命中”要么靠运气，要么靠撒谎。如果你对这个结论感到意外，那说明你心里还残留着直觉是魔法的信念。
  - 现译：没有有效线索时，直觉的“命中”要么靠运气，要么靠撒谎。如果你对这个结论感到意外，那说明你心里还没有完全放下直觉是魔法的信念。
  - 处理：复核后重写。“在……的情况下”，“残留着……的信念”直译 lingering belief 复核：lingering 强调信念仍未消散；“隐隐相信”却强调信念模糊或微弱，改变了修饰含义。

- 英文：Think of how you developed your style of using the brakes on your car. As you were mastering the skill of taking curves, you gradually learned when to let go of the accelerator and when and how hard to use the brakes. Curves differ, and the variability you experienced while learning ensures that you are now ready to brake at the right time and strength for any curve you encounter.
  - 原译：想一想你是怎样形成自己踩刹车的方式的。在掌握过弯技巧的过程中，你逐渐学会了什么时候松开油门，什么时候踩刹车、踩多重。弯道各不相同，你在学车时经历过的这些变化，保证了你现在无论碰到什么弯道，都能在恰当的时候、用恰当的力度刹车。
  - 现译：想一想你踩刹车的方式是怎样形成的。学开车过弯的时候，你逐渐学会了什么时候松开油门，什么时候踩刹车、踩多重。弯道各不相同，正因为学车时经历过这些变化，你现在无论碰到什么弯道，都能在恰当的时候、用恰当的力度刹车。
  - 处理：Astra 复核通过。“怎样形成自己……的方式的”语序别扭，“在……的过程中”，抽象主语“经历过的这些变化，保证了”

- 英文：In contrast, radiologists obtain little information about the accuracy of the diagnoses they make and about the pathologies they fail to detect.
  - 原译：相比之下，放射科医生很少能得到关于自己诊断是否准确的信息，也很少知道自己漏掉了哪些病变。
  - 现译：相比之下，放射科医生很少能得知自己的诊断准不准，也很少知道自己漏掉了哪些病变。
  - 处理：Astra 复核通过。“得到关于……的信息”直译 information about

- 英文：Here again, as in the case of subjective confidence, the experts may not know the limits of their expertise.
  - 原译：这里，和主观信心的情况一样，专家也可能不知道自己专长的局限。
  - 现译：这里又和主观信心的情况一样：专家也可能不知道自己专长的局限。
  - 处理：Astra 复核通过。“这里，和……的情况一样，”照搬英文插入语

- 英文：The unrecognized limits of professional skill help explain why experts are often overconfident.
  - 原译：专业技能的局限没有被认识到，这有助于解释为什么专家常常过度自信。
  - 现译：专业技能有局限，专家自己却认识不到，这有助于解释他们为什么常常过度自信。
  - 处理：Astra 复核通过。“没有被认识到”被动句加抽象主语

- 英文：When evaluating expert intuition you should always consider whether there was an adequate opportunity to learn the cues, even in a regular environment.
  - 原译：评估专家直觉时，你应该始终考虑他们是否有足够的机会学会识别这些线索，即使是在有规律的环境中。
  - 现译：评估专家直觉时，即使是在有规律的环境中，你也应该始终考虑他们有没有足够的机会学会识别这些线索。
  - 处理：Astra 复核通过。让步状语照搬英文放在句末

- 英文：In a less regular, or low-validity, environment, the heuristics of judgment are invoked. System 1 is often able to produce quick answers to difficult questions by substitution, creating coherence where there is none. The question that is answered is not the one that was intended, but the answer is produced quickly and may be sufficiently plausible to pass the lax and lenient review of System 2.
  - 原译：在规律性较差，也就是有效性较低的环境里，判断启发式就会被调用。系统 1 常常能通过替代，迅速给困难的问题作出回答，在没有连贯性的地方制造出连贯性。被回答的问题并不是原本要问的那个问题，但答案来得很快，而且可能看上去足够合理，能通过系统 2 松懈、宽容的审查。
  - 现译：在规律性较差，也就是有效性较低的环境里，就会用到判断启发式。系统 1 常常能借助替代，迅速回答困难的问题，在没有连贯性的地方制造出连贯性。它回答的并不是原本要问的那个问题，但答案来得很快，而且可能看上去足够合理，能通过系统 2 松懈、宽容的审查。
  - 处理：Astra 复核通过。“被调用”“被回答的问题”照搬被动，“作出回答”虚化动词

- 英文：But this is what always happens when a project ends reasonably well: once you understand the main conclusion, it seems it was always obvious.
  - 原译：不过，一个项目只要结局还算不错，总会是这样：一旦你理解了主要结论，它似乎就一直是显而易见的。
  - 现译：不过，一个项目只要结局还算不错，总会是这样：一旦理解了主要结论，你就会觉得它好像一直都显而易见。
  - 处理：Astra 复核通过。“它似乎就一直是显而易见的”照搬 it seems it was 语序

- 英文：Klein still winces when the word bias is mentioned, and he still enjoys stories in which algorithms or formal procedures lead to obviously absurd decisions.
  - 原译：一提到“偏差”这个词，克莱因还是会皱眉；他也仍然喜欢听那些算法或形式化程序导致明显荒谬的决定的故事。
  - 现译：一提到“偏差”这个词，克莱因还是会皱眉；他也仍然喜欢听这样的故事：算法或形式化的程序导致了明显荒谬的决定。
  - 处理：Astra 复核通过。整个定语从句塞在“故事”前，“的”字连用

- 英文：“Did he really have an opportunity to learn? How quick and how clear was the feedback he received on his judgments?”
  - 原译：“他真的有机会去学吗？他的判断得到的反馈有多快，有多清楚？”
  - 现译：“他真的有机会去学吗？他作完判断，反馈来得有多快，有多清楚？”
  - 处理：Astra 复核通过。“他的判断得到的反馈”是书面直译，不像闲谈时会说的话

## 第 23 章 外部视角

- 英文：The initial enthusiasm for the idea in the Ministry of Education had waned by the time the text was delivered and it was never used.
  - 原译：等到教材交上去的时候，教育部当初对这个想法的热情已经消退，这本教材也从来没有被用过。
  - 现译：等到教材交上去的时候，教育部当初对这个想法的热情已经消退，这本教材也从来没有人用过。
  - 处理：Astra 复核通过。照搬被动句“被用过”

- 英文：I was slower to accept the third lesson, which I call irrational perseverance: the folly we displayed that day in failing to abandon the project.
  - 原译：我过了更久才接受第三个教训，我把它叫作非理性坚持，也就是我们那天没有放弃项目所表现出来的愚蠢。
  - 现译：我过了更久才接受第三个教训，我把它叫作非理性坚持，指的是我们那天表现出的愚蠢：没有放弃这个项目。
  - 处理：Astra 复核通过。“愚蠢”前堆了一长串定语

- 英文：The members of those teams were also unable to imagine the events that would cause them to spend seven years to finish, or ultimately fail to finish, a project that they evidently had thought was very feasible.
  - 原译：那些团队的成员同样想象不到，会有哪些事情让他们花了七年才完成一个项目，或者最终没能完成，而他们当初显然认为这个项目非常可行。
  - 现译：那些团队的成员当初显然认为项目非常可行，他们同样想象不到，会有哪些事情让他们花了七年才完成，或者最终没能完成。
  - 处理：Astra 复核通过。照搬英文语序，把定语从句拖在句尾

- 英文：There are many ways for any plan to fail, and although most of them are too improbable to be anticipated, the likelihood that something will go wrong in a big project is high.
  - 原译：任何计划都可能以很多种方式失败，其中大多数可能性太小，事先预料不到，但在一个大项目中，某个环节出差错的可能性很高。
  - 现译：任何计划都有很多种失败的可能，其中大多数发生的概率太小，事先预料不到，但在一个大项目中，某个环节出差错的可能性很高。
  - 处理：Astra 复核通过。“以……方式失败”是直译

- 英文：He had in his head all the knowledge required to estimate the statistics of an appropriate reference class, but he reached his initial estimate without ever using that knowledge.
  - 原译：估计一个合适的参照类别的统计数据所需要的知识，他脑子里全都有，可是他作出最初的估计时，根本没有用到这些知识。
  - 现译：要估计一个合适的参照类别的统计数据，所需的知识他脑子里全都有，可是他作出最初的估计时，根本没有用到这些知识。
  - 处理：Astra 复核通过。“知识”前的定语过长，“的”字连串

- 英文：However, the remaining ambivalence about the outside view in the medical profession is expressed in concerns about the impersonality of procedures that are guided by statistics and checklists.
  - 原译：然而，医学界对外部视角仍然心存矛盾，这表现为医生们担心，由统计数据和检查清单指导的程序缺乏人情味。
  - 现译：然而，医学界对外部视角仍然心存矛盾：医生们担心，以统计数据和检查清单为依据的诊疗程序缺乏人情味。
  - 处理：复核后重写。“这表现为”“由……指导的”是英文句式直译 复核：“按统计数据和检查清单办事的程序”搭配不当：办事的是人，不是程序。拆句方向可保留，但应理顺程序与统计依据的关系。

- 英文：If they do not recognize the need for an outside view, they commit a planning fallacy.
  - 原译：如果他们认识不到需要外部视角，他们就犯了规划谬误。
  - 现译：他们如果认识不到需要外部视角，就犯了规划谬误。
  - 处理：Astra 复核通过。代词“他们”重复

- 英文：Using such distributional information from other ventures similar to that being forecasted is called taking an “outside view” and is the cure to the planning fallacy.
  - 原译：利用与被预测项目相似的其他项目的这类分布信息，就叫作采取“外部视角”，它是治疗规划谬误的良方。
  - 现译：预测一个项目时，利用与它相似的其他项目的这类分布信息，就叫作采取“外部视角”，它是治疗规划谬误的良方。
  - 处理：Astra 复核通过。被动式定语“被预测项目”加一串“的”

- 英文：Use specific information about the case to adjust the baseline prediction, if there are particular reasons to expect the optimistic bias to be more or less pronounced in this project than in others of the same type.
  - 原译：如果有特别的理由认为，这个项目中的乐观偏差会比同类其他项目更明显或更不明显，就用关于这个个案的具体信息来调整基线预测。
  - 现译：如果有特别的理由认为，这个项目的乐观偏差会比同类其他项目更明显或更轻微，就用这个个案的具体信息来调整基线预测。
  - 处理：Astra 复核通过。“更不明显”生硬，“关于”多余

- 英文：Together we sketched a theory of decision making in which the optimistic bias is a significant source of risk taking. In the standard rational model of economics, people take risks because the odds are favorable—they accept some probability of a costly failure because the probability of success is sufficient.
  - 原译：我们一起勾勒出一种决策理论，在这个理论里，乐观偏差是冒险行为的一个重要来源。在经济学标准的理性模型中，人们之所以冒险，是因为胜算较大：成功的概率足够高，所以他们愿意接受一定的失败概率，哪怕失败的代价很高。
  - 现译：我们一起勾勒出一种决策理论，把乐观偏差看作冒险行为的一个重要来源。在经济学的标准理性模型中，人们之所以冒险，是因为胜算较大：成功的概率足够高，所以他们愿意接受一定的失败概率，哪怕失败的代价很高。
  - 处理：Astra 复核通过。照搬 in which 从句；“经济学标准的”语序别扭

- 英文：When forecasting the outcomes of risky projects, executives too easily fall victim to the planning fallacy.
  - 原译：高管们在预测风险项目的结果时，太容易成为规划谬误的牺牲品。
  - 现译：高管们在预测风险项目的结果时，太容易陷入规划谬误。
  - 处理：Astra 复核通过。fall victim to 硬译成“成为……的牺牲品”

- 英文：It is easier to change directions in a crisis, but this was not a crisis, only some new facts about people we did not know.
  - 原译：在危机中改变方向比较容易，可这并不是危机，只是关于一些我们不认识的人的新事实。
  - 现译：在危机中改变方向比较容易，可这并不是危机，只是一些关于陌生人的新事实。
  - 处理：Astra 复核通过。“新事实”前定语堆叠

- 英文：There was no further attempt at rational planning for the rest of the time I spent as a member of the team—a particularly troubling omission for a team dedicated to teaching rationality.
  - 原译：在我作为团队成员的剩余时间里，我们再也没有尝试过理性地规划；对一个致力于教授理性的团队来说，这个疏漏尤其令人不安。
  - 现译：我后来留在团队里的那段时间，我们再也没有尝试过理性地规划；对一个致力于教授理性的团队来说，这个疏漏尤其令人不安。
  - 处理：Astra 复核通过。“作为团队成员的剩余时间”是直译

- 英文：“She is the victim of a planning fallacy. She’s assuming a best-case scenario, but there are too many different ways for the plan to fail, and she cannot foresee them all.”
  - 原译：“她陷入了规划谬误。她假定的是最好的情况，可是计划失败的方式太多了，她不可能全都预见到。”
  - 现译：“她陷入了规划谬误。她是按最好的情况打算的，可是导致计划失败的原因太多了，她不可能全都预见到。”
  - 处理：复核后重写。闲谈里的话像书面直译，“失败的方式”生硬 复核：“出岔子”不等于计划失败；“出岔子的地方”又把失败的多种方式改成了出问题的环节，弱化并改变了原意。

## 第 24 章 资本主义的引擎

- 英文：The planning fallacy is only one of the manifestations of a pervasive optimistic bias.
  - 原译：规划谬误只是一种普遍存在的乐观偏差的表现之一。
  - 现译：乐观偏差无处不在，规划谬误只是它的表现之一。
  - 处理：复核后保留改写。“一种……的……的表现之一”定语堆叠 复核：pervasive 表示普遍存在，“无处不在”把程度绝对化了。

- 英文：If you were allowed one wish for your child, seriously consider wishing him or her optimism.
  - 原译：如果你只能为孩子许一个愿，不妨认真考虑一下，祝他或她乐观。
  - 现译：如果你只能为孩子许一个愿，不妨认真考虑一下：愿孩子拥有乐观的性情。
  - 处理：按复核意见修改。him or her 硬译成“他或她” 复核：去掉“他或她”是对的，但“祝孩子乐观”仍不自然。这里是在建议为孩子许下拥有乐观性情的愿望。

- 英文：Optimistic individuals play a disproportionate role in shaping our lives.
  - 原译：乐观的人在塑造我们的生活方面，所起的作用大得不成比例。
  - 现译：乐观的人塑造着我们的生活，所起的作用大得不成比例。
  - 处理：Astra 复核通过。“在……方面”套式

- 英文：Because they misread the risks, optimistic entrepreneurs often believe they are prudent, even when they are not. Their confidence in their future success sustains a positive mood that helps them obtain resources from others, raise the morale of their employees, and enhance their prospects of prevailing.
  - 原译：由于误判了风险，乐观的创业者常常相信自己很谨慎，即使事实并非如此。他们对未来成功的信心让他们保持着积极的情绪，这种情绪帮助他们从别人那里获得资源，提振员工的士气，也提高了他们最终胜出的可能。
  - 现译：乐观的创业者误判了风险，所以即使实际上并不谨慎，也常常相信自己很谨慎。他们相信自己将来会成功，这份信心让他们保持积极的情绪，而这种情绪能帮他们从别人那里获得资源、提振员工士气，也让他们更有可能最终胜出。
  - 处理：Astra 复核通过。让步状语拖在句尾；抽象名词“信心”作主语

- 英文：Significantly, persistence after discouraging advice was relatively common among inventors who had a high score on a personality measure of optimism—on which inventors generally scored higher than the general population.
  - 原译：值得注意的是，在一项乐观人格测量中得分高的发明者，听了令人泄气的建议之后仍然坚持的情况相对常见；而在这项测量上，发明者的得分普遍高于一般人群。
  - 现译：值得注意的是，在一项乐观人格测量中得分高的发明者里，听了令人泄气的建议之后仍然坚持的人相对较多；而发明者在这项测量上的得分，普遍高于一般人群。
  - 处理：Astra 复核通过。主语和谓语搭不上，“……的情况相对常见”照搬英文结构

- 英文：The stock market commonly responds by downgrading the value of the acquiring firm, because experience has shown that efforts to integrate large firms fail more often than they succeed.
  - 原译：股市的常见反应是调低收购方的估值，因为经验表明，整合大公司的努力失败的时候比成功的时候多。
  - 现译：股市的常见反应是调低收购方的估值，因为经验表明，整合大公司失败的时候比成功的时候多。
  - 处理：Astra 复核通过。抽象名词“努力”作主语

- 英文：Remarkably, the stock of the acquiring company suffered substantially more in mergers if the CEO was overly optimistic by the authors’ measure.
  - 原译：值得注意的是，如果按两位作者的衡量标准，CEO 过度乐观，那么收购方的股票在兼并中受到的打击要大得多。
  - 现译：值得注意的是，按两位作者的衡量标准，如果 CEO 过度乐观，收购方的股票在兼并中受到的打击就要大得多。
  - 处理：Astra 复核通过。条件句里状语位置别扭，读不顺

- 英文：The optimistic risk taking of entrepreneurs surely contributes to the economic dynamism of a capitalistic society, even if most risk takers end up disappointed.
  - 原译：创业者乐观的冒险行为，无疑为资本主义社会的经济活力作出了贡献，尽管大多数冒险的人最后都会失望。
  - 现译：尽管大多数冒险的人最后都会失望，创业者乐观的冒险行为无疑为资本主义社会增添了经济活力。
  - 处理：Astra 复核通过。“尽管”从句照搬英文放在句尾；“为……作出了贡献”

- 英文：They know less about their competitors and therefore find it natural to imagine a future in which the competition plays little part.
  - 原译：他们对竞争对手了解得少，因此很自然地会想象一个竞争几乎不起作用的未来。
  - 现译：他们对竞争对手了解得少，因此很自然地设想，将来竞争几乎起不了什么作用。
  - 处理：复核后保留改写。“想象一个……的未来”照搬 in which 结构 复核：plays little part 表示作用不大，“几乎起不了什么作用”程度偏重，也带入了不能起作用的意味。less 与前文对自身情况的了解之间的比较应更清楚。

- 英文：In fact, Giovanni Dosi and Dan Lovallo call entrepreneurial firms that fail but signal new markets to more qualified competitors “optimistic martyrs”—good for the economy but bad for their investors.
  - 原译：事实上，乔瓦尼·多西和丹·洛瓦洛把那些虽然失败、却向更有实力的竞争者指出了新市场的创业公司称为“乐观的殉道者”：它们对经济有好处，对自己的投资者却是坏事。
  - 现译：事实上，有些创业公司虽然失败了，却向更有实力的竞争者指出了新市场，乔瓦尼·多西和丹·洛瓦洛把这样的公司称为“乐观的殉道者”：它们对经济有好处，对自己的投资者却是坏事。
  - 处理：Astra 复核通过。“创业公司”前定语过长

- 英文：Allowing for the information that does not come to mind—perhaps because one never knew it—is impossible.
  - 原译：那些没有浮现在脑中的信息（也许是因为我们从来就不知道），根本不可能被考虑进去。
  - 现译：至于没有浮现在脑中的信息（也许是因为我们从来就不知道），我们根本不可能把它考虑进去。
  - 处理：Astra 复核通过。不必要的被动句“被考虑进去”

- 英文：The confidence interval that properly reflects the CFOs’ knowledge (more precisely, their ignorance) is more than 4 times wider than the intervals they actually stated.
  - 原译：能恰当反映 CFO 们的知识（更准确地说，是他们的无知）的置信区间，宽度是他们实际给出的区间的 4 倍多。
  - 现译：要恰当反映 CFO 们的知识（更准确地说，是他们的无知），置信区间的宽度得是他们实际给出的区间的 4 倍多。
  - 处理：Astra 复核通过。“置信区间”前定语过长

- 英文：Organizations that take the word of overconfident experts can expect costly consequences.
  - 原译：听信过度自信的专家的组织，可以预料要付出高昂的代价。
  - 现译：组织如果听信过度自信的专家，就很可能为此付出高昂的代价。
  - 处理：按复核意见修改。长定语加“可以预料”，直译 can expect 复核：can expect 是对后果的预期；“就要准备”容易变成要求组织提前作准备，改变了原句的陈述语气。

- 英文：A study of patients who died in the ICU compared autopsy results with the diagnosis that physicians had provided while the patients were still alive.
  - 原译：一项研究考察了在重症监护室（ICU）去世的病人，把尸检结果和医生在病人生前作出的诊断进行比较。
  - 现译：一项研究考察了在重症监护室（ICU）去世的病人，对比了尸检结果和医生在病人生前作出的诊断。
  - 处理：Astra 复核通过。虚化动词“进行比较”

- 英文：Here again, expert overconfidence is encouraged by their clients: “Generally, it is considered a weakness and a sign of vulnerability for clinicians to appear unsure. Confidence is valued over uncertainty and there is a prevailing censure against disclosing uncertainty to patients.”
  - 原译：在这里，专家的过度自信同样受到了客户的鼓励：“一般来说，临床医生显得没有把握，会被看作一种弱点，一种脆弱的表现。人们看重信心胜过不确定，向病人透露不确定性的做法普遍会受到指责。”
  - 现译：在这里，客户同样在鼓励专家过度自信：“一般来说，临床医生显得没有把握，会被看作一种弱点，一种脆弱的表现。有把握比没把握更受重视，向病人透露不确定性的做法普遍会受到指责。”
  - 处理：复核后重写。不必要的被动句“受到了……的鼓励” 复核：主句改写可保留，但引语中的“人们看重信心胜过不确定”仍是生硬的英文比较结构，中文不顺。

- 英文：Experts who acknowledge the full extent of their ignorance may expect to be replaced by more confident competitors, who are better able to gain the trust of clients.
  - 原译：承认自己无知有多深的专家，可能会被更自信的竞争者取代，因为后者更能赢得客户的信任。
  - 现译：专家如果坦率承认自己有多么无知，就可能被更自信的竞争者取代，因为后者更能赢得客户的信任。
  - 处理：复核后重写。“承认自己无知有多深的专家”定语生硬 复核：“把自己的无知和盘托出”搭配生硬。原文强调充分承认自己所知有限的程度，不是把某些隐情全部说出来。

- 英文：When they come together, the emotional, cognitive, and social factors that support exaggerated optimism are a heady brew, which sometimes leads people to take risks that they would avoid if they knew the odds.
  - 原译：支撑过度乐观的情绪因素、认知因素和社会因素凑到一起，就成了一杯让人上头的烈酒，有时会让人去冒那些他们如果知道胜算就会避开的风险。
  - 现译：支撑过度乐观的情绪因素、认知因素和社会因素凑到一起，就成了一杯让人上头的烈酒，有时会让人去冒一些风险，而他们要是知道胜算有多大，本来会避开这些风险。
  - 处理：Astra 复核通过。“风险”前塞进整个条件从句

- 英文：There is no evidence that risk takers in the economic domain have an unusual appetite for gambles on high stakes; they are merely less aware of risks than more timid people are.
  - 原译：没有证据表明，经济领域的冒险者对高赌注的赌博有异乎寻常的胃口；他们只是比胆小的人更少意识到风险而已。
  - 现译：没有证据表明，经济领域的冒险者格外爱下大赌注；他们只是不像胆小一些的人那样能意识到风险而已。
  - 处理：复核后重写。“更少意识到”直译 less aware 复核：“对高赌注的赌博有异乎寻常的胃口”仍是生硬直译；more timid 的相对比较意味也没有保留。

- 英文：The effects of high optimism on decision making are, at best, a mixed blessing, but the contribution of optimism to good implementation is certainly positive.
  - 原译：高度乐观对决策的影响，往好里说也是利弊参半；但乐观对把事情执行好的贡献，无疑是正面的。
  - 现译：高度乐观对决策的影响，往好里说也是利弊参半；但在执行阶段，乐观无疑有助于把事情做好。
  - 处理：按复核意见修改。抽象名词“贡献”作主语，结构别扭 复核：“把事情执行好”搭配仍不自然：可以执行计划、任务，却不宜直接说执行事情。应保留决策与执行的区别。

- 英文：This style can be taught, at least to some extent, and Seligman has documented the effects of training on various occupations that are characterized by a high rate of failures, such as cold-call sales of insurance (a common pursuit in pre-Internet days).
  - 原译：这种风格至少在一定程度上是可以教会的；塞利格曼记录了这种训练对各种以高失败率为特点的职业产生的效果，比如陌生拜访式的保险推销（这在互联网出现以前是一种常见的营生）。
  - 现译：这种风格至少在一定程度上是可以教会的；塞利格曼记录了这种训练在多种失败率很高的职业里产生的效果，比如陌生拜访式的保险推销（这在互联网出现以前是一种常见的营生）。
  - 处理：Astra 复核通过。“以……为特点的”直译 characterized by

- 英文：The premortem has two main advantages: it overcomes the groupthink that affects many teams once a decision appears to have been made, and it unleashes the imagination of knowledgeable individuals in a much-needed direction.
  - 原译：事前验尸有两大好处：一是能克服群体思维，很多团队一旦看起来已经作出了决定，就会受到这种思维的影响；二是能把知情者的想象力释放到一个非常需要的方向上。
  - 现译：事前验尸有两大好处：一是能克服群体思维，很多团队一旦看起来已经作出了决定，就会受到这种思维的影响；二是能让了解情况的人充分发挥想象力，并把它用在急需的方向上。
  - 处理：复核后重写。“把想象力释放到方向上”搭配生硬 复核：“放开想象”“一个非常需要的方向”搭配仍生硬，没有真正消除原句的翻译腔。

- 英文：“They have an illusion of control. They seriously underestimate the obstacles.”
  - 原译：“他们有控制错觉。他们严重低估了障碍。”
  - 现译：“他们有控制错觉，严重低估了障碍。”
  - 处理：Astra 复核通过。口语里重复代词“他们”

- 英文：“This is a case of overconfidence. They seem to believe they know more than they actually do know.”
  - 原译：“这是过度自信。他们好像以为自己知道的比实际知道的更多。”
  - 现译：“这是过度自信。他们好像以为自己知道的比实际更多。”
  - 处理：复核后重写。照搬 do know 的重复，不像口语 复核：删去“实际知道的”后，“知道的”直接与副词“实际上”比较，比较对象残缺，反而不如原句清楚通顺。

- 英文：“We should conduct a premortem session. Someone may come up with a threat we have neglected.”
  - 原译：“我们应该开一次事前验尸会。说不定有人会想到一个我们忽视了的威胁。”
  - 现译：“我们应该开一次事前验尸会。说不定有人会想到我们忽视了的威胁。”
  - 处理：Astra 复核通过。多余的“一个”

## 第 25 章 伯努利的错误

- 英文：Choices between such gambles provide a simple model that shares important features with the more complex decisions that researchers actually aim to understand.
  - 原译：在这类赌局之间作选择，提供了一个简单的模型，它与研究者真正想要理解的那些更复杂的决策有一些重要的共同特征。
  - 现译：在这类赌局之间作出的选择提供了一个简单的模型，与研究者真正想弄懂的那些更复杂的决策有一些重要的共同特征。
  - 处理：按复核意见修改。照搬定语从句，用“它”另起一句 复核：“作选择是一个模型”搭配生硬；原文说的是这些选择提供了一个模型。

- 英文：The field had a theory, expected utility theory, which was the foundation of the rational-agent model
  - 原译：这个领域有一个理论，即期望效用理论。
  - 现译：当时这个领域有一个理论：期望效用理论。
  - 处理：Astra 复核通过。同位语用书面的“即”硬接

- 英文：Expected utility theory was not intended as a psychological model;
  - 原译：期望效用理论并不是作为心理学模型提出的。
  - 现译：期望效用理论并不是作为心理学模型提出的。
  - 处理：复核后退回原译。“作为……提出的”是被动结构直译 复核：原译准确自然；“理论的本意……充当”搭配反而生硬，没有改善中文。

- 英文：The mathematician John von Neumann, one of the giant intellectual figures of the twentieth century, and the economist Oskar Morgenstern had derived their theory of rational choice between gambles from a few axioms.
  - 原译：数学家约翰·冯·诺伊曼是 20 世纪的思想巨人之一，他和经济学家奥斯卡·摩根斯坦从几条公理出发，推导出了他们关于在赌局之间作理性选择的理论。
  - 现译：数学家约翰·冯·诺伊曼是 20 世纪的思想巨人之一，他和经济学家奥斯卡·摩根斯坦从几条公理出发，推导出了他们那套在赌局之间作理性选择的理论。
  - 处理：Astra 复核通过。“他们关于……的理论”照搬 their theory of

- 英文：We maintained our routine of spending many hours each day in conversation, sometimes in our offices, sometimes at restaurants, often on long walks through the quiet streets of beautiful Jerusalem.
  - 原译：我们保持着老习惯，每天花许多个小时交谈，有时在办公室，有时在餐馆，也常常是在美丽的耶路撒冷那些安静的街道上长时间散步的时候。
  - 现译：也常常沿着美丽的耶路撒冷城里安静的街道边走边聊，一走就是很久。
  - 处理：按复核意见修改。长定语加“……的时候”，照搬介词短语 复核：“也常常是在美丽的耶路撒冷，沿着……”衔接松散，也削弱了散步时交谈这一关系。

- 英文：Most important, our model was purely descriptive, and its goal was to document and explain systematic violations of the axioms of rationality in choices between gambles.
  - 原译：最重要的是，我们的模型纯粹是描述性的，它的目标是记录并解释人们在赌局之间作选择时对理性公理的系统性违背。
  - 现译：最重要的是，我们的模型纯粹是描述性的，目标是记录并解释人们在赌局之间作选择时怎样系统性地违背理性公理。
  - 处理：Astra 复核通过。名词化的“对……的系统性违背”，多余的“它的”

- 英文：However, our decision was not guided by a wish to influence economics; Econometrica just happened to be where the best papers on decision making had been published in the past, and we were aspiring to be in that company.
  - 原译：不过，我们作这个决定，并没有想着要影响经济学；过去关于决策的最好的论文，恰好就发表在《计量经济学》上，我们希望自己的论文也能跻身其中。
  - 现译：只是此前最好的决策研究论文恰好发表在《计量经济学》上，我们希望自己的论文也能跻身其中。
  - 处理：按复核意见修改。“关于决策的最好的论文”的字连用 复核：“研究决策最好的那些论文”修饰关系不清，容易把“最好”读成对“研究决策”的修饰。

- 英文：In this choice as in many others, we were lucky.
  - 原译：在这件事上，和在其他许多事情上一样，我们运气很好。
  - 现译：这次选择和其他许多选择一样，我们都很走运。
  - 处理：Astra 复核通过。照搬 in this … as in many others 的介词结构

- 英文：As Fechner well knew, he was not the first to look for a function that relates psychological intensity to the physical magnitude of the stimulus.
  - 原译：费希纳很清楚，在他之前就有人寻找过一个把心理强度和刺激的物理量联系起来的函数。
  - 现译：费希纳很清楚，在他之前就有人找过这样一个函数，用来把心理强度和刺激的物理量联系起来。
  - 处理：Astra 复核通过。定语从句前置，名词前堆了一长串修饰

- 英文：In 1738, the Swiss scientist Daniel Bernoulli anticipated Fechner’s reasoning and applied it to the relationship between the psychological value or desirability of money (now called utility) and the actual amount of money.
  - 原译：早在 1738 年，瑞士科学家丹尼尔·伯努利就想到了费希纳后来的这套推理，并把它用在金钱的心理价值或吸引力（现在称为效用）与金钱的实际数额之间的关系上。
  - 现译：早在 1738 年，瑞士科学家丹尼尔·伯努利就想到了费希纳后来的这套推理，并用它来考察金钱的心理价值或吸引力（现在称为效用）与金钱实际数额的关系。
  - 处理：Astra 复核通过。“把它用在……之间的关系上”中间夹着很长的成分

- 英文：One hundred years before Fechner, Bernoulli invented psychophysics to explain this aversion to risk.
  - 原译：比费希纳早一百年，伯努利就为了解释这种对风险的厌恶而发明了心理物理学。
  - 现译：为的是解释这种风险规避倾向。
  - 处理：按复核意见修改。状语照搬英文语序，“为了……而……”夹在中间 复核：这里的 aversion to risk 指术语“风险规避”，应与术语表及本段用语保持一致。

- 英文：Table 3 shows a version of the utility function that Bernoulli calculated; it presents the utility of different levels of wealth, from 1 million to 10 million.
  - 原译：表 3 列出了伯努利计算出的效用函数的一个版本[^t1]，它给出了从 100 万到 1,000 万不同财富水平的效用。
  - 现译：表 3 展示了伯努利算出的效用函数的一个版本[^t1]，列出了从 100 万到 1,000 万各个财富水平的效用。
  - 处理：按复核意见修改。多余的代词“它”，照搬分号后的第二个主语 复核：原文说表格展示效用函数的一个版本，不是说表格本身就是函数的一个版本。

- 英文：As you can see in the table, the loss of 1 million causes a loss of 4 points of utility (from 100 to 96) to someone who has 10 million and a much larger loss of 18 points (from 48 to 30) to someone who starts off with 3 million.
  - 原译：从表中可以看到，对拥有 1,000 万的人来说，损失 100 万会让效用减少 4 点（从 100 降到 96）；对一开始只有 300 万的人来说，同样损失 100 万，效用会减少多得多，达到 18 点（从 48 降到 30）。
  - 现译：从表中可以看到，拥有 1,000 万的人损失 100 万，效用减少 4 点（从 100 降到 96）；一开始只有 300 万的人损失同样的 100 万，效用要减少得多，达到 18 点（从 48 降到 30）。
  - 处理：Astra 复核通过。两次“对……来说”，照搬 to someone who

- 英文：To predict the subjective experience of loudness, it is not enough to know its absolute energy; you also need to know the reference sound to which it is automatically compared.
  - 原译：要预测响度的主观体验，只知道声音的绝对能量是不够的，你还需要知道，它会被自动拿去和哪个参照声音比较。
  - 现译：要预测一个声音听起来有多响，只知道它的绝对能量是不够的，你还需要知道，听的人会自动拿它和哪个参照声音作比较。
  - 处理：复核后重写。“响度的主观体验”是名词短语直译 复核：前半句有所改善，但后半句“它会被自动拿去”仍是生硬的被动表达。

- 英文：This is very attractive.
  - 原译：这非常有吸引力。
  - 现译：这非常诱人。
  - 处理：Astra 复核通过。人物心里话用了书面的“有吸引力”

- 英文：The mystery is how a conception of the utility of outcomes that is vulnerable to such obvious counterexamples survived for so long.
  - 原译：令人费解的是，一种关于结果效用的观念，经不起如此明显的反例，却能存活这么久。
  - 现译：令人费解的是，一种关于结果效用的观念，经不起如此明显的反例，却能存活这么久。
  - 处理：复核后退回原译。“一种关于……的观念”照搬 a conception of 复核：“看待结果效用的观念”不如原译“关于结果效用的观念”自然；新增“这样”“明明”等使句子更拖沓。

- 英文：Both candidates are willing to accept the salary we’re offering, but they won’t be equally satisfied because their reference points are different.
  - 原译：两位候选人都愿意接受我们开的薪水，但他们的满意程度不会一样，因为他们的参照点不同。
  - 现译：两位候选人都愿意接受我们开的薪水，但满意程度不会一样，因为两人的参照点不同。
  - 处理：Astra 复核通过。口语里连用“他们的”，代词多余

- 英文：That’s not surprising—she can only gain, so she’s risk averse. He, on the other hand, faces options that are all bad, so he’d rather take the risk.
  - 原译：这不奇怪：她只可能有所得，所以她规避风险。他呢，面对的选项全都很糟，所以他宁愿冒这个险。
  - 现译：这不奇怪：她只可能有所得，所以规避风险。他呢，面对的选项全都很糟，所以宁愿冒这个险。
  - 处理：Astra 复核通过。口语里重复主语“她”“他”

## 第 26 章 前景理论

- 英文：Amos and I stumbled on the central flaw in Bernoulli’s theory by a lucky combination of skill and ignorance.
  - 原译：阿莫斯和我偶然发现了伯努利理论的核心缺陷，这要归功于本事和无知的一次幸运组合。
  - 现译：阿莫斯和我偶然发现了伯努利理论的核心缺陷，靠的是本事和无知幸运地凑到了一起。
  - 处理：Astra 复核通过。“……的一次幸运组合”是名词短语直译

- 英文：He remembered that the economist Harry Markowitz, who would later earn the Nobel Prize for his work on finance, had proposed a theory in which utilities were attached to changes of wealth rather than to states of wealth.
  - 原译：他记得，后来因金融学研究获得诺贝尔奖的经济学家哈里·马科维茨，曾经提出过一种理论，在这种理论里，效用对应的是财富的变化，而非财富的状态。
  - 现译：他记得，后来因金融学研究获得诺贝尔奖的经济学家哈里·马科维茨，曾经提出过一种理论：效用对应的是财富的变化，而非财富的状态。
  - 处理：Astra 复核通过。“在这种理论里”照搬 in which 从句

- 英文：We soon knew that we had overcome a serious case of theory-induced blindness, because the idea we had rejected now seemed not only false but absurd.
  - 原译：我们很快就知道，自己克服了一次严重的理论导致的盲目，因为我们抛弃的那个想法，现在看来不仅是错的，而且荒唐。
  - 现译：我们很快就知道，自己已经克服了相当严重的理论导致的盲目，因为我们抛弃的那个想法，现在看来不仅是错的，而且荒唐。
  - 处理：Astra 复核通过。“一次严重的……”照搬 a serious case of

- 英文：In utility theory, the utility of a gain is assessed by comparing the utilities of two states of wealth.
  - 原译：在效用理论中，一笔收益的效用是通过比较两种财富状态的效用来评估的。
  - 现译：在效用理论中，要评估一笔收益的效用，就要比较两种财富状态的效用。
  - 处理：Astra 复核通过。“是通过……来评估的”是被动句直译

- 英文：As might be expected in a situation of theory-induced blindness, possible differences between gains and losses were neither expected nor studied.
  - 原译：正如在理论导致的盲目中可以预料的那样，收益和损失之间可能存在的差别，既没有人预料到，也没有人研究。
  - 现译：在理论导致的盲目之下，情况可想而知：收益和损失之间可能存在的差别，既没有人预料到，也没有人研究。
  - 处理：复核后重写。“正如……可以预料的那样”照搬 as might be expected 复核：“结果不出所料”暗示事先已有预料；as might be expected 表示这种情况可以理解、不足为奇，并未声称有人事先作出预测。

- 英文：The risk-averse choice in this problem would not have surprised Bernoulli.
  - 原译：这个问题中风险规避的选择，不会让伯努利感到意外。
  - 现译：人们在这个问题里选择规避风险，伯努利是不会感到意外的。
  - 处理：Astra 复核通过。带长定语的名词短语作主语

- 英文：If you are like most other people, you chose the gamble in this question.
  - 原译：如果你和其他大多数人一样，你在这个问题里选的是赌局。
  - 现译：如果你和其他大多数人一样，在这个问题里选的就是赌局。
  - 处理：Astra 复核通过。重复主语“你”

- 英文：Because the dominant theory did not provide a plausible way to accommodate different attitudes to risk for gains and losses, the fact that the attitudes differed had to be ignored.
  - 原译：占主导地位的理论无法以合理的方式容纳人们对收益和对损失的不同风险态度，于是，这两种态度不同的事实就只好被忽略了。
  - 现译：占主导地位的理论没法合理地容纳人们面对收益和损失时的不同风险态度，所以研究者只好对这种差别视而不见。
  - 处理：复核后重写。“以……的方式”和“被忽略”都是直译 复核：后半句省略主语，读起来成了“理论只好视而不见”；原文指人们因理论无法容纳差别而忽略事实。

- 英文：In both cases you have a choice between the same two options: you can have the certainty of being richer than you currently are by $1,500, or accept a gamble in which you have equal chances to be richer by $1,000 or by $2,000.
  - 原译：在两个问题中，你都是在同样的两个选项之间做选择：要么确定比现在多出 1,500 美元，要么接受一个赌局，在这个赌局里，你有同等的机会多出 1,000 美元或者多出 2,000 美元。
  - 现译：在两个问题中，你都是在同样的两个选项之间做选择：要么确定比现在多出 1,500 美元，要么接受一个赌局，多出 1,000 美元和多出 2,000 美元的机会各占一半。
  - 处理：Astra 复核通过。“在这个赌局里”照搬 in which 从句

- 英文：The finding of different preferences in problems 3 and 4 was a decisive counterexample to the key idea of Bernoulli’s theory.
  - 原译：问题 3 和问题 4 中的偏好不同，这一发现是对伯努利理论核心观念的一个决定性的反例。
  - 现译：问题 3 和问题 4 中的偏好不同，这一发现对伯努利理论的核心观念构成了一个决定性的反例。
  - 处理：Astra 复核通过。“是对……的一个……的反例”，的字堆叠

- 英文：You know something about your preferences that utility theorists do not—that your attitudes to risk would not be different if your net worth were higher or lower by a few thousand dollars (unless you are abjectly poor).
  - 原译：关于你自己的偏好，你知道一些效用理论家不知道的事：就算你的净资产多几千美元或者少几千美元，你对风险的态度也不会有什么不同（除非你一贫如洗）。
  - 现译：说到你自己的偏好，有些事你知道，效用理论家却不知道：就算你的净资产多几千美元或者少几千美元，你对风险的态度也不会有什么不同（除非你一贫如洗）。
  - 处理：Astra 复核通过。“关于……”开头，定语从句前置

- 英文：You just like winning and dislike losing—and you almost certainly dislike losing more than you like winning.
  - 原译：你只是喜欢赢、不喜欢输，而且几乎可以肯定，你对输的厌恶超过你对赢的喜爱。
  - 现译：你只是喜欢赢、不喜欢输，而且几乎可以肯定，你讨厌输胜过喜欢赢。
  - 处理：Astra 复核通过。动词名词化成“对输的厌恶”“对赢的喜爱”

- 英文：The missing variable is the reference point, the earlier state relative to which gains and losses are evaluated.
  - 原译：缺失的那个变量就是参照点，也就是评估收益和损失时所对照的那个先前的状态。
  - 现译：缺失的那个变量就是参照点，也就是先前的那个状态，评估收益和损失都要拿它作对照。
  - 处理：Astra 复核通过。relative to which 从句前置成长定语

- 英文：They play an essential role in the evaluation of financial outcomes and are common to many automatic processes of perception, judgment, and emotion.
  - 原译：它们在评估财务结果时起着关键的作用，也是知觉、判断和情绪的许多自动过程所共有的。
  - 现译：它们在评估财务结果时起着关键的作用，知觉、判断和情绪中的许多自动过程也都有这些特征。
  - 处理：Astra 复核通过。“是……所共有的”照搬 are common to

- 英文：Evaluation is relative to a neutral reference point, which is sometimes referred to as an “adaptation level.”
  - 原译：评估是相对于一个中性的参照点进行的，这个参照点有时也叫作“适应水平”。
  - 现译：- 评估以一个中性的参照点为基准，这个参照点有时也叫作“适应水平”。
  - 处理：按复核意见修改。虚化动词“进行”，“相对于……进行的” 复核：“评估是相对的”含糊且与后面的“以……为基准”重复；原文只需说明评估所依据的参照点。

- 英文：For financial outcomes, the usual reference point is the status quo, but it can also be the outcome that you expect, or perhaps the outcome to which you feel entitled, for example, the raise or bonus that your colleagues receive.
  - 原译：对于财务结果，通常的参照点是现状，但它也可以是你预期的结果，或者你觉得自己应得的结果，比如你的同事们得到的加薪或奖金。
  - 现译：财务结果的参照点通常是现状，但也可以是你预期的结果，或者是你觉得自己应得的结果，比如同事们拿到的加薪或奖金。
  - 处理：Astra 复核通过。“对于……”开头，多余的“它”“你的”

- 英文：This asymmetry between the power of positive and negative expectations or experiences has an evolutionary history.
  - 原译：正面与负面的预期或体验在力量上的这种不对称，有其演化上的来历。
  - 现译：正面和负面的预期或体验，影响力并不相等；这种不对称有其演化根源。
  - 处理：按复核意见修改。抽象名词作主语，前面堆了长定语 复核：“力量并不对称”“有它演化上的来历”仍然生硬；power 在这里指预期或体验的影响力。

- 英文：When participants in an experiment were instructed to “think like a trader,” they became less loss averse and their emotional reaction to losses (measured by a physiological index of emotional arousal) was sharply reduced.
  - 原译：在一项实验中，参与者被要求“像交易员一样思考”，结果他们对损失的厌恶程度降低了，对损失的情绪反应（用情绪唤醒的一项生理指标来衡量）也大幅减弱。
  - 现译：有一项实验让参与者“像交易员一样思考”，结果他们没那么厌恶损失了，对损失的情绪反应（用情绪唤醒的一项生理指标来衡量）也大幅减弱。
  - 处理：Astra 复核通过。“被要求”被动句，“厌恶程度降低”名词化

- 英文：Ignore any social considerations, do not try to appear either bold or cautious, and focus only on the subjective impact of the possible loss and the offsetting gain.
  - 原译：不要考虑任何社会因素，不要刻意表现得大胆或谨慎，只关注可能的损失和用来抵消它的收益在你心里的主观分量。
  - 现译：不要考虑任何社会因素，不要刻意表现得大胆或谨慎，只关注两样东西在你心里的分量：可能的损失，以及用来抵消它的收益。
  - 处理：Astra 复核通过。宾语前堆了很长的定语

- 英文：Even a lousy lawyer could have you declared legally insane for turning down this gamble.
  - 原译：哪怕是一个蹩脚的律师，也能凭你拒绝这个赌局这一点，让法庭宣布你在法律上精神失常。
  - 现译：哪怕是一个蹩脚的律师，也能以你拒绝了这个赌局为由，让法庭宣布你在法律上精神失常。
  - 处理：Astra 复核通过。“凭……这一点”搭配生硬

- 英文：So far in this part of the book I have extolled the virtues of prospect theory and criticized the rational model and expected utility theory.
  - 原译：到目前为止，在本书的这一部分里，我一直在称赞前景理论的优点，批评理性模型和期望效用理论。
  - 现译：本书这一部分写到这里，我一直在称赞前景理论的优点，批评理性模型和期望效用理论。
  - 处理：Astra 复核通过。两个状语照搬英文顺序堆在句首

- 英文：This assumption is truly necessary, and it would be undermined by introducing the Humans of prospect theory, whose evaluations of outcomes are unreasonably short-sighted.
  - 原译：这个假定确实是必要的，而如果引入前景理论中的普通人，这个假定就会被动摇，因为普通人对结果的评估目光短浅得不合理。
  - 现译：这个假定确实是必要的，而引入前景理论里的普通人就会动摇它，因为普通人评估结果时目光短浅，到了不合理的地步。
  - 处理：Astra 复核通过。“被动摇”被动句，“对结果的评估”名词化

- 英文：The basic concepts of economics are essential intellectual tools, which are not easy to grasp even with simplified and unrealistic assumptions about the nature of the economic agents who interact in markets.
  - 原译：经济学的基本概念是必不可少的思维工具，即使对市场中相互作用的经济主体的性质作了简化而不切实际的假定，这些概念也不容易掌握。
  - 现译：经济学的基本概念是必不可少的思维工具，即使把在市场上相互打交道的经济主体设想得简单而不切实际，这些概念也不容易掌握。
  - 处理：Astra 复核通过。“对……的性质作了……的假定”，的字连串

- 英文：Furthermore, the failure of rationality that is built into prospect theory is often irrelevant to the predictions of economic theory, which work out with great precision in some situations and provide good approximations in many others.
  - 原译：此外，前景理论里本来就包含的理性失灵，往往与经济理论的预测无关：这些预测在某些情境中非常精确，在许多其他情境中也能给出不错的近似。
  - 现译：此外，前景理论本身就包含了理性的失灵，而这一点往往与经济理论的预测无关：这些预测在某些情境中非常精确，在其他许多情境中也是不错的近似。
  - 处理：Astra 复核通过。带长定语的抽象名词作主语

- 英文：In some contexts, however, the difference becomes significant: the Humans described by prospect theory are guided by the immediate emotional impact of gains and losses, not by long-term prospects of wealth and global utility.
  - 原译：然而在某些情境中，这种差别就变得很重要了：指引前景理论所描述的普通人的，是收益和损失带来的即时情绪冲击，并非财富的长远前景和总体效用。
  - 现译：前景理论描述的普通人，作选择的依据是收益和损失带来的即时情绪冲击，而非财富的长远前景和总体效用。
  - 处理：按复核意见修改。“指引……的，是……”的字结构绕口 复核：“前景理论描述的普通人，引导他们的是……”先提出话题再用代词重述，句式仍然绕口。

- 英文：Prospect theory has flaws of its own, and theory-induced blindness to these flaws has contributed to its acceptance as the main alternative to utility theory.
  - 原译：前景理论也有它自己的缺陷，而它能被接受为效用理论的主要替代理论，部分原因正是人们对这些缺陷也有理论导致的盲目。
  - 现译：这也是它能被接受为效用理论主要替代理论的原因之一。
  - 处理：复核后重写。“被接受为”被动句直译，多余的“它” 复核：acceptance 表示被接受，改成“被公认”加强了共识程度，原文没有这一限定。

- 英文：Winning nothing is a nonevent in the first two cases, and assigning it a value of zero makes good sense.
  - 原译：在前两种情况下，什么也赢不到根本算不上一回事，给它赋予零值很有道理。
  - 现译：在前两种情况下，什么也赢不到根本算不上一回事，把它的价值定为零很有道理。
  - 处理：Astra 复核通过。“给它赋予零值”是 assign a value 的直译

- 英文：Like a salary increase that has been promised informally, the high probability of winning the large sum sets up a tentative new reference point.
  - 原译：就像一次非正式许诺过的加薪一样，赢得一大笔钱的高概率，确立了一个暂定的新参照点。
  - 现译：这就像一次非正式许诺过的加薪，确立了一个暂定的新参照点。
  - 处理：复核后重写。抽象名词“……的高概率”作主语 复核：informally 是“非正式地”，不等于“口头”；非正式许诺也可能通过书面方式作出，改写擅自限定了承诺方式。

- 英文：Relative to your expectations, winning nothing will be experienced as a large loss.
  - 原译：相对于你的预期，什么也赢不到会被体验为一次巨大的损失。
  - 现译：和你的预期相比，什么也没赢到，你会觉得是一次巨大的损失。
  - 处理：Astra 复核通过。“会被体验为”被动句直译

- 英文：Prospect theory cannot cope with this fact, because it does not allow the value of an outcome (in this case, winning nothing) to change when it is highly unlikely, or when the alternative is very valuable.
  - 原译：前景理论无法应对这个事实，因为当一个结果（这里是什么也赢不到）极不可能发生时，或者当另一种结果价值很高时，前景理论不允许这个结果的价值发生变化。
  - 现译：前景理论无法应对这个事实，因为在这个理论里，一个结果（这里是什么也赢不到）的价值，不能因为这个结果极不可能发生而改变，也不能因为另一种结果价值很高而改变。
  - 处理：Astra 复核通过。“当……时，或者当……时”照搬 when 从句

- 英文：Disappointment and the anticipation of disappointment are real, however, and the failure to acknowledge them is as obvious a flow as the counterexamples that I invoked to criticize Bernoulli’s theory.
  - 原译：然而，失望和对失望的预期都是真实存在的，不承认它们，是一个明显的缺陷，其明显程度不亚于我批评伯努利理论时援引的那些反例。
  - 现译：然而，失望和对失望的预期都是真实存在的；不承认它们的存在，就是一个明显的缺陷，和我批评伯努利理论时援引的那些反例一样明显。
  - 处理：按复核意见修改。“其明显程度不亚于”照搬 as obvious … as 复核：删除停顿后，“不承认它们是一个明显的缺陷”容易被理解为“不承认它们属于缺陷”，改变否定范围。原意是“不承认这些情绪的存在”本身构成缺陷。

- 英文：The two theories share the assumption that available options in a choice are evaluated separately and independently, and that the option with the highest value is selected.
  - 原译：这两种理论有一个共同的假定：在一次选择中，可供选择的各个选项是分别、独立地评估的，价值最高的那个选项会被选中。
  - 现译：这两种理论有一个共同的假定：在一次选择中，可供选择的各个选项是分别、独立地评估的，最后选中的是价值最高的那一个。
  - 处理：Astra 复核通过。“会被选中”被动句

- 英文：In regret, the experience of an outcome depends on an option you could have adopted but did not.
  - 原译：在后悔中，你对一个结果的体验，取决于一个你本可以选择却没有选的选项。
  - 现译：后悔时，你对一个结果的感受，取决于你本可以选、却没有选的那个选项。
  - 处理：复核后重写。“在后悔中”直译 in regret，“对……的体验”名词化 复核：“你怎样体验一个结果”仍是生硬的直译；这里说的是对结果的感受，不是体验的方法。

- 英文：The problem is that regret theories make few striking predictions that would distinguish them from prospect theory, which has the advantage of being simpler.
  - 原译：问题在于，后悔理论很少作出能把它们与前景理论区分开来的醒目预测，而前景理论的优势在于更简单。
  - 现译：问题在于，后悔理论很少能作出这样的预测：既引人注目，又能将它们与前景理论区分开来。而前景理论的优势在于更简单。
  - 处理：按复核意见修改。定语从句前置成长定语 复核：逗号拆开了限定关系，容易读成后悔理论总体上很少作出醒目预测；原文限定的是能将两种理论区分开的醒目预测。“还有一个优势”也无端暗示另有优势。

- 英文：“He weighs losses about twice as much as gains, which is normal.”
  - 原译：“他看重损失的程度大约是收益的两倍，这很正常。”
  - 现译：“在他心里，损失的分量大约是收益的两倍，这很正常。”
  - 处理：Astra 复核通过。“看重……的程度”不像口语

## 第 27 章 禀赋效应

- 英文：Each “indifference curve” connects the combinations of the two goods that are equally desirable—they have the same utility.
  - 原译：每条“无差异曲线”把由这两种商品构成、同样令人向往的各种组合连在一起，这些组合的效用相同。
  - 现译：每条“无差异曲线”都把这两种商品的若干组合连在一起，这些组合同样令人向往，也就是说效用相同。
  - 处理：Astra 复核通过。名词前堆了两层定语，“把由……构成、……的各种组合”读不顺

- 英文：If you are a salaried employee, the terms of your employment specify a salary and a number of vacation days, which is a point on the map.
  - 原译：如果你是一名领薪水的雇员，你的雇用条件规定了一份薪水和若干天假期，这就是图上的一个点。
  - 现译：如果你是领薪水的雇员，你的雇用条件会规定薪水是多少、假期有几天，这就是图上的一个点。
  - 处理：Astra 复核通过。照搬冠词，“一名”“一份”多余，搭配生硬

- 英文：The standard theory represented in the figure assumes that preferences are stable over time. Positions A and B are equally attractive for both twins and they will need little or no incentive to switch.
  - 原译：图中所代表的标准理论假定，偏好不随时间而变。职位 A 和 B 对两人同样有吸引力，他们几乎不需要激励，甚至完全不需要激励，就会互换。
  - 现译：图中体现的标准理论假定，偏好不随时间而变。职位 A 和 B 对两人同样有吸引力，他们互换时只需要一点点激励，甚至根本不需要。
  - 处理：Astra 复核通过。“所代表的”直译；little or no 硬拆成两个重复的“需要激励”

- 英文：Taking position A changes Albert’s reference point, and when he considers switching to B, his choice has a new structure:
  - 原译：接受职位 A 改变了艾伯特的参照点。当他考虑换到 B 时，他面临的选择有了新的结构：
  - 现译：接受职位 A 以后，艾伯特的参照点变了。他再考虑换到 B 时，面临的选择就有了新的结构：
  - 处理：Astra 复核通过。动名词短语作主语，“当……时，他”代词重复

- 英文：You just had the subjective experience of loss aversion.
  - 原译：你刚刚在主观上体验到了损失厌恶。
  - 现译：你刚刚亲身体会到了损失厌恶。
  - 处理：Astra 复核通过。subjective experience 直译成“在主观上体验”

- 英文：First, tastes are not fixed; they vary with the reference point. Second, the disadvantages of a change loom larger than its advantages, inducing a bias that favors the status quo.
  - 原译：第一，口味不是固定的，它随参照点而变。第二，一项改变的坏处显得比它的好处更重，由此产生一种偏向现状的偏差。
  - 现译：第一，口味不是固定的，会随参照点而变。第二，改变的坏处显得比好处更重，由此产生一种偏向现状的偏差。
  - 处理：Astra 复核通过。多余的代词“它”和量词“一项”

- 英文：Of course, loss aversion does not imply that you never prefer to change your situation; the benefits of an opportunity may exceed even overweighted losses.
  - 原译：当然，损失厌恶并不意味着你永远不愿意改变自己的处境；即使损失被赋予了过高的权重，一个机会带来的好处仍然可能超过这些损失。
  - 现译：当然，损失厌恶并不意味着你永远不愿意改变自己的处境；即使把损失看得过重，一个机会带来的好处仍然可能超过这些损失。
  - 处理：Astra 复核通过。不必要的被动句“被赋予了过高的权重”

- 英文：Thaler always had a sharp wit and an ironic bent, and as a student he amused himself by collecting observations of behavior that the model of rational economic behavior could not explain.
  - 原译：读书时，他以收集各种行为实例为乐，这些行为都是理性经济行为模型解释不了的。
  - 现译：读书时，他以收集理性经济行为模型解释不了的行为实例为乐。
  - 处理：Astra 复核通过。照搬定语从句，拆成“……，这些行为都是……的”

- 英文：If you resemble most of the audience at sold-out events you do not sell.
  - 原译：如果你和门票售罄的演出的大多数观众一样，你就不会卖。
  - 现译：如果你和门票售罄的演出的大多数观众一样，你就不会卖。
  - 处理：复核后退回原译。“的”字连串 复核：“售罄演出”压缩过头，搭配比原译生硬；售罄的是演出门票，不能只为减少“的”字而删去必要成分。

- 英文：Indeed, the shoes that he hands over have always been, from his point of view, a cumbersome proxy for money that he was hoping to collect from some consumer.
  - 原译：其实，在他看来，他交出去的鞋子一直只是钱的一种累赘的替代品，他本来就指望从某个顾客那里收到这笔钱。
  - 现译：其实在他看来，交出去的鞋子一直只是钱的替代品，而且是个累赘，他本来就指望从某个顾客那里收到这笔钱。
  - 处理：Astra 复核通过。“钱的一种累赘的替代品”形容词直译堆在名词前，代词多余

- 英文：Furthermore, you probably do not experience paying the merchant as a loss, because you were effectively holding money as a proxy for the shoes you intended to buy.
  - 原译：此外，你付钱给商人时，大概也不会把它体验为损失，因为你手里的钱实际上就是你打算买的那双鞋的替代品。
  - 现译：此外，你付钱给商人，大概也不会觉得这是损失，因为你手里的钱实际上就是你打算买的那双鞋的替代品。
  - 处理：Astra 复核通过。experience X as a loss 直译成“把它体验为损失”

- 英文：The redemption values differ for different individuals, to represent the fact that the goods traded in markets are more valuable to some people than to others.
  - 原译：不同的人得到的兑换价值不同，用来代表这样一个事实：市场上交易的物品，对有些人比对另一些人更有价值。
  - 现译：代币的兑换价值因人而异，这是为了体现一个事实：市场上交易的物品，对有些人比对另一些人更有价值。
  - 处理：按复核意见修改。to represent the fact that 直译成“用来代表这样一个事实” 复核：“不同的人兑换价值不同”搭配生硬，未说清兑换价值属于代币、因参与者而异。

- 英文：If half the participants in the market were randomly assigned tokens, the theory predicts that half of the tokens will change hands.
  - 原译：如果市场中一半的参与者被随机分到了代币，理论预测一半代币会易手。
  - 现译：如果随机给市场中一半的参与者分发代币，理论预测会有一半代币易手。
  - 处理：Astra 复核通过。不必要的被动句

- 英文：Then we conducted a similar market for an object that we expected people to value for use: an attractive coffee mug, decorated with the university insignia of wherever we were conducting the experiments.
  - 原译：接着，我们又开设了一个类似的市场，交易的是一件我们预计人们会为了使用而看重的物品：一只漂亮的咖啡杯，上面印着我们做实验所在的那所大学的校徽。
  - 现译：接着，我们又开设了一个类似的市场，这次交易的是一只漂亮的咖啡杯，我们预计人们会看重它的使用价值。我们在哪所大学做实验，杯子上就印着哪所大学的校徽。
  - 处理：按复核意见修改。长定语从句前置，“为了使用而看重”生硬；wherever 的意思也没译出 复核：话题转换不顺，且冒号紧接“它的用处”，后面却是在介绍物品，而不是说明用处。

- 英文：Mugs were distributed randomly to half the participants. The Sellers had their mug in front of them, and the Buyers were invited to look at their neighbor’s mug; all indicated the price at which they would trade.
  - 原译：杯子被随机分给一半的参与者。卖方把杯子放在自己面前，买方则被请去看邻座的杯子；所有人都给出了自己愿意成交的价格。
  - 现译：我们把杯子随机分给一半的参与者。卖方面前摆着自己的杯子，买方则受邀看看邻座的杯子；所有人都报出了自己愿意成交的价格。
  - 处理：Astra 复核通过。两个“被”字句照搬英文被动

- 英文：Unlike the Buyers, who had to spend their own money to acquire the good, the Choosers could receive either a mug or a sum of money, and they indicated the amount of money that was as desirable as receiving the good.
  - 原译：买方得花自己的钱才能得到这件物品，选择者则不同，他们可以得到一只杯子，也可以得到一笔钱，他们要给出一个金额，表示多少钱和得到杯子一样让他们满意。
  - 现译：买方得花自己的钱才能得到这件物品，选择者则不同，可以得到一只杯子，也可以得到一笔钱，他们要报出一个金额，表示多少钱和得到杯子一样让他们满意。
  - 处理：Astra 复核通过。代词“他们”连用

- 英文：Buyers and Choosers set similar cash values, although the Buyers have to pay for the mug, which is free for the Choosers. This is what we would expect if Buyers do not experience spending money on the mug as a loss.
  - 原译：买方和选择者定出的现金价值相近，尽管买方要花钱买杯子，而杯子对选择者来说是免费的。如果买方并不把花钱买杯子体验为损失，这正是我们会预料到的结果。
  - 现译：买方要花钱买杯子，杯子对选择者来说却是免费的，可两组定出的现金价值相近。如果买方并不觉得花钱买杯子是损失，我们预料的正是这样的结果。
  - 处理：Astra 复核通过。让步从句“尽管……”照搬英文后置；“体验为损失”直译

- 英文：The ratio is very close to the loss aversion coefficient in risky choice, as we might expect if the same value function for gains and losses of money is applied to both riskless and risky decisions.
  - 原译：这个比例与有风险的选择中的损失厌恶系数非常接近；如果同一个关于金钱得失的价值函数同时适用于无风险的决策和有风险的决策，这正是我们会预料到的。
  - 现译：这个比例与风险选择中的损失厌恶系数非常接近；如果无论决策有没有风险，金钱得失都适用同一个价值函数，这正是我们会预料到的。
  - 处理：Astra 复核通过。“的”字连串，“同一个关于……的价值函数”定语冗长

- 英文：As economists would predict, customers tend to increase their purchases of eggs, orange juice, or fish when prices drop and to reduce their purchases when prices rise; however, in contrast to the predictions of economic theory, the effect of price increases (losses relative to the reference price) is about twice as large as the effect of gains.
  - 原译：正如经济学家会预测的那样，鸡蛋、橙汁或鱼降价时，顾客往往会多买，涨价时会少买；然而，与经济理论的预测不同，涨价（相对于参照价格的损失）的影响，大约是降价这种收益的影响的两倍。
  - 现译：涨价（相对于参照价格的损失）的影响，大约是降价（收益）的影响的两倍。
  - 处理：复核后重写。“降价这种收益的影响的两倍”的字连串 复核：原文比较的是涨价与降价各自产生的影响。删掉后一个“影响”，变成了拿涨价的影响与降价收益本身相比，比较对象错位。

- 英文：The original demonstration of an asymmetry between selling prices and buying prices (or, more convincingly, between selling and choosing) was very important in the initial acceptance of the ideas of reference point and loss aversion.
  - 原译：在参照点和损失厌恶这两个观念起初被人们接受的过程中，这些实验起了非常重要的作用。
  - 现译：参照点和损失厌恶这两个观念起初能被人们接受，这些实验起了非常重要的作用。
  - 处理：Astra 复核通过。“在……的过程中”套语

- 英文：More surprisingly, List found a large effect of trading experience on the endowment effect for new goods.
  - 原译：更令人惊讶的是，李斯特发现，对于新物品的禀赋效应，交易经验也有很大的影响。
  - 现译：更令人惊讶的是，李斯特发现，交易经验对新物品的禀赋效应也有很大影响。
  - 处理：Astra 复核通过。“对于……”提前，语序别扭

- 英文：Participants displayed an endowment effect only if they had physical possession of the good for a while before the possibility of trading it was mentioned.
  - 原译：只有当参与者在得知可以交换之前已经实际持有该物品一段时间，他们才会表现出禀赋效应。
  - 现译：参与者只有在得知可以交换之前，已经实际持有物品一段时间，才会表现出禀赋效应。
  - 处理：复核后重写。“只有当……，他们才”代词重复，“该物品”公文腔 复核：physical possession 指实际占有或持有物品，不要求拿在手里。改写增加了手持物品这一具体实验条件，窄化了原意。

- 英文：Recent studies of the psychology of “decision making under poverty” suggest that the poor are another group in which we do not expect to find the endowment effect.
  - 原译：近来关于“贫困状态下的决策”心理的研究表明，穷人是另一个我们预计不会出现禀赋效应的群体。
  - 现译：近来有关“贫困状态下的决策”的心理学研究显示，穷人可能也是一个不会出现禀赋效应的群体。
  - 处理：复核后重写。“另一个我们预计……的群体”照搬定语从句 复核：“穷人是另一个群体”脱离后面的特征说明，读起来悬空；suggest 的审慎推断语气也宜保留。

- 英文：Their problem is that all their choices are between losses.
  - 原译：他们的问题在于，他们所有的选择都是在损失之间做选择。
  - 现译：他们的问题在于，每一次选择都只能在损失之间选。
  - 处理：Astra 复核通过。代词重复，“选择……做选择”累赘

- 英文：There may also be cultural differences in the attitude toward money, and especially toward the spending of money on whims and minor luxuries, such as the purchase of a decorated mug.
  - 原译：对待金钱的态度，尤其是对待一时兴起花钱、买些小小奢侈品（比如买一只有装饰图案的杯子）的态度，也可能存在文化差异。
  - 现译：人们对待金钱的态度也可能存在文化差异，尤其是对一时兴起花钱、买些小小奢侈品（比如买一只有装饰图案的杯子）的态度。
  - 处理：Astra 复核通过。长主语堆在句首，谓语迟迟不出现

- 英文：“He just hates the idea of selling his house for less money than he paid for it. Loss aversion is at work.”
  - 原译：他就是受不了以低于买入价的价格卖房子。
  - 现译：他就是受不了房子卖得比买的时候便宜。
  - 处理：Astra 复核通过。口头话里用“以低于……的价格”书面腔

- 英文：“He is a miser, and treats any dollar he spends as a loss.”
  - 原译：他是个守财奴，花出去的每一块钱都被他当成损失。
  - 现译：他是个守财奴，花出去的每一块钱，他都当成损失。
  - 处理：Astra 复核通过。不必要的“被”字句

## 第 28 章 坏事

- 英文：This is odd, because the idea that people evaluate many outcomes as gains and losses, and that losses loom larger than gains, surprises no one.
  - 原译：这有点奇怪，因为人们把许多结果评估为收益和损失，而且损失显得比收益更重，这种想法谁也不会觉得意外。
  - 现译：这有点奇怪，因为人们会把许多结果看作收益或损失，而且损失显得比收益更重，这种想法谁也不会觉得意外。
  - 处理：Astra 复核通过。evaluate X as 直译成“评估为”

- 英文：We can also trace the consequences of loss aversion in surprisingly diverse observations: only out-of-pocket losses are compensated when goods are lost in transport; attempts at large-scale reforms very often fail; and professional golfers putt more accurately for par than for a birdie.
  - 原译：我们还能在各种各样的观察中找到损失厌恶的后果，它们的多样程度出人意料：货物在运输中丢失时，只有自掏腰包的实际损失能得到赔偿；大规模改革的尝试常常失败；职业高尔夫球手推杆保标准杆时，比推杆抓小鸟球时推得更准。
  - 现译：我们还能在许多观察结果中看出损失厌恶的影响，涉及的领域之广令人意想不到：货物在运输中丢失时，只有实际花掉的成本能得到赔偿；大规模改革的尝试常常失败；职业高尔夫球手推杆保标准杆时，比推杆抓小鸟球时推得更准。
  - 处理：复核后重写。surprisingly diverse 拆成抽象名词“多样程度出人意料” 复核：trace 在这里是从观察中辨认出影响，“追溯到……后果”搭配不当；“自掏腰包的实际损失”也仍然生硬。

- 英文：Clever as she was, my grandmother would have been surprised by the specific predictions from a general idea she considered obvious.
  - 原译：我的祖母虽然聪明，但一个她认为显而易见的一般性想法竟能引出这么具体的预测，她也会感到惊讶。
  - 现译：我的祖母虽然聪明，可她认为显而易见的一条笼统道理，竟能引出这么具体的预测，她要是知道了，也会感到惊讶。
  - 处理：Astra 复核通过。“一个她认为……的一般性想法”定语堆叠，虚拟语气没有交代

- 英文：The two pictures were presented to people lying in a brain scanner.
  - 原译：研究者把这两张图呈现给躺在脑部扫描仪里的人。
  - 现译：研究者让躺在脑部扫描仪里的人看这两张图。
  - 处理：Astra 复核通过。present to 直译成“呈现给”

- 英文：Images of the brain showed an intense response of the amygdala to a threatening picture that the viewer did not recognize.
  - 原译：脑成像显示，观看者并没有认出那张有威胁的图片，杏仁核却对它作出了强烈的反应。
  - 现译：脑成像显示，观看者并没有认出那张有威胁的图片，杏仁核却对它反应强烈。
  - 处理：Astra 复核通过。虚化动词“作出……反应”

- 英文：The same circuit also causes schematic angry faces (a potential threat) to be processed faster and more efficiently than schematic happy faces.
  - 原译：同一条回路还使得示意性的愤怒面孔（一种潜在的威胁）比示意性的快乐面孔处理得更快、更有效率。
  - 现译：也是这条回路，让大脑处理示意性的愤怒面孔（一种潜在的威胁）时，比处理示意性的快乐面孔更快、更有效率。
  - 处理：Astra 复核通过。cause X to be processed 照搬成“使得……处理得更快”，施事不清

- 英文：No comparably rapid mechanism for recognizing good news has been detected.
  - 原译：目前还没有发现识别好消息的同样快速的机制。
  - 现译：目前还没有发现能同样快速地识别好消息的机制。
  - 处理：Astra 复核通过。定语次序照搬英文，“的”字连用

- 英文：Of course, we and our animal cousins are quickly alerted to signs of opportunities to mate or to feed, and advertisers design billboards accordingly. Still, threats are privileged above opportunities, as they should be.
  - 原译：当然，我们和我们的动物表亲都会很快注意到交配或觅食机会的迹象，广告商也据此设计广告牌。尽管如此，威胁还是比机会享有优先权，这也理所应当。
  - 现译：当然，我们和动物表亲都会很快注意到交配或觅食机会的迹象，广告商也据此设计广告牌。尽管如此，威胁还是优先于机会，这也理所应当。
  - 处理：复核后重写。多余物主代词；privileged 直译成“享有优先权” 复核：“威胁还是比机会优先”搭配生硬，不如原译顺畅。“享有优先权”在这里准确、自然，并非必须消除的翻译腔。

- 英文：Emotionally loaded words quickly attract attention, and bad words (war, crime) attract attention faster than do happy words (peace, love).
  - 原译：带有情绪色彩的词会很快吸引注意，而坏词（战争、犯罪）吸引注意的速度比快乐的词（和平、爱）更快。
  - 现译：带有情绪色彩的词会很快吸引注意，而令人不快的词（战争、犯罪）比令人愉快的词（和平、爱）更快吸引注意。
  - 处理：按复核意见修改。“吸引注意的速度比……更快”名词化比较 复核：“坏词”容易被理解为粗话或不当用词，“快乐的词”也不自然；这里区分的是引起负面情绪与愉快情绪的词。

- 英文：Of course, the daily goal is much easier to achieve (and exceed) on some days than on others.
  - 原译：当然，每天的目标在有些日子比在另一些日子容易达到（和超过）得多。
  - 现译：当然，有些日子要达到（和超过）每天的目标，比另一些日子容易得多。
  - 处理：复核后重写。照搬 on some days than on others 的比较结构 复核：much easier than 只比较不同日子的难易程度，并未断言某些日子“很容易”。改写把相对比较改成了绝对判断。

- 英文：If in his best years Tiger Woods had managed to putt as well for birdies as he did for par, his average tournament score would have improved by one stroke and his earnings by almost $1 million per season.
  - 原译：如果泰格·伍兹在他的巅峰时期推小鸟球能推得和推标准杆一样好，他每场比赛的平均成绩就会提高一杆，每个赛季的收入会增加将近 100 万美元。
  - 现译：如果泰格·伍兹在巅峰时期推小鸟球能推得和推标准杆一样好，他每场比赛的平均成绩就会提高一杆，每个赛季的收入会增加将近 100 万美元。
  - 处理：Astra 复核通过。多余的物主代词“他的”

- 英文：These fierce competitors certainly do not make a conscious decision to slack off on birdie putts, but their intense aversion to a bogey apparently contributes to extra concentration on the task at hand.
  - 原译：这些争强好胜的选手当然不会有意识地决定在小鸟球推杆上松劲，但他们对柏忌的强烈厌恶，显然有助于他们在眼前的任务上格外专注。
  - 现译：这些争强好胜的选手当然不会有意识地决定在小鸟球推杆上松劲，但他们对柏忌的强烈厌恶，似乎有助于他们格外专注于眼前这一杆。
  - 处理：按复核意见修改。task at hand 直译成“眼前的任务” 复核：apparently 在这里保留了对原因解释的推测语气；原译和改写中的“显然”都显得过于确定。

- 英文：The existing terms define reference points, and a proposed change in any aspect of the agreement is inevitably viewed as a concession that one side makes to the other.
  - 原译：现有的条款确定了参照点，协议任何方面的修改提议，都不可避免地被看作一方对另一方的让步。
  - 现译：现有的条款确定了参照点，无论提议修改协议的哪个方面，都不可避免地会被看作一方对另一方的让步。
  - 处理：Astra 复核通过。名词短语“协议任何方面的修改提议”作主语

- 英文：The concessions you make to me are my gains, but they are your losses; they cause you much more pain than they give me pleasure.
  - 原译：你对我作出的让步是我的收益，却是你的损失；它们给你带来的痛苦，远远超过给我带来的快乐。
  - 现译：你对我的让步是我的收益，却是你的损失；它们给你带来的痛苦，远远超过给我带来的快乐。
  - 处理：Astra 复核通过。虚化动词“作出”

- 英文：The same is true, of course, of the very painful concessions you demand from me, which you do not appear to value sufficiently!
  - 原译：当然，你要求我作出的那些非常痛苦的让步也是如此，而你似乎并没有充分重视它们！
  - 现译：当然，反过来也一样：你要我做的那些让步让我非常痛苦，你却似乎没有充分看重它们！
  - 处理：Astra 复核通过。照搬非限制性从句，“作出”虚化，“重视它们”代词生硬

- 英文：Because negotiators are influenced by a norm of reciprocity, a concession that is presented as painful calls for an equally painful (and perhaps equally inauthentic) concession from the other side.
  - 原译：由于谈判者受到互惠规范的影响，一方作出的让步如果被说成是痛苦的，就要求对方作出同样痛苦（也许同样不真实）的让步。
  - 现译：谈判者受互惠规范的影响，所以一方如果把自己的让步说得很痛苦，对方就得做出同样痛苦（也许同样不真实）的让步。
  - 处理：Astra 复核通过。被动句加两个“作出”，以“让步”作主语去“要求”

- 英文：We also found that the moral rules by which the public evaluates what firms may or may not do draw a crucial distinction between losses and gains.
  - 原译：我们还发现，公众用来评判企业可以做什么、不可以做什么的道德规则，在损失和收益之间划出了一条关键的界线。
  - 现译：我们还发现，公众评判企业可以做什么、不可以做什么时，依据的道德规则在损失和收益之间划出了一条关键的界线。
  - 处理：Astra 复核通过。by which 定语从句整个堆在“道德规则”前

- 英文：We described the rules as defining dual entitlements to the firm and to individuals with whom it interacts.
  - 原译：我们把这些规则描述为规定了双重权益：一重属于企业，一重属于与企业打交道的个人。
  - 现译：按照我们的描述，这些规则规定了双重权益：一重属于企业，一重属于与企业打交道的个人。
  - 处理：Astra 复核通过。describe X as doing 直译成“描述为规定了”

- 英文：They showed indignation only when a firm exploited its power to break informal contracts with workers or customers, and to impose a loss on others in order to increase its profit.
  - 原译：只有当企业利用自己的力量，撕毁与员工或顾客之间的非正式契约，把损失强加给别人来增加自己的利润时，他们才表现出愤慨。
  - 现译：只有企业利用自己的力量撕毁与员工或顾客之间的非正式契约，把损失强加给别人来增加自己的利润，他们才会表现出愤慨。
  - 处理：Astra 复核通过。“只有当……时”套语包着很长的状语

- 英文：Remarkably, altruistic punishment is accompanied by increased activity in the “pleasure centers” of the brain.
  - 原译：值得注意的是，利他惩罚伴随着大脑“快乐中枢”活动的增强。
  - 现译：值得注意的是，人们实施利他惩罚时，大脑“快乐中枢”的活动会增强。
  - 处理：Astra 复核通过。is accompanied by 直译成“伴随着……的增强”，抽象名词作宾语

- 英文：However, our brains are not designed to reward generosity as reliably as they punish meanness.
  - 原译：然而，我们的大脑生来就不能像惩罚刻薄那样可靠地奖赏慷慨。
  - 现译：然而，我们的大脑奖赏慷慨，天生就不如惩罚刻薄那么可靠。
  - 处理：复核后重写。照搬 as reliably as 的长状语，句子头重 复核：“生来奖赏慷慨”连接生硬，容易把“生来”理解为修饰奖赏动作；需要明确天生存在的是两种反应在可靠程度上的差异。

- 英文：In a more recent discussion, Eyal Zamir makes the provocative point that the distinction drawn in the law between restoring losses and compensating for foregone gains may be justified by their asymmetrical effects on individual well-being.
  - 原译：法律把弥补损失和补偿未能获得的收益区别对待，也许可以用两者对个人幸福的不对称影响来说明它的合理性。
  - 现译：法律把弥补损失与补偿未能获得的收益区别对待，也许有其道理，因为蒙受损失与未能获得收益对个人幸福的影响并不对称。
  - 处理：按复核意见修改。may be justified by 直译成“可以用……来说明它的合理性” 复核：结合下一句，产生不对称影响的是蒙受损失与未能获得收益，而不是两种补偿行为。“两者”紧接补偿行为，指代容易错位。

## 第 29 章 四重模式

- 英文：People who buy lottery tickets in vast amounts show themselves willing to pay much more than expected value for very small chances to win a large prize.
  - 原译：大量购买彩票的人表明，为了赢得大奖的极小机会，他们愿意付出远高于期望值的价钱。
  - 现译：大量购买彩票的人用行动表明，为了极小的中大奖机会，他们愿意付出远高于期望值的价钱。
  - 处理：Astra 复核通过。“人表明”硬套 show themselves，“赢得大奖的极小机会”修饰关系含混

- 英文：If such an event actually happens in your life, you should know that a large industry of “structured settlements” exists to provide certainty at a hefty price, by taking advantage of the certainty effect.
  - 原译：如果你的生活中真的发生了这样的事，你应该知道，有一个庞大的“结构化和解”行业，专门利用确定性效应，以高昂的价格向人们提供确定性。
  - 现译：如果你真的遇上这种事，你应该知道，有一个庞大的“结构化和解”行业，专门利用确定性效应，以高昂的价格向人们提供确定性。
  - 处理：Astra 复核通过。“你的生活中发生了这样的事”照搬 happens in your life

- 英文：When a loved one is wheeled into surgery, a 5% risk that an amputation will be necessary is very bad—much more than half as bad as a 10% risk.
  - 原译：当你所爱的人被推进手术室时，5% 的截肢风险就已经很糟糕了，它的糟糕程度远远超过 10% 风险的一半。
  - 现译：你所爱的人被推进手术室时，5% 的截肢风险就已经很糟糕了，糟糕程度远远超过 10% 风险的一半。
  - 处理：复核后重写。“当……时”加多余代词，“它的糟糕程度”抽象名词作主语 复核：“10% 风险的一半那么糟”容易被理解为把风险概率减半，而原文比较的是两种风险带来的糟糕感受。原译明确保留了“糟糕程度”这一比较基准，也更容易读懂。

- 英文：He also introduced me to a famous challenge to that theory.
  - 原译：他还向我介绍了对这个理论的一个著名挑战。
  - 现译：他还向我介绍了这个理论遇到的一个著名挑战。
  - 处理：Astra 复核通过。“对……的一个挑战”照搬 challenge to 结构

- 英文：Compare the two problems, and you will see that the two urns of problem B are more favorable versions of the urns of problem A, with 37 white marbles replaced by red winning marbles in each urn.
  - 原译：比较一下这两个问题，你会发现，问题 B 的两个罐子是问题 A 两个罐子的更有利版本：每个罐子里都有 37 颗白弹珠换成了能让人赢的红弹珠。
  - 现译：比较一下这两个问题，你会发现，问题 B 的两个罐子是从问题 A 的两个罐子改过来的，而且改得对你更有利：每个罐子里都有 37 颗白弹珠换成了能让人赢的红弹珠。
  - 处理：复核后重写。“……的更有利版本”直译 more favorable versions of 复核：“两个罐子，就是把……改得更有利了”主谓搭配不顺，“改得更有利”也没有明确对谁有利。

- 英文：Allais had intended this announcement to be a bombshell: the leading decision theorists in the world had preferences that were inconsistent with their own view of rationality! He apparently believed that his audience would be persuaded to give up the approach that he rather contemptuously labeled “the American school” and adopt an alternative logic of choice that he had developed.
  - 原译：阿莱本来打算让这番宣布成为一枚重磅炸弹：世界上顶尖的决策理论家，他们的偏好竟然与他们自己的理性观不一致！他显然相信，听众会被说服，放弃被他颇为轻蔑地称为“美国学派”的那套方法，转而采用他自己发展出来的另一种选择逻辑。
  - 现译：阿莱本来打算让这番话成为一枚重磅炸弹：世界上顶尖的决策理论家，偏好竟然与自己的理性观不一致！他似乎相信，听众会被他说服，放弃他颇为轻蔑地称作“美国学派”的那套方法，转而采用他自己发展出来的另一种选择逻辑。
  - 处理：按复核意见修改。“这番宣布”搭配生硬，“……家，他们的……他们自己”多余代词，一句两个“被” 复核：apparently 在这里表示作者对阿莱想法的推测，“显然相信”把确定程度说重了；这是原译已有、改写仍保留的问题。

- 英文：As often happens when a theory that has been widely adopted and found useful is challenged, they noted the problem as an anomaly and continued using expected utility theory as if nothing had happened. In contrast, decision theorists—a mixed collection of statisticians, economists, philosophers, and psychologists—took Allais’s challenge very seriously.
  - 原译：一个被广泛采用、也被证明有用的理论受到挑战时，常常会出现这样的情形：他们只把这个问题记作一个反常现象，然后若无其事地继续使用期望效用理论。相比之下，决策理论家，也就是由统计学家、经济学家、哲学家和心理学家组成的一个混杂群体，非常认真地对待阿莱的挑战。
  - 现译：一个已经广为采用、实践中也证明有用的理论受到挑战时，常常会出现这样的情形：他们只把这个问题记作一个反常现象，然后若无其事地继续使用期望效用理论。相比之下，决策理论家非常认真地对待阿莱的挑战，这群人来自不同领域，有统计学家、经济学家、哲学家，也有心理学家。
  - 处理：复核后重写。连用两个“被”；同位语“也就是由……组成的一个混杂群体”把主语和谓语隔开 复核：“也证明有用”搭配生硬；found useful 指人们发现或认为理论有用。“这群人成分很杂”容易带出贬义，原文主要说明其学科背景多样。

- 英文：Amos had little patience for these efforts; he called the theorists who tried to rationalize violations of utility theory “lawyers for the misguided.”
  - 原译：阿莫斯对这些努力很不耐烦；那些试图为违背效用理论的做法寻找合理解释的理论家，被他称为“误入歧途者的辩护律师”。
  - 现译：阿莫斯对这些努力没什么耐心；有些理论家试图为违背效用理论的做法找合理的解释，他管这些人叫“误入歧途者的辩护律师”。
  - 处理：Astra 复核通过。名词前定语过长，又改成“被他称为”的被动句

- 英文：However, when an unlikely event becomes the focus of attention, we will assign it much more weight than its probability deserves.
  - 原译：然而，当一个不太可能发生的事件成为注意的焦点时，我们给它的权重会远远超过它的概率所应得的。
  - 现译：然而，一旦某个不太可能发生的事件成了关注的焦点，我们给它的权重就会远远超过按它的概率本该给的。
  - 处理：复核后重写。“当……时”句式，“注意的焦点”搭配生硬 复核：“它的概率所应得的”仍是生硬直译，没有清楚表达比较基准是按发生概率本应赋予的权重。

- 英文：A cancer risk of 0.001% is not easily distinguished from a risk of 0.00001%, although the former would translate to 3,000 cancers for the population of the United States, and the latter to 30.
  - 原译：0.001% 的癌症风险和 0.00001% 的癌症风险不容易区分开来，尽管就美国的人口而言，前者意味着 3,000 例癌症，后者只意味着 30 例。
  - 现译：0.001% 的癌症风险和 0.00001% 的癌症风险不容易区分开来，可是按美国的人口算，前者意味着 3,000 例癌症，后者只有 30 例。
  - 处理：Astra 复核通过。让步从句“尽管……”照英文后置，“就……而言”书面套话

- 英文：When you pay attention to a threat, you worry—and the decision weights reflect how much you worry.
  - 原译：当你注意到一个威胁时，你就会担心，而决策权重反映的就是你担心的程度。
  - 现译：一旦你关注某个威胁，就会担心，而决策权重反映的正是你有多担心。
  - 处理：按复核意见修改。“当……时”加重复的“你”，“担心的程度”名词化 复核：pay attention to 指关注、把注意力放在威胁上，不只是“注意到”威胁的存在；原译中的这一偏差仍未修正。

- 英文：The question below is adapted from a study of the rationality of consumer valuations of health risks, which was published by a team of economists in the 1980s.
  - 原译：下面这个问题改编自一项关于消费者对健康风险的估价是否理性的研究，这项研究是一组经济学家在 20 世纪 80 年代发表的。
  - 现译：下面这个问题改编自一组经济学家在 20 世纪 80 年代发表的一项研究，这项研究考察的是消费者对健康风险的估价是否理性。
  - 处理：Astra 复核通过。“一项关于……的研究”定语过长，后面又照搬 which 从句补说发表者

- 英文：When Amos and I began our work on prospect theory, we quickly reached two conclusions: people attach values to gains and losses rather than to wealth, and the decision weights that they assign to outcomes are different from probabilities.
  - 原译：阿莫斯和我开始研究前景理论时，很快得出了两个结论：人们赋予价值的对象是收益和损失，而非财富；人们给结果赋予的决策权重与概率不同。
  - 现译：阿莫斯和我开始研究前景理论时，很快得出了两个结论：人们赋予价值的是收益和损失，而不是财富；人们给结果赋予的决策权重与概率不同。
  - 处理：Astra 复核通过。“赋予价值的对象是”多出“对象”，读起来像公文

- 英文：The name has stuck.
  - 原译：这个名称就此沿用下来。
  - 现译：这个名称就此沿用下来。
  - 处理：复核后退回原译。“就此沿用下来”生硬，不像口语 复核：has stuck 强调名称一直沿用下来；“叫开了”侧重名称传播开来，改变了原文的重点。原译准确自然。

- 英文：The top left is the one that Bernoulli discussed: people are averse to risk when they consider prospects with a substantial chance to achieve a large gain.
  - 原译：左上格是伯努利讨论过的情况：当人们考虑的前景有相当大的机会获得一大笔收益时，他们会规避风险。
  - 现译：左上格是伯努利讨论过的情况：面对有相当大机会获得一大笔收益的前景，人们会规避风险。
  - 处理：Astra 复核通过。“当……时，他们会……”照搬英文从句，多余代词

- 英文：Here again, people buy more than protection against an unlikely disaster; they eliminate a worry and purchase peace of mind.
  - 原译：在这里，人们买到的同样不只是对一场不太可能发生的灾难的保障；他们消除了一份担忧，买到了心安。
  - 现译：在这里，人们买到的同样不只是应对小概率灾难的保障；他们消除了一份担忧，买到了心安。
  - 处理：按复核意见修改。“对一场……的灾难的保障”的字连串 复核：“以防万一发生灾难”插在“不只是”的宾语之后，使保障的对象和后面的递进关系变得松散，读起来不顺。

- 英文：When we looked at our choices for bad options, we quickly realized that we were just as risk seeking in the domain of losses as we were risk averse in the domain of gains.
  - 原译：当我们看到自己在几个坏选项之间作出的选择时，很快意识到，我们在损失领域寻求风险的程度，和在收益领域规避风险的程度一样。
  - 现译：我们一看自己在几个坏选项之间怎么选，很快就意识到，我们在损失领域寻求风险的程度，和在收益领域规避风险的程度一样。
  - 处理：Astra 复核通过。“当……时”加“作出的选择”虚化动词

- 英文：However, we were fortunate to have a framework that made the finding of risk seeking easy to interpret, and that was a milestone in our thinking.
  - 原译：不过，我们很幸运，手里有一个框架，让风险寻求这一发现很容易得到解释，这是我们思想历程中的一个里程碑。
  - 现译：不过，我们很幸运，手里有一个框架，能轻松解释风险寻求这个发现，这是我们思想历程中的一个里程碑。
  - 处理：Astra 复核通过。“很容易得到解释”变相被动

- 英文：The sure loss is very aversive because the reaction to a loss of $900 is more than 90% as intense as the reaction to a loss of $1,000.
  - 原译：确定的损失让人非常反感，因为对损失 900 美元的反应，强度超过对损失 1,000 美元的反应的 90%。
  - 现译：确定的损失让人非常反感，因为损失 900 美元时的反应强度，超过了损失 1,000 美元时反应强度的 90%。
  - 处理：复核后重写。“对……的反应的 90%”的字连串，照搬英文比较结构 复核：“损失 1,000 美元时的 90%”省略了必要的比较对象，必须明确是该情形下反应强度的 90%。

- 英文：The result is that when you consider a choice between a sure loss and a gamble with a high probability of a larger loss, diminishing sensitivity makes the sure loss more aversive, and the certainty effect reduces the aversiveness of the gamble. The same two factors enhance the attractiveness of the sure thing and reduce the attractiveness of the gamble when the outcomes are positive.
  - 原译：结果是，当你在一个确定的损失和一个很可能遭受更大损失的赌局之间作选择时，敏感度递减让确定的损失更让人反感，确定性效应则降低了赌局让人反感的程度。如果结果是正面的，同样这两个因素就会增强确定的事的吸引力，降低赌局的吸引力。
  - 现译：结果是，当你在一个确定的损失和一个很可能遭受更大损失的赌局之间作选择时，敏感度递减让确定的损失更让人反感，确定性效应则让人对赌局没那么反感。如果结果是正面的，同样这两个因素就会让确定的事更有吸引力，让赌局的吸引力下降。
  - 处理：复核后重写。“降低……程度”“增强……的吸引力”照搬 reduce/enhance 加抽象名词 复核：“让赌局没那么让人反感”重复拖沓，“让赌局的吸引力变小”也不如“降低赌局的吸引力”自然。原译的“增强吸引力”“降低……程度”属于正常中文表达。

- 英文：In the bottom row, however, the two factors operate in opposite directions: diminishing sensitivity continues to favor risk aversion for gains and risk seeking for losses, but the overweighting of low probabilities overcomes this effect and produces the observed pattern of gambling for gains and caution for losses.
  - 原译：不过在下面一行，这两个因素的作用方向相反：敏感度递减仍然有利于收益时的风险规避和损失时的风险寻求，但低概率被赋予过高的权重，压倒了这种效应，形成了我们观察到的模式：面对收益时赌一把，面对损失时求稳妥。
  - 现译：不过在下面一行，这两个因素的作用方向相反：敏感度递减仍然让人在收益时倾向于规避风险、在损失时倾向于寻求风险，但低概率被赋予过高的权重，压倒了这种效应，形成了我们观察到的模式：面对收益时赌一把，面对损失时求稳妥。
  - 处理：Astra 复核通过。“有利于……的风险规避”直译 favor 加名词短语

- 英文：Many unfortunate human situations unfold in the top right cell.
  - 原译：人类的许多不幸处境，都发生在右上格。
  - 现译：人的许多不幸遭遇，都发生在右上格。
  - 处理：Astra 复核通过。“处境……发生”搭配不当，直译 situations

- 英文：Even 90% of the claim is a great deal of money, and I can walk away with it now.”
  - 原译：就算是索赔金额的 90%，也是一大笔钱，而且我现在就能拿着它走人。”
  - 现译：就算是索赔金额的 90%，也是一大笔钱，而且我现在就能拿着钱走人。”
  - 处理：Astra 复核通过。心里话里用“它”指钱，照搬 it

- 英文：Two emotions are evoked, both driving in the same direction: the attraction of a sure (and substantial) gain and the fear of intense disappointment and regret if you reject a settlement and lose in court. You can feel the pressure that typically leads to cautious behavior in this situation.
  - 原译：这时会引发两种情绪，两者都把你推向同一个方向：一是确定的（而且可观的）收益的吸引力，二是害怕自己拒绝和解后又在法庭上败诉，那样会极度失望和后悔。你能感受到，在这种情况下，有一种压力通常会让人行事谨慎。
  - 现译：和前面看到的一个情境一样，你是一宗民事诉讼的原告，要求对方赔偿一大笔损失。庭审进行得非常顺利，你的律师援引专家意见说，你有 95% 的机会彻底胜诉，但又补充了一句告诫：“不到陪审团宣布裁决，谁也说不准结果。”你的律师力劝你接受和解，和解时你可能只能拿到索赔金额的 90%。你处在四重模式的左上格，心里想的问题是：“哪怕一无所获的机会很小，我愿意冒这个险吗？就算是索赔金额的 90%，也是一大笔钱，而且我现在就能拿着钱走人。”这时你会产生两种情绪，两者都把你推向同一个方向：一是确定（而且可观）的收益让你心动，二是你害怕拒绝和解后万一在法庭上败诉，会极度失望和后悔。你能感受到一股压力，在这种处境下，它通常会让人谨慎行事。理由充分的原告很可能会规避风险。
  - 处理：复核后重写。无主语的“会引发两种情绪”照搬被动，“……收益的吸引力”的字连串，“有一种压力通常会”语序生硬 复核：第二种情绪针对的是拒绝和解后败诉所带来的强烈失望和后悔，改写却把恐惧对象直接写成败诉，再另述情绪后果。第一项也宜直接写出当事人受到吸引的感受。

- 英文：In the face-off between a risk-averse plaintiff and a risk-seeking defendant, the defendant holds the stronger hand. The superior bargaining position of the defendant should be reflected in negotiated settlements, with the plaintiff settling for less than the statistically expected outcome of the trial.
  - 原译：在规避风险的原告和寻求风险的被告之间的较量中，被告手里的牌更好。被告在谈判中的优势地位，应该会在谈判达成的和解中体现出来：原告最终接受的金额，会低于庭审在统计上的期望结果。
  - 现译：规避风险的原告和寻求风险的被告交起手来，被告手里的牌更好。被告的谈判地位更有利，这一点应该会在谈判达成的和解中体现出来：原告最终接受的金额，会低于庭审在统计上的期望结果。
  - 处理：Astra 复核通过。“在……之间的较量中”介词框架，“被告在谈判中的优势地位”抽象名词作主语

- 英文：Overweighting the small chance of a large loss favors risk aversion, and settling for a modest amount is equivalent to purchasing insurance against the unlikely event of a bad verdict.
  - 原译：给遭受巨大损失的小概率赋予过高的权重，会让人倾向于风险规避；花一笔不大的钱和解，就相当于买了一份保险，防范不太可能出现的不利判决。
  - 现译：给遭受巨大损失的小概率赋予过高的权重，会让人倾向于风险规避；花一笔不大的钱和解，就相当于买了一份保险，防范不太可能出现的不利判决。
  - 处理：复核后退回原译。“遭受巨大损失的小概率”照搬 chance of a large loss，中文不这么搭配 复核：原文强调给“遭受巨大损失的微小概率”赋予过高权重；改写把赋权对象换成“巨大损失”，模糊了本句对概率权重的强调。原译更准确。

- 英文：Suppose further that in each case the city could settle the lawsuit for a payment of $100,000.
  - 原译：再假设，每一起诉讼，市政府都可以通过支付 100,000 美元来和解。
  - 现译：再假设，每一起诉讼，市政府都可以花 100,000 美元和解。
  - 处理：Astra 复核通过。“通过支付……来……”照搬 for a payment of

- 英文：(For simplicity, I ignore legal costs.)
  - 原译：（为简单起见，我忽略诉讼费用。）
  - 现译：（为简单起见，我不考虑诉讼费用。）
  - 处理：Astra 复核通过。“忽略费用”直译 ignore，中文一般说“不考虑”

- 英文：When you take the long view of many similar decisions, you can see that paying a premium to avoid a small risk of a large loss is costly.
  - 原译：当你从长远的角度看待许多类似的决定时，就会发现，为了避免遭受巨大损失的小风险而支付溢价，代价是很高的。
  - 现译：把许多类似的决定放在一起从长远看，你就会发现，为了避开小概率的巨大损失而支付溢价，代价是很高的。
  - 处理：Astra 复核通过。“当……时”句式，“遭受巨大损失的小风险”照搬 small risk of a large loss

- 英文：“He is tempted to settle this frivolous claim to avoid a freak loss, however unlikely.
  - 原译：“他很想就这起无理索赔达成和解，免得出现一次意外的损失，哪怕这种可能性微乎其微。
  - 现译：“他很想就这起无理索赔达成和解，免得遭受意外损失，哪怕这种可能性微乎其微。
  - 处理：按复核意见修改。“出现一次意外的损失”照搬 a freak loss 的冠词，不像口语 复核：“免得万一遭受”叠加后不顺，“万一”也与后面的可能性限定重复。保留“遭受”的改进即可。

## 第 30 章 罕见事件

- 英文：I visited Israel several times during a period in which suicide bombings in buses were relatively common—though of course quite rare in absolute terms.
  - 原译：我曾多次去以色列，那段时间，公交车上的自杀式炸弹袭击相对常见（当然，从绝对数量上看仍然非常少）。
  - 现译：我曾多次去以色列，那段时间，公交车上的自杀式炸弹袭击相对常见（当然，从绝对数量上看仍然非常少）。
  - 处理：复核后退回原译。照搬英文定语从句，“那段时间”没有着落 复核：改后把“以色列”放到长句末尾，袭击发生的地点要读到最后才能确定；“有一段时间／那段时间”又重复，整体不如原译紧凑清楚。

- 英文：The thrilling possibility of winning the big prize is shared by the community and reinforced by conversations at work and at home. Buying a ticket is immediately rewarded by pleasant fantasies, just as avoiding a bus was immediately rewarded by relief from fear.
  - 原译：人们一起憧憬着中大奖这种激动人心的可能性，工作时、在家里的谈论又不断强化它。买一张彩票，马上就能得到美好幻想的回报，就像躲开公交车马上就能得到摆脱恐惧的回报一样。
  - 现译：人们一起憧憬着中大奖这种激动人心的可能性，上班时聊，回到家也聊，这种憧憬就越来越强烈。买一张彩票，马上就能美美地幻想一番，这就是回报，就像躲开公交车，马上就能摆脱恐惧一样。
  - 处理：Astra 复核通过。抽象名词作主语，“得到……的回报”直译被动结构

- 英文：We start from two simple answers, then qualify them.
  - 原译：我们先给出两个简单的答案，再对它们加以限定。
  - 现译：我们先给出两个简单的答案，再给它们加上限定条件。
  - 处理：Astra 复核通过。“对……加以”虚化动词

- 英文：When you thought about the unlikely victory of a third-party candidate, your associative system worked in its usual confirmatory mode, selectively retrieving evidence, instances, and images that would make the statement true.
  - 原译：当你思考第三党候选人那不太可能取得的胜利时，你的联想系统以它惯常的证实模式运作，有选择地提取那些能让这个说法成立的证据、实例和画面。
  - 现译：你在想第三党候选人赢得大选这件不太可能的事时，联想系统照常以证实模式运作，有选择地提取那些能让这个说法成立的证据、实例和画面。
  - 处理：Astra 复核通过。“当……时”加长定语名词化，多余代词

- 英文：Our mind has a useful capability to focus spontaneously on whatever is odd, different, or unusual.
  - 原译：我们的心智有一种有用的能力，会自发地关注一切古怪的、与众不同的或者不寻常的东西。
  - 现译：我们的心智有一种有用的本领：能自发地关注古怪、与众不同或不寻常的事物。
  - 处理：按复核意见修改。“有一种……的能力，会……”照搬英文结构 复核：原文说心智具有自发关注异常事物的能力；“凡是……它都会”把这种能力写成了无例外的必然反应，语气过满。

- 英文：Because you were in confirmatory mode, there is a good chance that your estimate of the frequency of problems was too high.
  - 原译：由于你处在证实模式中，你对出现问题的频率的估计很可能过高。
  - 现译：因为你处在证实模式中，你很可能把出问题的频率估计得过高。
  - 处理：Astra 复核通过。“你对……的……的估计”名词化，的字连串

- 英文：Imagine a fan who has been asked to estimate the chances that the Chicago Bulls will win the tournament.
  - 原译：设想一位球迷被要求估计芝加哥公牛队夺冠的几率。
  - 现译：设想有人请一位球迷估计芝加哥公牛队夺冠的几率。
  - 处理：Astra 复核通过。不必要的被动句“被要求”

- 英文：Other researchers had found, using physiological measures such as heart rate, that the fear of an impending electric shock was essentially uncorrelated with the probability of receiving the shock.
  - 原译：其他研究者用心率之类的生理指标发现，对即将到来的电击的恐惧，与受到电击的概率基本上不相关。
  - 现译：其他研究者用心率之类的生理指标发现，人们对即将到来的电击有多恐惧，与受到电击的概率基本上不相关。
  - 处理：Astra 复核通过。“对……的……的恐惧”抽象名词作主语

- 英文：…and the vague estimate was sufficient to provide a helpful anchor as you searched for an equally attractive cash gift.
  - 原译：在你寻找一笔同样有吸引力的现金礼物时，这个模糊的估计足以提供一个有用的锚。
  - 现译：在估量多少现金与这个赌局同样有吸引力时，这个模糊的估计就足以充当一个有用的锚。
  - 处理：按复核意见修改。“在……时”套用英文状语，“提供一个锚”搭配生硬 复核：“你要找一笔……现金礼物”仍显生硬，也没有清楚表达这里是在估量与赌局同样有吸引力的现金数额。改成两个分句后，原有的时间关系也变得松散。

- 英文：Respondents also assessed the cash equivalent of gambles with a 21% chance to win the two outcomes.
  - 原译：受访者还评估了另外两个赌局的现金等值，它们赢得这两种结果的机会都是 21%。
  - 现译：受访者还评估了另外两个赌局的现金等值：奖品仍然分别是 59 美元和那打玫瑰，只是赢的机会都变成了 21%。
  - 处理：复核后重写。“它们赢得……的机会”代词指代不清，语序别扭 复核：“赢得……结果”搭配生硬；“分别有……机会赢得……两种结果”也没有清楚说明两个赌局各对应一种奖品。

- 英文：People who thought of the gift as a chance to get roses did not use price information as an anchor in evaluating the gamble.
  - 原译：把这份礼物看作一个得到玫瑰的机会的人，在评估赌局时并没有把价格信息当作锚。
  - 现译：把这份礼物看成得到玫瑰的机会的人，评估赌局时并没有拿价格信息当锚。
  - 处理：复核后重写。“……的机会的人”前置定语过长，多余的“一个” 复核：原文限定的是“把礼物看作得到玫瑰的机会的人”。改成“人们把……”后，限定条件变成了对人们的泛指陈述，扩大了结论适用的人群。

- 英文：The story, I believe, is that a rich and vivid representation of the outcome, whether or not it is emotional, reduces the role of probability in the evaluation of an uncertain prospect.
  - 原译：我相信，这个故事是这样的：对结果的表征只要丰富而生动，无论它是否带有情绪色彩，都会削弱概率在评估一个不确定前景时所起的作用。
  - 现译：我相信，这个故事是这样的：只要对结果的表征丰富而生动，无论是否带有情绪色彩，人们评估一个不确定的前景时，概率所起的作用都会变小。
  - 处理：Astra 复核通过。“削弱概率在……时所起的作用”名词化长宾语

- 英文：The chances of winning are 10% in urn A and 8% in urn B, so making the right choice should be easy, but it is not: about 30%–40% of students choose the urn with the larger number of winning marbles, rather than the urn that provides a better chance of winning.
  - 原译：罐子 A 的获胜几率是 10%，罐子 B 是 8%，所以作出正确的选择应该很容易，但事实并非如此：大约 30% 到 40% 的学生选择了能赢的弹珠数量更多的那个罐子，而没有选获胜几率更高的那个。
  - 现译：罐子 A 的获胜几率是 10%，罐子 B 是 8%，所以选对罐子应该很容易，但事实并非如此：大约 30% 到 40% 的学生选择了能赢的弹珠数量更多的那个罐子，而没有选获胜几率更高的那个。
  - 处理：按复核意见修改。“作出正确的选择”虚化动词 复核：“要选对应该很容易”语序生硬，“要”多余，“选对”与“应该”连在一起也容易误断句。

- 英文：As you might expect, the remarkably foolish choices that people make in this situation have attracted the attention of many researchers.
  - 原译：你大概想得到，人们在这种情况下作出的愚蠢得出奇的选择，引起了许多研究者的注意。
  - 现译：人们在这种情况下作出的选择愚蠢得出奇。你大概想得到，这引起了许多研究者的注意。
  - 处理：按复核意见修改。定语从句整个前置作主语，名词前修饰过长 复核：拆句后，“你大概想得到”容易指向“人们会作出愚蠢选择”；原文说可以预料的是，这些选择引起了许多研究者的注意。

- 英文：The second statement does something to your mind that the first does not: it calls up the image of an individual child who is permanently disabled by a vaccine; the 99,999 safely vaccinated children have faded into the background.
  - 原译：第二种说法对你的心理产生了第一种说法没有的作用：它让你想起一个因为疫苗而永久残疾的具体孩子的形象；那 99,999 个安全接种的孩子则退到了背景里。
  - 现译：第二种说法对你的心理产生了第一种说法没有的作用：它让你脑海里浮现出一个具体的孩子，这个孩子因为疫苗而永久残疾；那 99,999 个安全接种的孩子则退到了背景里。
  - 处理：Astra 复核通过。“一个……的具体孩子的形象”定语堆叠

- 英文：It would take an exceptionally active System 2 to generate alternative formulations of the one you see and to discover that they evoke a different response.
  - 原译：要针对你看到的表述想出别的表述方式，并发现它们会引起不同的反应，需要一个格外活跃的系统 2。
  - 现译：只有系统 2 格外活跃，你才会针对眼前的表述想出别的表述方式，并发现它们会引起不同的反应。
  - 处理：Astra 复核通过。照搬 It would take … to 的句式，头重脚轻

- 英文：The power of format creates opportunities for manipulation, which people with an axe to grind know how to exploit.
  - 原译：表达格式的力量创造了操纵的机会，别有所图的人很懂得如何利用它。
  - 现译：表达格式的影响这么大，就给了人操纵的机会，别有所图的人很懂得怎样利用这一点。
  - 处理：Astra 复核通过。抽象名词作主语，“力量创造了机会”搭配生硬

- 英文：The evidence suggests the hypothesis that focal attention and salience contribute to both the overestimation of unlikely events and the overweighting of unlikely outcomes.
  - 原译：这些证据提示了一个假设：焦点注意和显著性，既助长了对不太可能发生的事件的高估，也助长了对不太可能出现的结果的过度加权。
  - 现译：这些证据提示了一个假设：焦点注意和显著性既会让人们更容易高估不太可能发生的事件的概率，也会让人们更容易给不太可能出现的结果过度加权。
  - 处理：按复核意见修改。“对……的高估”“对……的过度加权”名词化 复核：“助长了人们高估／给……过度加权”搭配生硬，机械改成动词结构后反而不顺；“高估事件”也宜明确为高估事件发生的概率。

- 英文：Choice from experience is implemented by exposing the participant to many trials in which she can observe the consequences of pressing one button or another.
  - 原译：基于经验的选择是这样实现的：让参与者经历许多轮试验，在这些试验中，她可以观察按下这个或那个按钮的后果。
  - 现译：基于经验的选择是这样实现的：让参与者经历许多轮试验，观察按下这个或那个按钮会有什么后果。
  - 处理：复核后保留改写。把 in which 从句拆成“在这些试验中，她……” 复核：删去了 can 所表示的“可以观察”，把试验提供的观察机会直接写成了参与者实际进行的行动。

- 英文：Choice from description is realized by showing the subject the verbal description of the risky prospect associated with each button (such as “5% to win $12”) and asking her to choose one.
  - 原译：基于描述的选择，则是向参与者展示每个按钮所对应的风险前景的文字描述（比如“5% 的机会赢 12 美元”），请她从中选一个。
  - 现译：基于描述的选择，则是把每个按钮对应的风险前景用文字描述出来（比如“5% 的机会赢 12 美元”），拿给参与者看，请她从中选一个。
  - 处理：Astra 复核通过。“每个按钮所对应的风险前景的文字描述”的字连串

- 英文：The interpretation of choice from experience is not yet settled, but there is general agreement on one major cause of underweighting of rare events, both in experiments and in the real world: many participants never experience the rare event!
  - 原译：对基于经验的选择该怎样解释，目前尚无定论，但对于罕见事件被加权不足的一个主要原因，无论是在实验中还是在现实世界里，大家的看法基本一致：许多参与者从来没有经历过那个罕见事件！
  - 现译：基于经验的选择该怎样解释，目前尚无定论，但大家基本认同，无论在实验中还是在现实世界里，罕见事件被加权不足都有一个主要原因：许多参与者从来没有经历过那个罕见事件！
  - 处理：Astra 复核通过。“对于……的一个主要原因”介词结构套长定语

- 英文：These examples of neglect are both important and easily explained, but underweighting also occurs when people have actually experienced the rare event.
  - 原译：这些忽视的例子很重要，也很容易解释；但是，即使人们确实经历过罕见事件，加权不足也会发生。
  - 现译：这些忽视的例子很重要，也很容易解释；但是，即使人们确实经历过罕见事件，也会出现加权不足。
  - 处理：Astra 复核通过。“加权不足也会发生”直译 occurs

- 英文：Separate attention is effectively guaranteed when prospects are described explicitly (“99% chance to win $1,000, and 1% chance to win nothing”).
  - 原译：当前景被明确描述出来时（“99% 的机会赢得 1,000 美元，1% 的机会什么也得不到”），罕见事件实际上必定会得到单独的注意。
  - 现译：如果前景是明确描述出来的（“99% 的机会赢得 1,000 美元，1% 的机会什么也得不到”），罕见事件实际上就一定会得到单独的注意。
  - 处理：Astra 复核通过。“当……被……时”被动加套语

## 第 31 章 风险策略

- 英文：Imagine that you face the following pair of concurrent decisions. First examine both decisions, then make your choices.
  - 原译：假设你面临下面这一对同时进行的决策。请先把两项决策都看一遍，再做出你的选择。
  - 现译：假设你要同时做出下面这两项决策。请先把两项决策都看一遍，再作选择。
  - 处理：Astra 复核通过。“一对同时进行的决策”直译，多余的“你的”

- 英文：Both payments come out of the same pocket, and when you face both kinds of problems at once, the discrepant attitudes are unlikely to be optimal.
  - 原译：两笔钱都出自同一个口袋，当你同时面对这两类问题时，这两种互相矛盾的态度不太可能是最优的。
  - 现译：两笔钱都出自同一个口袋，如果你同时面对这两类问题，这两种互相矛盾的态度就不太可能是最优的。
  - 处理：Astra 复核通过。“当……时”套用英文从句

- 英文：Now I have a sermon ready for Sam if he rejects the offer of a single highly favorable gamble played once, and for you if you share his unreasonable aversion to losses:
  - 原译：如果萨姆拒绝只玩一次的高度有利的赌局，我已经为他准备好了一段说教；如果你也像他一样不合理地厌恶损失，这段话也说给你听：
  - 现译：萨姆如果拒绝一个只玩一次、对他非常有利的赌局，我已经给他准备好了一段说教；你如果也像他一样不合理地厌恶损失，这段话也是说给你听的：
  - 处理：Astra 复核通过。“高度有利”直译 highly，定语堆在名词前

- 英文：Please consider this question: Are you on your deathbed?
  - 原译：请考虑这样一个问题：你已经躺在临终的床上了吗？
  - 现译：请考虑这样一个问题：你已经到临终的时候了吗？
  - 处理：Astra 复核通过。deathbed 硬译成“临终的床”

- 英文：Of course, you are unlikely to be offered exactly this gamble again, but you will have many opportunities to consider attractive gambles with stakes that are very small relative to your wealth. You will do yourself a large financial favor if you are able to see each of these gambles as part of a bundle of small gambles and rehearse the mantra that will get you significantly closer to economic rationality: you win a few, you lose a few.
  - 原译：但你会有很多机会去考虑一些有吸引力的赌局，它们的赌注相对于你的财富非常小。如果你能把这些赌局中的每一个都看作一大批小赌局中的一个，并且反复默念一句能让你大大接近经济理性的口诀，你就能在财务上给自己帮个大忙。这句口诀是：有赢有输。
  - 现译：但你会有很多机会去考虑一些有吸引力的赌局，跟你的财富比起来，它们的赌注非常小。如果你能把其中每一个赌局都看作一大批小赌局里的一个，再反复默念一句口诀，就能在经济上大为受益。这句口诀能让你离经济理性近得多，那就是：有赢有输。
  - 处理：按复核意见修改。“相对于”直译，“一句能让你大大接近经济理性的口诀”定语过长 复核：拆开长定语有所改善，但“在财务上帮自己一个大忙”仍是生硬直译，这里指这样做会给自己带来很大的经济好处。

- 英文：If you have the emotional discipline that this rule requires, you will never consider a small gamble in isolation or be loss averse for a small gamble until you are actually on your deathbed—and not even then.
  - 原译：> 如果你有这条规则所要求的情绪自律，那么在真正躺到临终的床上之前，你永远不会孤立地考虑一个小赌局，也不会在小赌局上厌恶损失；即使到了那时，你也不会。
  - 现译：> 如果你有这条规则所要求的情绪自律，那么直到你真正到了临终的时候，你都不会孤立地考虑一个小赌局，也不会在小赌局上厌恶损失；即使到了那时，你也不会。
  - 处理：复核后重写。deathbed 硬译，与上文的改法保持一致 复核：on your deathbed 指处于临终状态，不是死亡发生的“那一刻”；两处“那一刻”缩窄了原文的时间范围。

- 英文：The typical short-term reaction to bad news is increased loss aversion.
  - 原译：人们对坏消息的典型短期反应，是损失厌恶加剧。
  - 现译：听到坏消息，人们在短期内的典型反应是更加厌恶损失。
  - 处理：Astra 复核通过。抽象名词作主语和表语

- 英文：Richard Thaler tells of a discussion about decision making he had with the top managers of the 25 divisions of a large company.
  - 原译：理查德·塞勒讲过一次他和一家大公司 25 个事业部的最高管理者讨论决策的经历。
  - 现译：理查德·塞勒讲过这样一件事：他和一家大公司 25 个事业部的最高管理者讨论过决策问题。
  - 处理：Astra 复核通过。“一次他和……讨论决策的经历”整句塞进定语

- 英文：“I decided to evaluate my portfolio only once a quarter. I am too loss averse to make sensible decisions in the face of daily price fluctuations.”
  - 原译：> “我决定每个季度只评估一次我的投资组合。我太厌恶损失了，面对每天的价格波动，没法做出明智的决定。”
  - 现译：> “我决定了，投资组合每个季度只评估一次。我太厌恶损失了，天天看着价格波动，就没法做出明智的决定。”
  - 处理：Astra 复核通过。“评估一次我的投资组合”照搬英文语序，不像口语

- 英文：“Each of our executives is loss averse in his or her domain. That’s perfectly natural, but the result is that the organization is not taking enough risk.”
  - 原译：> “我们的每一位高管在自己负责的领域里都厌恶损失。这再自然不过了，但结果是，整个组织承担的风险不够。”
  - 现译：> “我们每位高管在自己负责的领域里都厌恶损失。这再自然不过了，可结果就是，整个组织承担的风险不够。”
  - 处理：Astra 复核通过。“我们的每一位”直译 each of our，口语里不这么说

## 第 32 章 记分

- 英文：The ultimate currency that rewards or punishes is often emotional, a form of mental self-dealing that inevitably creates conflicts of interest when the individual acts as an agent on behalf of an organization.
  - 原译：这是一种心理上的“自我交易”，当个人作为代理人替组织办事时，它必然会造成利益冲突。
  - 现译：这是一种心理上的“自我交易”，个人作为代理人替组织办事时，它必然会造成利益冲突。
  - 处理：Astra 复核通过。照搬 when 从句，多余的“当……时”

- 英文：These are tacit calculations of emotional balance, of the kind that System 1 performs without deliberation.
  - 原译：这些是对情绪余额的默默计算，正是系统 1 不经思考就会做的那一类计算。
  - 现译：这些是对情绪余额的默默计算，正是系统 1 不经思考就会做的那一类计算。
  - 处理：复核后退回原译。“对……的计算”名词化结构 复核：“这些都是在……计算，正是……计算”衔接拗口，“在心里默默”也显得重复，未比原译更清楚、紧凑。

- 英文：The emotions that people attach to the state of their mental accounts are not acknowledged in standard economic theory.
  - 原译：人们给心理账户的状态附加的情绪，在标准经济理论里是不被承认的。
  - 现译：人们会因心理账户的状况产生各种情绪，但标准经济理论并不考虑这些情绪。
  - 处理：按复核意见修改。长定语作主语，加上“是不被承认的”被动句 复核：“给心理账户的状态附上情绪”仍是生硬的直译；这里指人们对账户状况的情绪反应，而标准经济理论未将这些情绪纳入考虑。

- 英文：A plausible way to formulate the choice is this: “I could close the Blueberry Tiles account and score a success for my record as an investor.
  - 原译：这个选择很可能会被表述成这样：“我可以结清蓝莓瓷砖这个账户，给我的投资记录添上一笔成功。
  - 现译：这个选择可以这样表述：“我可以结清蓝莓瓷砖这个账户，给我的投资记录添上一笔成功。
  - 处理：按复核意见修改。不必要的“被”字句 复核：plausible 指这种表述说得通，不是说读者“很可能”采用这种表述；旧译也有这一问题。

- 英文：When Amos asked mildly, “Isn’t it supposed not to matter?” the adviser looked astonished.
  - 原译：阿莫斯温和地问了一句：“这个不是应该无关紧要吗？”顾问一脸惊讶。
  - 现译：阿莫斯温和地问了一句：“按理说，这个不是无关紧要吗？”顾问一脸惊讶。
  - 处理：Astra 复核通过。口语问句照搬 supposed not to 的结构，说起来别扭

- 英文：Amos’s guess about the financial adviser’s beliefs was probably right, but he was wrong to dismiss the buying price as irrelevant.
  - 原译：阿莫斯对那位理财顾问想法的猜测大概是对的，但他把买入价当作无关因素一笔勾销，却是错的。
  - 现译：阿莫斯大概猜对了那位理财顾问的想法，但他认为买入价无关紧要，这就错了。
  - 处理：复核后重写。抽象名词“猜测”作主语，“的”字连串 复核：“把买入价当作无关因素一笔勾销”搭配不当；原文说的是认为买入价无关紧要，并非将价格勾销。

- 英文：Another argument against selling winners is the well-documented market anomaly that stocks that recently gained in value are likely to go on gaining at least for a short while.
  - 原译：反对卖出赢家的另一个理由，是一种有大量记录的市场异常现象：最近涨过的股票很可能还会继续涨，至少再涨上一小段时间。
  - 现译：反对卖出赢家的另一个理由，是一种证据充分的市场异常现象：最近涨过的股票很可能还会继续涨，至少再涨上一小段时间。
  - 处理：Astra 复核通过。well-documented 直译成“有大量记录的”

- 英文：The members of the board do not necessarily believe that the new CEO is more competent than the one she replaces. They do know that she does not carry the same mental accounts and is therefore better able to ignore the sunk costs of past investments in evaluating current opportunities.
  - 原译：董事会成员未必相信新 CEO 比被她取代的那位更能干。他们确实知道的是，她没有背着同样的心理账户，因此在评估眼前的机会时，更能够不理会过去投资的沉没成本。
  - 现译：董事会成员未必相信新 CEO 比前任更能干。但他们知道，她没有背着同样的心理账户，因此在评估眼前的机会时，更能够不理会过去投资的沉没成本。
  - 处理：Astra 复核通过。“被她取代的那位”“确实知道的是”照搬英文结构

- 英文：The sunk-cost fallacy is identified and taught as a mistake in both economics and business courses, apparently to good effect: there is evidence that graduate students in these fields are more willing than others to walk away from a failing project.
  - 原译：经济学和商科课程都会指出沉没成本谬误是一种错误，并把它讲给学生听，看来效果不错：有证据表明，这些领域的研究生比其他人更愿意放弃一个正在失败的项目。
  - 现译：经济学和商科课程都会讲解沉没成本谬误，指出它是一种错误，看来效果不错：有证据表明，这些领域的研究生比其他人更愿意放弃一个正在走向失败的项目。
  - 处理：按复核意见修改。“并把它讲给学生听”拖沓，“正在失败的项目”直译 failing 复核：failing 不限定失败迫在眉睫，“眼看就要失败”增加了紧迫程度；“把……错误……教给学生”也容易产生歧义。

- 英文：The fear of regret is a factor in many of the decisions that people make (“Don’t do this, you will regret it” is a common warning), and the actual experience of regret is familiar.
  - 原译：对后悔的恐惧，是人们作许多决策时的一个考虑因素（“别这么做，你会后悔的”是一句常见的告诫），而后悔的实际体验，大家也都很熟悉。
  - 现译：怕后悔，会影响人们的许多决策（“别这么做，你会后悔的”是一句常见的告诫）；真正后悔是什么滋味，大家也都熟悉。
  - 处理：复核后重写。“对后悔的恐惧”“后悔的实际体验”抽象名词作主语 复核：is a factor 只说怕后悔会影响决策，“会考虑的一个因素”额外暗示人们会有意识地权衡它。

- 英文：The emotional state has been well described by two Dutch psychologists, who noted that regret is “accompanied by feelings that one should have known better, by a sinking feeling, by thoughts about the mistake one has made and the opportunities lost, by a tendency to kick oneself and to correct one’s mistake, and by wanting to undo the event and to get a second chance.”
  - 原译：他们指出，后悔“伴随着这样一些感受：觉得自己本该更明白事理，心里一沉；想着自己犯下的错误和错失的机会；忍不住狠狠责怪自己，想改正错误；还希望这件事能被撤销，自己能再得到一次机会”。
  - 现译：他们指出，后悔“伴随着这样一些感受：觉得自己本该更明智一些，心里一沉；想着自己犯下的错误和错失的机会；忍不住责怪自己，想改正错误；还希望这件事没有发生过，自己能再得到一次机会”。
  - 处理：复核后重写。“能被撤销”不必要的被动，多余的“自己” 复核：a tendency 表示倾向，“忍不住狠狠责怪自己”把反应写得更强、更确定；“撤销这件事”也不够自然。

- 英文：Intense regret is what you experience when you can most easily imagine yourself doing something other than what you did.
  - 原译：当你最容易想象自己当初换一种做法时，你体验到的后悔就最强烈。
  - 现译：你最容易想象自己当初换一种做法的时候，会感到强烈的后悔。
  - 处理：按复核意见修改。“当……时”加重复的“你” 复核：原文是“强烈的后悔”，不是“最强烈的后悔”；most 只修饰想象其他做法的容易程度。旧译也有这一程度扩大。

- 英文：After every plane crash there are special stories about passengers who “should not” have been on the plane—they got a seat at the last moment, they were transferred from another airline, they were supposed to fly a day earlier but had had to postpone.
  - 原译：每次空难之后，总会流传一些特别的故事，讲的是那些“本不该”在那架飞机上的乘客：他们在最后一刻才拿到座位，他们是从另一家航空公司转过来的，他们本来应该早一天走，却不得不推迟。
  - 现译：每次空难之后，总会流传一些特别的故事，讲的是那些“本不该”在那架飞机上的乘客：有的在最后一刻才拿到座位，有的是从另一家航空公司转过来的，有的本来应该早一天走，却不得不推迟。
  - 处理：Astra 复核通过。照搬英文连用三个“他们”

- 英文：But Mr. Brown is the one who is more likely to be kicking himself, because he acted out of character in this one instance.
  - 原译：但更可能懊恼自责的是布朗先生，因为他这一次的做法不像他平时的为人。
  - 现译：但更可能懊恼自责的是布朗先生，因为他这一次一反常态。
  - 处理：Astra 复核通过。acted out of character 逐词解释，拖沓

- 英文：This short example illustrates a broad story: people expect to have stronger emotional reactions (including regret) to an outcome that is produced by action than to the same outcome when it is produced by inaction.
  - 原译：这个小例子说明了一个普遍的道理：对于同一个结果，人们预计，如果它是由行动造成的，自己的情绪反应（包括后悔）会比它由不作为造成时更强烈。
  - 现译：这个小例子说明了一个普遍的道理：同样的结果，如果是行动造成的，人们预计自己的情绪反应（包括后悔）会比不作为造成时更强烈。
  - 处理：Astra 复核通过。“对于……”“它是由……造成的”照搬英文结构

- 英文：When you deviate from the default, you can easily imagine the norm—and if the default is associated with bad consequences, the discrepancy between the two can be the source of painful emotions.
  - 原译：当你偏离默认选项时，你很容易想象出常态；如果默认选项与坏结果联系在一起[^t1]，两者之间的差距就可能成为痛苦情绪的来源。
  - 现译：偏离默认选项时，你很容易想象出常态；如果默认选项与坏结果联系在一起[^t1]，两者之间的差距就可能成为痛苦情绪的来源。
  - 处理：Astra 复核通过。“当你……时，你”重复主语

- 英文：It is the departure from the default that produces regret.
  - 原译：产生后悔的，正是对默认选项的偏离。
  - 现译：让人后悔的，正是偏离了默认选项。
  - 处理：Astra 复核通过。“对默认选项的偏离”名词化

- 英文：Another situation in which action is the default is that of a coach whose team lost badly in their last game.
  - 原译：行动成为默认选项的另一种情形，是一位教练的球队在上一场比赛中输得很惨。
  - 现译：还有一种情形，默认选项是采取行动：一位教练的球队在上一场比赛中输得很惨。
  - 处理：Astra 复核通过。in which 定语从句前置，长定语压在“情形”上

- 英文：There is a vaccine that is effective only before any symptoms appear.
  - 原译：有一种疫苗，只在出现任何症状之前有效。
  - 现译：有一种疫苗，只在还没有出现任何症状时有效。
  - 处理：Astra 复核通过。“出现任何症状之前”照搬 before any 语序，读着别扭

- 英文：All that is required is that you expose yourself to a 1/1,000 chance of contracting the disease.
  - 原译：唯一的要求是，你要让自己面对 1/1,000 的染病概率。
  - 现译：唯一的要求是，你要冒 1/1,000 的染病风险。
  - 处理：Astra 复核通过。expose yourself to 直译成“让自己面对……概率”

- 英文：In the first place, you are not supposed to sell your health; the transaction is not considered legitimate and the reluctance to engage in it is expressed in a higher price.
  - 原译：首先，人们不该出卖自己的健康；这种交易被认为是不正当的，人们不愿参与，这种不情愿就体现在更高的价格上。
  - 现译：首先，人们不该出卖自己的健康；大家不认为这种交易正当，也不愿意参与，这种不情愿就体现在更高的价格上。
  - 处理：Astra 复核通过。“被认为是……的”被动句

- 英文：You know that if you wake up one morning with symptoms indicating that you will soon be dead, you will feel more regret in the second case than in the first, because you could have rejected the idea of selling your health without even stopping to consider the price.
  - 原译：你知道，如果你某天早上醒来，出现了表明自己不久就会死去的症状，那么在第二种情况下，你会比第一种情况下更后悔，因为你本可以连价格都不考虑，就拒绝出卖自己健康的想法。
  - 现译：你知道，如果你某天早上醒来，出现了表明自己不久就会死去的症状，那么在第二种情况下，你会比第一种情况下更后悔，因为你本可以连价格都不考虑，就一口回绝出卖健康这个主意。
  - 处理：Astra 复核通过。“拒绝出卖自己健康的想法”直译 rejected the idea，修饰关系含糊

- 英文：The minority who found a discount they could accept demanded an amount that was significantly higher than the amount they were willing to pay for a far larger improvement in the safety of the product.
  - 原译：少数父母找到了自己能接受的折扣，但他们要求的金额，明显高于他们愿意为产品安全性的大幅提升所支付的金额。
  - 现译：少数父母找到了自己能接受的折扣，但他们要求的金额，明显高于他们愿意为提高产品安全性而支付的金额，尽管后者换来的安全性提高要大得多。
  - 处理：复核后重写。“为……的大幅提升所支付”名词化加“所”字结构 复核：far larger 是比较级：“安全性提升”的幅度远大于前述安全性下降的幅度。“大幅提升”只保留程度，漏掉了比较关系。

- 英文：This trend is especially strong in Europe, where the precautionary principle, which prohibits any action that might cause harm, is a widely accepted doctrine.
  - 原译：在那里，预防原则禁止任何可能造成伤害的行动，是一条被广泛接受的准则。
  - 现译：在那里，预防原则是一条被广泛接受的准则，它禁止任何可能造成伤害的行动。
  - 处理：Astra 复核通过。把插入的 which 从句塞进主语，句子主干不清

- 英文：Multiple international bodies have specified that the absence of scientific evidence of potential damage is not sufficient justification for taking risks.
  - 原译：多个国际机构明确规定，缺乏潜在危害的科学证据，并不足以成为冒险的理由。
  - 现译：多个国际机构明确规定，没有科学证据表明存在潜在危害，并不足以成为冒险的理由。
  - 处理：Astra 复核通过。“缺乏潜在危害的科学证据”名词短语直译，修饰关系含糊

- 英文：He mentions an impressive list of innovations that would not have passed the test, including “airplanes, air conditioning, antibiotics, automobiles, chlorine, the measles vaccine, open-heart surgery, radio, refrigeration, smallpox vaccine, and X-rays.”
  - 原译：他列出了一长串通不过这项检验的创新，令人印象深刻，其中包括“飞机、空调、抗生素、汽车、氯、麻疹疫苗、心脏直视手术、无线电、制冷、天花疫苗和 X 光”。
  - 现译：他列出了一份令人印象深刻的清单，上面的创新当初要是接受这项检验，都过不了关，其中包括“飞机、空调、抗生素、汽车、氯、麻疹疫苗、心脏直视手术、无线电、制冷、天花疫苗和 X 光”。
  - 处理：复核后重写。定语从句前置，也丢了 would not have 的虚拟语气 复核：补出反事实条件是正确的，但 impressive 修饰清单，改写将其移成了每项创新的性质。

- 英文：But enhanced loss aversion is embedded in a strong and widely shared moral intuition; it originates in System 1.
  - 原译：但是，被强化的损失厌恶嵌在一种强烈而又广泛共有的道德直觉之中；它源自系统 1。
  - 现译：但是，强化了的损失厌恶植根于一种强烈而又普遍的道德直觉；它源自系统 1。
  - 处理：Astra 复核通过。“被强化的”“嵌在……之中”“广泛共有的”逐词直译

- 英文：The dilemma between intensely loss-averse moral attitudes and efficient risk management does not have a simple and compelling solution.
  - 原译：在强烈厌恶损失的道德态度和有效的风险管理之间，存在一种两难，而这个两难没有简单而又令人信服的解决办法。
  - 现译：一边是强烈厌恶损失的道德态度，一边是高效的风险管理，在两者之间如何取舍，没有简单而又令人信服的答案。
  - 处理：复核后重写。“在……之间存在一种两难，而这个两难”形合迁移 复核：efficient 强调效率，应译为“高效”，而非仅指“有效”；“两者之间的两难”也不够顺畅。

- 英文：How seriously should we take these intangible outcomes, the self-administered punishments (and occasional rewards) that we experience as we score our lives?
  - 原译：这些无形的结果，也就是我们给自己的人生记分时体验到的、由自己施加的惩罚（偶尔也有奖励），我们应该多认真地对待？
  - 现译：我们给自己的人生记分时，会受到自己施加的惩罚（偶尔也有奖励）。这些无形的结果，我们该看得多重？
  - 处理：复核后重写。同位语加长定语，问句被拉得很长 复核：拆句方向正确，但“自己施加给自己”重复，“应该多认真地对待”仍显生硬。

- 英文：Is it reasonable, in particular, to let your choices be influenced by the anticipation of regret?
  - 原译：具体来说，让对后悔的预期影响自己的选择，是合理的吗？
  - 现译：具体来说，让预想中的后悔影响自己的选择，是合理的吗？
  - 处理：Astra 复核通过。“让对后悔的预期影响”介词结构堆在一起

- 英文：If you are an investor, sufficiently rich and cautious at heart, you may be able to afford the luxury of a portfolio that minimizes the expectation of regret even if it does not maximize the accrual of wealth.
  - 原译：如果你是一位投资者，足够富有，骨子里又谨慎，你也许负担得起这样一种奢侈：持有一个能把预期中的后悔降到最低的投资组合，即使它不能让财富的积累达到最大。
  - 现译：如果你是一位投资者，足够富有，骨子里又谨慎，你也许负担得起这样一种奢侈：持有一个能把预期中的后悔降到最低的投资组合，哪怕它不能让你积累最多的财富。
  - 处理：Astra 复核通过。“让财富的积累达到最大”直译 maximize the accrual

- 英文：Perhaps the most useful is to be explicit about the anticipation of regret.
  - 原译：也许最有用的一条，是把对后悔的预期明明白白地摆出来。
  - 现译：也许最有用的一条，是事先明确考虑到自己可能会后悔。
  - 处理：按复核意见修改。“对后悔的预期”名词化 复核：“把预想中的后悔明明白白地摆出来”表达含混。结合下文，原文强调事先明确考虑自己可能会后悔。

- 英文：You should also know that regret and hindsight bias will come together, so anything you can do to preclude hindsight is likely to be helpful.
  - 原译：你还应该知道，后悔和后见之明偏差会结伴而来，所以凡是你能做的、可以杜绝后见之明的事，大概都会有帮助。
  - 现译：你还应该知道，后悔和后见之明偏差会结伴而来，所以任何能杜绝后见之明的事，只要你做得到，大概都会有帮助。
  - 处理：Astra 复核通过。两个并列定语堆在“事”前面

- 英文：Daniel Gilbert and his colleagues provocatively claim that people generally anticipate more regret than they will actually experience, because they underestimate the efficacy of the psychological defenses they will deploy—which they label the “psychological immune system.”
  - 原译：丹尼尔·吉尔伯特和他的同事们提出了一个颇具挑战性的观点：人们预想的后悔，通常比实际体验到的要多，因为他们低估了自己将会动用的心理防御的效力，吉尔伯特等人把这些防御称为“心理免疫系统”。
  - 现译：丹尼尔·吉尔伯特和他的同事们提出了一个颇具挑战性的观点：人们预想的后悔，通常比实际体验到的要多，因为他们到时候会动用心理防御，却低估了这些防御的效力；吉尔伯特等人把这些防御称为“心理免疫系统”。
  - 处理：Astra 复核通过。“自己将会动用的心理防御的效力”的字连串

- 英文：“We are hanging on to that stock just to avoid closing our mental account at a loss. It’s the disposition effect.”
  - 原译：“我们一直捏着那只股票不放，只是为了不让我们的心理账户以亏损结清。这就是处置效应。”
  - 现译：“我们一直捏着那只股票不放，只是不想让这个心理账户以亏损结清。这就是处置效应。”
  - 处理：复核后重写。闲谈里的话用了书面的“以亏损结清”和多余的“我们的” 复核：“亏着结清”搭配生硬，不如原译“以亏损结清”清楚；口语化并未改善可读性。

## 第 33 章 逆转

- 英文：You made your judgment in joint evaluation, where you consider two scenarios at the same time and make a comparison.
  - 原译：你是在联合评估中做出判断的，也就是同时考虑两种情境，并加以比较。
  - 现译：你是在联合评估中做出判断的，也就是同时考虑两种情境，把它们放在一起比较。
  - 处理：Astra 复核通过。虚化动词“加以”

- 英文：There is almost universal agreement on the answer: compensation should be the same in both situations.
  - 原译：对这个问题的回答，几乎所有人的意见都一致：两种情况下的赔偿应该相同。
  - 现译：对这个问题，几乎所有人的回答都一样：两种情况下的赔偿应该相同。
  - 处理：Astra 复核通过。“对……的回答，……意见都一致”主语和谓语搭不上

- 英文：The discrepancy between single and joint evaluation of the burglary scenario belongs to a broad family of reversals of judgment and choice.
  - 原译：单独评估和联合评估在这个抢劫情境上的不一致，属于判断与选择逆转这个大家族。
  - 现译：对这个抢劫情境，单独评估和联合评估的结果不一致，这属于判断与选择逆转这个大家族。
  - 处理：Astra 复核通过。抽象名词“不一致”带长定语作主语

- 英文：Remember that you are not negotiating with anyone—your task is to determine the lowest price at which you would truly be willing to give up the bet.
  - 原译：记住，你并没有在跟谁讨价还价，你的任务是确定一个最低价，在这个价格上你真心愿意放弃这个赌局。
  - 现译：记住，你并没有在跟谁讨价还价，你的任务是定出一个最低价：只要给到这个价，你就真心愿意放弃这个赌局。
  - 处理：Astra 复核通过。照搬 at which 从句，“在这个价格上你……”

- 英文：You may find that the prize that can be won is salient in this task, and that your evaluation of what the bet is worth is anchored on that value.
  - 原译：你可能会发现，在这个任务中，能赢到的奖金很显眼，你对这个赌局值多少钱的评估就锚定在这个数值上。
  - 现译：你可能会发现，在这个任务中，能赢到的奖金很显眼，你估计这个赌局值多少钱时，会以这笔奖金的数额为锚。
  - 处理：复核后重写。“你对……的评估”名词化作主语 复核：salient 应与术语表中的“显著／显著性”保持一致；后半句被锚定的是估值，不是“你”本人。

- 英文：Participants are unaware of the inconsistency, and their reactions when confronted with it can be entertaining.
  - 原译：参与者意识不到自己前后不一致，而当别人当面指出这种不一致时，他们的反应可能相当有趣。
  - 现译：参与者意识不到自己前后不一致；有人当面指出来时，他们的反应可能相当有趣。
  - 处理：Astra 复核通过。“而当……时”多余的连接词，重复“不一致”

- 英文：A 1968 interview of a participant in the experiment, conducted by Sarah Lichtenstein, is an enduring classic of the field.
  - 原译：萨拉·利希滕斯坦在 1968 年对一位实验参与者做的访谈，是这个领域经久不衰的经典。
  - 现译：1968 年，萨拉·利希滕斯坦访谈过一位实验参与者，这次访谈是这个领域经久不衰的经典。
  - 处理：Astra 复核通过。长定语堆在“访谈”前面

- 英文：A few years after the preference reversals were reported, two respected economists, David Grether and Charles Plott, published an article in the prestigious American Economic Review, in which they reported their own studies of the phenomenon that Lichtenstein and Slovic had described.
  - 原译：偏好逆转的报告发表几年后，两位受人尊敬的经济学家戴维·格雷瑟和查尔斯·普洛特在声望很高的《美国经济评论》上发表了一篇文章，报告了他们自己对利希滕斯坦和斯洛维奇所描述现象的研究。
  - 现译：偏好逆转的报告发表几年后，两位受人尊敬的经济学家戴维·格雷瑟和查尔斯·普洛特在声望很高的《美国经济评论》上发表了一篇文章，报告了他们自己的研究，研究的正是利希滕斯坦和斯洛维奇描述的那个现象。
  - 处理：Astra 复核通过。“对……所描述现象的研究”长定语加“所”字

- 英文：“How tall is John?” If John is 5' tall, your answer will depend on his age; he is very tall if he is 6 years old, very short if he is 16.
  - 原译：“约翰有多高？”如果约翰身高 5 英尺，你的回答就取决于他的年龄：如果他 6 岁，他就很高；如果他 16 岁，他就很矮。
  - 现译：“约翰有多高？”如果约翰身高 5 英尺，你的回答就取决于他的年龄：他要是 6 岁，就很高；要是 16 岁，就很矮。
  - 处理：Astra 复核通过。连用“如果他……他就”，代词和连接词多余

- 英文：You should not form the impression that single and joint evaluations are always inconsistent, or that judgments are completely chaotic.
  - 原译：你不应该由此形成这样的印象：单独评估和联合评估总是不一致，或者判断完全是一团混乱。
  - 现译：你不应该因此以为，单独评估和联合评估总是不一致，或者判断完全是一团混乱。
  - 处理：Astra 复核通过。form the impression 直译成“形成这样的印象”

- 英文：Judgments and preferences are coherent within categories but potentially incoherent when the objects that are evaluated belong to different categories.
  - 原译：在同一个类别之内，判断和偏好是一致的；但当被评估的对象属于不同类别时，就可能不一致。
  - 现译：在同一个类别之内，判断和偏好是一致的；但如果评估的对象属于不同类别，就可能不一致。
  - 处理：Astra 复核通过。“当……时”加“被评估的”被动定语

- 英文：A special fund supported by private contributions has been set up to provide pollution-free breeding locations for dolphins.
  - 原译：一个由私人捐款支持的专项基金已经成立，为海豚提供没有污染的繁殖地。
  - 现译：现已成立一个由私人捐款支持的专项基金，为海豚提供没有污染的繁殖地。
  - 处理：Astra 复核通过。“一个……已经成立”照搬英文语序，长主语开头

- 英文：Whether or not you were fully aware of them, ideas and memories of related causes came to your mind.
  - 原译：不管你有没有完全意识到，与此相关的公益事业的想法和记忆都浮现在你的脑中。
  - 现译：不管你有没有完全意识到，关于相关公益事业的想法和记忆，都浮现在了你的脑中。
  - 处理：Astra 复核通过。“的”字连串，“公益事业的想法”修饰关系含糊

- 英文：Like many other difficult questions, the assessment of dollar value can be solved by substitution and intensity matching.
  - 原译：和许多其他难题一样，美元价值的评估可以靠替代和强度匹配来解决。
  - 现译：和许多其他难题一样，评估美元价值这个问题，也可以靠替代和强度匹配来解决。
  - 处理：Astra 复核通过。“美元价值的评估”名词化作主语，和“难题”对不上

- 英文：As you translated your impression of the relative importance of the skin cancer issue into a dollar amount, you might well have come up with a smaller contribution than you offered to protect an endearing animal.
  - 原译：当你把皮肤癌问题在你印象中的相对重要性转换成美元数额时，你得出的捐款很可能比为保护那种惹人喜爱的动物给出的要少。
  - 现译：你把印象中皮肤癌问题的相对重要性转换成美元数额，定出的捐款额很可能比为保护那种惹人喜爱的动物给出的数额少。
  - 处理：按复核意见修改。“当……时”加重复的“你”，状语插在名词中间 复核：“得出的捐款”搭配不当；这里得出并比较的是捐款数额。

- 英文：Case 2: The unscrupulous dealings of a bank caused another bank a loss of $10 million.
  - 原译：案件 2：一家银行不择手段的交易，给另一家银行造成了 1,000 万美元的损失。
  - 现译：案件 2：一家银行在交易中不择手段，让另一家银行损失了 1,000 万美元。
  - 处理：Astra 复核通过。抽象名词“交易”作主语，“造成了……的损失”

- 英文：When the cases were considered together, however, sympathy for the individual victim prevailed over the anchoring effect and the jurors increased the award to the child to surpass the award to the bank.
  - 原译：然而，当两个案件放在一起考虑时，对个人受害者的同情胜过了锚定效应，陪审员提高了判给孩子的赔偿，使之超过了判给银行的赔偿。
  - 现译：然而，两个案件放在一起考虑时，对个人受害者的同情胜过了锚定效应，陪审员提高了判给孩子的赔偿，让它超过了判给银行的数额。
  - 处理：Astra 复核通过。“当……时”和书面腔的“使之”

- 英文：They could not anticipate that the award to the child would appear inadequate in the context of a large award to a financial institution.
  - 原译：他们预料不到，在判给一家金融机构一大笔赔偿的背景下，判给孩子的赔偿会显得不够。
  - 现译：他们预料不到，跟判给一家金融机构的一大笔赔偿放在一起，判给孩子的赔偿会显得不够。
  - 处理：Astra 复核通过。in the context of 直译成“在……的背景下”

- 英文：He concluded that “within categories, penalties seem extremely sensible, at least in the sense that the more serious harms are punished more severely.
  - 原译：“在类别之内，处罚似乎非常合理，至少在越严重的危害受到越严厉的惩罚这个意义上是这样。
  - 现译：“在类别之内，处罚似乎非常合理，至少从危害越严重、惩罚越重这一点看是这样。
  - 处理：Astra 复核通过。in the sense that 直译成“在……这个意义上”，中间夹着长从句

## 第 34 章 框架与现实

- 英文：The fact that logically equivalent statements evoke different reactions makes it impossible for Humans to be as reliably rational as Econs.
  - 原译：逻辑上等价的陈述会唤起不同的反应，这一事实使普通人不可能像经济人那样始终可靠地保持理性。
  - 现译：逻辑上等价的陈述会引发不同的反应，因此，普通人不可能像经济人那样始终保持理性。
  - 处理：按复核意见修改。照搬“这一事实使……”的抽象主语结构 复核：因果关系保留正确，但“始终可靠地保持理性”仍然生硬、累赘。

- 英文：Remarkably, the “rational” individuals were not those who showed the strongest neural evidence of conflict.
  - 原译：值得注意的是，这些“理性”的人，并不是冲突的神经证据最强的那些人。
  - 现译：值得注意的是，这些“理性”的人，并不是神经活动显示冲突最强烈的那些人。
  - 处理：Astra 复核通过。“冲突的神经证据最强”是名词短语硬译，搭配生硬

- 英文：Physician participants were given statistics about the outcomes of two treatments for lung cancer: surgery and radiation.
  - 原译：参加实验的医生拿到了肺癌两种疗法的疗效统计数据，这两种疗法是手术和放疗。
  - 现译：参加实验的医生拿到了手术和放疗这两种肺癌疗法的疗效统计数据。
  - 处理：Astra 复核通过。照搬英文冒号补充结构，另起一句重复“这两种疗法”

- 英文：Amos and I introduced our discussion of framing by an example that has become known as the “Asian disease problem”:
  - 原译：阿莫斯和我用一个例子引出了对框架的讨论，这个例子后来被人们称作“亚洲疾病问题”：
  - 现译：阿莫斯和我用一个例子引出了对框架的讨论，这个例子后来被人们称作“亚洲疾病问题”：
  - 处理：复核后退回原译。“被人们称作”是不必要的被动句 复核：known as 表示“被称为”，不等于“以……闻名”；改写增加了知名度方面的含义，原译更准确。

- 英文：These conclusions were well established for choices about gambles and sure things in the domain of money.
  - 原译：在涉及金钱的赌局和确定的事之间作选择时，这些结论早已得到确证。
  - 现译：对于涉及金钱的赌局和确定的事之间的选择，这些结论早已得到确证。
  - 处理：复核后重写。把 for choices 硬译成时间状语“作选择时”，和“结论得到确证”接不上 复核：删去了 choices 所指的选择行为。原文说这些结论已在金钱领域中有关赌局和确定的事的选择上得到确证，而不是笼统地说两类事物得到这些结论的支持。

- 英文：The difference between the tax due by a childless family and by a family with two children is described as a reduction of tax in the first version and as an increase in the second.
  - 原译：没有孩子的家庭和有两个孩子的家庭应缴税款之间的差额，在第一个版本里被描述为减税，在第二个版本里被描述为加税。
  - 现译：没有孩子的家庭和有两个孩子的家庭，应缴税款之间的差额在第一个版本里被说成减税，在第二个版本里被说成加税。
  - 处理：复核后重写。主语前定语过长，又连用两个“被描述为” 复核：“应缴的税款有一个差额”搭配生硬，拆句后又重复“差额”，比原译更拖沓，未改善可读性。

- 英文：The message about the nature of framing is stark: framing should not be viewed as an intervention that masks or distorts an underlying preference.
  - 原译：关于框架的本质，这里得出的结论毫不含糊：不应该把框架看成一种掩盖或扭曲了某种潜在偏好的干预。
  - 现译：关于框架的本质，这里得出的结论毫不含糊：不应该把框架看成一种掩盖或扭曲了某种潜在偏好的干预。
  - 处理：复核后退回原译。英文定语从句前置成一长串修饰语，压在“干预”前面 复核：“不应该把框架看成一种干预”扩大了否定范围。原文否定的是把框架视为掩盖或扭曲潜在偏好的干预，并非笼统否定框架是一种干预。

- 英文：The formulation of that directive is another case in which one frame is clearly superior to the other.
  - 原译：这项意愿怎样表述，是一种框架明显优于另一种框架的又一个例子。
  - 现译：在这项意愿的表述上，同样有一种框架明显优于另一种框架。
  - 处理：Astra 复核通过。照搬 is another case in which 结构，“的又一个例子”前定语过长

- 英文：Unless they take this simple action, they are considered willing donors.
  - 原译：除非他们做了这个简单的动作，否则就被视为愿意捐献。
  - 现译：只要没做这个简单的动作，他们就被视为愿意捐献。
  - 处理：Astra 复核通过。Unless 直译成“除非……否则”，读起来绕

- 英文：The best single predictor of whether or not people will donate their organs is the designation of the default option that will be adopted without having to check a box.
  - 原译：最能预测人们是否会捐献器官的单一因素，就是默认选项的设定，也就是不打勾就会被采用的那个选项是什么。
  - 现译：要预测人们是否会捐献器官，最好的单一指标就是默认选项怎么设定，也就是不打勾时会采用哪个选项。
  - 处理：Astra 复核通过。主语前长定语，“的设定”是名词化，“被采用的那个选项是什么”照搬从句

- 英文：If you believe that a large supply of donated organs is good for society, you will not be neutral between a formulation that yields almost 100% donations and another formulation that elicits donations from 4% of drivers.
  - 原译：如果你认为捐献器官的供应充足对社会有益，那么在一种能带来接近 100% 捐献率的表述和另一种只能让 4% 的司机捐献的表述之间，你就不会保持中立。
  - 现译：一种表述能带来接近 100% 的捐献率，另一种却只能让 4% 的司机捐献器官。如果你认为捐献器官的供应充足对社会有益，就不会在这两种表述之间保持中立。
  - 处理：按复核意见修改。“在……之间”里塞进两个带长定语的“表述”，句子头重脚轻 复核：“如果……那么”之间的对应关系被拆乱了，容易读成人的看法决定两种表述的捐献率。原文的条件只限定“你不会保持中立”。

- 英文：Furthermore, it is not how we experience the workings of our mind, but the evidence for these cognitive illusions is undeniable.
  - 原译：而且，我们自己感觉到的心智运作方式也并非如此，但这些认知错觉的证据无可否认。
  - 现译：而且，我们也感觉不到自己的心智是这样运作的，但这些认知错觉的证据无可否认。
  - 处理：Astra 复核通过。把 how we experience the workings 名词化成“感觉到的心智运作方式”

- 英文：“They will feel better about what happened if they manage to frame the outcome in terms of how much money they kept rather than how much they lost.”
  - 原译：“要是他们能用‘保住了多少钱’的框架来看这个结果，别老想着亏了多少，他们对这件事会好受一些。”
  - 现译：“要是他们能用‘保住了多少钱’而不是‘亏了多少钱’的框架来看这个结果，心里就会好受一些。”
  - 处理：复核后重写。feel better about 直译成“对这件事会好受”，口语里不这么说，代词也多余 复核：“心里就会好受一些”有所改善，但仍沿用了旧译的问题：“别老想着”把两种框架的对比改成了劝告，还增加了反复想着损失的含义。

- 英文：“They ask you to check the box to opt out of their mailing list. Their list would shrink if they asked you to check a box to opt in!”
  - 原译：“他们让你打勾退出他们的邮件列表。要是改成让你打勾才能加入，他们的名单就会缩水！”
  - 现译：“他们让你打勾退出邮件列表。要是改成打勾才能加入，名单就会缩水！”
  - 处理：Astra 复核通过。照搬英文代词，两句话里出现四个“他们”“你”

## 第 35 章 两个自我

- 英文：A decision maker who pays different amounts to achieve the same gain of experienced utility (or be spared the same loss) is making a mistake.
  - 原译：一个决策者如果为了得到同样多的体验效用（或者免去同样多的损失）而付出不同的代价，他就犯了错误。
  - 现译：决策者如果为了得到同样多的体验效用（或者免去同样多的损失）而付出不同的代价，就是在犯错。
  - 处理：Astra 复核通过。多余的“一个”和回指代词“他”

- 英文：This was Edgeworth’s theory, and we now have a precise understanding of the conditions under which his theory holds.
  - 原译：这就是埃奇沃思的理论，我们现在已经准确地了解了他的理论成立的条件。
  - 现译：这就是埃奇沃思的理论，现在我们已经确切地知道，这个理论在什么条件下成立。
  - 处理：Astra 复核通过。have a precise understanding of the conditions under which 名词化硬译，“了解了……的条件”生硬

- 英文：I will call the measures based on reports of momentary pain hedonimeter totals.
  - 原译：我把根据每一时刻的疼痛报告得出的这类测量值称为快乐计总量。
  - 现译：这类根据每一时刻的疼痛报告得出的测量值，我称之为快乐计总量。
  - 处理：Astra 复核通过。“把……称为”中间夹了一长串宾语定语

- 英文：Peak-end rule: The global retrospective rating was well predicted by the average of the level of pain reported at the worst moment of the experience and at its end.
  - 原译：峰终定律：对整个经历的回顾性评分，可以用两个时刻所报告疼痛程度的平均值很好地预测出来，一个是体验中最糟糕的时刻，一个是体验结束的时刻。
  - 现译：峰终定律：把体验中最糟糕的时刻和结束时刻报告的疼痛程度取平均值，就能很好地预测对整个经历的回顾性评分。
  - 处理：Astra 复核通过。照搬被动语序，“所报告疼痛程度”文白夹杂，两个时刻放到句末补说

- 英文：The hedonimeter totals are computed by an observer from an individual’s report of the experience of moments.
  - 原译：快乐计总量是由一位观察者根据一个人对每一时刻体验的报告计算出来的。
  - 现译：快乐计总量由观察者根据当事人对每一时刻体验的报告计算得出。
  - 处理：Astra 复核通过。“是由……计算出来的”被动框架，加上冠词直译的“一位”“一个人”

- 英文：A comment I heard from a member of the audience after a lecture illustrates the difficulty of distinguishing memories from experiences.
  - 原译：有一次讲座结束后，一位听众对我说的话，说明了把记忆和体验区分开有多难。
  - 现译：有一次讲座结束后，一位听众跟我说了一番话，这番话说明了把记忆和体验区分开有多难。
  - 处理：Astra 复核通过。把 A comment I heard 整个当主语，“一位听众对我说的话，说明了”像英文

- 英文：Fully 80% of the participants who reported that their pain diminished during the final phase of the longer episode opted to repeat it, thereby declaring themselves willing to suffer 30 seconds of needless pain in the anticipated third trial.
  - 原译：在报告说长的那次经历的最后阶段疼痛有所减轻的参与者中，足足有 80% 选择重复这一次，这就等于表示，他们愿意在预想中的第三次试验里多忍受 30 秒不必要的疼痛。
  - 现译：有些参与者报告说，长的那次经历到了最后阶段，疼痛有所减轻；这些人当中足足有 80% 选择重复这一次，这就等于表示，他们愿意在预想中的第三次试验里多忍受 30 秒不必要的疼痛。
  - 处理：Astra 复核通过。定语从句整个前置，“参与者”前堆了一长串修饰

- 英文：Other classic studies showed that electrical stimulation of specific areas in the rat brain (and of corresponding areas in the human brain) produce a sensation of intense pleasure, so intense in some cases that rats who can stimulate their brain by pressing a lever will die of starvation without taking a break to feed themselves.
  - 原译：另一些经典研究表明，用电刺激大鼠大脑的特定区域（以及人脑中相应的区域），会产生强烈的快感，在某些情况下强烈到这种程度：能通过按压杠杆来刺激自己大脑的大鼠，会顾不上停下来进食，最后活活饿死。
  - 现译：另一些经典研究表明，用电刺激大鼠大脑的特定区域（以及人脑中相应的区域），会产生强烈的快感。在某些情况下，大鼠能通过按压杠杆来刺激自己的大脑，快感强烈得让它们顾不上停下来进食，最后活活饿死。
  - 处理：Astra 复核通过。so intense that 硬译成“强烈到这种程度：”，后面又接带长定语的“大鼠”

- 英文：Decisions that do not produce the best possible experience and erroneous forecasts of future feelings—both are bad news for believers in the rationality of choice.
  - 原译：不能带来最佳体验的决策，以及对未来感受的错误预测，对于相信选择是理性的人来说，两者都是坏消息。
  - 现译：决策带不来尽可能好的体验，对未来感受的预测出了错，这两种情况对相信选择是理性的人来说都是坏消息。
  - 处理：Astra 复核通过。照搬英文名词短语并列加破折号的结构，又用“对于……来说”

- 英文：A memory that neglects duration will not serve our preference for long pleasure and short pains.
  - 原译：一种忽视时长的记忆，无法满足我们对长久快乐和短暂痛苦的偏好。
  - 现译：忽视时长的记忆，满足不了我们对长久快乐和短暂痛苦的偏好。
  - 处理：Astra 复核通过。冠词直译成多余的“一种”

- 英文：“You are thinking of your failed marriage entirely from the perspective of the remembering self.
  - 原译：“你完全是从记忆自我的角度来看你那段失败的婚姻。
  - 现译：“你看那段失败的婚姻，完全是站在记忆自我的角度。
  - 处理：Astra 复核通过。饮水机旁的口语里重复“你……你那段”，照搬英文语序

## 第 36 章 作为故事的人生

- 英文：The same core features appear in the rules of narratives and in the memories of colonoscopies, vacations, and films.
  - 原译：叙事的规则里有同样的核心特征，人们对结肠镜检查、度假和电影的记忆里也有。
  - 现译：同样的核心特征，既见于叙事的规则，也见于人们对结肠镜检查、度假和电影的记忆。
  - 处理：Astra 复核通过。句子拆成两截，后半句“……的记忆里也有”像补上去的

- 英文：Indeed, we can be deeply moved even by events that change the stories of people who are already dead.
  - 原译：事实上，即使一件事改变的是已经去世的人的故事，它也能深深打动我们。
  - 现译：事实上，哪怕一件事改变的是已故之人的故事，也能深深触动我们。
  - 处理：按复核意见修改。“已经去世的人的故事”的字连用，代词“它”多余 复核：“也会深受触动”偏向确定的结果，原文 can be 表示可能性，应保留这一情态。

- 英文：We feel the humiliation of a scientist who made an important discovery that was proved false after she died, although she did not experience the humiliation.
  - 原译：一位科学家做出了一项重要发现，在她死后，这项发现被证明是错的，我们会替她感到屈辱，尽管她本人并没有体验到这种屈辱。
  - 现译：一位科学家做出了一项重要发现，她死后，这项发现被证明是错的；她本人并没有体验到这种屈辱，我们却会替她感到屈辱。
  - 处理：Astra 复核通过。让步从句“尽管……”照搬英文放在句末

- 英文：In one version of Jen’s story, she was extremely happy throughout her life (which lasted either 30 or 60 years), enjoying her work, taking vacations, spending time with her friends and on her hobbies.
  - 原译：在一个版本的故事里，珍一生都极其幸福（她的一生要么是 30 年，要么是 60 年）：她喜欢自己的工作，会去度假，花时间陪朋友、培养自己的爱好。
  - 现译：在一个版本的故事里，珍一生都极其幸福（她活了 30 年或 60 年）：她喜欢自己的工作，会去度假，把时间花在朋友和自己的爱好上。
  - 处理：复核后重写。“一生要么是……要么是……”照搬 either…or 复核：括注改得更自然，但沿用了旧译中的偏差：spending time on her hobbies 指花时间从事业余爱好，不是培养爱好。

- 英文：The extra years were described as pleasant but less so than before.
  - 原译：多出来的这几年被描述为愉快的，但不如以前那么愉快。
  - 现译：文中说，多出来的这几年过得愉快，但不如以前那么愉快。
  - 处理：Astra 复核通过。被动句“被描述为愉快的”

- 英文：Clearly, her life was represented by a prototypical slice of time, not as a sequence of time slices.
  - 原译：显然，人们是用一个典型的时间切片来表征她的一生的，而非把它表征为一连串的时间切片。
  - 现译：显然，人们用一个典型的时间切片来代表她的一生，而非把它看成一连串的时间切片。
  - 处理：Astra 复核通过。“是用……来表征……的，而非把它表征为……”句式生硬

- 英文：As expected from this idea, Diener and his students also found a less-is-more effect, a strong indication that an average (prototype) has been substituted for a sum.
  - 原译：正如这个观点所预料的那样，迪纳和他的学生还发现了少即是多效应，这有力地表明，人们用平均值（原型）替代了总和。
  - 现译：迪纳和他的学生还发现了这个观点所预料的少即是多效应，这有力地表明，人们用平均值（原型）替代了总和。
  - 处理：Astra 复核通过。句首“正如……所预料的那样”是 as expected 的套译

- 英文：At my urging, they also collected data on the effect of the extra 5 years in a within-subject experiment; each participant made both judgments in immediate succession.
  - 原译：在我的敦促下，他们还用一项组内实验收集了数据，看看多出的 5 年有什么影响：每位参与者接连对两个版本作出判断。
  - 现译：每位参与者接连对两个版本作出判断。
  - 处理：复核后退回原译。虚化动词“作出判断” 复核：“判断两个版本”搭配生硬，也没有“对两个版本作出判断”清楚。“作出判断”在这里是正常表达，不宜机械删减。

- 英文：The pattern of judgments seemed so absurd that Diener and his students initially thought that it represented the folly of the young people who participated in their experiments.
  - 原译：这种判断模式显得太荒唐了，迪纳和他的学生起初以为，这反映的是参加他们实验的年轻人的愚蠢。
  - 现译：这种判断模式显得太荒唐了，迪纳和他的学生起初以为，这反映出参加他们实验的年轻人很愚蠢。
  - 处理：Astra 复核通过。“年轻人的愚蠢”把形容词名词化，的字连用

- 英文：The pains of labor and the benefits of vacations always come up as objections to the idea of duration neglect: we all share the intuition that it is much worse for labor to last 24 than 6 hours, and that 6 days at a good resort is better than 3.
  - 原译：分娩的痛苦和度假的好处，总是被人拿来反驳忽视时长的观点：我们都有这样的直觉，分娩持续 24 小时比持续 6 小时糟糕得多，在一个好的度假胜地待 6 天比待 3 天好。
  - 现译：说到忽视时长，总有人拿分娩的痛苦和度假的好处来反驳：我们都有这样的直觉，分娩持续 24 小时比持续 6 小时糟糕得多，在一个好的度假胜地待 6 天比待 3 天好。
  - 处理：Astra 复核通过。被动句“总是被人拿来反驳”

- 英文：What truly matters when we intuitively assess such episodes is the progressive deterioration or improvement of the ongoing experience, and how the person feels at the end.
  - 原译：我们凭直觉评估这类片段时，真正要紧的是正在进行的体验逐渐变坏或逐渐变好的过程，以及这个人在结尾时的感受。
  - 现译：我们凭直觉评估这类片段时，真正要紧的是体验在进行中是逐渐变坏还是逐渐变好，以及这个人在结尾时的感受。
  - 处理：Astra 复核通过。名词前堆长定语“正在进行的体验逐渐变坏或逐渐变好的过程”

- 英文：Distinct industries have developed to cater to these alternatives: resorts offer restorative relaxation; tourism is about helping people construct stories and collect memories.
  - 原译：针对这两种选择，已经发展出了不同的行业：度假村提供让人恢复元气的放松；旅游业则帮人们构建故事、收集记忆。
  - 现译：针对这两种选择，已经发展出了不同的行业：度假村提供让人恢复元气的放松；旅游业则帮人们构建故事、收集记忆。
  - 处理：复核后退回原译。无主句“已经发展出了不同的行业”照搬 have developed 复核：“行业来迎合选择”搭配不自然，也淡化了不同行业为满足这些需求而发展起来的意思。原译的“已经发展出了不同的行业”是自然的中文表达。

- 英文：In other situations—love comes to mind—the declaration that the present moment will never be forgotten, though not always accurate, changes the character of the moment.
  - 原译：在另一些情境中（我想到的是爱情），宣称此刻永远不会被忘记，虽然未必准确，却改变了这一刻的性质。
  - 现译：在另一些情境中（我想到的是爱情），说出“永远不会忘记这一刻”，虽然未必准确，却改变了这一刻的性质。
  - 处理：复核后重写。被动句“此刻永远不会被忘记” 复核：原文间接描述一种宣言，改写却新增第一人称“我”并写成直接引语，把未限定主体的“不会被忘记”收窄成说话者自己的承诺。

- 英文：A self-consciously memorable experience gains a weight and a significance that it would not otherwise have.
  - 原译：一段经历如果在发生时就被人有意当作难忘的时刻，就会获得它本来不会有的分量和意义。
  - 现译：人们如果在经历一件事时就有意把它当作难忘的时刻，这件事就会有它本来不会有的分量和意义。
  - 处理：Astra 复核通过。被动句“被人有意当作”，“获得……分量”搭配生硬

- 英文：The students also provided a global rating of the vacation when it had ended.
  - 原译：假期结束时，学生们还对整个假期作了一个总体评分。
  - 现译：假期结束时，学生们还对整个假期作了一个总体评分。
  - 处理：复核后退回原译。虚化动词“作了一个总体评分” 复核：global rating 是对假期整体的评分，不是汇总各项或各天分数所得的“总分”。原译“总体评分”准确，也不生硬。

- 英文：Statistical analysis established that the intentions for future vacations were entirely determined by the final evaluation—even when that score did not accurately represent the quality of the experience that was described in the diaries.
  - 原译：统计分析证实，人们对未来度假的打算完全由最后的评价决定，即使这个分数并不能准确反映日记里描述的体验的质量。
  - 现译：统计分析证实，人们以后还想不想这样度假，完全取决于最后的评价，哪怕这个分数并没有准确反映日记里记下的体验质量。
  - 处理：Astra 复核通过。“对未来度假的打算”名词化，“日记里描述的体验的质量”的字连用

- 英文：Here again, my informal observation is that most people are remarkably indifferent to the pains of their experiencing self.
  - 原译：这里，我的非正式观察同样是：大多数人对自己的体验自我所受的痛苦出奇地漠不关心。
  - 现译：在这个问题上，我非正式观察到的情况也一样：大多数人对自己的体验自我所受的痛苦出奇地漠不关心。
  - 处理：Astra 复核通过。句首“这里，”直译 here again

- 英文：“He is desperately trying to protect the narrative of a life of integrity, which is endangered by the latest episode.”
  - 原译：“他拼命想维护自己一生正直的故事，最近这件事让这个故事岌岌可危。”
  - 现译：“他拼命想守住‘一生正直’这个故事，最近这件事让它岌岌可危。”
  - 处理：Astra 复核通过。“一生正直的故事”定语生硬，“这个故事”重复，不像口语

- 英文：“The length to which he was willing to go for a one-night encounter is a sign of total duration neglect.”
  - 原译：“为了一夜情，他肯花那么大的力气，这是完全忽视时长的表现。”
  - 现译：“为了一夜情，他肯花那么大的力气，这说明他完全忽视了时长。”
  - 处理：Astra 复核通过。“这是……的表现”是 a sign of 的书面套话，不像闲谈

- 英文：“She is an Alzheimer’s patient. She no longer maintains a narrative of her life, but her experiencing self is still sensitive to beauty and gentleness.”
  - 原译：“她是阿尔茨海默病患者。她已经不再维系自己一生的故事，但她的体验自我依然能感受到美和温柔。”
  - 现译：“她得了阿尔茨海默病。她已经不再维系自己一生的故事，但她的体验自我依然能感受到美和温柔。”
  - 处理：Astra 复核通过。“她是……患者”照搬英文名词表达，口语会说“得了……病”

## 第 37 章 体验幸福感

- 英文：When I became interested in the study of well-being about fifteen years ago, I quickly found out that almost everything that was known about the subject drew on the answers of millions of people to minor variations of a survey question, which was generally accepted as a measure of happiness.
  - 原译：大约十五年前，我开始对幸福感研究产生兴趣，很快就发现，人们对这个课题所知道的几乎一切，都来自数百万人对一个调查问题的回答。
  - 现译：大约十五年前，我对幸福感研究产生了兴趣，很快就发现，关于这个课题，人们知道的几乎一切都来自数百万人对一个调查问题的回答。
  - 处理：Astra 复核通过。“人们对这个课题所知道的几乎一切”照搬 everything that was known about

- 英文：As the remembering self had not proved to be a good witness in my experiments, I focused on the well-being of the experiencing self.
  - 原译：在我的实验里，记忆自我并没有证明自己是个可靠的证人，于是我把注意力集中在体验自我的幸福感上。
  - 现译：在我的实验里，事实证明记忆自我并不是个好证人，于是我把注意力集中在体验自我的幸福感上。
  - 处理：Astra 复核通过。“没有证明自己是……”直译 had not proved to be，读成“缺少证据”，意思偏了

- 英文：One of the examples I had in mind for a situation that Helen would wish to continue is total absorption in a task, which Mihaly Csikszentmihalyi calls flow—a state that some artists experience in their creative moments and that many other people achieve when enthralled by a film, a book, or a crossword puzzle: interruptions are not welcome in any of these situations.
  - 原译：海伦会希望持续下去的情境，我当时想到的例子之一，是全身心地投入一项任务，米哈里·契克森米哈赖把这种状态称为“心流”。一些艺术家在创作时会体验到这种状态，许多其他人被一部电影、一本书或一个填字游戏深深吸引时，也会进入这种状态：在这些情境里，谁都不愿被打断。
  - 现译：说到海伦会希望持续下去的情境，我当时想到的一个例子是全身心投入一项任务，米哈里·契克森米哈赖把这种状态称为“心流”。一些艺术家在创作时会体验到这种状态，其他许多人被一部电影、一本书或一个填字游戏深深吸引时，也会进入这种状态：在这些情境里，谁都不愿被打断。
  - 处理：Astra 复核通过。“……的情境，我当时想到的例子之一，是……”照搬 one of the examples；“许多其他人”是英文词序

- 英文：I proposed to measure Helen’s objective happiness precisely as we assessed the experience of the two colonoscopy patients, by evaluating a profile of the well-being she experienced over successive moments of her life.
  - 原译：我提议，测量海伦的客观幸福，方法要和我们评估那两位结肠镜检查患者的体验完全一样：评估她在生活中一个接一个的时刻所体验到的幸福感，看它画出的曲线。
  - 现译：我提议，测量海伦的客观幸福，方法和我们评估那两位结肠镜检查患者的体验完全一样：把她在生活中一个接一个的时刻体验到的幸福感连成一条曲线，再评估这条曲线。
  - 处理：Astra 复核通过。“评估……幸福感，看它画出的曲线”照搬 by evaluating a profile，语意含糊

- 英文：We hoped it would approximate the results of experience sampling and provide additional information about the way people spend their time.
  - 原译：我们希望它得出的结果接近经验取样，还能提供更多关于人们怎样度过时间的信息。
  - 现译：我们希望它能得出与经验取样相近的结果，还能让我们更多地了解人们怎样度过时间。
  - 处理：按复核意见修改。“提供更多关于……的信息”是 provide information about 的套译 复核：仍保留了旧译的比较对象错误：“结果”应与经验取样的“结果”比较，不能直接说结果接近一种方法。

- 英文：We assumed that our participants would fairly accurately recover the feeling of a prototypical moment of the episode. Several comparisons with experience sampling confirmed the validity of the DRM.
  - 原译：我们假定，参与者能相当准确地找回每个片段中一个原型时刻的感受。与经验取样所做的几次比较，证实了日重现法的有效性。
  - 现译：我们假定，参与者能相当准确地回想起每个片段里一个典型时刻的感受。和经验取样所做的几次比较证实，日重现法是有效的。
  - 处理：Astra 复核通过。“找回感受”“原型时刻”直译；抽象名词“比较”作主语“证实了……有效性”

- 英文：Our questionnaire also included measures of life satisfaction, which we interpreted as the satisfaction of the remembering self.
  - 原译：我们的问卷还包括对生活满意度的测量，我们把它理解为记忆自我的满意度。
  - 现译：我们的问卷还测量了生活满意度，我们把它理解为记忆自我的满意度。
  - 处理：Astra 复核通过。“包括对……的测量”名词化

- 英文：It appears that a small fraction of the population does most of the suffering—whether because of physical or mental illness, an unhappy temperament, or the misfortunes and personal tragedies in their life.
  - 原译：看起来，大部分痛苦是由一小部分人承受的，原因可能是身体或精神上的疾病，可能是郁郁寡欢的性情，也可能是生活中的不幸和个人悲剧。
  - 现译：看起来，大部分痛苦都落在一小部分人身上，原因可能是身体或精神上的疾病，可能是郁郁寡欢的性情，也可能是生活中的不幸和个人悲剧。
  - 处理：Astra 复核通过。“是由……承受的”被动结构

- 英文：For 1,000 American women in a Midwestern city, the U-index was 29% for the morning commute, 27% for work, 24% for child care, 18% for housework, 12% for socializing, 12% for TV watching, and 5% for sex.
  - 原译：对美国中西部一座城市的 1,000 名女性来说，早上通勤的 U 指数是 29%，工作是 27%，照看孩子是 24%，做家务是 18%，社交是 12%，看电视是 12%，性生活是 5%。
  - 现译：美国中西部一座城市的 1,000 名女性，早上通勤的 U 指数是 29%，工作是 27%，照看孩子是 24%，做家务是 18%，社交是 12%，看电视是 12%，性生活是 5%。
  - 处理：Astra 复核通过。“对……来说”照搬 For…

- 英文：The biggest surprise was the emotional experience of the time spent with one’s children, which for American women was slightly less enjoyable than doing housework.
  - 原译：最大的意外，是和自己的孩子一起度过的时光带来的情绪体验：对美国女性来说，这段时间的愉快程度还略低于做家务。
  - 现译：最大的意外，是和自己孩子在一起时的情绪体验：对美国女性来说，这段时间的愉快程度还略低于做家务。
  - 处理：Astra 复核通过。名词前堆长定语“和自己的孩子一起度过的时光带来的”

- 英文：More important are situational factors such as an opportunity to socialize with coworkers, exposure to loud noise, time pressure (a significant source of negative affect), and the immediate presence of a boss (in our first study, the only thing that was worse than being alone).
  - 原译：更重要的是情境因素，比如有没有机会和同事交往，是否暴露在很大的噪声里，时间压力（消极情感的一个重要来源），以及老板是否就在身边（在我们的第一项研究中，这是唯一比独自一人还糟的情况）。
  - 现译：更重要的是情境因素，比如有没有机会和同事交往，周围噪声大不大，时间压力（消极情感的一个重要来源），以及老板是否就在身边（在我们的第一项研究中，这是唯一比独自一人还糟的情况）。
  - 处理：Astra 复核通过。“暴露在很大的噪声里”直译 exposure to loud noise

- 英文：We found that French and American women spent about the same amount of time eating, but for Frenchwomen, eating was twice as likely to be focal as it was for American women.
  - 原译：我们发现，法国女性和美国女性花在吃饭上的时间差不多，但对法国女性来说，吃饭成为注意焦点的可能性是美国女性的两倍。
  - 现译：我们发现，法国女性和美国女性花在吃饭上的时间差不多，但法国女性把吃饭当作注意焦点的可能性是美国女性的两倍。
  - 处理：Astra 复核通过。“对……来说，吃饭成为注意焦点的可能性”照搬英文主语

- 英文：The economist on our team, Alan Krueger, took the lead in an effort to introduce elements of this method into national statistics.
  - 原译：我们团队里的经济学家艾伦·克鲁格，牵头推动了把这种方法的一些要素纳入国家统计的工作。
  - 现译：我们团队里的经济学家艾伦·克鲁格牵头，推动将这种方法的一些要素纳入国家统计。
  - 处理：按复核意见修改。“推动了把……的工作”长定语套在“工作”前 复核：“这项工作”容易回指上一句的联合调查，模糊了克鲁格牵头的具体事项。原文明确指推动将方法的一些要素纳入国家统计。

- 英文：An analysis of more than 450,000 responses to the Gallup-Healthways Well-Being Index, a daily survey of 1,000 Americans, provides a surprisingly definite answer to the most frequently asked question in well-being research: Can money buy happiness?
  - 原译：对这项调查的 450,000 多份回答所做的分析，为幸福感研究中最常被问到的那个问题给出了一个明确得令人意外的答案。
  - 现译：盖洛普-健康之路幸福指数（Gallup-Healthways Well-Being Index）每天调查 1,000 名美国人。研究者分析了这项调查的 450,000 多份回答，对幸福感研究中最常被问到的那个问题，得出了一个明确得令人意外的答案。
  - 处理：复核后重写。抽象主语“对……所做的分析” 复核：原文明确分析了 450,000 多份回答，改写只明确调查收到了这么多回答，没有清楚保留分析样本的数量。原译以“分析”作主语自然且准确。

- 英文：A headache increases the proportion reporting sadness and worry from 19% to 38% for individuals in the top two-thirds of the income distribution.
  - 原译：在收入分布中处于上面三分之二的人里，头痛会让报告感到悲伤和担忧的人所占的比例从 19% 升到 38%。
  - 现译：在收入排在前三分之二的人里，头痛会让报告感到悲伤和担忧的人所占的比例从 19% 升到 38%。
  - 处理：Astra 复核通过。“在收入分布中处于上面三分之二”直译 top two-thirds of the income distribution

- 英文：The average increase of experienced well-being associated with incomes beyond that level was precisely zero.
  - 原译：收入超过这个水平后，与之相伴的体验幸福感平均增幅恰好为零。
  - 现译：收入超过这个水平以后，体验幸福感的平均增幅恰好是零。
  - 处理：Astra 复核通过。“与之相伴的”是 associated with 的套译

- 英文：Higher income brings with it higher satisfaction, well beyond the point at which it ceases to have any positive effect on experience.
  - 原译：收入更高，满意度也更高，即使收入已经远远超过了对体验不再有任何积极影响的那个点，也依然如此。
  - 现译：收入更高，满意度也更高；即使收入已经远远超过饱和点，不再给体验带来任何积极影响，也依然如此。
  - 处理：复核后重写。长定语“对体验不再有任何积极影响的那个点”照搬 the point at which 复核：“早已”增加了原文没有的时间含义；拆句后，“那个点”的定义也不够直接。原文比较的是收入水平，不是超过阈值有多久。

## 第 38 章 思考人生

- 英文：Figure 16 is taken from an analysis by Andrew Clark, Ed Diener, and Yannis Georgellis of the German Socio-Economic Panel, in which the same respondents were asked every year about their satisfaction with their life.
  - 原译：图 16 出自安德鲁·克拉克、埃德·迪纳和扬尼斯·乔杰利斯对德国社会经济追踪调查数据所做的一项分析。
  - 现译：图 16 出自安德鲁·克拉克、埃德·迪纳和扬尼斯·乔杰利斯的一项分析，分析的是德国社会经济追踪调查的数据。
  - 处理：Astra 复核通过。“对……数据所做的一项分析”定语过长

- 英文：Others, probably the majority, do not quickly find a response to the exact question they were asked, and automatically make their task easier by substituting the answer to another question.
  - 原译：另一些人，很可能是大多数人，没法很快为别人问的那个确切问题找到答案，于是自动换成另一个问题的答案，让自己的任务变得容易些。
  - 现译：另一些人，很可能是大多数人，一时答不出被问到的那个问题本身，于是自动用另一个问题的答案来替代，让自己的任务变得容易些。
  - 处理：Astra 复核通过。“为……确切问题找到答案”直译 find a response to the exact question

- 英文：Before they began that task, however, he asked them to photocopy a sheet of paper for him.
  - 原译：不过，在他们开始填写之前，他请他们先帮他复印一页纸。
  - 现译：不过，在参与者动笔之前，施瓦茨请他们先帮他复印一页纸。
  - 处理：Astra 复核通过。代词连用“他们……他请他们先帮他”

- 英文：But of course your current mood is not the only thing that comes to mind when you are asked to evaluate your life.
  - 原译：当然，被要求评价自己的生活时，你想到的不只是当下的心情。
  - 现译：当然，有人请你评价自己的生活时，你想到的不只是当下的心情。
  - 处理：Astra 复核通过。被动句“被要求评价”

- 英文：Even newlyweds who are lucky enough to enjoy a state of happy preoccupation with their love will eventually return to earth, and their experienced well-being will again depend, as it does for the rest of us, on the environment and activities of the present moment.
  - 原译：即使是那些足够幸运、能沉浸在爱情的快乐之中的新婚夫妇，最终也会回到现实；他们的体验幸福感会和我们其他人一样，再次取决于当下的环境和正在做的事。
  - 现译：即使是有幸沉浸在爱情的快乐之中的新婚夫妇，最终也会回到现实；他们的体验幸福感会和我们其他人一样，再次取决于当下的环境和正在做的事。
  - 处理：按复核意见修改。“足够幸运、能……”照搬 lucky enough to 复核：“有幸”比“足够幸运、能”自然，但“爱情快乐”压缩过度，应保留“爱情的快乐”这一修饰关系。

- 英文：The details of how the two groups used their time explained the finding.
  - 原译：两组人怎样分配时间的细节，解释了这个发现。
  - 现译：看看两组人各自怎样分配时间，就能解释这个发现。
  - 处理：Astra 复核通过。抽象名词“……的细节”作主语

- 英文：A disposition for well-being is as heritable as height or intelligence, as demonstrated by studies of twins separated at birth.
  - 原译：对出生时就被分开的双胞胎所做的研究表明，感到幸福的倾向，遗传程度和身高或智力相当。
  - 现译：研究出生时就被分开的双胞胎发现，感到幸福的倾向，遗传程度和身高或智力相当。
  - 处理：Astra 复核通过。“对……所做的研究表明”名词化结构

- 英文：The questionnaire they completed twenty years later included measures of their income in 1995, as well as a global measure of life satisfaction.
  - 原译：二十年后，他们填写的问卷里有他们 1995 年收入的数据，还有一项对生活满意度的总体测量。
  - 现译：二十年后他们填写的问卷，既记录了他们 1995 年的收入，也测量了他们的总体生活满意度。
  - 处理：Astra 复核通过。“一项对生活满意度的总体测量”名词化

- 英文：The effect of income on life satisfaction was larger for those who had listed being well-off financially as an essential goal: .57 point on a 5-point scale. The corresponding difference for those who had indicated that money was not important was only .12.
  - 原译：对那些曾把“在经济上非常富裕”列为必不可少的目标的人来说，收入对生活满意度的影响更大：在一个 5 级量表上相差 0.57 分。对那些表示钱不重要的人来说，相应的差别只有 0.12 分。
  - 现译：当初把“在经济上非常富裕”列为必不可少的目标的人，收入对生活满意度的影响更大：在 5 级量表上相差 0.57 分。表示钱不重要的人，相应的差别只有 0.12 分。
  - 处理：Astra 复核通过。两句都用“对那些……的人来说”，照搬 for those who

- 英文：We cannot hold a concept of well-being that ignores what people want.
  - 原译：我们不能持有一种无视人们想要什么的幸福感概念。
  - 现译：我们界定幸福感时，不能忽视人们想要什么。
  - 处理：按复核意见修改。“持有一种……的概念”直译 hold a concept，定语过长 复核：原文谈的是如何界定幸福感，而不是幸福感本身能否“无视”人的愿望。“心目中的幸福感”使概念层面的意思变得含混。

- 英文：We must accept the complexities of a hybrid view, in which the well-being of both selves is considered.
  - 原译：我们必须接受一种混合观点的复杂性，在这种观点里，两个自我的幸福感都要考虑。
  - 现译：我们必须接受一种兼顾两个自我幸福感的混合观点，也接受它带来的复杂性。
  - 处理：Astra 复核通过。照搬 in which 从句“在这种观点里，……都要考虑”

- 英文：The essence of the focusing illusion is WYSIATI, giving too much weight to the climate, too little to all the other determinants of well-being.
  - 原译：聚焦错觉的实质就是所见即全部：给了气候太多的权重，给了决定幸福感的其他所有因素太少的权重。
  - 现译：聚焦错觉的实质就是所见即全部：给气候的权重太大，给决定幸福感的其他所有因素的权重太小。
  - 处理：Astra 复核通过。“给了……太多的权重”直译 giving too much weight

- 英文：When asked about the happiness of Californians, you probably conjure an image of someone attending to a distinctive aspect of the California experience, such as hiking in the summer or admiring the mild winter weather.
  - 原译：被问到加州人有多幸福时，你脑中大概会浮现出这样一幅画面：某个人正在享受加州生活中某个与众不同的方面，比如夏天去远足，或者欣赏温和的冬日天气。
  - 现译：被问到加州人有多幸福时，你脑中大概会浮现出这样一幅画面：某个人正专注于加州生活中某个与众不同的方面，比如夏天去远足，或者欣赏温和的冬日天气。
  - 处理：Astra 复核通过。attending to 写成“享受”，丢了“注意”的意思，和下句“很少把注意力放在”接不上

- 英文：Moreover, long-term Californians are unlikely to be reminded of the climate when asked for a global evaluation of their life.
  - 原译：而且，在加州住了很久的人，被要求对自己的生活作出总体评价时，不太可能想到气候。
  - 现译：而且，在加州住了很久的人，被要求对自己的生活作出总体评价时，不太可能想到气候。
  - 处理：复核后退回原译。被动句“被要求……作出总体评价” 复核：“而且，请……”容易读成向读者发出的请求，削弱了原文“被问及生活总体评价时”的情境关系，中文也比原译别扭。

- 英文：The focusing illusion can cause people to be wrong about their present state of well-being as well as about the happiness of others, and about their own happiness in the future.
  - 原译：聚焦错觉会让人对自己当前的幸福状态作出错误的判断，对别人的幸福，以及对自己将来的幸福，也一样会判断错。
  - 现译：聚焦错觉可能让人误判自己眼下的幸福状态、他人的幸福程度以及自己未来的幸福。
  - 处理：按复核意见修改。虚化动词“作出错误的判断”，后半句照搬 as well as…and about 的结构 复核：“看错幸福”搭配生硬，不如“误判”明确；can cause 的可能性也宜明确保留。

- 英文：Pain and noise are biologically set to be signals that attract attention, and depression involves a self-reinforcing cycle of miserable thoughts.
  - 原译：疼痛和噪声在生物学上就被设定为吸引注意的信号，而抑郁包含一个悲惨念头不断自我强化的循环。
  - 现译：从生物学上说，疼痛和噪声本来就是吸引注意的信号；抑郁则伴随着痛苦念头不断自我强化的循环。
  - 处理：复核后重写。长定语“一个悲惨念头不断自我强化的循环” 复核：“在生物学上就被设定为”“悲惨的念头”仍显生硬；原文强调不断自我强化的是痛苦念头构成的循环，应把这一关系写清楚。

- 英文：Consistent with this idea, recent studies of colostomy patients have produced dramatic inconsistencies between the patients’ experienced well-being and their evaluations of their lives.
  - 原译：和这个看法一致，最近对结肠造口患者的研究发现，患者的体验幸福感和他们对自己生活的评价之间存在惊人的不一致。
  - 现译：和这个看法一致，最近对结肠造口患者的研究发现，患者的体验幸福感和他们对自己生活的评价相差悬殊。
  - 处理：Astra 复核通过。“之间存在……不一致”照搬 inconsistencies between

## 结论

- 英文：Choosing by the quality of the memory may be justified in extreme cases, for example when post-traumatic stress is a possibility, but the cold-hand experience was not traumatic.
  - 原译：在极端情况下，比如有可能出现创伤后应激的时候，按记忆的好坏来做选择也许有道理，但冷手的经历并不具有创伤性。
  - 现译：在极端情况下，比如有可能出现创伤后应激的时候，按记忆的好坏来做选择也许有道理，但冷手实验的那段经历并没有造成创伤。
  - 处理：Astra 复核通过。“并不具有创伤性”是英文形容词的直译

- 英文：The remembering self is a construction of System 2. However, the distinctive features of the way it evaluates episodes and lives are characteristics of our memory.
  - 原译：记忆自我是系统 2 的一种建构。不过，它评价一段段经历和整个人生的方式有一些独特之处，而这些特点属于我们的记忆。
  - 现译：记忆自我是系统 2 建构出来的。不过，它评价一段段经历和整个人生的方式有一些独特之处，这些都是我们记忆的特点。
  - 处理：Astra 复核通过。“一种建构”“属于我们的记忆”照搬英文名词结构

- 英文：The rules that govern the evaluation of the past are poor guides for decision making, because time does matter. The central fact of our existence is that time is the ultimate finite resource, but the remembering self ignores that reality.
  - 原译：支配我们评价过去的那些规则，用来指导决策并不可靠，因为时间确实重要。我们生存的核心事实是：时间是终极的有限资源，但记忆自我无视这个现实。
  - 现译：我们评价过去时遵循的那些规则，拿来指导决策并不可靠，因为时间确实重要。人生最核心的事实是：时间是最根本的有限资源，记忆自我却无视这个现实。
  - 处理：复核后重写。“支配”直译 govern，“我们生存的核心事实”照搬英文 复核：“时间是终极的有限资源”仍然生硬，未清楚表达时间作为资源的根本性和有限性。

- 英文：The mirror image of the same bias makes us fear a short period of intense but tolerable suffering more than we fear a much longer period of moderate pain.
  - 原译：同一种偏差的镜像，让我们害怕短时间的剧烈但尚可忍受的痛苦，胜过害怕长得多的中等程度的疼痛。
  - 现译：同一种偏差反过来，又让我们觉得，一段短暂、剧烈但尚可忍受的痛苦，比一段长得多的中度疼痛更可怕。
  - 处理：Astra 复核通过。“偏差的镜像”作主语，“的”字定语堆叠

- 英文：The advice sounds wise because anticipated regret is the verdict of the remembering self and we are inclined to accept such judgments as final and conclusive.
  - 原译：这个建议听起来很明智，因为预期的后悔是记忆自我的裁决，而我们倾向于把这类判断当作最终的定论。
  - 现译：这个建议听起来很明智，因为预期的后悔是记忆自我的裁决，而我们又容易把这类判断当作最终的定论。
  - 处理：Astra 复核通过。“倾向于”直译 are inclined to

- 英文：For example, an hour spent practicing the violin may enhance the experience of many hours of playing or listening to music years later.
  - 原译：例如，花一小时练小提琴，可能会让多年以后许多个小时的演奏或听音乐的体验变得更好。
  - 现译：例如，花一小时练小提琴，可能会让人在多年以后演奏或听音乐的许多个小时里，都有更好的体验。
  - 处理：Astra 复核通过。前置定语太长，“的”字连串

- 英文：The statements “I will always remember…” or “this is a meaningful moment” should be taken as promises or predictions, which can be false—and often are—even when uttered with complete sincerity.
  - 原译：“我会永远记得……”或者“这是一个有意义的时刻”这样的话，应该当作承诺或预测来看待；它们可能落空，而且常常落空，哪怕说的人完全真诚。
  - 现译：“我会永远记得……”或者“这一刻很有意义”这样的话，应该当作承诺或预测来看待；它们可能落空，而且常常落空，哪怕说的人完全真诚。
  - 处理：Astra 复核通过。引语“这是一个有意义的时刻”不像人说出口的话

- 英文：The logic of duration weighting is compelling, but it cannot be considered a complete theory of well-being because individuals identify with their remembering self and care about their story. A theory of well-being that ignores what people want cannot be sustained. On the other hand, a theory that ignores what actually happens in people’s lives and focuses exclusively on what they think about their life is not tenable either.
  - 原译：按时长加权的逻辑很有说服力，但它不能算是一套完整的幸福理论，因为每个人都认同自己的记忆自我，在乎自己的故事。一种不管人们想要什么的幸福理论，是维持不下去的。另一方面，一种不管人们生活中实际发生了什么、只关注他们怎样看待自己生活的理论，也同样站不住脚。
  - 现译：按时长加权的逻辑很有说服力，但它不能算是一套完整的幸福理论，因为人们把记忆自我当成自己，也在乎自己的故事。幸福理论如果不考虑人们想要什么，就无法成立。另一方面，如果一种理论不考虑人们生活中实际发生了什么，只关注他们怎样看待自己的生活，也同样站不住脚。
  - 处理：按复核意见修改。“认同”直译 identify with；“一种……的理论”长定语 复核：理论“维持不下去”仍是生硬直译。cannot be sustained 在这里指理论无法成立，而不是无法维持运转。

- 英文：In everyday speech, we call people reasonable if it is possible to reason with them, if their beliefs are generally in tune with reality, and if their preferences are in line with their interests and their values.
  - 原译：在日常说法里，如果可以跟一个人讲道理，他的信念大体符合现实，他的偏好和他的利益与价值观相一致，我们就说他是通情达理的（reasonable）。
  - 现译：在日常说法里，如果可以跟一个人讲道理，他的信念大体符合现实，偏好也和自己的利益与价值观相一致，我们就说他是通情达理的（reasonable）。
  - 处理：Astra 复核通过。多余代词“他的……他的……”

- 英文：The only test of rationality is not whether a person’s beliefs and preferences are reasonable, but whether they are internally consistent.
  - 原译：检验理性的唯一标准，是一个人的信念和偏好在内部是否一致，至于它们是否通情达理，并不在考虑之列。
  - 现译：检验理性的唯一标准，是一个人的信念和偏好在内部是否一致，至于它们是否通情达理，并不在考虑之列。
  - 处理：复核后退回原译。“在内部是否一致”直译 internally consistent 复核：internally consistent 指信念和偏好体系内部的逻辑自洽，包括各个信念之间、各个偏好之间的一致性。“信念和偏好彼此是否一致”容易被理解成只检验信念与偏好这两者是否相符，改变了判准。

- 英文：As interpreted by the important Chicago school of economics, faith in human rationality is closely linked to an ideology in which it is unnecessary and even immoral to protect people against their choices.
  - 原译：在举足轻重的芝加哥经济学派的解读中，对人类理性的信心和一种意识形态紧密相连：按照这种意识形态，保护人们免受自己选择的伤害是不必要的，甚至是不道德的。
  - 现译：在举足轻重的芝加哥经济学派的解读中，对人类理性的信心和一种意识形态紧密相连：按照这种意识形态，保护人们免受自己选择的伤害是不必要的，甚至是不道德的。
  - 处理：复核后退回原译。“在……的解读中”照搬 As interpreted by 复核：原文描述的是芝加哥学派所阐释的人类理性信念与意识形态之间的联系。“在……看来”把整项判断归给了该学派，变成该学派自己认为这种信念与意识形态紧密相连，改变了观点的归属。

- 英文：He was making a valuable point: when we observe people acting in ways that seem odd, we should first examine the possibility that they have a good reason to do what they do. Psychological interpretations should only be invoked when the reasons become implausible—which Becker’s explanation of obesity probably is.
  - 原译：他说出了很有价值的一点：当我们看到人们的行为显得古怪时，应该先考察一下，他们这样做是否有充分的理由。只有当这些理由变得难以置信时，才应该求助于心理学的解释，而贝克尔对肥胖的解释大概就难以置信。
  - 现译：他说出了很有价值的一点：看到人们的行为显得古怪，我们应该先考虑他们这样做有没有充分的理由。只有当这些理由变得难以置信时，才应该拿心理学来解释，而贝克尔对肥胖的解释大概就难以置信。
  - 处理：Astra 复核通过。“当……时”套式，“求助于”直译 invoked

- 英文：Citizens know what they are doing, even when they choose not to save for their old age, or when they expose themselves to addictive substances.
  - 原译：公民知道自己在做什么，即使他们选择不为养老存钱，或者让自己接触会成瘾的东西，也是如此。
  - 现译：公民知道自己在做什么，即使他们选择不为养老存钱，或者接触会让人成瘾的物质，也是如此。
  - 处理：按复核意见修改。“让自己接触”直译 expose themselves to 复核：addictive substances 明确指成瘾性物质；“会让人上瘾的东西”范围过宽，也可能包括活动或行为。

- 英文：No behavioral economist favors a state that will force its citizens to eat a balanced diet and to watch only television programs that are good for the soul.
  - 原译：没有哪位行为经济学家赞成国家强迫公民吃均衡的饮食、只看对心灵有益的电视节目。
  - 现译：没有哪位行为经济学家赞成国家强迫公民吃得营养均衡、只看对心灵有益的电视节目。
  - 处理：复核后重写。“吃均衡的饮食”搭配重复、生硬 复核：“强迫公民饮食均衡”搭配仍不自然，宜补出“保持”等动作。

- 英文：The default option is naturally perceived as the normal choice.
  - 原译：默认选项自然而然地被看作正常的选择。
  - 现译：人们自然而然地把默认选项看作正常的选择。
  - 处理：Astra 复核通过。不必要的“被”字句

- 英文：A remarkable feature of libertarian paternalism is its appeal across a broad political spectrum. The flagship example of behavioral policy, called Save More Tomorrow, was sponsored in Congress by an unusual coalition that included extreme conservatives as well as liberals.
  - 原译：自由意志家长制有一个引人注目的特点：它在很宽的政治光谱上都有吸引力。行为政策的旗舰范例叫作“明天多储蓄”计划（Save More Tomorrow），它在国会由一个不同寻常的联盟共同推动，其中既有极端保守派，也有自由派。
  - 现译：自由意志家长制有一个引人注目的特点：它吸引了政治立场各不相同的人。行为政策最具代表性的例子是“明天多储蓄”计划（Save More Tomorrow），在国会推动它的是一个不同寻常的联盟，其中既有极端保守派，也有自由派。
  - 处理：按复核意见修改。“在很宽的政治光谱上”直译，“由……推动”照搬被动 复核：“政治立场差别很大的人，都觉得”容易扩大为全称判断；原文只说其吸引力覆盖广泛的政治立场。“旗舰范例”也仍显生硬。

- 英文：Those who sign on allow the employer to increase their contribution to their saving plan by a fixed proportion whenever they receive a raise.
  - 原译：签约参加的员工允许雇主在他们每次加薪时，按固定比例提高他们在储蓄计划中的缴存额。
  - 现译：员工签约参加后，每逢加薪，雇主就可以按固定比例提高他们在储蓄计划中的缴存额。
  - 处理：Astra 复核通过。照搬英文句式，代词“他们”重复

- 英文：It is soundly based in the psychological principles that readers of this book will recognize.
  - 原译：它牢牢建立在本书读者一看就能认出的心理学原理之上。
  - 现译：它有扎实的心理学依据，用到的都是本书读者熟悉的原理。
  - 处理：复核后重写。“建立在……之上”中间夹着长定语 复核：拆句后“认得出来”的对象不够明确，可能被理解成看出这项创新具有心理学依据，而不是认出所用的心理学原理。“一看就”也增加了原文没有明确表达的即时性。

- 英文：The appeal of libertarian paternalism has been recognized in many countries, including the UK and South Korea, and by politicians of many stripes, including Tories and the Democratic administration of President Obama.
  - 原译：自由意志家长制的吸引力已经得到许多国家的认可，包括英国和韩国，也得到各个派别的政治人物的认可，包括英国保守党人和奥巴马总统领导的民主党政府。
  - 现译：自由意志家长制的吸引力，已经得到英国、韩国等许多国家的认可，也得到各派政治人物的认可，其中有英国保守党人，也有奥巴马总统领导的民主党政府。
  - 处理：Astra 复核通过。两个后置的“包括”照搬 including

- 英文：The official name for this group is the Behavioural Insight Team, but it is known both in and out of government simply as the Nudge Unit.
  - 原译：这个小组的正式名称是“行为洞察小组”（Behavioural Insight Team），但无论在政府内外，大家都简单地称它为“助推小组”（Nudge Unit）。
  - 现译：这个小组的正式名称是“行为洞察小组”（Behavioural Insight Team），但无论在政府内外，大家都干脆叫它“助推小组”（Nudge Unit）。
  - 处理：Astra 复核通过。“简单地称它为”直译 simply

- 英文：The mission is described in the 2010 Report of the Office of Management and Budget.
  - 原译：这项任务在白宫管理和预算办公室 2010 年的报告中有所描述。
  - 现译：白宫管理和预算办公室 2010 年的报告描述了这项任务。
  - 处理：Astra 复核通过。“在……中有所描述”照搬被动句

- 英文：They will also recognize background statements such as “presentation greatly matters; if, for example, a potential outcome is framed as a loss, it may have more impact than if it is presented as a gain.”
  - 原译：他们也会认出报告里的一些背景陈述，比如“呈现方式非常重要；例如，如果把一个可能的结果表述为损失，它的影响可能会比表述为收益时更大”。
  - 现译：他们也会认出报告里一些交代背景的说法，比如“呈现方式非常重要；例如，如果把一个可能的结果表述为损失，它的影响可能会比表述为收益时更大”。
  - 处理：Astra 复核通过。“背景陈述”直译 background statements

- 英文：Additional applications that have been implemented include automatic enrollment in health insurance, a new version of the dietary guidelines that replaces the incomprehensible Food Pyramid with the powerful image of a Food Plate loaded with a balanced diet, and a rule formulated by the USDA that permits the inclusion of messages such as “90% fat-free” on the label of meat products, provided that the statement “10% fat” is also displayed “contiguous to, in lettering of the same color, size, and type as, and on the same color background as, the statement of lean percentage.”
  - 原译：已经实施的其他应用还包括：自动加入医疗保险；新版膳食指南，用一个盛满均衡膳食的“食物餐盘”这个有力的形象，取代了让人看不懂的“食物金字塔”；还有美国农业部制定的一项规定，允许在肉类产品的标签上印“90% 无脂”这样的信息，前提是同时标出“含 10% 脂肪”的说明，而且要“紧挨着瘦肉百分比的说明，字体的颜色、大小和字形与之相同，背景颜色也与之相同”。
  - 现译：已经实施的其他应用还包括：自动加入医疗保险；新版膳食指南，用“食物餐盘”这个有力的形象取代了让人看不懂的“食物金字塔”，餐盘里盛满了均衡的膳食；还有美国农业部制定的一项规定，允许在肉类产品的标签上印“90% 无脂”这样的信息，前提是同时标出“含 10% 脂肪”的说明，而且要“紧挨着瘦肉百分比的说明，字体的颜色、大小和字形与之相同，背景颜色也与之相同”。
  - 处理：Astra 复核通过。“一个……的‘食物餐盘’这个……形象”定语叠在一起

- 英文：And “System 2 is mobilized to do Y” is a shortcut for “arousal increases, pupils dilate, attention is focused, and activity Y is performed.” I hope you find the language of systems as helpful as I do, and that you have acquired an intuitive sense of how they work without getting confused by the question of whether they exist.
  - 原译：“系统 2 被调动起来做 Y”则是“唤醒水平升高，瞳孔放大，注意力集中，Y 这项活动得以进行”的简便说法。我希望你和我一样，觉得用系统来讲很有帮助；也希望你已经对它们怎样运作有了直觉上的把握，不会被“它们是否存在”这个问题弄糊涂。
  - 现译：“系统 2 被调动起来做 Y”则是“唤醒水平升高，瞳孔放大，注意力集中，执行 Y 这项活动”的简便说法。我希望你和我一样，觉得“系统”这套说法很有帮助；也希望你已经对它们怎样运作有了直觉上的把握，不会被“它们是否存在”这个问题弄糊涂。
  - 处理：Astra 复核通过。“得以进行”是虚化表达，“用系统来讲”说不清指什么

- 英文：The investment of attention improves performance in numerous activities—think of the risks of driving through a narrow space while your mind is wandering—and is essential to some tasks, including comparison, choice, and ordered reasoning.
  - 原译：投入注意力能提高许多活动的表现（想想你心不在焉地把车开过一个狭窄的地方有多危险），而对于有些任务，包括比较、选择和有条理的推理，投入注意力是必不可少的。
  - 现译：投入注意力能让人在许多活动中表现得更好（想想你心不在焉地把车开过一个狭窄的地方有多危险），而有些任务，包括比较、选择和有条理的推理，离不开注意力的投入。
  - 处理：复核后重写。“对于……来说”式的介词结构 复核：“提高许多活动的表现”搭配不当。原文指改善人在这些活动中的表现，不是活动本身的表现。

- 英文：I have spent more time describing System 1, and have devoted many pages to errors of intuitive judgment and choice that I attribute to it.
  - 原译：我花了更多的时间描述系统 1，用了许多篇幅讨论我认为由它造成的直觉判断与选择上的错误。
  - 现译：我花了更多的时间描述系统 1，用了许多篇幅讨论直觉判断与选择上的错误，我认为这些错误是它造成的。
  - 处理：Astra 复核通过。宾语前的定语太长

- 英文：System 1 is indeed the origin of much that we do wrong, but it is also the origin of most of what we do right—which is most of what we do.
  - 原译：我们做错的许多事情，确实源于系统 1，但我们做对的大多数事情也源于它，而做对的事占了我们所做之事的大部分。
  - 现译：我们做错的许多事情，确实源于系统 1，但我们做对的大多数事情也源于它，而我们做的事大多是做对了的。
  - 处理：Astra 复核通过。“占了我们所做之事的大部分”生硬

- 英文：The acquisition of skills requires a regular environment, an adequate opportunity to practice, and rapid and unequivocal feedback about the correctness of thoughts and actions.
  - 原译：习得技能需要一个有规律的环境、足够的练习机会，以及关于想法和行动是否正确的快速而明确的反馈。
  - 现译：习得技能需要一个有规律的环境和足够的练习机会，还需要快速而明确的反馈，让人知道自己的想法和行动对不对。
  - 处理：Astra 复核通过。“关于……的……反馈”长定语

- 英文：Intuitive answers come to mind quickly and confidently, whether they originate from skills or from heuristics.
  - 原译：直觉的答案总是迅速而自信地浮现在脑海里，无论它们来自技能还是来自启发式。
  - 现译：直觉的答案，无论来自技能还是来自启发式，都会迅速浮现在脑海里，让人觉得很有把握。
  - 处理：复核后重写。让步从句照搬英文放在句末 复核：“答案……自信地浮现”仍是生硬的修饰语照搬。confidently 指人想到答案时对它的确信，不是答案自身具有自信。

- 英文：Many suggestions of System 1 are casually endorsed with minimal checking, as in the bat-and-ball problem.
  - 原译：系统 1 的许多建议，只经过最低限度的检查，就被随随便便地认可了，就像在球拍和球问题中那样。
  - 现译：系统 1 的许多建议，只稍加检查，就被随随便便地认可了，就像在球拍和球问题中那样。
  - 处理：Astra 复核通过。“最低限度的检查”直译 minimal checking

- 英文：How can we improve judgments and decisions, both our own and those of the institutions that we serve and that serve us?
  - 原译：我们怎样才能改进判断和决策，包括我们自己的，也包括我们服务的机构和为我们服务的机构的？
  - 现译：我们自己的判断和决策，以及我们服务的机构和为我们服务的机构所做的判断和决策，怎样才能改进？
  - 处理：Astra 复核通过。照搬 both...and 后置结构，句末“的？”悬空

- 英文：As I know from experience, System 1 is not readily educable.
  - 原译：我从自己的经验知道，系统 1 不容易教会。
  - 现译：亲身经验告诉我，系统 1 并不容易教好。
  - 处理：按复核意见修改。“我从自己的经验知道”照搬 As I know from experience 复核：“系统 1 不容易教会”搭配仍显生硬；这里泛指系统 1 不易受教，并不是说某项具体内容不容易教会。

- 英文：The way to block errors that originate in System 1 is simple in principle: recognize the signs that you are in a cognitive minefield, slow down, and ask for reinforcement from System 2.
  - 原译：要阻止源自系统 1 的错误，方法在原则上很简单：认出你正身处认知雷区的迹象，放慢速度，请系统 2 来增援。
  - 现译：要阻止源自系统 1 的错误，方法在原则上很简单：一旦察觉有迹象表明你正身处认知雷区，就放慢速度，请系统 2 来增援。
  - 处理：复核后重写。“认出……的迹象”宾语前定语过长 复核：“从迹象中认出你正身处……”搭配不自然。“认出”不宜直接接这一判断，应明确表达察觉到提示自己身处认知雷区的迹象。

- 英文：When you see lines with fins pointing in different directions, you will recognize the situation as one in which you should not trust your impressions of length. Unfortunately, this sensible procedure is least likely to be applied when it is needed most.
  - 原译：当你看到一些线段两端的短斜线朝向各不相同时，你会认出，在这种情境下，你不应该相信自己对长度的印象。遗憾的是，这个明智的程序恰恰在最需要它的时候最不可能被用上。
  - 现译：看到一些线段两端的短斜线朝向各不相同，你就会认出这种情境，知道此时不应该相信自己对长度的印象。遗憾的是，这个明智的做法恰恰在最需要它的时候最不可能被用上。
  - 处理：Astra 复核通过。“当……时”套式、“你”重复，“程序”直译 procedure

- 英文：More doubt is the last thing you want when you are in trouble.
  - 原译：在你遇到麻烦的时候，你最不想要的就是更多的怀疑。
  - 现译：遇到麻烦的时候，你最不想要的就是更多的怀疑。
  - 处理：Astra 复核通过。“在你……的时候，你”多余代词

- 英文：An organization that seeks to improve its decision product should routinely look for efficiency improvements at each of these stages.
  - 原译：一个想改进决策这种产品的组织，应该例行地在每个阶段寻找提高效率的办法。
  - 现译：组织如果想改进决策这种产品，就应该把在每个阶段寻找提高效率的办法当作例行工作。
  - 处理：Astra 复核通过。“一个……的组织”长定语，“例行地”生硬

- 英文：Constant quality control is an alternative to the wholesale reviews of processes that organizations commonly undertake in the wake of disasters.
  - 原译：持续的质量控制，可以替代组织通常在灾难之后才进行的全面流程审查。
  - 现译：组织通常会在灾难过后对流程做全面审查，持续的质量控制可以替代这种做法。
  - 处理：按复核意见修改。宾语前定语过长，“进行”虚化动词 复核：原文说组织通常在灾难后开展全面流程审查，没有“通常要等到灾难发生后才开展”的限定；“才”增加了这一层意思。

- 英文：Similarly, labels such as “anchoring effects,” “narrow framing,” or “excessive coherence” bring together in memory everything we know about a bias, its causes, its effects, and what can be done about it.
  - 原译：同样，“锚定效应”“窄框架”或“过度一致性”这样的名称，会把我们知道的关于一种偏差的一切，包括它的成因、它的影响以及应对它的办法，在记忆中汇集到一起。
  - 现译：同样，“锚定效应”“窄框架”或“过度一致性”这样的名称，会在记忆中把我们对一种偏差的了解全部汇集起来，包括它的成因、它的影响，以及可以怎样应对它。
  - 处理：Astra 复核通过。“把……的一切，包括……，在记忆中汇集”中间插入太长

## 附录 A 不确定条件下的判断：启发式与偏差

- 英文：The research was supported by the Advanced Research Projects Agency of the Department of Defense and was monitored by the Office of Naval Research under contract N00014-73-C-0438 to the Oregon Research Institute, Eugene.
  - 原译：这项研究由美国国防部高级研究计划局资助，由海军研究办公室根据与尤金市俄勒冈研究所签订的 N00014-73-C-0438 号合同进行监管。
  - 现译：这项研究由美国国防部高级研究计划局资助，由海军研究办公室根据与尤金市俄勒冈研究所签订的 N00014-73-C-0438 号合同监管。
  - 处理：Astra 复核通过。虚化动词“进行”

- 英文：These judgments are all based on data of limited validity, which are processed according to heuristic rules.
  - 原译：这些判断都基于有效性有限的数据，并按照启发式规则来处理这些数据。
  - 现译：这些判断依据的都是有效性有限的数据，人们按照启发式规则来处理这些数据。
  - 处理：Astra 复核通过。主语错位，读成“判断”在处理数据

- 英文：For an illustration of judgment by representativeness, consider an individual who has been described by a former neighbor as follows:
  - 原译：为了说明怎样根据代表性作判断，设想有这样一个人，他以前的一位邻居这样描述他：
  - 现译：为了说明怎样根据代表性作判断，设想某人以前的一位邻居这样描述他：
  - 处理：Astra 复核通过。照搬定语从句“一个人，他……”

- 英文：In the representativeness heuristic, the probability that Steve is a librarian, for example, is assessed by the degree to which he is representative of, or similar to, the stereotype of a librarian.
  - 原译：按照代表性启发式，史蒂夫是图书管理员的概率，是根据他在多大程度上代表图书管理员的刻板印象，或者说与这种刻板印象有多相似，来评估的。
  - 现译：例如，按照代表性启发式，人们评估史蒂夫是图书管理员的概率时，看的是他在多大程度上符合图书管理员的刻板印象，或者说与这种刻板印象有多相似。
  - 处理：复核后重写。被动句拆成“是……来评估的”，还漏了 for example 复核：“代表图书管理员的刻板印象”仍然生硬；这里指符合这种刻板印象，而不是代表一种印象。

- 英文：Subjects were shown brief personality descriptions of several individuals, allegedly sampled at random from a group of 100 professionals—engineers and lawyers.
  - 原译：被试看到了几个人的简短性格描述，据称这些人是从一个由 100 名专业人士（工程师和律师）组成的群体中随机抽取的。
  - 现译：被试看到了几个人的简短性格描述，据称这些人是从 100 名专业人士（工程师和律师）中随机抽取的。
  - 处理：Astra 复核通过。“从一个由……组成的群体中”长定语

- 英文：In one experimental condition, subjects were told that the group from which the descriptions had been drawn consisted of 70 engineers and 30 lawyers.
  - 原译：在一种实验条件下，研究者告诉被试，这些描述取自一个由 70 名工程师和 30 名律师组成的群体。
  - 现译：在一种实验条件下，研究者告诉被试，这些描述取自一个由 70 名工程师和 30 名律师组成的群体。
  - 处理：复核后退回原译。“一个由……组成的群体”长定语 复核：“抽取这些描述的群体”把群体写成了抽取行为的施事；原文指这些描述所取自的群体。原译的来源关系更准确。

- 英文：This description was intended to convey no information relevant to the question of whether Dick is an engineer or a lawyer.
  - 原译：这份描述的本意是不传达任何有助于判断迪克是工程师还是律师的信息。
  - 现译：研究者编写这份描述时，有意让它不提供任何有助于判断迪克是工程师还是律师的信息。
  - 处理：复核后重写。“本意是不传达”生硬 复核：原文明确说明设计意图是不提供与职业判断相关的信息；改写把它拆成“特意编写”和“不提供信息”的事实陈述，没有准确保留意图所指。

- 英文：When no specific evidence is given, prior probabilities are properly utilized; when worthless evidence is given, prior probabilities are ignored.
  - 原译：没有给出具体证据时，先验概率得到了恰当的利用；给出毫无价值的证据时，先验概率就被忽视了。
  - 现译：没有给出具体证据时，人们会恰当地利用先验概率；给出毫无价值的证据时，人们就会忽视先验概率。
  - 处理：Astra 复核通过。“得到了……利用”和被动句

- 英文：This fundamental notion of statistics is evidently not part of people’s repertoire of intuitions.
  - 原译：统计学的这个基本概念，显然不在人们的直觉储备之中。
  - 现译：人们的直觉里显然没有统计学的这个基本概念。
  - 处理：Astra 复核通过。repertoire 直译为“直觉储备”

- 英文：A similar insensitivity to sample size has been reported in judgments of posterior probability, that is, of the probability that a sample has been drawn from one population rather than from another.
  - 原译：在对后验概率的判断中，也有研究报告了类似的对样本量不敏感的现象。
  - 现译：也有研究报告，人们判断后验概率时，同样对样本量不敏感。
  - 处理：Astra 复核通过。抽象名词串和“的”字连用

- 英文：Thus, people expect that the essential characteristics of the process will be represented, not only globally in the entire sequence, but also locally in each of its parts.
  - 原译：由此可见，人们期望过程的基本特征不仅在整个序列中得到整体的体现，也在序列的每个局部得到体现。
  - 现译：由此可见，人们期望这个过程的基本特征不仅体现在序列整体上，也体现在每个局部。
  - 处理：按复核意见修改。“得到……体现”虚化结构 复核：“在整个序列上整体地体现出来”重复且生硬，改写未解决整体与局部的表达问题。

- 英文：A study of the statistical intuitions of experienced research psychologists[^8] revealed a lingering belief in what may be called the “law of small numbers,” according to which even small samples are highly representative of the populations from which they are drawn.
  - 原译：一项针对资深研究心理学家统计直觉的研究[^8]发现，他们心中始终残留着一种信念，可以称之为“小数定律”：即使是小样本，也高度代表它们所取自的总体。
  - 现译：有一项研究[^8]考察了资深研究心理学家的统计直觉，发现他们心中始终残留着一种信念，可以称之为“小数定律”：即使是从总体中抽取的小样本，也高度代表这个总体。
  - 处理：复核后重写。名词前长定语，“所取自的”照搬 from which 复核：“抽取它们的总体”把总体写成了抽取样本的施事；原文指样本所取自的总体。原译准确保留了这一关系。

- 英文：In the actual conduct of research, this bias leads to the selection of samples of inadequate size and to overinterpretation of findings.
  - 原译：在实际开展研究时，这种偏差会导致选用的样本量不足，并对研究发现作出过度解读。
  - 现译：在实际开展研究时，这种偏差会使研究者选用过小的样本，并过度解读研究发现。
  - 处理：按复核意见修改。“作出过度解读”虚化动词，缺主语 复核：“让研究者选用的样本量不足”仍以样本量为后续小句的主语，接“对研究发现解读过度”时又暗换成研究者，并未真正解决主语问题。

- 英文：For example, suppose one is given a description of a company and is asked to predict its future profit.
  - 原译：例如，假设有人拿到一份对某家公司的描述，并被要求预测它未来的利润。
  - 现译：例如，假设给一个人一份有关某家公司的描述，请他预测这家公司未来的利润。
  - 处理：按复核意见修改。“被要求”被动句 复核：“有人拿到……，要他……”中，拿到描述的人与提出要求的人没有衔接清楚。

- 英文：This mode of judgment violates the normative statistical theory in which the extremeness and the range of predictions are controlled by considerations of predictability.
  - 原译：按照这种理论，预测的极端程度和范围，应该由对可预测性的考虑来控制。
  - 现译：按照这种理论，预测的极端程度和范围应根据可预测性来确定。
  - 处理：按复核意见修改。“由……来控制”被动直译，另加了原文没有的“应该” 复核：这里说明规范性理论对预测的要求，“应该”并非无依据的增译；“取决于对……的考虑”仍然抽象生硬，也淡化了规范含义。

- 英文：As we have seen, people often predict by selecting the outcome (for example, an occupation) that is most representative of the input (for example, the description of a person).
  - 原译：我们已经看到，人们常常通过挑选最能代表输入信息（例如对一个人的描述）的结果（例如一种职业）来作预测。
  - 现译：我们已经看到，人们作预测时，常常挑选最能代表输入信息（例如对一个人的描述）的那个结果（例如一种职业）。
  - 处理：Astra 复核通过。“通过……来作预测”中间夹长定语

- 英文：The unwarranted confidence which is produced by a good fit between the predicted outcome and the input information may be called the illusion of validity.
  - 原译：预测结果与输入信息之间的良好契合所产生的这种没有根据的信心，可以称为有效性错觉。
  - 现译：因预测结果与输入信息十分契合而产生的那种没有根据的信心，可以称为有效性错觉。
  - 处理：按复核意见修改。抽象名词作主语，定语过长 复核：原文是在界定由良好契合产生的那种无根据信心；拆句后容易读成良好契合都会导致无根据信心，扩大了断言范围。

- 英文：However, an elementary result in the statistics of correlation asserts that, given input variables of stated validity, a prediction based on several such inputs can achieve higher accuracy when they are independent of each other than when they are redundant or correlated.
  - 原译：然而，相关分析中的一个基本结论指出，在各输入变量的有效性已定的情况下，基于几个这样的输入作出的预测，在这些输入彼此独立时能达到的准确度，要高于它们冗余或相关时。
  - 现译：然而，相关分析中有一个基本结论：如果各输入变量的有效性已经给定，那么根据几个这样的输入作预测，输入彼此独立时能达到的准确度，要高于输入冗余或相关时。
  - 处理：Astra 复核通过。“结论指出”“在……的情况下”和长定语层层叠套

- 英文：These observations illustrate a general phenomenon known as regression toward the mean, which was first documented by Galton more than 100 years ago.
  - 原译：这些观察说明了一个普遍现象，叫作均值回归，它在 100 多年前由高尔顿首先记录下来。
  - 现译：这些观察说明了一个普遍现象，叫作均值回归，100 多年前高尔顿首先记录了这种现象。
  - 处理：Astra 复核通过。“它……由……记录下来”照搬被动和代词

- 英文：In social interaction, as well as in training, rewards are typically administered when performance is good, and punishments are typically administered when performance is poor.
  - 原译：在社会交往中，和在训练中一样，奖励通常在表现好时给予，惩罚通常在表现差时给予。
  - 现译：无论在社会交往中还是在训练中，人们通常在对方表现好时给予奖励，在对方表现差时给予惩罚。
  - 处理：按复核意见修改。as well as 插入语照搬 复核：语序有所改善，但“给出奖励”“给出惩罚”搭配生硬，仍保留了不必要的被动结构。

- 英文：In fact, the elusive role of regression in determining the apparent consequences of reward and punishment seems to have escaped the notice of students of this area.
  - 原译：事实上，回归在决定奖励和惩罚的表面后果时所起的这种难以察觉的作用，似乎连这个领域的研究者都没有注意到。
  - 现译：事实上，奖励和惩罚表面上带来什么后果，回归在其中起着作用，但这种作用很难察觉，似乎连这个领域的研究者都没有注意到。
  - 处理：Astra 复核通过。“所起的这种……作用”长定语抽象主语

- 英文：Availability is a useful clue for assessing frequency or probability, because instances of large classes are usually recalled better and faster than instances of less frequent classes. However, availability is affected by factors other than frequency and probability.
  - 原译：可得性是评估频率或概率的一条有用线索，因为大类别的实例通常比频率较低的类别的实例回忆得更好、更快。然而，可得性还受到频率和概率以外的因素的影响。
  - 现译：可得性是评估频率或概率的一条有用线索，因为大类别的实例通常比频率较低的类别中的实例回忆得更好、更快。然而，影响可得性的还有频率和概率以外的因素。
  - 处理：复核后重写。“的类别的实例”“的因素的影响”的字连串 复核：比较对象错位：改写把“大类别的实例”与“频率较低的类别”相比；原文比较的是两类实例的回忆情况，不能删去比较基准中的“实例”。

- 英文：When the size of a class is judged by the availability of its instances, a class whose instances are easily retrieved will appear more numerous than a class of equal frequency whose instances are less retrievable.
  - 原译：当一个类别的大小根据其实例的可得性来判断时，实例容易提取的类别，会显得比频率相同但实例较难提取的类别数量更多。
  - 现译：如果根据实例的可得性来判断一个类别的大小，那么实例容易提取的类别，会显得比频率相同但实例较难提取的类别数量更多。
  - 处理：Astra 复核通过。“当……来判断时”被动直译

- 英文：In an elementary demonstration of this effect, subjects heard a list of well-known personalities of both sexes and were subsequently asked to judge whether the list contained more names of men than of women.
  - 原译：在演示这种效应的一个简单实验中，被试听了一份由男女知名人士组成的名单，随后要判断名单里男性的名字是否比女性多。
  - 现译：在演示这种效应的一个简单实验中，被试听了一份男女知名人士的名单，随后要判断名单里男性的名字是否比女性多。
  - 处理：Astra 复核通过。“由……组成的”冗长定语

- 英文：It is a common experience that the subjective probability of traffic accidents rises temporarily when one sees a car overturned by the side of the road.
  - 原译：一个常见的经验是，看到一辆车翻倒在路边时，人们对交通事故的主观概率会暂时上升。
  - 现译：很多人都有这样的经验：看到一辆车翻倒在路边，交通事故发生的主观概率就会暂时上升。
  - 处理：按复核意见修改。It is a common experience that 直译 复核：“对交通事故的主观概率”搭配不成立；应明确上升的是交通事故发生的主观概率。

- 英文：People approach this problem by recalling words that begin with r (road) and words that have r in the third position (car) and assess the relative frequency by the ease with which words of the two types come to mind.
  - 原译：人们处理这个问题的方式，是回想以 r 开头的单词（如 road）和第三个字母是 r 的单词（如 car），并根据这两类单词想起来的难易程度来评估它们的相对频率。
  - 现译：人们会这样处理这个问题：回想以 r 开头的单词（如 road）和第三个字母是 r 的单词（如 car），再根据这两类单词想起来的难易程度来评估它们的相对频率。
  - 处理：Astra 复核通过。“……的方式，是……”名词化句式

- 英文：They do so even for consonants, such as r or k, that are more frequent in the third position than in the first.
  - 原译：即使对于像 r 或 k 这样出现在第三位比出现在首位更频繁的辅音字母，他们也会这样判断。
  - 现译：有些辅音字母，比如 r 或 k，出现在第三位比出现在首位更频繁，人们对它们也会这样判断。
  - 处理：Astra 复核通过。“对于像……这样……的”长定语

- 英文：If the frequency of words is judged by the availability of the contexts in which they appear, abstract words will be judged as relatively more numerous than concrete words.
  - 原译：如果根据单词出现的语境的可得性来判断单词的频率，抽象词就会被判断为比具体词相对更多。
  - 现译：如果根据单词所在语境的可得性来判断单词的频率，人们就会认为抽象词比具体词出现得更频繁。
  - 处理：按复核意见修改。“的语境的”连用和“被判断为” 复核：“比具体词相对更多”搭配生硬，也容易被理解成词的种类更多；结合上下文，这里比较的是出现频率。

- 英文：The risk involved in an adventurous expedition, for example, is evaluated by imagining contingencies with which the expedition is not equipped to cope.
  - 原译：例如，一次冒险远征所涉及的风险，是通过想象远征队没有准备好应对的意外情况来评估的。
  - 现译：例如，评估一次冒险远征有多大风险时，人们会想象远征队没有准备好应对的意外情况。
  - 处理：Astra 复核通过。“是通过……来评估的”被动直译

- 英文：Chapman and Chapman[^17] have described an interesting bias in the judgment of the frequency with which two events co-occur.
  - 原译：查普曼夫妇[^17]描述了一种有趣的偏差，它出现在判断两个事件共同发生的频率时。
  - 现译：人们判断两个事件共同发生的频率时，会出现一种有趣的偏差，查普曼夫妇[^17]描述过这种偏差。
  - 处理：Astra 复核通过。“一种偏差，它出现在……”照搬后置修饰

- 英文：In their erroneous judgments of the data to which they had been exposed, naive subjects “rediscovered” much of the common, but unfounded, clinical lore concerning the interpretation of the draw-a-person test.
  - 原译：在对自己接触过的数据作出错误判断时，没受过专业训练的被试“重新发现”了许多关于如何解读画人测验的临床说法，这些说法流传很广，却毫无根据。
  - 现译：没受过专业训练的被试对自己看过的数据作出错误判断时，“重新发现”了许多关于如何解读画人测验的临床说法，这些说法流传很广，却毫无根据。
  - 处理：复核后重写。“在对……作出错误判断时”虚化动词 复核：“错误判断自己看过的数据”搭配生硬，删掉“对……作出错误判断”反而损害了中文的自然度；原译表达更清楚。

- 英文：The judgment of how frequently two events co-occur could be based on the strength of the associative bond between them.
  - 原译：对两个事件共同发生频率的判断，可能依据的是它们之间联想纽带的强度。
  - 现译：人们判断两个事件共同发生的频率，依据的可能是两者之间联想纽带的强度。
  - 处理：Astra 复核通过。“对……的判断”抽象名词作主语

- 英文：According to this view, the illusory correlation between suspiciousness and peculiar drawing of the eyes, for example, is due to the fact that suspiciousness is more readily associated with the eyes than with any other part of the body.
  - 原译：按照这种观点，例如多疑与眼睛画得怪异之间的错觉相关，就是因为多疑更容易让人联想到眼睛，而不是身体的其他任何部位。
  - 现译：按照这种观点，拿多疑与眼睛画得怪异之间的错觉相关来说，它之所以出现，是因为比起身体的其他任何部位，多疑更容易让人联想到眼睛。
  - 处理：Astra 复核通过。for example 插在主语前，句子不通

- 英文：Lifelong experience has taught us that, in general, instances of large classes are recalled better and faster than instances of less frequent classes; that likely occurrences are easier to imagine than unlikely ones; and that the associative connections between events are strengthened when the events frequently co-occur.
  - 原译：一生的经验告诉我们，一般来说，大类别的实例比频率较低的类别的实例回忆得更好、更快；可能发生的事情比不太可能发生的事情更容易想象；事件经常共同发生时，它们之间的联想联系就会加强。
  - 现译：一生的经验告诉我们，一般来说，大类别的实例比频率较低的类别中的实例回忆得更好、更快；可能发生的事情比不太可能发生的事情更容易想象；事件经常共同发生时，它们之间的联想联系就会加强。
  - 处理：复核后重写。“的类别的实例”的字连串 复核：与第 21 项相同，比较对象从两类实例变成了“类别”与“实例”，破坏了原文的比较关系。

- 英文：However, as the preceding examples have demonstrated, this valuable estimation procedure results in systematic errors.
  - 原译：然而，正如前面的例子所表明的，这种宝贵的估计程序会导致系统性错误。
  - 现译：然而，前面的例子已经表明，这种宝贵的估计程序会导致系统性错误。
  - 处理：Astra 复核通过。“正如……所表明的”照搬 as 从句

- 英文：In many situations, people make estimates by starting from an initial value that is adjusted to yield the final answer.
  - 原译：在许多情境中，人们作估计时，会从一个初始值出发，再加以调整，得出最终答案。
  - 现译：在许多情境中，人们作估计时，会从一个初始值出发，通过调整得出最终答案。
  - 处理：Astra 复核通过。虚化动词“加以”

- 英文：Different groups were given different numbers for each quantity, and these arbitrary numbers had a marked effect on estimates.
  - 原译：对于每个量，不同的组拿到的数字不同，而这些任意的数字对估计产生了显著的影响。
  - 现译：对于每个量，不同的组拿到的数字不同，而这些任意的数字明显影响了估计结果。
  - 处理：Astra 复核通过。“对……产生了显著的影响”直译 have an effect on

- 英文：Furthermore, because the result of the first few steps of multiplication (performed from left to right) is higher in the descending sequence than in the ascending sequence, the former expression should be judged larger than the latter.
  - 原译：此外，由于乘法的前几步（从左往右算）的结果在降序序列中比在升序序列中大，前一个算式应该会被判断为比后一个大。
  - 现译：此外，由于乘法的前几步（从左往右算）的结果在降序序列中比在升序序列中大，人们应该会判断前一个算式比后一个大。
  - 处理：Astra 复核通过。“会被判断为”被动直译

- 英文：The successful completion of an undertaking, such as the development of a new product, typically has a conjunctive character: for the undertaking to succeed, each of a series of events must occur.
  - 原译：一项事业的成功完成，比如开发一种新产品，通常具有合取的性质：要让这项事业成功，一系列事件中的每一个都必须发生。
  - 现译：成功完成一项任务（比如开发一种新产品），通常是一个合取事件：要让这项任务成功，一系列事件中的每一个都必须发生。
  - 处理：复核后重写。“……的成功完成”名词化主语 复核：“成功完成一项事业，通常具有……性质”仍然生硬；这里的 undertaking 指开发新产品这类具体任务，“事业”不够贴切。

- 英文：The general tendency to overestimate the probability of conjunctive events leads to unwarranted optimism in the evaluation of the likelihood that a plan will succeed or that a project will be completed on time.
  - 原译：高估合取事件概率的普遍倾向，会让人们在评估一项计划成功或一个项目按时完成的可能性时，抱有没有根据的乐观。
  - 现译：人们普遍倾向于高估合取事件的概率，因此在评估一项计划成功或一个项目按时完成的可能性时，会过于乐观。
  - 处理：复核后重写。“……的普遍倾向”抽象名词作主语 复核：“抱有没有根据的乐观”搭配不完整且读起来拗口，宜补足“态度”等中心词。

- 英文：These distributions indicated large and systematic departures from proper calibration.
  - 原译：这些分布显示出与恰当校准之间存在巨大的、系统性的偏离。
  - 现译：这些分布表明，判断者的校准存在很大的系统性偏差。
  - 处理：按复核意见修改。名词化“存在……的偏离” 复核：“分布偏离了校准”搭配不当，也混淆了证据与结论：原文说这些分布显示出判断者的校准存在很大且系统性的偏离。

- 英文：This bias is common to naive and to sophisticated subjects, and it is not eliminated by introducing proper scoring rules, which provide incentives for external calibration.
  - 原译：无论被试是外行还是内行，都普遍存在这种偏差，而且引入为外部校准提供激励的适当评分规则，也不能消除它。
  - 现译：无论被试是外行还是内行，都普遍存在这种偏差；即使引入适当的评分规则，激励被试改善外部校准，也不能消除这种偏差。
  - 处理：按复核意见修改。非限定性从句塞成长定语 复核：“激励外部校准”搭配生硬；接受激励的是被试，外部校准是要改善的方面。

- 英文：Indeed, several of the severe errors of judgment reported earlier occurred despite the fact that subjects were encouraged to be accurate and were rewarded for the correct answers.
  - 原译：事实上，前面报告的几个严重的判断错误，都是在鼓励被试力求准确、并对正确答案给予奖励的情况下出现的。
  - 现译：事实上，尽管研究者鼓励被试力求准确，并对答对的被试给予奖励，前面报告的几个严重判断错误仍然出现了。[^22]
  - 处理：按复核意见修改。“对……给予奖励”虚化动词，缺主语 复核：“研究者鼓励被试……、答对还有奖励”并列结构不齐整，而且没有充分表达 despite 所强调的让步关系。

- 英文：For example, the tendency to predict the outcome that best represents the data, with insufficient regard for prior probability, has been observed in the intuitive judgments of individuals who have had extensive training in statistics.
  - 原译：例如，在受过大量统计学训练的人所作的直觉判断中，也观察到了这样一种倾向：预测最能代表数据的结果，而对先验概率考虑不足。
  - 现译：例如，研究者观察到，受过大量统计学训练的人作直觉判断时，也有这样一种倾向：预测最能代表数据的结果，对先验概率却考虑不足。
  - 处理：Astra 复核通过。无主语被动“观察到了”，“所作的”长定语

- 英文：It is not surprising that useful heuristics such as representativeness and availability are retained, even though they occasionally lead to errors in prediction or estimation.
  - 原译：像代表性和可得性这样有用的启发式会被保留下来，尽管它们偶尔会导致预测或估计出错，这并不令人意外。
  - 现译：代表性和可得性这类有用的启发式，尽管偶尔会导致预测或估计出错，却仍被保留下来，这并不令人意外。
  - 处理：Astra 复核通过。让步从句照搬英文语序后置

- 英文：Although everyone is exposed, in the normal course of life, to numerous examples from which these rules could have been induced, very few people discover the principles of sampling and regression on their own.
  - 原译：虽然每个人在日常生活中都会接触到大量本可以从中归纳出这些规则的例子，但很少有人能自己发现抽样和回归的原理。
  - 现译：虽然每个人在日常生活中都会接触到大量例子，本可以从中归纳出这些规则，但很少有人能自己发现抽样和回归的原理。
  - 处理：Astra 复核通过。from which 从句塞成长定语

- 英文：Statistical principles are not learned from everyday experience because the relevant instances are not coded appropriately.
  - 原译：统计原理之所以不能从日常经验中学到，是因为相关的实例没有得到恰当的编码。
  - 现译：人们之所以没能从日常经验中学到统计原理，是因为他们没有恰当地给相关实例编码。
  - 处理：按复核意见修改。“没有得到……编码”被动虚化 复核：沿用了原译的情态问题：are not learned 说明人们没有学到，“不能……学到”却容易被理解为不可能从日常经验中学到。

- 英文：Specifically, the subjective probability of a given event is defined by the set of bets about this event that such a person is willing to accept.
  - 原译：具体来说，一个给定事件的主观概率，是由这样一个人愿意接受的关于该事件的一组赌注来定义的。
  - 现译：具体来说，某个事件的主观概率，由这样一个人愿意就这个事件接受哪些赌注来定义。
  - 处理：Astra 复核通过。“一个给定事件”直译，赌注前定语过长

- 英文：Consider a person whose subjective probabilities for all possible outcomes of a coin-tossing game reflect the gambler’s fallacy.
  - 原译：设想一个人，他对抛硬币游戏所有可能结果的主观概率都反映了赌徒谬误。
  - 现译：设想某个人对抛硬币游戏所有可能结果给出的主观概率都反映了赌徒谬误。
  - 处理：按复核意见修改。照搬 whose 从句“一个人，他……” 复核：“某个人对……的主观概率”关系表达不完整，缺少“给出”或“赋予”等连接成分，直接合句没有解决这个问题。

- 英文：The judgments of such a person could be internally consistent and therefore acceptable as adequate subjective probabilities according to the criterion of the formal theory.
  - 原译：这样一个人的判断可以是内部一致的，因此按照形式理论的标准，可以作为恰当的主观概率被接受。
  - 现译：这样一个人的判断可以是内部一致的，因此按照形式理论的标准，可以算作恰当的主观概率。
  - 处理：Astra 复核通过。“可以作为……被接受”被动直译

- 英文：For judged probabilities to be considered adequate, or rational, internal consistency is not enough.
  - 原译：要让判断出的概率被认为是恰当的，或者说理性的，光有内部一致性是不够的。
  - 现译：判断出的概率要算得上恰当，或者说理性，光有内部一致性是不够的。
  - 处理：Astra 复核通过。“要让……被认为是”被动直译

- 英文：This article described three heuristics that are employed in making judgments under uncertainty: (i) representativeness, which is usually employed when people are asked to judge the probability that an object or event A belongs to class or process B; (ii) availability of instances or scenarios, which is often employed when people are asked to assess the frequency of a class or the plausibility of a particular development; and (iii) adjustment from an anchor, which is usually employed in numerical prediction when a relevant value is available.
  - 原译：本文描述了在不确定条件下作判断时使用的三种启发式：（i）代表性，通常在人们被要求判断对象或事件 A 属于类别或过程 B 的概率时使用；（ii）实例或情景的可得性，常常在人们被要求评估一个类别的频率或某种事态发展的可信程度时使用；（iii）从锚出发的调整，通常在有相关数值可用时用于数值预测。
  - 现译：本文描述了在不确定条件下作判断时使用的三种启发式：（i）代表性，通常在人们需要判断对象或事件 A 属于类别或过程 B 的概率时使用；（ii）实例或情景的可得性，常常在人们需要评估一个类别的频率或某种事态发展的可信程度时使用；（iii）从锚出发的调整，通常在有相关数值可用时用于数值预测。
  - 处理：复核后保留改写。两处“被要求”被动句 复核：两处“被要求判断／评估”改成“需要判断／评估”，把接受判断任务改成了一般需求，改变了原文所述情境；原译的被动表达并无语病。

## 附录 B 选择、价值与框架

- 英文：ABSTRACT: We discuss the cognitive and the psychophysical determinants of choice in risky and riskless contexts.
  - 原译：摘要：我们讨论在有风险和无风险的情境中决定选择的认知因素和心理物理因素。
  - 现译：摘要：我们讨论在有风险和无风险的情境中，有哪些认知因素和心理物理因素决定人们的选择。
  - 处理：Astra 复核通过。名词前堆了一长串定语

- 英文：The tension between normative and descriptive considerations characterizes much of the study of judgment and choice.
  - 原译：规范考量与描述考量之间的张力，是判断与选择领域大部分研究的一个特点。
  - 现译：判断与选择领域的许多研究，都体现出规范考量与描述考量之间的张力。
  - 处理：按复核意见修改。抽象名词作主语，照搬英文句式 复核：much of 表示相当多，并未断言占多数；“大部分”把数量范围说得过强。这一问题原译也有。

- 英文：Because the consequences of such actions depend on uncertain events such as the weather or the opponent’s resolve, the choice of an act may be construed as the acceptance of a gamble that can yield various outcomes with different probabilities.
  - 原译：这类行动的后果取决于天气或对手的决心这类不确定的事件，因此，选择一种行动，可以理解为接受一场赌局，这场赌局会以不同的概率带来各种结果。
  - 现译：这类行动的后果取决于天气、对手的决心等不确定的事件，因此，选择一种行动，可以理解为接受一场赌局：赌局可能出现各种结果，每种结果的概率不同。
  - 处理：Astra 复核通过。“这类”重复，照搬定语从句

- 英文：In such a function, the difference between the utilities of $200 and $100, for example, is greater than the utility difference between $1,200 and $1,100.
  - 原译：在这样的函数中，比如说，200 美元和 100 美元的效用之差，大于 1,200 美元和 1,100 美元的效用之差。
  - 现译：比如，在这样的函数中，200 美元和 100 美元的效用之差，大于 1,200 美元和 1,100 美元的效用之差。
  - 处理：Astra 复核通过。插入语位置照搬英文

- 英文：For example, an offer to bet $20 on the toss of a fair coin is represented as a choice between an individual’s current wealth W and an even chance to move to W + $20 or to W – $20.
  - 原译：例如，有人提议就一次公平的抛硬币赌 20 美元，这会被表示为两者之间的选择：一边是这个人现在的财富 W，另一边是各有一半的机会变成 W + 20 美元或 W − 20 美元。
  - 现译：例如，一个人收到这样的提议：抛一枚均匀的硬币，赌 20 美元。决策分析会把这表示为两者之间的选择：一边是他现在的财富 W，另一边是各有一半的机会变成 W + 20 美元或 W − 20 美元。
  - 处理：复核后重写。不必要的被动句，“这个人”可能被误读成提议的人 复核：“收到提议，就……赌”衔接不清，容易混淆收到邀约与实际下注；“公平的抛硬币”也不自然，fair 修饰的是硬币。

- 英文：Modern decision theory can be said to begin with the pioneering work of von Neumann and Morgenstern (1947), who laid down several qualitative principles, or axioms, that should govern the preferences of a rational decision maker.
  - 原译：可以说，现代决策理论始于冯·诺伊曼和摩根斯坦（1947）的开创性工作，他们提出了几条定性的原则，也就是公理，理性决策者的偏好应当受这些公理支配。
  - 现译：可以说，现代决策理论始于冯·诺伊曼和摩根斯坦（1947）的开创性工作，他们提出了几条定性的原则，也就是公理，理性决策者的偏好应当遵循这些公理。
  - 处理：Astra 复核通过。“受……支配”的被动结构

- 英文：Dominance demands that if prospect A is at least as good as prospect B in every respect and better than B in at least one respect, then A should be preferred to B.
  - 原译：占优性要求：如果前景 A 在每一方面都至少和前景 B 一样好，并且至少在一个方面比 B 好，那么 A 就应该比 B 更受偏好。
  - 现译：占优性要求：如果前景 A 在每一方面都至少和前景 B 一样好，并且至少在一个方面比 B 好，那么就应该偏好 A 胜过 B。
  - 处理：复核后保留改写。“更受偏好”直译被动 复核：“偏好 A 胜过 B”仍是生硬的比较句式，改成“比起 B，更偏好 A”更清楚。

- 英文：The following pair of problems illustrates a violation of this requirement.
  - 原译：下面这对问题说明了这一要求如何被违背。
  - 现译：下面这对问题就是违背这一要求的一个例子。
  - 处理：Astra 复核通过。“如何被违背”被动生硬

- 英文：Such a representation would avoid the violations of invariance illustrated in the previous problems, but the advice is easier to give than to follow.
  - 原译：这样的表征可以避免前面那些问题所展示的对不变性的违背，但这个建议说起来容易，做起来难。
  - 现译：用这样的表征，可以避免前面那些问题里出现的违背不变性的情况，但这个建议说起来容易，做起来难。
  - 处理：Astra 复核通过。“所展示的对……的违背”的字连串

- 英文：Low probabilities, however, are overweighted, and very low probabilities are either overweighted quite grossly or neglected altogether, making the decision weights highly unstable in that region.
  - 原译：然而，低概率会被赋予过高的权重，极低的概率则要么被赋予严重过高的权重，要么被完全忽略，这使得决策权重在这个区域非常不稳定。
  - 现译：然而，低概率的权重过高；极低的概率则要么权重严重过高，要么被完全忽略，因此这个区域的决策权重非常不稳定。
  - 处理：Astra 复核通过。“被赋予”被动句连用，“这使得”照搬分词结构

- 英文：More specifically, we propose that in Problem 5 people ignore the first phase, which yields the same outcome regardless of the decision that is made, and focus their attention on what happens if they do reach the second stage of the game.
  - 原译：具体来说，我们认为，在问题 5 中，第一阶段无论做什么决定，结果都一样，人们忽略了这个阶段，把注意力集中在真的进入第二阶段后会发生什么上。
  - 现译：具体来说，我们认为，在问题 5 中，第一阶段无论做什么决定，结果都一样，人们忽略了这个阶段，专注于真的进入第二阶段后会发生什么。
  - 处理：Astra 复核通过。“集中在……什么上”搭配别扭

- 英文：According to expected utility theory, probabilistic insurance should be definitely preferred to normal insurance when the latter is just acceptable (see Kahneman and Tversky 1979).
  - 原译：根据期望效用理论，当普通保险刚好可以接受时，概率性保险应该明确地比普通保险更受偏好（见 Kahneman and Tversky 1979）。
  - 现译：根据期望效用理论，当普通保险刚好可以接受时，人们无疑应当更偏好概率性保险，而不是普通保险（见 Kahneman and Tversky 1979）。
  - 处理：按复核意见修改。“更受偏好”直译被动 复核：“明确地偏好……，胜过……”搭配和比较结构都生硬；definitely 的确定语气宜用“无疑应当”表达。

- 英文：An insurance policy that covers fire but not flood, for example, could be evaluated either as full protection against a specific risk (e.g., fire), or as a reduction in the overall probability of property loss.
  - 原译：例如，一份保火灾、不保洪水的保单，既可以被看作针对某种特定风险（比如火灾）的全面保障，也可以被看作降低了财产损失的总体概率。
  - 现译：例如，一份保火灾、不保洪水的保单，既可以看作针对某种特定风险（比如火灾）的全面保障，也可以看作降低了财产损失的总体概率。
  - 处理：Astra 复核通过。多余的“被”字

- 英文：Unfortunately, the mental machinery that performs these operations silently and effortlessly is not adequate to perform the task of recoding the two versions of the public health problem or the mortality-survival statistics into a common abstract form.
  - 原译：遗憾的是，这套悄无声息、毫不费力地完成这些操作的心理机制，却不足以把公共卫生问题的两个版本，或者死亡率和存活率的统计数据，重新编码成共同的抽象形式。
  - 现译：遗憾的是，这套心理机制虽然能悄无声息、毫不费力地完成这些操作，却不足以把公共卫生问题的两个版本，或者死亡率和存活率的统计数据，重新编码成共同的抽象形式。
  - 处理：按复核意见修改。主语前堆了一长串定语 复核：silently 和 effortlessly 修饰完成操作的方式，改写后却直接描述心理机制，造成“心理机制毫不费力”的不当搭配。

- 英文：The following problem, based on examples of Savage (1954) and Thaler (1980), introduces some of the rules that govern the construction of mental accounts and illustrates the extension of the concavity of value to the acceptability of transactions.
  - 原译：下面这个问题以萨维奇（1954）和塞勒（1980）的例子为基础，介绍了支配心理账户建立的一些规则，也说明了价值的凹性怎样推广到交易的可接受性上。
  - 现译：下面这个问题以萨维奇（1954）和塞勒（1980）的例子为基础，介绍了建立心理账户时遵循的一些规则，也说明了价值的凹性怎样推广到交易的可接受性上。
  - 处理：Astra 复核通过。“支配……建立的规则”直译 govern

- 英文：A topical account relates the consequences of possible choices to a reference level that is determined by the context within which the decision arises.
  - 原译：主题账户把可能选择的后果，与一个由决策所处的情境决定的参照水平联系起来。
  - 现译：主题账户把各种可能选择的后果，与某个参照水平联系起来，这个参照水平由决策所处的情境决定。
  - 处理：Astra 复核通过。定语从句前置成长定语

- 英文：The formulation of the preceding problem appears neutral with respect to the adoption of a minimal, topical, or comprehensive account.
  - 原译：就采用最小账户、主题账户还是综合账户而言，上面这个问题的表述看起来是中立的。
  - 现译：上面这个问题的表述，看起来并不偏向最小账户、主题账户和综合账户中的任何一种。
  - 处理：Astra 复核通过。“就……而言”照搬 with respect to

- 英文：Topical organization, in conjunction with the concavity of value, entails that the willingness to travel to the other store for a saving of $5 on a calculator should be inversely related to the price of the calculator and should be independent of the price of the jacket.
  - 原译：按主题组织账户，再加上价值的凹性，就意味着：为了在计算器上省 5 美元而跑去另一家店的意愿，应该与计算器的价格负相关，并且与夹克的价格无关。
  - 现译：按主题组织账户，再加上价值的凹性，就意味着：为了在计算器上省 5 美元而跑去另一家店的意愿，应该与计算器的价格负相关，并且与夹克的价格无关。
  - 处理：复核后退回原译。抽象名词“意愿”前堆长定语 复核：把“……的意愿”拆成“为了……，人们愿意……的程度”，表达反而拖沓、拗口。原译的“意愿”准确自然，不属于需要消除的名词化。

- 英文：The significance of topical accounts for consumer behavior is confirmed by the observation that the standard deviation of the prices that different stores in a city quote for the same product is roughly proportional to the average price of that product (Pratt, Wise, and Zeckhauser 1979). Since the dispersion of prices is surely controlled by shoppers’ efforts to find the best buy, these results suggest that consumers hardly exert more effort to save $15 on a $150 purchase than to save $5 on a $50 purchase.
  - 原译：主题账户对消费者行为的重要性，还得到了这样一项观察的证实：同一座城市里不同商店对同一种商品的报价，其标准差大致与这种商品的平均价格成正比（Pratt, Wise, and Zeckhauser 1979）。价格的分散程度必定受购物者寻找最划算交易的努力所制约，所以这些结果表明，消费者为了在 150 美元的购物中省 15 美元所付出的努力，几乎不比为了在 50 美元的购物中省 5 美元所付出的多。
  - 现译：还有一项观察证实了主题账户对消费者行为的重要性：同一座城市里不同商店对同一种商品的报价，其标准差大致与这种商品的平均价格成正比（Pratt, Wise, and Zeckhauser 1979）。价格的分散程度必定取决于购物者花多大力气寻找最划算的交易，所以这些结果表明，消费者为了在 150 美元的购物中省 15 美元，付出的努力几乎不比为了在 50 美元的购物中省 5 美元多。
  - 处理：Astra 复核通过。“得到……证实”“受……所制约”被动，“所付出的”重复

- 英文：The following problems illustrate another example of mental accounting in which the posting of a cost to an account is controlled by topical organization:
  - 原译：下面的问题说明了心理账户的另一个例子，在这个例子里，一笔成本记到哪个账户上，取决于账户按主题组织的方式：
  - 现译：下面的问题是心理账户的另一个例子，这里一笔成本记到哪个账户上，取决于账户按主题组织的方式：
  - 处理：Astra 复核通过。“说明了……的例子”直译 illustrate，“在这个例子里”照搬 in which

- 英文：The difference between the responses to the two problems is intriguing.
  - 原译：两个问题的回答之间的差别耐人寻味。
  - 现译：两个问题的回答不一样，这一点耐人寻味。
  - 处理：Astra 复核通过。“的……之间的差别”的字连串，名词化主语

- 英文：These results have been presented as challenges to standard economic theory, in which buying and selling prices coincide except for transaction costs and effects of wealth.
  - 原译：这些结果被看作对标准经济理论的挑战，在标准经济理论中，除去交易成本和财富效应，买入价和卖出价是一致的。
  - 现译：这些结果被看作对标准经济理论的挑战：按照标准经济理论，除去交易成本和财富效应，买入价和卖出价是一致的。
  - 处理：Astra 复核通过。照搬 in which 从句接在后面

- 英文：In addition to favoring stability over change, the combination of adaptation and loss aversion provides limited protection against regret and envy by reducing the attractiveness of foregone alternatives and of others’ endowments.
  - 原译：适应和损失厌恶结合在一起，除了让人偏爱稳定、不喜欢变化之外，还会降低已经放弃的选项和别人的禀赋的吸引力，从而在有限的程度上保护人们免受后悔和嫉妒之苦。
  - 现译：适应和损失厌恶结合在一起，除了让人偏爱稳定、不喜欢变化之外，还会让已经放弃的选项和别人拥有的东西显得没那么有吸引力，从而在有限的程度上保护人们免受后悔和嫉妒之苦。
  - 处理：复核后重写。“……的禀赋的吸引力”的字连串 复核：“偏爱稳定、不喜欢变化”把相对偏好扩大成了对变化的否定。这一问题原译也有。另外，endowments 在此指拥有的资源或条件，单写“禀赋”容易被理解成天赋。

- 英文：In accord with standard economic analysis, money is naturally viewed as a proxy for the goods and services that it could buy.
  - 原译：与标准的经济分析一致，钱很自然地被看作它能买到的商品和服务的代表。
  - 现译：与标准的经济分析一致，人们很自然地把钱看作它能买到的商品和服务的代表。
  - 处理：Astra 复核通过。不必要的被动句

- 英文：The concepts of utility and value are commonly used in two distinct senses: (a) experience value, the degree of pleasure or pain, satisfaction or anguish in the actual experience of an outcome; and (b) decision value, the contribution of an anticipated outcome to the overall attractiveness or aversiveness of an option in a choice.
  - 原译：效用和价值这两个概念通常有两种不同的用法：（a）体验价值，指实际体验一个结果时感到的快乐或痛苦、满足或苦恼的程度；（b）决策价值，指在一次选择中，一个预期的结果对某个选项总体的吸引力或令人反感的程度所起的作用。
  - 现译：效用和价值这两个概念通常有两种不同的用法：（a）体验价值，指实际体验一个结果时感到的快乐或痛苦、满足或苦恼的程度；（b）决策价值，指在一次选择中，一个预期的结果对某个选项总体的吸引力或令人反感的程度所起的作用。
  - 处理：复核后退回原译。“对……所起的作用”名词化结构，意思含糊 复核：“为……吸引力或让人反感的程度贡献了多少”搭配生硬，比原译更像对 contribution 的逐词硬译。“所起的作用”已经准确表达原意，改写没有改善中文。

- 英文：In contrast to the large amount of research on decision making, there has been relatively little systematic exploration of the psychophysics that relate hedonic experience to objective states. The most basic problem of hedonic psychophysics is the determination of the level of adaptation or aspiration that separates positive from negative outcomes.
  - 原译：与大量的决策研究相比，对于享乐体验与客观状态之间关系的心理物理规律，系统的探索相对较少。享乐心理物理学最基本的问题，是确定那个把正面结果和负面结果分开的适应水平或抱负水平。
  - 现译：决策方面的研究很多，相比之下，人们较少系统地探索享乐体验与客观状态之间的心理物理关系。享乐心理物理学最基本的问题，是确定正面结果和负面结果的分界，也就是适应水平或抱负水平。
  - 处理：复核后重写。“对于……的”长定语，“那个……的”照搬关系从句 复核：第一句把“有怎样的心理物理关系”直接接到“系统的探索相对较少”，话题与谓语衔接生硬；应明确探索的对象。

- 英文：The framing of outcomes often induces decision values that have no counterpart in actual experience.
  - 原译：结果的框架常常会引出一些在实际体验中没有对应物的决策价值。
  - 现译：结果的框架常常会引出一些决策价值，它们在实际体验中没有对应物。
  - 处理：Astra 复核通过。定语从句前置成长定语

- 英文：In such cases, the evaluation of outcomes in the context of decisions not only anticipates experience but also molds it.
  - 原译：在这类情况下，在决策情境中对结果的评估，不仅是对体验的预期，还会塑造体验。
  - 现译：在这类情况下，人们在决策时对结果的评估，不仅是对体验的预期，还会塑造体验。
  - 处理：Astra 复核通过。“在……在……”介词短语叠用，照搬 in the context of

## 注释

- 英文：We had read a book that criticized psychologists for using small samples, but did not explain their choices:
  - 原译：我们读过一本书，它批评心理学家使用小样本，却没有解释心理学家为什么会这样选择：
  - 现译：我们读过一本书，书中批评心理学家使用小样本，却没有解释他们为什么这样选择：
  - 处理：Astra 复核通过。照搬从句用“它”回指，主语重复

- 英文：Agents within the mind are called homunculi and are (quite properly) objects of professional derision.
  - 原译：心智内部的这些主体被称为“小矮人”（homunculi），它们是专业人士嘲笑的对象，这也理所应当。
  - 现译：心智内部的这类主体叫作“小矮人”（homunculi），是专业人士嘲笑的对象，这也理所应当。
  - 处理：Astra 复核通过。不必要的“被称为”和多余代词“它们”

- 英文：Their detection results showed the inverted-V pattern observed with other subjects.
  - 原译：他们的检测结果呈现出在其他受试者身上观察到的倒 V 形模式。
  - 现译：他们的检测结果也呈现出倒 V 形模式，和在其他受试者身上观察到的一样。
  - 处理：Astra 复核通过。名词前堆了长定语

- 英文：Neuroscientists have identified a region of the brain that assesses the overall value of an action when it is completed.
  - 原译：神经科学家已经找到了大脑中的一个区域，它会在一个行动完成时评估这个行动的总体价值。
  - 现译：神经科学家已经发现，大脑中有一个区域会在行动完成时评估该行动的总体价值。
  - 处理：按复核意见修改。照搬定语从句“一个区域，它会……” 复核：“找到一个区域，一个行动完成时”衔接突兀，后面又连续回指，语序仍不够顺畅。

- 英文：Timothy Wilson’s Strangers to Ourselves (Cambridge, MA: Belknap Press, 2002) presents a concept of an “adaptive unconscious” that is similar to System 1.
  - 原译：蒂莫西·威尔逊的 Strangers to Ourselves (Cambridge, MA: Belknap Press, 2002) 提出了“适应性潜意识”的概念，它与系统 1 相似。
  - 现译：蒂莫西·威尔逊的 Strangers to Ourselves (Cambridge, MA: Belknap Press, 2002) 提出了一个与系统 1 相似的概念：“适应性潜意识”。
  - 处理：Astra 复核通过。照搬 that 从句，用“它”回指

- 英文：It is a fallback. Although its reliability is imperfect, the fallback is much better than nothing. It is the sense of familiarity that protects you from the embarrassment of being (and acting) astonished when you are greeted as an old friend by someone who only looks vaguely familiar.
  - 原译：它是一种后备手段。它虽然不完全可靠，却比什么都没有好得多。一个看上去只是隐约有点眼熟的人像老朋友一样跟你打招呼时，正是熟悉感让你免于尴尬，不至于大吃一惊（并且露出吃惊的样子）。
  - 现译：它是一种后备手段，虽然不完全可靠，却比什么都没有好得多。有人像老朋友一样跟你打招呼，你却只觉得他看着隐约有点眼熟，这时正是熟悉感让你免于尴尬，不至于大吃一惊（并且露出吃惊的样子）。
  - 处理：Astra 复核通过。代词重复，主语前长定语加“……时”

- 英文：The analysis excludes all cases in which the subject actually found the correct solution.
  - 原译：这项分析排除了受试者实际找到正确答案的所有情况。
  - 现译：这项分析把受试者真正找到正确答案的情况全部排除在外。
  - 处理：复核后重写。宾语前定语过长 复核：原句的定语并不难懂；改后把较长的宾语悬置在句首，语序反而更拗口。

- 英文：They describe “fast and frugal” formal procedures such as “Take the best [cue],” which under some circumstances generate quite accurate judgments on the basis of little information.
  - 原译：他们描述了一些“快速节俭”的形式化程序，例如“取最佳（线索）”，这些程序在某些情况下能根据很少的信息作出相当准确的判断。
  - 现译：他们描述了一些“快速节俭”的形式化程序，例如“取最佳（线索）”，这些程序在某些情况下只凭很少的信息，就能得出相当准确的判断。
  - 处理：Astra 复核通过。直译 on the basis of，虚化动词“作出”

- 英文：The most memorable discovery associated with this approach is the recognition heuristic, illustrated by an example that has become well-known: a subject who is asked which of two cities is larger and recognizes one of them should guess that the one she recognizes is larger.
  - 原译：有一个例子已经广为人知：一位受试者被问到两座城市哪座更大，如果她认得其中一座，就应该猜她认得的那座更大。
  - 现译：有一个例子已经广为人知：问一位受试者两座城市哪座更大，如果她认得其中一座，就应该猜她认得的那座更大。
  - 处理：Astra 复核通过。不必要的被动句

- 英文：if she knows it to be small, however, she will quite reasonably guess that the unknown city is larger.
  - 原译：但如果她知道那座城市很小，她就会很合理地猜那座不认识的城市更大。
  - 现译：但如果她知道那座城市很小，就会猜那座不认识的城市更大，这也十分合理。
  - 处理：Astra 复核通过。副词“很合理地”照搬 quite reasonably，代词多余

- 英文：Mood is known to vary with the weather, and substitution explains the effect on reported happiness.
  - 原译：我们知道心情会随天气变化，替代就能解释天气对报告的幸福感的影响。
  - 现译：我们知道心情会随天气变化，而替代可以解释天气为什么会影响人们报告的幸福感。
  - 处理：按复核意见修改。“对……的影响”名词化，“的”字连串 复核：“天气之所以……，用替代就能解释”前后句式衔接不顺，仍有明显的拼接感。

- 英文：These respondents were asked about the current weather before they were asked the happiness question. For them, weather had no effect at all on reported happiness! The explicit priming of weather provided them with an explanation of their mood, undermining the connection that would normally be made between current mood and overall happiness.
  - 原译：这个版本的受访者在被问到幸福感问题之前，先被问到了当时的天气。对他们来说，天气对报告的幸福感完全没有影响！明确地用天气来启动，给他们的心情提供了一个解释，从而削弱了当前心情与总体幸福感之间通常会建立起来的联系。
  - 现译：这个版本先问受访者当时的天气，再问幸福感问题。这些受访者报告的幸福感，完全不受天气影响！明确问到天气，起到了启动作用，让他们对自己的心情有了一个解释；人们通常会把当前的心情和总体幸福感联系起来，这层联系因此削弱了。
  - 处理：复核后重写。连用被动句，“对他们来说”，宾语前长定语 复核：“明确地用天气来启动”没有交代启动的具体方式，“让他们的心情有了一个解释”也较生硬；应明确是受访者获得了对自身心情的解释。

- 英文：Damasio’s idea is known as the “somatic marker hypothesis” and it has gathered substantial support:
  - 原译：达马西奥的观点称为“躯体标记假说”，它已经得到大量支持：
  - 现译：达马西奥的观点叫作“躯体标记假说”，已经得到大量支持：
  - 处理：Astra 复核通过。多余代词“它”

- 英文：Also the story exposed EPA’s lack of competence in attending to and evaluating the safety of Alar, destroying trust in regulatory control.
  - 原译：这个报道还暴露出美国环境保护署（EPA）在关注和评估阿拉尔的安全性方面能力不足，摧毁了人们对监管的信任。
  - 现译：这个报道还暴露出，美国环境保护署（EPA）关注和评估阿拉尔安全性的能力不足，这摧毁了人们对监管的信任。
  - 处理：Astra 复核通过。“在……方面”套话

- 英文：The test is fairly accurate. Its likelihood ratio is 25:1, which means that the probability that a person who has the disease will test positive is 25 times higher than the probability of a false positive.
  - 原译：这种检测相当准确，它的似然比是 25:1，意思是患病的人检测呈阳性的概率，是出现假阳性的概率的 25 倍。
  - 现译：这种检测相当准确，似然比是 25:1，意思是患病的人检测呈阳性的概率，是出现假阳性的概率的 25 倍。
  - 处理：Astra 复核通过。多余代词“它的”

- 英文：This will not be true in an environment in which some children are malnourished.
  - 原译：在一些儿童营养不良的环境中，情况就不是这样了。
  - 现译：如果环境里有一些儿童营养不良，情况就不是这样了。
  - 处理：Astra 复核通过。照搬 in an environment in which，“一些”修饰对象含糊

- 英文：The relevant formula is √(1–r²), where r is the correlation.
  - 原译：相关的公式是 √(1 − r²)，其中 r 是相关系数。
  - 现译：这里用到的公式是 √(1 − r²)，其中 r 是相关系数。
  - 处理：Astra 复核通过。relevant 直译成“相关的”，和“相关系数”混淆

- 英文：The Halo Effect was praised as one of the best business books of the year by both the Financial Times and The Wall Street Journal:
  - 原译：《光环效应》（The Halo Effect）被《金融时报》和《华尔街日报》都评为年度最佳商业图书之一：
  - 现译：《金融时报》和《华尔街日报》都称赞《光环效应》（The Halo Effect）是年度最佳商业图书之一：
  - 处理：Astra 复核通过。照搬被动句，“被……都评为”别扭

- 英文：The incoming CEO then gets credit, at least temporarily, for his new firm’s subsequent improvement.
  - 原译：随后，新任 CEO 会因为新公司后来的好转而得到赞誉，至少暂时如此。
  - 现译：随后新公司有了起色，功劳就算在新任 CEO 头上，至少一时如此。
  - 处理：Astra 复核通过。“因为……而得到赞誉”直译 get credit for

- 英文：Research on stock trades in Taiwan concluded that the transfer of wealth from individuals to financial institutions amounts to a staggering 2.2% of GDP:
  - 原译：一项对台湾股票交易的研究得出结论，从个人投资者转移到金融机构的财富相当于 GDP 的 2.2%，数额惊人：
  - 现译：一项研究分析了台湾的股票交易，结论是，从个人投资者转移到金融机构的财富相当于 GDP 的 2.2%，数额惊人：
  - 处理：复核后重写。“一项对……的研究”名词化主语 复核：原句“一项对台湾股票交易的研究”清楚自然；改成“有一项研究分析了……，得出的结论是”增加了不必要的铺垫，反而拖沓。

- 英文：The Getty Museum in Los Angeles brings in the world’s leading experts on Greek sculpture to view a kouros—a marble statue of a striding boy—that it is about to buy. One after another, the experts react with what one calls “intuitive repulsion”—a powerful hunch that the kouros is not 2,500 years old but a modern fake.
  - 原译：洛杉矶的盖蒂博物馆请来世界顶尖的希腊雕塑专家，察看一尊它即将买下的青年雕像，也就是一尊大步行走的少年大理石像。专家们一个接一个，都产生了其中一位所说的“直觉上的排斥”，也就是一种强烈的预感：这尊雕像没有 2,500 年的历史，是现代的赝品。
  - 现译：洛杉矶的盖蒂博物馆准备买下一尊青年雕像，也就是一尊少年迈步行走的大理石像，买之前请来世界顶尖的希腊雕塑专家察看。专家们一个接一个，都产生了其中一位所说的“直觉上的排斥”，也就是一种强烈的预感：这尊雕像没有 2,500 年的历史，是现代的赝品。
  - 处理：复核后重写。“一尊它即将买下的”照搬定语从句，“其中一位所说的”长定语 复核：调整叙述顺序有帮助，但“一个接一个地产生了一种反应”空泛拖沓，“大步行走的少年大理石像”的修饰层次也不清楚。

- 英文：The closest any of them could come to a rationale is an Italian art historian’s complaint that something—he does not know exactly what—“seemed wrong” with the statue’s fingernails.
  - 原译：最接近于给出理由的，是一位意大利艺术史学家的抱怨：雕像的指甲有什么地方“看起来不对劲”，至于究竟是什么地方，他也说不清。
  - 现译：勉强算得上理由的，是一位意大利艺术史学家的抱怨：雕像的指甲有什么地方“看起来不对劲”，至于究竟是什么地方，他也说不清。
  - 处理：复核后重写。“最接近于给出理由的”照搬英文结构 复核：“最接近理由的说法”搭配生硬，并不比原来的“最接近于给出理由”清楚。

- 英文：and a Greek expert flatly stated, “Anyone who has ever seen a sculpture coming out of the ground could tell that that thing has never been in the ground.”
  - 原译：一位希腊专家则直截了当地说：“任何见过刚出土的雕塑的人都看得出来，这东西从没在土里待过。”
  - 现译：一位希腊专家则直截了当地说：“只要见过刚出土的雕塑，谁都看得出来，这东西从没在土里待过。”
  - 处理：Astra 复核通过。“任何……的人都”照搬 anyone who，引语不像口语

- 英文：He wrote a classic on decision making in organizations while still in his twenties, and among many other achievements he went on to be one of the founders of the field of artificial intelligence, a leader in cognitive science, an influential student of the process of scientific discovery, a forerunner of behavioral economics and, almost incidentally, a Nobel laureate in economics.
  - 原译：他二十多岁时就写出了一部关于组织决策的经典著作；在众多其他成就之外，他后来还成为人工智能领域的创始人之一、认知科学的领军人物、科学发现过程的一位有影响力的研究者、行为经济学的先驱，而且几乎是顺带地，还获得了诺贝尔经济学奖。
  - 现译：他二十多岁时就写出了一部关于组织决策的经典著作。他的成就还有很多：后来成为人工智能领域的创始人之一、认知科学的领军人物、研究科学发现过程的一位有影响力的学者、行为经济学的先驱，而且几乎是顺带着，还获得了诺贝尔经济学奖。
  - 处理：Astra 复核通过。“在众多其他成就之外”照搬 among，“科学发现过程的研究者”语序生硬

- 英文：The labels are often misunderstood.
  - 原译：这两个名称常常被误解。
  - 现译：常有人误解这两个名称。
  - 处理：Astra 复核通过。不必要的被动句

- 英文：A form of competition neglect has also been observed in the time of day at which sellers on eBay choose to end their auctions.
  - 原译：在 eBay 卖家选择在一天中的什么时候结束拍卖这件事上，也可以看到一种忽视竞争的现象。
  - 现译：eBay 卖家在选择一天中的哪个时段结束拍卖时，也表现出一种忽视竞争的现象。
  - 处理：按复核意见修改。“在……这件事上”长状语 复核：“选在……什么时候结束拍卖，从这里……”衔接松散，仍未理顺句子结构。

- 英文：It is known as Weber’s law, after the German physiologist Ernst Heinrich Weber, who discovered it.
  - 原译：它被称为韦伯定律，得名于发现它的德国生理学家恩斯特·海因里希·韦伯。
  - 现译：它叫作韦伯定律，得名于发现它的德国生理学家恩斯特·海因里希·韦伯。
  - 处理：Astra 复核通过。不必要的“被称为”

- 英文：How much would you pay for an opportunity to play that game?” People do not think the gamble is worth more than a few dollars, although its expected value is infinite—because the prize keeps growing, the expected value is $1 for each toss, to infinity.
  - 原译：你愿意花多少钱来换取玩这个游戏的机会？”人们觉得这个赌局最多值几美元，尽管它的期望值是无穷大：因为奖金不断增长，每抛一次的期望值都是 1 美元，一直加到无穷。
  - 现译：你愿意出多少钱来玩这个游戏？”人们觉得这个赌局最多值几美元，可它的期望值是无穷大：因为奖金不断增长，每抛一次的期望值都是 1 美元，一直加到无穷。
  - 处理：Astra 复核通过。“换取……的机会”直译，“尽管”从句后置

- 英文：Not many people thought about choices in which all options are bad, although we were by no means the first to observe risk seeking. Another fact that favors Bernoulli’s theory is that thinking in terms of final states of wealth and ignoring the past is often a very reasonable thing to do.
  - 原译：很少有人思考过所有选项都很糟糕的选择，尽管我们绝不是最早观察到风险寻求的人。另一个对伯努利理论有利的事实是，从最终财富状态的角度来思考、不去管过去，往往是非常合理的做法。
  - 现译：很少有人思考过所有选项都很糟糕的选择，不过，最早观察到风险寻求的人也绝不是我们。还有一个事实对伯努利的理论有利：着眼于最终的财富状态、不去管过去，往往是非常合理的做法。
  - 处理：Astra 复核通过。“尽管”后置，主语前长定语，“从……的角度”

- 英文：Writing this sentence reminded me that the graph of the value function has already been used as an emblem.
  - 原译：写这句话时，我想起价值函数的图像已经被当作徽记用过了。
  - 现译：写这句话时，我想起价值函数的图像已经被当作徽记用过了。
  - 处理：复核后退回原译。不必要的被动句 复核：原文只说已经用作徽记，没有交代使用次数；“一回”增加了数量表述，“当过徽记”也不如原译自然。

- 英文：My illustration was a stylized rendition of figure 10.
  - 原译：我证书上的插图，就是图 10 的一个风格化版本。
  - 现译：我证书上的插图，就是图 10 的一个风格化版本。
  - 处理：复核后退回原译。直译 a stylized rendition，多余的“一个” 复核：“风格化了的图 10”拗口；原译“图 10 的一个风格化版本”更清楚地表达了 rendition，也更自然。

- 英文：He was now prepared to take the conclusion much more seriously than in the past. Mathematical arguments have a definitive quality that is more compelling than appeals to common sense.
  - 原译：他现在愿意比过去认真得多地对待这个结论。数学论证有一种确定无疑的性质，比诉诸常识更有说服力。
  - 现译：这一次，他对待这个结论比过去认真得多。数学论证有一种不容置疑的确定性，比诉诸常识更有说服力。
  - 处理：复核后重写。比较状语堆在动词前，“有一种……的性质”直译 复核：“愿意认真对待这个结论了”容易暗示此前不愿认真对待；原文只是说现在愿意比过去认真得多，原译保留了这一比较关系。

- 英文：Suppose an individual’s wealth is W, and she rejects a gamble with equal probabilities to win $11 or lose $10.
  - 原译：假设一个人的财富是 W，她拒绝了一个以相同概率赢 11 美元或输 10 美元的赌局。
  - 现译：假设一个人的财富是 W，她拒绝了这样一个赌局：赢 11 美元和输 10 美元的概率相同。
  - 处理：Astra 复核通过。名词前长定语

- 英文：This is an extraordinarily steep decline and the effect increases steadily as the gambles become more extreme.
  - 原译：这是一种极其陡峭的下降，而且赌局越极端，这种效应就越强。
  - 现译：这是极其陡峭的下降，而且赌局越极端，这种效应就越强。
  - 处理：复核后重写。“这是一种……的下降”名词化 复核：“这个下降”搭配生硬，改写并未消除名词化，反而不如原句顺畅。

- 英文：Decision makers’ choices between gambles depend on whether they expect to know the outcome of the gamble they did not choose.
  - 原译：决策者在赌局之间的选择，取决于他们是否预期能知道自己没选的那个赌局的结果。
  - 现译：决策者在几个赌局之间怎么选，取决于他们预期自己能不能知道没选的那个赌局的结果。
  - 处理：Astra 复核通过。抽象名词作主语

- 英文：These people (half of the total) are expected to move by trading places with each other, so that in the end everyone in the first half of the line has a token, and no one behind them does.
  - 原译：预计这些人（占总人数的一半）会通过相互交换位置来移动，最终，队伍前半段的每个人都有一枚代币，他们后面的人都没有。
  - 现译：可以预料，这些人（占总人数的一半）会彼此交换位置，最终，队伍前半段的每个人都有一枚代币，排在他们后面的人都没有。
  - 处理：Astra 复核通过。“通过……来移动”直译 move by

- 英文：Plott and Zeiler believe that participants who show the endowment effect are under some misconception about what their true values are, and they modified the procedures of the original experiments to eliminate the misconceptions.
  - 原译：普洛特和蔡勒认为，表现出禀赋效应的参与者在自己对物品的真实估值上抱有某种误解，于是他们修改了原始实验的程序，以消除这些误解。
  - 现译：普洛特和蔡勒认为，表现出禀赋效应的参与者对自己的真实估值有某种误解，于是修改了原始实验的程序，以消除这些误解。
  - 处理：Astra 复核通过。“在……上抱有某种误解”生硬，代词多余

- 英文：In their studies of decision making under poverty, Eldar Shafir, Sendhil Mullainathan, and their colleagues have observed other instances in which poverty induces economic behavior that is in some respects more realistic and more rational than that of people who are better off.
  - 原译：埃尔达·沙菲尔、塞德希尔·穆来纳森和他们的同事在研究贫困状态下的决策时，还观察到另外一些例子：贫困促使人们做出的经济行为，在某些方面比境况较好的人的行为更现实、更理性。
  - 现译：埃尔达·沙菲尔、塞德希尔·穆来纳森和他们的同事在研究贫困状态下的决策时，还观察到另外一些例子：贫困促使人们做出的经济行为，在某些方面比境况较好的人的行为更现实、更理性。
  - 处理：复核后退回原译。主语前长定语 复核：删去“的行为”后，变成“经济行为”与“境况较好的人”比较，比较对象不对等；原文比较的是两类人的经济行为。

- 英文：The conclusion that money spent on purchases is not experienced as a loss is more likely to be true for people who are relatively well-off.
  - 原译：花钱购物不被体验为损失，这个结论更可能适用于比较富裕的人。
  - 现译：人们不会觉得购物花出去的钱是一种损失，这个结论更可能适用于比较富裕的人。
  - 处理：按复核意见修改。照搬被动“不被体验为” 复核：“把购物花的钱体验为损失”仍是生硬的直译，改成主动句并未解决搭配问题。

- 英文：Including exposure to a “Dutch book,” which is a set of gambles that your incorrect preferences commit you to accept and is guaranteed to end up in a loss.
  - 原译：荷兰赌是一组赌局，你错误的偏好让你必须接受它们，而它们最终注定让你亏损。
  - 现译：荷兰赌是这样一组赌局：你错误的偏好让你不得不接受它们，结果注定是亏损。
  - 处理：Astra 复核通过。代词“它们”连用

- 英文：It is both much simpler and actually a stronger violation than the original paradox.
  - 原译：它比原来的悖论简单得多，实际上也是对理性规则更强烈的违背。
  - 现译：它比原来的悖论简单得多，实际上也更严重地违背了理性规则。
  - 处理：Astra 复核通过。“是对……的违背”名词化

- 英文：In a rational model with diminishing marginal utility, people should pay at least two-thirds as much to reduce the frequency of accidents from 15 to 5 units as they are willing to pay to eliminate the risk.
  - 原译：在一个边际效用递减的理性模型中，人们为把事故频率从 15 个单位降到 5 个单位愿意支付的钱，至少应该是他们为完全消除这种风险愿意支付的钱的三分之二。
  - 现译：在边际效用递减的理性模型中，人们愿意花钱把事故频率从 15 个单位降到 5 个单位，这笔钱至少应该是他们愿意为完全消除这种风险所付金额的三分之二。
  - 处理：Astra 复核通过。主语前超长定语，多余的“一个”

- 英文：When people are asked about a topic they know very little about (“What is your probability that the temperature in Bangkok will exceed 100° tomorrow at noon?”), the judged probabilities of the event and its complement add up to less than 100%.
  - 原译：当人们被问到一个自己所知甚少的话题时（“你认为明天中午曼谷的气温超过 100 华氏度的概率是多少？”），他们判断的这个事件的概率和它的对立面的概率，加起来不到 100%。
  - 现译：问到人们所知甚少的话题时（“你认为明天中午曼谷的气温超过 100 华氏度的概率是多少？”），他们对这个事件和它的对立面分别判断的概率，加起来不到 100%。
  - 处理：复核后重写。“当……被问到……时”，“的”字连串 复核：complement 指该事件的对立事件；“对立面”不够准确，改写后又省去了明确的所属关系，容易含混。

- 英文：A follow-up of attendance revealed that students who had paid the full price for their tickets were more likely to attend, especially during the first half of the season. Missing a show one has paid for involves the unpleasant experience of closing an account in the red.
  - 原译：后续对观剧情况的跟踪发现，买全价票的学生更可能去看演出，尤其是在演出季的前半段。错过一场已经付了钱的演出，就要体验在亏损状态下关闭一个账户的不愉快。
  - 现译：后来跟踪学生的观剧情况，发现买全价票的学生更可能去看演出，尤其是在演出季的前半段。错过一场已经付了钱的演出，就意味着要在亏损的状态下关闭一个账户，这种体验令人不快。
  - 处理：Astra 复核通过。名词化主语“后续对……的跟踪”，“体验……的不愉快”直译

- 英文：Christopher Hsee introduced the terminology of joint and separate evaluation, and formulated the important evaluability hypothesis, which explains reversals by the idea that some attributes become evaluable only in joint evaluation:
  - 原译：这个假说用这样一个观点来解释逆转：有些属性只有在联合评估中才变得可以评估：
  - 现译：这个假说认为，有些属性只有在联合评估中才变得可以评估，并以此解释逆转：
  - 处理：按复核意见修改。直译 explains ... by the idea 复核：同一句中连续使用两层冒号，末尾冒号又引出文献，层次不清；应保留文献前的冒号，调整前面的解释句式。

- 英文：We probably would not use it today, but the example was written in the 1970s, when sensitivity to group labels was less developed than it is today.
  - 原译：放在今天，我们大概不会用它，但这个例子是在 20 世纪 70 年代写的，那时人们对群体标签的敏感程度不如现在。
  - 现译：放在今天，我们大概不会用它，但这个例子是在 20 世纪 70 年代写的，那时人们对群体的称呼还不像现在这样敏感。
  - 处理：复核后重写。名词化“敏感程度” 复核：比较关系和语气保留正确，但沿用了“群体标签”；术语表规定 label 作名词时使用“名称”，不用“标签”。

- 英文：Jen was not judged twice as unhappy if she lived miserably for 60 years rather than 30, but she was regarded as considerably happier if 5 mildly miserable years were added just before her death.
  - 原译：如果珍痛苦地活了 60 年，而不是 30 年，人们并不会因此认为她的不幸翻了一倍；但如果在她临死前加上 5 年轻度痛苦的日子，人们就会认为她幸福得多。
  - 现译：把珍痛苦的一生从 30 年延长到 60 年，人们并不认为她的不幸翻了一倍；但如果在她临死前加上 5 年稍有些痛苦的日子，人们就会认为她幸福得多。
  - 处理：Astra 复核通过。照搬 rather than，“5 年轻度”容易读成“年轻”

- 英文：A pure measure of life evaluation used in the Gallup surveys is the Cantril Self-Anchoring Striving Scale, in which the respondent rates his or her current life on a ladder scale in which 0 is “the worst possible life for you” and 10 is “the best possible life for you.”
  - 原译：盖洛普调查使用的一种纯粹的生活评价测量，是坎特里尔自我锚定奋斗量表：受访者在一个阶梯式的量表上给自己当前的生活打分，0 代表“你可能过上的最差的生活”，10 代表“你可能过上的最好的生活”。
  - 现译：盖洛普调查里有一个单纯测量生活评价的工具，就是坎特里尔自我锚定奋斗量表：受访者在一个阶梯式的量表上给自己当前的生活打分，0 代表“你可能过上的最差的生活”，10 代表“你可能过上的最好的生活”。
  - 处理：复核后重写。主语前“的”字长定语 复核：“一种纯粹的生活评价测量，叫……量表”搭配不当，也没有说明 pure 的含义。上下文是在区分单纯衡量生活评价的工具与混合测量满意度、体验幸福感的工具。

- 英文：The language suggests that people should anchor on what they consider possible for them, but the evidence shows that people all over the world have a common standard for what a good life is, which accounts for the extraordinarily high correlation (r = .84) between the GDP of countries and the average ladder score of their citizens.
  - 原译：这种措辞暗示，人们应该以自己认为对自己来说可能的生活为锚，但证据表明，全世界的人对什么是好生活有一个共同的标准，正因如此，各国的 GDP 与其国民的平均阶梯得分之间才有极高的相关（r = 0.84）。
  - 现译：这种措辞暗示，人们应该以自己觉得可能过上的生活为锚，但证据表明，全世界的人对什么是好生活有一个共同的标准，正因如此，各国的 GDP 与其国民的平均阶梯得分之间才有极高的相关（r = 0.84）。
  - 处理：Astra 复核通过。“对自己来说”套话，定语绕口

- 英文：The economist was Alan Krueger of Princeton, noted for his innovative analyses of unusual data.
  - 原译：那位经济学家是普林斯顿大学的艾伦·克鲁格，他以对不寻常的数据作出创新性分析而闻名。
  - 现译：那位经济学家是普林斯顿大学的艾伦·克鲁格，他以对不寻常数据的创新分析而闻名。
  - 处理：复核后重写。“对……作出……分析”虚化动词 复核：“创新地分析”搭配生硬；原译“作出创新性分析”准确自然，不能仅因使用名词结构就改掉。

- 英文：Norbert Schwarz, a social psychologist who was also an expert on survey method and had contributed experimental critiques of well-being research, including the experiment on which a dime left on a copying machine influenced subsequent reports of life satisfaction.
  - 原译：诺伯特·施瓦茨，一位社会心理学家，他也是调查方法方面的专家，曾对幸福感研究作过一些实验性的批评，其中包括那个复印机上留下一枚 10 美分硬币就影响了随后生活满意度报告的实验。
  - 现译：诺伯特·施瓦茨，一位社会心理学家，他也是调查方法方面的专家，曾用实验对幸福感研究提出过一些批评，其中包括这样一个实验：复印机上留下的一枚 10 美分硬币，就影响了人们随后报告的生活满意度。
  - 处理：Astra 复核通过。名词前超长定语，“作过……批评”

- 英文：For a number of years I have been one of several Senior Scientists associated with the efforts of the Gallup Organization in the domain of well-being.
  - 原译：多年来，我一直是盖洛普公司在幸福感领域研究工作的几位资深科学家之一。
  - 现译：多年来，我一直是参与盖洛普公司幸福感研究的几位资深科学家之一。
  - 处理：Astra 复核通过。定语搭配生硬，照搬 in the domain of

- 英文：Jing Xu and Norbert Schwarz have found that the quality of the car (as measured by Blue Book value) predicts the owners’ answer to a general question about their enjoyment of the car, and also predicts people’s pleasure during joyrides.
  - 原译：Jing Xu 和诺伯特·施瓦茨发现，汽车的品质（按二手车《蓝皮书》的估价衡量）能预测车主被笼统地问到有多享受这辆车时给出的回答，也能预测人们开车兜风时的愉快程度。
  - 现译：Jing Xu 和诺伯特·施瓦茨发现，汽车的品质（按二手车《蓝皮书》的估价衡量）既能预测车主怎样回答“你有多享受这辆车”这个笼统的问题，也能预测人们开车兜风时的愉快程度。
  - 处理：复核后重写。宾语前长定语，带被动 复核：“发现，笼统地问车主……”缺少“时”等衔接，提问动作与研究结论混在一起；两个预测对象也宜分开表述。

- 英文：Progress has been especially rapid in the UK, where the use of measures of well-being is now official government policy.
  - 原译：英国的进展尤其迅速，在那里，使用幸福感测量如今已是政府的正式政策。
  - 现译：英国的进展尤其迅速，如今，采用幸福感指标已经成了英国政府的正式政策。
  - 处理：复核后重写。照搬 where 从句“在那里” 复核：“使用幸福感测量”搭配生硬；measures 在这里指衡量幸福感的指标或工具，不宜直接译成测量活动。

- 英文：Layard is among the prominent economists and social scientists who have been drawn into the study of well-being and its implications.
  - 原译：许多著名的经济学家和社会科学家被吸引来研究幸福感及其意义，莱亚德是其中之一。
  - 现译：一些著名的经济学家和社会科学家被吸引来研究幸福感及其影响，莱亚德是其中之一。
  - 处理：复核后重写。不必要的被动句 复核：沿用了原译增添的“许多”，原文没有这一数量限定；implications 指相关影响或启示，笼统译成“意义”不够准确。

