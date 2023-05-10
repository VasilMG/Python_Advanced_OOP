from wild_zoo.project import MainDish
class Salmon(MainDish):
    GRAMS = 22
    def __init__(self, name, price, grams = GRAMS):
        super().__init__(name, price, grams = self.GRAMS)

