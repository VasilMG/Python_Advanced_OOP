import abc
from abc import abstractmethod

class Sorter(abc.ABC):
    # TEMPLATE METHOD. TO MAKE AND ABSTRACT METHOND WHICH THE NESTED CLASSES WILL USE
    @abstractmethod
    def key_func(self):
        pass

    def sort(self, elements):
        return sorted(elements, key=self.key_func)

class NaturalSorter(Sorter):
    def key_func(self, value):
        return value

class ByDivisionSorter(Sorter):
    def __init__(self, base):
        self.base = base

    def key_func(self, value):
        return value % self.base, value 


ns = NaturalSorter()
bds = ByDivisionSorter(3)

value = [1, 9, 2, 91, 85, 80]
print(ns.sort(value))
print(bds.sort(value))