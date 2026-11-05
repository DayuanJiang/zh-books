# 关于作者（about-the-author）审校记录

全节 3 个块，原文没有脚注，中英逐块对应（`site.py status` 显示 3/3）。下文的“第 N 块”按 `site.py status` 计数，从节名算起。

## 1. 译者自检

- 执行者：translation agent（Opus 5.5），译者本人。
- 范围：全节 3 块（节名、两段正文），逐块对照英文，检查漏译、增译、数字和日期、谁做了什么、术语义项、人名、书名、专栏名和机构名；人名对照 `review/terms/people-zh.tsv`，书名和机构名对照 `glossary.md`；用框架的 markdown-it 渲染中文，确认书名的斜体生效；全文查破折号和体例禁用的对比句式。
- 发现并修改：
  - 第 2 块 “for fifteen years she wrote a weekly column, ‘The Global Citizen,’”：初拟“每周为‘全球公民’专栏撰稿”，“撰稿”像是给别人主持的专栏投稿。这个专栏是她本人的，改为“她还连续 15 年撰写每周一篇的‘全球公民’专栏（‘The Global Citizen’）”，专栏名的写法照术语表。
- 写法上的决定：
  - 第 2 块 “Donella Meadows (1941–2001)”：生卒年和英文原名合进同一个括号，写“德内拉·梅多斯（Donella Meadows，1941 年到 2001 年）”；短横线照体例写“到”。
  - 数字：“twenty-eight languages”写“28 种语言”，“nine more books”写“九本”，“fifteen years”写“15 年”，按“全书统一的写法”的数字规则；年份 1970、1972、1991、1994、1996、2001 都和原文一致。
  - 书名：《增长的极限》（*The Limits to Growth*）第一次出现时括注，后面单独出现的 *Limits* 照术语表写《增长的极限》。
  - World3：原文第一次出现带引号，中文写“全球计算机模型‘World3’”，后面的 the World3 modeling project 写“World3 建模项目”；“模型”二字已经在句子里，没有再写成“World3 模型”。
  - “explores the dynamics of human population and economic growth on a finite planet”：dynamics 照术语表写“动态”，译“探究在一个有限的星球上，人口和经济增长的动态”。
  - “carrying capacity” 照术语表写“承载能力”；“sparked debate around the world” 译“在世界各地引发了一场……争论”。
  - 第 3 块 Pew Scholar in Conservation and the Environment、MacArthur Fellowship、Sustainability Institute、Environmental Studies Program of Dartmouth College 照术语表写“皮尤环境保护学者”“麦克阿瑟奖”“可持续发展研究所”“达特茅斯学院的环境研究项目”；organizational learning 译“组织学习”。
  - 第 2 块的 Dennis Meadows 在本节第一次出现，括注英文；后面的 Meadows 都指作者本人，写“梅多斯”。
- 检查：`site.py status` 显示 3/3；渲染后没有残留的星号；中文没有破折号，也没有体例禁用的对比句式。
- 未决：
  - 第 2 块的丹尼斯·梅多斯是作者的丈夫，原文没有说明。中文读者看到两个“梅多斯”可能会疑惑，但英文读者面对的是同样的情况，没有加译者注。

## 原文疑点

| 位置 | 原文 | 处理 |
| --- | --- | --- |
| 第 2 块 | the Massachusetts Institute of Technology team lead by Dennis Meadows | lead 应为 led（过去分词）。按“丹尼斯·梅多斯领导的”译，不加注 |

## 2. 双语审校

- 执行者：另一个独立上下文的 agent（Opus 5.5），没有参与翻译。
- 范围：这次审校一起看了献辞、作者的话、编者的话、题词、三个部分页、编者致谢和关于作者九节。本节 3 块逐块对照英文，核对了年份和数字（1941 年到 2001 年、1970 年、1972 年、28 种语言、九本书、15 年、1991 年、1994 年、1996 年）、人名、书名、专栏名、机构名，以及上面原文疑点的处理。
- 发现：1 条（表达）；核实后采纳 1 条，不采纳 0 条。
  - 照建议改的：
    - 第 3 块 “to apply systems thinking and organizational learning to economic, environmental, and social challenges”：初稿“把系统思考和组织学习运用到经济、环境和社会挑战上”照搬 apply ... to，搭配生硬。改为“用系统思考和组织学习来应对经济、环境和社会方面的挑战”。
  - 不采纳：无。
- 审校者的总体判断：九节译文整体可靠，中英逐块对应完整，这几节原文都没有脚注；人名和 people-zh.tsv 一致，每节第一次出现都括注了英文；术语、机构名、书名和三个部分页标题都和术语表一致；年份和数字都和原文相符；中文没有破折号，也没有体例禁用的对比句式；没有发现漏译、增译、否定方向或谁做了什么的错误。关于作者一节有一句搭配问题，就是上面一条；原文疑点（lead 应为 led）的处理恰当。

## 3. 中文通读

- 执行者：编辑 agent（Opus 5.5）。
- 范围：改完双语审校的意见后，从节名顺着读到最后一段，看连贯、指代是否清楚，和编者的话里同一批事实的写法是否一致。
- 发现并修改（回查了英文，意思没有变）：
  - 第 2 块 “a global computer model that explores the dynamics of human population and economic growth on a finite planet”：初稿“这个团队开发了全球计算机模型‘World3’，探究在……”，“探究”的主语看上去是团队；英文里做探究的是模型。补“用来”二字，改为“……‘World3’，用来探究在一个有限的星球上，人口和经济增长的动态”。
- 核对过、没有改的地方：
  - lead author 写“第一作者”，皮尤环境保护学者、可持续发展研究所、达特茅斯学院的写法，都和编者的话一致。
  - 丹尼斯·梅多斯在本节只出现一次，括注了英文；第 2 块和第 3 块其余的“梅多斯”都指作者本人，指代清楚。
  - 全节没有破折号和体例禁用的对比句式；`site.py status` 显示 3/3。

## 状态

- 没有未解决的意义问题。译者自检留下的“两个梅多斯”一条，保留现在的写法、不加译者注：作者的话和编者致谢也提到丹尼斯·梅多斯，英文读者面对的情况相同。
- 上面“原文疑点”表里的一条照旧；这次没有发现新的原文疑点。
- 第 4 节阅读器校样还没有做。

## 第三轮：GPT-6 Astra 独立审校

- 审校者：GPT-6 Astra，通过 Codex 运行，只读，和译者属于不同的模型家族。
- 发现：0 条。审校者逐块对照了全节 3 块，认为人名、术语和体例都符合约定，没有提出需要修改的地方。成立并修改 0 条，不成立 0 条。
- 成立并修改：无。
- 不成立，保留原译：无。
- 按全书统一的写法修改：0 处。对照术语表“全书统一的写法”和“全书统一的写法（译完后定）”两节逐条核对，本节已经符合，没有要改的地方。核对过的写法有：
  - 数字：“twenty-eight languages”写“28 种语言”，“nine more books”写“九本”，“fifteen years”写“15 年”，十以内写汉字、11 以上写阿拉伯数字；生卒年的范围写“1941 年到 2001 年”。
  - lead author 写“第一作者”，和“其他说法”一条一致。
  - systems thinking 写“系统思考”，和“系统”的复合词一条一致。
  - 书名和专栏名：《增长的极限》（*The Limits to Growth*）在本节第一次出现时括注，后面的 *Limits* 写《增长的极限》；专栏写“全球公民”专栏（“The Global Citizen”），原题用引号、不用斜体。
  - 人名：德内拉·梅多斯（Donella Meadows）和丹尼斯·梅多斯（Dennis Meadows）在本节第一次出现时括注英文，和 people-zh.tsv 一致。
  - 机构名：麻省理工学院、皮尤环境保护学者、麦克阿瑟奖、可持续发展研究所、达特茅斯学院的环境研究项目，都和术语表的“机构、产品与地名”一致。
  - 本节没有留给主会话裁定的事项。译者自检的“未决”一条（两个梅多斯，不加译者注）在前面的“状态”里已经定下，新定的写法没有涉及，照旧。
- 对英文原文的疑问：审校者也指出第 2 块 “the Massachusetts Institute of Technology team lead by Dennis Meadows” 里的 lead 应为过去分词 led，和上面“原文疑点”表里的一条相同；译文“丹尼斯·梅多斯领导的”已按正确的意思译，不加注。这一条还没有写进全书的 `review/source.md` 原文疑点表，可以考虑补上。
- 核实与修改：agent（Opus 5.5）。逐条读了审校结果，对照英文和中文全节，又对照术语表核对了一遍；中文全节没有破折号，也没有体例禁用的对比句式；本轮没有改动 zh-cn/ 的译文。运行 `python3 scripts/site.py status thinking-in-systems`，本节显示 3/3 块已译，原文没有脚注；全书 1115/1115 块已译。
