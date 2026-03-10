# 2025-2026 大模型分布式训练工程师面试真题 (资深版)

作为资深大模型类别面试官，我更看重候选人对超大规模计算集群下，算力、存储、通讯三者平衡的深度理解。以下是更新后的面试考点：

## 一、 核心架构与并行策略 (Core Architecture & Parallelism)
1. **3D 并行深度解析**：请详细阐述张量并行 (TP)、流水线并行 (PP) 与数据并行 (DP) 的耦合机制。在万亿参数模型中，如何确定最佳的并行比例？
2. **ZeRO 系列优化**：对比 ZeRO-1, ZeRO-2, ZeRO-3 的技术演进。ZeRO-Offload 在带宽受限场景下的性能损失如何量化？
3. **混合专家模型 (MoE) 训练**：在分布式环境下如何处理 MoE 的专家不平衡问题？EP (Expert Parallelism) 如何与 TP/PP 协同？
4. **流水线调度算法**：对比 1F1B 与 Interleaved 1F1B 调度的气泡率 (Bubble Rate) 计算及收益。

## 二、 硬件加速与内核优化 (Hardware & Kernel Optimization)
5. **FlashAttention 演进**：详细说明 FlashAttention-3 相对于 V2 在异步执行 (Asynchronous execution) 和硬件加速 (WGMMA) 上的改进。
6. **H100/v100 架构适配**：如何利用 Transformer Engine (FP8) 进行高效训练？FP8 训练中的精度损失补偿方案有哪些？
7. **算子融合 (Operator Fusion)**：在大模型训练中，哪些算子融合路径最具收益？如何利用 Triton 自定义高性能算子？

## 三、 通讯与系统瓶颈 (Communication & Bottlenecks)
8. **NCCL 通讯原语原理**：详细解释 AllReduce, ReduceScatter 和 AllGather 的数学原理及在不同拓扑结构 (NVLink vs InfiniBand) 下的吞吐表现。
9. **网络拥塞控制**：在万卡集群中，如何应对“多对一”产生的入端口拥塞 (Incast)？RoCEv2 与 InfiniBand 在大规模训练中的平衡点在哪？
10. **重算 (Relocal/Recomputation)**：对比 Selective Activation Recomputation 与全重算的计算/显存权衡。

## 四、 稳定性与弹性训练 (Scale & Reliability)
11. **容错与断点续训**：如何实现无损的弹性伸缩 (Elastic Training)？在大规模故障（如节点宕机）时，目前的 Checkpoint 异步存储方案如何实现分钟级恢复？
12. **显存监控与泄露排查**：如何利用 PyTorch Profiler 或自定义工具实时追踪分布式环境下的 CPU/GPU 内存碎片和泄露？

## 五、 系统实现前沿
13. **长文本训练优化**：针对 1M+ 上下文，如何实现 Ring Attention 或变长序列的负载均衡？
14. **推理引擎与训练一体化**：从算力利用率角度，探讨 Prefill 阶段与 Decoding 阶段在分布式环境下的动态资源调度。