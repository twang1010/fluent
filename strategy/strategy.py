# doc Test must be at the begining of the script
# better use """ and """ to include doctest, although triple single quote works

"""
>>> joe = Customer('John Doe', 0)
>>> ann = Customer('Ann Smith', 1100)
>>> cart = [LineItem('banana', 4, .5),
...         LineItem('apple', 10, 1.5),
...         LineItem('watermelon', 5, 5.0)]
>>> banana_cart = [LineItem('banana', 30, .5),
... LineItem('apple', 10, 1.5)]
>>> long_order = [LineItem(str(item_code), 1, 1.0)
... for item_code in range(10)]

>>> Order(joe, long_order, best_promotion)
<Order total: 10.00 due 9.30>
>>> Order(joe, banana_cart, best_promotion)
<Order total: 30.00 due 28.50>
>>> Order(ann, cart, best_promotion)
<Order total: 42.00 due 39.90>
"""

import inspect
from collections import namedtuple

import promotions

Customer = namedtuple('Customer', 'name fidelity')


class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.__total - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due {:.2f}>'
        return fmt.format(self.total(), self.due())


def best_promotion(order):
    return max(promo(order) for promo in promotions.registry)
