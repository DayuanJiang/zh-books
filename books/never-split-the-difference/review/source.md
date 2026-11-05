# 原文核对

## 来源

- 文件：用户提供的 EPUB（`book.epub`，324 KB），SHA-256 记在 `book.json` 的 `source` 里。EPUB 本身不放进仓库。
- 版本：calibre 5.15.0 在 2021 年 4 月 12 日重新打包的 HarperCollins 电子书。元数据里的 ISBN 9780062407801 是 HarperBusiness 2016 年的精装本；正文文件的 `body` 标记为 `x9780062407818`，这是 HarperCollins 电子书的 ISBN（2016 年 5 月 17 日发行）。书名以封面和 HarperCollins 的书目为准：《Never Split the Difference: Negotiating As If Your Life Depended On It》，Chris Voss with Tahl Raz。
- 范围：EPUB 里只有第 1 到 10 章，每章一个文件（`text/Part01.html` 到 `Part10.html`），另有一个只放封面图的书名页。没有版权页、目录页、献辞，也没有书末的部分。宾州州立大学图书馆的目录记载印刷版有参考文献（第 259 到 262 页）和索引；凭对原书的了解，印刷版第 10 章之后还有致谢和附录 Prepare a Negotiation One Sheet。这些内容在这个 EPUB 里都没有，正文里也没有注释编号，所以书末注释无法恢复。需要完整的书，要换用出版社的完整电子书。
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
