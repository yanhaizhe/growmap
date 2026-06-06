# Feature Impact Analysis: 闫孜睿成长地图

> Prioritizing product features based on their psychological impact on target personas

**Created:** 2026-06-06
**Author:** Yanhaizhe
**Status:** Approved (Dream Mode Synthesis)

---

## Scoring Methodology

To ensure every feature directly supports our target users' psychology, we evaluate them against our two personas:
* **Primary Persona (⭐ - Rui the Explorer):** High Impact = 5 pts | Medium Impact = 3 pts | Low Impact = 1 pt
* **Secondary Persona (Dad the Guide):** High Impact = 3 pts | Medium Impact = 1 pt | Low Impact = 0 pts

- **Max Possible Score:** 8 (2 personas)
- **Must Have Threshold:** 6+ OR Primary High (5 pts)

---

## Prioritized Features

| Rank | Feature | Rui (⭐) | Dad | Score | Decision |
| :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | **完全几何对称且可交互的同心圆 SVG** (成长地图主视图) | 5 (High) | 3 (High) | 8/8 | **Must Have MVP** |
| 2 | **趣味魔法冒险故事扩充** (小人书故事情节精细化) | 5 (High) | 3 (High) | 8/8 | **Must Have MVP** |
| 3 | **每日自省打卡表组件** (极简拖拽与心情点选交互) | 5 (High) | 3 (High) | 8/8 | **Must Have MVP** |
| 4 | **本地“魔法勋章”收集与奖励陈列室** | 5 (High) | 1 (Med) | 6/8 | **Must Have MVP** |
| 5 | **故事情节互动验证小答题** (轻量选择题验证) | 3 (Med) | 3 (High) | 6/8 | **Must Have MVP** |
| 6 | **100% 离线单文件运行架构** (内联 CSS/JS/原生 SVG 插画) | 1 (Low) | 3 (High) | 4/8 | **Technical Must** |
| 7 | **环境背景音乐与点击音效** (音频支持) | 3 (Med) | 0 (Low) | 3/8 | **Defer** |

---

## Decisions & Detailed Explanations

### 1. Must Have MVP (Core Release)

#### 🗺️ 完全几何对称且可交互的同心圆 SVG (Score: 8/8)
* **Description:** 用基于极坐标的精准 SVG 重新绘制“成功同心圆”图表，纠正原版的视觉偏差。支持鼠标 hover 或点击扇区时，对应的“态度”和“行为”卡片进行高亮聚焦，反之亦然。
* **Rui Impact:** 提供即时的视觉和交互反馈，使抽象图表像是一个精致的魔法盘。
* **Dad Impact:** 视觉上的完美对称契合了“第一性原理”和“不重不漏”（MECE）的系统美学，有利于在孩子脑海中建立高度结构化的记忆。

#### 📖 趣味魔法冒险故事扩充 (Score: 8/8)
* **Description:** 扩充《小人书.html》的文本，将原本简陋的理论名词转化为小圆（主角）收集 6 颗态度魔法宝石和 6 双行为跑鞋的冒险旅程。
* **Rui Impact:** 极大地满足了故事带入感，用角色行为展示（如用同理心宝石感化发怒的怪兽）代替干瘪概念。
* **Dad Impact:** 提供了绝佳的亲子睡前伴读剧本，爸爸不需要自己去编故事，照着网页读就能把道理讲透。

#### 📝 每日自省打卡表组件 (Score: 8/8)
* **Description:** 设计一个圆润、色彩柔和的每日自省交互区域。孩子可以通过简单的滑块、图标点击或多选卡片，记录“今日心情”和“今日使用成功的魔法态度”。打卡数据存储在本地 LocalStorage 中。
* **Rui Impact:** 交互无压力，打卡像玩玩具一样轻松。
* **Dad Impact:** 提供了量化孩子心理和日常行为表现的可视化图表，让周末沟通复盘更科学、更有实证。

#### 🏆 本地“魔法勋章”收集与奖励陈列室 (Score: 6/8)
* **Description:** 当孩子连续打卡 3 天、7 天，或者在小人书中答对所有题目时，解锁相应的“魔法徽章”（如“自省小魔导”、“勇气之盾”）。徽章在陈列室中亮起。
* **Rui Impact:** 强烈的收集癖驱动和成就反馈，鼓励她每天坚持打开页面。
* **Dad Impact:** 为现实中的正面管教（如兑换现实小奖品）提供了可视化的数值与记录依据。

#### ❓ 故事情节互动验证小答题 (Score: 6/8)
* **Description:** 在小人书的章节末尾或打卡前，插入 1-2 道非常简单的场景选择题（如：“当同桌不小心弄脏了你的画纸，你应该用什么魔法态度面对她？【A. 同理心与胸怀】 【B. 逃避与生气】”）。
* **Rui Impact:** 提供适度的探索挑战，增强主角代入感。
* **Dad Impact:** 检验和确保孩子真正理解了概念的外延，而不是机械式打卡。

---

### 2. Technical Must (无条件保留)

#### 📦 100% 离线单文件运行架构 (Score: 4/8)
* **Description:** 将整个系统打包为单个 `.html` 文件，所有插画使用原生 SVG 标签直接嵌入，所有 CSS 和 JS 内嵌。
* **Strategic Value:** 虽在用户心理层面评分低（孩子不关心底层技术），但这是最高的技术硬性约束。单文件形式保证了极其方便的分发性（直接拷进平板即可运行），彻底消除了网络延迟和外部图片断裂的隐患，保证了极致稳定性。

---

### 3. Defer (下阶段考虑)

#### 🎵 环境背景音乐与点击音效 (Score: 3/8)
* **Description:** 引入背景魔法音乐和按钮点击反馈音效。
* **Reason for Deferral:** 依照限制条件，为了极简的离线分发体量（避免引入大体积 MP3 资源导致打包体积爆棚），暂时砍掉音效，保证页面的轻量和纯净。

---

_Back to [Trigger Map](../00-trigger-map.md)_
