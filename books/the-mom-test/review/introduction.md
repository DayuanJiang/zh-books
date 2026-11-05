# 引言（introduction）审校记录

全节 38 个块，原文没有注释，译文也没有加译者注；中英逐块对应（`site.py status` 显示 38/38）。

## 1. 译者自检

- 执行者：translation agent（Opus 5.5）。
- 范围：全节 38 块，从第一块译到最后一块，译完后对照原文逐块检查漏译、增译、否定、条件、数字和日期、谁做了什么、比较对象、术语义项、人名和格式。本节没有脚注，不涉及脚注标记和定义。另外做了这几项：
  - 五个标题（`#` 一个、`##` 三个、`###` 一个）：`#` 照术语表的各节标题写“引言”，其余照原文译。
  - 用阅读器的渲染库 markdown-it 渲染译文，查有没有没生效的斜体。
  - 运行 `tools/term_consistency.py` 和 `site.py check`。
- 发现并修改：
  - “They are, in one way or another, forcing people to say something nice about their business.”：初稿“逼着别人对自己的生意说几句好话”，“自己”既可以指团队，也可以指被逼的人。原文 their business 是团队的生意，改为“对他们的生意”。
  - “every question we ask carries the very real possibility of biasing the person we’re talking to”：初稿“都实实在在地可能带偏和我们交谈的人”，语序别扭，改为“都实实在在有可能把和我们交谈的人带偏”。
  - “The approach and tools within are gathered from a wide range of communities ... It’s based on working with a bunch of founders and from my experiences ... as well as from the support of ...”：初稿一段里连用四个“来自”。第一句改为“取自许多不同的圈子”，后一句保留“来自……来自……也来自……”三项并列，对应原文的三个来源。
  - “It’s all in here.”：初稿“这些书里都有”，容易读成“这几本书里都有”，改为“这些在这本书里都有”。
- 几处译法的考虑：
  - “do you think it’s a good idea”：和第 1 章问题列表的第一问一致，写“你觉得这个想法好吗”，句中引用不加问号，和原文相同。“you already agree that talking to customers is a good idea” 里的 a good idea 是“值得做”的意思，和生意点子无关，译“是个好主意”。
  - “Hello,”：单独一段的称呼，按中文书信的习惯写“你好：”。
  - “want to figure out if it has legs”：译“能不能走得远”，保留 legs 的形象。
  - “Isn’t that exactly what talking to people is meant to prevent?”：译“和人交谈，图的不就是别落到这一步吗？”，保留反问。
  - “I may as well not have bothered.”：译“我还不如压根没费那个劲”。
  - “there’s a big gap between textbooks and check books”：译“教科书和支票簿之间，差着一大截”，保留两种“书”的对照（书本上的道理和真正收到的钱），没有加译者注。
  - “based on chipping away the formality and awkwardness of talking to people”：chipping away 接着开头几段的考古比喻，译“一点点凿掉”；formality 用术语表 formal 一行的“正式”，名词写“正式感”。
  - “customer conversation” (lowercase) instead of “Customer Development” (uppercase)：照术语表在下定义处括注英文并保留大小写的说明，写“客户对话”（customer conversation，小写），不称作“客户开发”（Customer Development，大写）。前面第一次出现的客户开发、精益创业没有括注英文。
  - “User Experience”：原文没有缩写，译“用户体验”，没有补“（UX）”。
  - “customer learning”：照术语表译“了解客户”；“learn from them” 译“从他们那里学到东西”。
  - “I’m a techie, not a sales guy”：译“我是搞技术的，不是干销售的”；“naturally bad in meetings” 照术语表 meeting 译“会面”，写“天生不擅长应付会面”。
  - “We’d relocated internationally to be closer to our market”：原文没说搬到哪个国家，译“搬到了另一个国家”，没有补出地名。
  - “They forget to mention that it’s hard.”：前一句是单数的 the popular kid，这里原文用 They 泛指给这种建议的人，中文照写“他们”。
- 人名、书名和机构：Steve Blank 只出现一次，写“史蒂夫·布兰克（Steve Blank）”，和 `review/terms/people-zh.tsv` 一致。两本书照术语表写“《四步创业法》（*4 Steps to the E.piphany*）”“《创业者手册》（*The Startup Owner’s Manual*）”，原题斜体，撇号和英文相同。Habit、MTV 照写，和汉字之间加空格；Sony 写“索尼”。
- 数字：3 years 写“三年”，a hundred times over 写“上百次”，a million little pieces 是夸张的说法，写“无数碎片”，months 写“好几个月”。都照术语表“全书统一的写法”。
- 检查结果：
  - `site.py status`：38/38。
  - `site.py check`：草稿构建通过，只有字体子集缺字的警告，发布前要运行 `site.py fonts the-mom-test`。
  - `term_consistency.py`：本节没有被标出的块，术语和人名都用了约定的译法。
  - 渲染结果：斜体 5 处（*应该*、*真的*、*能* 和两个英文书名），和英文的 5 处一一对应；页面上没有露出的星号。
  - 全节没有破折号，也没有体例禁用的对比句式。
- 未决：
  - 请用户确认几处译法：“Hello,” 写“你好：”；小标题 “Why another book on talking and selling?” 译“为什么还要再写一本讲交谈和销售的书？”，“A note on scope & terminology” 译“关于范围和术语的说明”；formality 写“正式感”；“textbooks and check books” 不加译者注。
  - 术语表没有规定客户开发、精益创业第一次出现时要不要括注英文。本节只在作者区分大小写的那一段括注了 Customer Development；如果希望第一次出现就括注，要在“你读过一些讲客户开发或精益创业的东西”一句补上。

## 2. 双语审校

- 执行者：另一个独立上下文的 agent（Opus 5.5），没有参与翻译。
- 范围：对照英文逐块读完全节 38 块，核对意义、漏译和增译、否定、数字、人名、书名、术语、机构名、斜体，以及破折号和体例禁用的句式。本节原文没有脚注，译文也没有译者注。
- 发现：11 条，其中术语 1 条，表达 10 条；编辑逐条对照英文和中文核实后，采纳 10 条，不采纳 1 条。采纳的条目里有 3 条认同审校者指出的问题，但改用了编辑自己的写法，理由写在对应的条目里。
  - 术语：“based on chipping away the formality and awkwardness of talking to people”：原译“正式感”。术语表 formal / formality 一行给 formality 定的是“拘泥形式”，第 4 章 “When you strip all the formality from the process” 也写“所有拘泥形式的东西”，“正式感”全书只在这里出现一次。照建议改为“一点点凿掉和人交谈时那些拘泥形式的东西和尴尬”，读者能看出和第 4 章说的是同一件事。译者自检“未决”里请用户确认的“正式感”一项随之不再需要。
  - “You’re a traditional business or sales person”：原译“做传统商务或销售的”，“传统商务”容易读成和电子商务相对的线下生意。照建议改为“传统企业出身的商务或销售人员”，和后半句“还没找到商业模式的年轻公司”形成对照。
  - “want to help them have more useful customer conversations”：原译“把客户对话谈得更有用”，搭配别扭。审校者建议“从客户对话里得到更多有用的东西”，意思偏到了对话的结果上；编辑改为“把客户对话谈得更有收获”，被改进的仍是对话本身，“收获”也是术语表给名词 learning 定的译法。
  - “want to start making real progress today”：原译“从今天起开始”，“起”和“开始”重复。审校者给了两种写法，第一种删掉“开始”，start 就没有译出来；编辑取第二种的句式，保留原译的“实实在在的进展”，改为“想今天就开始取得实实在在的进展”。
  - “Does your shelf really need another book on selling and talking? And does it need one written by me in particular?”：原译“还需要再多一本”三个字意思重叠，“还偏偏需要一本我写的？”拗口。审校者建议第二问写“还非得是我写的？”，可下一段回答的是“需要。确实需要。”，问句里最好仍有“要”字和它呼应。改为“你的书架上真的还需要多一本讲销售和交谈的书吗？而且，还非得要一本我写的吗？”
  - 照建议改的其余 5 条：
    - “it didn’t look like we’d be getting more”：“看样子也拿不到更多”没有宾语，改为“看样子也融不到新的钱了”。
    - “They forget to mention that it’s hard.”：原文 They 指给这类建议的人，中文的“他们”紧跟在人缘好的孩子和书呆子朋友之后，容易读成这两个孩子。改为“说这种话的人都忘了提一句：这事很难。”
    - “Bad customer conversations aren’t just useless.”：“不光是没用。”用句号收住，读着像没说完，改为“可不只是没用而已。”
    - “Even when you’re not actively screwing something up”：actively 说的是由你自己的做法造成，“主动搞砸”会读成故意搞砸，改为“就算你自己没把什么事搞砸”。
    - “Throughout the book, I’ll try to help you figure out where you might be messing stuff up in unnoticed ways.”：句首“这本书从头到尾”和主语“我”接不上，改为“在整本书里，我都会尽力帮你找出：你可能在哪些地方不知不觉就把事情搞砸了。”
- 不采纳 1 条：
  - “This book is a practical how-to.”：审校者建议把“这本书是一本实用的操作指南”改成“这是一本实用的操作指南”，理由是“这本书”和“一本”重复。“这本书是一本……”是很平常的中文说法，读起来不卡；改成“这是一本”以后，这一段和紧接着的下一段（“这是一种轻松随意的对话方法”）都以“这是一”开头，重复反而更明显。保留原译。
- 审校者的总体判断：引言译文整体质量好，改完这些小问题后可以进入中文通读。38 个块和英文逐块对应；逐块对照后没有发现意义错误、漏译、增译、否定用错或数字问题（3 years 写“三年”，a hundred times over 写“上百次”）；史蒂夫·布兰克第一次出现时括注了英文，两本书名照术语表写并括注斜体原题，客户开发、精益创业、客户对话、了解客户、假阳性、会面等术语和 Habit、MTV、索尼都和术语表一致；5 处斜体和英文一一对应；全文没有破折号，也没有体例禁用的对比句式；开头几段的考古比喻和作者自嘲的口吻保留得很好。问题集中在一处术语（formality）和十处读起来不够顺的措辞。

## 3. 中文通读

- 执行者：编辑 agent（Opus 5.5）。
- 范围：采纳审校意见之后，从节首顺着中文读到节末，看行文是否连贯、有没有重复、指代是否清楚、人名和术语前后是否一致。
- 发现并修改 1 处，改后回查了英文：
  - “They are, in one way or another, forcing people to say something nice about their business. They use heavy-handed questions like ...”：中文两句里连着出现“他们用……”“他们的生意”“他们问……”，三个“他们”读着重复。第三句去掉主语，改为“问起问题来生硬粗暴，比如“你觉得这个想法好吗”，结果把自己想要的宝贝打得粉碎。”主语承接上一句的团队，前后都是团队在做事，不会被读成被逼着说好话的人；heavy-handed questions 和 shatter their prize 的意思都还在。
- 读过后保留的地方：
  - 第 1 段“但工具要是太粗笨，你很可能把它砸成无数碎片”：“它”离“工具”更近，但前一句“可它很容易碎”已经把真相立为话题，读者会顺着话题理解成真相，保留。
  - 最后一节连用三次“这本书”（“这本书不是……”“这本书专门讲……”“这本书讲……”），英文也连用三次 This book，作者是在一条条划清范围，保留。
  - “数不清的”出现两次，分别对应英文的两处 innumerable，保留。
  - 采纳审校意见后的几处（“融不到新的钱了”“说这种话的人”“拘泥形式的东西”等）和上下文读着连贯，没有带出新的重复。
- 人名和术语：史蒂夫·布兰克只在第一次出现时括注英文；客户开发、精益创业、客户对话、和客户交谈、会面、了解客户、假阳性、创始人、创业公司前后写法一致。
- 检查结果：`site.py status` 显示 38/38；`term_consistency.py` 没有标出本节的块；`site.py check` 草稿构建通过，只有字体子集缺字的警告；全节没有破折号，也没有体例禁用的对比句式。

## 状态

- 本节没有未解决的意义问题，也没有原文疑点。
- 还要等用户确认的译法（来自译者自检，这次没有变化）：“Hello,” 写“你好：”；小标题 “Why another book on talking and selling?” 和 “A note on scope & terminology” 的译法；“textbooks and check books” 不加译者注；客户开发、精益创业第一次出现时要不要括注英文。formality 一项已照术语表改为“拘泥形式”，不再需要确认。
- 阅读器校样还没有做；`book.json` 里本节的状态由主会话修改。

## 第三轮：GPT-6 Astra 独立审校

- 审校者：GPT-6 Astra，通过 Codex 运行，只读，和译者属于不同的模型家族。
- 发现：0 条。审校者逐块核对了全部中英文，总体意见是“译文完整、准确，未发现需要修改的实质问题”，也没有提出对英文原文的疑问。没有需要逐条找中英文核实的条目：成立并修改 0 条，不成立 0 条。
- 成立并修改：无。
- 不成立，保留原译：无。
- 按全书统一的写法修改：0 处。对照术语表“全书统一的写法”和“全书统一的写法（译完后定）”两节逐条核对了本节，各条都已经照规定写：
  - 数字：3 years 写“三年”，a hundred times over 写“上百次”；本节没有金额、章节引用和平台名。
  - 人名和书名括注：史蒂夫·布兰克（Steve Blank）、《四步创业法》（*4 Steps to the E.piphany*）、《创业者手册》（*The Startup Owner’s Manual*）都只在第一次出现时括注一次。
  - 作者命名的概念：客户开发、精益创业第一次出现时直接写中文；区分客户对话（customer conversation，小写）和客户开发（Customer Development，大写）的一句保留括注。
  - 单条规定：“Don’t call me, I’ll call you.” 写“别给我打电话，我会打给你”；go wrong in a nefarious way 写“出错的方式很阴险”；traditional business or sales person 写“传统企业出身的商务或销售人员”；formality 写“拘泥形式的东西”。
- 按体例“破折号和句式”一条另改 2 处。英文的 “X, not Y” 在其他各章都改成了直接的说法，例如第 2 章“你要的是事实和承诺，用不着恭维”，第 8 章“和客户交谈是一种工具，你没有义务非做不可”；全书只剩本节这两句还写成“是 X，不是 Y”的对比句式，照其他各章改成直接的说法：
  - “Firstly, I’m a techie, not a sales guy.”：原译“第一，我是搞技术的，不是干销售的。”，改为“第一，我是搞技术的，干销售是外行。”下一句“我性格内向，天生不擅长应付会面”接着说他不会和人打交道，前后连贯。
  - “Finally, this is a practical handbook, not a theoretical tome.”：原译“最后，这是一本实用手册，不是厚重的理论著作。”，改为“最后，这是一本实用手册，不讲厚重的理论。”后面举的例子（怎样找到可以交谈的人、怎样一边记笔记一边专心听）都是实际做法，和改后的说法接得上。
- 对英文原文的疑问：无。审校者没有提出；核实时也没有发现影响理解的笔误，`review/source.md` 的“原文疑点”里没有本节的条目。
- 核实与修改：agent（Opus 5.5）。改完后运行 `python3 scripts/site.py status the-mom-test`：引言 38/38 块已翻译，原文没有注释，注释一栏为空；全书 873/873 块已翻译。`tools/term_consistency.py` 没有标出本节的块。全节仍然没有破折号。
