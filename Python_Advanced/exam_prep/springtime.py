def start_spring(**kwargs):
    result = {}
    for k, v in kwargs.items():
        if v not in result.keys():
            result[v] = []
            result[v].append(k)
        else:
            result[v].append(k)
    the_sorted = sorted(result.items(), key= lambda x: (-len(x[1]), x[0]))
    dd= {}
    for i in the_sorted:
        dd[i[0]] = sorted(i[1])
    answer = []
    for k, v in dd.items():
        answer.append(f'{k}:')
        for j in v:
            answer.append(f'-{j}')

    return '\n'.join(answer)



#ll= [f"{k} - {sorted(v)}" for k, v in sorted(result.items(), key= lambda x: (-len(x[1]), x[0]))]
# example_objects = {"Water Lilly": "flower",
#
#                    "Swifts": "bird",
#
#                    "Callery Pear": "tree",
#
#                    "Swallows": "bird",
#
#                    "Dahlia": "flower",
#
#                    "Tulip": "flower",}
#
# print(start_spring(**example_objects))

# example_objects = {"Swallow": "bird",
#
#                    "Thrushes": "bird",
#
#                    "Woodpeckers": "bird",
#
#                    "Swallows": "bird",
#
#                    "Warblers": "bird",
#
#                    "Shrikes": "bird",}
#
# print(start_spring(**example_objects))

example_objects = {"Magnolia": "tree",

                   "Swallow": "bird",

                   "Thrushes": "bird",

                   "Pear": "tree",

                   "Cherries": "tree",

                   "Shrikes": "bird",

                   "Butterfly": "insect"}

print(start_spring(**example_objects))