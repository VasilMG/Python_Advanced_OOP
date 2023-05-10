import itertools
test_list = [1, 2, 3]
def p(the_list):
    x = list(itertools.permutations(the_list))
    for i in x:
        print(list(i))

p(test_list)