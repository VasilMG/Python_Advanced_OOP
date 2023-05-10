# [ - literal for list comherensions
# { - literal for dict comherensions
# ( - literal for generator comherensions

def print_values_iter(iterable):
    for value in iterable:
        print(value)


def gen_fund(n):
    for x in range(n):
        yield x

print_values_iter(gen_fund(5))
print_values_iter((x for x in range(5))) #---> generator comprehension


