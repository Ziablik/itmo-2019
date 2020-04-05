# -*- coding: utf-8 -*-

from django.test import TestCase
from django.test import Client
from .models import Ingredient, Pizza, Order
from decimal import Decimal


def create_test_ingredient(name):
    """Creates :term:`Ingredient` object for test purposes."""
    ingredient = Ingredient(name=name)
    ingredient.save()
    return ingredient


def create_test_pizza(name, price, ingredient_list):
    """Creates :term:`Pizza` object for test purposes."""
    pizza = Pizza(
        name=name,
        price=price,
    )
    pizza.save()
    pizza.ingredient_list.set(ingredient_list)
    return pizza


def create_test_order(pizza_list, delivery_address, client_email):
    """Creates :term:`Order` object for test purposes."""
    order = Order(
        delivery_address=delivery_address,
        client_email=client_email,
    )
    order.save()
    order.pizza_list.set(pizza_list)
    return order


class GetMenuTest(TestCase):
    client = Client()

    def setUp(self):
        """Create 2 test :term:`Ingredient` and :term:`Pizza`."""
        ingredient_test = create_test_ingredient('test')
        ingredient_cheese = create_test_ingredient('cheese')

        self.pizza = create_test_pizza(name='Test with cheese',
                                       price=Decimal(1.00),
                                       ingredient_list=[ingredient_cheese,
                                                        ingredient_test])

    def test_can_get_menu(self):
        """Check that API returns list of :term:`Pizza`."""
        response = self.client.get(path='/api/pizza')
        assert response.status_code == 200


class PostOrderTest(TestCase):
    client = Client()

    def setUp(self):
        """Create 2 test :term:`Ingredient` and :term:`Pizza`."""
        ingredient_test = create_test_ingredient('test')
        ingredient_cheese = create_test_ingredient('cheese')

        self.pizza = create_test_pizza(name='Test with cheese',
                                       price=Decimal(1.00),
                                       ingredient_list=[ingredient_cheese,
                                                        ingredient_test])

    def test_can_post_order(self):
        """Make POST request and assert that :term:`Order` is saved in database and email is sent."""
        response = self.client.post(path='api/order',
                                    data={
                                        'status': 'accept',
                                        'pizza_list': [self.pizza.pk],
                                        'delivery_address': 'Kronverskiy prospect, Russia',
                                        'client_email': 'ziablikl@mail.ru',
                                    })
        assert response.status_code == 200

    def test_cannot_post_invalid_order(self):
        """Make POST request with invalid params and assert that :term:`Order` is not saved in database."""
        response = self.client.post(path='api/order',
                                    data={
                                        'pizza_list': [],
                                        'delivery_address': 'Kronverskiy prospect, Russia',
                                        'client_email': 'ziablikl@mail.ru',
                                    })
        assert response.status_code == 200


class GetStatisticsTest(TestCase):
    client = Client()

    def setUp(self):
        """Make test :term:`Order`."""
        self.order = create_test_order(
            pizza_list=[create_test_pizza(
                name='bacon with pepper',
                price=Decimal(1.00),
                ingredient_list=[
                    create_test_ingredient('bacon'),
                    create_test_ingredient('pepper'),
                ]
            )],
            delivery_address='Kronverskiy prospect, Russia',
            client_email='ziablikl@mail.ru',
        )

    def test_can_get_statistics(self):
        """Make GET request and check status code and :term:`Pizza` list."""
        response = self.client.get(path='/api/statistics/pizza')
        assert response.status_code == 200
