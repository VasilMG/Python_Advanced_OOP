class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return ', '.join([f'{k}: {v}' for k, v in self.__dict__.items()])
class Employee(Person): 
    def __init__(self, name, age, field):
        super().__init__(name, age)  
        self.field = field

class Teacher(Employee): 
    def __init__(self, name, age, field, subject):
        super().__init__(name, age, field) 
        self.subject = subject

print(Teacher('Pesho', 92, 'mathematics', 'Math'))