import os
import json
import requests

API_KEY = "sk-7910ab3c3b984df39fbdc7becfc3f59" # 你的 DeepSeek KEY
DATA_DIR = os.path.expanduser("~/executive-ai-coach/data")

def get_classification(file_name):
    prompt = f"分析文档名称: {file_name}。请按照 JSON 格式返回：main_role (CIO/CEO/CVC等), career_stage (初级/中级/资深), sub_domains (领域列表)。"
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    payload = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}],
        "response_format": {"type": "json_object"}
    }
    try:
        res = requests.post("https://api.deepseek.com/v1/chat/completions", headers=headers, json=payload)
        return res.json()['choices'][0]['message']['content']
    except:
        return "{}"

def run():
    meta_dir = os.path.join(DATA_DIR, "classification_metadata")
    os.makedirs(meta_dir, exist_ok=True)
    
    # 示例扫描 gartner_reports
    report_dir = os.path.join(DATA_DIR, "gartner_reports")
    for file in os.listdir(report_dir):
        if file.endswith(".pdf"):
            print(f"正在分类: {file}")
            tags = get_classification(file)
            with open(os.path.join(meta_dir, f"{file}.json"), "w") as f:
                f.write(tags)
    print("✅ 分类标签已生成")

if __name__ == "__main__":
    run()
