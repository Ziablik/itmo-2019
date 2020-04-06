# -*- coding: utf-8 -*-

from django.urls import path    # noqa: I001

from ziabpizza.views import get_pizza, get_statistics, post_order

urlpatterns = [
    path('pizza/', get_pizza),
    path('order/', post_order),
    path('statistics/pizza/', get_statistics),
]
