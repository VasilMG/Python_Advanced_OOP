from collections import deque
food_for_the_day = int(input())
orders = deque(input().split())
int_orders = list(map(int, orders))
print(max(int_orders))
while len(orders) > 0:
    current_order = int(orders[0])
    if current_order <= food_for_the_day:
        food_for_the_day -= current_order
        orders.popleft()
    else:
        break
    
if len(orders) > 0:
    print(f"Orders left: {' '.join(orders)}")
else:
    print("Orders complete")