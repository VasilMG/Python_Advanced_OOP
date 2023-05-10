from collections import deque

people = deque()
while True:
    command = input()
    if command == "End":
        break
    
    if command == "Paid":
        for p in people:
            print(p)
        people.clear()
        
    else:
        people.append(command)
        
print(f"{len(people)} people remaining.")