from collections import deque
bees = deque([int(x) for x in input().split()])
nectars = [int(x) for x in input().split()]
operators = deque(input().split())

honey = 0

operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
}

while bees and nectars:
    current_bee = bees.popleft()
    the_nectar = nectars.pop()
    if the_nectar < current_bee:
        bees.appendleft(current_bee)
        continue
    if the_nectar == 0:
        continue

    the_operator = operators.popleft()
    honey += abs(operations[the_operator](current_bee, the_nectar))

print(f"Total honey made: {honey}")

if bees:
    print(f"Bees left: {', '.join([str(x) for x in bees])}")
if nectars:
    print(f"Nectar left: {', '.join([str(x) for x in nectars])}")
