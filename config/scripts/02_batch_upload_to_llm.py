import os
import shutil

# 源头：你的各种数据文件夹
DATA_DIR = os.path.expanduser("~/executive-ai-coach/data")
# 目的地：AnythingLLM 真正读取的文档区
TARGET_DIR = os.path.expanduser("~/executive-ai-coach/storage/documents")

def force_sync():
    if not os.path.exists(TARGET_DIR): os.makedirs(TARGET_DIR)
    
    # 定义要搬运的文件夹
    sub_folders = ['gartner_reports', 'industry_news', 'books']
    for folder in sub_folders:
        src = os.path.join(DATA_DIR, folder)
        dest = os.path.join(TARGET_DIR, folder)
        if os.path.exists(src):
            if os.path.exists(dest): shutil.rmtree(dest) # 清理旧的
            shutil.copytree(src, dest) # 搬运新的
            print(f"已强制同步文件夹: {folder}")

if __name__ == "__main__":
    force_sync()
