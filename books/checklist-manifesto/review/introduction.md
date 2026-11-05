# 引言（introduction）审校记录

全章 55 个块、7 条注释，另有 2 条译者注，中英逐块对应（`site.py status` 显示 55/55、7/7）。这一章是全书的样章，译文风格以它为准。

## 1. 译者自检

- 执行者：sample translation agent（Opus 5.5），译者本人。
- 范围：全章 55 块（1 个标题、54 个段落）和 7 条注释，对照原文逐段检查漏译、增译、否定、数字、人名、术语和注释；译完后又顺着中文读了一遍，改动的地方都回查了英文。
- 检查：`site.py status` 显示 55/55、7/7；`site.py check` 的草稿构建通过（字体子集还没有生成，构建提示缺字，这本书还没有运行过 `site.py fonts`）；`tools/term_consistency.py` 查了 29 处术语和人名，没有不符合约定译法的块；正文没有破折号，也没有体例禁用的对比句式；注释 2 至 7 的出处和英文逐字相同，[^t1]、[^t2] 在正文里都有引用。
- 发现并修改：
  - 第 13 块 “The description was pretty close, it turned out. The other guy at the costume party, John later learned”：初稿“后来才知道……约翰事后得知”两次说“后来”，改为“事实证明，这个说法八九不离十。约翰后来得知……”。
  - 第 37 块 “Much of the world and universe … outside our understanding and control”：初稿“世界和宇宙的大部分”说重了，much of 是“很多”，改为“世界和宇宙中有很多东西”。
  - 第 52 块 “People spend years of sixty, seventy-, eighty-hour weeks”：初稿加了“甚至”，原文只是把三个数字排在一起，删去，改为“每周工作 60、70、80 个小时”。
  - 第 52 块 “what is striking about John’s cases”：初稿“引人深思”偏离了 striking（值得注意），改为“约翰的病例有一点值得注意”。
  - 第 36 块 “We talk about our great saves but also about our great failures”：初稿“最了不起的那些救回来的病例”“最惨痛的失败”把 great 译成了最高级，改为“那些漂亮地救回来的病例”“那些惨痛的失败”。救回来的病例按术语表 great saves 的译法。
  - 第 35 块 “They’d not only nearly killed the man but also failed to recognize how”：初稿“当时没能看出是怎么回事”，改为“而且自己都没能看出问题出在哪里”，说清楚没看出来的是手术团队自己。
  - 第 18 块 “a fleshy mouse-size mass”：初稿“一团老鼠大小的肉”像在说一块肉，改为“一个老鼠大小的肉质肿块”；同一块的 “And there on the images it was” 初稿用了“果然”，原文没有预料之中的意思，改为“片子上看得清清楚楚”。
  - 第 18 块 “in his late forties”：初稿“四十七八岁”比原文精确，改为“年近五十”。
  - 第 5、7 块 “nurses racing to get the surgical equipment set up”：初稿“护士们抢着把手术器械摆好”，“抢着”容易读成互相争抢，两处都改为“争分夺秒地准备手术器械”，保留原文两段话前后呼应的写法。
  - 第 48 块 “You see it in the 36 percent increase … the most common being simple administrative errors”：初稿用冒号把“从中也能看到”和后面的失误类型接在一起，读起来像看到的就是这些失误。拆成两句：“……增加了 36%，从中也能看到这一点。这些失误里最常见的，是简单的事务性差错……”；“在有缺陷的软件设计……里，也都能看到这一点”补上了“在……里”。
  - 第 36 块 “are often about the shock of the unexpected … and sometimes about regret over missed possibilities”：初稿“常常围绕……有时也关于……”前后搭配不一致，改为“常常讲的是……有时讲的是……”。
  - 第 42 块 “at home as a cardiac cripple”：初稿“作为一个心脏落下残疾的人度过余生”带翻译腔，改为“回家做个心脏残疾的人，度过余生”。
  - 第 41 块 “We didn’t know about the role of cholesterol, either, or genetics or smoking or diabetes”：初稿把一句拆成两半，读着啰嗦，改为“我们也不知道胆固醇、遗传、吸烟和糖尿病各自起什么作用”。
  - 第 47 块 “insurance company hassles”：初稿“刁难”带了原文没有的故意意味，改为“种种麻烦事”；第 49 块 “seems to cloud how we think about them” 初稿“没法看清它们”改为“没法冷静地思考它们”。
- 照体例处理的地方：
  - 人名：约翰（John）、塞缪尔·戈罗维茨（Samuel Gorovitz）、阿拉斯代尔·麦金太尔（Alasdair MacIntyre）在本章第一次出现时括注英文，之后只写中文，和 `review/terms/people-zh.tsv` 一致；注释里的人名照写英文。
  - 术语：ignorance 译“无知”，ineptitude 第一次出现写“无能（ineptitude）”，failures of ignorance 译“无知造成的失败”；necessary fallibility 写“必然的易错”，加引号并括注原文；eptitude 写“有能”（eptitude），加译者注 [^t2] 说明构词；Code Blue 写“蓝色代码（Code Blue）”，加译者注 [^t1]；asystole 原文正在解释这个词，写“心脏停搏（asystole）”；know-how 译“知识和本领”，expertise 译“专业能力”，avoidable failures 译“可以避免的失败”。
  - 单位：about two hundred pounds 写“大约 200 磅（约 90 公斤）”，two-inch 写“两英寸（约 5 厘米）”，more than a foot 写“一英尺（约 30 厘米）还多”。伤口只有两英寸，刀却刺进去一英尺多，这个对比对读者要紧，所以都括注了公制。
  - 数字：一到十和约数用汉字（两天、五秒钟、四个小时、十几种、十多年、上千处），11 以上的确数用阿拉伯数字（15 分钟、20 分钟、90 分钟、100 倍），百分比写 100%、50%、30%、36%。
  - 原文的破折号按意思改成冒号、逗号或括号，或者另起一句。
  - 原文表示强调的斜体保留：“这下，他们*真的*要冲进手术室了”“*这*才让他烧心”。第 49 块用斜体指称词语本身的 *ineptitude*、*negligence*、*heartlessness*，中文改用引号：“无能”“失职”“冷血”。
  - 第 47 块 “It is not money or government … It is the complexity”、第 50 块 “has not been to punish failure but instead to encourage” 两处英文都是先否定一种说法、再给出另一种的对照结构，中文按体例换成直接的说法：“虽然都有影响，但根源都不在这里。根源在于……”“是鼓励人们积累更多经验、接受更多训练，而不去惩罚失败”。
  - 注释：开头引号里的词句译成中文，和正文里标记前面的中文对应，例如注释 2 “20 世纪 70 年代”、注释 4 “超过这个时间，存活率”、注释 7 “增加了 36%”；出处保留英文，注释 3 的 See also 译“另见”；注释 1 按术语表给定的译法。注释 1 在原文里标在句号后面，中文也放在句号后面。
- 未决（供用户确认风格时参考）：
  - 第 7 块 “a whole bottle of Betadine antiseptic”：Betadine 是聚维酮碘的品牌名，中国大陆通称“碘伏”，译作“一整瓶碘伏消毒液”，品牌名没有保留。
  - 第 28 块 “a bolus of epinephrine … adrenalin”：英文同时给出学名和俗名，中文两个词都是“肾上腺素”，只写一次。
  - 第 2 块 “We were trading war stories”：war stories 是惯用语，指从业中的惊险经历，按意思译作“我们互相讲起从医以来的惊险经历”。后面的 “since Vietnam” 是真的战争，译作“越战”。
  - 第 10 块 “Crap.” 译作“该死。”，第 32 块 “that’s how states execute prisoners” 译作“美国各州处决犯人，用的就是这个办法”，补出了“美国”。
  - 第 55 块，引言的最后一句 “It is a checklist.” 译作“那就是清单。”，另一个可选的说法是“那就是一张清单。”，后者更突出这个东西的简单。
  - 第 44 块 eptitude 的译法“有能”和译者注 [^t2] 的写法，以及 Code Blue 的译者注 [^t1]，样章认可后各章照此处理。
  - 建议在术语表里补两条，留给主会话决定：heart attack 全书统一写“心脏病发作”（本章正文出现 9 次）；原文用斜体指称词语本身的地方，中文改用引号。**已定**：术语表核心概念表规定 heart attack 写“心脏病发作”，heart attack patients 写“心脏病发作的病人”；“全书统一的写法（译完后定）”的“指称词语本身的斜体”一条规定中文改用引号。本章按这两条执行，见第三轮。

## 原文疑点

| 位置 | 原文 | 处理 |
| --- | --- | --- |
| 第 17 块，注释 1 | EPUB 里 “his heart suddenly stopped.*” 只有星号，没有注释文字 | 已记在 `review/source.md`：注释文字按美国版第 4 页的脚注补回，英国版纸质书没有核对。中文按补回的文字翻译 |
| 第 6 块 | His blood pressure was barely detectible | detectible 是 detectable 的异体拼写，不算错误，`en/` 照原文保留，意思照常翻译 |
| 第 34 块 | they also gave intravenous calcium and inhaled doses of a drug called albuterol, which act more quickly. The potassium levels dropped rapidly. | 第三轮审校者指出：静脉钙剂的作用是保护心肌，并不降低血钾；美国急诊医师学会（ACEP）的药理资料写雾化沙丁胺醇约 30 分钟内起效，胰岛素加葡萄糖约 15 分钟内开始降钾，沙丁胺醇并不更快。也有研究（PubMed 10084465）测到吸入沙丁胺醇 3 到 5 分钟后血钾就开始下降，钙剂对心脏的保护也是几分钟内见效，原文的说法大体站得住。不影响读者理解这次抢救，正文照原文译，不加译者注 |

## 2. 双语审校

- 执行者：另一个独立上下文的 agent（Opus 5.5），没有参与翻译。审校意见由编辑 agent（Opus 5.5）逐条对照英文和中文核实后处理。
- 范围：全章 55 块（1 个标题、54 个段落）和 7 条注释、2 条译者注，对照原文逐块检查意义、数字、单位换算、人名、术语、注释格式和体例。
- 发现：13 条；核实后采纳 13 条（其中 4 条按另拟的改法修改），不采纳 0 条。意义问题 5 条，表达问题 7 条，术语 1 条：
  - 第 48 块 “the most common being simple administrative errors, like missed calendar dates and clerical screwups, as well as errors in applying the law”：适用法律时出的错和事务性差错是并列的两类，原译把它接在“比如”的例子后面，像是第三个例子。采纳，改为“是简单的事务性差错（比如错过日程上的期限、文书上出了岔子），以及适用法律时出的错”。
  - 第 49 块 “we are happy to have people simply make their best effort”：原译“心满意足”说重了，“根本还不存在”的“根本”是原文没有的强调，定语也太长。采纳，另拟改法：“如果在某种情况下，还没有人知道怎样做最好，那么大家只要尽力而为，我们也就满意了。”审校者建议的“我们就能接受”比 happy 弱，没有用。
  - 第 7 块 “So now they *were* crashing into the operating room”：原译“真的要冲进手术室了”读起来像将要发生，和后面已经在做的动作对不上，也少了和第 5 块呼应的“火速”。采纳，改为“这下，他们*真的*火速冲进了手术室”。
  - 第 13 块 “The other guy at the costume party”：原译“另一个人”看不出指的是和病人起冲突、捅了他的人。采纳，改为“化装派对上跟他起冲突的那个人扮的是一名士兵，还带着一把刺刀”。
  - 第 42 块 “we had little idea of how to treat it”：原译“不太知道”说轻了，和上一段同样的 had little idea（“几乎一无所知”）不一致。采纳，改为“一旦有人心脏病发作，我们也几乎不知道该怎么治”。
  - 第 52、53 块 “best-trained surgeons”“most highly trained”：“训练最有素”拆开了固定说法“训练有素”。采纳，另拟改法：两处都写“训练最扎实”，第 53 块和后面的“技术最高超、工作最勤奋”句式一致；审校者为第 53 块建议的“受过最严格训练”没有用。
  - 第 52 块 “Far from it.”：原译“差得远呢”容易读成个人能力还差得远，意思正好相反。采纳，并入前句写“个人能力都远远算不上我们的主要困难”。
  - 第 49 块 “gave these failures so unmerciful a name”：原译“一个这样不留情面的名字”语序别扭。采纳问题，另拟改法：只改成“这样一个不留情面的名字”，名字“无能”仍放在句子后面，保留原文用破折号把这个词放在句末的效果。
  - 第 23 块 “But John had the patient’s abdomen completely open … and he told the anesthesiologist so”：原译“被约翰完全打开”是翻译腔的被字句，“他也这样告诉了”的“也”没有对应。采纳，改为“可约翰已经把病人的腹腔完全打开了，里面没有出血，他把这一点告诉了麻醉科医生”。
  - 第 53 块 “not to mention demoralizing and frustrating”：原译缺主语。采纳，改为“更不用说它们有多让人泄气、多让人沮丧了”。
  - 第 37 块 “is—and will remain—outside our understanding and control”：“现在在”两个“在”相连。采纳，改为“现在超出我们的理解和掌控，将来也仍会如此”。
  - 第 47 块 “our greatest difficulties and stresses in medicine … the enormous strains”：“我们在医学上”按术语表补成“我们医生”；stresses 和 strains 原来都译“压力”，后一处改为“沉重负担”，也和第 53 块的“知识……也成了我们的重负”相应。采纳。
  - 第 27 块 “heard good air movement on both sides of the chest”：“两侧胸腔的呼吸音都很好”不像临床说法。采纳，另拟改法：写“两侧呼吸音都很清晰”。审校者建议的“清楚”偏口语，排除气胸要看两侧都听得到呼吸音，“清晰”更贴近。
- 审校者的总体判断：译文整体质量很高，可以作为全书的样章。`site.py status` 显示 55/55 块、7/7 条注释，标题和术语表一致；事实、数字和单位换算都核对无误（200 磅约 90 公斤、两英寸约 5 厘米、一英尺约 30 厘米、100 倍、90 分钟、30%、45%、60%、36%、2004 年到 2007 年）；人名首次出现都括注了英文，写法和 `people-zh.tsv` 一致；术语按术语表处理；7 条注释的标记位置、引语和英文出处都没有问题；两条译者注准确、必要；正文没有破折号和禁用句式。发现的意义问题都是细节，其余是可以更顺的表达，都只需局部修改。译者列为待定的“该死”“那就是清单”“碘伏”三处，审校者认为可以保留。

## 3. 中文通读

- 执行者：编辑 agent（Opus 5.5）。
- 范围：采纳审校意见后，顺着中文从标题读到第 55 块和全部注释，检查连贯、重复、指代和全章的人名、术语是否一致。
- 发现并修改（每处都回查了英文）：
  - 第 52 块 “The capability of individuals is not proving to be our primary difficulty”：句首的“事实证明”和第 46 块 “is proving brutally hard” 的“事实证明”只隔几段，读着重复。第 52 块改为“现在看来”，is proving 表示从经验中显出来的情况，意思不变。
  - 第 40 块 “We knew little about what caused them or what could be done to remedy them”：原译“知之甚少，也不太知道……”把同一个 knew little 说成一重一轻，和第 42 块的改动是同一个问题。改为“疾病是什么引起的，能做些什么来医治，我们都知之甚少”。
- 检查过、没有改的地方：约翰、戈罗维茨、麦金太尔首次出现括注英文，之后只写中文；asystole 写“心脏停搏”，cardiac arrest 写“心搏骤停”，和英文的区分一致；第 3 块“创伤急救团队”和第 6 块“创伤团队”指同一个团队，第二次用简称，读者不会误会；第 48 块三次“看到这一点”照原文 You see it 的排比保留。
- 检查：`site.py status` 仍显示 55/55、7/7；正文没有破折号，也没有体例禁用的对比句式；`tools/term_consistency.py` 没有发现不符合约定译法的块。第 1 节“照体例处理的地方”引的“这下，他们*真的*要冲进手术室了”已按第 2 节的审校意见改为“这下，他们*真的*火速冲进了手术室”。

## 状态

没有未解决的意义问题。第 1 节列出的待定处理（“该死”“那就是清单”“碘伏”、eptitude 和 Code Blue 的译者注、两条术语表建议）属于风格和全书体例的选择，留给用户确认样章时决定（其中两条术语表建议后来已经由术语表定下，见第 1 节）；阅读器校样（第 4 节）还没有做。

## 第三轮：GPT-6 Astra 独立审校

- 审校者：GPT-6 Astra，通过 Codex 运行，只读，和译者属于不同的模型家族。
- 发现：6 条。逐条找到中英文对应的句子，读过上下文后核实：成立并修改 4 条，不成立 2 条。6 条里 5 条是表达问题，1 条是数字问题，没有发现意思译错的地方。
- 成立并修改：
  - 第 43 块 “prescribing a statin to lower cholesterol and inflammation”：原译“开他汀类药物降低胆固醇和炎症”，“降低”和“炎症”搭配不当。改为“开他汀类药物降低胆固醇、减轻炎症”。审校者建议的写法多了“水平”两个字，没有用。
  - 第 48 块 “and as a result so has our struggle to deliver on them”：原译“相应地，要把它们兑现出来也越来越吃力”，“兑现”能搭配承诺，搭配不了知识和本领。审校者建议“要把这些知识和本领用好”，同一句前面已经写了“知识和本领”，所以改为“相应地，要让它们真正发挥作用也越来越吃力”。第 47 块的“兑现科学的承诺”对应 making good on its promise，搭配没有问题，保留。
  - 第 52 块 “It is not clear how we could produce substantially more expertise than we already have.”：原译“我们很难想象，还能怎样培养出比现在多得多的专业能力”，“能力”一般说强弱，不说多少。审校者建议整句改写为“还能怎样在现有基础上大幅提高人们的专业能力”，改动大于需要，这里把“多得多”改为“强得多”：“我们很难想象，还能怎样培养出比现在强得多的专业能力。”
  - 第 53 块 “the volume and complexity of what we know has exceeded our individual ability to deliver its benefits correctly, safely, or reliably”：原译“我们掌握的知识数量庞大、复杂万分，个人已经没有能力正确、安全、可靠地把它的好处兑现出来”，“把好处兑现出来”是 deliver 的字面译法，“复杂万分”比原文说得重，原文“超出了个人的能力”这层关系也没有译出来。审校者建议的写法太长，又把一件事拆成“运用这些知识、发挥其效用”两件。改为“我们掌握的知识数量之多、复杂程度之高，已经超出了我们每个人的能力，谁都没法单靠自己正确、安全、可靠地让这些知识造福于人”。
- 不成立，保留原译：
  - 第 42 块 “spend the rest of his or her life at home as a cardiac cripple”，原译“回家做个心脏残疾的人，度过余生”。审校者认为生硬，建议“回到家里，余生都因心脏受损而活动受限”。cripple 是很重的说法，作者用它说明当年心脏病发作的病人前景多么黯淡；“残疾”保留了这份分量，意思也清楚。建议的改法换成了平淡的临床描述，丢了原文的口气。属于风格选择，保留原译。
  - 第 43 块 “at least a dozen effective ways”，原译“至少有十几种有效的办法”。审校者认为 a dozen 是 12，应写“至少有 12 种”。这里的 a dozen 是整数概数，作者随后举的例子是六种；写成“12 种”反倒像一个确切的统计。按全书统一的写法，带“十几”的约数用汉字，第 1 节也把“十几种”列为约数。保留原译。
- 按全书统一的写法修改：3 处，都回查了英文。
  - 第 41 块 “Even as recently as the 1950s, we had little idea of how to prevent or treat them”：按“其他说法”一条，had little idea 写“几乎不知道”或“知之甚少”，原译“还几乎一无所知”改为“还知之甚少”。第 42 块的“我们也几乎不知道该怎么治”已经符合，不改。
  - 第 44 块 “heart attack patients undergoing cardiac balloon therapy should have it done within ninety minutes of arrival at a hospital”：按核心概念表 heart attack patients 写“心脏病发作的病人”，原译“接受心脏球囊治疗的心脏病发作病人，应该在到达医院后 90 分钟内完成治疗”改为“心脏病发作的病人如果接受心脏球囊治疗，应该在到达医院后 90 分钟内进行”，语序调整后句子更顺。“完成治疗”改为“进行”的原因见下面“对英文原文的疑问”。
  - 第 49 块 “What do you mean half of heart attack patients don’t get their treatment on time?”：同一条，原译“什么叫一半的心脏病发作病人没能及时得到治疗？”改为“什么叫心脏病发作的病人有一半没能及时得到治疗？”。
  - 其余各条逐一核对过，本章已经符合：数字（两天、五秒钟、四个小时、十几种、十多年、上千处用汉字；15 分钟、20 分钟、90 分钟、100 倍、60、70、80 个小时用阿拉伯数字）；人名首次出现括注英文，注释里的人名照写英文；第 47 块的 we 补成“我们医生”；asystole 写“心脏停搏（asystole）”，cardiac arrest 写“心搏骤停”；sterile drapes 写“无菌单”；expert clinicians 写“临床专家”；best-trained、most highly trained 写“训练最扎实”；We knew little 写“知之甚少”；*ineptitude*、*negligence*、*heartlessness* 改用引号；an average hospital 写“一家普通的医院”，和 a random hospital 那一条无关；注释开头引号里的词句和正文对应。第 1 节留给主会话决定的两条术语表建议已经由术语表定下，在原处注明“已定”。
- 对英文原文的疑问：审校者提出两条。
  - 第 34 块，静脉钙剂和吸入沙丁胺醇“起效更快”，随后血钾迅速下降：审校者指出钙剂保护心肌，并不降低血钾，沙丁胺醇按指南约 30 分钟内起效。核实后认为原文的说法大体站得住（钙剂对心脏的保护几分钟内见效，也有研究测到吸入沙丁胺醇 3 到 5 分钟后血钾就开始下降），而且不影响读者理解这次抢救。按“原文疑点和译者注”一条，记入本记录的“原文疑点”表，正文照原文译，不加译者注。
  - 第 44 块和注释 4，“should have it done within ninety minutes” 和段末 “and get started” 的计时终点：审校者认为两处说法不一致。核实后认为英文前后一致：注释 4 和注释 5 的研究讲的都是 door-to-balloon time，也就是从进医院到第一次用球囊扩张血管的时间；have it done 指做上这项治疗，get started 指开始治疗，说的是同一个时间点。前后矛盾的是中文：原译“90 分钟内完成治疗”像是整个治疗都要在 90 分钟内结束，和段末的“然后开始治疗”对不上，已经改为“90 分钟内进行”（见上一条）。英文不算原文疑点，没有记入表里。
- 核实与修改：agent（Opus 5.5）。改完后运行 `python3 scripts/site.py status checklist-manifesto`，introduction 显示 55/55 块、7/7 条注释，块和注释都已翻译，块数和注释编号没有变化。`tools/term_consistency.py` 没有发现本章有不符合约定译法的块。中文仍然没有破折号，也没有禁用的对比句式。

## 补全后的改动

- 日期和执行者：2026-11-05，Claude（Opus 5.5）。用户提供了美国 Picador 版的 MOBI，比较方法和全书的结果见 [source.md](source.md) 的“用更好的来源补全（2026-11-05）”。英文的改动由 `tools/apply_us_edition.py` 完成，中文由人工修改。这一节写的块号都是改动以后的块号，写明“原来的”除外。
- 英文：第 52 块 “years of sixty, seventy-, eighty-hour weeks” 补上转换丢掉的连字符，改成 sixty-。意思不变，中文不改。
- 星号注释（注释 1）的文字和位置都和美国版相同，上面“原文疑点”里说只核对过扫描本的这一句，现在有了完整的美国版作依据。
- 块号没有变化。
- 复查：改完后 `python3 scripts/site.py status checklist-manifesto` 显示本节 55/55、7/7，全书 665/665；`python3 scripts/site.py check checklist-manifesto` 通过。

## 2. 双语审校（补全部分）

- 审校者：agent（Opus 5.5），2026-11-05。审校者没有参与这次补全和翻译，对照的是改动以后的 `en/` 和 `zh-cn/`；英文改动里涉及意思的地方，另外在美国 EPUB 的原文里查过。
- 方法：逐块对照英文读中文，核对意思、遗漏、数字、人名、术语、脚注和中文是否通顺，也查了有没有破折号和体例禁用的对比句式；合并和拆开的段落还核对了断处和接缝。
- 范围：第 52 块（英文补上 sixty- 的连字符）和注释 1（星号注释）。
- 结果：第 52 块中文“每周工作 60、70、80 个小时”和英文一致，补上连字符不影响中文；注释 1 的中文和美国版的文字一致，标记的位置也一致。
- 没有发现需要改的地方，本节没有修改。
- 复查：改完后 `python3 scripts/site.py status checklist-manifesto` 显示本节 55/55、7/7，全书 14 节都是 review，665/665；`python3 scripts/site.py check checklist-manifesto` 通过。
