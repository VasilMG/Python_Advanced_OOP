import time
from functools import wraps
from random import random


def retry(retry_count, retry_timeout):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            the_exception = None
            for i in range(retry_count):
                try:
                    return func(*args, **kwargs)
                except Exception as Ex:
                    print(f'Try {i + 1} failed. Retying...')
                    the_exception = Ex
                    time.sleep(retry_timeout)

            raise the_exception
        return wrapper
    return decorator

@retry(3, 1)
def fail(chance):
    value = random()

    if value < chance:
        raise Exception('It Fails')
    else:
        return "it Works"

print(fail(0.9))