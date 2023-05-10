from project.rooms.room import Room
from project.appliances.tv import TV

class AloneYoung(Room):
    MEMBERS_COUNT = 1

    def __init__(self, family_name: str, salary: float, members_count=MEMBERS_COUNT):

        super().__init__(family_name,salary,members_count)
        self.budget = salary
        self.room_cost = 10
        self.appliances = [TV()]
        self.expenses = self.calculate_expenses(self.appliances)
 


