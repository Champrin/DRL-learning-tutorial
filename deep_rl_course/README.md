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

## 目录结构

```text
deep_rl_course/
├── README.md                ← 本文件
├── 00_orientation/          ← Stage 0：RL 全景地图 + 入门测验
├── 01_math/                 ← Stage 1：概率 / 线代 / 微积分 / 优化
├── 02_rl_foundation/        ← Stage 2：MDP / Bellman / MC / TD
├── 03_value_based/          ← Stage 3-4：Q-learning → DQN
├── 04_policy_gradient/      ← Stage 5：REINFORCE → Policy Gradient Theorem
├── 05_actor_critic/         ← Stage 6-7：A2C → GAE → PPO
├── 06_continuous_control/   ← Stage 8：DDPG → TD3 → SAC
├── 07_rl_engineering/       ← Stage 9：reward 设计 / 探索 / 归一化 / 调试 / 评估
├── 08_partial_observability/← Stage 10：POMDP / 历史 / 循环策略
├── 09_robotics_rl/          ← Stage 11：机器人 RL / sim-to-real / 安全
├── 10_person_following/     ← Stage 12-17：行人跟随建模与环境
├── 11_isaac_sim/            ← Stage 18：Isaac Sim / Isaac Lab
├── 12_ros2_deployment/      ← Stage 19：ROS 2 部署
├── 13_research/             ← Stage 20+：科研分析与论文审稿
├── papers/                  ← 论文阅读笔记（审稿式模板）
├── references/              ← Source Index + 网页/PDF 离线快照
├── evidence/                ← Evidence Cards（事实核查卡）
├── state/                   ← 学习进度状态机（STATE.yaml）
├── exercises/               ← 跨阶段练习
├── projects/                ← 最终项目代码
└── glossary/                ← 术语表 / 公式表 / 算法地图
```

## 关键文件

| 文件 | 说明 |
| --- | --- |
| `references/index.md` | 所有外部来源的索引（URL + 本地快照 + 可靠性分级） |
| `evidence/cards/` | 每个重要知识点的证据卡（CLAIM/EVIDENCE/VERDICT/CONFIDENCE） |
| `state/STATE.yaml` | 当前学习进度（中断后可恢复） |
| `glossary/glossary.md` | RL 术语表（已核验定义） |
| `00_orientation/exercises.md` | Stage 0 入门小测验 |
| `PHASE0_REPORT.md` | Phase 0 核验工作完整报告 |

## 当前状态

见 `state/STATE.yaml`。当前处于 **Stage 0（Orientation）**，尚未开始学习算法。
