class Person:
    def __init__(self, name, age):
        self.name = name  
        self.age = age 

    def increase_age(self):
        self.age += 1

p = Person('Gosho', 92)
print(p.age)
p.increase_age()
print(p.age)