# 致谢（acknowledgments）审校记录

全节 7 个块，原文没有注释，另加 1 条译者注，中英逐块对应（`site.py status` 显示 7/7）。

## 1. 译者自检

- 执行者：translation agent（Opus 5.5），译者本人。
- 范围：标题和 6 段正文，加 1 条译者注，从头译到尾，没有跳过。译完后用脚本把中英文逐块并排列出，逐句检查漏译、增译、否定、数字、人物关系和职务；又顺着中文读了一遍，读时的改动都回查了英文。
- 发现并修改：
  - “I am very lucky that this book landed at Knopf and in the deft hands of Andrew Miller.”：初稿“交到安德鲁·米勒那双灵巧的手里”直译 deft hands，中文读来像在说手工活，改为“交到编辑高手安德鲁·米勒（Andrew Miller）手里”。米勒是本书在克诺夫出版社的编辑（人名表），“编辑高手”只是把 deft 的意思说明白。
- 有意这样处理的地方：
  - 第一段原文是一个长句：“This book, which flowed from my work exposing the Theranos scandal..., would not have been possible without the help of the confidential sources who spoke to me at great personal peril throughout 2015 and 2016.” 照英文套成一句定语太长，译时拆成三句：书源自报道；没有匿名消息来源就没有这本书；他们在 2015 年和 2016 年冒着风险向我讲述内情。第二段 “This book would also not have been possible without the dozens of other former Theranos employees who...” 同样拆开，先说“这本书同样离不开另外几十位 Theranos 前员工”，再说他们做了什么。
  - “Ianthe Dugan, Paulo Prada, Philip Shishkin, and Matthew Kaminski ... provided...”：原文在人名后面用两个破折号夹着 to name but a few，中文改成逗号，写“这里只能举出这几位”。
  - “Mike has been a mentor, not just to me but to generations of reporters, and is a standard-bearer for the great journalistic institution that is the Wall Street Journal.”：写成“迈克一直是我的导师，也是一代又一代记者的导师；《华尔街日报》是一家伟大的新闻机构，他是这家机构的旗手”，符合体例对句式的要求。
  - “Mike wasn’t my only ally” 写“我的盟友也不止迈克一个”。
  - “including during a stretch when I was on book leave” 写“我休假写书的那段时间也不例外”，意思是韦弗在作者休假期间也在跟进报道。
  - “But by far my greatest source of strength and inspiration came from the four people...” 写“我最大的力量和灵感来源，无疑是和我共度人生的四个人”，by far 用“无疑”表达。
  - 术语按术语表：confidential sources 写“匿名消息来源”，gone on the record 写“公开具名”，pseudonyms 写“化名”，tip 写“线报”，general counsel 写“总法律顾问”，chairman 写“董事长”，Knopf 写“克诺夫出版社”，Dow Jones & Co. 写“道琼斯公司”，Weill Cornell Medical Center 写“威尔康奈尔医学中心”，the Journal 一律写《华尔街日报》。laboratory experts 写“实验室专家”，和第 24 章一致。Knopf Doubleday Publishing Group 按人名表桑尼·梅塔一条写“克诺夫·双日出版集团”。Fletcher & Company 按术语表照写原名。Random House Tower 写“兰登书屋大厦”。
  - 数字：fifteen-year history 写“15 年的历史”，dozens 写“几十位”，three and a half years 写“三年半”，2015 年、2016 年、2015 年初照写。
  - Jason Conti：人名表说明他就是第 21 章起写作 Jay Conti 的那个人（第 21 章注释 5 也写作 Jason P. Conti）。英文读者看得出 Jay 是 Jason 的昵称，中文“贾森”和“杰伊”看不出关系，所以加译者注 t1 说明。
- 人名：21 人和 `review/terms/people-zh.tsv` 一致，每人在本节第一次出现时括注英文一次（泰勒·舒尔茨、斯蒂芬·马斯特、迈克·西科诺尔菲、贾森·孔蒂、雅各布·戈尔茨坦、克里斯托弗·韦弗、克里斯托弗·斯图尔特、埃里克·卢普弗、安德鲁·米勒、桑尼·梅塔、伊安西·杜根、保罗·普拉达、菲利普·希什金、马修·卡明斯基、简、热拉尔、亚历山德拉、莫莉、塞巴斯蒂安、杰克、弗朗切斯卡）。原文的 Chris 是克里斯托弗·斯图尔特的昵称，写“克里斯”，不再括注。my sister, Alexandra 写“我的姐妹亚历山德拉”，原文没说是姐姐还是妹妹。
- 检查：`site.py status bad-blood` 显示本节 7/7；中文正文没有破折号，也没有“不是……而是……”“而不是”句式；汉字和数字、英文之间都有空格，没有半角标点。
- 未决：
  - my sister 写“姐妹”，中文读者可能会觉得别扭；如果主会话查到亚历山德拉是姐姐还是妹妹，可以改成具体的称呼。
  - Jason Conti 和 Jay Conti 的译者注，是否需要，请主会话定；如果全书改成统一写一个中文名，这条注可以删掉。
  - `book.json` 里本节状态仍是 `todo`，按分工由主会话修改。

## 2. 双语审校

- 执行者：另一个独立上下文的 agent（Opus 5.5），没有参与翻译。
- 范围：标题、6 段正文和译者注 t1，逐块对照英文读完；核对了人名、职务、数字和术语。同一位审校者也审了献辞、作者说明、尾声和关于作者四节。
- 发现：2 条，都是读起来别扭的句子；核实后采纳 2 条，不采纳 0 条。两条都改用了编辑调整过的措辞。
  - 采纳（措辞由编辑调整）：“All were moved to talk to me, despite the legal and career risks they faced, by one overriding concern: protecting the patients who stood to suffer harm from Theranos’s faulty blood tests.” 原译冒号紧跟在“才站出来跟我谈”后面，“保护那些……患者”会被读成谈话的内容。拆成两句：“尽管面临法律上和职业上的风险，他们还是站出来跟我谈了。促使他们这样做的，都是同一个压倒一切的考虑：保护那些可能因 Theranos 有缺陷的血液检测而受到伤害的患者。”这样冒号后面解释的是“考虑”。中文通读时又把前一句的“还是”改成了“全都”，见下一节。
  - 采纳（措辞由编辑调整）：“to name but a few” 原译“这里只能举出这几位”插在主语和谓语中间，“只能”多出不得已的意思；“急需的欢笑”有翻译腔。改为“这里只举几位：伊安西·杜根（Ianthe Dugan）、保罗·普拉达（Paulo Prada）、菲利普·希什金（Philip Shishkin）和马修·卡明斯基（Matthew Kaminski），他们常常鼓励我，也在我最需要的时候逗我开心。”much-needed comic relief 写“在我最需要的时候逗我开心”；frequent 修饰 encouragement，对应“常常鼓励我”。
- 审校者的总体判断：五节都逐块对照英文读完，致谢 7/7 块对得上，人名和 people-zh.tsv 一致，术语符合术语表，中文没有破折号，也没有“不是……而是……”句式。致谢需要改的只有第一段的冒号和最后一段的插入语两处，改完就可以进入中文通读。审校时审校者没有改动文件。

## 3. 中文通读

- 执行者：编辑 agent（Opus 5.5）。
- 范围：审校意见改完以后，从标题顺着读到译者注，检查连贯、重复、指代和人名写法。
- 发现并修改（每一处都回查了英文）：
  - 第 1 段前两句一句以“这本书”开头、一句以“这本书”结尾（“如果没有那些匿名消息来源的帮助，就不会有这本书”），第二句改为“如果没有那些匿名消息来源的帮助，它不可能写成”，对应 would not have been possible。
  - 审校改过的“他们还是站出来跟我谈了”，前一句讲的是“另一些人”，读者可能以为只指用化名的那些人。英文是 All were moved，改为“他们全都站出来跟我谈了。促使他们这样做的，是同一个压倒一切的考虑”。
- 一致性：21 个人名全节写法一致，每人第一次出现括注英文一次；the Journal 都写《华尔街日报》；“线报”“匿名消息来源”“公开具名”“总法律顾问”和术语表一致。献辞的四个人名和本节末段写法相同。
- 检查：`site.py status bad-blood` 显示本节 7/7；中文没有破折号，也没有“不是……而是……”句式。

## 状态

没有未解决的意义问题。留给主会话的两件事都不影响意思：亚历山德拉写“姐妹”是否改成具体的称呼；贾森·孔蒂的译者注是否保留。`book.json` 里本节状态仍是 `todo`，阅读器校样还没有做。
