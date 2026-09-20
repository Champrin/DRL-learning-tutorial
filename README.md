# DRL_learning

基于 GitHub Pages + RunDocs 的 Deep RL 课程站点仓库。

- 站点源码与课程内容：[`deep_rl_course/`](deep_rl_course/)
- 在线文档：启用 GitHub Pages 后自动部署（见 `.github/workflows/pages.yml`）

## 本地预览

```bash
cd deep_rl_course
bundle install
bundle exec jekyll serve
# 打开 http://127.0.0.1:4000
```

## 部署

推送到 `main` 分支后，GitHub Actions 会自动构建并发布到 GitHub Pages
（需在仓库 Settings → Pages 中将 Source 设为 "GitHub Actions"）。
