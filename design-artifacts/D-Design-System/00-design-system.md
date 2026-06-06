# Design Tokens: 闫孜睿成长地图

**Last Updated:** 2026-06-06
**Token Count:** 48

---

## 1. Visual Themes

本系统包含两个页面，分别适配不同的用户群体（儿童/家长），采用双重主题设计系统：

### 主题 A：魔法童话绘本风 (适合儿童 · 小人书.html)
- **视觉特质**：马卡龙粉嫩色系、手绘感扁平矢量插画、大圆角、毛玻璃光晕、温柔呼吸动效。
- **字体**：以圆润、温和的 `PingFang SC` / `Microsoft YaHei` 为主，加入斜体与手写体风格。

### 主题 B：深邃极简分析风 (适合家长 · 成长地图.html)
- **视觉特质**：暗沉夜空深邃蓝/紫色背景、高对比度荧光渐变（态度为橙黄，行为为翠绿，诚信为嫣红）、超清玻璃防直射微光、几何精确对称、平滑过渡动效。
- **字体**：清晰、高可读性的无衬线字体体系。

---

## 2. Color Palette (颜色标记)

### 主题 A (儿童魔法绘本) 调色盘
```yaml
# 页面底色与纸张色
kids-bg-pastel: "linear-gradient(180deg, #fffcf4 0%, #fff8e7 100%)" # 温润麦芽糖浅黄
kids-card-bg: "rgba(255, 255, 255, 0.85)"
kids-text-primary: "#4a3c31" # 温暖深褐（替代纯黑）
kids-text-muted: "#8c7a6b"

# 三层环魔法宝石色彩
kids-magic-core: "#ff7675"    # 诚信宝石 - 嫣红
kids-magic-attitude: "#fab1a0" # 态度魔法 - 蜜桃粉橙
kids-magic-behavior: "#55efc4" # 行为超能力 - 亮薄荷绿

# 状态色
kids-state-success: "#2ecc71" # 答题绿
kids-state-error: "#e74c3c"   # 抖动红
kids-state-highlight: "#ffeaa7" # 宝石亮金
```

### 主题 B (家长分析面板) 调色盘
```yaml
# 背景与容器色
parent-bg-dark: "linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%)" # 三色极夜深邃
parent-card-bg: "rgba(255, 255, 255, 0.06)"
parent-card-border: "rgba(255, 255, 255, 0.1)"
parent-text-primary: "#ffffff"
parent-text-muted: "#aab0c6"

# 成功同心圆几何色彩
parent-circle-core: "#ff4757"     # 核心价值观 (诚信) - 脉冲红
parent-circle-attitude: "#ffa502" # 态度环 - 琥珀橙
parent-circle-behavior: "#2ed573" # 行为环 - 翡翠绿

# 状态与交互色彩
parent-state-glow: "#ffd200"      # 高亮金光
parent-state-success: "#2ed573"
parent-state-error: "#ff4757"
```

---

## 3. Typography (字体与字阶)

```yaml
# 字体族
font-sans: '"PingFang SC", "Microsoft YaHei", sans-serif'
font-kids: '"PingFang SC", "Microsoft YaHei", "KaiTi", sans-serif' # 融入楷体

# 字号 Scale
text-xs: "0.75rem"   # 12px 辅助文字
text-sm: "0.875rem"  # 14px 次要文字
text-base: "1.0rem"  # 16px 默认正文
text-lg: "1.125rem"  # 18px 小标题/卡片名
text-xl: "1.25rem"   # 20px 章节名称
text-2xl: "1.5rem"   # 24px 大标题
text-3xl: "2.0rem"   # 32px 儿童大标题
text-4xl: "3.0rem"   # 48px 封面魔法字

# 字重
weight-normal: "400"
weight-medium: "500"
weight-bold: "700"
```

---

## 4. Spacing Scale (间距比例)

我们采用 4 像素为基准的紧凑间距系统，适配单网页大信息密度与平板操作：

```yaml
space-zero: "0px"
space-xs: "4px"
space-sm: "8px"
space-md: "16px"
space-lg: "24px"
space-xl: "32px"
space-2xl: "48px"
space-3xl: "64px"
space-flex: "auto"
```

---

## 5. Layout & Roundness (布局与圆角)

```yaml
# 视口尺寸
viewport-tablet: "100%"       # 平板全宽
viewport-max-width: "1100px"  # 桌面对齐最大宽
viewport-kids-max-width: "800px" # 绘本模式舒适屏宽

# 圆角标记 (Border Radius)
radius-none: "0px"
radius-sm: "8px"    # 次要元素
radius-md: "16px"   # 标准卡片
radius-lg: "24px"   # 绘本气泡/大框
radius-full: "9999px" # 徽章/表情圆/圆心

# 阴影与特效
shadow-kids: "0 8px 24px rgba(140, 122, 107, 0.12)" # 柔和温润的浅褐色阴影
shadow-parent: "0 8px 32px 0 rgba(31, 38, 135, 0.37)" # 玻璃拟态深色阴影
backdrop-parent: "blur(12.5px)" # 玻璃材质模糊
```

---

## 6. Shared Animations (共享微动画)

```yaml
# 过渡时间
transition-fast: "0.15s ease"
transition-base: "0.3s ease"
transition-slow: "0.5s cubic-bezier(0.25, 0.8, 0.25, 1)"

# 动态特效
bounce-animation: "bounce 2s infinite" # 向下指示箭头轻微跳跃
glow-pulse: "pulse 3s infinite"       # 魔法瓶与徽章缓慢呼吸呼吸
shake-error: "shake 0.4s ease"        # 密码错或答错时震动
```
