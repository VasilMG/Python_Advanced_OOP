from collections import deque
text = deque(input().split())
the_main = {"red", "yellow", "blue", "orange", "purple", "green"}
found_main = []

while len(text) > 0:
    if len(text) == 1:
        result = text.pop()
        if result in the_main:
            found_main.append(result)
            break
        else:
            break
    else:
        left = text.popleft()
        right = text.pop()
        result = left + right
        rev_result = right + left
        if result in the_main:
            found_main.append(result)
            continue
        elif rev_result in the_main:
            found_main.append(rev_result)
            continue
        if (result not in the_main and rev_result not in the_main):
            new_left = left[0: (len(left) - 1)]
            new_right = right[0: (len(right) - 1)]
            the_index = len(text) // 2
            if new_right:
                text.insert(the_index, new_right)
            if new_left:
                text.insert(the_index, new_left)

if "purple" in found_main and ("red" not in found_main or "blue" not in found_main):
    found_main.remove("purple")
if "orange" in found_main and ("red" not in found_main or "yellow" not in found_main):
    found_main.remove("orange")
if "green" in found_main and ("blue" not in found_main or "yellow" not in found_main):
    found_main.remove("green")

print(found_main)





