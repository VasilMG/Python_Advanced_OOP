def singleton(cls):
    instance = None
    def wrapper(*args, **kwargs):
        nonlocal instance
        if instance == None:
            instance = cls(*args, **kwargs)
            return instance
        return instance
    return wrapper

@singleton
class MyClass:
    pass

mc1 = MyClass()
mc2 = MyClass()
print(mc1)
print(mc2)



