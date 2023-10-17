from django.views.generic.list import ListView

from todo_tracker.models import Task


class TodoListView(ListView):
    model = Task
    template_name = "todo_list.html"

    paginate_by = 25
    queryset = Task.objects.order_by("-created_at")
