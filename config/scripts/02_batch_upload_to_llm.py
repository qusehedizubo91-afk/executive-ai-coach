import os
import shutil

# 源头：你放 Gartner 报告的地方
DATA_DIR = os.path.expanduser("~/executive-ai-coach/data")
# 目的地：新 Docker 容器读取的地方
DEST_DIR = os.path.expanduser("~/executive-ai-coach/anythingllm_data/documents")

def sync():
    if not os.path.exists(DEST_DIR): os.makedirs(DEST_DIR)
    # 扫描子文件夹并整个搬过去
    for folder in ['gartner_reports', 'industry_news', 'books']:
        src = os.path.join(DATA_DIR, folder)
        dst = os.path.join(DEST_DIR, folder)
        if os.path.exists(src):
            if os.path.exists(dst): shutil.rmtree(dst)
            shutil.copytree(src, dst)
            print(f"✅ 已同步: {folder}")

if __name__ == "__main__":
    sync()
