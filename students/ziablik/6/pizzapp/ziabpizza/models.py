# -*- coding: utf-8 -*-

from django.db import models


class Ingredient(models.Model):
    """A model that describes :term:`Ingredient` object."""

    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        """Returns string representation of :term:`Ingredient`."""
        return self.name


class Pizza(models.Model):
    """A model that describes :term:`Pizza` object."""

    name = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(
        decimal_places=2,
        max_digits=8,
    )
    ingredient_list = models.ManyToManyField(Ingredient)

    def __str__(self):
        """Returns string representation of :term:`Pizza`."""
        return self.name


class Order(models.Model):
    """A model that describes :term:`Order` object."""

    creation_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('accept', 'accept'),
            ('preparation', 'preparation'),
            ('delivery', 'delivery'),
            ('done', 'done'),
        ],
        default='accept',
    )
    pizza_list = models.ManyToManyField(Pizza)
    delivery_address = models.CharField(max_length=100)
    client_email = models.EmailField(max_length=50)
    email_is_sent = models.BooleanField(default=False)

    def __str__(self):
        """Returns string representation of :term:`Order`."""
        return 'Created: {0}, status: {1}'.format(
            self.creation_date,
            self.status,
        )
