# 序章 问鼎王座（prologue）审校记录

全章 95 个块、23 条注释，中英逐块对应（`site.py status` 显示 95/95、23/23）。这一章是全书的样章，译文风格以它为准。

## 1. 译者自检

- 执行者：Claude（主会话，Opus 5.5），译者本人。
- 范围：全章 95 块和 23 条注释，对照原文逐段检查。
- 发现并修改：
  - “four of his five board members” 指除奥特曼以外的五名董事，译作“董事会另外五名成员中的四人”。
  - “tripled its market capitalization” 译作“市值增长到原来的三倍”，和原文的倍数一致。
  - “multibillion-dollar tech giant” 按字面译作“价值数十亿美元的科技巨头”，数字照原文。
  - 员工猜测奥特曼“也许没有违法，只是在道德上有问题”一句，按体例用了直接的说法。
  - 推文和 Slack 回复按原文语气译：“You and what fucking army” 译作“就凭你？你他妈有几个兵？”，“we are so back” 译作“我们满血回归了”。
- 人名：译完后和 `review/terms/people-zh.tsv` 逐个核对，改了两处：Jakub Pachocki 改作“雅库布·帕霍茨基”，Aleksander Mądry 改作“亚历山大·蒙德雷”（都按波兰语读音）。
- 未决：无。

## 原文疑点

| 位置 | 原文 | 处理 |
| --- | --- | --- |
| 注释 16 | 布罗克曼的推文日期写作 November 21, 2024 | 推文发于 2023 年 11 月 21 日奥特曼复职当晚（推文编号 1727230819226583113 解出的时间是 2023-11-22 07:41 UTC，即太平洋时间 11 月 21 日深夜），原注应是笔误。英文和中文注释 16 的出处都照原文保留；双语审校后，说明改为正文里的译者注 [^t1]，写在文件末尾 |
| 第 80 块 | its commitment to these ideals were fast eroding | 主谓不一致（commitment 配 were），是小的语法笔误，不影响意思，按原意翻译 |

## 2. 双语审校

- 执行者：另一个独立上下文的 agent（Opus 5.5），没有参与翻译。
- 范围：全章 95 个块和 23 条注释，逐块对照英文；核对了人名、术语、数字和金额换算、注释标记的位置和出处，也查了破折号和体例禁用的对比句式。
- 发现：32 条；核实后采纳 32 条，不采纳 0 条。32 条里，16 条照审校者给的改法改，16 条采纳意见、措辞由编辑另拟。逐条都对照了英文。
- 采纳的例子：
  - 注释 16（“He tweeted it with… November 21, 2024”）：原来把译者注接在出处后面，出处因此和英文不一致。现在注释 16 的出处和英文逐字相同，说明移到正文“我们满血回归了。”后面的 [^t1]，定义写在文件末尾，和第 1、4、6、9 章的做法一致。
  - 人名括注：蕾哈娜（Rihanna）、大卫·贝克汉姆（David Beckham）、泰勒·斯威夫特（Taylor Swift）、史蒂夫·乔布斯（Steve Jobs）在本章第一次出现，补上了英文原名。
  - 第 49 块 “Reinstate Altman and resign, or risk a mass employee exodus”：原译“让奥特曼复职并且辞职”读起来像奥特曼复职后又辞职。改为“让奥特曼复职，董事会自己辞职，否则公司就可能面临员工大批出走”，risk 也译出了“可能”。
  - 第 15 块 “She had alleged in tweets that had gone viral a month before”：一个月前是推文疯传的时间，原译挂到了发推文上。改为“她曾在推文里指控哥哥虐待过她，一个月前，这些推文在网上疯传开来”。
  - 第 9 块 “Just weeks before, it had been valued at up to $90 billion as part of a tender offer it was in the middle of finalizing”：几周前说的是估值，要约到奥特曼被解雇时还在敲定。改为“就在几周前，在一轮股份收购要约中，公司估值最高达到 900 亿美元。这轮要约当时还在敲定……”。
  - 第 91 块 “growing demands from superiors”：补上 growing，改为“上级要他们做的工作越来越多”；“The following month”改为“次月”，注释 21 的引导语同步修改。注释 20 的引导语补成“2024 年 6 月，高盛的一份报告”，和正文标记的位置对上。
  - 数字：按体例“多位数字用阿拉伯数字”，改为“将近 800 人”“不到 24 小时”“36 个多小时”“大约 200 名员工”“100 多位”“20 分钟后”“1.5 万多倍”“1 万名员工”，注释 4 改为“11 位”。带“几”“数”“十几”“十多”的概数，以及和“两天后”并列的“十天后”，保留汉字。
- 措辞另拟的例子和理由：
  - 第 80 块 “not in fact an altruistic project but rather one of ego”：审校者建议“驱动它的是个人的自负与私心”。“私心”是原文没有的意思，定为“驱动它的是个人的自负”。
  - 第 87 块 “all suffering new degrees of precarity”：建议“前所未有地朝不保夕”，“前所未有”比 new degrees 说得重，定为“处境都变得比以往更加朝不保夕”。
  - 第 45 块 “act in the best interest not of OpenAI’s shareholders but of its mission”：建议“无须以股东利益为先”，读起来像股东利益仍在考虑之列，排在后面。原文的意思是董事会对股东不负这份责任，定为“无须为股东的利益负责”。
  - 第 79 块 “The founders asserted a radical commitment”：建议里的“高调”原文没有，定为“创始人们宣示了一项激进的承诺：开发所谓的通用人工智能……”。
  - 第 4 块 “the city’s first Formula One race in a generation”：定为“这座城市时隔几十年再次举办的一级方程式大奖赛”，读者不必再换算“一代人”。
  - 第 56 块 “firmly stands by its decision”：定为“坚决维持这一决定”，“维持决定”是中文常用的搭配；注释 12 的引导语同步修改。
  - 第 86 块 “the people who had the power to be in the decision-making room”：定为“那些有权跻身决策圈的人”。
- 不采纳：无。
- 审校者的总体判断：序章译文整体质量很高，可以继续作为全书样章。中英两边逐块对应，所有注释标记的编号和位置都对得上，出处除注释 16 外都和英文一字不差，人名和 people-zh.tsv 一致，术语基本按术语表处理，没有破折号和体例禁用的对比句式；金额换算都核对过，没有错误。语言是清楚生动的记者式叙事中文，粗话和口语的语气也保留了。需要改的是四类局部问题：格式规则（注释 16 的译者注、四处人名括注、注释 20 的引导语），几处意思偏差（第 9、15、49、90、91、92、95 块），数字写法不统一，以及十几处搭配生硬或带翻译腔。这些都属于局部修改，不需要重译。

## 3. 中文通读

- 执行者：编辑 agent（Opus 5.5）。
- 范围：双语审校修改后的全章中文，从头读到尾，看连贯、重复、指代，以及人名和术语前后是否一致。
- 发现并修改 11 处，每处都回查了英文：
  - 第 4 块：“拉斯维加斯”在相邻两句里各出现一次，第二句改回“这座城市”。
  - 第 14 块 “These days, employees had fewer opportunities”：“如今”容易被读成写书时的现在，改为“那段时间”。
  - 第 24 块 “many had made plans to buy property, or already had”：原译一句里两个“已经”，改为“许多人都计划好了要买房，有的已经买了”。
  - 第 40 块 “word arrived that three more senior researchers had quit”：原译“传言……又传来消息：又有……”字面重复，改为“这时有消息说，又有三名资深研究员离开了公司”。
  - 第 44 块：双语审校后的“又进一步加码”里“又”和“进一步”重复，改为“还进一步加码”。
  - 第 49 块 “They needed to replace her”：上一句的主语是员工、投资者和穆拉蒂，“他们”指谁不清楚，改为“董事会需要找人接替她”。
  - 第 78 块 “In even less time, it is now on track to rewire”：“如今”和“照目前的势头”意思重复，删去“如今”，改为“照目前的势头，它还将用更短的时间改造……”。
  - 第 84 块 “The ouster and reinstatement of Altman … was final proof”：改为“2023 年 11 月，奥特曼被赶下台，又官复原职，这件事最终证明，这场治理实验失败了”，后一句开头的“这件事”改为“它”。
  - 第 84 块 “dissolving the last remnant of the organization’s altruistic facade”：“荡然无存”和第 82 块重复，改为“最后一点利他的门面也不复存在”。
  - 第 86 块 “I’ve come to understand two things: Artificial intelligence is…”：句号改为冒号，读者能看出后面这句就是第一件事，和第 87 块“我明白的另一件事”呼应。
  - 第 89 块 “they, too, seize and extract precious resources”：按术语表（对象是资源时 extract 译“开采”）和第 88 块的改法，“攫取”改为“夺取并开采”。
- 一致性：全章人名都和 people-zh.tsv 一致，每人在本章第一次出现时都有英文括注；tender offer（股份收购要约，后文简称收购要约）、not consistently candid（没有始终坦诚）、AGI、智能时代等术语前后一致。
- 检查：`site.py status` 显示 95/95、23/23；`site.py check` 的草稿构建通过；全文没有破折号和体例禁用的对比句式；注释 1 至 23 的出处和英文逐字相同，[^t1] 在正文里有引用。

## 4. 阅读器校样

- 执行者：Claude（主会话），用 `site.py serve --drafts` 构建后，在无界面 Chrome 里打开真实页面，桌面宽度 1280 像素，手机宽度（390 像素）也看过。
- 结果：标题“序章 问鼎王座”；23 条注释的编号和英文一致，点开弹窗有内容，另有 1 条译者注；没有待译段落，中文里没有破折号；正文之后显示“本章小结与要点”；没有控制台错误和加载失败的请求，没有横向溢出。

## 状态

- 没有未解决的意义问题。
- 留给主会话决定：数字写法。本章已按体例把多位数字改成阿拉伯数字；其他章节还有“一万块 GPU”“两百多起”“一百多倍”这类写法，建议在术语表里写清楚英文用单词拼出的整数怎么处理，再统一全书。
- 发布前要运行 `python3 scripts/site.py fonts empire-of-ai`：`check` 提示字体子集缺字，本章这次也用到了新字（例如“掀”“跻”“腹”）。

## 第三轮：GPT-6 Astra 独立审校

- 审校者：GPT-6 Astra，通过 Codex 运行，只读，和译者属于不同的模型家族。
- 发现：7 条。逐条找到中英文对应的句子，读过上下文后核实：成立并修改 6 条，不成立 1 条。
- 成立并修改：
  - 第 35、36 块，员工的提问 “Are we worried about the hostile takeover via coercive influence of the existing board members?” 和苏茨克维的回答 “Hostile takeover? … It is not a hostile takeover.”：原译“恶意收购”，共三处。员工指的是董事会用强硬手段夺取公司控制权，“收购”会让读者以为有人在买下公司。三处都改为“恶意接管”。
  - 第 30 块 “How do you reconcile the desire to grow together through crisis with a frustrating lack of transparency?”：原译“你一方面希望大家在危机中共同成长，一方面又让人沮丧地缺乏透明度，这两者怎么调和？”，“让人沮丧地缺乏透明度”照搬了英文的修饰关系，读着生硬。改为“你一方面希望大家在危机中共同成长，一方面又这样不透明，让人很沮丧，这两者怎么调和？”。“调和”和下一句的“和解”照旧，对应原文 reconcile 和 reconciliation 的呼应。
  - 第 81 块 “The loss of its primary backer pushed OpenAI into financial uncertainty.”：原译“失去主要金主之后，OpenAI 陷入了财务上的不确定。”，“陷入……不确定”套用了英文的抽象名词，读着像话没说完。改为“失去主要金主之后，OpenAI 的财务前景变得不明朗。”
  - 第 90 块 “Companies themselves, which once invested in sprawling exploratory research, can no longer afford to do so under the weight of the generative AI development bill.”：原译“那些曾经投资于大量探索性研究的公司，在生成式 AI 开发账单的重压下，自己也再负担不起了。”，“负担不起”没有宾语，又紧挨着“开发账单”，容易读成负担不起这笔账单。改为“就连公司自己，过去曾大量投资范围很广的探索性研究，如今在生成式 AI 开发账单的重压下，也再负担不起这类研究了。”定稿保留了原文“账单的重压”的说法，用“就连”译出 themselves 的语气。
  - 第 93 块，奥特曼博客文章里的 “the discovery of all of physics”：原译“发现全部的物理学”，“发现”和学科名“物理学”搭配不当。这是奥特曼的原话，定为改动较小的“发现物理学的全部规律”。
  - 第 93 块 “anyone … who wants a piece of that vision will have to rely on the empires to provide it”：原译“任何想分享这个愿景的人，无论是公司还是政府，都只能依赖这些帝国来提供。”“分享愿景”容易读成认同或传播这个设想，a piece of 说的是想从中分到好处；句末的“提供”也没有宾语。改为“任何想从这个愿景里分一杯羹的人，无论是公司还是政府，都只能靠这些帝国分给他们。”
- 不成立，保留原译：
  - 第 90 块 “employees working to advance AI technologies for drug discovery had to suspend their research and cede their computer chips to develop the chatbot instead”：审校者认为原文只说员工把芯片让给聊天机器人用，译文“交出他们的计算机芯片，转而去开发这个聊天机器人”多说了员工转去开发聊天机器人。英文里 to develop the chatbot instead 修饰前面两个动作，逻辑主语就是这些员工，instead 对照的是他们原来的药物研究，原译的读法符合原文语法。注释 18 引的《华尔街日报》报道也写到，百度要其他团队把人员和芯片一起借给这个聊天机器人项目（“lend their staff and their powerful computer chips”）。原译保留。
- 对英文原文的疑问：审校者指出注释 16 把布罗克曼 “we are so back” 推文的日期写作 November 21, 2024，正文写的是 2023 年 11 月 21 日奥特曼复职当晚，疑为笔误。这一条已记在上面的“原文疑点”表里，译者注 [^t1] 也已说明，这一轮不再改动。
- 按全书统一的写法修改：0 处。逐项对照了术语表“全书统一的写法”，本章已经符合：数字方面，一到十和约数用汉字（“十几名高管”“两天后”“十天后”“几十名员工”），11 以上的确数和万、亿前面的数字用阿拉伯数字（“将近 800 人”“36 个多小时”“1 万名员工”“1.5 万多倍”），倍数写“市值增长到原来的三倍”；本章出现的名人在第一次出现时都括注了英文，脚注出处里的人名都是英文；平台名写“X（原来的 Twitter）”“在 Twitter 上发了一张照片”；cochairmen 写“联席董事长”。Twitter 和联席董事长此前已由脚本统一。本章正文没有需要括注原题的书名或报刊，彭博社和其他各章一样按机构名写；inference、传播团队、Open Philanthropy 等其他条目本章都没有出现。钟点“下午 5 点”“晚上 9 点”术语表没有写到，其他章节里“凌晨 2 点”和“凌晨三点”两种写法都有，本章暂时保留阿拉伯数字，留给主会话统一决定。
- 核实与修改：agent（Opus 5.5）。改完后运行 `python3 scripts/site.py status empire-of-ai`，序章显示 95/95 块、23/23 条注释，全书 1681/1681 块已译。改过的块重新检查过，全章中文仍然没有破折号，也没有体例禁用的对比句式。
