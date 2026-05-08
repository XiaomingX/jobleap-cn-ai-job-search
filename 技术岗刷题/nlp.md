# 自然语言处理 (NLP) 面试精要

## 从传统到现代

### 1. 词向量 (Word Embeddings)
从早期的 Word2Vec, GloVe 等静态向量，演进到 BERT, RoBERTa 等上下文相关的动态向量，解决了多义词问题。

### 2. 序列建模的演进
RNN → LSTM/GRU → Transformer。Transformer 凭借并行化能力和全局注意力，取代了递归模型成为 NLP 的绝对主流。

---

## 大语言模型 (LLM) 专题

### 3. 预训练、微调与对齐
- 预训练 (Pre-training)：在海量文本上进行无监督学习（如预测下一个词）。
- 指令微调 (SFT)：在指令对数据上训练，使其具备任务执行能力。
- 对齐 (Alignment)：通过 RLHF 或 DPO，使模型输出符合人类意图。

### 4. 什么是思维链 (Chain of Thought)?
通过在 Prompt 中加入推理步骤，或者要求模型“一步步思考”，显著提升 LLM 处理复杂逻辑、数学和常识推理的能力。

### 5. 解码策略 (Decoding Strategies)
- Greedy Search：每次选概率最高的词，生成的文本可能重复单调。
- Nucleus Sampling (Top-p)：从累积概率超过 p 的集合中采样，平衡了连贯性与多样性。

---

## 核心技术点

### 6. Tokenization (分词)
现代 LLM 多采用 Byte Pair Encoding (BPE) 或 WordPiece。分词器的效率直接影响模型的上下文窗口长度和多语言处理能力。

### 7. 注意力机制变体
- Flash Attention：通过 IO 感知和算子融合，极大提升了 Attention 的计算速度并降低了内存消耗。
- Multi-Query Attention (MQA) / Grouped-Query Attention (GQA)：减少 KV Cache 的显存占用，加速推理。

---

## 应用与实战

### 8. 幻觉问题 (Hallucination)
模型生成看似合理但事实错误的内容。解决方法：RAG (检索增强生成)、外接工具 (Tools/Agents)、增加知识库密度。

### 9. 智能体 (Agents)
利用 LLM 作为“大脑”，配合规划 (Planning)、记忆 (Memory) 和工具调用 (Tool Use) 能力，完成复杂的自动化任务。

### 10. 长文本挑战
如何处理超过 128k 甚至更长的 Context？旋转位置编码 (RoPE) 的外推能力和内存优化是当前的研究热点。

---

> 掌握 NLP 前沿动态，请访问 [jobleap.cn](https://www.jobleap.cn)
