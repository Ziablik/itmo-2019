# -*- coding: utf-8 -*-

from ziabpizza.logic.cooking import count_cooking_time
from ziabpizza.logic.mail import send_mail_on_order
from ziabpizza.models import Order
from ziabpizza.serializers import OrderSerializer


class PostOrder(object):
    """
    Posts new :term:`Order`.

    .. literalinclude:: user_stories/post_order.feature
      :language: gherkin

    .. versionadded:: 0.1.0
    """

    def __call__(self, incoming_data):
        """Method to call when a user wants to put an :term:`Order`."""
        serializer = OrderSerializer(data=incoming_data)
        if serializer.is_valid():
            serializer.save()
            order = Order.objects.get(pk=serializer.data['id'])
            order.cooking_time = count_cooking_time(order.creation_date)
            order.save()
            send_mail_on_order(order)
        return serializer.data, serializer.errors
