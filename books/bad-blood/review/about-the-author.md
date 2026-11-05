# 关于作者（about-the-author）审校记录

全节 2 个块，原文没有注释，中英逐块对应（`site.py status` 显示 2/2）。

## 1. 译者自检

- 执行者：translation agent（Opus 5.5），译者本人。
- 范围：标题和 1 段正文，从头译到尾。译完后逐句对照英文核对奖项名称、获奖次数和人名。
- 发现并修改：没有发现漏译或误译。核对了三项奖项的数量（三项）和顺序，以及原文说作者两次获得普利策奖（two-time Pulitzer Prize winning），写成“曾两度获得普利策奖”，没有把两次普利策奖算成这次 Theranos 报道得的奖。
- 有意这样处理的地方：
  - 三个奖项没有通行的中文名，中文名后括注英文全称：“乔治·波尔克财经报道奖（George Polk Award for Financial Reporting）”“杰拉尔德·洛布商业与财经新闻杰出奖（Gerald Loeb Award for Distinguished Business and Financial Journalism）的条线报道类奖项”“巴利特与斯蒂尔商业调查新闻银奖（Barlett & Steele Silver Award for Investigative Business Journalism）”。in the category of beat reporting 指洛布奖下面的一个类别，写“条线报道类”，beat 是记者长期跟踪的固定领域。
  - Pulitzer Prize 写“普利策奖”，不括注。
  - For his extensive coverage of Theranos 写“凭借对 Theranos 的大量报道”。
  - 作者第一次出现写“约翰·卡雷鲁（John Carreyrou）”，后面照原文写姓“卡雷鲁”。Brooklyn 写“布鲁克林”。
- 检查：`site.py status bad-blood` 显示本节 2/2；中文没有破折号和体例禁用的对比句式；没有半角标点。
- 未决：
  - 三个奖项的中文名是按字面拟的，没有核实过有没有官方或通行的中文名；beat reporting 写“条线报道”，也可以写“跑口报道”，请主会话定。
  - `book.json` 里本节状态仍是 `todo`，按分工由主会话修改。

## 2. 双语审校

- 执行者：另一个独立上下文的 agent（Opus 5.5），没有参与翻译。
- 范围：标题和 1 段正文，对照英文读完；核对了获奖次数、三个奖项的名称和顺序，以及人名。同一位审校者也审了献辞、作者说明、尾声和致谢四节。
- 发现：0 条；采纳 0 条，不采纳 0 条。
- 审校者的总体判断：五节都逐块对照英文读完，关于作者 2/2 块对得上，人名和 people-zh.tsv 一致，中文没有破折号，也没有体例禁用的对比句式。关于作者没有需要改的地方。审校时审校者没有改动文件。

## 3. 中文通读

- 执行者：编辑 agent（Opus 5.5）。
- 发现并修改：顺着中文读了一遍，没有改动。“曾两度获得普利策奖”和三个奖项的关系读来清楚，作者第一次出现写全名并括注英文，后面写“卡雷鲁”。
- 检查：`site.py status bad-blood` 显示本节 2/2。

## 状态

没有未解决的意义问题。三个奖项的中文名是按字面拟的，beat reporting 写“条线报道”还是“跑口报道”，仍由主会话决定，不影响意思。`book.json` 里本节状态仍是 `todo`，阅读器校样还没有做。

## 第三轮：GPT-6 Astra 独立审校

- 审校者：GPT-6 Astra，通过 Codex 运行，只读，和译者属于不同的模型家族。
- 发现：0 条。审校者逐块核对了全文，总体判断是“未发现需要修订的实质问题；本节无脚注”。逐条核实的结果：成立并修改 0 条，不成立 0 条。
- 成立并修改：无。
- 不成立，保留原译：无。
- 按全书统一的写法修改：0 处。对照了“全书统一的写法”和“全书统一的写法（译完后定）”两部分，本节已经符合：英文第一次写全名 John Carreyrou，中文写“约翰·卡雷鲁（John Carreyrou）”，括注和原文在这个位置的写法一致，译名和 `review/terms/people-zh.tsv` 一致，后面原文只写姓 Carreyrou，中文写“卡雷鲁”；《华尔街日报》属于常见报刊，不括注；Theranos 照写原名；two-time 写“两度”，three children 写“三个孩子”，符合一到十用汉字的数字写法；Pulitzer Prize 写“普利策奖”，和第 15 章的写法一致。标题“关于作者”和 glossary 各节标题表一致。本节没有头衔、脚注、邮件主题或 miniLab 这类术语，其余几条用不上。中文里没有破折号，也没有体例禁用的对比句式。
- 对英文原文的疑问：审校者没有提出，核实时也没有发现。
- 核实与修改：agent（Opus 5.5）。本轮没有改动中文文件。前两轮留下的问题保持原样：三个奖项的中文名按字面拟定，beat reporting 写“条线报道”还是“跑口报道”，仍由主会话决定。运行 `python3 scripts/site.py status bad-blood`，本节显示 2/2 块已译，原文没有注释。
