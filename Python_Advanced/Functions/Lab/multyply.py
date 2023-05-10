def multiply(*args):
    product = 1
    for v in args:
        product *= v
    return product


print(multiply(1, 2, 330))
