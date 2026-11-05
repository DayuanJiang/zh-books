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
- 检查：`site.py status bad-blood` 显示本节 2/2；中文没有破折号和“不是……而是……”句式；没有半角标点。
- 未决：
  - 三个奖项的中文名是按字面拟的，没有核实过有没有官方或通行的中文名；beat reporting 写“条线报道”，也可以写“跑口报道”，请主会话定。
  - `book.json` 里本节状态仍是 `todo`，按分工由主会话修改。

## 2. 双语审校

- 执行者：另一个独立上下文的 agent（Opus 5.5），没有参与翻译。
- 范围：标题和 1 段正文，对照英文读完；核对了获奖次数、三个奖项的名称和顺序，以及人名。同一位审校者也审了献辞、作者说明、尾声和致谢四节。
- 发现：0 条；采纳 0 条，不采纳 0 条。
- 审校者的总体判断：五节都逐块对照英文读完，关于作者 2/2 块对得上，人名和 people-zh.tsv 一致，中文没有破折号，也没有“不是……而是……”句式。关于作者没有需要改的地方。审校时审校者没有改动文件。

## 3. 中文通读

- 执行者：编辑 agent（Opus 5.5）。
- 发现并修改：顺着中文读了一遍，没有改动。“曾两度获得普利策奖”和三个奖项的关系读来清楚，作者第一次出现写全名并括注英文，后面写“卡雷鲁”。
- 检查：`site.py status bad-blood` 显示本节 2/2。

## 状态

没有未解决的意义问题。三个奖项的中文名是按字面拟的，beat reporting 写“条线报道”还是“跑口报道”，仍由主会话决定，不影响意思。`book.json` 里本节状态仍是 `todo`，阅读器校样还没有做。
