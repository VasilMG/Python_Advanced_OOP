
from collections import deque
text = input().split()
current_numbers = deque()
result = 0
operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a // b,
}

for i in text:
    if i not in "+-*/":
        current_numbers.append(int(i))
    else:
        while len(current_numbers) > 1:
            first = current_numbers.popleft()
            second = current_numbers.popleft()
            result = operations[i](first, second)
            current_numbers.appendleft(result)

print(current_numbers.pop())
