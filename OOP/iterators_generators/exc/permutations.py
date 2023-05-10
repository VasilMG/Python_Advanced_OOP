import itertools

def possible_permutations(the_list):
    x = list(itertools.permutations(the_list))
    for i in x:
        yield list(i)

# [print(n) for n in possible_permutations([1, 2, 3])]

[print(n) for n in possible_permutations([1])]