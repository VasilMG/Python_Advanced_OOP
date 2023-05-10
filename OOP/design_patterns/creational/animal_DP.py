from abc import  ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_noise(self):
        pass

class Cat(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_noise(self):
        return 'myow'

class Dog(Animal):
    def __init__(self, name):
        self.name = name

'''
cat Pesjo 7
dog Sharo
cat Pusss 5
'''

while True:
    type, * others = input().split()
    animal = animal_factory.create(type, *others)
    # creates an abstraction to create the classes like this
