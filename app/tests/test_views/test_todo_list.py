from typing import List

from django.template.response import TemplateResponse
from django.test.client import Client
from django.urls import reverse

from todo_tracker.models import Task


def test_get_todo_list(client: Client, fake_tasks: List[Task]):
    url: str = reverse("todo-tracker:todo-list")
    response: TemplateResponse = client.get(url)

    assert response.status_code == 200
    for task in fake_tasks:
        assert task.value in response.rendered_content
