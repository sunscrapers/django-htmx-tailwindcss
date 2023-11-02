from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class ColorChoices(models.TextChoices):
    WHITE = "White", _("White")
    SILVER = "Silver", _("Silver")
    YELLOW = "Yellow", _("Yellow")
    BLUE = "Blue", _("Blue")
    RED = "Red", _("Red")
    GREEN = "Green", _("Green")
    BLACK = "Black", _("Black")
    OTHER = "Other", _("Other")


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=False, null=False)
    color = models.CharField(
        max_length=10,
        choices=ColorChoices.choices,
        default=ColorChoices.OTHER.value,
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False, null=False)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.00"))],
    )
    photo = models.ImageField(upload_to="cars")

    def __str__(self):
        return self.name
