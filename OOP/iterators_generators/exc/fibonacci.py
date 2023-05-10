# better solution

# def fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a
#         b = a+b
#         yield b
#         a = a+b
#
# generator = fibonacci()
#
# for i in range(20):
#     print(next(generator))



# another solution
def fibonacci():
    n = 0
    p1 = 0
    p2 = 0
    while True:
        if n == 0:
            n += 1
            yield 0
            continue
        if n == 1:
            p2 = n
            n += 1
            yield 1
            continue
        value = p1 + p2
        p1 = p2
        p2 = value
        n += 1
        yield value