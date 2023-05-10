from abc import ABC, abstractmethod


class Car(ABC):
    FUEL_CONSUMPTION = 0


    def __init__(self, make, model, years_old):
        self.years_old = years_old
        self.model = model
        self.make = make

    def consumption(self):
        return self.FUEL_CONSUMPTION * (self.years_old // 10)

class SportsCar(Car):
    FUEL_CONSUMPTION = 10

    def __init__(self, make, model, years_old=10):
        super().__init__(make, model, years_old)

    @property
    def years_old(self):
        return self.__years_old

    @years_old.setter
    def years_old(self, value):
        if value < 0:
            raise Exception('Cannnot be')
        # if value == None:
        #     value = 10
        self.__years_old = value



f = SportsCar('Audi', 'A6', -1)
