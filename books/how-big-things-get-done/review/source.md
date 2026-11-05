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
