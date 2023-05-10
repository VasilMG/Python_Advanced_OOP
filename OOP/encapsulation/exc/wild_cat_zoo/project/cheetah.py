from wild_zoo.project import Animal
class Cheetah(Animal):
    def __init__(self, name, gender, age, money_for_care = 60):
        super().__init__(name, gender, age, money_for_care=60)