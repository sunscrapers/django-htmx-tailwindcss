from typing import List

import pytest
from faker import Faker

from todo_tracker.models import Task

fake = Faker()


@pytest.fixture
def fake_tasks():
    tasks: List[Task] = []

    for _ in range(10):
        task: Task = Task(value=fake.word())
        tasks.append(task)

    Task.objects.bulk_create(tasks)
    return tasks
