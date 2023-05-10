def even_odd(*args):
    command = args[-1]
    if command == 'even':
        the_list = [x for x in args if isinstance(x, int) and x % 2 == 0]
    else:
        the_list = [x for x in args if isinstance(x, int) and x % 2 != 0]
    return the_list

print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
