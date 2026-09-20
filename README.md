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
