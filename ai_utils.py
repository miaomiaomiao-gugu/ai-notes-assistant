import os
import requests
import re
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
API_KEY = os.environ.get("OPENAI_API_KEY")
BASE_URL = os.environ.get("OPENAI_BASE_URL")
URL = f"{BASE_URL}/chat/completions"


def extract_keywords(text):
    keywords = []
    chinese_seg = re.findall(r'[\u4e00-\u9fa5]+',text)
    for sge in chinese_seg:
        if len(sge) <= 2:
            keywords.append(sge)
        else:
            for i in range(len(sge)-1):
                keywords.append(sge[i:i+2])
    english_sge = re.findall(r'[a-zA-z]+',text)
    keywords.extend(english_sge)
    return list(set(keywords))


def build_context(notes, question):
        if not notes:
            return ""
        context = "以下是用户保存的全部笔记：\n"
        for note in notes:
            context += (
                f"标题：{note['title']}\n"
                f"内容：{note['content']}\n\n"
            )
        print(f"已向 AI 提供 {len(notes)} 条笔记")
        return context


def chat_with_ai(messages):
    """调用 AI，返回回复内容"""
    if not API_KEY:
        return "[错误] 未找到 API Key，请检查环境变量"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "deepseek-chat",
        "messages": messages
    }

    try:
        response = requests.post(URL, headers=headers, json=data,
                                 verify=False, timeout=30)
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            return f"[错误 {response.status_code}] {response.text}"
    except requests.exceptions.RequestException as e:
        return f"[网络错误] {e}"


