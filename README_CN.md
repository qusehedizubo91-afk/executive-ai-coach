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
