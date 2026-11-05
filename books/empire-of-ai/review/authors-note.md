# 作者说明（authors-note）审校记录

全节 5 个块、0 条注释，中英逐块对应（`site.py status` 显示 5/5）。

## 1. 译者自检

- 执行者：translation agent（Opus 5.5）。
- 范围：全节 5 块，对照原文逐句检查数字、限定条件和列举关系。
- 发现并修改：
  - 数字逐个核对：“over 300 interviews with around 260 people”作“对约 260 人所做的 300 多次采访”，“Over 150 of the interviews were with more than 90”作“150 多次采访的对象，是 90 多名”，“some 40”作“约 40 名”，“my last seven years”作“过去七年”。
  - “more than 90 current or former OpenAI executives and employees, and a handful of contractors”保留原文的并列，外包人员不算在 90 多名里，译作“90 多名……高管和员工，以及少数几名外包人员”；contractors 按术语表作“外包人员”。
  - “the AI industry, and its global impacts”初稿写成“它们在全球造成的影响”，把 its 扩大到 OpenAI 和整个行业，改作“这个行业在全球造成的影响”。
  - “contractors who had access to detailed documentation of parts of OpenAI's model development practices”初稿“OpenAI 部分模型开发做法”有歧义（像是“部分模型”），改作“接触过详细的文档，里面记录了 OpenAI 模型开发流程中的部分做法”。
  - “In cases where I do not have a copy, I paraphrase the text without quotes”初稿多了“只”，删去。
  - “corroborated by at least two people, with contemporaneous notes and documentation, or, in a few cases that I mark in the endnotes, with other media reporting”按原文“A、B 或 C”的列举译出，括号里说明靠媒体报道佐证的只有少数几处、已在尾注标注，这个限定只管最后一项。
  - “This book is not a corporate book”译作“这本书并非一部企业传记”，单独成句。
  - “Scale”指数据标注公司 Scale AI，按术语表的机构名写作“Scale AI”。
  - 刊名第一次出现时括注原名，和样章一致。
- 未决：“corporate book”也可以理解成“商业类图书”，这里按下文“讲 OpenAI 的内幕却意在看到公司之外”的语境取“企业传记”。

## 2. 双语审校

- 执行者：另一个独立上下文的 agent（Opus 5.5），没有参与翻译。
- 范围：全节 5 块，逐句对照英文，核对数字、限定条件和列举关系。
- 发现：2 条；核实后采纳 2 条，不采纳 0 条。
  - 采纳（意义）：“All dialogue is reconstructed from people's memories, from contemporaneous notes, or, when marked in the endnotes, pulled from an audio recording or transcript.”原译“所有对话都是根据当事人的回忆或当时的笔记重现的；尾注中注明的几处，则直接取自录音或文字记录。”前半句说“所有对话”都来自回忆或笔记，后半句又说有些取自录音，前后矛盾；“几处”是原文没有的数量。改为“至于对话，有的根据当事人的回忆重现，有的根据当时的笔记重现；尾注中注明的，则直接取自录音或文字记录。”三种来源并列，合起来覆盖全部对话。句首的“至于对话”接上前面讲引用文件的几句；这一段已经有三处“书中”“书里”，审校者建议的“书中的对话”编辑换成了这个说法。
  - 采纳：末句“as much as the stories within the walls of one of Silicon Valley's most secretive organizations”原译“硅谷最讳莫如深的机构之一高墙之内的故事”，定语太长，中间还夹着“之一”。审校者建议“硅谷数一数二神秘的那家机构”，可“神秘”和 secretive（刻意保密）意思有差别。编辑改为“我希望，他们的故事在书中能和这家机构高墙之内的故事一样，清晰地呈现出来；在硅谷，很少有哪家机构比它更讳莫如深。”保留“讳莫如深”和“高墙之内”，“很少有哪家机构比它更”对应 one of the most；“这家机构”承接同一段前文的“OpenAI 的内幕”“这家公司”，原文这里也没有点名。
- 审校者的总体判断：五个分节逐块对照英文读完，脚注和译者注都看过，整体质量较好，可以作为定稿的基础。结构完全对齐（献辞 7/7、题词 6/6 和 2/2、作者说明 5/5、致谢 15/15、关于作者 2/2），五个文件里没有破折号，也没有“不是……而是……”句式；人名按 people-zh.tsv，每节第一次出现括注英文；术语符合术语表；数字（300 多次采访、约 260 人、150 多次、90 多名、约 40 名、十多个小时、六个月、2021 年底）都核对无误。实质问题有四处：作者说明里对话来源一句前后矛盾，题词里“不如他开明”误译，致谢里“报警抓他”多了意思，“让报道得以成行”搭配不当；其余是表达问题，集中在致谢一节。作者说明一节的数字和“外包人员”等术语都核对无误。

## 3. 中文通读

- 执行者：编辑 agent（Opus 5.5）。
- 发现并修改（改动都回查过英文）：
  - 末句在通读时又调整了一次：起初改成“那家机构”，连读时觉得“那家”离前文太远、指代不清，改为“这家机构”；后半句“那是数一数二讳莫如深的机构”和前半句重复“机构”，改为“很少有哪家机构比它更讳莫如深”。意思和英文一致。
  - 通读确认：三家刊物第一次出现括注英文，奥特曼第一次出现括注英文，“Scale AI”和术语表一致；“它刻画了……；它考察……；它也是……”保留原文三个并列的说法；新改的对话来源一句和后一句“回忆这些话的人”衔接自然。

## 状态

- 没有未解决的意义问题。译者自检的未决项“corporate book”：编辑同意按下文语境译“企业传记”，不再列为未决。
- `site.py status` 显示 5/5。
