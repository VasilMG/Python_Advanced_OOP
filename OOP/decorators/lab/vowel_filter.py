from functools import wraps


def vowel_filter(func):
    @wraps(func)
    def wrapper():
        vowels = 'eyuioa'
        result = func()
        return [x.lower() for x in result if x in vowels]
    return wrapper

@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())