# 关于作者（about-the-authors）审校记录

全节 3 个块（标题和两个段落），原文没有注释，中英逐块对应（`site.py status` 显示 3/3）。英文是 2026 年 11 月 5 日从 HarperCollins 的完整电子书补进来的，见 [source.md](source.md) 的“用更好的来源补全（2026-11-05）”。电子书这一节的最后一行是出版社网站 hc.com 的广告，没有收入。

## 1. 译者自检

- 执行者：Claude（Opus 5.5），译者本人。
- 范围：标题和两个段落，逐句对照英文，查漏译、增译、人名、机构名、书名和体例。
- 处理：
  - 标题 About the Authors 写“关于作者”，和仓库里其他书一样。
  - 人名：电子书用加粗大写写段首的人名，`en/` 写成加粗的 **Chris Voss**、**Tahl Raz**，中文也加粗。照体例，作者本人的名字“克里斯·沃斯”省去括注；塔尔·拉兹第一次出现括注 Tahl Raz。第 2 块原文后面又写 Chris，中文写“他”，读者不会弄错是谁。
  - 学校：University of Southern California’s Marshall School of Business 写“南加州大学马歇尔商学院”，Georgetown University’s McDonough School of Business 写“乔治城大学麦克多诺商学院”，Sloan School of Management 和 Kellogg School of Management 照原文不带大学名，写“斯隆管理学院”“凯洛格管理学院”。这些写法补进了术语表。
  - 书名：*Never Eat Alone* 有中译本《别独自用餐》（世界知识出版社、读客文化都出过），用中译本书名，括注原题；《纽约时报》照体例不括注。
  - 电子邮件地址和网址照写原文。
  - preeminent 出现两次，第一次写“最杰出的……之一”，第二次写“顶尖大学”。
- 发现并修改：
  - 第 3 块 “lectures widely on the forces transforming the new world of work”：初稿“讲述正在改变新的工作世界的种种力量”，“改变新的”读着别扭，改为“讲述正在重塑这个新的工作世界的种种力量”。
- 术语一致性：`tools/term_consistency.py` 在本节没有标出问题。
- 还没有做：双语审校、中文通读和阅读器校样。

## 2. 双语审校（补全部分）

- 审校者：agent（Opus 5.5），独立的双语审校，没有参与这次补全和翻译。
- 范围：全节 3 个块，逐句对照英文，查意思、漏译、人名、学校名、书名、中文是否通顺、破折号和对比句式。英文和完整电子书一致，两位作者的名字在电子书里是大写，`en/` 改成了首字母大写。
- 结果：没有需要修改的地方。学校名和术语表一致；《别独自用餐》（*Never Eat Alone*）是中译本书名；克里斯·沃斯不括注、塔尔·拉兹第一次出现括注，合乎体例；第 2 块后面的 Chris 写“他”，不会误解；电子邮件地址和网址照原文。全节没有破折号和对比句式。
- 运行 `python3 scripts/site.py status never-split-the-difference`：全书 13 节都是 review，1958/1958 个块已译，注释 23/23；`python3 scripts/site.py check never-split-the-difference` 的草稿构建通过。
