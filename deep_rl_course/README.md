# Deep RL 从零到机器人行人跟随 — 离线课程库

> 项目类型：多 Agent 科研级学习系统
> 主 Agent（Chief Instructor）：Kimi K3
> 创建日期：2026-09-16（Phase 0：课程设计 & 知识审计）

## 目标

从零开始系统学习 Deep Reinforcement Learning，最终独立设计、训练、评估并部署一个
**移动机器人行人跟随（Person Following）** 的深度强化学习策略。

## 最高原则

1. **所有事实属性内容必须联网核验**（Evidence Card + Source Index），禁止凭模型记忆回答。
2. **先基础后算法**：禁止跳过 MDP/Bellman/经典 RL 直接学 PPO/SAC。
3. **四层学习**：每个算法必须完成 直觉 → 数学推导 → 从零实现 → 实验分析。
4. **反伪理解**：通过 Concept + Math + Code + Experiment 才算掌握。
5. **不假设 RL 一定最优**：最终算法由 文献 + baseline + 实验 决定。

## 课程阶段

| 阶段 | 内容 | 状态 |
| --- | --- | --- |
| Stage 0 | [RL 导论入门测验](00_orientation/exercises/) | ✅ 已完成 |
| Stage 1 | [数学基础（概率 / 线代 / 微积分 / 优化）](01_math/README) | 📋 计划中 |
| Stage 2 | [MDP / Bellman / MC / TD](02_rl_foundation/README) | 📋 计划中 |
| Stage 3-4 | [Q-learning → DQN](03_value_based/README) | 📋 计划中 |
| Stage 5 | [Policy Gradient](04_policy_gradient/README) | 📋 计划中 |
| Stage 6-7 | [A2C → GAE → PPO](05_actor_critic/README) | 📋 计划中 |
| Stage 8 | [DDPG → TD3 → SAC](06_continuous_control/README) | 📋 计划中 |
| Stage 9-20+ | 工程化 → 机器人行人跟随 → ROS 2 部署 | 📋 计划中 |

## 关键文件

| 文件 | 说明 |
| --- | --- |
| [Source Index](references/index) | 所有外部来源的索引（URL + 本地快照 + 可靠性分级） |
| 证据卡（[官方文档](evidence/cards/docs/README) · [论文文献](evidence/cards/lit/README) · [数学工具](evidence/cards/math/README)） | 每个重要知识点的事实核查卡 |
| `state/STATE.yaml` | 当前学习进度（中断后可恢复） |
| [RL 术语表](glossary/glossary) | 已核验定义 |
| [Phase 0 报告](PHASE0_REPORT) | Phase 0 核验工作完整报告 |

## 当前状态

见 `state/STATE.yaml`。当前处于 **Stage 0（Orientation）**，尚未开始学习算法。
