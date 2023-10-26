from django.views.generic import TemplateView
from django.views.generic.list import ListView

from advanced_htmx.models import Product


class TableView(ListView):
    model = Product
    template_name = "advanced_htmx/table.html"

    paginate_by = 10
    queryset = Product.objects.select_related("category").order_by("id")


class CarCreateView(TemplateView):
    template_name = "advanced_htmx/car_create.html"
