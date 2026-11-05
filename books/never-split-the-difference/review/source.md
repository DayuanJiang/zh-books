# 原文核对

## 来源

- 文件：用户提供的 EPUB（`book.epub`，324 KB），SHA-256 记在 `book.json` 的 `source` 里。EPUB 本身不放进仓库。
- 版本：calibre 5.15.0 在 2021 年 4 月 12 日重新打包的 HarperCollins 电子书。元数据里的 ISBN 9780062407801 是 HarperBusiness 2016 年的精装本；正文文件的 `body` 标记为 `x9780062407818`，这是 HarperCollins 电子书的 ISBN（2016 年 5 月 17 日发行）。书名以封面和 HarperCollins 的书目为准：《Never Split the Difference: Negotiating As If Your Life Depended On It》，Chris Voss with Tahl Raz。
- 范围：EPUB 里只有第 1 到 10 章，每章一个文件（`text/Part01.html` 到 `Part10.html`），另有一个只放封面图的书名页。没有版权页、目录页、献辞，也没有书末的部分。宾州州立大学图书馆的目录记载印刷版有参考文献（第 259 到 262 页）和索引；凭对原书的了解，印刷版第 10 章之后还有致谢和附录 Prepare a Negotiation One Sheet。这些内容在这个 EPUB 里都没有，正文里也没有注释编号，所以书末注释无法恢复。需要完整的书，要换用出版社的完整电子书。2026 年 11 月已经用 HarperCollins 的完整电子书补上了致谢、附录、注释和关于作者，见文末“用更好的来源补全（2026-11-05）”。
- 文字质量：正文是出版社的文字，没有乱码、断词或连在一起的单词。只发现两处排版错误，见下面的表格。

## 原文的编码方式

| 内容 | EPUB 里的写法 |
| --- | --- |
| 章标题 | 两个 `h2`：`class="cn"` 的 “CHAPTER 1” 和 `class="ct"` 的 “THE NEW RULES”，都是大写 |
| 章副标题 | 只在目录（`nav.xhtml`）里，是章标题下面的子条目，指向章标题本身 |
| 小节标题 | `class="image"` 的加粗段落，大写，每章 5 到 14 个，第 2 到 10 章的最后一个是 KEY LESSONS |
| 小节下的标题 | `class="noindent"` 的段落，整段加粗、全部大写，共 21 个，在第 6、9、10 章（例如 “1. ANCHOR THEIR EMOTIONS”“ANALYST”） |
| 列表 | `class="bl"` 的段落，每段一项，用 “■ ” 或加粗的 “1.” 开头 |
| 引用的邮件 | `class="email"` 的段落，整段斜体 |
| 筹款电话脚本（第 4 章） | `class="di"` 的段落，说话人用小型大写（FUND-RAISER:、MR. SMITH:） |
| 首字下沉 | 每章第一个字母放在加粗的 `span.dropcap` 里 |
| 斜体 | `i.calibre6`，书名、强调和术语；第 7 章一个小节标题里的 NOT 是 `span.bold_italic` |
| 加粗 | 第 9、10 章学生案例里的强调用 `b.calibre3`，其中第 9 章的几句被拆成了一个词一个加粗 |

EPUB 里没有图片、表格、脚注或尾注，也没有指向其他位置的链接。

## 导入和整理

```bash
uv run --project framework/tools python -I books/never-split-the-difference/tools/prepare_epub.py book.epub prepared.epub
python3 scripts/site.py import-epub never-split-the-difference prepared.epub --force
uv run --project framework/tools python -I books/never-split-the-difference/tools/curate_source.py book.epub
uv run --project framework/tools python -I books/never-split-the-difference/tools/check_source.py book.epub
```

直接导入时，结构都在段落的 class 里，导入器看不出来：每章有两个一级标题，小节标题变成加粗段落，列表变成以 “■” 开头的段落，首字母单独加粗。所以先由 `tools/prepare_epub.py` 复制一份 EPUB，把结构改成导入器认得的 HTML，再导入：

| 问题 | 处理 | 原因 |
| --- | --- | --- |
| 每章两个标题 “CHAPTER 1” 和 “THE NEW RULES” | 合成一个一级标题 “# 1. The New Rules”，`book.json` 里写 `number` | 每节只能有一个一级标题，编号章节按仓库的写法 |
| 章副标题只在目录里 | 放在章标题下面，单独一段，用斜体，例如 *How to Become the Smartest Person . . . in Any Room* | 目录删掉以后，副标题就没有地方保留了。10 个副标题和宾州州立大学图书馆目录里的章节副标题一致 |
| 小节标题和小节下的标题全部大写 | 改成二级和三级标题，按芝加哥格式改成首字母大写（冠词、并列连词、介词小写），FBI、DJ、FM 保留大写；第 7 章 “How *Not* to Get Paid” 保留斜体 | 大写只是排版效果，仓库里其他书的标题都用首字母大写 |
| 第 2 章开头的日期 “September 30, 1993” 和小节标题用同一个 class | 保留为加粗的段落 | 它是故事发生的日期 |
| 首字下沉的字母单独加粗 | 改成普通字母 | 加粗只是首字下沉的排版 |
| 列表项是一段一段的 “■ …” 和 “1. …” | 连续的列表项合成无序列表或编号列表，共 20 个列表 | 每章末的 Key Lessons 和书里的步骤清单保留原来的列表结构 |
| 邮件和电话脚本只是缩进的段落 | 连续的段落合成一个引用块，共 7 个；邮件保留斜体，说话人的小型大写写成普通大写 | 原书用缩进表示引用 |
| 第 9 章几句话被拆成一个词一个加粗（“\*\*how\*\* \*\*am\*\* \*\*I\*\*…”） | 相邻的加粗合并成一段加粗 | 这是转换造成的，原意是整句加粗 |
| 4 处斜体以破折号结尾，后面紧跟单词（“*Labeling*—that”“*known knowns*—guide” 两处、“*unknown unknowns*—whose”） | 破折号移到斜体外面 | Markdown 在这种位置不能结束斜体，否则星号会原样显示 |
| 第 9 章网址中间多了一个空格（“http://info .blackswanltd.com/3-types”） | 去掉空格 | 印刷版换行留下的空格 |
| 第 8 章 “the Counterfeit “Yes. “” 的后引号打成了前引号，前面还有空格 | 改成 “the Counterfeit “Yes.”” | 排版错误 |

`prepare_epub.py` 同时把目录里的章名改成 “1. The New Rules” 的形式，导入后文件名和 id 就是 `01-1-the-new-rules.md`、`ch01`。书名页没有文字，导入器自动跳过，没有别的分节需要删除。

`tools/curate_source.py` 再做收尾：把 EPUB 的封面图存成 `assets/images/cover.jpg`，在 `book.json` 里写 `cover`、`start`（`ch01`）、`facts`，把 `source` 改记原始 EPUB（导入时记的是准备过的副本），并检查 10 章的 id、编号和一级标题。

## 完整性核对

`tools/check_source.py` 逐章比较 EPUB 和 `en/`。词是含字母或数字、以空白分隔的词；两边都不算 “CHAPTER 1” 和标题前的 “1.”；编号列表的序号两边都算。副标题来自目录，单独一列。

| 章 | EPUB 正文 | 目录里的副标题 | `en/` | 段落、标题和列表项 |
| --- | ---: | ---: | ---: | --- |
| 第 1 章 | 6,452 | 9 | 6,461 | 174/174 |
| 第 2 章 | 8,325 | 5 | 8,330 | 173/173 |
| 第 3 章 | 7,621 | 7 | 7,628 | 205/205 |
| 第 4 章 | 6,435 | 13 | 6,448 | 195/195 |
| 第 5 章 | 4,857 | 7 | 4,864 | 144/144 |
| 第 6 章 | 8,428 | 6 | 8,434 | 208/208 |
| 第 7 章 | 6,518 | 9 | 6,527 | 163/163 |
| 第 8 章 | 7,830 | 11 | 7,841 | 214/214 |
| 第 9 章 | 7,492 | 5 | 7,496 | 221/221 |
| 第 10 章 | 9,796 | 9 | 9,805 | 266/266 |
| 合计 | 73,754 | 81 | 73,834 | 1,963/1,963 |

- 每章的 `en/` 词数都等于 EPUB 正文加副标题。唯一的差别在第 9 章：网址去掉空格以后，原来的两个词合成一个，少 1 个词。
- 两边的字母和数字按顺序逐个相同，没有漏掉、多出或挪动的文字。
- EPUB 的每个段落、标题和列表项都在 `en/` 里找到且只找到一次，反过来也一样，所以没有丢失或重复的段落。
- EPUB 的 204 处斜体在 `en/` 里都还是斜体，另外多出的 10 处是各章的副标题。第 9、10 章合并后的 20 处加粗都保留。
- 原书的注释在这个 EPUB 里没有，`en/` 里也没有脚注。
- 在临时复制的书里把各章设成草稿构建了一次，在阅读器里看了第 2、4、6、7 章：标题、列表、引用块和斜体显示正常，页面没有报错。

## 保留的结构

第 1 到 10 章，共 10 节、1,860 个块：10 个章标题、76 个小节标题、21 个三级标题、1,726 个段落、20 个列表和 7 个引用块。第 2 到 10 章的末尾是 Key Lessons：几段导语加一个要点列表，保留为 “## Key Lessons” 和原来的列表；第 2 章的要点列表中间夹着一段话和一个三项的编号列表（三种语调），照 EPUB 的顺序保留。第 1 章在 EPUB 里没有 Key Lessons。

## 原文疑点

英文照原文保留，翻译时再决定中文怎样处理。

| 位置 | 原文 | 说明 |
| --- | --- | --- |
| 第 4 章，筹款电话脚本 | “Yes, President Obama is a bad person” | 句末没有句号 |
| 第 4 章，筹款电话脚本 | “If you want do something today” | 少了 to |
| 第 8 章 | “As we discussed in Chapter 5” | 三种 “Yes”（Counterfeit、Confirmation、Commitment）是在第 4 章讲的 |
| 第 8 章 | “so many pushy salesman” | 应为复数 salesmen |
| 第 9 章 | “the FM DJ Voice I talked about in Chapter 3” | 深夜电台主持人的语调是在第 2 章讲的 |
| 第 9 章 | “a complementary PDF” | 意思是免费的，应为 complimentary |

## 用更好的来源补全（2026-11-05）

### 来源

- 文件：用户提供的 `new.epub`（507 KB），SHA-256 是 `84a69519add24bc910a7489056353244fc379218a386a93a1296cdc27cf74871`，现在记在 `book.json` 的 `source` 里。第一次导入用的 `book.epub`，SHA-256 是 `7c4429e0da351cb5b2e1e394128975e0e774ebf2df8ee7865c4d2e611e810ed7`。两个文件都不放进仓库。处理时只用临时目录里的副本，读它的 Python 都用 `python -I` 运行。
- 版本：calibre 1.12.0 从 Kindle 版（ASIN B014DUR7L2）转出的 HarperCollins 电子书，出版日期 2016 年 5 月 17 日。正文和第一次导入的电子书是同一个版本，`body` 同样标着 `x9780062407818`。
- 范围：目录（`toc.ncx`）有 19 项：献辞、第 1 到 10 章、致谢、附录 Prepare a Negotiation One Sheet、注释（Notes）、索引、关于作者、Credits、版权页、About the Publisher。各章的副标题在目录里单独占一项，指向章标题。另外还有封面、目录页和一张 Bookperk 的广告图。
- 注释：注释一节按章列出 23 条文献出处（第 5 章没有注释）。正文里用上标数字（`<sup>`）标出了每一条的位置，没有链接，但位置和编号都清楚。
- 图片：只有封面、书名页上的封面图和 Bookperk 广告三张。各章、致谢、附录和关于作者里都没有图片，也没有表格。

### 比较了什么

用 `tools/compare_source.py` 逐节、逐块比较电子书和 `en/`：

```bash
uv run --project framework/tools python -I books/never-split-the-difference/tools/compare_source.py new.epub --words
```

- 块：电子书的段落、标题和列表项，和 `en/` 的标题、段落和列表项一一对齐。列表的每一项算一块，所以块数比 `site.py status` 的多。先按字母和数字对齐（difflib），再逐对比较文字：空白合并成一个空格，标题不分大小写（电子书的标题全用大写）。
- 只是排版不同的地方单独归类，归入排版差异：电子书的省略号是带空格的 “. . .”，`en/` 是 “…”；标题和人名的大小写；第一次整理时有意改过的两处（第 9 章网址里的空格、第 8 章打反的引号，电子书里也是这样）。
- 另外比较了每节的斜体和加粗、注释上标的位置、图片和表格，以及每节的词数（词的算法和上面“完整性核对”一样）。

补全前的结果：

| 节 | 电子书的块 | `en/` 的块 | 文字不同 | 只是省略号写法 | 只是大小写 | 第一次整理改过 | 注释 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 第 1 章 | 174 | 174 | 0 | 0 | 0 | 0 | 4 |
| 第 2 章 | 173 | 173 | 0 | 4 | 0 | 0 | 1 |
| 第 3 章 | 205 | 205 | 0 | 6 | 0 | 0 | 2 |
| 第 4 章 | 195 | 195 | 0 | 4 | 0 | 0 | 1 |
| 第 5 章 | 144 | 144 | 0 | 3 | 0 | 0 | 0 |
| 第 6 章 | 208 | 208 | 1 | 1 | 1 | 0 | 4 |
| 第 7 章 | 163 | 163 | 0 | 3 | 0 | 0 | 2 |
| 第 8 章 | 214 | 214 | 0 | 2 | 0 | 1 | 2 |
| 第 9 章 | 221 | 221 | 1 | 3 | 0 | 1 | 3 |
| 第 10 章 | 266 | 266 | 2 | 5 | 0 | 0 | 4 |
| 致谢 | 15 | 没有 |  |  |  |  |  |
| 附录 | 83 | 没有 |  |  |  |  |  |
| 关于作者 | 3 | 没有 |  |  |  |  |  |

- 缺少的分节：致谢、附录和关于作者。献辞、目录、索引、Credits、版权页、About the Publisher 和 Bookperk 广告照上面“导入和整理”的做法不收：它们是出版社的前后附件，印刷版的索引也不收。关于作者最后一行 “Discover great authors, exclusive offers, and more at hc.com.” 是出版社的广告，也不收。
- 缺少的图片和表格：没有。
- 缺少的注释：23 条都缺，现在都能按上标的位置放进各章。
- 文字：第 1 到 10 章没有缺少或多出的段落。除了省略号写法、大小写和第一次整理改过的两处，文字的差别只有下面“改了什么”里的四处，都是第一次导入的 EPUB 在转换时丢了连字符或空格，电子书里是对的。
- 斜体：两边一致（第 1、10 章斜体和破折号的位置、第 7 章标题里 NOT 的大小写，是第一次整理时有意改的）。加粗：第 9 章电子书把几句话拆成一个词一个加粗，`en/` 合并成一段加粗，合并后文字相同。
- 第 9 章 “I was in love… . I” 在电子书里是 “I was in love. . . . I”（句号加省略号），按省略号写法归类，没有改。电子书用段前空行（`spacebreak`）表示场景转换，第一次整理时没有保留，这次照旧。

### 改了什么

用 `tools/complete_source.py` 改 `en/` 和 `book.json`，再运行一次不会有变化：

```bash
uv run --project framework/tools python -I books/never-split-the-difference/tools/complete_source.py new.epub
```

英文里改正的四处（中文都已经是这个意思，没有改）：

| 位置 | 原来的 `en/` | 改成 | 中文 |
| --- | --- | --- | --- |
| 第 6 章第 48 块 | the real deal-and concession-making | the real deal- and concession-making | “真正谈交易、做让步的阶段” |
| 第 9 章第 100 块 | a punchin-the-face anchor | a punch-in-the-face anchor | “迎面一拳的锚点” |
| 第 10 章第 9 块 | have a shootout with him | have a shoot-out with him | “跟他在停车场枪战” |
| 第 10 章第 190 块 | think and recenter themselves | think and re-center themselves | “重新稳住自己” |

第 10 章第 41 块的 “a shootout on a deadline?” 电子书里本来就没有连字符，照电子书保留。

注释：23 条写成脚注 `[^1]` 起，每章从 1 开始，编号和电子书一样。标记放在电子书上标所在的位置，定义放在章末。注释的正文照电子书写，书名用斜体；改了两处排版错误：第 7 章注释 2 的网址中间多了一个空格（“http://well.blogs.nytimes.com /2014”，和第 9 章那个网址一样是印刷版换行留下的），第 4 章注释 1 的 “Don‘t” 把撇号打成了左单引号。

| 章 | 注释 | 标记在 `en/` 的位置 | 出处 |
| --- | --- | --- | --- |
| 第 1 章 | 1 到 4 | 第 12、93、104、117 块 | 姆努金《与魔鬼谈判》、《谈判力》、《思考，快与慢》、韦科报告 |
| 第 2 章 | 1 | 第 31 块 | 米勒 1956 年的论文 |
| 第 3 章 | 1、2 | 第 37、55 块 | 普林斯顿的神经耦合研究、利伯曼的情绪标注研究 |
| 第 4 章 | 1 | 第 44 块 | 吉姆·坎普《从“不”开始》 |
| 第 6 章 | 1 到 4 | 第 41、60、95、140 块 | 《万事皆可谈判》、《笛卡尔的错误》、《如何成为呼风唤雨的人》、埃姆斯和梅森的区间报价研究 |
| 第 7 章 | 1、2 | 第 69、72 块 | 《瞬间说服》、《纽约时报》上的医学生文章 |
| 第 8 章 | 1、2 | 第 116、142 块 | 梅拉比安的两本书、匹诺曹效应研究 |
| 第 9 章 | 1 到 3 | 第 53、127、130 块 | 律师谈判者研究、西纳瑟尔和蒂登斯的愤怒研究、埃姆斯和瓦兹拉韦克的研究 |
| 第 10 章 | 1 到 4 | 第 24（两条）、150、160 块 | 塔勒布的两本书、兰格的复印机实验、《哈佛经典谈判术》 |

新的分节，照 `prepare_epub.py` 整理各章的做法转换（标题改成首字母大写，首字下沉改成普通字母，列表项合成列表），放在第 10 章后面，顺序和电子书一样，`book.json` 里的状态都是 `review`：

| id | 文件 | 内容 | 块（`site.py status`） |
| --- | --- | --- | ---: |
| `acknowledgments` | `11-acknowledgments.md` | 致谢：标题和 14 个段落 | 15 |
| `appendix` | `12-appendix-prepare-a-negotiation.md` | 附录：一级标题 “Appendix: Prepare a Negotiation One Sheet”（电子书分成 APPENDIX 和 PREPARE A NEGOTIATION ONE SHEET 两行，合成一个标题），五个部分是二级标题，三组问题是三级标题，一个四项的列表，填空式标注和问题照电子书写成一句一段的斜体 | 80 |
| `about-the-authors` | `13-about-the-authors.md` | 关于作者：两段，电子书用加粗大写的人名改成加粗的 **Chris Voss**、**Tahl Raz** | 3 |

附录标题的大小写有两处是手工定的：“Labels/Accusation Audit” 斜杠后的词大写，“Behind-the-Table” 是复合形容词，第一个词也大写。

其他改动：

- `book.json`：`facts` 改成 “10 章与附录”“中英逐段对照”“23 条注释”，`source` 改记 `new.epub`。
- 第 1 章：`zh-cn` 第 169 块原来有译者注 `[^t6]`，说这个电子书没有附录，现在附录已经补上，删掉了这条译者注和它的标记。英文没有改。
- `glossary.md`：改写“注释”一条，补了三个新分节的标题、附录里的几个说法（一页纸、填空式的标注、搅黄交易的因素、非现金的提议）、两个书名和几个机构名。
- `review/terms/people-zh.tsv`：补了致谢里的 19 个人和附录里的 J. K. 罗琳。
- `README.md`：改写来源和内容两段。
- 中文字体子集重新生成（`site.py fonts`），新增 18 个字，共 2,550 个字符。

### 词数

词的算法和上面“完整性核对”一样，注释编号不计入。

| 部分 | 补全前 | 补全后 |
| --- | ---: | ---: |
| 第 1 到 10 章正文 | 73,834 | 73,835 |
| 致谢 | 0 | 891 |
| 附录 | 0 | 2,073 |
| 关于作者 | 0 | 146 |
| 注释（23 条） | 0 | 512 |
| 合计 | 73,834 | 77,457 |

第 1 到 10 章只多了 1 个词：第 6 章 “deal-and” 改成 “deal- and” 以后，一个词变成两个。电子书这 10 章是 73,836 个词，比 `en/` 多 1 个，是第 9 章网址去掉空格以后少的那 1 个，和第一次整理时一样。全书块数从 1,860 增加到 1,958，都已经译完（`site.py status` 显示 1958/1958，注释 23/23）。

### 补全部分的原文疑点

| 位置 | 原文 | 说明 |
| --- | --- | --- |
| 附录第 7 块 | “It will have five short sections” | 句末没有标点；中文照常写句号 |
| 附录第 58 块 | “Questions to Identify and Diffuse Deal-Killing Issues” | diffuse 用作 defuse（化解），照术语表写“化解” |
| 致谢第 10 块 | “the Joint Terrorist Task Force” | 正式名称是 Joint Terrorism Task Force；中文写“联合反恐特遣队”，没有加译者注 |
| 第 4 章注释 1 | “Pros Don‘t Want” | 撇号打成了左单引号，`en/` 已改 |
| 第 7 章注释 2 | “http://well.blogs.nytimes.com /2014/…” | 网址中间多了空格，`en/` 已改 |
