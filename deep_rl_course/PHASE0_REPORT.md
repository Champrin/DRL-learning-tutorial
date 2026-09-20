---
title: "Phase 0 报告：课程设计与知识审计"
sort: 100
permalink: "phase0/"
---

# Phase 0 报告：课程设计与知识审计

> 日期：2026-09-16
> 状态：完成
> 证据：`evidence/cards/`（26 张卡）+ `references/index.md` + `references/snapshots/`（70+ 快照）

## 1. 核验工作摘要

5 个 Subagent 并行执行，全部结果经主 Agent 交叉复核：

| Agent | 模型 | 任务 | 结果 |
| --- | --- | --- | --- |
| A | glm-5.3 | 数学前置知识核验（Spinning Up / CS285 / S&B / DL Book） | 4 源 CONFIRMED，无冲突 |
| B | grok-4.6 | 算法事实核查 + person following 文献搜索 | 7 条 CLAIM 全 PASS；13 篇论文入索引 |
| D | kimi-k2.7 | Gymnasium / SB3 / PyTorch / ROS 2 / Isaac / MuJoCo 官方文档核验 | 6 项生态全部核验，版本锁定 |
| F | hy4-preview | 盲答：路线图 / "要不要 RL" / 建模候选 | 独立结论已采纳（见 §5），3 个 arXiv 引用经主 Agent 复核存在 |
| E | deepseek-v4.1-flash | 术语表 / Source Index / Stage 0 测验 | 完成，发现并修正 2 处文档自错 |

## 2. 关键已核验事实（双源以上）

- **学习方法论**：OpenAI Spinning Up 明确建议 "Write your own implementations ... from scratch ... by far the best way"，且建议 "implement the simplest algorithms first, and only gradually introduce complexity"。（EV-L-101；`references/snapshots/docs/spinning_up_researcher.html` 原文引用）
- **数学先修**：Spinning Up 要求概率统计（随机变量、贝叶斯、链式法则、期望、标准差、重要性采样）+ 多元微积分（梯度、Taylor 展开可选）。（EV-M-001）
- **课程先修**：Berkeley CS285 要求 CS189 或同等（ML/数值优化/RL 导论），并指向 S&B 第 3-4 章。（EV-M-002）
- **Gymnasium API**：`reset() → (obs, info)`；`step() → (obs, reward, terminated, truncated, info)` 五元组；terminated（环境终止）与 truncated（时间限制截断）语义分离。（EV-D-001）
- **算法元数据**：PPO 1707.06347 / SAC 1801.01290 / TD3 1802.09477 / DDPG 1509.02971 / GAE 1506.02438 / DQN Nature 14236 —— 全部 arXiv abs 页核验通过。（EV-L-001~007）

## 3. 版本锁定（Stage 18 前需重新核验 Isaac）

gymnasium 1.3.0 / stable-baselines3 2.9.0 / torch 2.14.0 / mujoco 3.13.0 /
ROS 2 目标 LTS：Jazzy（EOL 2029-05）/ Isaac Sim 6.1.0 + Isaac Lab 3.0.0-beta2.patch1

## 4. 冲突与不确定性登记

- Isaac 文档存在 4.5/6.1 版本混合提示 → 置信度 MEDIUM-HIGH，到 Stage 18 重新核验。
- SoNIC / SGN 等 2024 论文的 reward/obs 细节摘要未披露 → 标记 UNCERTAIN，论文精读阶段补核。
- 无来源间实质冲突（CONFLICT DETECTED: 0）。

## 5. HY4 盲答核心结论（已采纳进课程设计）

1. **经典 baseline 必须先于 RL 实验**：没有 PID/纯跟踪/DWA baseline 就无法判断 RL 是否有价值。
2. **"要不要 RL"不能预设**：跟随本质是轨迹跟踪控制问题；RL 的差异化优势在拥挤人群社交权衡、遮挡时预测性行为、多目标难手写代价。最终由实验裁决。
3. **混合架构是文献实际做法**：RL 输出高层决策（如角速度），底层交给 DWA/MPC 执行 + 安全兜底（arXiv:2211.04993 即此模式）。
4. **reward 建议用势函数（potential-based）形式**、全项归一化 + 消融；终止条件与奖励边界一致。
