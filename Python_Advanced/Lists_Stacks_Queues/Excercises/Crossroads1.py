# 100%

from collections import deque

greelight = int(input())
free_window = int(input())

line = deque()
pass_counter = 0
crashed = False

while not crashed:
    command = input()
    if command == "END":
        break
    
    if command == "green":
        current_green = greelight
        while line and current_green > 0:
            car = line.popleft()
            if len(car) <= current_green + free_window:
                pass_counter +=1
            else:
                print(f"A crash happened!")
                print(f"{car} was hit at {car[current_green + free_window]}.") 
                crashed = True
                break
            current_green -= len(car)
            
    else:
        line.append(command)
        
if not crashed:
    print(f"Everyone is safe.")
    print(f"{pass_counter} total cars passed the crossroads.")