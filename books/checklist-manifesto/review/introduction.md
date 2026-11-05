# 引言（introduction）审校记录

全章 55 个块、7 条注释，另有 2 条译者注，中英逐块对应（`site.py status` 显示 55/55、7/7）。这一章是全书的样章，译文风格以它为准。

## 1. 译者自检

- 执行者：sample translation agent（Opus 5.5），译者本人。
- 范围：全章 55 块（1 个标题、54 个段落）和 7 条注释，对照原文逐段检查漏译、增译、否定、数字、人名、术语和注释；译完后又顺着中文读了一遍，改动的地方都回查了英文。
- 检查：`site.py status` 显示 55/55、7/7；`site.py check` 的草稿构建通过（字体子集还没有生成，构建提示缺字，这本书还没有运行过 `site.py fonts`）；`tools/term_consistency.py` 查了 29 处术语和人名，没有不符合约定译法的块；正文没有破折号，也没有体例禁用的对比句式；注释 2 至 7 的出处和英文逐字相同，[^t1]、[^t2] 在正文里都有引用。
- 发现并修改：
  - 第 13 块 “The description was pretty close, it turned out. The other guy at the costume party, John later learned”：初稿“后来才知道……约翰事后得知”两次说“后来”，改为“事实证明，这个说法八九不离十。约翰后来得知……”。
  - 第 37 块 “Much of the world and universe … outside our understanding and control”：初稿“世界和宇宙的大部分”说重了，much of 是“很多”，改为“世界和宇宙中有很多东西”。
  - 第 52 块 “People spend years of sixty, seventy-, eighty-hour weeks”：初稿加了“甚至”，原文只是把三个数字排在一起，删去，改为“每周工作 60、70、80 个小时”。
  - 第 52 块 “what is striking about John’s cases”：初稿“引人深思”偏离了 striking（值得注意），改为“约翰的病例有一点值得注意”。
  - 第 36 块 “We talk about our great saves but also about our great failures”：初稿“最了不起的那些救回来的病例”“最惨痛的失败”把 great 译成了最高级，改为“那些漂亮地救回来的病例”“那些惨痛的失败”。救回来的病例按术语表 great saves 的译法。
  - 第 35 块 “They’d not only nearly killed the man but also failed to recognize how”：初稿“当时没能看出是怎么回事”，改为“而且自己都没能看出问题出在哪里”，说清楚没看出来的是手术团队自己。
  - 第 18 块 “a fleshy mouse-size mass”：初稿“一团老鼠大小的肉”像在说一块肉，改为“一个老鼠大小的肉质肿块”；同一块的 “And there on the images it was” 初稿用了“果然”，原文没有预料之中的意思，改为“片子上看得清清楚楚”。
  - 第 18 块 “in his late forties”：初稿“四十七八岁”比原文精确，改为“年近五十”。
  - 第 5、7 块 “nurses racing to get the surgical equipment set up”：初稿“护士们抢着把手术器械摆好”，“抢着”容易读成互相争抢，两处都改为“争分夺秒地准备手术器械”，保留原文两段话前后呼应的写法。
  - 第 48 块 “You see it in the 36 percent increase … the most common being simple administrative errors”：初稿用冒号把“从中也能看到”和后面的失误类型接在一起，读起来像看到的就是这些失误。拆成两句：“……增加了 36%，从中也能看到这一点。这些失误里最常见的，是简单的事务性差错……”；“在有缺陷的软件设计……里，也都能看到这一点”补上了“在……里”。
  - 第 36 块 “are often about the shock of the unexpected … and sometimes about regret over missed possibilities”：初稿“常常围绕……有时也关于……”前后搭配不一致，改为“常常讲的是……有时讲的是……”。
  - 第 42 块 “at home as a cardiac cripple”：初稿“作为一个心脏落下残疾的人度过余生”带翻译腔，改为“回家做个心脏残疾的人，度过余生”。
  - 第 41 块 “We didn’t know about the role of cholesterol, either, or genetics or smoking or diabetes”：初稿把一句拆成两半，读着啰嗦，改为“我们也不知道胆固醇、遗传、吸烟和糖尿病各自起什么作用”。
  - 第 47 块 “insurance company hassles”：初稿“刁难”带了原文没有的故意意味，改为“种种麻烦事”；第 49 块 “seems to cloud how we think about them” 初稿“没法看清它们”改为“没法冷静地思考它们”。
- 照体例处理的地方：
  - 人名：约翰（John）、塞缪尔·戈罗维茨（Samuel Gorovitz）、阿拉斯代尔·麦金太尔（Alasdair MacIntyre）在本章第一次出现时括注英文，之后只写中文，和 `review/terms/people-zh.tsv` 一致；注释里的人名照写英文。
  - 术语：ignorance 译“无知”，ineptitude 第一次出现写“无能（ineptitude）”，failures of ignorance 译“无知造成的失败”；necessary fallibility 写“必然的易错”，加引号并括注原文；eptitude 写“有能”（eptitude），加译者注 [^t2] 说明构词；Code Blue 写“蓝色代码（Code Blue）”，加译者注 [^t1]；asystole 原文正在解释这个词，写“心脏停搏（asystole）”；know-how 译“知识和本领”，expertise 译“专业能力”，avoidable failures 译“可以避免的失败”。
  - 单位：about two hundred pounds 写“大约 200 磅（约 90 公斤）”，two-inch 写“两英寸（约 5 厘米）”，more than a foot 写“一英尺（约 30 厘米）还多”。伤口只有两英寸，刀却刺进去一英尺多，这个对比对读者要紧，所以都括注了公制。
  - 数字：一到十和约数用汉字（两天、五秒钟、四个小时、十几种、十多年、上千处），11 以上的确数用阿拉伯数字（15 分钟、20 分钟、90 分钟、100 倍），百分比写 100%、50%、30%、36%。
  - 原文的破折号按意思改成冒号、逗号或括号，或者另起一句。
  - 原文表示强调的斜体保留：“这下，他们*真的*要冲进手术室了”“*这*才让他烧心”。第 49 块用斜体指称词语本身的 *ineptitude*、*negligence*、*heartlessness*，中文改用引号：“无能”“失职”“冷血”。
  - 第 47 块 “It is not money or government … It is the complexity”、第 50 块 “has not been to punish failure but instead to encourage” 两处英文都是先否定一种说法、再给出另一种的对照结构，中文按体例换成直接的说法：“虽然都有影响，但根源都不在这里。根源在于……”“是鼓励人们积累更多经验、接受更多训练，而不去惩罚失败”。
  - 注释：开头引号里的词句译成中文，和正文里标记前面的中文对应，例如注释 2 “20 世纪 70 年代”、注释 4 “超过这个时间，存活率”、注释 7 “增加了 36%”；出处保留英文，注释 3 的 See also 译“另见”；注释 1 按术语表给定的译法。注释 1 在原文里标在句号后面，中文也放在句号后面。
- 未决（供用户确认风格时参考）：
  - 第 7 块 “a whole bottle of Betadine antiseptic”：Betadine 是聚维酮碘的品牌名，中国大陆通称“碘伏”，译作“一整瓶碘伏消毒液”，品牌名没有保留。
  - 第 28 块 “a bolus of epinephrine … adrenalin”：英文同时给出学名和俗名，中文两个词都是“肾上腺素”，只写一次。
  - 第 2 块 “We were trading war stories”：war stories 是惯用语，指从业中的惊险经历，按意思译作“我们互相讲起从医以来的惊险经历”。后面的 “since Vietnam” 是真的战争，译作“越战”。
  - 第 10 块 “Crap.” 译作“该死。”，第 32 块 “that’s how states execute prisoners” 译作“美国各州处决犯人，用的就是这个办法”，补出了“美国”。
  - 第 55 块，引言的最后一句 “It is a checklist.” 译作“那就是清单。”，另一个可选的说法是“那就是一张清单。”，后者更突出这个东西的简单。
  - 第 44 块 eptitude 的译法“有能”和译者注 [^t2] 的写法，以及 Code Blue 的译者注 [^t1]，样章认可后各章照此处理。
  - 建议在术语表里补两条，留给主会话决定：heart attack 全书统一写“心脏病发作”（本章正文出现 9 次）；原文用斜体指称词语本身的地方，中文改用引号。

## 原文疑点

| 位置 | 原文 | 处理 |
| --- | --- | --- |
| 第 17 块，注释 1 | EPUB 里 “his heart suddenly stopped.*” 只有星号，没有注释文字 | 已记在 `review/source.md`：注释文字按美国版第 4 页的脚注补回，英国版纸质书没有核对。中文按补回的文字翻译 |
| 第 6 块 | His blood pressure was barely detectible | detectible 是 detectable 的异体拼写，不算错误，`en/` 照原文保留，意思照常翻译 |
