from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import ListView

from todo_tracker.models import Task


class AjaxTaskCreateView(CreateView, ListView):
    model = Task
    http_method_names = ["post"]
    fields = [
        "value",
    ]
    template_name = "partials/tasks_list.html"

    paginate_by = 25
    object_list = Task.objects.order_by("-created_at")

    def get_success_url(self):
        # Not used, required by Django generic view
        return "/"

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        return render(
            request,
            self.template_name,
            context=self.get_context_data(),
        )


class AjaxTaskDeleteView(DeleteView):
    model = Task
    pk_url_kwarg = "task_id"
    http_method_names = ["post"]

    def get_success_url(self):
        # Not used, required by Django generic view
        return "/"

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        return HttpResponse()
