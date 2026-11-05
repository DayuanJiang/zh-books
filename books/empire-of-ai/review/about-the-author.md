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
