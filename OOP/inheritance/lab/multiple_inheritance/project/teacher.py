from wild_zoo.project import Person
from wild_zoo.project import Employee
class Teacher(Person, Employee):
    def teach(self):
        return 'teaching...'