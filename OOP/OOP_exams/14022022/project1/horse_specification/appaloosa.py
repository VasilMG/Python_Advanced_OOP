from project1.horse_specification.horse import Horse

class Appaloosa(Horse):
    MAX_SPEED = 120
    def __init__(self, name, speed):
        super().__init__(name, speed)


    def train(self):
        new_speed = self.speed + 2
        if new_speed > self.MAX_SPEED:
            self.speed = self.MAX_SPEED
        else:
            self.speed = new_speed

