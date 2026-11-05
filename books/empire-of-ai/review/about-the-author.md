# 关于作者（about-the-author）审校记录

全节 2 个块、0 条注释，中英逐块对应（`site.py status` 显示 2/2）。

## 1. 译者自检

- 执行者：translation agent（Opus 5.5）。
- 范围：全节 2 块，对照原文逐句检查头衔、机构和奖项。
- 发现并修改：
  - 作者姓名按 `people-zh.tsv` 作“郝珂灵（Karen Hao）”。原文姓名是粗体，中文写成 `**郝珂灵**（Karen Hao）`：如果把括号也放进粗体，右括号后面紧跟汉字，Markdown 不会把粗体闭合，渲染后会露出星号。
  - “numerous accolades”初稿“获奖无数”偏夸张，改作“多次获奖”。
  - “a program training thousands of journalists around the world on how to cover AI”用现在时，译作“这个项目培训世界各地数以千计的记者”。
  - “American Society of Magazine Editors NEXT Award for Journalists Under 30”译作“美国杂志编辑协会颁给 30 岁以下记者的 NEXT 奖”。
- 未决：“AI Spotlight Series”和“American Humanist Media Award”没有查到通行中文名，分别译作“AI 聚焦系列”“美国人文主义者媒体奖”，括注原文。

## 2. 双语审校

- 执行者：另一个独立上下文的 agent（Opus 5.5），没有参与翻译。
- 范围：全节 2 块，对照英文核对头衔、机构和奖项。
- 发现：0 条；核实后采纳 0 条，不采纳 0 条。
- 审校者的总体判断：五个分节逐块对照英文读完，脚注和译者注都看过，整体质量较好，可以作为定稿的基础。结构完全对齐（献辞 7/7、题词 6/6 和 2/2、作者说明 5/5、致谢 15/15、关于作者 2/2），五个文件里没有破折号，也没有“不是……而是……”句式；人名按 people-zh.tsv，每节第一次出现括注英文；术语符合术语表；数字（300 多次采访、约 260 人、150 多次、90 多名、约 40 名、十多个小时、六个月、2021 年底）都核对无误。实质问题有四处：作者说明里对话来源一句前后矛盾，题词里“不如他开明”误译，致谢里“报警抓他”多了意思，“让报道得以成行”搭配不当；其余是表达问题，集中在致谢一节。“关于作者”一节没有发现问题。

## 3. 中文通读

- 执行者：编辑 agent（Opus 5.5）。
- 发现并修改：“她的作品经常被大学用于教学，也经常被各国政府引用”，两个“经常”连用，第二个改为“常”。回查英文 regularly taught in universities and cited by governments，意思不变。
- 通读确认：“郝珂灵（Karen Hao）”按 `people-zh.tsv`；刊名第一次出现括注英文；“屡获殊荣”和后文“多次获奖”分别对应 award-winning 和 numerous accolades，原文也是两处，保留。

## 状态

- 没有未解决的意义问题。“AI 聚焦系列”“美国人文主义者媒体奖”是暂译，括注了原文，留给主会话确认。
- `site.py status` 显示 2/2。

## 第三轮：GPT-6 Astra 独立审校

- 审校者：GPT-6 Astra，通过 Codex 运行，只读，和译者属于不同的模型家族。
- 发现：0 条。审校者逐块核对了全节 2 块，认为没有需要修改的实质问题；本节没有脚注。核实者另外对照英文重读了正文一段：award-winning 译“屡获殊荣”，numerous accolades 译“多次获奖”；“leads the Pulitzer Center's AI Spotlight Series”译“主持普利策中心（Pulitzer Center）的‘AI 聚焦系列’（AI Spotlight Series）”，普利策中心的写法和致谢一节一致；“formerly a reporter for the Wall Street Journal ... and a senior editor for AI at MIT Technology Review”译“曾任《华尔街日报》记者……也曾任《麻省理工科技评论》的 AI 高级编辑”；两个奖项和“机械工程理学学士学位”都和原文相符。同意审校者的判断。成立并修改 0 条，不成立 0 条。
- 成立并修改：无。
- 不成立，保留原译：无。
- 对英文原文的疑问：无。
- 按全书统一的写法修改：0 处。逐条对照术语表“全书统一的写法”：“30 岁以下”是 11 以上的确数，用阿拉伯数字，“数以千计”是约数，用汉字；《大西洋月刊》《华尔街日报》《麻省理工科技评论》属于常见报刊，按约定不括注，现在的译文也没有括注；作者名“郝珂灵（Karen Hao）”第一次出现括注英文；没有平台名、需要统一的头衔和机构名。全节中文里也没有破折号和“不是……而是……”句式。
- 核实与修改：agent（Opus 5.5）。本节没有改动。之后运行 `python3 scripts/site.py status empire-of-ai`，关于作者一节显示 2/2 块已译、没有注释，全书 1681/1681 块已译（100%）。
