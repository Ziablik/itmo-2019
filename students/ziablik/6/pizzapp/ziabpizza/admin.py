from django.contrib import admin

from .models import Ingredient, Order, Pizza   # noqa: I001

admin.site.register(Ingredient)
admin.site.register(Order)
admin.site.register(Pizza)
