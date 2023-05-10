class StrMixin: 
    str_delimeter = '; '
    def __str__(self):
        return self.str_delimeter.join(f'{k} = {v}' for k, v in self.__dict__.items())

class Person(StrMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Building(StrMixin):
    str_delimeter = '-->'
    def __init__(self, name, address):
        self.name = name
        self.address = address


p = Person('Goosho', 92)
b = Building('Blok','ulica')
print(p)
print(b)
