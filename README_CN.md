# Executive AI Coach - 高管AI教练系统

## 🎯 项目简介

这是一个为 IT 高管、创业者和投资人打造的**个人知识管理 + AI 助手系统**。

它可以帮助你：
- ✅ **管理海量知识资源** - Gartner 报告、书籍、会议纪要、社媒内容等
- ✅ **智能分类和检索** - 按角色、领域、阶段自动分类
- ✅ **个性化建议** - 根据你的职位和阶段提供专业指导
- ✅ **每日新闻更新** - 自动爬取行业最新动态
- ✅ **完全私密** - 所有数据本地运行，不上云

---

## 🏗️ 系统架构
你的数据输入 ↓ ┌─────────────────────┐ │ AnythingLLM │ │ (本地知识库) │ ├─────────────────────┤ │ ✓ 文件上传 │ │ ✓ 自动分块 │ │ ✓ 向量化存储 │ │ ✓ 知识库管理 │ └────────┬────────────┘ ↓ ┌─────────────────────┐ │ DeepSeek API │ │ (AI 回答) │ ├─────────────────────┤ │ ✓ 文档分类 │ │ ✓ 问题回答 │ │ ✓ 建议生成 │ └────────┬────────────┘ ↓ 你的答案


---

## 📂 项目结构
executive-ai-coach/ ├── config/ ← 配置文件 │ ├── roles_schema.json # 11个角色定义 │ ├── career_stages.json # 职业生涯阶段 │ ├── deepseek_config.json # DeepSeek API配置 │ ├── anythingllm_config.json # AnythingLLM配置 │ ├── classification_rules.json # 分类规则 │ └── system_prompt.md # AI助手人设 │ ├── data/ ← 你的数据（待添加） │ ├── gartner_reports/ # Gartner报告 │ ├── books/ # 书籍PDF │ ├── conference_notes/ # 会议纪要 │ ├── social_media/ # 社媒内容 │ ├── reading_notes/ # 读书笔记 │ ├── industry_news/ # 自动爬虫 │ └── custom_input/ # 其他输入 │ ├── scripts/ ← 脚本（待添加） │ └── [Python脚本] │ ├── README_CN.md # 这个文件 ├── QUICK_START_CN.md # 快速开始指南 └── requirements.txt # 依赖项


---

## 🚀 快速开始

### 前置要求
- 电脑（Windows/Mac/Linux）
- Docker（推荐）或本地 AnythingLLM 桌面版
- 网络连接

### 第1步：安装 AnythingLLM

**方式 A：Docker（推荐）**
```bash
docker run -d \
  -v anythingllm:/home/anythingllm/storage \
  -e STORAGE_DIR=/home/anythingllm/storage \
  -p 3001:3001 \
  mintplexlabs/anythingllm:latest
