# 原文核对

## 来源

- 文件：用户提供的 EPUB（`Fitzpatrick - The Mom Test.epub`；这次任务拿到的副本叫 `book.epub`，两者 SHA-256 相同）。文件名和 SHA-256 记在 `book.json` 的 `source` 里。EPUB 本身不放进仓库。
- 版本：书名页写着 “v1.04”“@robfitz”“August, 2013”，书名是 “The Mom Test: how to talk to customers and learn if your business is a good idea when everybody is lying to you”，下面是 “by Rob Fitzpatrick” 和 “a foundercentric.com book”。这是作者自己出版的早期版本。网上还能查到 2014 年 8 月修订的 v1.06 和后来的 “Revised and Expanded Edition”，措辞和笔误与这一版有出入。这份译本以 v1.04 为准。
- EPUB 的制作：由文字处理软件导出（生成器是 Cocoa HTML Writer），没有封面图，也没有插图、表格、脚注或尾注。每个文件各带一份样式表，标题、对话、缩进的引文都只靠段落的字号和缩进区分。EPUB 在目录的每个条目处切开，一共 34 个文件，一章最多切成 6 个。

## 原书结构

目录（`toc.ncx`）依次是：书名页、目录页、Introduction（下设 Is this book for you?、Talking to customers is hard），第 1 到 8 章（各章下设若干小节），Conclusion and cheatsheet（下设 Cheatsheet、Thanks!、Acknowledgements）。

排版上的层次：

| EPUB 里的写法 | 含义 | `en/` 里的写法 |
| --- | --- | --- |
| 居中的 h2 “CHAPTER ONE” 加 327% 的 h3 | 章标题 | `# 1. The Mom Test` |
| 327% 的 h3 “Introduction”“Conclusion and cheatsheet” | 引言、结语的标题 | `# Introduction` |
| 164% 的段落或 h3 | 节标题 | `##` |
| 127% 的段落 | 小节标题，例如第 1 章逐条讨论的问题、第 6 章的 Cold calls | `###` |
| 加粗的短段落，例如 “A bad conversation:” | 对话或列表前的小标签 | 加粗段落，照原样 |
| 悬挂缩进的段落，开头是等宽字体的 “You:”“Mom:” | 示例对话，每句一段，后面的斜体是作者的旁白 | 每句一段，说话人加粗：`**You:** “…” *旁白*` |
| 左缩进的段落 | 引文：示范邮件、一句回话 | 引用块 `>`，一封邮件一个引用块 |
| 斜体的 “Rule of thumb:” | 每节末尾的经验法则 | 照原样保留斜体 |

## 保留的分节

| id | 文件 | 来自 EPUB 的文件 | 内容 |
| --- | --- | --- | --- |
| introduction | 01-introduction.md | body1 到 body3 | Introduction、Is this book for you?、Talking to customers is hard |
| ch01 | 02-1-the-mom-test.md | body4 到 body9 | 第 1 章 The Mom Test |
| ch02 | 03-2-avoiding-bad-data.md | body10 | 第 2 章 Avoiding bad data |
| ch03 | 04-3-asking-important-questions.md | body11、body12 | 第 3 章 Asking important questions |
| ch04 | 05-4-keeping-it-casual.md | body13、body14 | 第 4 章 Keeping it casual |
| ch05 | 06-5-commitment-and-advancement.md | body15 到 body19 | 第 5 章 Commitment and advancement |
| ch06 | 07-6-finding-conversations.md | body20 到 body24 | 第 6 章 Finding conversations |
| ch07 | 08-7-choosing-your-customers.md | body25 | 第 7 章 Choosing your customers |
| ch08 | 09-8-running-the-process.md | body26 到 body28 | 第 8 章 Running the process |
| conclusion | 10-conclusion-and-cheatsheet.md | body29 到 body31 | Conclusion and cheatsheet、Hack it、Cheatsheet、Thanks! |
| acknowledgments | 11-acknowledgements.md | body32 | Acknowledgements |

一共 11 节、873 个块，没有脚注。目录把 Thanks! 和 Acknowledgements 都放在结语下面：Thanks! 是作者的结束语，留在结语里；致谢单独成节，和仓库里其他书的做法一致。

去掉的两页：书名页（版本号、作者推特账号、日期、书名、作者、出版标记，共 33 个词）和目录页（28 个词）。

## 导入和整理

```bash
uv run --project framework/tools python -I books/the-mom-test/tools/prepare_epub.py book.epub prepared.epub
python3 scripts/site.py import-epub the-mom-test prepared.epub --force
uv run --project framework/tools python -I books/the-mom-test/tools/curate_source.py "Fitzpatrick - The Mom Test.epub"
uv run --project framework/tools python -I books/the-mom-test/tools/check_source.py "Fitzpatrick - The Mom Test.epub"
```

直接导入这个 EPUB 会丢掉大部分结构：标题只是字号不同的段落，对话的说话人只是换了字体，一章被切成好几个文件。所以先用 `tools/prepare_epub.py` 生成一份整理过的 EPUB 副本，再交给框架的导入工具；导入后由 `tools/curate_source.py` 做最后几处修改；`tools/check_source.py` 拿原始 EPUB 核对结果。

`tools/prepare_epub.py` 处理的问题：

| 问题 | 处理 |
| --- | --- |
| 一章分在最多 6 个文件里 | 按目录把同一章的文件合成一节；书名页和目录页不收 |
| 标题靠段落字号区分 | 按上面的层次表改成 h1、h2、h3；章标题写成 “1. The Mom Test”，原来的 “CHAPTER ONE” 去掉 |
| 对话的说话人是等宽字体 | 改成粗体 |
| 缩进的段落 | 示范邮件和回话改成引用块。第 1 章 “Good question / bad question” 和第 5 章 “Good meeting / bad meeting” 开头那两组待判断的问题（14 句、8 句），原文称作 “the list”，改成无序列表 |
| 文字处理软件把列表拆成两个，第二个从 1 重新编号（第 7 章 “three problems” 和 “3 ways to end up…” 两处，后一处的正文接着用 “#1” 指称第一项；Customer slicing 下的三个问题也拆成了两个列表） | 合回一个列表，编号连续 |
| 速查表的 “Mistakes and symptoms” 是六个各自只有一项的编号列表，每项下面跟着症状（第一项的症状是两段缩进文字，其余是无序列表），导入后会显示成六个 “1.” | 合成一个 1 到 6 的编号列表，症状作为各项下面的子列表 |
| 第 8 章和速查表的笔记符号是 “符号、制表符、含义” 的段落 | 每组改成一个无序列表，例如 “- :) Excited” |
| 符号总览一行里 “☑＄♀☆” 连在一起 | 在符号之间加空格 |
| 空的分隔段落、空的列表项（第 8 章 “Signs you’re just going through the motions” 的第一项）、空的粗体和斜体 | 删除 |
| 斜体和粗体里带着首尾空格（如 “Rule of thumb: ” 的斜体包含结尾空格），还有不少多余的空格 | 空格移到强调标记外面，连续的空白合成一个空格 |
| 第 1 章 “I was figuring out where we could stay.” 后面的引号打成了左引号，前面还多一个空格 | 改成右引号 |

`tools/curate_source.py` 处理的问题：

| 问题 | 处理 |
| --- | --- |
| 导入工具按标题生成的 id | 改成 `conclusion`、`acknowledgments`；`start` 设为 `introduction`；`source` 记原始 EPUB，不记整理后的副本 |
| 速查表 “The process before, during and after the meeting” 下面是三个连着的列表（会前、会中、会后），中间没有小标题。Markdown 会把连在一起、用同一种列表符号的列表合成一个 | 中间那个列表的符号改用 `*`，三个列表保持分开。**译文也要这样写**，否则中英两边的块对不上 |
| 第 6 章示范邮件里 “(*pedestal)*…” 的斜体把右括号也包进去了 | 改成 “(*pedestal*)…”，和同一段的其他括注一致 |

EPUB 没有封面图，`book.json` 的 `cover` 留空，书架上显示书名。

## 完整性核对

`tools/check_source.py` 逐节比较原始 EPUB 和 `en/`：

- 词数：含字母或数字的、以空白分隔的词，EPUB 一侧数这一节对应文件的全部文字，`en/` 一侧数 Markdown 里的标题、段落、列表项和引文。
- 词序：两边的字母和数字按顺序连成一串，必须完全相同，这样能查出漏掉、多出或挪了位置的文字。
- 段落：EPUB 里每个非空的段落、标题和列表项，都要在 `en/` 里找到恰好一个文字相同的块，反过来也一样。

结果：11 节的词数、词序和段落全部一致。

| 节 | EPUB 词数 | `en/` 词数 | 段落、标题和列表项（EPUB / `en/`） |
| --- | --- | --- | --- |
| introduction | 1175 | 1175 | 38 / 38 |
| ch01 | 3754 | 3754 | 134 / 134 |
| ch02 | 4557 | 4557 | 181 / 181 |
| ch03 | 4619 | 4619 | 125 / 125 |
| ch04 | 1821 | 1821 | 40 / 40 |
| ch05 | 2768 | 2768 | 110 / 110 |
| ch06 | 3943 | 3943 | 121 / 121 |
| ch07 | 2834 | 2834 | 71 / 71 |
| ch08 | 3403 | 3403 | 130 / 130 |
| conclusion | 1437 | 1437 | 121 / 121 |
| acknowledgments | 294 | 294 | 8 / 8 |
| 合计 | 30605 | 30605 | 1079 / 1079 |

两边都不算的只有 8 个章标签 “CHAPTER ONE” 到 “CHAPTER EIGHT”（16 个词），它们在 `en/` 里变成了章标题前的数字 “1.” 到 “8.”。算上这 16 个词，EPUB 正文文件一共 30621 个词。书里没有注释，`en/` 里也没有脚注标记。

此外在阅读器的草稿预览里（临时副本，状态改成 `draft`）看过第 1 章的对话、第 6 章的示范邮件、第 8 章的笔记符号和速查表：说话人粗体、旁白斜体、引用块、嵌套列表和三个分开的列表都显示正常，页面没有脚本错误。

## 原文疑点

这一版是作者自己出版的早期版本，笔误比较多。`en/` 照原文保留作者的文字，只修上面列出的导入和排版问题。翻译时按作者显然要表达的意思译出；会影响理解的地方，可以加译者注。

| 位置 | 原文 | 说明 |
| --- | --- | --- |
| 第 1 章 Passing the mom test | so answer to this probably won’t be terribly valuable | 少了 the |
| 第 1 章 Passing the mom test | The gift market may be strong . | 句号前多一个空格 |
| 第 1 章 A useful conversation | let’s let’s put The Mom Test to work | let’s 重复 |
| 第 1 章 Using the mom test | Before we move look at ways to confirm | move 多余，或少了 on to |
| 第 1 章 | 问题小标题用直引号（"Do you think it's a good idea?"），前面列表里的同一批问题用弯引号 | 原文如此，照原样保留 |
| 第 2 章 Dig beneath ideas | I really think that’s the a killer feature. | the 和 a 重复 |
| 第 2 章 Dig beneath ideas | accepting the feature request and face value | 应为 at face value |
| 第 2 章 Dig beneath ideas | push back the launch add that feature | 少了 to |
| 第 2 章 Dig beneath ideas | 问题列表最后一项 How would that fit into your day? 没有引号 | 其他各项都有引号 |
| 第 2 章 Stop seeking approval | need someone’s blessing take the leap | 少了 to |
| 第 2 章 Stop seeking approval | Gordon Ramsey | 厨师的名字拼作 Ramsay |
| 第 2、3、5、7 章 | (e.g. fluffy)、(e.g. you’re selling a painkiller)、(e.g. fishing for compliments)、(e.g. What is their problem or goal) 等 | 作者把 e.g. 当 i.e. 用，意思是“也就是”，按这个意思译 |
| 第 3 章 Love bad news | we avoid important question；this we need to learn to love bad news | question 少了复数；this 多余 |
| 第 3 章 Look before you zoom | You: What are your big problems with marketing? 和下一句 You: What are your big problems right now? | 这两句对话没有引号 |
| 第 4 章 How long are meetings? | you've liable to burn 15 minutes | 应为 you're liable |
| 第 4 章 How long are meetings? | The potential speed of the early conversations one of the big reasons | 少了 is |
| 第 4 章 | go to a industry meet-up | 应为 an |
| 第 5 章 Don't pitch blind | figuring out what’s unique about this particular person feels | 句尾的 feels 无法接上前文，大意是弄清眼前这个人有什么特别之处 |
| 第 6 章 Find a good excuse | You’ve go the ultimate excuse | 应为 got |
| 第 6 章 Organise meetups | if I got moved a new industry | 少了 to |
| 第 6 章 7 degrees of bacon | 小标题和经验法则都写 7 degrees，Kevin Bacon’s 7 degrees of separation | 通行的说法是 six degrees，作者的写法照原样译 |
| 第 6 章 Asking for and framing the meeting | both set set off alarm bells；Find a clever ways | set 重复；a 多余 |
| 第 6 章 To commute or to call | They’re enjoying the conversation | 段末缺句号 |
| 第 7 章 Segmentation | Paypal、EBay | 公司名通常写作 PayPal、eBay |
| 第 7 章 Customer slicing | Going out and talking to people is that it takes time. | 句子残缺，大意是“出去和人交谈的问题在于很花时间” |
| 第 7 章 Customer slicing | We now have a two groups；who also and meets the three big criteria | a 多余；and 多余 |
| 第 7 章 Talking to the wrong people | There are 3 ways to end up fall into this；If you’re building an app for kids, need to “sell” | end up 和 fall 重复；少了 you |
| 第 8 章 开头 | the customer and learning has to be shared | 大意是“客户方面的了解” |
| 第 8 章 This stuff is fast | This book isn’t meant you an excuse | 少了 to give |
| 第 8 章 This stuff is fast | catch any badgers in the bush, so to speak | 这个说法不常见，作者自己也加了 so to speak，按“及早发现潜在的问题”这个意思译 |
| 结语 Cheatsheet | Being a learning bottleneck 下的第三项，结尾 I need to be coding! | 缺右引号 |
| 结语 Cheatsheet | 速查表的部分列表比正文多一项，例如 Being too formal 下的 “Let’s set up a meeting.”、going through the motions 下的 “You aren’t sure why you’re having the meeting” | 原文如此，照译 |
| 结语 Thanks! | 链接文字是 aloha@foundercentric.com，链接地址是 mailto:mom@foundercentric.com | 两者不一致，照原样保留；这些网址和邮箱是 2013 年的，现在未必有效 |
| 致谢 | The author image is provided by heisenbergmedia.com | 这个 EPUB 里没有作者照片 |

## 留给后面步骤的事

- 笔记符号 ☇、⨅、☐、⤴、☑、＄、♀、☆ 不一定在阅读器的中文字体子集里，会用读者系统里的字体显示。做阅读器校样时要看一下这些符号在电脑和手机上是否都能显示。
- 对话里说话人的粗体、旁白的斜体、“Rule of thumb:” 的斜体，译文要照同样的格式写。
