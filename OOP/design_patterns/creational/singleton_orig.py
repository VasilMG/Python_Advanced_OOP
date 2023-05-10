#1vi nachin
class MyClass:
    __instance = None
    def __init__(self):
        if self.__instance is not None:
            raise TypeError('Singletons, cannot be created with init')

    @classmethod
    @property
    def instance(cls):
        if cls.__instance == None:
            cls.__instance = MyClass()
        return cls.__instance


class New_class:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance == None:
            cls.__instance = New_class()
        return cls.__instance

    @property
    def instance(cls):
        return cls.__instance

mc1 = New_class()

mc2 = New_class()
mc3 = New_class()
print(mc1 == mc2)
print(mc1)
print(mc2)
print(mc3)
