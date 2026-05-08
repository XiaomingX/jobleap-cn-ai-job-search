# Android 开发实战指南

## 核心趋势与能力要求
Android 开发已全面拥抱 Kotlin 与声明式 UI (Compose)。大厂现在更看重候选人对性能治理、现代框架及跨端方案的深度掌握。

### 1. 技术栈建议
- 核心语言：Kotlin (精通协程 Coroutines)。
- UI 框架：Jetpack Compose (声明式 UI), View 体系自定义组件。
- 架构模式：MVVM / MVI。
- 性能优化：启动优化、内存治理、卡顿监测 (Profiler, Systrace)。

### 2. 简历避坑与提升
- 避免陈述：熟练使用 Java 开发 Android 应用。
- 建议陈述：基于 Kotlin + Jetpack 重构核心模块，利用 Coroutines 优化异步任务，使得应用冷启动时间降低 60%。
- 核心词汇：KMP (Kotlin Multiplatform), Hilt (依赖注入), Flow, 内存泄漏治理, APK 瘦身。

---

## 简历模板（核心片段）

### 技能清单
- 语言基础：精通 Kotlin 语言特性，熟练应用协程与 Flow 处理复杂并发逻辑。
- 现代框架：熟练掌握 Jetpack 全家桶 (Room, ViewModel, Hilt, Navigation)。
- UI 方案：熟悉 Compose 布局与状态管理，掌握自定义 View 绘制原理。
- 性能实战：有丰富的启动速度、内存泄漏、卡顿治理经验，精通调试工具。

### 项目经历

#### 极致体验的新闻客户端
- 情况：应用冷启动超过 2s，列表滑动存在明显卡顿。
- 任务：全面优化应用性能，提升用户留存。
- 行动：
    - 利用 App Startup 库优化任务初始化，并采用 IdleHandler 实现非核心组件延迟加载。
    - 使用 RecyclerView 的 Prefetch 机制与 DiffUtil 算法优化长列表渲染性能。
    - 通过 LeakCanary 监测并修复了多处顽固内存泄漏。
- 结果：冷启动降低至 800ms，列表滑动 FPS 稳定在 60 帧。

---

> 更多 Android 技术进阶与大厂面经，请访问 [jobleap.cn](https://www.jobleap.cn)
