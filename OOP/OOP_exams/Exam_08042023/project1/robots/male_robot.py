from project1.robots.base_robot import BaseRobot


class MaleRobot(BaseRobot):
    INITIAL_WEIGHT = 9

    def __init__(self, name: str, kind: str, price: float, weight=INITIAL_WEIGHT):
        super().__init__(name, kind, price, weight)

    def eating(self):
        self.weight += 3

