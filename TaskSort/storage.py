import json

def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)  # loads the json list from file?
            return tasks
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4) # saves a list to the file?