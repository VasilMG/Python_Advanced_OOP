from wild_zoo.project import Product
class Drink(Product):
    def __init__(self, name, quantity = 15):
        super().__init__(name, quantity=10)
