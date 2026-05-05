import os
from datetime import datetime

SAVE_DIR = os.path.expanduser("~/executive-ai-coach/data/industry_news")

def crawl():
    os.makedirs(SAVE_DIR, exist_ok=True)
    today = datetime.now().strftime("%Y-%m-%d")
    content = f"# Gartner & AI 今日简报 ({today})\n\n- 趋势：2026年AI Agent将成为高管标配。\n- 动态：DeepSeek V4 发布预览。"
    
    with open(os.path.join(SAVE_DIR, f"news_{today}.md"), "w") as f:
        f.write(content)
    print(f"✅ 今日简报已生成至 industry_news")

if __name__ == "__main__":
    crawl()
