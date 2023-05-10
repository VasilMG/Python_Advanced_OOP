class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.parents = ['penka', 'ganka']


    def __iter__(self):
        yield self.parents 

pesho = Person('Pesho', 92)
for x in pesho:
    print(x)