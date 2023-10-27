from typing import Any
from typing import Dict

from django.views.generic import TemplateView
from django.views.generic.list import ListView

from advanced_htmx.handlers import ChatHandler
from advanced_htmx.models import Product


class TableView(ListView):
    model = Product
    template_name = "advanced_htmx/table.html"

    paginate_by = 10
    queryset = Product.objects.select_related("category").order_by("id")


class CarCreateView(TemplateView):
    template_name = "advanced_htmx/car_create.html"


class ChatView(TemplateView):
    template_name = "advanced_htmx/chat.html"

    def get_context_data(self, *args, **kwargs):
        ctx: Dict[str, Any] = super().get_context_data(*args, **kwargs)
        ctx["messages"] = ChatHandler.get_messages_data()

        return ctx
