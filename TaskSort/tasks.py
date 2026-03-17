def get_highest_task(tasks):
    if not tasks:
        return 0
    return max(task["task_id"] for task in tasks)
def add_task(tasks, task):
    new_task = {
        "task_id": get_highest_task(tasks) + 1,
        "title": task,
        "complete": False,
    }
    tasks.append(new_task)

def complete_task(tasks, task_id):
    for task in tasks:
        if task["task_id"] == task_id:
            task["complete"] = True
            return True
    return False

def delete_task(tasks, task_id):
    new_tasks = [task for task in tasks if task["task_id"] != task_id]
    return new_tasks