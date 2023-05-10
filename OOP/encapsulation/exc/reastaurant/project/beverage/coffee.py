from wild_zoo.project import HotBeverage
class Coffee(HotBeverage):
    MILLILITERS = 50
    PRICE = 3.50
    def __init__(self, name, caffeine: float, price = PRICE, milliliters = MILLILITERS):
        super().__init__(name, price = self.PRICE, milliliters = self.MILLILITERS)
        self.__caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine

