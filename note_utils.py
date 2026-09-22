

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
    add_tag = input("请输入标签(可以用逗号分隔且留空):").strip()  #去掉空格，净化列表
    tags = [t.strip() for t in add_tag.strip(" ，") if t.strip()]
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
        print(f"ID:{note['id']},标题:{note['title']},内容:{note['content']},标签:{tags_str}")


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
            print(f"ID:{note['id']},标题:{note['title']},内容:{note['content']},标签:{tags_str}")
            found = True
            break
    if not found:
        print("暂无该标题")


def delete_note(notes):
    print("\n--- 删除记录 ---")
    content = input("输入要删除的标题：").strip()
    for n, note in enumerate(notes):
        if note["content"] == content:
            notes.pop(n)
            print("删除成功")
            return
    print("未找到匹配的记录")


