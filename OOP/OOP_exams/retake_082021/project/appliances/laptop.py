from project.appliances.appliance import Appliance


class Laptop(Appliance):
    LAPTOP_COST = 1

    def __init__(self, cost=LAPTOP_COST):
        super().__init__(cost)
