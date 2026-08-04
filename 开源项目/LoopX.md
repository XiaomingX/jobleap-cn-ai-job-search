# LoopX 架构说明

> 本文档帮助你理解 LoopX 是什么、怎么工作的、为什么要这样设计。

## 一句话理解 LoopX

**LoopX 是 AI Agent 的"任务管理器"**——它不干活，但它知道谁在干什么、干到哪了、什么时候该停下来等人类决策。

---

## 架构分层（可视化）

```
┌─────────────────────────────────────────────────────────────┐
│                    用户交互层 (Presentation)                  │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │   CLI    │  │Dashboard │  │ Frontstage│  │Lark/Feishu│  │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    Agent 集成层 (Integration)                │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │Codex App │  │Claude Code│  │  Cursor  │  │  Shell   │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    控制平面层 (Control Plane)                │
│  ┌──────────────────────────────────────────────────────┐  │
│  │                  LoopX Kernel                        │  │
│  │  ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐       │  │
│  │  │ Goal   │ │  Todo  │ │  Gate  │ │ Quota  │       │  │
│  │  │ State  │ │Manager │ │Manager │ │Manager │       │  │
│  │  └────────┘ └────────┘ └────────┘ └────────┘       │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    能力层 (Capabilities)                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │Issue-Fix │  │ContentOps│  │ Explore  │  │Benchmark │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    存储层 (Storage)                          │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │Registry  │  │Run History│  │ Evidence │  │  Quota   │   │
│  │  JSON    │  │  JSON/MD  │  │  Files   │  │  State   │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
└─────────────────────────────────────────────────────────────┘
```

### 每层干什么

| 层 | 职责 | 举例 |
|---|------|------|
| **用户交互层** | 给人看的界面 | `loopx status`、Dashboard、飞书看板 |
| **Agent 集成层** | 和各种 AI Agent 对接 | Codex、Claude Code、Cursor |
| **控制平面层** | 核心状态管理 | 目标状态、任务分配、门禁、配额 |
| **能力层** | 具体业务能力 | 修 Bug、内容运营、探索实验 |
| **存储层** | 持久化数据 | 注册表、运行历史、证据、配额 |

---

## 核心概念

### 1. 目标（Goal）

**什么是目标？**
- 长期运行的工作单元
- 可以跨多个会话、多个 Agent 持续存在
- 例如："修复 OpenViking 项目的所有 P0 Bug"

**目标包含什么？**
- `objective`: 要做什么
- `scope`: 范围边界
- `authority`: 谁有权改
- `state`: 当前状态
- `quota`: 计算配额

### 2. 任务（Todo）

**什么是任务？**
- 目标下的具体工作项
- 有明确的所有者和状态
- 例如："修复 issue #123"

**任务状态流转**
```
pending → claimed → in_progress → completed
                ↘ blocked → pending (重新排队)
```

### 3. 门禁（Gate）

**什么是门禁？**
- 需要人类判断的决策点
- Agent 必须停下来等人类批准
- 例如："这个设计可以吗？"、"要发布吗？"

**为什么需要门禁？**
- 防止 AI 自作主张
- 保留人类控制权
- 符合安全规范

### 4. 配额（Quota）

**什么是配额？**
- 限制 Agent 自动执行的资源预算
- 防止 AI 无限制运行
- 例如：每天最多自动执行 12 小时

**配额状态**
- `eligible`: 可以执行
- `throttled`: 已用完，等待重置
- `paused`: 暂停
- `operator_gate`: 等待人类决策

---

## 四角色责任模型

```
Agent → Capability → Provider → 外部系统
   ↑
   └── Kernel（LoopX 核心）
```

| 角色 | 负责什么 | 不负责什么 |
|------|----------|------------|
| **Agent** | 规划、分析、工具使用、执行一次有界任务 | 持久化状态、权限控制 |
| **Capability** | 定义调用者结果、验证输出、提出状态转换 | 持久化调度、门禁管理 |
| **Provider** | 调用外部系统、返回观察结果 | 域转换策略、LoopX 状态管理 |
| **Kernel** | 管理目标、任务、门禁、配额、恢复、调度 | 具体业务逻辑、Provider 实现 |

---

## 依赖的三方组件

| 组件 | 用途 | 必需/可选 |
|------|------|----------|
| Python 3.11+ | 运行环境 | 必需 |
| curl | HTTP 请求 | 必需 |
| tar | 文件解压 | 必需 |
| git | 版本控制（仅贡献者） | 可选 |
| tmux | 多 Agent 并行 | 可选 |

**零依赖设计**: LoopX 核心包不依赖任何第三方 Python 库

---

## 提示词工程说明

LoopX 使用提示词（Prompt）来引导 Agent 行为：

### 1. 心跳提示词（Heartbeat Prompt）

**用途**: 定时唤醒 Agent，检查是否需要执行任务

**格式**: 结构化 JSON，包含 quota、todo、gate 信息

**生成命令**:
```bash
loopx heartbeat-prompt --goal-id <goal-id>
```

**示例输出**:
```json
{
  "goal_id": "project-abc",
  "quota": {"compute": 0.5, "state": "eligible"},
  "todos": {"open_count": 3, "next": "修复登录 bug"},
  "gate": null
}
```

### 2. 目标模式提示词（Goal Mode Prompt）

**用途**: Claude Code 集成，将目标状态注入会话

**格式**: Markdown + YAML frontmatter

**位置**: `loopx/claude_goal_mode/`

### 3. 技能提示词（Skill Prompt）

**用途**: 预定义的工作流模板

**格式**: Markdown + 代码示例

**位置**: `skills/`

---

## 核心能力常用方法入口

```python
# 目标管理
from loopx.status import get_goal_state, refresh_goal_state
from loopx.state_refresh import refresh_state

# 任务管理
from loopx.todos import claim_todo, update_todo, list_todos

# 配额管理
from loopx.quota import should_run, spend_slot

# 证据管理
from loopx.history import append_run, list_runs
from loopx.review_packet import build_review_packet

# Agent 集成
from loopx.worker_bridge import run_worker_bridge
from loopx.heartbeat_prompt import build_heartbeat_prompt
```

---

## 常用函数和使用用例

### 用例 1: 连接到 LoopX

```bash
# 初始化项目
loopx connect

# 检查连接状态
loopx doctor

# 查看当前状态
loopx status
```

### 用例 2: 执行一次 Agent 循环

```bash
# 1. 检查是否应该运行
loopx quota should-run --goal-id <goal-id>

# 2. 领取任务
loopx todo claim --goal-id <goal-id>

# 3. 执行任务（Agent 完成工作）

# 4. 更新任务状态
loopx todo update --goal-id <goal-id> --todo-id <todo-id> --status completed

# 5. 刷新状态
loopx refresh-state --goal-id <goal-id>

# 6. 消耗配额
loopx quota spend-slot --goal-id <goal-id>
```

### 用例 3: 启动心跳自动化

```bash
# 生成心跳提示词
loopx heartbeat-prompt --goal-id <goal-id>

# 在 Agent 会话中使用生成的提示词
```

### 用例 4: 查看运行历史

```bash
# 查看最近的运行记录
loopx history --goal-id <goal-id> --limit 10

# 查看特定运行的详情
loopx history --goal-id <goal-id> --run-id <run-id>
```

---

## 数据存储结构

```
.loopx/
├── registry.json          # 目标注册表
├── goals/
│   └── <goal-id>/
│       ├── ACTIVE_GOAL_STATE.md  # 当前目标状态
│       ├── run_history/          # 运行历史
│       └── quota/                # 配额状态
└── global_registry.json   # 全局注册表（多项目时）
```

---

## 设计原则

### 1. 本地优先（Local First）

- 所有状态存储在本地
- 不上传到任何服务器
- 保护用户隐私

### 2. Agent 无关（Agent-Agnostic）

- 不绑定特定 AI Agent
- 支持 Codex、Claude Code、Cursor 等
- 可扩展到新的 Agent

### 3. 人类控制（Human-in-the-Loop）

- 危险操作需要人类批准
- 门禁机制确保安全
- AI 不能自作主张

### 4. 零依赖（Zero Dependencies）

- 核心包不依赖第三方库
- 减少安全风险
- 简化安装部署

---

## 常见问题

### Q: LoopX 会自动执行任务吗？

A: 不会。LoopX 只是控制平面，实际执行由 Agent（如 Codex、Claude）完成。

### Q: 如何停止自动执行？

A: 使用 `loopx quota suspend --goal-id <goal-id>` 暂停配额。

### Q: 数据存储在哪里？

A: 本地 `.loopx/` 目录，不会上传到任何服务器。

### Q: 支持哪些 AI Agent？

A: 支持 Codex App、Codex CLI、Claude Code、Cursor、Shell 等。

### Q: 如何扩展新的 Agent？

A: 实现 `Provider` 接口，参考 `loopx/worker_bridge.py`。

---
