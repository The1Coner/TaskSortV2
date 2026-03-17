# TaskSort
TaskSort is a simple CLI task manager written in Python.
It lets you add, complete, delete, and list tasks that are stored locally in a JSON file.
## Features
- Add Tasks
- Mark tasks as "complete"
- Delete tasks
- List tasks
- Persistent JSON storage
- CLI using argparse
- Unit tests with pytest
## Requirements
Python 3.10+
## Structure
    TaskSort/
        main.py     # CLI
        tasks.py    # task logic
        storage.py  # save and load json
    tests/
        test_tasks.py   # unit tests
## How to run it
Open the root directory in the terminal, and run `python TaskSort/main.py <command>`
## Example commands
`python main.py add "Task 1"`

`python main.py list`

`python main.py complete 1`

`python main.py delete 1`
## Running tests
`python -m pytest`
