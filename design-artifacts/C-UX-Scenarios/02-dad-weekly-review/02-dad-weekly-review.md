---
design_intent: D
design_status: not-started
---
# 02: Dad's Weekly Progress Check & Guided Reflection

**Project:** 闫孜睿成长地图
**Created:** 2026-06-06
**Method:** Whiteport Design Studio (WDS)

---

## Transaction (Q1)

**What this scenario covers:**
- 爸爸在周末与孩子开展亲子复盘时，在电脑上打开成长地图页面，查看完美的几何对称同心圆，并读取本地 LocalStorage 渲染的图表，分析孩子本周的打卡雷达图/柱状图。

---

## Business Goal (Q2)

**Goal:** Goal 3 (网页视觉与离线优化) 与 Goal 1 (同心圆模型的深度理解)
**Objective:** Objective 3.1 (SVG完美对称), Objective 3.3 (离线运行零报错), Objective 2.3 (家长每周两次对话)

---

## User & Situation (Q3)

**Persona:** 爸爸 (Dad the Guide) (SECONDARY)
**Situation:** 30 多岁的理性职场父亲，在周末下午的客厅里，拿着笔记本电脑，陪女儿坐在沙发上，准备对这周的行为习惯进行亲子复盘与沟通。

---

## Driving Forces (Q4)

**Hope:** 能够看到完美对称的同心圆图表，并直观掌握孩子最近的心境变化和态度分布。

**Worry:** 担心本地离线运行报错、打卡数据发生丢失，或者说教过于死板引起女儿的抵触。

---

## Device & Starting Point (Q5 + Q6)

**Device:** Desktop / Laptop (台式机或笔记本电脑 / 鼠标点击操作)
**Entry:** 双击本地的 `成长地图.html`，或者在 `小人书.html` 的页面底部点击“魔法导师（家长）入口”切换跳转而来。

---

## Best Outcome (Q7)

**User Success:**
- 爸爸在 2 分钟内看清女儿这周打卡最少的是“同理心”，从而在接下来的亲子对话中，借助书中“同理心宝石”的故事进行温馨复盘，促成高质量对话。

**Business Success:**
- 页面 100% 离线完美渲染，完美极坐标对称的 SVG concentric circle 实现平滑的高亮交互，LocalStorage 数据安全读出，展现高级感。

---

## Shortest Path (Q8)

1. **家长验证入口 (parent-login-or-toggle)** — 爸爸双击打开 `成长地图.html`，或从小人书通过暗门导航切换，展示极简的“魔法导师”身份验证或侧边栏切换。
2. **成长地图与数据复盘页 (parent-growth-map)** — 呈现完美对称的 SVG 成功同心圆图表。下方自动读取 LocalStorage，动态渲染雷达图（六维态度）和本周心情柱状图。 ✓

---

## Trigger Map Connections

**Persona:** 爸爸 (Dad the Guide) (SECONDARY)

**Driving Forces Addressed:**
- ✅ **Want:** 直观掌握孩子心境与成长轨迹 (Trace Progress Visually) — 统计图表展示，精准了解孩子。
- ✅ **Want:** 几何对称、极简美观的 SVG 成功同心圆 (Visual Symmetry) — 对称极坐标设计，展现模型神韵。
- ❌ **Fear:** 理论流于形式无法落地 (Superficiality) — 亲子伴读引导提示，提供实用的引导话题。

**Business Goal:** Goal 3 (视觉美化与离线体验) 与 Goal 1 (认知理解)

---

## Scenario Steps

| Step | Folder | Purpose | Exit Action |
|------|--------|---------|-------------|
| 02.1 | `02.1-parent-login-or-toggle/` | 区分孩子打卡区与家长复盘区，避免孩子误删本地打卡记录。 | 点击“进入魔法导师视角”并输入简易口令/确认。 |
| 02.2 | `02.2-parent-growth-map/` | 呈现高水准的对称 SVG 同心圆图示和孩子打卡的可视化雷达图/周报，提供亲子对话的实证材料。 | 复盘对话完毕，点击退出或备份数据。 ✓ |

---

_Generated with Whiteport Design Studio framework_
