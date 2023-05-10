from abc import ABC, abstractmethod


class Room(ABC):
    def __init__(self, name: str, budget: float, members_count: int, expenses=0):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
   
        self.expenses = expenses

        
    @property
    def expenses(self):
        return self.__expenses
    
    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value


    def calculate_expenses(self, *args):
        result = 0
        for index in args:
            for item in index:
                result += item.get_monthly_expense()
        
        return result
