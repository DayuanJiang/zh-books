# 后记 事后的三点想法（postscript）审校记录

全节 34 个块，原文没有注释，中文另加 1 条译者注 [^t1]；中英逐块对应（`site.py status` 显示 34/34）。双语审校后译者注增为 2 条，按出现顺序重新编号：第 6 块的新注是 [^t1]，第 20 块原来的 [^t1] 改为 [^t2]（见第 2 节）。

## 1. 译者自检

- 执行者：translation agent（Opus 5.5），译者本人。
- 范围：全节 34 块和 1 条译者注，从第 1 块到第 34 块对照原文逐段检查漏译、增译、否定、条件、数字和日期、行为主体、比较对象、术语义项、人名、斜体和脚注格式。另外运行了 `python3 scripts/site.py status fooled-by-randomness`（34/34）和 `tools/term_consistency.py`（全书检查 1431 处，本节没有缺少约定译法的块），用 CommonMark 渲染中英两个文件，各有 17 处斜体，没有露出的星号；也查过本节没有破折号，没有体例禁用的对比句式，中文里没有半角标点。块序号按 `site.py` 计，第 1 块是标题。
- 发现并修改：
  - 第 2 块 “listening to a speaker reciting *verbatim* his lecture notes makes me invariably daydream”：初稿“听演讲的人*一字不差*地照念讲稿”里，“听演讲的人”会被读成听众，改为“每当主讲人*一字不差*地照着讲稿念，我总会走神”。
  - 第 5 块 “a second, third, and a thousandth time”：初稿“第一千次”不合本书数字体例（11 以上的确数用阿拉伯数字），改为“第 1000 次”。
  - 第 10 块 “rather than pure skills in making optimal decisions” 和后面的 “we call that “corporate political skill.””：初稿把“我们管这叫‘公司政治手腕’”放在“做出最优决策的真本事，就谈不上了”后面，“这”像是指后半句。调整语序，让它紧跟“在公司里获得提拔的本事”。
  - 第 18 块 “something that appears to be very undesirable”：初稿“一件极不情愿的事”搭配不当，改为“而这似乎是件非常糟糕的事”。
  - 第 19 块 “a fixed and known timetable”：初稿“众所周知的时刻表”把 known 说成大家都知道，这里指乘客事先知道，改为“事先知道的”。
  - 第 20 块 “Buridan’s donkey”：初稿“布里丹（Buridan）之驴”把术语表的“布里丹之驴”拆开了，`term_consistency.py` 报了这一处，改为“布里丹之驴（Buridan’s donkey）”。
  - 第 21 块 “wealth causes them to increase their dependence”：初稿“更加受制于人”多出了“被别人控制”的意思，改为“财富似乎反倒让他们更不独立了”。
  - 第 23 块 “am enjoying an air unpolluted by persons squeezed by life”：初稿“一片没有被那些让生活挤压的人污染过的空气”定语太长，读不顺，改为“现在正享受着这里的空气，那些被生活压榨的人没来污染它”。
  - 第 25 块 “I was asked to write papers by the editors”：初稿“约我写文章”，和同一段 “the difference between writing a paper and writing a book” 的“写论文”对不上，改为“约我写论文”；后面的 “how long the piece should be” 仍写“文章该写多长”。
- 译法上的选择，供审校时核对：
  - 原文的 not X but Y 对比句，按体例换成直接的说法：第 13 块 “it is not society’s problem but that of the investors” 写“这是投资者的问题，和社会无关”；第 29 块 “It does not promise a fixed rate, but one that can fluctuate a bit” 写“它不承诺固定的汇率，它承诺的汇率可以先波动一点”；第 33 块 “he did not *summarize;* instead, he provided” 写“他并没有去*概括*；他给出的是”。
  - 术语：*inverse rule* 写“*反向法则*”，*empty suit* 写“*空架子*（empty suit）”，第一次出现时括注英文，让读者看出它和后文 good-looking suits（好看的西装）的关联；“quant” 写“宽客”（quant）；“corporate political skill” 写“公司政治手腕”；*ergodicity* 写“*遍历性*”；*law of large numbers* 写“*大数定律*”；monkey-on-the-typewriter problem 写“打字机前的猴子问题”；power law–style winner-takes-all effects 写“幂律式的赢家通吃效应”。
  - satisficer、maximizer 和 optimizer：*satisficer* 写“*满意即止者*”，和术语表 satisficing 的“满意即止”一致；*maximizer* 写“*最大化者*”；作者随后改用 optimizer，写“追求最优的人”。
  - generator：第 33、34 块 “the core generator of the idea”“what my generator is” 按术语表写“生成器”（“这套思想的核心生成器，也就是它的公理框架”“我自己的生成器”），保留作者借用数学说法的口吻。
  - 第 33 块希勒尔的话 “*Don’t do to others what you don’t want them to do to you; the rest is just commentary.*”：作者说这是他的转述，所以照他的英文直译成“*你不愿意别人对你做的事，就不要对别人做；其余的都只是注释*”。中文成语“己所不欲，勿施于人”意思相近，留给审校时斟酌。
  - 第 29 块 *Fluctuat nec mergitur*：照写原文并保留斜体，括注译作者给的英文 “it fluctuates but does not sink”，写“它随波起伏，但不会沉没”。
  - 第 22 块 “either as a cure or as Novocain”：写“要么起到治疗的作用，要么像奴佛卡因一样起到麻醉的作用”，把奴佛卡因的作用在正文里说出来。
  - 生活用语：“Money talks” 写“钱说了算”；the 7:42 local 写“7 点 42 分的慢车”，express trains 写“快车”；decaffeinated skim cappuccino 写“低因脱脂卡布奇诺”；the Stairmaster 写“踩楼梯机”；CEO 写“首席执行官”，和第三部分一致。
  - 第 7 块 “The rest is supposed to be philosophy.” 写“其余的，据说都只是哲学”，保留反讽。
- 人名：和 `review/terms/people-zh.tsv` 核对过，每人在本节第一次出现时括注英文：理查德·格拉索（Richard Grasso）、西蒙（Simon，原文只写姓，括注也只写姓）、希勒尔拉比（Rabbi Hillel，按表的 note 写法）；第二次提到希勒尔时只写中文。布里丹只出现在术语“布里丹之驴”里，括注整个术语。
- 数字：按术语表“全书统一的写法”。100 万美元、100 万次、每次 1 美元、2 亿美元、2003 年、10 到 20 倍、7 点 08 分、7 点 42 分、6 点 58 分、35 分钟、12 点 45 分、4 点 40 分、8 点、17 句、第 18 个、第 1000 次用阿拉伯数字；几千倍、几个百分点、三颗星、七个半小时、大约十年前、十几分钟（a dozen minutes）、一刻钟用汉字。交叉引用写“第 2 章”“第 8 章”“第 10 章”“第 11 章”。
- 未决：
  - 标题：术语表定的“后记 事后的三点想法”没有译出原题里的 in the Shower（淋浴时），正文第 2 块又说这些想法有的是在淋浴时想到的。是否改成“后记 淋浴时的三点想法”，请主会话决定；第一行暂时照术语表写。
  - 第 6 块的“第 8 章”：原文疑似记错章号（见下面“原文疑点”），目前照原文译出。是否加译者注，指明遍历性在第 3 章提出、第 9 章另有一小节，请主会话或双语审校决定。
  - 第 20 块的译者注 [^t1] 是否保留，请主会话决定。阅读器里中文读者读过第 11 章的“满意”和“足够”，到这里会看到另一种说法，所以译者倾向保留。
  - `book.json` 里本节的状态还是 `todo`，按分工由主会话修改。
  - 双语审校、中文通读和阅读器校样还没有做。

## 原文疑点

| 位置 | 原文 | 处理 |
| --- | --- | --- |
| 第 6 块 | because of what I called *ergodicity* in Chapter 8 | 第 8 章（“Too Many Millionaires Next Door”）没有讲遍历性。这个词是第 3 章提出的（“Mathematicians of probability give that a fancy name: *ergodicity.*”），第 9 章有一小节标题就是 “Ergodicity”。疑似章号写错，作者本意是第 3 章还是第 9 章无法确定，所以照原文译“第 8 章”，正文不加注。双语审校后改为加译者注 [^t1]，只写事实（第 8 章没有谈到遍历性，这个词在第 3 章提出，第 9 章有专门的一小节），不替作者确定本意；“第 8 章”仍照原文 |
| 第 20 块 | Chapter 11 discussed Simon’s satisficing as a blend of satisfying and maximizing | 第 11 章原文写的是 “the melding together of *satisfy* and *suffice*”，也就是满意加足够，和这里的“满意和最大化”不一致；同一句又拿 satisficer 和 maximizer 作对比，“由最大化合成”说不通。疑似作者记错。照原文译“说它是满意和最大化的合成”，加译者注 [^t1] 写出第 11 章的说法。双语审校后按出现顺序改编号为 [^t2] |
| 第 13 块 | pay someone $200 million … as they did with the New York Stock Exchange’s Richard Grasso in 2003 | 已核实：纽约州总检察长 2004 年的起诉公告说格拉索的薪酬方案是 1.875 亿美元，其中引发争议的递延薪酬是 1.395 亿美元；2003 年的纽约证券交易所是会员所有的非营利机构，没有严格意义上的股东。2 亿美元是约数，“股东”是作者顺着上文的说法。不影响论点，照原文译“2 亿美元”“股东”，不加注 |
| 第 10 块 | As a matter a fact, they are often *empty suits.* | 漏了 of，应为 As a matter of fact。按这个意思译“事实上” |
| 第 19 块 | the New York area Metropolitan Transit Authority | 纽约地区公共交通机构的正式名称是 Metropolitan Transportation Authority（MTA）。不影响意思，按通常的中文名译“大都会运输署” |

## 2. 双语审校

- 执行者：另一个独立上下文的 agent（Opus 5.5），没有参与翻译。
- 范围：对照英文逐块读完全节 34 块和译者注 [^t1]（现在的 [^t2]），核对了意思、数字和金额、人名、术语、交叉引用、斜体和格式，也检查了破折号、体例禁用的对比句式和半角标点，并运行 `python3 scripts/site.py status fooled-by-randomness` 确认 34/34。审校者没有改动文件，发现交给编辑逐条核实后处理。
- 发现：22 条；核实后采纳 21 条，不采纳 0 条；另有 1 条（标题）意见成立，按分工交主会话处理。编辑逐条对照了英文和中文，每条指出的问题都确实存在，所以没有不采纳的，其中几条换了改法。
  - 第 14 块 “We can’t even know that he didn’t destabilize the economy by increasing the risk of future inflation.”：采纳，换了改法。原译“没法确定，他没有因为加大了未来通胀的风险而破坏经济的稳定”里，“没有因为……而……”会被读成“他破坏经济稳定，原因和通胀风险无关”。原文的意思是我们排除不了他这样做过，改成“我们甚至没法排除这样的可能：他加大了未来通胀的风险，反倒破坏了经济的稳定。”
  - 第 33 块 “if Hillel could teach him the Torah while the student was standing on one leg”：采纳，换了改法。原译“能不能在他单腿站着的工夫里”分不清是谁单腿站着；审校者建议的“在自己单腿站着的工夫里”，“自己”仍可能指希勒尔。改成直接引语：“这让我想起希勒尔拉比（Rabbi Hillel）的故事。有个特别懒的人来问希勒尔：‘趁我单腿站着的工夫，您能把《托拉》教给我吗？’”（正文用的是双引号）
  - 第 7 块 “Lower-ranking persons in the enterprise are judged on both process and results”：采纳。原译“企业里级别较低的人，既按过程评判”读起来像这些人在评判别人，改成“评判企业里级别较低的人，既看过程，也看结果”，保留和前一句“按过程评判”“按结果评判”的呼应。
  - 第 10 块 “what they have is skill in getting promoted within a company”：采纳。“他们有的是……本事”在口语里会读成“多的是”，改成“他们具备的，是在公司里获得提拔的本事”。
  - 第 4 块 “it makes plenty of sense to pay individuals according to their contributions”：采纳。“道理再充分不过”是最高级，比原文重，和前半句“也许说得过去”的保留语气也不配，改成“是很有道理的”。
  - 第 6 块 “because of what I called *ergodicity* in Chapter 8”：采纳。编辑核对了英文：第 8 章全文没有 ergodic 这个词，第 3 章提出这个词，第 5 章用过一次，第 9 章有一小节标题就是 “Ergodicity”。本节已经为第 20 块第 11 章的出入加了译者注，这里也加一条 [^t1]，只写这几件事实，不替作者确定他本来指哪一章；正文“第 8 章”照原文。两条译者注按出现顺序重新编号，原来的 [^t1] 改为 [^t2]。
  - 第 5 块 “the cook at the company headquarters or the factory worker will exhibit their direct abilities with minimal uncertainty”：采纳，换了改法。原译“厨师或者工厂的工人，在展现自己的直接本事时，不确定性极小”照搬英文结构；审校者建议的“几乎不带什么不确定性就能看出来”多了“看出来”这层意思，改成“他们直接的本事显露出来时，几乎不带什么不确定性”。
  - 第 8 块 “he may be subjected to the monkey-on-the-typewriter problem”：采纳，换了改法。“他身上可能存在……问题”像在说他本人有毛病；审校者建议的“他的成功”是原文没有的词，改成“他的情形可能正属于打字机前的猴子问题”。
  - 第 21 块 “will uproot himself and change his official residence”：采纳，换了改法。“就会连根拔起”缺宾语；审校者建议的“把自己连根拔起”仍是直译，改成“就肯离开自己扎根的地方，把正式住所迁到别处”。
  - 第 30 块 “sometimes overreacting at the slightest joke”：采纳，换了改法。“开一个最小的玩笑”搭配不当；审校者建议的“小小的玩笑”和同一段后面的“一点小小的过失”、上一段的“小小的下跌”重复，改成“有时哪怕别人只开一句玩笑，你也会反应过度”。
  - 第 20 块 “(or lack of knowledge)” 和 “a *satisficer* instead of a *maximizer*”：采纳。“知识的缺乏”改成“不知情”，和第 19 块“假设他不知道各班车的发车时间”对得上；“当不成*最大化者*”改成“没法再当*最大化者*”，说明他原先正是在追求最大化。
  - 其余 10 条照建议改，或只动了个别字：第 2 块写“有的是我淋浴时想到的，有的是在我听过的那几场无聊的哲学讲座上想到的”；第 11 块 “to be taller than average” 写“个子比一般人高”；第 12 块 “The problem is as old as leadership.” 写“自从有了领导者，就有了这个问题。”；第 19 块 “about every, say, thirty-five minutes” 写“他只知道火车大致多久一班，比如说，大约每 35 分钟一班”；第 21 块 “the internal treadmill effects of constantly trying to improve on their consumption of goods by seeking higher and higher levels of sophistication” 写“不停地追求越来越讲究的东西，想让自己的消费一再升级”；第 21 块 “wealth causes them to increase their dependence” 写“财富似乎反倒让他们更不自由了”，和前半句“能自由选择住在哪里”呼应；第 23 块 “some people might be involuntarily turned into optimizers” 写“有些人可能身不由己，成了追求最优的人”；第 29 块 “It does not promise a fixed rate, but one that can fluctuate a bit before the bank starts intervening.” 写“它不承诺汇率固定不变：汇率可以先波动一点，然后央行才出手干预。”；第 30 块 “Say you always have the same threshold of reactions.” 的“假如”改成“假设”，这一句本身没有结果分句；第 32 块 “in spite of the insults” 写“尽管我没少骂 MBA”，insults 比“挖苦”重。
  - 标题 “Postscript: Three Afterthoughts in the Shower”：意见成立，原题的 in the Shower（淋浴时）没有译出，术语表这一行的英文也少了 in the Shower。第一行要照术语表“各节标题”写，术语表归主会话修改，所以本节暂不改，见“状态”。
- 审校者还核对了第 20 块的译者注（现在的 [^t2]），建议保留；第 2 章区分牙医的本事和俄罗斯轮盘赌，审校者核对过第 2 章原文，原文没有错。
- 审校者的总体判断：这一节译得扎实可靠，可以进入中文通读。全部 34 块和 1 条译者注逐块看完，没有漏译、增译或主次颠倒；100 万美元、2 亿美元、2003 年、35 分钟、17 句、第 18 个和各个钟点都对；人名照 people-zh.tsv 写，本节第一次出现时都括注了英文；反向法则、空架子、宽客、遍历性、大数定律、满意即止、布里丹之驴、打字机前的猴子、赢家通吃、幂律都和术语表一致；没有破折号、体例禁用的对比句式和半角标点。语气贴近样章，反讽和口语都保留了，例如“钱说了算”“其余的，据说都只是哲学”。要改的主要是第 14、33、7、10 块几处读者可能误解的地方，另有十几处照搬英文结构的生硬句子。标题和第 6 块的章号两件事请主会话决定。

## 3. 中文通读

- 执行者：编辑 agent（Opus 5.5）。
- 范围：采纳双语审校的修改以后，顺着中文从标题读到最后一段，再读两条译者注，检查连贯、重复、指代，以及人名和术语前后是否一致。
- 发现并修改（每一处都回查了英文，意思没有变）：
  - 第 12 块 “Our attribution of heroism to those who took crazy decisions but were lucky enough to win shows the aberration”：首句改成“自从有了领导者，就有了这个问题”以后，后面“这就暴露出这种反常”里的“这种”前面没有可指的东西，改成“这就暴露出其中的反常”，冒号后面照旧解释这种反常是什么。
  - 第 11 块 “We end up with a mildly wealthy, but fired, executive”：“小有财富、但被解雇了的高管”用顿号接“但”，读着别扭，改成“小有财富却被解雇了的高管”。
  - 第 23 块 “To go from Munich to Milan, I picked the seven-and-a-half-hour train instead of the plane, which no self-respecting businessperson would do on a weekday, and am enjoying an air unpolluted by persons squeezed by life.”：分号后面的“现在正享受着这里的空气”没有主语，紧挨着的主语是“商务人士”，可能读成商务人士在享受空气。原文的主语是 I，补上“我”。
- 检查过、保留原样的：
  - 第 14 块两处“套上”对应原文两处 fit（fit a theoretical explanation、easy to fit retrospectively），保留这个重复。
  - 第 21 块 “increase their dependence” 写“更不自由”，第 24 块 “rich but as dependent as a slave” 写“像奴隶一样受制于人”：两处英文的说法和上下文不同，前一处对应“自由选择住在哪里”，后一处有“奴隶”作比，分别保留。
  - 第 33 块希勒尔的话照作者的英文直译成“*你不愿意别人对你做的事，就不要对别人做；其余的都只是注释*”。作者说这是他的转述，译者自检时留给审校斟酌的成语“己所不欲，勿施于人”就不换了。
  - 人名：理查德·格拉索（Richard Grasso）、西蒙（Simon）、希勒尔拉比（Rabbi Hillel）只在第一次出现时括注，第二次提到希勒尔只写中文；术语“空架子”“宽客”“反向法则”“公司政治手腕”“遍历性”“大数定律”“满意即止”“追求最优的人”“最大化者”“生成器”全节写法一致。
- 修改后的检查：`python3 scripts/site.py status fooled-by-randomness` 显示 postscript 为 34/34；用 `framework/tools/book.py` 的 `compile_chapter` 编译本节，34 个单元、2 条译者注 t1 和 t2 都能解析；全节没有破折号，没有体例禁用的对比句式，中文旁边没有半角标点；`tools/term_consistency.py` 全书检查 1707 处，没有报出本节的块。`python3 scripts/site.py check fooled-by-randomness` 的草稿构建通过，本节状态还是 `todo`，没有进入构建。

## 状态

- 没有未解决的意义问题。第 6 块的章号和第 20 块 satisficing 的说法都是原文的出入，已经照原文译出并各加一条译者注，记在“原文疑点”里。
- 需要主会话处理的：
  - 标题：建议把术语表“各节标题”里 postscript 一行的英文改成 Postscript: Three Afterthoughts in the Shower，中文改成“后记 淋浴时的三点想法”，再把本节第一行改成同样的写法。本节第一行暂时照术语表写“后记 事后的三点想法”。
  - `book.json` 里本节的状态还是 `todo`，请按流程修改。
- 请用户决定的：两条译者注 [^t1]、[^t2] 是否保留。编辑倾向于保留，理由是中文读者照着章号去找会找不到，或者会看到和第 11 章不一样的说法。
- 还没做的：阅读器校样（第 4 节）；发布前运行 `python3 scripts/site.py fonts fooled-by-randomness`。

## 第三轮：GPT-6 Astra 独立审校

- 审校者：GPT-6 Astra，通过 Codex 运行，只读，和译者属于不同的模型家族。
- 发现：6 条。逐条找到中英文对应的句子，读过上下文后核实：成立并修改 4 条，不成立 2 条。
- 成立并修改：
  - 第 8 块 “By some argument, the boss of the company may be unskilled labor but one who presents the necessary attributes of charisma”：原译“公司的老板也许算是不需要技能的劳动力”，“不需要技能”说的是这份工作的要求；原文后半句 “but one who presents...” 说他本人具备个人魅力，前后对照的是这个人有没有本事，上一句也在说首席执行官的能力和业绩联系薄弱。审校者建议的“并没有什么专业本领”丢掉了 unskilled labor 这个劳动经济学的说法，和上文的厨师、工人、清洁工对不上，所以换了改法，改一个词：“公司的老板也许算是没有技能的劳动力”。
  - 第 5 块 “the cook at the company headquarters or the factory worker will exhibit their direct abilities with minimal uncertainty”：原译“他们直接的本事显露出来时，几乎不带什么不确定性”，“直接的本事”不通顺，“显露出来时不带不确定性”也别扭。审校者建议的“判断时几乎没有什么不确定性”多出了“判断”，换了改法：“他们的本事是直接显露出来的，几乎没有什么不确定性”。
  - 第 7 块 “owing to the repetitive aspect of their efforts, their process converges rapidly to results”：原译“由于他们做的事有重复性，他们的过程很快就会收敛到结果上”，一句里两个“他们”，“他们的过程”读着生硬。审校者建议的“结果很快就能可靠地反映过程的好坏”替作者解释了 converge，丢掉了作者借用的数学说法，所以保留“收敛到结果上”，前半句改成：“由于他们做的事一再重复，过程很快就会收敛到结果上”。
  - 第 20 块 “A slightly random schedule prevents us from optimizing and being exceedingly efficient, particularly in the wrong things.”：原译“时刻表稍微随机一点，就能让我们没法去优化，没法效率过高，尤其是在不对的事情上”，“没法效率过高”搭配不当，“不对的事情”容易读成做错事、做坏事。审校者建议的“事事追求最优”多出了“事事”，“时间安排”也和上文一直在说的时刻表脱节，所以换了改法：“时刻表稍微随机一点，我们就没法追求最优，没法把效率提得过高，尤其是在那些不该这样做的事情上”。“追求最优”和本节 optimizer 的译法“追求最优的人”一致。
- 不成立，保留原译：
  - 第 21 块 “The cook no longer deserves the three stars given to him by the Michelin guide”：审校者建议写“《米其林指南》（*Michelin guide*）”。原文用正体、小写 guide，指的是给餐厅评星的机构；中文“米其林指南”不加书名号也是通行的叫法。括注规则针对原文排成斜体书名的原题，这一处用不上，所以保留“米其林指南”。
  - 第 33 块 “if Hillel could teach him the Torah”：审校者建议写“《托拉》（*Torah*）”。原文 the Torah 是正体，和经书的通常排法一样；本书第 9 章的 the Bible 写“《圣经》”，也没有括注。保留“《托拉》”，和《圣经》的处理一致。
- 按全书统一的写法修改：1 处。第 2 块 “reciting *verbatim* his lecture notes” 的 verbatim 是英文里常用的拉丁语词，按“外文词”一条译成中文、用正体，“*一字不差*地照着讲稿念”改为“一字不差地照着讲稿念”，和第 2 章的“本身”（per se）、第 3 章的“事先”（a priori）一样。改后中文 16 处斜体，英文 17 处，差的就是这一处。另外核对过其余各条：标题已经是术语表定的“后记 淋浴时的三点想法”，前面“状态”里关于标题的待办已经解决；数字、人名括注（理查德·格拉索、西蒙、希勒尔拉比）、布里丹之驴（Buridan’s donkey）的括注位置、宽客（quant）、进化、内心的跑步机效应、两条译者注的格式和括注落在外层括号里的写法都符合规定，不用改。
- 对英文原文的疑问：
  - 审校者提出的第 6 块 “ergodicity in Chapter 8” 的章号、第 20 块 satisficing “a blend of satisfying and maximizing” 的说法、第 10 块 “As a matter a fact” 漏了 of，前几轮已经记在“原文疑点”里，前两处各有一条译者注。
  - 新增一处：第 8 块 “The link between the skill of the CEO and the results of the company are tenuous.” 的主语是 link，动词应为 is。不影响意思，照原意译“联系十分薄弱”。
- 核实与修改：agent（Opus 5.5）。改完后运行 `python3 scripts/site.py status fooled-by-randomness`，postscript 显示 34/34，全书 1294/1294；`tools/term_consistency.py` 全书检查 1705 处，没有报出本节的块；用 markdown-it 按 CommonMark 渲染，中文没有露出的星号；全节没有破折号和体例禁用的对比句式。

## 补全后的改动

2026-11-05，Claude（Opus 5.5 agent）拿用户提供的更好的来源（Random House 电子书较新的一次修订，版本号 rh_3.0 r12，原来导入的是 r8）和 en/ 逐块比对，按它改了本节。来源、比对方法和全书的改动清单见 `review/source.md` 的“用更好的来源补全（2026-11-05）”。下面的块号是改动以后的块号。

- 第 5 块 if he gets it right 改成 if he or she gets it right，hard for him 改成 hard for him or her；第 14 块讲央行行长的四个 he 和一个 He 改成 they、They。新版把泛指的 he 改成了 he or she（或 she or he），意思不变；按术语表“代词”一条，中文照旧写“他”，没有改。
- 块数不变，仍是 34 块。
- 检查：`python3 scripts/site.py status fooled-by-randomness` 全书 1300/1300 块已译；`python3 scripts/site.py check fooled-by-randomness` 通过；`tools/compare_better_source.py` 报告要查的差异为 0；用 markdown-it 渲染全书，中英文都没有露出的星号；新写的中文没有破折号，也没有体例禁用的对比句式。这些改动只做了译者自检，还没有经过另一个 agent 的双语审校。

## 2. 双语审校（补全部分）

- 执行者：另一个独立上下文的 agent（Opus 5.5），没有参与这次补全和翻译。日期 2026-11-05。
- 范围：第 5 块（he or she）和第 14 块（讲央行行长的 he 改成 they）。逐块对照现在 en/ 里的新版（r12）文字，表格和图另外对照新版 EPUB 里的原图；检查了意思、漏译和增译、数字、人名和括注、术语、注释，以及中文读起来是否通顺。
- 发现：0 条。第 14 块的 they 指单个的央行行长，中文按术语表“代词”一条写“他”，意思和新版一致；第 5 块同理。
- 修改：无。
- 检查：改完后运行 `python3 scripts/site.py status fooled-by-randomness`，28 节都是 review，1300/1300 块已译，第 7 章注释 2/2；`python3 scripts/site.py check fooled-by-randomness` 通过。新写和改过的中文里没有破折号，没有体例禁用的对比句式，也没有混进中文的半角标点。
