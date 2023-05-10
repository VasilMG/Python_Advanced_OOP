def sorting_cheeses(**kwargs):
    s_cheese = sorted(kwargs.items(), key= lambda x: (-len(x[1]), x[0]))
    result = []
    for name, count in s_cheese:
        result.append(name)
        for piece_count in sorted(count, reverse=True):
            result.append(piece_count)
    return "\n".join([str(x) for x in result])


print(

sorting_cheeses(

Parmigiano=[165, 215],

Feta=[150, 515],

Brie=[150, 125]

))