from time import time 
from functools import wraps
def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time()
        print(start_time)
        result = func(*args, **kwargs)
        end_time = time()
        print(end_time)
        difference = end_time - start_time
        print(f"{func.__name__} executed in {difference} time")
        return result
    return wrapper
@measure_time
def sum_two(x, y):
    return x + y
ll= [1, 2, 3, 4, 8, 8, 8, 8]

the_set= {1, 2, 3, 4, 8, 8 , 8 , 8 }
@measure_time
def get_item(item):
    return [x * 2 for x in item]

print(sum_two(5, 6))
print(get_item(ll))

@measure_time
def fullname(first_name, last_name):
    return first_name + " " + last_name

print(fullname('pesho', 'petrov'))



