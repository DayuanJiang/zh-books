# 原文核对

## 来源

- 文件：用户提供的 PDF（`book.pdf`，260 页），SHA-256 记在 `book.json` 的 `source` 里。PDF 本身不放进仓库。
- 制作方式：PDF 的元数据写着 calibre 6.4.0，2023 年 3 月 2 日生成，是用 calibre 把电子书转成的 PDF。页面上是真正的文字（有字体名、字号和斜体标记），可以直接提取，不需要 OCR。没有页眉、页脚和页码。
- 版本：版权页写的是英国 Macmillan 2023 年的电子版（This electronic edition first published in the UK 2023 by Macmillan），ISBN 978-1-0350-1896-3；原书 2023 年先由美国 Currency（Random House 旗下）出版。书名页的副标题是英国版的 “The Surprising Factors Behind Every Successful Project, from Home Renovations to Space Exploration”，美国版的副标题是 “The Surprising Factors That Determine the Fate of Every Project, from Home Renovations to Space Exploration and Everything In Between”。`book.json` 的原书名按这份 PDF 的书名页填写。
- 中文书名：这本书已有中文版《怎样做成大事》（浙江科学技术出版社，2024 年 3 月，作者译名傅以斌、丹·加德纳），书架上的中文书名沿用它。

## PDF 的结构

| 内容 | PDF 里的样子 | 处理 |
| --- | --- | --- |
| 分节 | PDF 书签列出每一节和它的起始页 | 一节从书签的页开始，到下一节的前一页结束 |
| 节的标题区 | 无衬线体 16.9 磅以上：章号（“1”“CODA”“APPENDIX A”）和大写的标题，下面一条装饰线（小图片） | 标题用书签里的写法（“1. Think Slow, Act Fast”），装饰线不要 |
| 章首导语 | 标题下面居中的几行衬线斜体 | 一个斜体段落，放在标题后面 |
| 小节标题 | 无衬线体 15 磅，全部大写，长的分两行 | `##` 标题，改成标题大小写（见下文） |
| 正文 | 衬线体 15 磅；段首缩进（x 约 92），续行顶格（x 约 77）；跨页的段落在下一页顶格接着写 | 缩进的行或标题、图片、表格之后的行开始新段落，顶格的行接上一段 |
| 注释编号 | 正文里 11.2 磅的上标数字，每章从 1 编起；PDF 链接指向书末 Notes 里的那一条，注释编号也链回正文 | 按链接找到注释，改成这一节的脚注 `[^n]`，放在上标原来的位置 |
| 书末注释 | Notes 一节（第 190 到 215 页），按章分组，组名是大写的章名；悬挂缩进 | 每条注释成为所在章节的脚注 |
| 星号注 | Footnotes 一节（第 189 页）只有两条，都属于附录 A：一条注在附录标题上，一条注在表头上 | 附录 A 的脚注 1 和 2 |
| 表格 | 只有附录 A 一张表，无衬线体 11.2 磅，跨两页，第二页重复了表头 | Markdown 表格，重复的表头只留一次 |
| 图片 | 第 1 章、第 9 章共 3 张图表，图题印在图片里 | 存到 `en/images/`，写上英文替代文字 |
| 小型大写 | “4:00 A.M.” 里的 A.M 用小一号的字 | 照字母写成 A.M. |
| 列表、引文 | 正文里没有缩进的引文或列表；附录 B 的书目是悬挂缩进的小字 | 附录 B 的书目改成一个列表 |

## 导入和整理

```bash
uv run --with pymupdf python -I books/how-big-things-get-done/tools/import_pdf.py books/how-big-things-get-done book.pdf --force
uv run --with pymupdf python -I books/how-big-things-get-done/tools/curate_source.py book.pdf
uv run --with pymupdf python -I books/how-big-things-get-done/tools/verify_against_pdf.py books/how-big-things-get-done book.pdf
```

框架没有 PDF 导入器，`tools/import_pdf.py` 按上面的表格从字体和位置读出结构，输出和 EPUB 导入器相同的格式：每节一个 `en/NN-<slug>.md`，第一行是 `#` 标题，斜体写成 `*...*`，脚注写成 `[^n]` 并把定义放在引用它的那一节末尾，所有注释都搬走的注释节不再输出，章节按顺序写进 `book.json`，状态是 `todo`。接行的规则：两行之间加一个空格；上一行以连字符或破折号结尾、下一行以破折号开头时不加空格；网址跨行时（两行的末尾和开头属于 PDF 里同一个网址链接）也不加空格。calibre 排版时不会自动断词，行末的连字符都是原文里的连字符，所以保留。

导入结果：21 节，269 条注释全部按链接找到了引用位置，每条只被引用一次；每章的注释序号和书里印的编号一致。

`tools/curate_source.py` 再处理导入结果：

| 问题 | 处理 |
| --- | --- |
| 书名页、目录、参考文献、纸质版索引、版权页被导成了节 | 删除。参考文献里的书目在各条注释里都已写全；索引的条目只有 ref1、ref2 这样的链接，没有页码，用不上 |
| 节的 id 是从标题生成的长名字 | 改成 dedication、introduction、ch01 到 ch09、coda、appendix-a、appendix-b、acknowledgments、about-the-authors |
| 献辞的标题是书签里的 “Dedication page” | 改成 “Dedication”，文件改名为 `02-dedication.md` |
| 小节标题在 PDF 里全部大写 | 改成标题大小写（冠词、并列连词和介词小写，首尾词大写），斜体部分保留：例如 “Projects Don’t *Go* Wrong, They *Start* Wrong”“Back to *Experiri*”。“4:00 A.M.” 照原样 |
| 附录 A 的星号注标在标题上 | 移到第一句的 “cost overruns” 之后。阅读器的目录和页面标题直接用标题的原文，标题里的 `[^1]` 会显示出来 |
| 附录 A 的表头和 “SOURCE: FLYVBJERG DATABASE” 全部大写 | 改成普通大小写：“Project type”“(A) Mean cost overrun (%)”等，“Source: Flyvbjerg Database” |
| 附录 B 的书目是一条条小字段落 | 改成一个列表，开头的说明段落保留 |
| 三张图没有替代文字 | 按图题写英文替代文字 |
| 封面 | PDF 第 1 页的封面图存为 `assets/images/cover.jpg`，`book.json` 写上 `cover` 和 `start`（introduction） |

### 修正的乱码

电子书由纸质版转换而来，纸质版在行末断开的地方留下了两类错误：复合词的连字符丢了，或者断词用的连字符留在了词中间。另外有几处缺空格、缺句号。用词频表（wordfreq）找出不成词、拆开后是两个常见词的写法，再和书里别处的写法对照，逐条确认后修正。下表每一条在原文里只出现一次：

| 位置 | PDF 原文 | 改为 |
| --- | --- | --- |
| 第 4 章 | eradefining movies | era-defining movies |
| 第 4 章注释 | computeraided manufacturing | computer-aided manufacturing（同一句前面是 computer-aided design） |
| 第 5 章 | woodand-cardboard models | wood-and-cardboard models |
| 第 6 章 | a fattailed distribution | a fat-tailed distribution |
| 第 6 章 | comparable highspeed rail projects | comparable high-speed rail projects |
| 第 6 章 | lowerlevel employees | lower-level employees（同一句后面是 lower-level） |
| 第 6 章 | realworld experience | real-world experience |
| 第 7 章 | lowfrequency sound | low-frequency sound |
| 第 8 章 | crowded, rundown halls | crowded, run-down halls（第 1 章写作 run-down） |
| 第 9 章 | twentysix-story | twenty-six-story |
| 第 9 章 | everbigger developments | ever-bigger developments |
| 第 9 章 | governmentcreated framework | government-created framework |
| 第 9 章 | ribboncutting ceremony | ribbon-cutting ceremony |
| 致谢 | us factchecking | us fact-checking |
| 第 1 章 | a min-uscule 0.5 percent | a minuscule 0.5 percent |
| 第 5 章注释 | Domstols-styrelsen | Domstolsstyrelsen（丹麦法院管理局的正式名称） |
| 第 6 章注释 | økonomistyrings–model | økonomistyringsmodel（同一条注释里的另一处和参考文献里都这样写） |
| 第 9 章 | anticipate.That’s | anticipate. That’s |
| 第 9 章 | business.The most | business. The most |
| 第 9 章 | development.“Without | development. “Without |
| 第 1 章 | or both And 99.5 percent | or both. And 99.5 percent |
| 第 1 章 | But it almost never happens（段末没有句号） | 补上句号 |
| 第 1 章 | Graphically, the Iron Law looks like this（下面是图） | 补上冒号 |

没有改的写法：midconstruction、underinformed、scalewise、postpandemic 这类前缀词合写是美式拼法，照原文保留；作者造的 masterbuilder、inchstone 也照原文。

## 完整性核对

`tools/verify_against_pdf.py` 从 PDF 里按阅读顺序取出每节的全部词（不算节的标题和上标注释编号），和 `en/` 里的正文逐词比较（不算第一行标题、脚注定义和 Markdown 符号，不分大小写）；每章的注释也一样，PDF 里这一章名下的注释和这一节的脚注定义逐词比较。词按字母和数字的连续串计算，所以接行、连字符和破折号不影响结果。同时比较两边段落、标题、表格开始的位置。

| 节 | PDF 正文词数 | en 正文词数 | PDF 注释词数 | en 脚注词数 | 差异的原因 |
| --- | --- | --- | --- | --- | --- |
| dedication | 6 | 6 | 0 | 0 | |
| introduction | 2583 | 2583 | 725 | 725 | |
| ch01 | 5975 | 5974 | 1428 | 1428 | min-uscule 合成一个词 |
| ch02 | 6930 | 6930 | 1878 | 1878 | |
| ch03 | 5738 | 5738 | 411 | 411 | |
| ch04 | 6750 | 6751 | 870 | 871 | 正文 era-defining、注释 computer-aided 各补一个连字符 |
| ch05 | 5418 | 5419 | 2132 | 2131 | 正文 wood-and-cardboard 补连字符；注释 Domstolsstyrelsen 合成一个词 |
| ch06 | 10005 | 10009 | 3343 | 3340 | 正文补了 4 个连字符；注释里 økonomistyringsmodel 合成一个词；两个网址里的数字在 PDF 行末断开（例如 file/1 和下一行的 91507），核对脚本按行取词，各算成两个词；10¹⁴ 的上标 14 在 en 里是上标数字，不算词 |
| ch07 | 5111 | 5112 | 653 | 653 | low-frequency 补连字符 |
| ch08 | 4385 | 4386 | 715 | 715 | run-down 补连字符 |
| ch09 | 8773 | 8777 | 2197 | 2197 | 补了 4 个连字符 |
| coda | 1584 | 1584 | 454 | 454 | |
| appendix-a | 410 | 390 | 109 | 109 | 表头在 PDF 第二页重复了一次（20 个词），en 只留一次 |
| appendix-b | 1467 | 1467 | 0 | 0 | |
| acknowledgments | 1751 | 1752 | 0 | 0 | fact-checking 补连字符 |
| about-the-authors | 76 | 76 | 0 | 0 | |
| 合计 | 66962 | 66954 | 14915 | 14912 | |

除了表里写明的地方，两边的词序列完全相同，没有漏掉或重复的段落。段落、标题和表格的开始位置两边一致，只有作者简介一处：两位作者的简介在 PDF 里都顶格，中间空了一行，导入器按空行分成两段，核对脚本只看缩进，算作一段。

其他核对：

- 注释：269 条（书末注释 267 条，附录 A 的星号注 2 条）都成了脚注，每条只出现一次；每节的脚注从 1 连续编号，正文里的标记和定义一一对应，次序和书里印的编号相同。
- 斜体：每节斜体里的词和 PDF 斜体字里的词逐词相同（核对时用 Markdown 渲染结果里的 `<em>` 计算）。渲染后的文字里没有多余的星号。
- 图片：3 张图都在原来的位置，图片之间没有被拆开的段落。

`python3 scripts/site.py status how-big-things-get-done`：16 节，886 个块，269 条脚注。

## 保留的结构

献辞、引言、第 1 到 9 章、结语（Coda: Eleven Heuristics for Better Project Leadership）、附录 A、附录 B、致谢、作者简介，共 16 节。各章的章首导语保留为斜体段落。

## 原文疑点

导入时发现、没有改动英文的地方：

| 位置 | 原文 | 说明 |
| --- | --- | --- |
| 引言注释 12 | John Tauranc | 同一章注释 16 写作 Tauranac，作者名应为 John Tauranac。照原文保留，翻译时注意 |
| 附录 A、第 9 章 | The table on the next page、The chart on the next page | 指纸质版的版面，在阅读器里表格和图就在下面 |
| 第 7 章 | f \*\*\*ing | 原文星号前有一个空格，照原文保留 |
| 第 6 章注释 | archive.ph/20180320091111/ http://archive.defense.gov/... | 存档网址和原网址之间原文有空格，照原文保留 |
| 第 5 章注释 24，第 6 章注释 22、23 | 一条注释有好几段 | 框架的脚注定义只能写在一行里，几段合成了一段，文字没有变。别的注释也可能有段落在 PDF 上看不出来 |
| 第 1 章章首导语、献辞 | 不到 120 个字符的整段斜体 | 阅读器会把这样的段落显示成小标题样式；第 1 章的导语因此和其他各章的导语样子不同 |

## 用更好的来源补全（2026-11-05）

### 来源

- 文件：用户提供的 EPUB（`new.epub`，1.5 MB），SHA-256 `0fa295e39f1bb6b0ee444fb0fc2b38ff237be3ccfd85f73718b667f3a0642bf1`。EPUB 文件本身不放进仓库，处理时用的是 `/tmp/zh-books-merge/tmp/batch/update/how-big-things-get-done/` 下的副本，读取它的 Python 都用 `-I` 运行。`book.json` 的 `source` 仍然记 PDF，因为 en/ 是从 PDF 导入的。
- 版本：出版方 Pan Macmillan，ISBN 978-1-0350-1896-3，和 PDF 相同。版权页写 This electronic edition first published 2024 by Macmillan Business，OPF 的修改日期是 2024 年 4 月 10 日，所以它是 PDF 所依据的 2023 年电子版在 2024 年重新发行的文件。正文和注释和 PDF 逐词相同（见下文），只多了一页书评摘录（Praise）。
- 结构：XHTML 里有真正的标题、段落、斜体和上下标标记。Notes 一节有 267 条注释，按章分组，每条用链接连回正文；Footnotes 一节是附录 A 的 2 条星号注；Bibliography 一节有 580 条书目；附录 A 的表格是 HTML 表格；3 张图表和 PDF 里的是同一批文件。

### 怎样对照

```bash
uv run --with beautifulsoup4 python -I books/how-big-things-get-done/tools/compare_epub.py books/how-big-things-get-done <EPUB 副本> [--bibliography <输出文件>]
```

`tools/compare_epub.py` 把 EPUB 里属于 en/ 各节的文档转成本仓库的 Markdown 块：小节标题、段落、图片、表格和列表，斜体写成 `*...*`，注释标记按节编号写成 `[^n]`，注释正文放到引用它的那一节，一条注释有几段时用空格接成一段（和 en/ 的做法相同）。然后把这些块和 en/ 的文件逐块对齐，列出：只有一边有的块；词不同的块和改动的词；词相同、斜体或注释标记的位置不同的块；只有大小写不同的标题；每一条注释也做同样的比较；图片文件是否逐字节相同。空格、换行，以及列表和表格的 Markdown 符号，都不算差异。词数按空格分开的词计算，不算各节的标题、Markdown 符号和注释标记。加 `--bibliography` 时，脚本把 Bibliography 一节写成 Markdown。

### 对照结果

下表是补全后的结果。块数不算各节的 `#` 标题；“差异”一栏包括只有大小写不同的小节标题。

| 节 | 块数 en / EPUB | 注释 en / EPUB | 正文词数 en / EPUB | 注释词数 en / EPUB | 差异 |
| --- | --- | --- | --- | --- | --- |
| dedication | 1 / 1 | 0 / 0 | 6 / 6 | 0 / 0 | 0 |
| introduction | 38 / 38 | 18 / 18 | 2528 / 2528 | 633 / 633 | 2 |
| ch01 | 90 / 90 | 30 / 30 | 5799 / 5799 | 1289 / 1289 | 8 |
| ch02 | 84 / 84 | 39 / 39 | 6705 / 6705 | 1824 / 1824 | 10 |
| ch03 | 77 / 77 | 16 / 16 | 5562 / 5562 | 357 / 357 | 5 |
| ch04 | 89 / 89 | 27 / 27 | 6565 / 6565 | 800 / 800 | 9 |
| ch05 | 70 / 70 | 25 / 25 | 5263 / 5263 | 2084 / 2084 | 10 |
| ch06 | 128 / 128 | 32 / 32 | 9720 / 9720 | 3198 / 3198 | 15 |
| ch07 | 77 / 78 | 17 / 17 | 4939 / 4939 | 630 / 630 | 10 |
| ch08 | 60 / 60 | 13 / 13 | 4246 / 4246 | 662 / 662 | 5 |
| ch09 | 110 / 110 | 44 / 44 | 8518 / 8515 | 1875 / 1875 | 17 |
| coda | 24 / 24 | 6 / 6 | 1529 / 1529 | 425 / 425 | 11 |
| appendix-a | 5 / 5 | 2 / 2 | 469 / 469 | 104 / 104 | 3 |
| appendix-b | 2 / 2 | 0 / 0 | 1122 / 1122 | 0 / 0 | 0 |
| acknowledgments | 16 / 16 | 0 / 0 | 1714 / 1714 | 0 / 0 | 1 |
| bibliography | 1 / 1 | 0 / 0 | 12260 / 12256 | 0 / 0 | 1 |
| about-the-authors | 2 / 2 | 0 / 0 | 75 / 75 | 0 / 0 | 0 |

逐项的结论：

1. **缺少的节**：只缺参考文献（Bibliography）。补成新的一节 `bibliography`（`en/18-bibliography.md` 和 `zh-cn/18-bibliography.md`），放在致谢之后、作者简介之前，和 EPUB 的阅读顺序一致（EPUB 在这两节之间还有 Footnotes、Notes、Index 和 Praise：前两节的注释已经在各章里，后两节不收）。书目是一个 580 项的列表，照 EPUB 原样写：作者、年份、篇名、刊名或书名、出版地和出版社、卷期、页码和网址都是英文，斜体照写，链接写成网址的纯文字。中文文件只把标题译成“参考文献”，列表和英文逐字相同，做法和附录 B 的书目、注释里的出处一样。第一次整理时删掉参考文献，理由是书目在各条注释里都已写全；这次按要求把它作为书的内容补回来。书目里有两处缺空格，和正文的 23 处错字是同一类，改了：

   | 位置 | EPUB 原文 | 改为 |
   | --- | --- | --- |
   | 第 6 项（Adler 1993） | *Harvard Business Review*17 (1): 97–108. | *Harvard Business Review* 17 (1): 97–108. |
   | 第 231 项（Genus 1997） | Genus,Audley.1997.“Managing Large-Scale Technology … | Genus, Audley. 1997. “Managing Large-Scale Technology … |

   另外用词频表（wordfreq）查了书目里不成词、拆开后是两个常见词的写法，查出来的都是人名、网址片段或者正常的合成词（Megaprojects、Premortem、Antifragile 等），没有别的要改。
2. **缺少的图和表**：没有。en 的 3 张图（第 1 章的铁律柱状图，第 9 章从肥尾到瘦尾的散点图和中国新增装机容量图）和 EPUB 的 img_001 到 img_003 逐字节相同，位置也相同。EPUB 还有一张 img_004，是附录 A 表格的图片，在 XHTML 里被注释掉了，不显示。附录 A 的表格以 EPUB 的 HTML 表格为准，25 行、每行 3 个数字都和 en 相同，表头和 SOURCE: FLYVBJERG DATABASE 只有大小写不同（en 照第一次整理的决定写成普通大小写）。其余图片是封面、出版社标志和章首的装饰线。EPUB 给 3 张图写了很长的图片描述，en 保留第一次整理时写的简短替代文字。
3. **注释**：269 条全部对上。每节的条数、次序和标记的位置都和 EPUB 相同，267 条书末注释和 2 条星号注逐词相同，只有一处不同：第 1 章注释 8 的成本超支公式，EPUB 用下标写 C<sub>a</sub>、C<sub>e</sub>，PDF 导入时下标丢了，写成了 Ca、Ce。en 和 zh-cn 都改成 Unicode 的下标字符 Cₐ、Cₑ（公式里一处，后面的说明里各一处），和第 6 章注释里的 10¹⁴ 用上标字符的做法一致。附录 A 两条星号注的位置照第一次整理的决定（第 1 条从标题移到第一句的 cost overruns 后面）。EPUB 还标出了哪几条注释有好几段：第 5 章注释 24 和第 6 章注释 23 各有 5 段；上面原文疑点表里写的“第 6 章注释 22”其实只有一段。框架的脚注只能写在一行里，这两条注释仍然合成一段，文字不变。
4. **正文文字**：除了下面几类，en 和 EPUB 逐词相同：
   - **23 处错字**：EPUB 里 23 处都和 PDF 一样（eradefining、min-uscule、anticipate.That’s 等），可见这些错字在电子书里本来就有，PDF 转换没有带进新的错误。EPUB 给不出更好的写法，第一次整理的修正全部保留。
   - **小节标题的大小写**：EPUB 的 80 个小节标题也是用大写字母写成的文字（样式表里没有 text-transform），和 PDF 一样，所以没法用它核对大小写，第一次整理时改成的标题大小写照旧。各节的 `#` 标题和 EPUB 目录的写法相同；献辞在 EPUB 目录里叫 Dedication page，照第一次整理的决定写 Dedication。
   - **斜体**：只有一处写法不同：第 9 章注释 23 的刊名，EPUB 写成两段斜体（*International Railway* *Journal,*），en 写成一段，显示出来一样，不改。
   - **第 7 章的 f \*\*\*ing**：en 在星号前加了反斜杠，Markdown 显示出来的文字和 EPUB 相同。
   - **分段**：只有一处不同。第 7 章的章首导语在 EPUB 里分成两段，第二段只有一句 “But is it true?”；en 和 zh-cn 都是一段。这一处没有拆开：拆开后这一句成了不到 120 个字符的整段斜体，阅读器会把它显示成小标题的样式，读者容易当成小节标题。文字两边完全相同。要不要拆开，留给用户决定。
   - **第 6 章注释的 archive.ph 网址**：EPUB 里是两个分开的链接，中间有空格，照上面原文疑点表的处理保留。
5. **不收的部分**：书名页、目录、书评摘录（Praise）、纸质版索引和版权页照第一次整理的决定不收。书评摘录是 EPUB 比 PDF 多出来的一页，6 条推荐语，属于出版社的宣传材料；索引的条目在 EPUB 里也只有 ref1、ref2 这样的链接，没有页码。

### 改动

- 新增一节：参考文献（`bibliography`），`book.json` 里的状态是 `review`，2 个块（标题和 580 项的列表）。审校记录见 [bibliography.md](bibliography.md)。
- 改动的已有章节：第 1 章注释 8（en 和 zh-cn 各 3 处下标），记录见 [ch01.md](ch01.md) 的“补全后的改动”。
- `glossary.md`：“各节标题”加了参考文献一行，“体例”加了参考文献一条。`README.md` 的来源、内容和整理步骤改成现在的样子。
- 字体子集重新生成：参考文献里的 ç、ê、û、ć 和注释里的 ₐ、ₑ 原来不在子集里。

### 词数和块数

| | 补全前 | 补全后 |
| --- | --- | --- |
| 节数 | 16 | 17 |
| `site.py status` 的块数 | 886 | 888 |
| 脚注 | 269 | 269 |
| 正文词数（`compare_epub.py` 的算法，按空格分词） | 64760 | 77020 |
| 注释词数（同上） | 13881 | 13881 |
| 正文词数（`verify_against_pdf.py` 的算法，字母和数字的连续串） | 66954 | 80278 |

增加的词全部来自参考文献：按空格分词是 12260 个，按字母和数字的连续串是 13324 个（网址会拆成很多段，所以多一些）。

### 检查

- `python3 scripts/site.py status how-big-things-get-done`：17 节，888/888 个块，269 条脚注全部译出。
- `python3 scripts/site.py check how-big-things-get-done`：草稿构建通过；重新生成字体子集以后没有警告。
- 用 `framework/tools/build.py --drafts` 构建到 `/tmp`，在无头浏览器里打开参考文献一节：标题“参考文献”和 580 项的列表都正常显示，没有脚本错误。第 1 章的构建数据里，注释 8 带着下标字符。

### 未决

- 第 7 章的章首导语要不要照 EPUB 拆成两段（见上面第 4 条“分段”）。
