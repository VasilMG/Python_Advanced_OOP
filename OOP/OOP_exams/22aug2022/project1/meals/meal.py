from abc import ABC, abstractmethod


class Meal(ABC):
    def __init__(self, name: str, price: float, quantity: int):
        self.quantity = quantity
        self.price = price
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Name cannot be an empty string!")
        self.__name  = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError( "Invalid price!")
        self.__price = value

    @abstractmethod
    def details(self):
        pass
