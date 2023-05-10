def naughty_or_nice_list(canta_list, *args, **kwargs):
    dd = {}
    for i in canta_list:
        if i[0] not in dd:
            dd[i[0]] = [i[1]]
        else:
            dd[i[0]].append(i[1])

    nice =  []
    naughty =  []
    not_found = []
    for a in args:
        key, decision = a.split('-')
        if int(key) not in dd.keys():
            continue
        if len(dd[int(key)]) > 1:
            continue
        if decision == 'Nice':
            nice.append(dd[int(key)][0])
            canta_list.remove((int(key), dd[int(key)][0]))
        elif decision == 'Naughty':
            naughty.append(dd[int(key)][0])
            canta_list.remove((int(key), dd[int(key)][0]))

    for the_key, value in kwargs.items():
        count = 0
        for item in canta_list:
            if the_key == item[1]:
                the_item = item
                count += 1
        if count > 1 or count == 0:
            continue
        if value == "Nice":
            nice.append(the_key)
            canta_list.remove(the_item)
        elif value == "Naughty":
            naughty.append(the_key)
            canta_list.remove(the_item)

    if canta_list:
        for item in canta_list:
            not_found.append(item[1])
    the_lists = {'Nice:': nice, 'Naughty:': naughty, 'Not found:': not_found}
    return "\n".join([f'{k} {", ".join(v)}' for k, v in the_lists.items() if len(v) > 0])
    # if nice:
    #     print(f'Nice: {" ".join([x for x in nice])}')
    # if naughty:
    #     print(f'Naughty: {" ".join([x for x in naughty])}')
    # if not_found:
    #     print(f'Not found: {" ".join([x for x in not_found])}')

# print(naughty_or_nice_list(
#
# [
#
# (6, "John"),
#
# (4, "Karen"),
#
# (2, "Tim"),
#
# (1, "Merry"),
#
# (6, "Frank"),
#
# ],
#
# "6-Nice",
#
# "5-Naughty",
#
# "4-Nice",
#
# "3-Naughty",
#
# "2-Nice",
#
# "1-Naughty",
#
# Frank="Nice",
#
# Merry="Nice",
#
# John="Naughty",
#
# ))


# print(naughty_or_nice_list( [ (3, "Amy"), (1, "Tom"), (7, "George"), (3, "Katy"), ],
#                             "3-Nice", "1-Naughty", Amy="Nice", Katy="Naughty", ))

print(naughty_or_nice_list(

[

(7, "Peter"),

(1, "Lilly"),

(2, "Peter"),

(12, "Peter"),

(3, "Simon"),

],

"3-Nice",

"5-Naughty",

"2-Nice",

"1-Nice",

))