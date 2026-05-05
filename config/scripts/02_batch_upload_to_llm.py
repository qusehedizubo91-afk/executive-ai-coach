import os
import shutil

BASE_DIR = os.path.expanduser("~/executive-ai-coach/data")
# AnythingLLM 扫描的主目录
TARGET_DOC_DIR = os.path.join(BASE_DIR, "documents")

def sync():
    # 自动创建 documents 下的子文件夹
    folders = ['industry_news', 'gartner_reports']
    for f in folders:
        src = os.path.join(BASE_DIR, f)
        dest = os.path.join(TARGET_DOC_DIR, f)
        if os.path.exists(src):
            if not os.path.exists(dest): os.makedirs(dest)
            for file in os.listdir(src):
                if file.endswith(('.md', '.pdf')):
                    shutil.copy2(os.path.join(src, file), os.path.join(dest, file))
                    print(f"已同步: {f}/{file}")

if __name__ == "__main__":
    sync()
