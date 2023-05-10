sequence = input()
balanced = False
brackets = []
 
for el in sequence:
    if el in '({[':
        brackets.append(el)
    elif el in ')}]' and brackets:
        popped_last = brackets.pop()
        if popped_last + el in '()[]{}':
            balanced = True
        else:
            balanced = False
            break
    else:
        balanced = False
        break
 
if balanced and not brackets:
    print('YES')
else:
    print('NO')