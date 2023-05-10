from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.stove import Stove

class OldCouple(Room):
    MEMBERS = 2

    def __init__(self, family_name: str, pension_one: float, pension_two: float):

        super().__init__(
            family_name,
            budget=pension_one + pension_two,
            members_count = self.MEMBERS
        )
        self.budget = pension_one + pension_two
        self.room_cost = 15
        self.appliances = self.MEMBERS * [TV(), Fridge(), Stove()]
        self.expenses = self.calculate_expenses(self.appliances)

