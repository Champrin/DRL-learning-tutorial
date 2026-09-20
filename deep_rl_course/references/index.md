---
title: "Source Index（来源索引）"
sort: 101
permalink: "references/"
---

# Source Index（来源索引）

> **用途**：记录本课程引用过的每一份外部来源，做到「每条结论可回溯」。
> 新增来源时请追加行，勿改动既有 ID。
>
> **核验方式**：URL 一律于 **2026-09-16** 用 `curl -L` 实际请求，以返回 HTTP 200 且正文章节文字可提取为准；
> `Local file` 列给出仓库内快照的真实相对路径（相对于本文件所在目录）。
>
> **Reliability 分级**：
> - `A-primary`：一手来源（原始论文、官方文档、作者官网）
> - `B-secondary`：权威二手教程/课程
> - `C-draft`：个人笔记、博客，仅作线索

---

## Source Index

| ID | Title | Source | URL | Local file | Topic | Reliability | Used in |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-001 | Part 1: Key Concepts in RL（Spinning Up） | OpenAI Spinning Up | https://spinningup.openai.com/en/latest/spinningup/rl_intro.html | `snapshots/docs/spinningup_rl_intro.html` | RL 导论：agent/environment/state/observation/action/reward/policy/trajectory/return/discount/MDP | A-primary | `glossary/glossary.md`, `00_orientation/exercises.md` |
| SRC-002 | Gymnasium 官网（文档首页） | Farama Foundation | https://gymnasium.farama.org/ | （未存档） | RL 环境标准 API 与生态入口 | A-primary | 已核验可访问（HTTP 200）；**尚未被本课程文档引用** |
| SRC-003 | Gymnasium `Env` API | Farama Foundation | https://gymnasium.farama.org/api/env/ | `snapshots/docs/gymnasium_api_env.html` | `Env` 类：`step()` / `reset()` / `action_space` / terminated / truncated | A-primary | 已核验；**尚未被本课程文档引用**（备 Stage 7 使用） |
| SRC-004 | Reinforcement Learning: An Introduction (2nd ed.) 教材页 | Sutton & Barto (MIT Press, 2018) | http://incompleteideas.net/book/the-book-2nd.html | `snapshots/math/sutton_barto.html` | RL 经典教材：MDP、回报、折扣的权威定义与完整 PDF | A-primary | 已核验可访问（HTTP 200）；**尚未被本课程文档引用** |
| SRC-005 | Introduction（Spinning Up） | OpenAI Spinning Up | https://spinningup.openai.com/en/latest/user/introduction.html | `snapshots/papers/spinningup_introduction.html` | Spinning Up 定位与学习路径 | A-primary | 课程规划参考 |
| SRC-006 | Spinning Up 首页 | OpenAI Spinning Up | https://spinningup.openai.com/en/latest/ | `snapshots/math/spinningup.html` | 算法总览入口（VPG/TRPO/PPO/DDPG/TD3/SAC） | A-primary | 后续 Stage 3–6 参考 |
| SRC-007 | Human-level control through deep reinforcement learning | Mnih et al., *Nature* 518 (2015) | https://www.nature.com/articles/nature14236 | `snapshots/papers/nature14236.html` | DQN 原始论文 | A-primary | 后续 Stage 3（value-based） |
| SRC-008 | CS285 Deep Reinforcement Learning（课程页） | UC Berkeley / Sergey Levine | https://rail.eecs.berkeley.edu/deeprlcourse/ | `snapshots/math/cs285.html` | 系统性深度 RL 课程 | B-secondary | 后续 Stage 2–6 参考 |
| SRC-009 | Stable-Baselines3 文档首页 | DLR-RM (GitHub) | https://stable-baselines3.readthedocs.io/ | `snapshots/docs/sb3_docs_home.html` | 工程实现参考与算法清单 | A-primary | 后续 Stage 7（RL engineering） |
| SRC-010 | Deep Learning（教材页） | Goodfellow, Bengio, Courville (MIT Press) | https://www.deeplearningbook.org/ | `snapshots/math/deep_learning_book.html` | 深度学习基础教材 | A-primary | 前置数学/深度学习 |

---

## 待归档（gaps）

以下来源已被引用或已核验，但尚无仓库内快照；需要时补档。

| ID | Title | URL | 备注 |
| --- | --- | --- | --- |
| SRC-002 | Gymnasium 官网 | https://gymnasium.farama.org/ | 本次仅核验可访问性（HTTP 200）与站点结构，未存档；如需引用其正文，请补快照到 `snapshots/docs/`。 |

---

## 快照规范（snapshot policy）

1. 命名：`<host>_<page>.html`，例如 `spinningup_rl_intro.html`、`gymnasium_api_env.html`。
2. 存放：`snapshots/docs/`（官方文档）、`snapshots/papers/`（论文）、`snapshots/math/`（教材/课程）。
3. 命令：`curl -sL -o <target>.html <url>`。
4. 若来源有版本号/Revision，请在 `Title` 或备注中记录（例：SRC-001 页面 Revision `038665d6`）。
5. 快照仅用于离线复核，**版权归原作者**，请勿再分发。

## 新增来源检查清单

- [ ] URL 用 `curl -L` 请求返回 HTTP 200
- [ ] 已提取正文并确认术语/结论确实出现在该页（不凭记忆）
- [ ] 已下载快照并按规范命名
- [ ] 已填写 Reliability 分级与 Used in

## 变更记录

| 日期 | 说明 |
| --- | --- |
| 2026-09-16 | 初版：核验并录入 SRC-001…SRC-010；新增 SRC-001 快照至 `snapshots/docs/spinningup_rl_intro.html`。 |
| 2026-09-16 | 勘误：SRC-003 的 URL 由 `/api/env.html` 改为 `/api/env/`。站点 `<link rel="canonical">` 仍写 `.html`，但该地址实测 HTTP 404（`/api/env/` 为 200）——**以实测为准，勿信页面 canonical 标签**。 |
