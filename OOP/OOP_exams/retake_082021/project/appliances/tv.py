from project.appliances.appliance import Appliance


class TV(Appliance):
    TV_COST = 1.5

    def __init__(self, cost=TV_COST):
        super().__init__(cost)
