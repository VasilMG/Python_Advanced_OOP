from collections import deque
total_water = int(input())

people = deque()

while True:
    command = input()
    if command == "Start":
        break
    
    people.append(command)
    
while True:
    second_command = input().split()
    if second_command[0] == "End":
        break
    
    if second_command[0] == "refill":
        total_water += int(second_command[1])
    else:
        needed_liters = int(second_command[0])
        person_name = people.popleft()
        if needed_liters <= total_water:
            total_water -= needed_liters
            print(f"{person_name} got water")
        else:
            print(f"{person_name} must wait")
            
print(f"{total_water} liters left")
            