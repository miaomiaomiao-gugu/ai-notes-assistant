 AI 学习笔记助手:

一个基于本地笔记的 AI 问答系统。先记录知识点，然后向 AI 提问，AI 会参考你的笔记回答。

 功能:

- 添加、查看、搜索、删除笔记
- 向 AI 提问（基于笔记内容）
- 查看对话历史
- 导出对话记录
- 数据持久化（JSON 存储）

技术栈:

- Python 3
- requests（调用大模型 API）
- DeepSeek API
- JSON / 文件操作

 项目结构:
ai-notes-assistant/
├── main.py # 主程序入口
├── file_utils.py # 文件读写
├── note_utils.py # 笔记操作
├── ai_utils.py # AI 调用
└── .gitignore



   


