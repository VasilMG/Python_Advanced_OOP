from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop

class YoungCouple(Room):
    MEMBERS = 2

    def __init__(self, family_name: str, salary_one: float, salary_two: float):
        super().__init__(
            family_name,
            budget= salary_one + salary_two,
            members_count=self.MEMBERS)
        self.room_cost = 20
        self.appliances = self.members_count * [TV(), Fridge(), Laptop()]
        self.expenses = self.calculate_expenses(self.appliances)


