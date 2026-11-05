# 序章（prologue）审校记录

全章 37 个块、4 条注释，中英逐块对应（`site.py status` 显示 37/37、4/4）。两条分隔线只在英文里。这一章是全书的样章，译文风格以它为准。

## 1. 译者自检

- 执行者：sample translation agent（Opus 5.5），译者本人。
- 范围：全章 37 块和 4 条注释，对照原文逐段检查漏译、增译、否定、数字、人名、术语和注释；译完后又顺着中文读了一遍，读时改动的地方都回查了英文。
- 发现并修改：
  - “Novartis was so impressed that they have asked for a proposal”：初稿“诺华印象非常深刻，已经请我们提交一份方案”丢了 so … that 的因果，补成“所以已经请我们提交一份方案”。
  - “There weren’t many three-year-old startups that could say they were worth that much”：初稿“敢说自己值这么多钱”多了胆量的意思，改为“能说”。
  - “Mosley’s unease with all these claims had grown since that morning’s discovery”：初稿“自从那天上午发现了真相”比原文说得重，改为“那天上午知道了这件事以后”。
  - “A rumpled dresser”：初稿“他穿着总是皱巴巴的”里的“穿着”容易读成动词，改为“他的衣着总是皱巴巴的”。
  - “Her voice added to the mesmerizing effect”：初稿“她的嗓音让这种魔力更强了”生硬，改为“她的嗓音更让人着迷”，冒号后面的男中音照旧。
  - “It showed revenue stagnating for a few years”：初稿“这种预测里，收入先停滞几年”改为“这种预测显示”，和 showed 对上。
  - “to an actual product a huge multinational corporation was interested in using”：初稿句末“一家庞大的跨国公司有意采用”读着像没说完，改为“有一家庞大的跨国公司想要采用”。
  - “the venture capitalists startups courted for funding knew that startup founders overstated these forecasts”：初稿一句里“创业公司”和“风险投资人”各出现两次，改为“创业公司为了融资四处争取的那些风险投资人，也都知道创始人会夸大这类预测”，courted 的意思保留在“四处争取”里。
  - “She had the presence of someone much older than she was”：删去“远超她年龄”里重复的“她”。
  - 注释 1 “sent by Tim Kemp to his team”：“发给他的团队的邮件”连用两个“的”，改为“发给手下团队的邮件”。
- 有意这样处理的地方：
  - “I think you should leave right now.” 译作“我看你现在就该离开”。“离开”在中文里同样可以指离开办公室或离开公司，下一段才点明意思，和原文的安排一致；“走人”会提前把意思说破。
  - “Elizabeth wasn’t merely asking him to get out of her office. She was telling him to leave the company” 和后面用破折号引出的 immediately，译作“伊丽莎白要他离开的，除了她的办公室，还有这家公司，而且是马上离开”。破折号改成“而且是”，前后两句合成一个递进句，体例禁用的对比句式也就用不上了。
  - “*extra*-ordinary” 按术语表写“*非*凡”。原文紧接着说 extra 用了斜体和连字符，中文读者从“*非*凡”看不出连字符，所以括注英文原词：“*非*凡”（*extra*-ordinary），后面的说明照译。术语表这一条已补上这个写法。
  - “*one hundred and sixty-five million dollars*” 按术语表写“*1.65 亿美元*”，保留斜体。
  - “an ambitious idea Holmes had dreamed up” 这一句原文用姓，照写“霍姆斯”；本章其余地方原文都用 Elizabeth，写“伊丽莎白”。Shaunak 原文一直用名，写“肖纳克”。
  - “His expert testimony[^2] about the addictive properties of cigarettes” 译作“他以专家证人的身份就香烟的成瘾性作证[^2]，这份证词迫使……”，注释 2 的粗体引子相应写成“他以专家证人的身份作证”，和中文正文对上。
  - “the trial’s sponsor” 用临床试验的通用说法“试验的申办方”。
  - “Theranos was far from his first rodeo” 译作“Theranos 远不是他第一次上阵”；“kind of a crapshoot” 译作“有点像掷骰子，全看运气”；“sleight of hand” 译作“障眼法”。
  - 数字：一到十用汉字（三年、八个月、四家、两家、六笔、五家、两台），11 以上的确数用阿拉伯数字（15 人、22 岁、30 年、25 年、60 名员工、18 个月、15 笔），金额换算成万和亿（1500 万美元、3200 万美元、1.65 亿美元、1.2 亿到 3 亿美元、15 亿美元、65 亿美元），tens of billions 写“数百亿美元”，30 percent 写“30%”。逐个和英文核对过，没有换算错误。
- 人名：9 人都和 `review/terms/people-zh.tsv` 一致，每人在本章第一次出现时括注英文：蒂姆·肯普、伊丽莎白·霍姆斯、亨利·莫斯利、唐纳德·L. 卢卡斯、拉里·埃里森、钱宁·罗伯逊、黛安·帕克斯、约翰·霍华德、肖纳克·罗伊。诺华、英特尔、甲骨文、松下按术语表写中文名，不括注。
- 术语：创业公司、联合创始人、风险投资人（VCs 写“风投们”）、融资、估值、曲棍球棒式预测、董事会、董事长、卡盒、读取器、Theranos 1.0、血液检测、硅谷（the Valley 也写硅谷）都按术语表。`tools/term_consistency.py` 检查了 93 处，没有一处缺少约定的译法。
- 注释：4 条的编号和位置和英文一致。注释 2 的出处照写英文；注释 1、3、4 里描述出处的说法译成中文，邮件主题、报告来源 VC Experts、幻灯片标题、人名保留英文。
- 检查：全章中文没有破折号，也没有体例禁用的对比句式；`site.py check bad-blood` 的草稿构建通过，只提示这本书还没有生成字体子集。
- 未决：
  - 原文特意把 one hundred and sixty-five million dollars 拼成英文单词再加斜体，让读者在这个数字上停一下。术语表定的“*1.65 亿美元*”保留了斜体，少了拼写出来的效果；如果想保留，可以写成“*一亿六千五百万美元*”。请用户决定，改动只涉及本章这一处。
  - 肯普邮件里的 “expressed interest in a financial arrangement for a project” 译作“表示有意就一个项目达成财务安排”，保留了公司邮件的公文腔，读起来略硬，留给双语审校判断。
  - 发布前要运行 `python3 scripts/site.py fonts bad-blood`。

## 2. 双语审校

- 执行者：另一个独立上下文的 agent（Opus 5.5），没有参与翻译。
- 范围：全章 37 块和 4 条注释，逐块对照英文，核对漏译、增译、否定、数字和金额换算、人名、术语、注释的编号和位置，以及体例（破折号、禁用句式、中英文之间的空格、全角标点）。审校者只提意见，没有改文件。
- 发现：8 条；编辑（Opus 5.5）逐条回查英文和中文后，采纳 8 条，其中 5 条用了编辑自己的改法；不采纳 0 条。
  - 意思偏差：“You didn’t change the world by being cynical.” 原译“冷嘲热讽是改变不了世界的”。cynical 指对理想和热情一概不信的态度，“冷嘲热讽”是挖苦人的言语。采纳，改为“愤世嫉俗是改变不了世界的”，句子结构不变。
  - 指代不清：“Mosley’s unease with all these claims had grown since that morning’s discovery.” 原译“那天上午知道了这件事以后”，前面三段讲的是融资、估值和幻灯片，“这件事”找不到所指。采纳。审校者建议的“有了那天上午的发现”带翻译腔，另一种写法“从肖纳克那里得知演示的内情”又和后面一句“莫斯利已经知道了内情”重复，所以改为“那天上午得知演示是怎么回事以后”。
  - 定语过长：“He brought up what Shaunak had told him about the investor demos.” 原译“他说起了肖纳克告诉他的投资人演示的事”，容易先读成“肖纳克告诉他的投资人”，下一句又以“他说”开头。采纳。审校者建议里的“都说了”多出了原文没有的“全部”，所以改为“他提起投资人演示的事，转述了肖纳克告诉他的情况”。
  - 主谓搭配：“Theranos was far from his first rodeo.” 原译“Theranos 远不是他第一次上阵”，公司做主语配“上阵”，读着别扭。采纳审校者的第一种改法，把“来到”换成前文用过的“加入”：“加入 Theranos 时，他早已身经百战。”
  - 容易误读：“Elizabeth Holmes, Theranos’s twenty-two-year-old founder, had flown to Switzerland”。原译“Theranos 22 岁的创始人”可能读成公司 22 岁，这一段也已经出现了三次 Theranos。采纳，删去这个 Theranos，写成“22 岁的创始人伊丽莎白·霍姆斯（Elizabeth Holmes）飞到瑞士”，上一句已经点明是这家公司。
  - 翻译腔：“Mosley saw an opening to broach the trip to Switzerland … When he did, Elizabeth admitted that there had been a problem”。原译“看到了一个机会，可以提起……他提了之后”照搬英文结构。采纳。审校者建议的“瞅准机会”口语色彩偏重，改为“莫斯利趁机提起了瑞士之行”，并删去“他提了之后”，前后两句的顺序已经说明伊丽莎白是在他提起以后才承认的。
  - 使动结构叠用：“helped him take Oracle Corporation public in the mid-1980s”。原译“帮他让甲骨文公司上了市”，照审校者的建议改为“协助他完成了甲骨文公司的上市”。
  - 术语统一：“the drug’s maker would be able to lower the dosage immediately”。原译“药厂”，术语表把 pharmaceutical company 和 drugmaker 都定为“制药公司”。采纳，改为“制药公司就能立刻降低剂量”。这一段因此出现三次“制药公司”，读来清楚，没有再改。
  - 不采纳：0 条。8 条都核实有据，改后都回查了英文，意思没有变化。
- 译者留给双语审校的两个问题：
  - 肯普邮件里的“表示有意就一个项目达成财务安排”（expressed interest in a financial arrangement for a project）：审校者认为放在公司内部邮件里合适。编辑同意，保留原译。
  - “*one hundred and sixty-five million dollars*”：审校者建议维持术语表的“*1.65 亿美元*”，斜体已经起到强调作用，改成“*一亿六千五百万美元*”会打破全书的数字体例。编辑同意，正文没有改，这一处仍等用户最后决定。
- 审校者的总体判断：译文质量很高，可以作为样章。逐块核对了 37 块和 4 条注释，没有发现误译、漏译、增译或否定方向错误；所有数字和金额换算无误；9 个人名都和 `review/terms/people-zh.tsv` 一致，并在本章第一次出现时括注了英文，原文用 Holmes 的一处写“霍姆斯”，其余写“伊丽莎白”；术语都按术语表处理；4 条注释的编号、位置和顺序正确，粗体引子和中文正文对得上，注释 2 的出处原样保留，注释 1、3、4 的说明性说法按术语表译成中文；全文没有破折号和禁用句式，中英文之间的空格和全角标点正确。需要改的 8 处都很小：一处意思偏差，一处指代不清，五处读着别扭或有翻译腔，一处术语不统一。

## 3. 中文通读

- 执行者：编辑 agent（Opus 5.5）。
- 范围：双语审校的改动落实以后，顺着中文从头读到尾，检查连贯、重复、指代，以及人名和术语前后是否一致。
- 发现并修改：
  - “Not that that was unusual.” 原译“这倒也不稀奇”紧跟在“这又一次说明这趟行程很顺利”后面，两句都以“这”开头，读者容易以为不稀奇的是行程顺利。原文的 that 指她满面笑容地走来走去，改为“她这样倒也不稀奇”。
  - 这处改动和双语审校的 8 处改动都回查了英文，意思、数字和语气都和原文一致。
- 读过、决定保留的地方：
  - “那天上午得知演示是怎么回事以后”和后面“莫斯利已经知道了内情”说的是同一件事，前后呼应，所指清楚。
  - 写莫斯利经历的一段和写卢卡斯的一段先后出现“完成了上市”，是同一个商业说法，读着并不别扭，保留。
  - “兴致勃勃”和下一段“她那份兴致”是有意的呼应，保留。
  - 人名和术语全章一致：霍姆斯只在“霍姆斯在斯坦福大学宿舍里想出来的”这一处按原文写姓，其余都写“伊丽莎白”；卡盒、读取器、创业公司、制药公司、风险投资人、估值、融资都只用一种写法。
- 检查：`tools/term_consistency.py` 在本章没有报出缺少约定译法的块；`site.py status bad-blood` 显示序章 37/37 块、4/4 条注释；`site.py check bad-blood` 的草稿构建通过，只提示还没有生成字体子集；全章中文没有破折号，也没有体例禁用的句式。

## 状态

- 没有未解决的意义问题。
- 等用户决定的写法问题：“*one hundred and sixty-five million dollars*”要不要改成“*一亿六千五百万美元*”。译者和审校者都倾向维持术语表的“*1.65 亿美元*”，正文目前按术语表写。
- 第 4 节阅读器校样还没有做；发布前要运行 `python3 scripts/site.py fonts bad-blood`。
