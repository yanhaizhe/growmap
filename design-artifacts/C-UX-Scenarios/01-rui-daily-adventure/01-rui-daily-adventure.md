---
design_intent: D
design_status: not-started
---
# 01: Rui's Daily Character Quest & Check-in

**Project:** 闫孜睿成长地图
**Created:** 2026-06-06
**Method:** Whiteport Design Studio (WDS)

---

## Transaction (Q1)

**What this scenario covers:**
- 小睿每日放学回家的成长地图“魔法探险”，完成本日的冒险故事阅读，通过轻量答题小练习，并一键完成自省打卡、解锁魔法勋章。

---

## Business Goal (Q2)

**Goal:** Goal 2 (培养日常自省打卡习惯) 与 Goal 1 (提升儿童模型理解)
**Objective:** Objective 2.1 (每日自主打卡率达 70%), Objective 1.1 (互动答题通过率 80%), Objective 2.2 (7天徽章解锁率 50%)

---

## User & Situation (Q3)

**Persona:** 小睿 (Rui the Explorer) (PRIMARY ⭐)
**Situation:** 8 岁的小学二年级学生小睿，放学回家刚写完作业，在自己的房间里拿着平板电脑，处于放松但有些疲惫、渴望趣味娱乐和成就认可的心理状态。

---

## Driving Forces (Q4)

**Hope:** 能够看到可爱、有趣的魔法宝石冒险故事，并在点击打卡后能收集到亮闪闪的虚拟成长勋章。

**Worry:** 害怕遇到大段看不懂的死板学术文字和繁杂输入（如写大段文字反思），让她觉得像在写额外作业。

---

## Device & Starting Point (Q5 + Q6)

**Device:** Tablet (平板电脑 / 触屏设备)
**Entry:** 双击平板桌面上已经保存好的本地 `小人书.html` 文件快捷方式，直接在浏览器中离线打开。

---

## Best Outcome (Q7)

**User Success:**
- 成功读完可爱的冒险故事章节，无压力地答对概念选择题，通过轻量点击/滑块完成打卡，开心地看到金黄色的“自省小魔导”徽章亮起并向爸爸展示。

**Business Success:**
- 本地 LocalStorage 成功稳定记录本次打卡数据，整个打卡反思过程在 5 秒内无障碍完成，小睿达成了本周连续 5 天打卡的成就，巩固了对同心圆对应态度的认知。

---

## Shortest Path (Q8)

1. **小人书封面 (kids-book-cover)** — 用户看到温暖可爱的魔法城堡与同心圆宝石封面，点击“开始冒险”按钮。
2. **故事阅读页 (kids-book-story)** — 用户阅读小圆寻找“积极宝石”与“努力跑鞋”的简短童话故事，在章节底部点击“获得宝石挑战”按钮。
3. **互动答题测验 (kids-book-quiz)** — 用户点击选项答对带有可爱插画的多选题，系统撒花提示挑战成功，自动滑出“每日打卡表”。
4. **每日自省打卡表与勋章陈列 (kids-book-checkin)** — 用户点选今日心情、滑拖今日积极表现分，勾选今日使用的宝石态度，点击“存入魔法瓶（打卡）”，系统弹出金光闪闪的“徽章解锁”界面并保存到陈列室。 ✓

---

## Trigger Map Connections

**Persona:** 小睿 (Rui the Explorer) (PRIMARY ⭐)

**Driving Forces Addressed:**
- ✅ **Want:** 获得魔法勋章与自我认可 (Unlock Magic Badges) — 解锁动态徽章，提升打卡成就感。
- ✅ **Want:** 经历可爱的魔法冒险 (Cute Magic Adventure) — 故事化拟人解释模型，通俗易懂。
- ❌ **Fear:** 枯燥说教与密集文字 (Boredom) — 极简童趣语言，纯原生 SVG 魔法感矢量图渲染，杜绝断图。

**Business Goal:** Goal 2 (自省习惯培养) 与 Goal 1 (模型理解)

---

## Scenario Steps

| Step | Folder | Purpose | Exit Action |
|------|--------|---------|-------------|
| 01.1 | `01.1-kids-book-cover/` | 呈现魔法绘本主题与同心圆结构心智模型，激发小女孩的探险好奇心。 | 点击“开始冒险”按钮进入第一章故事。 |
| 01.2 | `01.2-kids-book-story/` | 以图文并茂的故事具象化阐述“积极主动”与“努力学习”的态度与行为联系。 | 点击章节底部的“挑战积极宝石”按钮。 |
| 01.3 | `01.3-kids-book-quiz/` | 通过轻度选择题检验并巩固对本章态度的基本理解（MECE 关系）。 | 答对题目后，点击“挑战成功，去打卡”按钮。 |
| 01.4 | `01.4-kids-book-checkin/` | 完成心情、表现的滑动记录打卡，自动计算连续打卡天数并点亮/解锁徽章。 | 点击“收工！明天再来”，弹出徽章解锁成功弹窗。 ✓ |

---

_Generated with Whiteport Design Studio framework_
