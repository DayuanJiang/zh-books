# 致谢（acknowledgments）审校记录

全节 15 个块、0 条注释，中英逐块对应（`site.py status` 显示 15/15）。另加 1 条译者注 t1。

## 1. 译者自检

- 执行者：translation agent（Opus 5.5）。
- 范围：全节 15 块和译者注，对照原文逐句检查人名、刊名、数量和谁做了什么。
- 发现并修改：
  - “Thank you first and foremost to the people who believed in this book project”初稿“相信这本书”，那时书还没有写成，改作“相信这个写书计划”。
  - “Lindsay fielded many calls from me”初稿“无数个电话”偏夸张，改作“很多个电话”。
  - “my intrepid guide through Nairobi who was there for anything I needed”初稿“随时在场”意思不清，改作“我需要什么，他都随时相助”。
  - “I am indebted to Deborah Blum and Ashley Smart at MIT KSJ and Marina Walker Guevara and Boyoung Lim at the Pulitzer Center for giving me the funding”初稿句首“感谢”、句末“我欠他们一份情”重复，删去句首的“感谢”。
  - “the first person who knew what she was talking about to tell me she believed I could make a great journalist”译作“在懂行的人里，她是第一个对我说她相信我能成为一名出色记者的人”，保留“懂行的人里第一个”这层幽默。
  - “*Why don't you profile OpenAI?*”保留斜体；问号放在斜体外面，斜体的结束星号前面是标点、后面紧跟汉字时 Markdown 不会闭合。profile 和第 3 章一致，译作“深度报道”；“Tech Review”和第 3 章一致，译作《科技评论》。
  - “sitting for upward of ten hours of interviews across multiple sessions”译作“分好几次坐下来接受我累计十多个小时的采访”。
  - “Not only was he a moral compass and cheerleader…, he and Ann Godoff also committed Penguin Press's financial and legal resources”保留“不仅……还和安·戈多夫一起”的递进，资源是两人一起投入的。
  - “To my 奶奶”：原文这里直接用了汉字，中文照写“奶奶”，加译者注 t1 说明。
  - “To my in-laws”：作者下文提到丈夫，译作“公公婆婆”。
  - 术语按术语表：accountability 作“问责”，“AI colonialism”作“AI 殖民主义”，“data colonialism”作“数据殖民主义”，“chapter 4”作“第 4 章”。
- 人名：里娅·卡卢里、安德烈娅·保拉·埃尔南德斯、莫法特·奥金伊用 `people-zh.tsv` 的译名。其余 40 多人不在表里（致谢里的人不进索引），按新华社译名规则音译，括注原名；罗杰·麦克纳米、奥伦·埃齐奥尼用通行译名；名字的译法照表里已有的先例（David 作“戴维”，Josh 作“乔什”，Deborah 作“德博拉”，Wong 照“汉娜·黄”作“黄”）。Yuki Hirose 和 Boyoung Lim 是日本和韩国名字，查不到本人用的汉字，照表里 Chip Huyen 的先例保留原名。原文后文只称名字的（吉迪恩、安杰拉、尼尔、穆里埃尔、玛丽娜、海迪、安德烈娅、纳迪娜），中文也只写名字。
- 未决：
  - 表外人名的音译需要主会话确认后补进 `people-zh.tsv`，其中 Janet Guyon（暂作“珍妮特·盖永”）的姓读音没有核实，Josh Chin（暂作“乔什·钦”）没有查到本人的中文名。
  - Quartz 暂作《石英》（Quartz），中文媒体也有“石英财经网”的叫法。

## 原文疑点

| 位置 | 原文 | 处理 |
| --- | --- | --- |
| 第 5 段末句 | “the many others with whom I didn't interface directly but were critical to the process” | but 后面缺了关系代词 who，属于语法小疏漏，意思清楚。按原意译作“其他许多我没有直接打过交道、对整个过程却至关重要的人” |

## 2. 双语审校

- 执行者：另一个独立上下文的 agent（Opus 5.5），没有参与翻译。
- 范围：全节 15 块和译者注 t1，逐句对照英文，核对人名、刊名、数字和谁做了什么。
- 发现：14 条；核实后采纳 14 条，不采纳 0 条。审校者的写法有几处编辑换了说法，下面写明。
  - 意义（2 条）：
    - “someone called the cops on him”原译“有人打电话报警抓他”，“抓”是原文没有的意思。审校者建议的“有人报警告了他”容易读成“报警告”，编辑改为“有人向警方举报了他”。
    - “Drew Dowell and Jason Dean helped secure my reporting trip to make it happen”原译“让报道得以成行”，“成行”只能说行程，改为“这篇报道才得以完成”。
  - 用词和术语（4 条）：
    - “MIT's Knight Science Journalism fellowship”原译“奖学金”。这是给在职记者的研究员项目，改为“麻省理工学院奈特科学新闻研究员项目”，和下一句 MIT KSJ 的“奈特科学新闻项目”对得上。
    - “chased down sources”原译“追寻消息来源”，改为“四处寻找消息来源”。
    - “the logistical chaos that Mia so expertly contained”原译“米娅高明地化解掉的种种琐碎事务上的混乱”，改为“统筹调度上的种种乱子，米娅都干净利落地摆平了，我看到的连一半都不到”。同一条里的“同人”，审校者说大陆通用“同仁”；《现代汉语词典》以“同人”为正体，可这个词现在常让人联想到同人创作，编辑改为平实的“成员”。
    - “Thank you first and foremost to the people who believed in this book project”和“they believed in truth, transparency, and accountability”原译“首先，也是最重要的，感谢那些相信这个写书计划的人”“相信真相”。“首先，也是最重要的”是翻译腔，“相信真相”容易读成“认为它是真的”。改为“我首先要感谢那些对这个写书计划抱有信心的人”“信奉真相、透明和问责”。
  - 句子结构（7 条）：
    - 戴维·杜勒一句“It was through his patience, his probing questions, and, most importantly, his ability to kindly and firmly tell me when something just wasn't working”原译两个名词后面接一个小句，并列断开。编辑改为三个短句再接“正是靠着这些”：“他很有耐心，提问总是刨根问底，最重要的是，哪里实在行不通，他总能温和而坚定地告诉我。正是靠着这些，我才渐渐看清……”；“成为一本书的基础”保留，对应 form the basis of a book。
    - 斯科特一句“whose unfailing support ever since allowed me to pursue it in its most ambitious form”原译“此后始终如一的支持”缺主语，改为“此后又始终如一地支持我，让我能以最宏大的形式去实现它”；“Reporting and writing a book like this”原译“为写这样一本书去采访、写作”，改为“采写这样一本书”。
    - “I am indebted to Deborah Blum and Ashley Smart … for giving me the funding”原译主语很长，句末才落到“我欠他们一份情”。改为句首“疫情期间”、句末“对此我深怀感激”；“这样一个涉及面这么广的项目”改为“这样一项范围广阔的报道”，这一段已有好几处“项目”。
    - “under Marina's visionary leadership in global journalistic collaborations”原译“在玛丽娜对全球新闻合作富有远见的领导下”，改为“玛丽娜在推动全球新闻合作上很有远见，正是在她的带领下”；后半“开展跨越全球的报道项目的新方法”两个“的”连用，改为“一种新方法，来开展横跨全球的报道项目”。
    - “Niall was also instrumental in supporting my new line of inquiry”原译“在支持我这个新的探究方向上起了关键作用”，改为“尼尔同样鼎力支持我走上这条新的探究路线”；审校者建议的“支持我转向这个新的探究方向”和前半句的“转向”重复，“方向”又和后文“帮我找准了方向”重复，编辑换了“走上这条新的探究路线”。“the vast global inequality that AI was perpetuating”改为“AI 正在让全球范围的巨大不平等延续下去”。
    - “what it means to report and write stories at the highest levels of mastery”原译“对以最高的水准采访和写作意味着什么”，改为“对什么才是最高水准的采访和写作”；“inimitable colleagues”原译“无可比拟的同事们”，改为“出类拔萃的同事们”。
    - “whose intellectual and moral clarity on the subject has been a guiding light”原译“她在这个问题上思想和道德的清晰”，改为“她在这个问题上思路清晰、道德立场分明，始终是指引我的明灯”。
  - 标点（1 条）：丈夫一句“best friend, life partner, moral compass, …, endless romantic”并列名词原来用逗号，改用顿号；“永远的浪漫主义者”容易联想到文艺流派，改为“也是一个永远浪漫的人”。
- 审校者的总体判断：五个分节逐块对照英文读完，脚注和译者注都看过，整体质量较好，可以作为定稿的基础。结构完全对齐（献辞 7/7、题词 6/6 和 2/2、作者说明 5/5、致谢 15/15、关于作者 2/2），五个文件里没有破折号，也没有“不是……而是……”句式；人名按 people-zh.tsv，每节第一次出现括注英文；术语符合术语表；数字（300 多次采访、约 260 人、150 多次、90 多名、约 40 名、十多个小时、六个月、2021 年底）都核对无误。实质问题有四处：作者说明里对话来源一句前后矛盾，题词里“不如他开明”误译，致谢里“报警抓他”多了意思，“让报道得以成行”搭配不当；其余是表达问题，集中在致谢一节。致谢一节的表达问题主要是几处定语堆叠和名词化直译、一句缺主语、几处用词和一处标点。

## 3. 中文通读

- 执行者：编辑 agent（Opus 5.5）。
- 发现并修改（改动都回查过英文）：
  - 第 2 段：新的首句用了“我首先要感谢”，紧接着的“我尤其要感谢所有的消息来源”又是“要感谢”，改为“尤其是我所有的消息来源，我欠他们太多”，对应 I especially owe so much to all my sources。
  - 第 7 段：“在两周马不停蹄的采访中，她做调研、安排采访”，“采访”连用两次，改为“在马不停蹄的两周报道行程里”，对应 across two weeks of nonstop reporting。
  - 第 9 段：里娅一句前半已有“一直给我力量和快乐”，后半的“一直是指引我的明灯”改为“始终是”。
  - 第 10 段：“他当时是《麻省理工科技评论》的主编，他疯狂地赌了一把”删去第二个“他”。
  - 通读确认：后文只称名字的人（吉迪恩、安杰拉、尼尔、穆里埃尔、玛丽娜、海迪、安德烈娅、纳迪娜）前面都出现过全名；“道德指南针”“啦啦队”在斯科特和丈夫两处都有，原文就这样重复，保留；《科技评论》和“深度报道”和第 3 章一致；“问责”“AI 殖民主义”“数据殖民主义”符合术语表；“对……抱有信心”“信奉”“信任”和第 1 段“信念”的主题仍然呼应。

## 状态

- 没有未解决的意义问题。
- 留给主会话决定的事项（不涉及意义）：表外人名的音译要补进 `people-zh.tsv`，其中 Janet Guyon、Josh Chin 的中文名没有核实；Quartz 暂作《石英》。
- `site.py status` 显示 15/15。

## 第三轮：GPT-6 Astra 独立审校

- 审校者：GPT-6 Astra，通过 Codex 运行，只读，和译者属于不同的模型家族。
- 发现：5 条（意义 1 条，表达 4 条）。逐条找到中英文对应的句子，读过上下文后核实：成立并修改 5 条，不成立 0 条。
- 成立并修改：
  - 第 5 块（米娅·康塞尔一段），英文“Her masterful coordination behind the scenes made the entire editing and production process feel so seamless”。原译“她在幕后的协调高超老练”，新译“她在幕后协调得极为高明”。“老练”通常形容人或手法，拿来做“协调”的谓语搭配不上，“协调高超”也别扭。审校者建议“她在幕后协调有方”，意思对，但 masterful 的分量弱了，编辑改用“极为高明”。
  - 第 8 块（斯蒂芬·图奥·基古鲁一段），英文“whose humor and relentless optimism remained unflappable even when someone called the cops on him”。原译“即便在那时，他的幽默和永不消退的乐观也丝毫没有动摇”，新译“即便在那时，他也处变不惊，照样幽默，乐观劲儿一点没减”。“幽默没有动摇”搭配不自然；unflappable 说的是人遇事镇定。审校者建议“他仍然幽默风趣，一如既往地乐观”，没有译出 unflappable 的镇定，编辑加了“处变不惊”，用“一点没减”对应 relentless。
  - 第 9 块（朋友和导师一段），英文“who generously read early drafts of the book or various excerpts”。原译“他们慷慨地读了这本书的早期书稿”，新译“他们慷慨地抽出时间，读了这本书的早期书稿”。中文的“慷慨”说的是舍得拿出钱财、时间这类东西，“慷慨地读”是直译；照审校者的建议补出“抽出时间”。
  - 第 9 块（同一段奥伦·埃齐奥尼一句），英文“to ensure they were correct and appropriately nuanced”。原译“确保它们准确无误、分寸得当”，新译“确保它们准确无误，该有的细微差别也都照顾到了”。nuanced 指对 AI 历史的叙述和技术解释保留了必要的细微区别和限定，“分寸得当”多指说话做事的态度和尺度，读者容易理解成语气适度。审校者建议“确保内容准确，并恰当呈现其中的细微区别与必要限定”，意思对，但偏长偏书面，编辑改得短一些、口语一些。
  - 第 13 块（《华尔街日报》和《大西洋月刊》一段），英文“my editor Damon Beres needed no convincing when I pitched him a wonky story”。原译“他完全不需要我说服”，新译“他二话没说就同意了”。原译照搬英文的否定说法，“需要我说服”又缺宾语，读着生硬；原意是他爽快地接受了这个选题。审校者建议“无须我多费口舌，他就认可了这个选题”，放在分号前偏长，编辑改用口语的“二话没说就同意了”；后半句“保罗……也一样”仍然接得上。
- 不成立，保留原译：无。
- 对英文原文的疑问：审校者没有提出。译者自检时记下的一处仍然成立：第 5 块末句“the many others with whom I didn't interface directly but were critical to the process”，but 后面缺了关系代词 who，属于语法小疏漏，意思清楚，译文照原意，没有改。
- 按全书统一的写法修改：0 处。逐项核对过：“十多个小时”“两周”“六个月”“分四篇”“他们四人”是十以内的数或约数，用汉字，“2021 年底”“第 4 章”用阿拉伯数字，都符合规定；《石英》不在常见报刊之列，已括注斜体原题（*Quartz*），《麻省理工科技评论》《科技评论》《华尔街日报》《大西洋月刊》按常见报刊不括注，书名号之间也没有顿号；人名第一次出现都括注了英文，Yuki Hirose 和 Boyoung Lim 照写原名；本节没有脚注，唯一的译者注 t1 里没有人名；平台名、inference、头衔、术语表列出的机构和其他说法本节都没有出现。
- 核实与修改：agent（Opus 5.5）。改动都在 zh-cn/30-acknowledgments.md 里，块的对应保持原样，本节没有注释。改完后运行 `python3 scripts/site.py status empire-of-ai`，本节显示 `| acknowledgments | review | 15/15 |  |`，全部 15 个块都已翻译，本节没有注释；全书 1681/1681 块（100%）。中文文件里没有破折号，也没有体例禁用的对比句式。
