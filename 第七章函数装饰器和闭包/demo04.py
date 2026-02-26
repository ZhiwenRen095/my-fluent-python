"""设计模式之策略模式：装饰器实现"""
from abc import ABC, abstractmethod
from typing import NamedTuple
import uuid

promos = []


def promotion(promo_func):
    promos.append(promo_func)
    return promo_func


class Customer(NamedTuple):
    name: str = "default_user_name_" + str(uuid.uuid4())
    fidelity: int = 0


class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:  # 上下文
    def __init__(self, customer: Customer, cart: list, promotion=None):
        self.__total = None
        self.customer = customer
        self.cart = cart
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
        return self.total() - discount

    def __repr__(self) -> str:
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


@promotion
def fidelity(order):
    """为积分为1000或以上的顾客提供5%折扣"""

    return order.total() * .05 if order.customer.fidelity >= 1000 else 0


@promotion
def bulk_item(order):
    """单个商品为20个或以上时提供10%折扣"""

    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount


@promotion
def large_order(order):
    """订单中的不同商品达到10个或以上时提供7%折扣"""

    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0


def best_promo(order):
    return max(promo(order) for promo in promos)


if __name__ == '__main__':
    ann = Customer(name='Ann Smith', fidelity=1100)
    cart = [
        LineItem('banana', 4, .5),
        LineItem('apple', 10, 1.5),
        LineItem('watermellon', 5, 5.0)
    ]
    print(Order(ann, cart, best_promo))
