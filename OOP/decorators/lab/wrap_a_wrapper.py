
from functools import wraps
def uppercase(func):
    @wraps(func)
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

print(get_name.__name__)
