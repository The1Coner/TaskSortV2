from TaskSort.tasks import add_task, complete_task, delete_task

def test_add_task():
    tasks = []
    add_task(tasks, "Test")
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Test"

def test_complete_task():
    tasks = [{"task_id": 1, "title": "Test", "complete": False}]
    result = complete_task(tasks, 1)
    assert result is True
    assert tasks[0]["complete"] is True

def test_delete_task():
    tasks = [{"task_id": 1, "title": "Test"}]
    new_tasks = delete_task(tasks, 1)
    assert len(new_tasks) == 0