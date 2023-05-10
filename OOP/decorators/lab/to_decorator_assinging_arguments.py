
import sys
from functools import wraps


def log(filepath):
    DEFAULT_PATH = '.\\log.txt' 
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            std_out_original = sys.stdout
            with open(filepath, 'a') as file:
                sys.stdout = file 
                result = func(*args, **kwargs)
            sys.stdout = std_out_original
            return result
        return wrapper

    func = filepath if callable(filepath) else None
    filepath = filepath if not callable(filepath) else DEFAULT_PATH

    if func:
        return decorator(func)
    else:
        return decorator

@log(filepath = '.\\log.txt')
def say_hello(name):
    print(f'Hello, {name} how are you')

say_hello('pesho')
