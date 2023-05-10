
def uppercase(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper


@uppercase
def get_name():
    '''An example for a very long and complex function that finally retirns some name'''
    return "Pesho"

@uppercase

def shopping_list():
    return 'eggs, milk, sugar'
print(get_name)
print(get_name())
print(shopping_list)
print(shopping_list())
print(get_name.__name__)