tasks = []

def add_task():
    task = input("请输入要添加的任务：")
    tasks.append(task)
    print("任务已添加！")

def remove_task():
    task = input("请输入要删除的任务：")
    if task in tasks:
        tasks.remove(task)
        print("任务已删除！")
    else:
        print("任务不存在！")

def show_tasks():
    print("当前任务列表：")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")

def todo_list():
    while True:
        print("\n=== TODO列表 ===")
        print("1. 添加任务")
        print("2. 删除任务")
        print("3. 显示任务")
        print("4. 退出")
        choice = input("请输入操作编号：")

        if choice == '1':
            add_task()
        elif choice == '2':
            remove_task()
        elif choice == '3':
            show_tasks()
        elif choice == '4':
            print("退出程序，谢谢使用！")
            break
        else:
            print("无效的操作！")

todo_list()
```
编写一个简单的命令行TODO列表程序，可以添加、删除和显示任务。
```
