from django.template.response import TemplateResponse
from django.views.generic import TemplateView
from django.views.generic.list import ListView

from advanced_htmx.models import Product


class TableProductsListAjax(ListView):
    template_name = "advanced_htmx/partials/table_products_list.html"

    model = Product
    queryset = Product.objects.select_related("category").order_by("id")
    paginate_by = 10

    def get(self, request, *args, **kwargs) -> TemplateResponse:
        response: TemplateResponse = super().get(request, *args, **kwargs)
        response["HX-Trigger"] = "products-list-page-changed"
        return response


class RandomProductAjax(TemplateView):
    template_name = "advanced_htmx/mini_partials/product_random.html"

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx["random_product"] = Product.objects.order_by("?").first()
        return ctx


class RandomProductEventAjax(RandomProductAjax):
    template_name = "advanced_htmx/mini_partials/product_random_event.html"
