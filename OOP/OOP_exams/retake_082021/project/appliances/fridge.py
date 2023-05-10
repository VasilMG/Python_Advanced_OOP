from project.appliances.appliance import Appliance

class Fridge(Appliance):
    FRIDGE_COST = 1.2

    def __init__(self, cost=FRIDGE_COST):
        super().__init__(cost)
