from .dough import Dough
from .topping import Topping


class Pizza:
    def __init__(self, name: str, dough: Dough, toppings_capacity: int, toppings = {}):
        self.name = name
        self.dough = dough
        self.toppings_capacity = toppings_capacity
        self.toppings = toppings

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or value == '':
            raise ValueError("The name cannot be an empty string")
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if value is None:
            raise ValueError("You should add dough to the pizza")
        self.__dough = value

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, value):
        if value <= 0 or not isinstance(value, int):
            raise ValueError("The topping's capacity cannot be less or equal to zero")
        self.__toppings_capacity = value

    def add_topping(self, topping: Topping):
        if len(self.toppings) >= self.__toppings_capacity:
            raise ValueError("Not enough space for another topping")
        elif topping.topping_type not in self.toppings:
            self.toppings[topping.topping_type] = topping.weight
        else:
            self.toppings[topping.topping_type] += topping.weight

    def calculate_total_weight(self):
        # print(self.dough.weight)
        total_weight = self.dough.weight + sum([self.toppings[x] for x in self.toppings.keys()])
        return total_weight
