import json
import os


def load_notes(filename):
    if not os.path.exists(filename):
        print(f"{filename}不存在,使用空列表")
        return []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            notes = json.load(f)
        print(f"已加载{len(notes)}条笔记")
        return notes
    except json.JSONDecodeError:
        print(f"{filename}已损坏使用空列表")
        return []


def save_notes(notes, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(notes, f, ensure_ascii=False, indent=4)
        print(f"已写入{len(notes)}条数据")


def load_chat_history(filename):
    if not os.path.exists(filename):
        print("数据不存在")
        return []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"{filename}数据已损坏使用空列表")
        return []


def save_chat_history(history, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=4)
        print(f"已写入{len(history)}条数据")


def export_history(history,filename):
    if not history:
        print("对话为空")
        return
    with open(filename,"w",encoding="utf-8")as f:
        for msg in history:
            if msg['role'] == "user":
                role = "用户"
            else:
                role = "AI"
            f.write(f"[{role}] {msg['content']}\n\n")
    print(f"已导入{len(history)}条数据")
