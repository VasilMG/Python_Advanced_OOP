def fact(n):
    if n == 1:
        return 1
    if n == 0:
        return 1
    return  n * fact(n-1)

[print(fact(x)) for x in range(5) ]