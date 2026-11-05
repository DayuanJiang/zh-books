# 关于作者（about-the-author）审校记录

全节 2 个块（1 个标题、1 个段落），没有注释，也没有译者注，中英逐块对应（`site.py status` 显示 2/2）。

## 1. 译者自检

- 执行者：translation agent（Opus 5.5）。
- 范围：标题和作者简介一段，对照原文逐句检查漏译、增译、人名、书名、机构名、职务和地名；`site.py status` 显示 2/2；`tools/term_consistency.py` 只标出一处，核实后是误报（见下）；正文没有破折号，也没有体例禁用的对比句式。
- 发现并修改：
  - “A MacArthur Fellow, a general and endocrine surgeon …, a staff writer for *The New Yorker*, and an associate professor …, he also leads …”：初稿把四个身份和“还领导着”用逗号串成一长句，身份和后面的动作读起来分不开。改为四个身份用顿号并列，以“也是……副教授”收住，“他还领导着世界卫生组织（WHO）的‘安全手术拯救生命’项目”另起一句。
- 照体例处理的地方：
  - 人名：Atul Gawande 按 `people-zh.tsv` 写“阿图·葛文德（Atul Gawande）”。
  - 书名：*Better* 和 *Complications* 用作者在中国大陆通行的中译本书名，写“《医生的精进》（*Better*）”和“《医生的修炼》（*Complications*）”，这两个书名是浙江人民出版社中译本的正书名（副题没有译出），已经在网上的图书条目里核对过；原题照体例用斜体括注。
  - 术语和机构：MacArthur Fellow 按术语表写“麦克阿瑟学者”；general and endocrine surgeon 写“普通外科和内分泌外科医生”；the Brigham and Women’s Hospital 写“布莱根妇女医院”；Harvard Medical School、Harvard School of Public Health 写“哈佛医学院”“哈佛公共卫生学院”；World Health Organization 在本节第一次出现，写“世界卫生组织（WHO）”；Safe Surgery Saves Lives program 按术语表写“‘安全手术拯救生命’项目”；《纽约客》不括注。
  - 地名：Newton, Massachusetts 写“马萨诸塞州牛顿市”；three children 写“三个孩子”。
  - `term_consistency.py` 在第 2 块标出 complication 没有译成“并发症”：这里的 *Complications* 是书名，按中译本写“《医生的修炼》”，属于误报，不改。
- 未决：
  - staff writer 译作“专职撰稿人”。中文媒体介绍作者时常写“《纽约客》特约撰稿人”，但 staff writer 指杂志在职的撰稿人，和“特约”（contributing）的意思不同，所以没有用。致谢里 “keeping me on staff” 也按这个意思写成“一直保留着我在杂志的职位”。
  - 两本书名没有加译者注：中译本书名和英文原题的字面意思（“更好”“并发症”）不同，括注原题已经能让读者对上原书。如果主会话希望说明，可以加一条译者注。

## 2. 双语审校

- 执行者：另一个独立上下文的 agent（Opus 5.5），没有参与翻译。
- 范围：标题和作者简介一段，对照原文逐句核对人名、书名、机构名、职务、地名和人数，并对照 `review/terms/people-zh.tsv` 和术语表。
- 发现：0 条；核实后采纳 0 条，不采纳 0 条。审校者确认阿图·葛文德的译名和人名表一致，第一次出现时括注了英文；*Better* 和 *Complications* 用的是中国大陆通行的中译本书名《医生的精进》《医生的修炼》；“麦克阿瑟学者”“世界卫生组织（WHO）”“‘安全手术拯救生命’项目”都按术语表处理；`site.py status` 显示 2/2，没有破折号，也没有体例禁用的句式。
- 审校者的总体判断：献辞和关于作者两节没有问题，可以定稿。

## 3. 中文通读

- 执行者：编辑 agent（Opus 5.5）。
- 发现并修改：顺着中文读完全段，四个身份用顿号并列、“他还领导着……”另起一句的结构读起来清楚，没有修改。核对了和致谢一节的一致性：“布莱根妇女医院”“哈佛公共卫生学院”“《纽约客》”的写法两节相同；“专职撰稿人”和致谢里 “keeping me on staff” 译作“保留着我在杂志的职位”意思相合。`tools/term_consistency.py` 标出的 complication 是书名《医生的修炼》，属于误报。修改后运行 `site.py status`，仍是 2/2。

## 状态

没有未解决的意义问题。

## 第三轮：GPT-6 Astra 独立审校

- 审校者：GPT-6 Astra，通过 Codex 运行，只读，和译者属于不同的模型家族。
- 发现：1 条，是体例问题。逐条找到中英文对应的句子，读过上下文后核实：成立并修改 1 条，不成立 0 条。审校者的总体判断是译文整体准确、通顺，只有这一处体例问题；没有提出意义、人名、书名或机构名方面的问题。
- 成立并修改：
  - 第 2 块 “a general and endocrine surgeon at the Brigham and Women’s Hospital in Boston”：原译“波士顿布莱根妇女医院的普通外科和内分泌外科医生”把地名和机构名直接连写。“全书统一的写法（译完后定）”里“地名和机构名连写”一条规定，机构名前面有地名时，中间加“的”或者用“位于”；“波士顿”也不是这家医院正式名称的一部分。采纳审校者的改法，改为“位于波士顿的布莱根妇女医院的普通外科和内分泌外科医生”，和术语表举的例子“位于波士顿的美国医疗保健改进研究所”写法相同。
- 不成立，保留原译：没有。
- 按全书统一的写法修改：除上面这一处（它同时也是“地名和机构名连写”一条要求的修改），没有别的需要改的地方，另改 0 处。逐条对照过、已经符合的：人名每节第一次出现括注英文（阿图·葛文德（Atul Gawande））；书名括注斜体原题（《医生的精进》（*Better*）、《医生的修炼》（*Complications*）），《纽约客》属于常见报刊，不括注；World Health Organization 本节第一次出现写“世界卫生组织（WHO）”；“三个孩子”按数字规则用汉字；MacArthur Fellow 写“麦克阿瑟学者”，Safe Surgery Saves Lives program 写“‘安全手术拯救生命’项目”，都和术语表一致；“马萨诸塞州牛顿市”只有地名，和机构名连写一条无关；本节没有指称词语本身的斜体。
  - 第 1 节“未决”里的两项（staff writer 译作“专职撰稿人”，以及两本书名要不要加译者注），术语表“全书统一的写法”和“全书统一的写法（译完后定）”都没有作出规定，仍然留给主会话决定，原处没有改动。
- 对英文原文的疑问：审校者没有提出。核实时也没有发现疑点。
- 核实与修改：agent（Opus 5.5）。中文文件只改了第 2 块一处，块的对应关系没有变，本节没有注释。改完后运行 `python3 scripts/site.py status checklist-manifesto`，关于作者一节显示 2/2 块，全书 666/666 块已翻译；`tools/term_consistency.py` 在本节仍只标出书名《医生的修炼》里的 complication，属于前几轮已经说明的误报；中文正文没有破折号，也没有体例禁用的对比句式。
