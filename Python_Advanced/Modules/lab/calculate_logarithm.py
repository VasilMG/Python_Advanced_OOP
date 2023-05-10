from math import log, e

value = int(input())
base = input()

if base.isdigit():
    print(log(value, int(base)))
else:
    print(log(value))