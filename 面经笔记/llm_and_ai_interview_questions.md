# 大语言模型 (LLM) 面试真题与深度解析

本文汇总了国内 24 家大厂及独角兽公司的面试经验，并提炼了高频考点。

## 一、24 家大模型面试战报摘要

- **智元机器人 (Agibot)**：稚晖君亲面，侧重 Transformer 基础与具身智能。
- **月之暗面 (Moonshot)**：技术深度极高。考点包括分布式训练切分、设备间通信（Ring-reduce 原理）、CUDA 底层。
- **蚂蚁集团**：强调“研工不分家”，侧重模型研究与工程落地。
- **百度文心**：分工极细（数据、模型、框架）。考点侧重 Transformer 训练、Loss Spike 处理。
- **阿里达摩院**：关注技术愿景与多模态预训练，算力资源充足。
- **Minimax / 百川智能**：侧重 LeetCode 算法基础与大模型训练参数规模。

## 二、高频考点排行榜

1. **自注意力机制 (MHA)**：复杂度计算、KV-Cache、MQA/GQA 优化、手写实现。
2. **归一化 (Norm)**：RMSNorm 与 LayerNorm 的区别，手写代码。
3. **分布式训练**：数据并行 (DP/DDP)、模型并行 (TP/PP)、ZeRO 优化器原理。
4. **大模型训练技巧**：如何处理训练不稳定性 (Loss Spike)、激活函数选择 (SwiGLU)。
5. **位置编码**：RoPE (旋转位置编码) 的数学原理与外推性。
6. **对齐技术**：SFT、RLHF (PPO/DPO) 的原理与实操细节。

## 三、DeepSeek 免费使用渠道推荐

- **官方 Web/APP**：性能最强。
- **云厂商 API**：如腾讯云、阿里云、百度云提供的 DeepSeek 满血版。
- **本地部署**：利用 Ollama + DeepSeek-R1-Distill-Qwen 系列模型。
- **AI 搜索集成**：如秘塔搜索、Perplexity 等。

---

> 掌握 AIGC 前沿面试动态，访问 [jobleap.cn](https://www.jobleap.cn)
