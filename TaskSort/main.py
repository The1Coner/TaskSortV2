import argparse
from storage import load_tasks, save_tasks
from tasks import add_task, complete_task, delete_task

def main():

    parser = argparse.ArgumentParser(description="TaskSort") # not sure what this does
    subparsers = parser.add_subparsers(dest="command",required=True) # not sure what this does

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("title", type=str)
    complete_parser = subparsers.add_parser("complete")
    complete_parser.add_argument("task_id", type=int)
    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("task_id", type=int)

    subparsers.add_parser("list")

    args = parser.parse_args()

    tasks = load_tasks()

    if args.command == "add":
        add_task(tasks, args.title)
        save_tasks(tasks)
    elif args.command == "complete":
        success = complete_task(tasks, args.task_id)
        if not success:
            print("Task not found, could not complete")
        else:
            save_tasks(tasks)
    elif args.command == "delete":
        new_tasks = delete_task(tasks, args.task_id)
        if len(new_tasks) == len(tasks):
            print("Task not found, could not delete")
        else:
            tasks = new_tasks
            save_tasks(tasks)
    elif args.command == "list":
        if not tasks:
            print("No tasks found")
        else:
            lines = ["Tasks:"]
            for task in tasks:
                lines.append(
                    f'{task["task_id"]}: {task["title"]} [{"Complete" if task.get("complete", False) else "Pending"}]')
            print("\n".join(lines))
    else:
        parser.print_help()

if __name__ == '__main__':
    main()