from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def refuel(self):
        pass

class Car(Vehicle):
    def __init__(self,fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        consumption = (self.fuel_consumption + 0.9) * distance
        if consumption <= self.fuel_quantity:
            self.fuel_quantity -= consumption

    def refuel(self, quantity):
        self.fuel_quantity += quantity


class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        consumption = (self.fuel_consumption + 1.6) * distance
        if consumption <= self.fuel_quantity:
            self.fuel_quantity -= consumption
    def refuel(self, quantity):
        self.fuel_quantity += quantity * 0.95


truck = Truck(100, 15)

truck.drive(5)

print(truck.fuel_quantity)

truck.refuel(50)

print(truck.fuel_quantity)