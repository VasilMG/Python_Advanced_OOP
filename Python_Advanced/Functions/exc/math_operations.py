

def math_operations(*args, **kwargs):
    counter = 0
    ll = [*args]
    dd = kwargs
    for item in range(len(ll)):
        number = ll[0]
        if counter == 0:
            dd["a"] += number
            ll.remove(number)
            counter += 1
        elif counter == 1:
            dd['s'] -= number
            ll.remove(number)
            counter +=1
        elif counter == 2:
            if number == 0:
                ll.remove(number)
                counter += 1
                continue
            dd['d'] /= number
            counter += 1
            ll.remove(number)
        elif counter == 3:
            dd['m'] *= number
            ll.remove(number)
            counter = 0

    result = [f"{key}: {value:.1f}" for key, value in sorted(dd.items(), key= lambda x: (-x[1], x[0]))]
    print(result)
    return '\n'.join(result)


print(math_operations(6.0, a=0, s=0, d=5, m=0))


# print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-
#
# 2.3), d=0, m=0))


# print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7,
#
# d=33, m=15))