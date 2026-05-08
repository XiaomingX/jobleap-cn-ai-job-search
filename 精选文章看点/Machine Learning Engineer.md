# 2025-2026 大模型算法工程师 (Machine Learning Engineer) 面试真题

本题库聚焦于大模型落地全链路，从预训练、微调到 RAG 与 Agent。去掉基础机器学习，直击当前行业最前沿。

## 一、 大模型对齐与微调 (Alignment & Fine-tuning)
1. **RLHF 深度机制**：详细阐述 PPO 与 DPO 的数学本质差异。在什么场景下你会优先选择 DPO 而不是传统的 RLHF？
2. **PEFT 进阶**：LoRA 的秩 (Rank) 大小对模型泛化能力的影响。如何评价 DoRA (Weight-Decomposition Low-Rank Adaptation) 的性能提升？
3. **指令遵循与样本平衡**：如何构建高质量的 SFT (Supervised Fine-Tuning) 数据集？在多任务微调（MFT）中如何平衡不同任务的分布？

## 二、 长文本与外部知识增强 (Long-Context & RAG)
4. **RAG 系统演进**：从简单的向量检索到 Agentic RAG。如何处理多模态 RAG 中的跨模态特征融合？
5. **检索评估 (Advanced Retrieval)**：如何解决 RAG 中的“幻觉”问题？Self-RAG 与 Corrective RAG (CRAG) 的核心思想。
6. **长文本架构升级**：对比不同位置编码 (RoPE, ALiBi) 在外推性上的表现。如何实现无限长度的 Cache 管理？

## 三、 推理优化与量化 (Inference & Quantization)
7. **量化前沿**：AWQ, GPTQ 与 FP8 量化的差异。在大规模部署时，如何解决 W4A8 (Weight int4, Activation int8) 的量化误差？
8. **推理加速技术**：投机采样 (Speculative Decoding) 在生产环境中的实际收益及适用场景。
9. **KV Cache 显存优化**：PagedAttention 的原理及其对吞吐量的实际提升。

## 四、 评价与幻觉治理 (Evaluation & Hallucination)
10. **评价体系去偏**：目前 MMLU/HumanEval 刷榜现象严重，作为 MLE 你如何设计内部的评估基准 (internal benchmark)？
11. **幻觉检测机制**：如何在推理实时阶段捕捉并修正幻觉？

## 五、 多模态与 Agent (Multimodal & Agent)
12. **多模态路径**：对比 Flamingo 式的 Cross-Attention 注入与 LLaVA 式的 Projection Layer 方案。
13. **Agent 智能体设计**：ReAct 框架如何处理工具调用 (Tool-use) 中的循环依赖或逻辑死锁？