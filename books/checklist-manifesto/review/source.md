# 原文核对

## 来源

- 文件：用户提供的 EPUB，文件名 `Gawande - The Checklist Manifesto.epub`。整理时复制成 `book.epub` 使用，两份文件的 SHA-256 相同（`9d0092845a0b7f0df0c095b9c749f174fe479e9d4566dccba642cc65639d2c2d`），记在 `book.json` 的 `source` 里。EPUB 本身不放进仓库。
- 版本：英国 Profile Books 2010 年版《The Checklist Manifesto: How to Get Things Right》，电子书 ISBN 978-1-84765-187-7。版权页写明这本书 2009 年先由美国 Metropolitan Books（Henry Holt 旗下）出版，部分内容以不同的形式发表在《纽约客》的文章《The Checklist》里。EPUB 用 Sigil 0.1.9 制作，元数据里的出版日期 2000-01-01 是占位值。
- 正文没有乱码，左右双引号各 412 个，成对。转换留下的问题主要是空格：有些词连在了一起（`harmof`、`I gave hima call`），有些词被纸质版换行处的连字符拆开（`Hager-man`），英文破折号后面多出空格。处理方法见下文。

## EPUB 的结构

| 内容 | 在 EPUB 里的写法 |
| --- | --- |
| 分节和顺序 | 22 个 XHTML 文件，按 spine 排列。目录（`toc.ncx`）列出封面、书名页、版权页、献辞、目录、引言、第 1 到 9 章、Notes on Sources 和致谢；作者简介在 spine 里，目录里没有 |
| 标题 | class 为 `h9` 的段落，全部大写（`1. THE PROBLEM OF EXTREME COMPLEXITY`），里面是链回目录页的链接。EPUB 没有用 `<h1>` 这类标题标签 |
| 章内分节 | 新一节的第一段 class 为 `tx1`，前几个词是粗体（纸质版的小型大写字母），前面没有分隔符号。每章第一段另外带 `sgc-11` 类 |
| 引文 | 第 6 章驾驶舱录音的三段引文是 `<div class="ext">`，一句话一个段落 |
| 斜体 | `<i>`。书名常被拆成两段（`<i>New England</i> <i>Journal</i>`） |
| 注释 | 书末的 Notes on Sources 按章分组，共 82 条，第 9 章没有注释。每条以纸质版页码和引用的词句开头，例如 `7 “In the 1970s”: S. Gorovitz and A. MacIntyre, …`。正文里没有注释编号，也没有链接 |
| 星号注释 | 引言里 “his heart suddenly stopped.*” 有一个星号，EPUB 里没有对应的注释文字 |
| 图片 | 封面（1043×1600）、书名页的 Profile Books 标志、版权页的 FSC 标志，还有一个没有被任何页面引用的 11×10 像素小图。书里没有清单的插图，书中的各张清单都是在正文里用文字描述的 |
| 列表、表格 | 没有 |

## 导入和整理

```bash
uv run --project framework/tools python -I books/checklist-manifesto/tools/prepare_epub.py book.epub prepared.epub
python3 scripts/site.py import-epub checklist-manifesto prepared.epub --force
uv run --project framework/tools python -I books/checklist-manifesto/tools/curate_source.py book.epub
uv run --project framework/tools python -I books/checklist-manifesto/tools/check_source.py book.epub
```

这几步可以重复运行，每次都从原始 EPUB 重新生成 `en/`，结果相同。

`tools/prepare_epub.py` 先复制一份 EPUB，在副本里做五件事，导入器才能认出这本书的结构：

- `h9` 段落改成 `<h1>`，去掉里面链回目录页的链接；注释里按章分组的 `h6` 段落改成 `<h2>`。
- 三段驾驶舱录音的 `<div class="ext">` 改成 `<blockquote>`。
- 分节的开头段落去掉粗体，段落前面加一条分隔线；每章的第一段只去掉粗体。共 33 条分隔线。
- 拆成两段的斜体合并成一段。
- 注释里的链接改成纯文字，这些链接的目标本身是错的（结尾带句点、`www%20.census.gov`、单独一个 `http://`）。

`tools/curate_source.py` 再整理导入结果：

| 问题 | 处理 |
| --- | --- |
| “also by” 页、两张半书名页、印着作者名的页、书名页、版权页被导成了章节 | 删除。EPUB 的封面图改作书架封面 `assets/images/cover.jpg`；书名页和版权页上的两个标志图一起删掉 |
| 82 条注释集中在书末 | 每条放进所属章节，成为脚注 `[^n]`，位置在注释引用的词句后面；引用的话以引号结束时，放在右引号后面。每章按注释的顺序向后查找。只有第 5 章的 “After three months” 在正文出现两次，按顺序取第二处，和注释的内容（Makary 等人关于术前简报的研究）相符。纸质版页码去掉。82 条全部找到了位置，所以不再保留单独的注释节 |
| 引言的星号注释没有文字 | 按美国版第 4 页的脚注补回 “Identifying details were changed at John’s request.”，作为引言的第 1 条脚注，见“原文疑点” |
| 标题全大写 | 改成一般的大小写，每节一个一级标题；编号章节写成 “# 1. The Problem of Extreme Complexity”，`book.json` 里有 `number` |
| 章节 id | dedication、introduction、ch01 到 ch09、acknowledgments、about-the-author；第一次打开时进入引言 |
| 22 处两个词连在一起 | 补上空格：victim is、PERSONNEL ONLY、and maintaining、one million、harm of、Ghana was、how sick、So what（原作 “Sowh at”）、team briefing、him a call、problem of、get missed、right main、momentum and、no matter（2 处）、them to、couldn’t work、for making、as much、by missed、generally well |
| 标点后面缺空格 | `*Food and Wine*magazine`、`philosophy.”When`、`side.”)We’ve`、`CAPTAIN:What`、`ENGINEER:What` 补上空格 |
| 词被换行处的连字符或空格拆开 | 合并成 O’Sullivan、Hagerman、Donaldson、overwhelmed（原作 “over whelmed”）；`line-byline` 改成 line-by-line。这几个名字在书里其他地方都是完整的写法 |
| 多余的空格 | 英文破折号后面的空格删掉（正文 50 处，纸质版换行留下的）；词尾 f 和后面的引号、撇号之间的空格删掉（正文 4 处，例如 “staff ’s”，注释 2 处） |
| 注释里的转换错误 | 三处 `”:M.` 和 `New York:William`、`eds.,*World`、`blog,*Wall`、`A-09-17-18,”Washington` 补上空格；`www .census.gov`、`http:// www.slate.com`、`middleseat/2009/02/ 09/` 去掉多余的空格；Rose-grant 改成 Rosegrant，Human- Computer 改成 Human-Computer |

每一处修正都写在脚本的 `FIXES` 和 `NOTE_FIXES` 里，并检查出现的次数，原文变了脚本就会报错。

## 完整性核对

`tools/check_source.py` 拿原始 EPUB（没有经过 `prepare_epub.py` 的那份）逐节核对：

- **词数**：连续的字母和数字算一个词，两边都不算标题。每节的差额必须正好等于修正带来的增减：连在一起的词拆开后多一个词，被拆开的词合并后少一个词。脚本自动核对这一点。
- **段落**：逐段比较字母和数字，每节的段落和 EPUB 一一对应，顺序相同，没有漏段、重复或错位。另外检查了全书：超过 40 个字符的段落没有出现两次的。
- **斜体**：每节 `<i>` 里的字母和 `*…*` 里的字母完全相同。
- **分节**：每节的分隔线数等于 EPUB 里粗体开头的 `tx1` 段落数。
- **注释**：82 条注释（去掉页码）各对应一条脚注，每条只出现一次；多出的一条是补回的星号注释。正文里没有剩下的标记、指向 EPUB 文件的链接或粗体。

| 节 | EPUB 词数 | en/ 词数 | 差额 | 差额的来源 | 段落 | 分隔线 | 脚注 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| dedication | 5 | 5 | 0 |  | 1 | 0 | 0 |
| introduction | 3682 | 3682 | 0 |  | 54 | 3 | 7 |
| ch01 | 4972 | 4973 | +1 | victim is | 44 | 2 | 9 |
| ch02 | 4423 | 4423 | 0 |  | 48 | 2 | 10 |
| ch03 | 7158 | 7159 | +1 | PERSONNEL ONLY、line-by-line 各加 1，O’Sullivan 减 1 | 79 | 5 | 6 |
| ch04 | 3941 | 3942 | +1 | and maintaining、Wine magazine 各加 1，overwhelmed 减 1 | 47 | 2 | 6 |
| ch05 | 7924 | 7929 | +5 | 5 处连在一起的词（So what 不改变词数） | 97 | 5 | 13 |
| ch06 | 6214 | 6221 | +7 | 7 处连在一起的词 | 92 | 3 | 14 |
| ch07 | 6178 | 6180 | +2 | them to、couldn’t work | 69 | 5 | 5 |
| ch08 | 8384 | 8387 | +3 | for making、as much、by missed | 101 | 6 | 13 |
| ch09 | 2060 | 2060 | 0 | generally well 加 1，Hagerman 减 1 | 24 | 0 | 0 |
| acknowledgments | 1070 | 1069 | −1 | Donaldson | 10 | 0 | 0 |
| about-the-author | 72 | 72 | 0 |  | 1 | 0 | 0 |
| 合计 | 56083 | 56102 | +19 |  | 667 | 33 | 83 |

注释：EPUB 的 Notes on Sources 共 2179 个词，其中 82 个是页码；脚注共 2104 个词，等于 2179 减去 82 个页码，减去 Rosegrant 合并的 1 个，再加上补回的星号注释的 8 个。

## 保留的结构

献辞、引言、第 1 到 9 章、致谢、作者简介，共 13 节、666 个块、83 条脚注。目录页、书名页、版权页、“also by” 页和半书名页不需要翻译，已经删掉；Notes on Sources 的内容全部成了脚注。

## 原文疑点

| 位置 | 原文 | 处理 |
| --- | --- | --- |
| 引言，“his heart suddenly stopped.*” | EPUB 只有星号，没有注释文字 | 文字取自网上可以读到的美国 Metropolitan 版全文扫描本第 4 页的脚注，只核对了这一句。英国版纸质书没有核对 |
| 第 3 章注释 3（“We’ve been slow to adapt”） | 网址写作 www.darmouthatlas.org，正确的是 www.dartmouthatlas.org | 英文照原文保留，翻译时可以加译者注 |
| 全部注释 | 开头的页码是纸质版的页码，和电子书无关 | 改成脚注后去掉 |
| EPUB 的封面页 | `<title>` 写作 “An Optimist’s Tour of the Future”（Profile Books 另一本书的书名），OPF 里的封面引用指向不存在的 `images/img0004.jpg` | 制作时的遗留，和正文无关，不处理 |
| 全书 | 连在一起的词是用词频表（wordfreq）查出来的，两个词连起来恰好也是常见词时查不出来；被空格拆开的词也一样 | 翻译时遇到读不通的地方，再对照纸质版 |

英文照原文保留，`en/` 只修转换造成的问题；书的拼写（如 detectible）、注释里的 Air&Space 等写法都没有改。
