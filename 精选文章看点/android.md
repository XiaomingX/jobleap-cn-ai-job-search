# Android 简历自救：大厂现在到底要什么？

## Android 凉了？
Google 每年都在推新技术（Kotlin, Jetpack, Compose），但很多同学的简历还停留在 5 年前：Java + MVC + ListView。
这种简历，在这个“寒冬”里基本是炮灰。
大厂校招现在看重什么？**Kotlin 协程**、**Jetpack 全家桶**、**Flutter/KMP 跨端**、**性能优化**。

## 💡 学长/学姐的修改建议
### 1. 拥抱 Kotlin，抛弃 Java
如果你的项目全是用 Java 写的，那是很大的减分项。
❌ **Before：**
“熟练使用 Java 开发 Android 应用。”

✅ **After：**
“基于 Kotlin + Jetpack (Lifecycle, ViewModel, LiveData) 重构老旧项目，使用 Coroutines 替代 Thread/AsyncTask 处理异步任务。”

### 2. 性能优化是重中之重
启动速度、卡顿优化、内存泄漏检测……这些是必考题。
不要只写“优化了性能”，要写怎么优化的，效果多少。

> **🚀 JobLeap 助攻**：
> 不知道怎么衡量优化的指标？去 [**JobLeap**](https://www.jobleap.cn) 搜一下大厂的面经，看看他们都关注哪些性能指标（如 FPS, StartTime, Memory usage）。

---

## 📄 Android 程序员简历模板（参考版）

### 个人信息
*   **姓名：** 胶布帝
*   **求职意向：** Android 开发工程师
*   **电话：** 138xxxxxxx
*   **邮箱：** jobleap@example.com

### 🛠 技能清单
*   **语言 & 框架：** 精通 Kotlin，熟练掌握 Jetpack 组件（Room, Hilt, Navigation）。
*   **UI 开发：** 熟悉 Compose 声明式 UI 开发，了解 View 绘制原理及自定义 View。
*   **异步编程：** 熟练使用 Kotlin Coroutines / Flow 处理复杂的并发场景。
*   **性能优化：** 熟悉 Profiler, Systrace 工具，有启动优化和内存治理经验。

---

### 💻 项目经历

#### 🚀 **极致体验的新闻客户端**
**项目描述：**
基于 MVVM 架构开发的资讯类 APP，集成 Jetpack 组件库。

**我的贡献（STAR）：**
*   **Situation：** 应用冷启动时间过长（2s+），且列表滑动存在卡顿。
*   **Task：** 优化启动流程，提升列表流畅度。
*   **Action：**
    *   利用 **App Startup** 库优化初始化任务，通过 **IdleHandler** 延迟加载非核心组件。
    *   使用 **RecyclerView** 的 Prefetch 机制和 DiffUtil 优化列表刷新。
    *   通过 **LeakCanary** 检测并在开发期修复了 5 处内存泄漏。
*   **Result：** 冷启动时间降低至 **800ms**，列表滑动 FPS 稳定在 60 帧。

#### 🌐 **Kotlin Multiplatform 跨端模块**
**项目描述：**
探索 KMP (Kotlin Multiplatform) 技术，实现网络层和数据层的逻辑复用。

**我的贡献：**
*   基于 Ktor + SQLDelight 编写通用的网络和数据库模块，复用于 Android 和 iOS 端。
*   使得双端业务逻辑代码复用率达到 70%。

---

### 🏆 实习经历
**某手机厂商 · Android 系统开发实习生**（2024.06 - 2024.09）
*   参与 Framework 层 AMS (ActivityManagerService) 的源码分析与定制。
*   编写了自动化测试脚本，提升了 ROM 发版测试效率。

---

> **写在最后：**
> 移动端虽然卷，但只要技术栈够新、基础够扎实，依然有大把机会。
> 尤其是跨端技术和Framework层原理，是通往大厂的捷径。来 [**jobleap.cn**](https://www.jobleap.cn) 看看更多高薪职位的 JD 吧。
