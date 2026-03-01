tasks = []

def add_task(task):
    tasks.append({"task": task, "done": False})

def list_tasks():
    for i, t in enumerate(tasks):
        status = "✓" if t["done"] else "✗"
        print(f"{i+1}. {t['task']} [{status}]")

def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        print("Task deleted successfully")
    else:
        print("Invalid task number")

add_task("Learn GitHub")
add_task("Complete assignment")
list_tasks()
delete_task(0)
list_tasks()