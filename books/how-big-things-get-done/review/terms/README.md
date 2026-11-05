# 术语统计

翻译之前做的统计。英文用整理过的 `en/`（和 PDF 逐节逐词核对过，见 [../source.md](../source.md)），统计时去掉脚注定义和正文里的脚注标记，只算正文。纸质版索引从 PDF 第 243 到 258 页读取：calibre 保留了索引的词条，页码变成了 ref1、ref2 这样的链接，每个链接指向它所引的那一页，脚本按 PDF 书签把目标页换算成章节。

```bash
# 1. 去掉脚注的 en/ 副本，放在工作目录里（PDF 和副本都不进仓库）
#    每个文件删掉以 [^n]: 开头的行，再删掉正文里的 [^n]
# 2. 正文语料和 spaCy 候选词（en-zh-translation-polish 的脚本，spaCy 3.8.7、en_core_web_sm 3.8.0，门槛：频次不少于 3）
corpus.py extract --root <去掉脚注的 en/ 副本> --include '*.md' --language en --out en.json
terms.py candidates --corpus en.json --english-backend spacy --spacy-model en_core_web_sm --min-frequency 3 --out candidates.json
# 3. 其余几份表（在仓库根目录运行）
uv run --with pymupdf python -I books/how-big-things-get-done/tools/term_stats.py book.pdf candidates.json
# 4. 术语表的首次出现、出现次数和 glossary-evidence.tsv（改了术语表的英文列或 GLOSSARY 之后重新运行）
uv run --with pymupdf python -I books/how-big-things-get-done/tools/term_stats.py --glossary
```

| 文件 | 内容 | 数量 |
| --- | --- | --- |
| `candidates.tsv` | spaCy 名词短语候选：频次、分布的章数、首次出现的章节、词数、常见词形 | 1797 |
| `index-terms.tsv` | 纸质版索引里人名以外的词条：概念（小写开头，202 条）和专名（机构、项目、地名、作品等，252 条），含索引链接数、链接指向的章节、正文出现次数、章数、首次出现的章节、子条目和 see also | 454 |
| `people.tsv` | 纸质版索引里的人名，正文出现次数按姓统计 | 141 |
| `people-zh.tsv` | 每个人的中文译名、依据（established 通行译名，transliterated 按新华社译名规则音译，keep 照写原名）和身份 | 300 |
| `definitions.tsv` | 原文里的定义句（I call、what I call、called “…”、known as、dubbed、coined、the term、so-called、nicknamed、the phrase、defined as 等） | 76 |
| `headings.tsv` | 各节标题（`#`）和小节标题（`##`） | 96 |
| `glossary-evidence.tsv` | 术语表核心概念每一条的首次出现、出现次数、章数、原文例句，以及裁定者 | 109 |

- **索引**：595 个主条目，1838 个页码链接。人名按“姓, 名”的格式识别，地名限定（“Bilbao, Spain”“Boston, Massachusetts”）和机构、建筑（“Atomic Energy Agency, Japan”）用词表排除，单名的人（Adele、Aristotle、Jay-Z）单独列出。链接指向书末注释的记作 notes。索引的两处笔误照原样留在 people.tsv 里，在 people-zh.tsv 里改正：Del Ray 正文作 Del Rey；“Tali, Sharot”是 Tali Sharot，原书第 2 章注释 9 也写反了。
- **人名表**：people-zh.tsv 收了索引里的 141 人，正文里没有进索引的人（第 3 章的戴维和德博拉、菲伊·雷、菲利普·格拉斯、埃莉诺·罗斯福、詹姆斯·邦德、丹·加德纳的合著者菲利普·E.泰洛克），作者丹·加德纳和献辞的对象卡丽莎·贝利斯，致谢里的全部人名（包括最后一段只写名的家人和朋友），以及只在附录 B 书目里出现的合著者。这些人是用 spaCy 的人名识别加上按大写词串的扫描找出来、逐个核对的。来源：
  - **通行译名（111 人）**：名人、有中译本的作者（卡尼曼、侯世达、吉仁泽、艾德·卡特姆、埃里克·莱斯等）用中文出版物和主流媒体的译名；和本仓库《思考，快与慢》《随机漫步的傻瓜》《坏血》重合的人用同样的译名。傅以斌和丹·加德纳用中文版的署名，萨默维尔的姓也照中文版。
  - **音译（174 人）**：按新华社译名的习惯，丹麦、法国、西班牙、意大利等地的人按原语言读音。致谢里和作者同姓的人，姓 Flyvbjerg 按丹麦语读音写“弗吕比约”；作者本人用中文名傅以斌。
  - **照写原名（15 人）**：查不到中文姓名的华裔（Edwin Chan、Ricky Wong、Zhi Liu、Newton Li、Caixia Mao、W. H. Fok，可能是华裔的 Mason Eng）、日裔和韩裔（Tensho Takemori、Jong Seok Lee）、通常照写的艺名 Jay-Z，以及只在附录 B 书目里出现的五位合著者。
- **筛选**：从这几份数据里挑出书中特有、反复出现或作者专门定义过的概念。作者自己提出的概念大多出现在定义句里（I call、what I call）：超大型项目铁律、“慢思考，快行动”、承诺谬误、策略性虚假陈述、皮克斯式规划、独特性偏差、永远的新手综合征、凝固的经验、参照类别预测、向尾部回归、黑天鹅管理、“寸程碑”、无标度的可扩展性。卡尼曼、特沃斯基和塔勒布的概念（规划谬误、外部视角、锚定与调整、所见即全部、黑天鹅、肥尾）沿用本仓库《思考，快与慢》的译法。只在小节标题里出现的说法（萨默维尔螺旋、承诺暂不承诺、“先挖个坑”）从 headings.tsv 补上。项目管理和能源方面的常用词（成本超支、承包商、风电）也收进来，保证各章译法一致。
- **中文版**：《怎样做成大事》（贾拥民译，浙江科学技术出版社 2024 年版）的目录从豆瓣读到，章名和其中的译法（大型项目铁律、计划谬误、参考类别预测法、基本比率、建筑大师）只作参考；和《思考，快与慢》不一致的地方，本书跟《思考，快与慢》走。
- **结果**：术语表 106 条核心概念（译第 1 章样章时补了 buffer、按实际价值计算的口径、核废料储存和水务项目 3 条，现为 109 条）、结语的 11 条启发式、45 行机构、产品与地名、20 行书名与作品，状态都是“初定”。
- **注意**：
  - 出现次数按英文词形的正则匹配统计，含标题，不含脚注；会把同词根的普通用法也算进去，例如 plan、experience、test、team、design。index-terms.tsv 的“正文出现次数”按索引标题的原样匹配，复数、倒装和括注都会让次数偏低。
  - 人名表里按姓统计的次数会把同姓的人算在一起，例如两位布朗、三位史密斯、迪士尼一家和乌松父子。

## 一致性检查（全书译完后）

```bash
uv run --project framework/tools python books/how-big-things-get-done/tools/term_consistency.py report.json
```

对每个术语，找出含这个英文词的段落，统计对应的中文段落里用了哪些译法；人名按姓查，同姓的人一起查，几种中文写法都算对。同一术语有不止一种译法的，回到上下文判断是否需要统一。
