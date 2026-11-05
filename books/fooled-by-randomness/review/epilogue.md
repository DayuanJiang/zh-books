# 尾声 梭伦早就说过（epilogue）审校记录

全节 5 个块，原文没有注释，中文另加 1 条译者注 [^t1]；中英逐块对应（`site.py status` 显示 5/5）。

## 1. 译者自检

- 执行者：translation agent（Opus 5.5），译者本人。
- 范围：全节 5 块和 1 条译者注，对照原文逐段检查漏译、增译、否定、条件、数字、人名、术语和格式。另外运行了 `python3 scripts/site.py status fooled-by-randomness`（5/5）；在 `/tmp` 的一份副本里把本节设成草稿后构建通过，[^t1] 显示为“译者注”弹窗；`tools/term_consistency.py` 对本节没有提示。也查过本节没有破折号、没有体例禁用的对比句式、中文里没有半角标点。
- 发现并修改：
  - 第 3 块 “Simultaneously as he beat the 28% odds, up to the point of complete cure”：只写“28% 的概率”，读者分不清是生还是死。第 11 章说尼禄的癌症五年存活率是 72%，死亡概率是 28%，所以写“他挺过了那 28% 的死亡概率，一直到完全康复”，补出“死亡”二字。
  - 第 4 块 “through a crash course in Cambridgeshire”：crash 和本节结尾的直升机坠毁（crashed）是双关，中文“速成班”保不住这层意思，加译者注 [^t1] 说明。
  - 第 5 块 “For Nero’s helicopter crashed …”：For 表示用后面的事来说明前一句，写“因为在一个刮大风的日子里……”。
- 译法上的选择：
  - 小标题 Beware the London Traffic Jams 写“当心伦敦的堵车”。
  - 第 3 块 *schadenfreude* 照术语表写“幸灾乐祸（*schadenfreude*）”，原文是小写斜体，括注照样；“A couple of years after we left him looking at John smoking a cigarette” 写“上次我们离开尼禄的时候……两三年后”，指第 1 章结尾约翰在门前抽烟那一幕；“Wall Street hotshots” 写“华尔街其他红人”，Wall Streeters 照术语表写“华尔街的人”。
  - 第 4 块 “his office in the city of London”“his office in the city”：尼禄是交易员，按上下文理解为伦敦金融城（the City），写“伦敦金融城的办公室”“金融城的办公室”；Cotswolds、Cambridgeshire、Kensington 照术语表写“科茨沃尔德”“剑桥郡”“肯辛顿”；“a pet extravagance” 写“一样心爱的奢侈享受”。
  - 第 5 块 Battersea Park 照术语表写“巴特西公园”；“In the end the black swan got its man.” 写“最终，黑天鹅还是逮住了它要找的人”。
- 人名：尼禄（Nero）、约翰（John），原文只写名，括注也只写名；标题里的梭伦不括注。
- 数字：28% 用阿拉伯数字；五个小时、两三年后用汉字。
- 未决：
  - 译者注 [^t1] 请用户决定是否保留；也可以去掉，只在这份记录里说明。
  - 第 4 块两处 city 理解为伦敦金融城，属于译者的判断，留给双语审校再看。
  - 双语审校、中文通读和阅读器校样还没有做；`book.json` 里本节的状态由主会话修改。

## 2. 双语审校

- 执行者：另一个独立上下文的 agent（Opus 5.5），没有参与翻译。
- 范围：全节 5 块和译者注 [^t1]，逐块对照英文；同时检查了破折号、禁用句式、半角标点、人名、术语和数字。
- 发现：2 条；核实后采纳 2 条，不采纳 0 条。
  - 第 3 块 “which could have allowed him to buy the goods they owned at very large discounts, if he wanted to”：原译“用极低的折扣”有歧义，中文里“折扣低”既可以理解成打折打得很狠，也可以理解成只便宜一点点，容易读反。采纳，改为“只要他愿意，本可以用极低的价格买下他们手里的东西”。
  - 第 5 块 “For Nero’s helicopter crashed as he was landing it near Battersea Park on a windy day.”：原译以“因为”开头单独成句，读起来像半句话。采纳，去掉“因为”；上一句说他对人身风险不够敏感，这一句紧接着讲坠机，读者自然看得出这是例证。
- 审校者还核对了译者注 [^t1]：它解释 crash course 和结尾直升机坠毁（crashed）的双关，审校者认为有必要，标记的位置也对。
- 审校者的总体判断：十个分节逐块对照英文读完，总体质量很高，可以进入中文通读。每一块都已译完，中英逐块对应；没有破折号、“不是……而是……”句式和混进中文的半角标点；28%、两三年、五个小时这些数字都正确。没有发现事实、数字、否定或人物关系上的错误。

## 3. 中文通读

- 执行者：编辑 agent（Opus 5.5）。
- 范围：顺着中文把全节从头读到尾，看行文是否连贯、有没有重复、指代是否清楚、人名和术语前后是否一致；审校带来的两处改动连同上下文回查了英文。
- 发现并修改：通读没有发现需要再改的地方。
- 核对过的地方：“28% 的死亡概率”和第 11 章英文 “a 28% chance of death and a 72% chance of survival” 对得上；第 4 块两处 city 写“伦敦金融城”“金融城”，尼禄是交易员，这样理解合乎上下文，双语审校也没有提出异议，保留；幸灾乐祸（*schadenfreude*）的括注照原文用小写斜体；尼禄、约翰只在第一次出现时括注。改完后没有破折号、禁用句式和半角标点，`site.py status` 仍显示 5/5。

## 状态

- 没有未解决的意义问题。
- 留给用户决定的事项：译者注 [^t1] 是否保留（见译者自检的未决事项）。阅读器校样还没有做；`book.json` 里本节的状态由主会话修改。
