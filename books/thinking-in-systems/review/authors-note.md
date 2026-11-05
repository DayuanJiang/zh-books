# 作者的话（authors-note）审校记录

全节 6 个块，原文没有脚注，中英逐块对应（`site.py status` 显示 6/6）。下文的“第 N 块”按 `site.py status` 计数，从节名算起。

## 1. 译者自检

- 执行者：translation agent（Opus 5.5），译者本人。
- 范围：全节 6 块（节名、四段正文、署名行），逐块对照英文，检查漏译、增译、否定、条件、数字、谁做了什么、比较对象、术语义项和人名；19 个人名逐个对照 `review/terms/people-zh.tsv`；术语用 `tools/term_consistency.py` 检查，这一节没有报告；用框架的 markdown-it 渲染中文；全文查破折号和“不是……而是……”句式。
- 发现并修改：
  - 第 2 块 “most of them originally based at or influenced by the MIT System Dynamics group”：初稿“他们大多最初就在麻省理工学院系统动力学小组”，“就”是原文没有的强调，“在小组”后面也缺了动词。改为“他们大多最初出自麻省理工学院系统动力学小组，或者受过这个小组的影响”，originally 同时管住前后两项。
  - 第 3 块 “Strange bedfellows, but systems thinking transcends disciplines and cultures”：初稿“可系统思考本来就超越学科和文化”，“本来就”是增译，删去，改为“但系统思考超越学科和文化”。
  - 第 4 块 “And I present only the core of systems theory here, not the leading edge.”：译“我在这里介绍的仅限于系统理论的核心部分，前沿的研究不在其中”，意思完整，句式也合体例。
- 写法上的决定：
  - 人名按原文这一处的写法括注：Jay Forrester 写“杰伊·福里斯特（Jay Forrester）”，John Sterman 写“约翰·斯特曼（John Sterman）”（people-zh.tsv 的条目是 John D. Sterman，这里原文没有 D.）。同一段后面的 Jay 写“杰伊”，不再括注。
  - 第 2 块 “thirty years” 写“30 年”，“dozens of” 写“几十位”，按“全书统一的写法”的数字规则。
  - 第 2 块 “lore” 译“掌故”，指这个学术群体里流传的经验和故事；“a large intellectual community” 译“一个人数众多的学术群体”。
  - 第 3 块 “Strange bedfellows” 译“把他们放在一起，好像很不搭调”；“it overarches history as well” 译“它还能贯通古今”。
  - 第 4 块 “they have entirely human personalities” 译“他们的性情和常人完全一样”；“fractious schools of systems thought” 译“争执不休的系统思想流派”；“the school in which I was taught” 译“我就是在这个流派里学出来的”。
  - 第 5 块 “One of my purposes” 的 purpose 是作者写书的目的，照常译“目的”。
  - 第 6 块署名行 “—Donella Meadows, 1993” 写“德内拉·梅多斯（Donella Meadows），1993 年”，原文没有 H.，中文也不写。
- 检查：`site.py status` 显示 6/6；渲染后没有残留的星号；中文没有破折号，也没有体例禁用的对比句式。
- 未决：
  - 第 3 块 “and many anonymous sources of ancient wisdom, from Native Americans to the Sufis of the Middle East” 译“以及古老智慧的许多无名源头，从美洲原住民到中东的苏菲派”，和前面的人名并列在“他们当中有”之下。原文也是这样并列的，中文读起来稍显松散，留给中文通读时再看。

## 2. 双语审校

- 执行者：另一个独立上下文的 agent（Opus 5.5），没有参与翻译。
- 范围：这次审校一起看了献辞、作者的话、编者的话、题词、三个部分页、编者致谢和关于作者九节。本节 6 块逐块对照英文，核对了 19 个人名和括注、数字、术语和署名行。
- 发现：2 条（都是表达）；核实后采纳 2 条，不采纳 0 条。两条指出的问题都对照英文核实过，确实存在；其中 1 条用了和建议不同的字句，原因写在下面。
  - 照建议改的：
    - 第 3 块 “I also have drawn from thinkers in a variety of disciplines”：初稿“我还借鉴了许多学科的思想家”，“借鉴”的宾语应该是思想、经验，接人搭配不当。改为“我还从许多学科的思想家那里有所借鉴”。
  - 改法和建议不同的：
    - 第 3 块 “and many anonymous sources of ancient wisdom, from Native Americans to the Sufis of the Middle East”：初稿“古老智慧的许多无名源头”照搬英文的名词短语，排在一串人名后面，读者不容易看出它也指人；这也是译者自检留下的未决。审校者建议“许多没有留下名字、传下古老智慧的人”。编辑改为“许多留下了古老智慧、却没有留下名字的人”，两个“留下”前后对照，anonymous 和 sources of ancient wisdom 两层意思都在，后面的“从美洲原住民到中东的苏菲派”接得也更顺。
  - 不采纳：无。
- 审校者的总体判断：九节译文整体可靠，中英逐块对应完整，这几节原文都没有脚注；人名和 people-zh.tsv 一致，每节第一次出现都括注了英文；术语、机构名、书名和三个部分页标题都和术语表一致；年份和数字都和原文相符；中文没有破折号，也没有“不是……而是……”句式；没有发现漏译、增译、否定方向或谁做了什么的错误。作者的话有两句搭配问题，就是上面两条，其余没有问题。

## 3. 中文通读

- 执行者：编辑 agent（Opus 5.5）。
- 范围：改完双语审校的意见后，从节名顺着读到署名行，看连贯、重复、指代是否清楚，人名和术语是否前后一致。
- 发现并修改：没有新的改动。上面两处改动都回查了英文，意思没有变。
- 核对过、没有改的地方：
  - 第 2 块“借用的语言、观念……”和第 3 块改后的“有所借鉴”，分别对应英文两处 drawn from，用词不同但不冲突。
  - 第 3 块改后，“从美洲原住民到中东的苏菲派”紧跟在“……的人”后面，说的是这些人的范围，和英文一致。
  - 人名：19 位人物第一次出现都括注英文；第 2 块后面的“杰伊”不再括注；署名行“德内拉·梅多斯（Donella Meadows），1993 年”照原文不写 H.。
  - 全节没有破折号和“不是……而是……”句式；`site.py status` 显示 6/6。

## 状态

- 没有未解决的意义问题。译者自检留下的第 3 块未决已在双语审校中改定。
- 第 4 节阅读器校样还没有做。
