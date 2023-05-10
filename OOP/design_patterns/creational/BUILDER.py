class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '; '.join(f'{key} = {value}' for key, value in self.__dict__.items())

class PersonBuilder:
    person_attrs = {'name': 'Pesho', 'age': 96}  
    def set_name(self, name):
        self.person_attrs['name'] = name

    def set_age(self, age):
        self.person_attrs['age'] = age

    def build(self):
        return Person(**self.person_attrs)

builder = PersonBuilder()
print(builder.build())


