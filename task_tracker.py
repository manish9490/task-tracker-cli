tasks = []

def add_task(task):
    tasks.append({"task": task, "done": False})

def list_tasks():
    for i, t in enumerate(tasks):
        status = "✓" if t["done"] else "✗"
        print(f"{i+1}. {t['task']} [{status}]")

add_task("Learn GitHub")
add_task("Complete assignment")
list_tasks()