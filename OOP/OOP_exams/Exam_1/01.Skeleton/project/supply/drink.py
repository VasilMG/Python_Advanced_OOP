from project.supply.supply import Supply

class Drink(Supply):
    def __init__(self, name, energy= 15):
        super().__init__(name, energy)
        self.type = 'Drink'

    def details(self):
        return f"{self.type}: {self.name}, {self.energy}"