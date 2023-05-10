stations = int(input())
tank = 0
the_stack = []
for n in range(stations):
    current_station = input().split()
    tank += int(current_station[0])
    distance = int(current_station[1])
    if tank >= distance:
        the_stack.append(n)
        tank -= distance
    else:
        the_stack.clear()
        tank = 0
print(the_stack[0])
        
    