# -*- coding: utf-8 -*-

from ziabpizza.models import Pizza
from ziabpizza.serializers import PizzaSerializer


class GetMenu(object):
    """
    Gets menu - a list of all :term:`Pizza`.
    .. literalinclude:: user_stories/get_menu.feature
      :language: gherkin
    .. versionadded:: 0.1.0
    """

    def __call__(self):
        """Method to call when a user wants to get :term:`Pizza` menu."""
        pizzas = Pizza.objects.all()
        serializer = PizzaSerializer(pizzas, many=True)
        return serializer.data
