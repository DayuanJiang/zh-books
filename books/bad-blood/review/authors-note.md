# 作者说明（authors-note）审校记录

全节 4 个块，原文没有注释，另加 1 条译者注，中英逐块对应（`site.py status` 显示 4/4）。

## 1. 译者自检

- 执行者：translation agent（Opus 5.5），译者本人。
- 范围：标题和 3 段正文，加 1 条译者注，从头译到尾，没有跳过。译完后用脚本把中英文逐块并排列出，逐句检查漏译、增译、否定、条件、数字、动作主体和术语；又顺着中文读了一遍，读时的改动都回查了英文。
- 发现并修改：
  - “However, everything else I describe about them and their experiences is factual and true.”：初稿“都是真实的”语气比 factual and true 弱，改为“都是确凿的事实”；前面加“除了名字”，点明 everything else 指化名以外的全部内容。
  - “offered them the opportunity to comment on any allegations concerning them”：初稿“请他们对涉及自己的任何指控作出回应”把“给对方回应的机会”说成了“请求对方回应”，改为“给了他们机会，对涉及自己的任何指控作出回应”。
- 有意这样处理的地方：
  - “I have identified those records at length in the notes section at the end of the narrative”：本版已把书末注释改成各章脚注。按术语表“译者注”一条的安排，正文照原文译“我都在正文之后的注释部分详细注明了这些记录”，再加译者注 t1 说明注释的位置。
  - “either because they feared retribution..., worried that they might be swept up..., or wanted to guard their privacy” 拆成“有的……有的……有的……”三个分句，三种原因都保留。
  - “When I have attributed quotes to characters in dialogues, those quotes are reconstructed from participants’ memories.” 写“对话里人物说的话，是根据对话参与者的回忆还原的”，participants 指当时在场说话的人。
  - “as is her right” 移到句末，写“这是她的权利”，意思不变，中文更顺。
  - 术语按术语表：pseudonyms 写“化名”，deposition testimony 写“取证证词”，Justice Department 写“司法部”。the Theranos saga 写“Theranos 事件”。
  - 数字：hundreds of interviews 写“数百次采访”，more than 150 people 写“150 多人”，more than sixty former Theranos employees 写“60 多名 Theranos 前员工”，和术语表“150 多人”的写法一致。
- 人名：本节只有伊丽莎白·霍姆斯一人，原文写全名，中文写“伊丽莎白·霍姆斯（Elizabeth Holmes）”，和人名表一致。
- 检查：`site.py status bad-blood` 显示本节 4/4；中文正文没有破折号，也没有“不是……而是……”“而不是”句式；汉字和数字、英文之间都有空格，没有半角标点。
- 未决：
  - 没有未解决的意义问题。
  - `book.json` 里本节状态仍是 `todo`，按分工由主会话修改。

## 2. 双语审校

- 执行者：另一个独立上下文的 agent（Opus 5.5），没有参与翻译。
- 范围：标题、3 段正文和译者注 t1，逐块对照英文读完；核对了数字、术语和人名。同一位审校者也审了献辞、尾声、致谢和关于作者四节。
- 发现：1 条，是读起来有歧义的句子；核实后采纳 1 条，不采纳 0 条。
  - 采纳：“This book is based on hundreds of interviews with more than 150 people, including more than sixty former Theranos employees.” 原译“本书依据的是对 150 多人所做的数百次采访，其中包括 60 多名 Theranos 前员工”，“其中”紧跟在“数百次采访”后面，按语法指的是采访。改为“本书依据的是数百次采访，受访者有 150 多人，其中 60 多人是 Theranos 前员工”。编辑核对过：including 说的是受访的人，三个数字和英文一致。
- 审校者的总体判断：五节都逐块对照英文读完，作者说明 4/4 块对得上，译者注 t1 的位置和编号正确，术语符合术语表，中文没有破折号，也没有“不是……而是……”句式。作者说明只有第一句的“其中”需要改。审校时审校者没有改动文件。

## 3. 中文通读

- 执行者：编辑 agent（Opus 5.5）。
- 范围：审校意见改完以后，从标题顺着读到译者注。
- 发现并修改：没有新的改动。审校改过的第一句读来通顺，和后面“书中出场的人物大多用的是真名”衔接自然，改动已回查英文。“化名”“取证证词”“司法部”和术语表一致，伊丽莎白·霍姆斯第一次出现括注英文。
- 检查：`site.py status bad-blood` 显示本节 4/4；中文没有破折号，也没有“不是……而是……”句式。

## 状态

没有未解决的意义问题。`book.json` 里本节状态仍是 `todo`，阅读器校样还没有做。
