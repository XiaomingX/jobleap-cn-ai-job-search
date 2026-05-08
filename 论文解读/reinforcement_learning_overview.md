# 深度强化学习PyTorch实现仓库说明
以下是原文的中文翻译，已优化表述逻辑与术语准确性，更符合中文技术文档阅读习惯。


## 项目状态
**状态**：活跃中（目前处于积极开发阶段，可能会出现破坏性更新）

本仓库将实现经典及前沿的深度强化学习算法。其核心目标是提供清晰的PyTorch代码，帮助开发者学习深度强化学习算法的原理与实现。

未来计划：
- 持续新增更多前沿算法
- 维护并优化现有代码


## 依赖环境
需提前安装以下工具及对应版本：
- Python 版本 ≤ 3.6
- tensorboardX（用于可视化训练过程）
- gym 版本 ≥ 0.10（强化学习环境库）
- PyTorch 版本 ≥ 0.4（深度学习框架）

**注意**：TensorFlow 不支持 Python 3.7 版本，需匹配兼容的 Python 版本。


## 安装步骤
1. 优先通过依赖文件批量安装（推荐）：
```bash
pip install -r requirements.txt
```

2. 若上述命令执行失败，可按以下步骤单独安装依赖：
   - 安装 gym 环境库：
   ```bash
   pip install gym
   ```

   - 安装 PyTorch 框架：
   ```bash
   # 请前往官方网站下载安装：https://pytorch.org/
   # 推荐使用 Anaconda 虚拟环境管理依赖包，避免版本冲突
   ```

   - 安装 tensorboardX（含TensorFlow依赖）：
   ```bash
   pip install tensorboardX
   pip install tensorflow==1.12
   ```

3. 安装验证（测试是否成功）：
```bash
# 进入 TD3 算法的示例目录（以Char10文件夹为例）
cd Char10\ TD3/
# 运行测试脚本，验证环境是否正常
python TD3_BipedalWalker-v2.py --mode test
```
若安装成功，将自动弹出“双足步行者（BipedalWalker）”的仿真窗口。

双足步行者（BipedalWalker）仿真效果：  
![](https://github.com/sweetice/Deep-reinforcement-learning-with-pytorch/blob/master/figures/test.png)

4. 可选：安装 OpenAI Baselines（强化学习基准算法库）
```bash
# 克隆 OpenAI Baselines 仓库到本地
git clone https://github.com/openai/baselines.git
# 进入仓库目录
cd baselines
# 以可编辑模式安装（方便后续修改源码）
pip install -e .
```


## DQN（深度Q网络）
本仓库已上传两个DQN模型，分别用于训练以下两个经典环境：
- CartPole-v0（倒立摆环境）
- MountainCar-v0（山地车环境）

### MountainCar-v0 训练提示
该环境属于**稀疏二元奖励任务**：只有当小车到达山顶时，才会获得非零奖励；未到达时无奖励。  
- 若使用随机策略，通常需要约 10万步（1e5 steps）才能完成训练。  
- 优化方案1：新增奖励项（例如，让奖励与小车当前位置正相关，激励小车向山顶移动）。  
- 优化方案2：采用更进阶的逆强化学习（Inverse Reinforcement Learning）方法。

DQN训练过程可视化：  
![价值损失曲线](https://github.com/sweetice/Deep-reinforcement-learning-with-pytorch/blob/master/Char01%20DQN/DQN/pic/value_loss.jpg)   
![训练步数曲线](https://github.com/sweetice/Deep-reinforcement-learning-with-pytorch/blob/master/Char01%20DQN/DQN/pic/finish_episode.jpg)  

**曲线说明**：  
上图为DQN的价值损失（value loss）曲线，可见损失值最高升至 1e13，但网络仍能正常工作。原因如下：
1. 训练过程中，目标网络（target_net）与行为网络（act_net）的参数差异逐渐增大，导致计算出的损失值累积变大。
2. 前期损失值较小，是因为任务奖励稀疏，两个网络的参数更新幅度较小。

### DQN相关论文（附代码链接）
1. 《Playing Atari with Deep Reinforcement Learning》（基于深度强化学习玩雅达利游戏）[[arxiv链接]](https://www.cs.toronto.edu/~vmnih/docs/dqn.pdf) [[代码链接]](https://github.com/higgsfield/RL-Adventure/blob/master/1.dqn.ipynb)
2. 《Deep Reinforcement Learning with Double Q-learning》（双Q学习深度强化学习）[[arxiv链接]](https://arxiv.org/abs/1509.06461) [[代码链接]](https://github.com/higgsfield/RL-Adventure/blob/master/2.double%20dqn.ipynb)
3. 《Dueling Network Architectures for Deep Reinforcement Learning》（决斗网络架构的深度强化学习）[[arxiv链接]](https://arxiv.org/abs/1511.06581) [[代码链接]](https://github.com/higgsfield/RL-Adventure/blob/master/3.dueling%20dqn.ipynb)
4. 《Prioritized Experience Replay》（优先经验回放）[[arxiv链接]](https://arxiv.org/abs/1511.05952) [[代码链接]](https://github.com/higgsfield/RL-Adventure/blob/master/4.prioritized%20dqn.ipynb)
5. 《Noisy Networks for Exploration》（用于探索的噪声网络）[[arxiv链接]](https://arxiv.org/abs/1706.10295) [[代码链接]](https://github.com/higgsfield/RL-Adventure/blob/master/5.noisy%20dqn.ipynb)
6. 《A Distributional Perspective on Reinforcement Learning》（强化学习的分布视角）[[arxiv链接]](https://arxiv.org/pdf/1707.06887.pdf) [[代码链接]](https://github.com/higgsfield/RL-Adventure/blob/master/6.categorical%20dqn.ipynb)
7. 《Rainbow: Combining Improvements in Deep Reinforcement Learning》（Rainbow：融合深度强化学习的多种改进方法）[[arxiv链接]](https://arxiv.org/abs/1710.02298) [[代码链接]](https://github.com/higgsfield/RL-Adventure/blob/master/7.rainbow%20dqn.ipynb)
8. 《Distributional Reinforcement Learning with Quantile Regression》（基于分位数回归的分布强化学习）[[arxiv链接]](https://arxiv.org/pdf/1710.10044.pdf) [[代码链接]](https://github.com/higgsfield/RL-Adventure/blob/master/8.quantile%20regression%20dqn.ipynb)
9. 《Hierarchical Deep Reinforcement Learning: Integrating Temporal Abstraction and Intrinsic Motivation》（分层深度强化学习：融合时间抽象与内在动机）[[arxiv链接]](https://arxiv.org/abs/1604.06057) [[代码链接]](https://github.com/higgsfield/RL-Adventure/blob/master/9.hierarchical%20dqn.ipynb)
10. 《Neural Episodic Control》（神经情景控制）[[arxiv链接]](https://arxiv.org/pdf/1703.01988.pdf) [[代码链接]](#)


## Policy Gradient（策略梯度）
### 运行命令
1. 加载已训练好的模型：
```bash
python Run_Model.py
```

2. 重新训练模型（以MountainCar-v0环境为例）：
```bash
python pytorch_MountainCar-v0.py
```

### 模型文件说明
- `policyNet.pkl`：本仓库提供的已训练完成的策略网络模型文件，可直接用于测试。


## Actor-Critic（演员-评论家）
这是一种强化学习算法框架，经典的REINFORCE算法也包含在该框架下。


## DDPG（深度确定性策略梯度）
### 训练效果
在Pendulum-v0（钟摆环境）中的回合奖励（Episode Reward）曲线：  
![Pendulum-v0回合奖励](https://github.com/sweetice/Deep-reinforcement-learning-with-pytorch/blob/master/Char05%20DDPG/DDPG_exp.jpg)  


## PPO（近端策略优化）
- 原始论文：https://arxiv.org/abs/1707.06347  
- OpenAI Baselines 官方博客解读：https://blog.openai.com/openai-baselines-ppo/  


## A2C（优势演员-评论家）
A2C 全称为“优势策略梯度（Advantage Policy Gradient）”。  
2017年的一篇论文指出，A2C 与 A3C（异步优势演员-评论家）的性能差异并不显著。  

A3C 算法自论文发表以来影响深远，其核心思想包括：
1. 基于固定长度的经验片段（如20个时间步）进行更新，用这些片段估计回报（returns）和优势函数（advantage function）。
2. 策略网络与价值网络共享部分网络层，减少参数冗余。
3. 采用异步更新方式，提高训练效率。


## A3C（异步优势演员-评论家）
- 原始论文：https://arxiv.org/abs/1602.01783  


## SAC（软演员-评论家）
**说明**：本仓库的SAC实现并非论文作者官方实现。

### 训练效果
在Pendulum-v0（钟摆环境）中的回合奖励（Episode Reward）曲线：  
![SAC Pendulum-v0回合奖励](https://github.com/sweetice/Deep-reinforcement-learning-with-pytorch/blob/master/Char09%20SAC/SAC_ep_r_curve.png)  


## TD3（双延迟深度确定性策略梯度）
**说明**：本仓库的TD3实现并非论文作者官方实现。

### 训练效果
1. 在Pendulum-v0（钟摆环境）中的回合奖励曲线：  
![TD3 Pendulum-v0回合奖励](https://github.com/sweetice/Deep-reinforcement-learning-with-pytorch/blob/master/Char10%20TD3/TD3_Pendulum-v0.png)  

2. 在BipedalWalker-v2（双足步行者环境）中的回合奖励曲线：  
![TD3 BipedalWalker-v2回合奖励](https://github.com/sweetice/Deep-reinforcement-learning-with-pytorch/blob/master/Char10%20TD3/Episode_reward_TD3_BipedakWalker.png)  

### 模型测试命令
若需测试已训练的TD3模型，执行以下命令：
```bash
python TD3_BipedalWalker-v2.py --mode test
```


## 深度强化学习相关论文
[01] 《A Brief Survey of Deep Reinforcement Learning》（深度强化学习简要综述）[[arxiv链接]](https://arxiv.org/abs/1708.05866)  
[02] 《The Beta Policy for Continuous Control Reinforcement Learning》（连续控制强化学习的Beta策略）[[链接]](https://www.ri.cmu.edu/wp-content/uploads/2017/06/thesis-Chou.pdf)  
[03] 《Playing Atari with Deep Reinforcement Learning》（基于深度强化学习玩雅达利游戏）[[arxiv链接]](https://www.cs.toronto.edu/~vmnih/docs/dqn.pdf)  
[04] 《Deep Reinforcement Learning with Double Q-learning》（双Q学习深度强化学习）[[arxiv链接]](https://arxiv.org/abs/1509.06461)  
[05] 《Dueling Network Architectures for Deep Reinforcement Learning》（决斗网络架构的深度强化学习）[[arxiv链接]](https://arxiv.org/abs/1511.06581)  
[06] 《Continuous control with deep reinforcement learning》（基于深度强化学习的连续控制）[[arxiv链接]](https://arxiv.org/abs/1509.02971)  
[07] 《Continuous Deep Q-Learning with Model-based Acceleration》（结合模型加速的连续深度Q学习）[[arxiv链接]](https://arxiv.org/abs/1603.00748)  
[08] 《Asynchronous Methods for Deep Reinforcement Learning》（深度强化学习的异步方法）[[arxiv链接]](https://arxiv.org/abs/1602.01783)  
[09] 《Trust Region Policy Optimization》（信任区域策略优化）[[arxiv链接]](https://arxiv.org/abs/1502.05477)  
[10] 《Proximal Policy Optimization Algorithms》（近端策略优化算法）[[arxiv链接]](https://arxiv.org/abs/1707.06347)  
[11] 《Scalable trust-region method for deep reinforcement learning using Kronecker-factored approximation》（基于克罗内克分解近似的可扩展信任区域深度强化学习方法）[[arxiv链接]](https://arxiv.org/abs/1708.05144)  
[12] 《High-Dimensional Continuous Control Using Generalized Advantage Estimation》（基于广义优势估计的高维连续控制）[[arxiv链接]](https://arxiv.org/abs/1506.02438)  
[13] 《Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor》（软演员-评论家：基于随机演员的离策略最大熵深度强化学习）[[arxiv链接]](https://arxiv.org/abs/1801.01290)  
[14] 《Addressing Function Approximation Error in Actor-Critic Methods》（解决演员-评论家方法中的函数近似误差）[[arxiv链接]](https://arxiv.org/abs/1802.09477)  


## 待办事项（TO DO）
- [x] 完成 DDPG 算法实现  
- [x] 完成 SAC 算法实现  
- [x] 完成 TD3 算法实现  


## 推荐RL学习课程
- [OpenAI Spinning Up](https://spinningup.openai.com/)（OpenAI官方强化学习入门教程，含代码实践）  
- [David Silver 强化学习课程](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html)（经典课程，偏理论推导）  
- [伯克利深度强化学习课程](http://rll.berkeley.edu/deeprlcourse/)（理论与实践结合，含项目案例）  
- [Practical RL](https://github.com/yandexdataschool/Practical_RL)（侧重实践的RL课程，含大量代码）  
- [李宏毅深度强化学习课程](https://www.youtube.com/playlist?list=PLJV_el3uVTsODxQFgzMzPLa16h6B8kWM_)（中文讲解，适合入门）  


为了方便你后续使用这个仓库，要不要我帮你整理一份**《仓库核心算法速查表》** ？表格会包含算法名称、适用场景、关键命令和论文链接，让你能快速定位所需内容。