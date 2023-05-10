from functools import wraps

def cache(func):
    the_log = {}
    @wraps(func)
    def wrapper(*args, **kwargs): 
        func.log = the_log
        key = args[0]
        if key not in the_log:
            the_log[key] = func(*args, **kwargs)
        return the_log[key]
    wrapper.log = the_log  
    return wrapper
@cache
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(4))

print(fibonacci.log)