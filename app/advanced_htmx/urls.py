from django.urls import path

from advanced_htmx.ajax import CarCreateAjax
from advanced_htmx.ajax import RandomProductAjax
from advanced_htmx.ajax import RandomProductEventAjax
from advanced_htmx.ajax import TableProductsListAjax
from advanced_htmx.views import CarCreateView
from advanced_htmx.views import TableView

app_name = "advanced-htmx"
urlpatterns = [
    # Ajax
    path("ajax/products", TableProductsListAjax.as_view(), name="table-products-list-ajax"),
    path("ajax/product/random", RandomProductAjax.as_view(), name="product-random-ajax"),
    path("ajax/product/random/event", RandomProductEventAjax.as_view(), name="product-random-event-ajax"),
    path("ajax/car", CarCreateAjax.as_view(), name="car-create-ajax"),
    # Views
    path("", TableView.as_view(), name="table"),
    path("car", CarCreateView.as_view(), name="car-create"),
]
