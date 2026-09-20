---
title: "Stage 0（RL 导论）术语表"
sort: 1
category: "附录"
---

# Stage 0（RL 导论）术语表

> **核验说明**：本表全部条目均于 **2026-09-16** 通过 `curl` 拉取并逐条对照
> [Spinning Up — Part 1: Key Concepts in RL](https://spinningup.openai.com/en/latest/spinningup/rl_intro.html)
> 原文措辞后撰写，**未凭记忆书写**。快照存档见
> [`../references/snapshots/docs/spinningup_rl_intro.html`](../references/snapshots/docs/spinningup_rl_intro.html)
> （页面 Revision `038665d6`）。
>
> 符号一栏遵循该页的记法约定；`s`/`o` 混用问题见文末「符号约定说明」。

---

## 1. 核心交互对象

| 术语 | 英文 | 符号 | 定义 |
| --- | --- | --- | --- |
| 智能体 | agent | （无专用符号；常以策略 π 代称） | 在环境中通过试错（trial and error）学习、并据策略选择动作的主体，其目标是最大化累积奖励。 |
| 环境 | environment | （无专用符号） | 智能体所处且与之交互的世界，它会因智能体的动作而改变，也可能自行变化。 |

## 2. 状态与观测

| 术语 | 英文 | 符号 | 定义 |
| --- | --- | --- | --- |
| 状态 | state | $s$、$s_t$；状态空间 $S$ | 对世界状态的一份完整描述，没有任何关于世界的信息对其隐藏（不存在被隐藏的信息）。 |
| 观测 | observation | $o$ | 对状态的部分描述，可能遗漏信息；只能看到部分观测时称环境为**部分可观测**（partially observed），能看到完整状态时称**完全可观测**（fully observed）。 |

## 3. 动作与奖励

| 术语 | 英文 | 符号 | 定义 |
| --- | --- | --- | --- |
| 动作 | action | $a$、$a_t$；动作空间 $A$ | 智能体在每一步交互中选择的行为；某环境中全部合法动作的集合称为**动作空间**（action space），可离散也可连续。 |
| 奖励 | reward | $r_t$；奖励函数 $R$ | 环境给出的标量信号，用以指明当前世界状态的好坏，其一般形式为 $r_t = R(s_t, a_t, s_{t+1})$（常简化为 $R(s_t)$ 或 $R(s_t,a_t)$）。 |

## 4. 决策与轨迹

| 术语 | 英文 | 符号 | 定义 |
| --- | --- | --- | --- |
| 策略 | policy | $\pi$（随机），$a_t \sim \pi(\cdot\mid s_t)$；确定性策略 $a_t = \mu(s_t)$；参数 $\theta$、$\phi$ | 智能体用来决定采取何种动作的规则，可确定性也可随机，本质上是「智能体的大脑」，在深度 RL 中为参数化策略。 |
| 回合 | episode | 与轨迹同记 $\tau$ | 从初始状态到终止的一段完整交互过程；该页指出轨迹（trajectories）也常被称作 **episodes** 或 **rollouts**。 |
| 轨迹 | trajectory | $\tau = (s_0, a_0, s_1, a_1, \dots)$ | 世界中状态与动作构成的序列，其首个状态 $s_0 \sim \rho_0(\cdot)$ 由初始状态分布随机采样，状态转移 $s_{t+1} \sim P(\cdot\mid s_t,a_t)$ 仅依赖最近一次动作。 |

## 5. 目标与形式化

| 术语 | 英文 | 符号 | 定义 |
| --- | --- | --- | --- |
| 回报 | return | $R(\tau)$ | 沿轨迹累积的奖励总量，分为**有限时域无折扣回报** $R(\tau)=\sum_{t=0}^{T} r_t$ 与**无限时域折扣回报** $R(\tau)=\sum_{t=0}^{\infty}\gamma^{t} r_t$，RL 的目标是最大化期望回报 $J(\pi)$。 |
| 折扣因子 | discount factor | $\gamma \in (0,1)$ | 对越晚获得的奖励打越低折扣的系数（「现在的钱优于以后的钱」），其数学作用在于使无限时域奖励和收敛为有限值；该页给出取值范围为 $\gamma \in (0,1)$。 |
| 马尔可夫决策过程 | Markov Decision Process (MDP) | 五元组 $\langle S, A, R, P, \rho_0 \rangle$ | 标准数学形式化框架：$S$ 为全部合法状态、$A$ 为全部合法动作、$R: S \times A \times S \to \mathbb{R}$ 为奖励函数、$P: S \times A \to \mathcal{P}(S)$（在 $s$ 采取 $a$ 后转移到 $s'$ 的概率）、$\rho_0$ 为初始状态分布；其「马尔可夫」之名源于**马尔可夫性质**：转移只依赖最近的状态与动作，而与更早历史无关。 |

---

## 符号约定说明

核验时该页特别提示（*You Should Know*）：RL 记法中有时会把状态符号 $s$ 放在技术上更应写观测符号 $o$ 的位置——尤其是描述智能体如何决定动作时，形式上写的是「动作以状态为条件」，
而实际上智能体因无法访问真实状态，只能以**观测**为条件。本表沿用该页的标准记法，具体含义需依上下文判断。

## 三条最易混淆的边界

1. **state vs observation**：state 是完整描述，observation 是可能丢失信息的部分描述。
2. **reward vs return**：reward 是单步标量信号 $r_t$，return 是沿轨迹的累积量 $R(\tau)$。
3. **episode vs trajectory**：在该页语境下二者可互换，均指 $s_0,a_0,s_1,a_1,\dots$ 序列；episode 更强调「有始有终的一段交互」。

## 来源

- OpenAI Spinning Up, *Part 1: Key Concepts in RL* —
  https://spinningup.openai.com/en/latest/spinningup/rl_intro.html
  （核验日期 2026-09-16，页面 Revision `038665d6`）
