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

## 用更好的来源补全（2026-11-05）

用户后来提供了一个更好的来源：美国版的 MOBI 电子书。这一节记录拿它和 `en/` 比较的方法、发现的问题和处理。比较开始时，`en/` 是上文整理好的英国 Profile 版文本，13 节都已译完，状态都是 review。

### 来源

- 文件：用户提供的 MOBI（`new.mobi`，SHA-256 `337a39e05629a310a97f5183f0746d5ec4791f09d94d9760ead6fb06a21cb9a3`），用 `mobi` 库解包成 EPUB（`new.epub`，SHA-256 `f8ed2dcd52eb8b9b0a14e308234840be31cec70b3d4afd78756d36e73fef7188`）。两份文件都当作不可信的数据，只在临时目录里的副本上操作，读它们的 Python 都用 `-I` 运行。文件本身不放进仓库。
- 版本：版权页写明这是美国 Picador 平装版。Picador 是 Henry Holt 使用的平装书品牌，版权年份写作 2009、2010；平装版 2011 年 1 月第一次印行，电子书 2013 年 12 月第一次发行；Picador 版 ISBN 978-0-312-43000-9，电子书 ISBN 9781429953382；美国国会图书馆的编目用的是 Henry Holt 精装版的 ISBN 978-0-8050-9174-8。正文和 2009 年 Metropolitan 精装版是同一套，下文列出的几处改正说明平装版改过个别字句。
- 页码标记：电子书的正文里留着纸质版的页码标记（`<span id="page_37">` 这样的空标签）。英国 EPUB 里在段落中间断开的地方，全都正好落在美国版的一个页码标记上，可见英国 EPUB 也是从这套纸质版面转换来的，在换页处断了段。
- 结构：28 个 XHTML 文件，顺序是封面、书名页、版权声明、目录、献辞、引言、第 1 到 9 章、附录、Notes on Sources、致谢、Additional Praise（书评摘录）、Also by（作者的其他书）、作者简介、版权页、星号注释、书末的新书广告。英国 EPUB 没有附录、书评摘录和新书广告。
- 图片：12 张。封面，书名页，附录的四张清单，作者简介页上的作者照片（署名 © Fred Field），新书广告页上四本书的封面和一个 20×21 像素的小标志。

### 比较的方法

```bash
uv run --project framework/tools python -I books/checklist-manifesto/tools/compare_us_edition.py new.epub
```

`tools/compare_us_edition.py` 逐节、逐块比较美国版和 `en/`：

- 每节两边都切成词和符号的序列：连续的字母和数字算一个词，其余每个非空白字符算一个符号。再用 `difflib` 对齐，列出每一处不同，前后各带几个词。比较前去掉空白、表示斜体的星号、脚注标记和 Markdown 的反斜杠转义，列出来的只有文字和标点的差别。每个段落的结尾记作 ¶，每条分隔线记作 §，所以一边断了段、另一边连成一段，或者一边少了一条分隔线，也会作为差异列出来。
- 斜体：两边斜体里的字母按顺序比较。
- 注释：美国版 Notes on Sources 的 82 条注释，按章、按顺序和 `en/` 的脚注逐条比较；星号注释单独比较。
- `curate_source.py` 的 `FIXES`（22 处补空格和另外 9 处修正）：在美国版的文本里逐条查找修正后的写法。
- 附录的四张图逐字节和美国 EPUB 里的原图比较。
- 美国 EPUB 的解包程序会在很多标签后面加一个换行和一个空格。脚本遇到它夹在两个字母或数字之间时当作一个空格，挨着标点时去掉，例如 `patient<span id="page_3"></span>` 后面跟着换行、空格和句点，还原成 “patient.”。

比较之后，用 `tools/apply_us_edition.py` 修改 `en/`、写出附录、复制图片，并在 `book.json` 的第 9 章后面加上附录：

```bash
uv run --project framework/tools python -I books/checklist-manifesto/tools/apply_us_edition.py new.epub
```

- 它接在上文 `curate_source.py` 的后面运行。每处修改都是精确替换，并核对出现的次数；已经改过的跳过，所以可以重复运行。`zh-cn/` 由人工修改。
- 重新运行 `curate_source.py` 会从英国 EPUB 重建 `en/`，还会删掉 `en/images/`，之后要再运行一次 `apply_us_edition.py`。
- `check_source.py` 拿英国 EPUB 逐段核对，现在会报告 15 个问题，都来自按美国版做的改动：第 1、2、4、5、7、8 章和致谢的段落对不上（合并、拆分的段落和第 1 章对调的两个词），第 1、2 章和第 5 到 8 章的词数差额和 `FIXES` 对不上，第 3 章多了一条分隔线，脚注少了 1 个词（Handwashing）。附录不在英国 EPUB 里，`check_source.py` 跳过它。现在以 `compare_us_edition.py` 的结果为准。

### 比较的结果

- **缺少的章节**：只有附录 Example Checklists（清单示例）。它在第 9 章之后、Notes on Sources 之前：一页列出四张清单的名称，后面四页各是一张图。其余 13 节两边都有，标题相同。
- **缺少的图片和表格**：附录的四张清单图。两个版本的正文里都没有表格，也没有别的图。
- **注释**：82 条注释两边逐条对应，内容一致，没有缺的，也没有新的注释可以安放。注释里有 3 处差异：Handwashing 按美国版改了，Rose-grant 保留英国版，另一处是 Markdown 的转义写法，见下面两张表和表后的说明。
- **星号注释**：美国版的文字是 “Identifying details were changed at John’s request.”，和上文按美国版扫描本补回的完全相同；星号的位置也一样，在 “his heart suddenly stopped.” 后面。上文“原文疑点”表里说这一条“只核对了这一句”，现在有了完整的美国版作依据。英国版纸质书仍然没有核对。
- **22 处补空格**：全部和美国版的写法一致。`FIXES` 里另外 9 处修正（被连字符拆开的 O’Sullivan、Hagerman、Donaldson，被空格拆开的 overwhelmed，line-by-line，标点后面补的空格）也和美国版一致。
- **其他差异**：27 处按美国版改了，见下面第一张表；另外 9 项差别保留英国版，只作记录，见第二张表。

#### 按美国版改正的地方

块号是改动以后的块号，从标题算起，和各节审校记录的算法相同。

| 节 | 块 | 英国 EPUB | 美国版 | 原因 | 中文 |
| --- | --- | --- | --- | --- | --- |
| introduction | 第 52 块 | years of sixty, seventy-, eighty-hour weeks | sixty-, seventy-, eighty-hour | 转换丢了连字符 | 不变 |
| ch01 | 第 38 块 | shifted to super-specialists | superspecialists | 纸质版换行处的连字符留了下来，同一段后面就写 superspecialists | 不变 |
| ch02 | 第 2 块 | A Seattle newspaper man | newspaperman | 换行处的词被空格拆开 | 不变 |
| ch03 | 第 53 块 | the fire proofing material | fireproofing | 同上 | 不变 |
| ch03 | 第 79 块 | as Joe Salvia explained tome | explained to me | 两个词连在一起，上文用词频表查不出来 | 不变 |
| ch05 | 第 44 块 | *Cleared for Take off* | *Cleared for Takeoff* | 换行处的词被空格拆开，术语表写的就是 Cleared for Takeoff | 不变 |
| ch05 | 第 69 块 | button holed | buttonholed | 同上 | 不变 |
| ch05 | 注释 6 | “Effect of Hand-washing on Child Health” | Handwashing | 换行处的连字符；论文的原题写作 handwashing | 脚注里的出处照英文改 |
| ch06 | 第 35 块 | in mid-flight | midflight | 换行处的连字符，本章另外两处都写 midflight | 不变 |
| ch07 | 第 3 块 | on my hall way | hallway | 换行处的词被空格拆开 | 不变 |
| ch08 | 第 13 块 | in under recognized, undervalued companies | underrecognized | 同上 | 不变 |
| ch04 | 第 31 块 | a roasted tomato soap | soup | 英国版的笔误 | 不变，原译已写“烤番茄汤” |
| ch02 | 第 15 块 | for themselves. ¶ With all the things nurses | 同一段 | 英国 EPUB 在换页处断段（美国版第 37 页起） | 两块合成一块 |
| ch02 | 第 24 块 | primitive insights. ¶ Pronovost is routinely | 同一段 | 同上（第 40 页） | 两块合成一块 |
| ch02 | 第 43 块 | no saves. ¶ So he and a couple | 同一段 | 同上（第 46 页） | 两块合成一块 |
| ch05 | 第 57 块 | this kind of teamwork was ¶ mostly a matter of luck | 同一段 | 同上（第 104 页），原来断在句子中间 | 两块合成一块 |
| ch05 | 第 64 块 | good news. ¶ The problem was limited. | 同一段 | 同上（第 106 页） | 两块合成一块 |
| ch07 | 第 27 块 | surgical personnel. ¶ We supplied the hospitals | 同一段 | 同上（第 146 页） | 两块合成一块 |
| ch08 | 第 25 块 | He had missed the ¶ fact that | 同一段 | 同上（第 166 页），原来断在句子中间 | 两块合成一块，“他忽略了一个事实。”改成“他忽略了一个事实：”，接上后面的话 |
| ch08 | 第 98 块 | a “weak” pilot. ¶ Instead they chose | 同一段 | 同上（第 186 页） | 两块合成一块 |
| acknowledgments | 第 3 块 | more coherence. ¶ Laura Schoenherr | 同一段 | 同上（第 206 页） | 两块合成一块 |
| ch02 | 第 29、30 块 | fill out some daily checklists? Tom Piskorowski | 分成两段 | 英国 EPUB 把两段连在了一起 | 一块分成两块，断在“每天填几份清单？”后面 |
| ch04 | 第 45、46 块 | said the grill chef. As in the construction world | 分成两段 | 同上；前一段是报单的对话，后一段讲碰头会 | 一块分成两块，断在“烧烤厨师说。”后面 |
| ch07 | 第 63、64 块 | percentage drop. This thing was real. | 分成两段 | 同上；美国版里 This thing was real. 单独一段 | 一块分成两块，“这个效果是实实在在的。”单独一块 |
| ch03 | 第 40 块前 | 没有分隔线 | 有分隔线，To show me 是新一节的开头 | 英国 EPUB 在纸质版页首（第 60 页）丢了分隔符号和粗体开头 | 分隔线只写在英文里，中文不变 |
| ch01 | 第 4 块 | sew … into her femoral artery to take the blood out of her, then another into her femoral vein to send the blood back | femoral vein … femoral artery | 英国版把两根管子的用途写反了，第三轮审校已经对照病例报告查实，美国版已经改正 | 改成“缝接在她的股静脉上，把血引出来；再把另一根缝接在股动脉上，把血送回去”，删掉说明这处错误的译者注 [^t1] |
| ch08 | 第 65 块 | a Pan American flight taking off in the opposite direction on the same runway | a Pan American flight still taxiing on the same runway | 英国版的史实错误，审校时已按事故调查查实，美国版已经改正 | 改成“事实上，当时还有一架泛美航空的客机在同一条跑道上滑行”，删掉说明这处错误的译者注 [^t2] |

#### 保留英国版、只作记录的差别

| 位置 | 英国 EPUB（`en/` 照此保留） | 美国版 | 判断 |
| --- | --- | --- | --- |
| ch01 最后一段（第 45 块） | Medicine, with its dazzling successes but also frequent failures, therefore poses a significant challenge: … one that has nothing to do with medicine at all. | 没有这一段，第 1 章到 “Mistakes are still made.” 结束 | 版本差别。这一段把第 1 章引向第 2 章，是英国版完整的正文，保留 |
| ch03 第 70 块 | called Project Center | called ProjectCenter | 拼写的版本差别，两种写法都说得通，保留 |
| ch07 第 31 块 | two hundred miles … from the capital, Dar es Salaam | from Dar es Salaam | 版本差别。坦桑尼亚的法定首都是多多马，达累斯萨拉姆当时是政府的实际所在地，当时把它称作首都很常见；中文照原来的“首都达累斯萨拉姆” |
| ch08 第 56、71 块 | Canadian geese（两处） | Canada geese | 鸟的正式名称是 Canada goose，美国版改了叫法；意思相同，中文都是“加拿大黑雁”，保留 |
| about-the-author | 作者简介到 Newton, Massachusetts. 结束 | 后面多一行网址 www.gawande.com，上方有作者照片 | 电子书版面的差别，`en/` 照英国版 |
| Notes on Sources 开头 | 没有 | Please note that some of the links referenced in this work are no longer active. | 电子书出版时加的说明，属于已经分到各章做脚注的 Notes on Sources 一节，`en/` 照英国版 |
| ch01 第 13 块 | antibiotic | anti-biotic | 美国电子书自己留下的换行连字符，保留英国版 |
| ch04 注释 2 | Rosegrant | Rose-grant | 同上；作者名是 Susan Rosegrant，上文已经合并，保留 |
| ch04 第 26、35 块 | ...（三个句点） | …（省略号字符） | 纯格式，不改 |

注释里的另一处差异是 ch06 注释 13 网址里的 `\_`，这是 Markdown 的转义写法，显示出来和美国版相同。引言的星号是注释标记，`en/` 里换成了 `[^1]`。

### 新加的附录

- `en/18-appendix-example-checklists.md`：一级标题 “Appendix: Example Checklists”，四个清单名称各写成一个加粗的段落，放在对应的图片上方，图片放在 `en/images/`（`appendix-1-door-fwd-cargo.jpeg` 到 `appendix-4-checklist-for-checklists.jpeg`），和美国 EPUB 的原图逐字节相同。整理的细节见 [appendix.md](appendix.md)。
- `zh-cn/18-appendix-example-checklists.md`：标题“附录：清单示例”，四个中文小标题，每个后面挂一条译者注，译出图里的全部文字，并写明版权页注明的提供者：第 1 张由波音公司提供，第 2 张由科罗拉多飞行中心（Colorado Flight Center）提供，第 3 张出自世卫组织 2009 年的出版物，第 4 张版权页没有注明。
- `book.json`：附录的 id 是 `appendix`，状态 review，排在第 9 章和致谢之间，和美国版的顺序相同；书架卡片的 facts 改成“引言、9 章、附录与致谢”。
- 没有加的：美国版的目录、书名页、版权声明和版权页、书评摘录、Also by、作者照片、新书广告和小标志，都属于上文已经删掉的前后附页；Notes on Sources 照上文的做法分到各章做脚注。书架封面仍用英国版的封面。

### 改动前后的数字

词数的算法和上文相同：连续的字母和数字算一个词，不算标题，不算脚注。块数是 `site.py status` 里的可译块数。

| 节 | 改前词数 | 改后词数 | 差额 | 改前块数 | 改后块数 | 差额的来源 |
| --- | --- | --- | --- | --- | --- | --- |
| dedication | 5 | 5 | 0 | 2 | 2 |  |
| introduction | 3682 | 3682 | 0 | 55 | 55 | 补回的连字符不改变词数 |
| ch01 | 4973 | 4972 | −1 | 45 | 45 | superspecialists |
| ch02 | 4423 | 4422 | −1 | 49 | 47 | newspaperman；合并三段、拆开一段 |
| ch03 | 7159 | 7159 | 0 | 80 | 80 | fireproofing 减 1，to me 加 1；加了一条分隔线 |
| ch04 | 3942 | 3942 | 0 | 48 | 49 | 拆开一段 |
| ch05 | 7929 | 7927 | −2 | 98 | 96 | Takeoff、buttonholed；合并两段 |
| ch06 | 6221 | 6220 | −1 | 79 | 79 | midflight |
| ch07 | 6180 | 6179 | −1 | 70 | 70 | hallway；合并一段、拆开一段 |
| ch08 | 8387 | 8382 | −5 | 102 | 100 | underrecognized 减 1，泛美客机一句减 4；合并两段 |
| ch09 | 2060 | 2060 | 0 | 25 | 25 |  |
| appendix | 0 | 15 | +15 | 0 | 5 | 新加的一节，15 个词是四个清单名称 |
| acknowledgments | 1069 | 1069 | 0 | 11 | 10 | 合并一段 |
| about-the-author | 72 | 72 | 0 | 2 | 2 |  |
| 合计 | 56102 | 56106 | +4 | 666 | 665 |  |

- 美国版用同样算法数出的正文词数是 56034，比改后的 `en/`（不算附录，56091）少 57 个词：第 1 章最后一段只在英国版里，58 个词；the capital 2 个词；Project Center 比 ProjectCenter 多 1 个词；美国版的 anti-biotic 多 1 个词，作者简介的网址多 3 个词。58 + 2 + 1 − 1 − 3 = 57。
- 脚注 83 条，改前 2104 个词，改后 2103 个词（Handwashing 少了 1 个词）。美国版的 82 条注释共 2096 个词（不算开头的说明）；`en/` 的脚注去掉星号注释的 8 个词，是 2095 个词，差的 1 个词来自美国版的 Rose-grant。
- `python3 scripts/site.py status checklist-manifesto`：14 节都是 review，665/665 个块、83/83 条注释都已翻译。`python3 scripts/site.py check checklist-manifesto` 通过。附录的译者注里有 4 个字体子集里没有的字符（©、爽、磁、逻），已用 `site.py fonts checklist-manifesto` 重新生成字体子集。
- 阅读器检查：用 `site.py serve --drafts` 打开附录和第 8 章，中英模式和纯中文模式都看过：四张图都加载出来，译者注能点开，合并以后的段落显示正常。

### 中文的改动

- 跟着英文合并的 9 处，中文的两块直接接成一块；第 8 章第 25 块的断处原来在“他忽略了一个事实。”，合并时改成冒号，接上后面那句。跟着英文拆开的 3 处，中文在对应的句号后面分开。
- 意思变了的 2 处（第 1 章第 4 块、第 8 章第 65 块）按美国版重译了那半句，删掉了两条译者注。第 1 章现在没有译者注，第 8 章剩下关于 the right stuff 的 [^t1]。
- 第 5 章注释 6 的出处照英文改成 Handwashing。
- 其余的英文改动（补连字符、合并被拆开的词、soap 改 soup、加分隔线）意思不变，中文保持原样。
- 各节审校记录的末尾加了“补全后的改动”一节；附录的审校记录是 [appendix.md](appendix.md)；术语表的“各节标题”“译者注”“原文疑点和译者注”三处和机构表的两行跟着更新。

