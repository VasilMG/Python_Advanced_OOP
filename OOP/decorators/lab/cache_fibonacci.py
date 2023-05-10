from functools import wraps
from time import process_time_ns
from accepting_args import measure_time
def cache(func):
    chached_values = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = args + tuple(kwargs.items())
        if key not in chached_values:
            chached_values[key] = func(*args, **kwargs)
        return chached_values[key]
    return wrapper

@measure_time
@cache
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))



