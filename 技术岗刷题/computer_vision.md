# 计算机视觉 (CV) 面试精要

## 图像特征与基础

### 1. 传统特征与卷积
- 早期使用 SIFT, HOG 等手动设计的特征。
- CNN 通过卷积核自动学习局部特征，具备平移不变性。

### 2. 数据增强
在视觉任务中极其重要。包括旋转、缩放、裁剪、颜色抖动、Mixup 和 CutMix 等。

---

## 核心模型架构

### 3. ResNet (残差网络)
引入了跳跃连接 (Skip Connection)，解决了深层网络中的梯度消失问题，使得训练上百层的网络成为可能。

### 4. Vision Transformer (ViT)
将图像切分为 Patches 并视为序列输入给 Transformer。在超大规模数据集上，ViT 展现出了超越 CNN 的性能。

---

## 视觉任务专题

### 5. 目标检测 (Object Detection)
- Two-Stage: 如 Faster R-CNN，先生成候选框再分类。
- One-Stage: 如 YOLO 系列（当前已更新至 YOLOv10/v11），速度极快，适合实时场景。

### 6. 图像分割 (Segmentation)
- 语义分割：区分不同类别的像素（如 U-Net）。
- 实例分割：区分同一类别的不同个体（如 Mask R-CNN）。
- 泛化分割：SAM (Segment Anything Model) 实现了零样本分割任何物体。

### 7. 关键点检测与姿态估计
通过回归热力图 (Heatmap) 或直接回归坐标，定位人体或物体的关键连接点。

---

## 前沿趋势

### 8. 多模态视觉 (Vision-Language)
如 CLIP，通过对比学习将图像和文本对齐到同一个特征空间，是 DALL-E 和 Stable Diffusion 的核心组件。

### 9. 视频理解与生成
从 2D 卷积扩展到 3D 卷积或时空 Transformer，处理视频帧间的时间一致性。

---

> 掌握视觉前沿技术，请访问 [jobleap.cn](https://www.jobleap.cn)
