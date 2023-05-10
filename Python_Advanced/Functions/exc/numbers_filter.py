def even_odd_filter(**kwargs):
    for key, value in kwargs.items():
        if key == 'odd':
            kwargs[key] = [x for x in value if x % 2 != 0]
        elif key == 'even':
            kwargs[key] = [x for x in value if x % 2 == 0]
    ll = sorted(kwargs.items(), key=lambda x: -len(x[1]))
    dd = {}
    for i in ll:
        dd[i[0]] = i[1]
    return dd


print(even_odd_filter(

    odd=[1, 2, 3, 4, 10, 5, 6, 11, 12, 14, 55],

    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],

))
