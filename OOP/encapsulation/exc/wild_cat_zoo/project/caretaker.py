from wild_zoo.project import Worker
class Caretaker(Worker):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)