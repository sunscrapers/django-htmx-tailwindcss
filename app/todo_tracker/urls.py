from django.urls import path

from todo_tracker.ajax.todo_list import AjaxTaskCreateView
from todo_tracker.ajax.todo_list import AjaxTaskDeleteView
from todo_tracker.views.todo_list import TodoListView

app_name = "todo-tracker"
urlpatterns = [
    path("", TodoListView.as_view(), name="todo-list"),
    # Ajax views
    path("ajax/todo-list", AjaxTaskCreateView.as_view(), name="ajax-task-create"),
    path("ajax/todo-list/<int:task_id>", AjaxTaskDeleteView.as_view(), name="ajax-task-delete"),
]
