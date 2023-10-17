from typing import Dict
from typing import List
from urllib.parse import urlencode

from django.http.response import HttpResponse
from django.template.response import TemplateResponse
from django.test.client import Client
from django.urls import reverse

from todo_tracker.models import Task


def test_create_todo_task(client: Client, fake_tasks: List[Task]):
    url: str = reverse("todo-tracker:ajax-task-create")

    data: Dict[str, str] = {"value": "Go outside!"}
    response: TemplateResponse = client.post(
        url,
        data=urlencode(data),
        content_type="application/x-www-form-urlencoded",
    )

    assert response.status_code == 200

    task: Task = Task.objects.filter(value="Go outside!").first()
    assert task
    assert task.value in str(response.content)
    for fake_task in fake_tasks:
        assert fake_task.value in str(response.content)


def test_delete_todo_task(client: Client, fake_tasks: List[Task]):
    original_tasks_count: int = Task.objects.count()
    url: str = reverse("todo-tracker:ajax-task-delete", kwargs={"task_id": fake_tasks[0].id})

    response: HttpResponse = client.post(url)

    changed_tasks_count: int = Task.objects.count()
    assert response.status_code == 200
    assert changed_tasks_count == original_tasks_count - 1
