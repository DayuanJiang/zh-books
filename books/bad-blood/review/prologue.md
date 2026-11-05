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
