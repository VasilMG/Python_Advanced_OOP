from abc import ABC, abstractmethod

from abc import ABC, abstractmethod

#
# class Musician(ABC):
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age
#         self.skills = []
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         if value.strip() == "":
#             raise ValueError("Musician name cannot be empty!")
#         self.__name = value
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, value):
#         if value < 16:
#             raise ValueError("Musicians should be at least 16 years old!")
#         self.__age = value
#
#     @abstractmethod
#     def learn_new_skill(self, new_skill):
#         ...


class Musician(ABC):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.skills = []
        self.skill_set = []

    @abstractmethod
    def learn_new_skill(self, skill):
        if skill not in self.skill_set:
            raise ValueError(f"{skill} is not a needed skill!")
        elif skill in self.skills:
            raise Exception(f"{skill} is already learned!")
        self.skills.append(skill)
        return f"{self.name} learned to {skill}."

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '': # here I hadn't read the condition properly!!! 138/150
            raise ValueError("Musician name cannot be empty!")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 16:
            raise ValueError("Musicians should be at least 16 years old!")
        self.__age = value

