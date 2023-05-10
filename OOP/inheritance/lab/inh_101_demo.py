class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Teacher(Person):
    pass

t = Teacher('Gosho', 92) 
print(t.name)
print(t.age)
