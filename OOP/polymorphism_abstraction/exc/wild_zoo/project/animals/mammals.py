from abc import ABC, abstractmethod
from wild_zoo.project import Mammal


class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if food.__class__.__name__ == "Meat" or food.__class__.__name__ == "Seed":
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * 0.1
        self.food_eaten += food.quantity

class Dog(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if food.__class__.__name__ != "Meat":
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * 0.40
        self.food_eaten += food.quantity

class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if food.__class__.__name__ == "Fruit" or food.__class__.__name__ == "Seed":
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * 0.30
        self.food_eaten += food.quantity

class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if food.__class__.__name__ != "Meat":
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * 1.00
        self.food_eaten += food.quantity