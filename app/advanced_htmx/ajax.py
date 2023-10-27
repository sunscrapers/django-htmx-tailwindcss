from django.http import HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views.generic import CreateView
from django.views.generic import FormView
from django.views.generic import TemplateView
from django.views.generic.list import ListView

from advanced_htmx.forms import ChatMessageForm
from advanced_htmx.handlers import ChatHandler
from advanced_htmx.handlers import ChatMessage
from advanced_htmx.models import Car
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


class CarCreateAjax(CreateView):
    model = Car
    fields = ("name", "price", "photo")
    template_name = "advanced_htmx/partials/car_create.html"
    success_template_name = "advanced_htmx/partials/success_car_create.html"

    def form_valid(self, request, form):
        return render(
            self.request,
            self.success_template_name,
        )

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(request, form)
        else:
            return self.form_invalid(form)


class ChatAjax(FormView):
    template_name = "advanced_htmx/partials/chat_messages_form.html"
    http_method_names = ["post"]
    form_class = ChatMessageForm

    def form_valid(self, form):
        message: ChatMessage = ChatMessage(
            signature=form.cleaned_data["signature"],
            text=form.cleaned_data["text"],
        )
        ChatHandler.save_message(message=message)

        return HttpResponse(status=204)
