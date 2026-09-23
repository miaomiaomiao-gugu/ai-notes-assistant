

def add_note(notes):
    while True:
        add_title = input("请输入标题:").strip()
        if not add_title:
            print("标题不能为空")
            continue
        if any(n["title"] == add_title for n in notes):
            print(f"{add_title}已有记录，请更换标题")
            continue  # 继续循环
        break
    while True:
        add_content = input("请输入内容:").strip()
        if not add_content:
            print("内容不能为空")
            continue
        break
    add_tag = input("请输入标签(用逗号分隔，可留空):").strip()
    add_tag = add_tag.replace("，", ",")  # 中文逗号统一成英文
    tags = [t.strip() for t in add_tag.split(",") if t.strip()]
    new_id = max((n['id'] for n in notes),default=0)+1
    new_note = {"id":new_id,
                "title":add_title,
                "content":add_content,
                "tags":tags}
    print("添加成功")
    notes.append(new_note)


def view_notes(notes):
    if not notes:
        print("暂无数据")
        return
    for note in notes:
        tags_str = "、".join(note['tags']) if note['tags'] else "-"
        content = note["content"]
        if len(content) > 40:
            content = content[:40] + "..."
        print("-"*40)
        print(f"ID:{note['id']}")
        print(f"标题:{note['title']}")
        print(f"内容:{content}")
        print(f"标签:{tags_str}")
        print("-"*40)


def search_notes(notes):
    if not notes:
        print("暂无数据")
        return
    found = False   #只判断一次无需循环判断
    search_title = input("请输入你要查找的标题：")
    for note in notes:
        if search_title == note['title']:
            print("查找成功")
            tags_str = "、".join(note["tags"]) if note["tags"] else "-"
            print("-" * 40)
            print(f"ID:{note['id']}")
            print(f"标题:{note['title']}")
            print(f"内容:{note['content']}")
            print(f"标签:{tags_str}")
            print("-" * 40)
            found = True
            break
    if not found:
        print("暂无该标题")


def delete_note(notes):
    print("\n--- 删除笔记 ---")
    target_title = input("输入要删除的标题：").strip()
    for n, note in enumerate(notes):
        if note['title'] == target_title:
            notes.pop(n)
            print("删除成功")
            return
    print("未找到匹配的记录")


