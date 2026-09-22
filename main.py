import file_utils
import note_utils
import ai_utils


def view_history(history):
    if not history:
        print("暂无历史记录")
        return
    print(f"已保存{len(history)}记录")
    for msg in history:
        if msg['role'] == "user":
            role = "用户"
        else:
            role = "AI"
        print(f"[{role}]{msg['content']}")
    print(f"已加载{len(history)}条历史数据")


def ask_ai(notes,history):
    if not notes:
        print("暂无笔记")
        return
    question = input("\n请输入你的问题:").strip()
    if not question:
        print("问题不能为空")
        return
    context = ai_utils.build_context(notes, question)
    if context:
        system_prompt = f"你是一个学习助手。请参考以下笔记回答用户问题：\n{context}"
    else:
        system_prompt = "你是一个学习助手。没有找到相关笔记，请凭你的知识回答。"

    messages = [{"role":"system","content": system_prompt}]  #给ai进行一个初始化设定
    for msg in history:
        messages.append(msg)
    messages.append({"role":"user","content":question})

    print("--ai正在思考--")
    reply = ai_utils.chat_with_ai(messages)
    print(f"AI回答:{reply}")

    history.append({"role":"user","content":question})
    history.append({"role":"assistant","content":reply})



def main():
    notes_filename = "data/notes.json"
    history_filename = "data/chat_history.json"
    notes = file_utils.load_notes(notes_filename)
    history = file_utils.load_chat_history(history_filename)
    while True:
        print("===AI笔记助手===")
        print("请选择你需要实现的功能:\n1.添加笔记\n2.查看所有笔记\n3.搜索笔记\n4.向AI提问\n5.查看对话历史\n6.导出对话记录\n7.删除记录"
              "\n8.退出")
        choice = input("请输入选项:")
        if choice == "1":
            note_utils.add_note(notes)
        elif choice == "2":
            note_utils.view_notes(notes)
        elif choice == "3":
            note_utils.search_notes(notes)
        elif choice == "4":
            ask_ai(notes,history)
        elif choice == "5":
            view_history(history)
        elif choice == "6":
            file_utils.export_history(history,"data/chat_export.txt")
        elif choice == "7":
            note_utils.delete_note(notes)
        elif choice == "8":
            file_utils.save_notes(notes,notes_filename)
            file_utils.save_chat_history(history,history_filename)
            print("保存成功")
            break
        else:
            print("无效选项")


if __name__ == '__main__':
    main()