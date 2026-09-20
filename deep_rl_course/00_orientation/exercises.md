---
title: "Stage 0 入门小测验"
sort: 1
permalink: "00_orientation/exercises/"
---

# Stage 0 入门小测验

> **范围**：RL 与监督学习的区别、agent / environment / reward / policy / episode 等核心概念。
> **题量**：10 题（选择 5 题 × 8 分 + 判断 3 题 × 10 分 + 简答 2 题 × 15 分 = 100 分）。
> **用法**：先闭卷作答，再对照文末参考答案；术语口径以
> [`../glossary/glossary.md`](../glossary/glossary.md) 为准。
> **命题依据**：[Spinning Up — Key Concepts in RL](https://spinningup.openai.com/en/latest/spinningup/rl_intro.html)（2026-09-16 核验）。

---

## 一、单项选择（5 题 × 8 分）

**Q1.** 与监督学习相比，下列哪一项**最准确**地描述了强化学习的本质特征？

A. 强化学习不需要任何数据，完全靠随机试错
B. 强化学习没有「正确答案」标签，智能体靠环境给出的**奖励信号**来评价行为好坏，并需在**序列决策**中最大化累积奖励
C. 强化学习一定使用神经网络，因此属于深度学习的一个分支
D. 强化学习的目标是让每一步的奖励尽可能大，与长期结果无关

**Q2.** 关于 agent（智能体）与 environment（环境）的关系，正确的是：

A. 环境只在智能体采取动作时才会改变，不会自行变化
B. 智能体每步观察到一个（可能只是部分的）世界观测，据此选择动作；环境因动作而改变，也可能自行改变
C. 智能体可以随时获取世界的完整状态，因此观测即状态
D. 智能体即环境，二者只是称呼不同

**Q3.** 某机器人的关节角度与角速度被完整记录并交给策略网络。相对该记录而言，正确说法是：

A. 它一定是 observation，因为凡是传感器读数都是观测
B. 它一定是 state；而在「只能看到部分信息」的场景下，提供给策略的才是 observation
C. observation 与 state 无差别，可随意互换使用
D. state 必须由 RGB 像素构成

**Q4.** 「确定性策略」与「随机策略」的符号书写，正确的是：

A. 确定性记为 $a_t \sim \pi(\cdot|s_t)$；随机记为 $a_t = \mu(s_t)$
B. 确定性记为 $a_t = \mu(s_t)$；随机记为 $a_t \sim \pi(\cdot|s_t)$
C. 二者均记为 $\pi(a_t|s_t)$，没有区别
D. 策略必须是确定性的，随机策略不属于 RL 范畴

**Q5.** 关于 reward 与 return，正确的是：

A. reward 是沿轨迹的累积量，return 是单步信号
B. reward 是单步标量信号 $r_t$；return 是沿轨迹的累积量 $R(\tau)$，RL 的目标是最大化**期望回报** $J(\pi)$
C. return 只能定义为 $\sum_{t=0}^{T} r_t$，与折扣因子无关
D. 折扣因子 $\gamma$ 越大表示越不看重未来奖励

## 二、判断并说明理由（3 题 × 10 分）

**Q6.** 「episode 与 trajectory 是两个完全不同的概念，一个指一段交互，一个指状态动作序列。」
判断对错，并说明二者在本课程口径下的关系。

**Q7.** 「引入折扣因子 $\gamma \in (0,1)$ 只是为了工程实现方便，数学上没有必要。」
判断对错，并给出该页给出的「数学上的理由」。

**Q8.** 「MDP 中的状态转移可以依赖此前全部历史信息。」
判断对错，并说明 MDP 名称中「马尔可夫」的含义。

## 三、简答（2 题 × 15 分）

**Q9.** 请用不超过 60 字给出 action（动作）与 action space（动作空间）的定义，并各举一个**离散**与**连续**动作空间的例子，说明该区分对算法选择的影响。

**Q10.** 写出标准 MDP 的五元组记号，并**逐项**用一句话解释每个元素的含义。

---

# 参考答案

> 评分说明：简答题按「要点」给分，术语准确优先于字数。

## 一、单项选择

**Q1. 答案：B**
关键在「无标签 + 评价性奖励信号 + 序列决策 + 最大化累积奖励」四个要点。A 错在「不需要数据」；
该页的表述是 RL 研究**智能体如何在试错中学习**，即环境交互数据正是其学习来源。C 错在把「深度 RL」等同于 RL 全体：
深度 RL 只是 RL 中以（深层）参数化函数表示策略的分支，RL 本身并不要求神经网络。D 错在只盯单步奖励——目标是最大化**累积**奖励。

**Q2. 答案：B**
该页原文要点：环境是智能体所处并与之交互的世界；每一步智能体看到对世界状态的（可能为部分的）观测，
然后决定动作；**环境会因智能体的动作而改变，也可能自行变化**。A 遗漏了「自行变化」；C 混淆了
fully observed / partially observed；D 无依据。

**Q3. 答案：B**
state 是**对世界状态的完整描述，没有信息被隐藏**；observation 是**对状态的部分描述，可能省略信息**。
关节角度与角速度若构成完整描述即为 state；若智能体只能看到部分信息，则提供给策略的是 observation。
该页特别提示：记法上常把 $s$ 写在技术上应为 $o$ 的位置（因为动作实际以观测为条件）。

**Q4. 答案：B**
该页：策略可确定性，通常记作 $a_t = \mu(s_t)$；也可随机，通常记作 $a_t \sim \pi(\cdot|s_t)$。
A 把两者写反，C/D 无依据。

**Q5. 答案：B**
return 有两种形式：**有限时域无折扣** $R(\tau)=\sum_{t=0}^{T} r_t$ 与**无限时域折扣** $R(\tau)=\sum_{t=0}^{\infty}\gamma^{t} r_t$；
RL 目标是选择使**期望回报**最大的策略。C 漏掉了折扣形式；D 说反了——$\gamma$ 越接近 1 越看重远期奖励。

## 二、判断并说明理由

**Q6. 答案：错。**
该页原文（*You Should Know*）：**Trajectories are also frequently called episodes or rollouts.**
即在本课程口径下二者可互换，均指状态与动作构成的序列 $\tau = (s_0, a_0, s_1, a_1, \dots)$。
细微差别仅在语感：episode 更强调「从初始状态到终止的一段完整交互」，trajectory 更强调数学上那条序列。
**判分**：判「错」得 4 分，能指出「可互换/同义」得 6 分（若额外点出语感差异可加满 10 分）。

**Q7. 答案：错。**
该页给出两点理由：
（1）**直觉上**合理——「现在的钱优于以后的钱」（cash now is better than cash later）；
（2）**数学上**必要——无限时域的奖励和**可能不收敛**到有限值，在方程中难以处理；
而加上折扣因子后，在合理条件下无限和**收敛**。
**判分**：判「错」得 4 分；答出「不收敛 / 便于收敛」得 6 分；额外答出直觉理由可加满。

**Q8. 答案：错。**
该页：MDP 得名于系统满足**马尔可夫性质（Markov property）**——
**转移只依赖最近的状态与动作，而与更早的历史无关**。
「依赖全部历史」说的恰恰是其反面。该页亦给出转移写法 $s_{t+1} \sim P(\cdot|s_t,a_t)$
以及 $P(s'|s,a)$，条件中只出现**当步**的 $s,a$。
**判分**：判「错」得 4 分；准确写出马尔可夫性质得 6 分。

## 三、简答

**Q9. 参考答案要点**

- **action（动作）**：智能体在每一步交互中依据策略选择的行为，记为 $a$ / $a_t$。（4 分）
- **action space（动作空间）**：某环境中**全部合法动作的集合**，记为 $A$。（4 分）
- 例子（4 分）：**离散**——Atari、围棋，可用动作有限；
  **连续**——在物理世界中控制机器人，动作为实值向量。
- 影响（3 分）：该区分对深度 RL 方法有**相当深远**的后果——某些算法族只能直接用于其中一种情形，
  换到另一种则须大幅改写（substantially reworked）。

> 备注：本页记连续动作空间为 $(-\infty,\infty)$ 这样的实值区间；「离散/连续」的对比措辞出自该页 Action Spaces 一节。

**Q10. 参考答案要点**

五元组：$\langle S, A, R, P, \rho_0 \rangle$（写出五元组得 3 分，每项各 2.4 分，合计 15 分）

| 元素 | 含义 |
| --- | --- |
| $S$ | 全部合法**状态**的集合 |
| $A$ | 全部合法**动作**的集合 |
| $R$ | **奖励函数**，$R: S \times A \times S \to \mathbb{R}$，依赖当前状态、刚采取的动作与下一状态 |
| $P$ | **转移概率函数**，$P: S \times A \to \mathcal{P}(S)$；$P(s'\mid s,a)$ 表示从 $s$ 出发采取 $a$ 后转移到 $s'$ 的概率 |
| $\rho_0$ | **初始状态分布**，轨迹首个状态 $s_0 \sim \rho_0(\cdot)$ 由此采样 |

---

## 自测对照表

| 题号 | 考点 | 对应术语表条目 |
| --- | --- | --- |
| Q1 | RL vs 监督学习 | agent, reward, return |
| Q2 | agent / environment 交互循环 | agent, environment |
| Q3 | state vs observation | state, observation |
| Q4 | policy 的两种形式 | policy |
| Q5 | reward vs return, discount | reward, return, discount factor |
| Q6 | episode vs trajectory | episode, trajectory |
| Q7 | discount factor 的作用 | discount factor |
| Q8 | 马尔可夫性质 | MDP |
| Q9 | action / action space | action |
| Q10 | MDP 五元组 | MDP |

**得分参考**：≥ 85 分可进入 Stage 1；70–84 分建议重读术语表；< 70 分请回看
[Key Concepts in RL](https://spinningup.openai.com/en/latest/spinningup/rl_intro.html) 原文。

## 来源

- OpenAI Spinning Up, *Part 1: Key Concepts in RL* —
  https://spinningup.openai.com/en/latest/spinningup/rl_intro.html
  （核验日期 2026-09-16；快照 Revision `038665d6`）
- 术语口径：[`../glossary/glossary.md`](../glossary/glossary.md)
