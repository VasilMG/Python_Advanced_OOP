from abc import  ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_noise(self):
        pass

class Cat:
    kind = 'cat'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_noise(self):
        return 'myow'

class Dog:
    kind = 'dog'
    def __init__(self, name):
        self.name = name
    def make_noise(self):
        return 'bow'

'''
cat Pesjo 7
dog Sharo
cat Pusss 5
'''
#
# while True:
#     type, * others = input().split()
#     if type == 'cat':
#         Cat(*others)
#     else:
#         Dog(*others)
