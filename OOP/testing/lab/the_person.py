class Person:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
    @property
    def get_full_name(self):
        return f'{self.first} {self.last}'

    def get_info(self):
        return f'{self.first} {self.last} is {self.age} years old.'