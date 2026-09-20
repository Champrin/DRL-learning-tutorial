# Sphinx 配置文件 —— 参考 Read the Docs 官方教程模板
# https://github.com/readthedocs/tutorial-template/

# -- 项目信息 -------------------------------------------------------
project = "Deep RL 从零到机器人行人跟随"
copyright = "2026, champrin"
author = "champrin"
release = "0.1"

# -- 常规配置 -------------------------------------------------------
extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "myst_parser",  # 支持 Markdown 源文件
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
}
intersphinx_disabled_domains = ["std"]

templates_path = ["_templates"]

# 支持 .md 与 .rst 两种源文件
source_suffix = [".rst", ".md"]

# 站点首页（根 toctree 所在文档）
master_doc = "index"

# 排除不参与构建的内容
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    ".github",
    "references/snapshots",   # 大体积离线快照，仅存仓库不入站
    "exercises",
    "projects",
    "papers",
    "state",
    "PHASE0_REPORT.rst.bak",
    "README.md",  # 内容已并入 index.rst，避免重复文档告警
]

language = "zh_CN"

# -- HTML 输出选项 ---------------------------------------------------
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

# MyST 解析器选项：允许目录树风格的标题层级
myst_heading_anchors = 3

# 证据卡等文档为「小节式」结构，允许非 H1 起始标题
suppress_warnings = ["myst.header"]
