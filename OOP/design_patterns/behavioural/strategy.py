import abc
from abc import abstractmethod

class SortStrategy(abc.ABC):
    @abstractmethod
    def get_key_func(self, *args, **kwargs):
        pass
class NaturalSorterStrategy(SortStrategy):
    def __key_func(self, value):
        return value
    def get_key_func(self, *args, **kwargs):
        return self.__key_func

class Sorter:
    sort_strategy = NaturalSorterStrategy()
    def sort(self, elements):
        return sorted(elements, key=self.sort_strategy.get_key_func())


class ByDivisionSorterStrategy(SortStrategy):
    def __init__(self, base):
        self.base = base

    def __key_func(self, value):
        return value % self.base, value
    def get_key_func(self, *args, **kwargs):
        return self.__key_func


s = Sorter()

value = [1, 9, 2, 91, 85, 80]
print(s.sort(value))
s.sort_strategy = ByDivisionSorterStrategy(3)
print(s.sort(value))
