from wild_zoo.project import Vehicle
from wild_zoo.project import Car
class FamilyCar(Car):
    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

vehicle = Vehicle(50, 150)

print(Vehicle.DEFAULT_FUEL_CONSUMPTION)

print(FamilyCar.DEFAULT_FUEL_CONSUMPTION)

print(vehicle.fuel)

print(vehicle.horse_power)

print(vehicle.fuel_consumption)

vehicle.drive(100)

print(vehicle.fuel)

family_car = FamilyCar(150, 150)

family_car.drive(50)

print(family_car.fuel)

family_car.drive(50)

print(family_car.fuel)

print(family_car.__class__.__bases__[0].__name__)