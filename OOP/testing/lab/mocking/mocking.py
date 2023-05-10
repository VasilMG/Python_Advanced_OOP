from testing.lab.mocking import name_validators


class Person:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    @property
    def first(self):
        return self.__first

    @first.setter
    def first(self, value):
        if name_validators.validate_name(value):
            self.__first = value

    @property
    def last(self):
        return self.__last

    @last.setter
    def last(self, value):
        if name_validators.validate_name(value):
            self.__last = value

    @property
    def get_full_name(self):
        return f'{self.__first} {self.__last}'

    def get_info(self):
        return f'{self.__first} {self.__last} is {self.age} years old.'

