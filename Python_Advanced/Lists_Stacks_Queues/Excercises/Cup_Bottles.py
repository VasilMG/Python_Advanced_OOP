from collections import deque
capacities_cups = deque(input().split())
capacities_bottles = deque(input().split())
wasted_water = 0

while len(capacities_bottles) > 0:
    if capacities_cups:
        current_bottle = int(capacities_bottles.pop())
        current_cup = int(capacities_cups[0])
        if current_bottle >= current_cup:
            capacities_cups.popleft()
            wasted_water += current_bottle - current_cup
        else:
            capacities_cups[0] = str(current_cup - current_bottle)
    else:
        break
        
reverse = []        
if capacities_bottles:
    reverse.append(capacities_bottles.pop())
if len(capacities_cups) > 0:
    print(f"Cups: {' '.join(capacities_cups)}")
    print(f"Wasted litters of water: {wasted_water}")
else:
    print(f"Bottles: {' '.join(reverse)}")
    print(f"Wasted litters of water: {wasted_water}")      
        
    



