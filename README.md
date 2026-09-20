# DRL_learning

基于 **GitHub Pages + Read the Docs 官方模板（Sphinx + sphinx_rtd_theme）** 的 Deep RL 课程站点。
站点结构与构建方式参考官方教程模板：<https://github.com/readthedocs/tutorial-template/>

- 站点源码与课程内容：[`deep_rl_course/`](deep_rl_course/)
- 自动部署：推送到 `main` 后由 GitHub Actions 构建发布（见 `deep_rl_course/.github/workflows/pages.yml`）

## 本地预览

```bash
cd deep_rl_course
pip install -r requirements.txt
sphinx-build -b html . _site
# 打开 _site/index.html，或：
python3 -m http.server -d _site 8000
```

## 部署

在仓库 **Settings → Pages → Source** 选择 **GitHub Actions**，推送 `main` 后自动发布到
`https://<用户名>.github.io/<仓库名>/`。

## 如何添加新页面（维护指南）

本站基于 **Sphinx + MyST-Parser**，所有内容为 Markdown。侧边栏目录由 `toctree` 生成，
**新建页面后必须登记进 toctree**，否则不会出现在左侧目录中（构建时会警告
`document isn't included in any toctree`）。

### 三种典型场景

#### 1. 在已有课程阶段中添加一页（最常见）

以在 `02_rl_foundation/`（Stage 2）新增 `td.md`（时序差分学习）为例：

```bash
# 1. 直接创建 Markdown 文件，无需任何 front matter / 配置
cat > deep_rl_course/02_rl_foundation/td.md << 'MD'
# TD Learning：时序差分

> 正文……
MD

# 2. 在该阶段的索引页 deep_rl_course/02_rl_foundation/README.md 末尾的
#    toctree 中登记（条目写文件相对路径，去掉 .md 后缀）
```

`02_rl_foundation/README.md` 中的 toctree 目前为空（该阶段还没有子页面），追加：

````markdown
```{toctree}
:maxdepth: 1

td
```
````

> 若该阶段的 README.md 已有 toctree（如 `00_orientation/README.md`），只需在条目列表中
> 加一行 `td` 即可。多个条目按顺序排列即侧边栏顺序。

#### 2. 添加一个全新的顶级栏目（出现在侧边栏根目录）

1. 新建目录与索引页：`deep_rl_course/14_new_topic/README.md`（首行为 `# 标题`，即侧边栏显示名）
2. 打开 `deep_rl_course/index.rst`，在对应分组的 `.. toctree::` 中加一行：

```rst
.. toctree::
   :maxdepth: 2
   :caption: 课程阶段

   00_orientation/README
   ...（略）...
   13_research/README
   14_new_topic/README      ← 新增
```

#### 3. 在证据卡（evidence/cards）中添加一张卡

只需把新卡按分类放进 `evidence/cards/docs|lit|math/` 目录，例如
`evidence/cards/lit/EV-L-108.md`。**但**还需在对应 `README.md` 的 toctree 中追加条目：

````markdown
```{toctree}
:maxdepth: 1

EV-L-001
...（略）...
EV-L-108      ← 新增
```
````

### 页面写作规范

- 文件首行为 `# 标题`（H1 有且仅有一个），侧边栏与浏览器标签页标题都取自它
- 正文用标准 Markdown（表格、代码块、引用均支持）；**不要**写 Jekyll front matter
- 站内链接写**不带后缀的相对路径**：`[术语表](../glossary/glossary)`、
  `[Stage 1](../01_math/README)`（MyST 会自动解析为正确 URL；写 `.md` 后缀也能工作，
  但无后缀更规范）
- 引用仓库内但不发布到网站的文件（如 `references/snapshots/` 下的快照、
  `state/STATE.yaml`），**不要做成链接**，用反引号写成代码格式并注明"仓库内文件"

### 不想发布到网站的目录

在 `conf.py` 的 `exclude_patterns` 中登记（现有：`references/snapshots`、`exercises`、
`projects`、`papers`、`state`）。被排除的目录不会出现在构建产物中。

### 修改后的检查清单

```bash
cd deep_rl_course
pip install -r requirements.txt   # 首次
sphinx-build -b html . _site      # 必须 0 个 WARNING
python3 -m http.server -d _site 8000   # 浏览器打开 http://127.0.0.1:8000 检查
git add -A && git commit -m "..." && git push   # 推送后约 1 分钟自动上线
```

常见警告对照：

| 警告 | 原因与修复 |
| --- | --- |
| `document isn't included in any toctree` | 新页面没登记进任何 toctree → 按上文场景 1/2/3 登记 |
| `toctree contains reference to nonexisting document` | toctree 条目路径写错（注意：不带 `.md` 后缀、相对当前文件） |
| `'myst' cross-reference target not found` | Markdown 链接目标不存在 → 检查相对路径是否正确、是否误链到被 exclude 的目录 |
