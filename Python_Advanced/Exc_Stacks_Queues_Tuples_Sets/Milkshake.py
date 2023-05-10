from collections import deque
chokolate = [int(x) for x in input().split(", ")]
milk_cups = deque([int(x) for x in input().split(", ")])

milkshakes = 0

while chokolate and milk_cups and milkshakes < 5:
    current_chocolate = chokolate.pop()
    cup = milk_cups.popleft()
    if current_chocolate <= 0 and cup <=0:
        continue
    if current_chocolate <= 0:
        milk_cups.appendleft(cup)
        continue
    if cup <= 0:
        chokolate.append(current_chocolate)
        continue
    if current_chocolate == cup:
        milkshakes += 1
    else:
        milk_cups.append(cup)
        chokolate.append(current_chocolate - 5)

if milkshakes >= 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chokolate:
    print(f"Chocolate: {', '.join([str(x) for x in chokolate])}")
else:
    print("Chocolate: empty")
if milk_cups:
    print(f"Milk: {', '.join([str(x) for x in milk_cups])}")
else:
    print("Milk: empty")


