import os
import shutil

# 定义源目录和 AnythingLLM 的文档挂载目录
BASE_DATA_DIR = os.path.expanduser("~/executive-ai-coach/data")
LLM_DOC_DIR = os.path.expanduser("~/executive-ai-coach/data/documents") # 映射后的主目录

def sync_to_llm():
    if not os.path.exists(LLM_DOC_DIR):
        os.makedirs(LLM_DOC_DIR)
    
    # 扫描子文件夹
    sub_folders = ['gartner_reports', 'books', 'industry_news', 'conference_notes']
    for folder in sub_folders:
        src = os.path.join(BASE_DATA_DIR, folder)
        if os.path.exists(src):
            for file in os.listdir(src):
                if file.endswith(('.pdf', '.md', '.txt', '.docx')):
                    # 将文件复制到 AnythingLLM 能识别的 documents 根目录
                    shutil.copy2(os.path.join(src, file), os.path.join(LLM_DOC_DIR, file))
                    print(f"已同步到 AnythingLLM: {file}")

if __name__ == "__main__":
    sync_to_llm()
