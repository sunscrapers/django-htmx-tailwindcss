from django.contrib import admin

from advanced_htmx.models import Car
from advanced_htmx.models import Category
from advanced_htmx.models import Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "color", "category", "price")


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("name", "price")
    search_fields = ("name",)
