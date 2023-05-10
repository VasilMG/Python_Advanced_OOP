the_stack = []
number_of_queries = int(input())

for i in range(number_of_queries):
    command = input().split()
    if command[0] == "1":
        new_number = int(command[1])
        the_stack.append(new_number)
    
    if command[0] == "2":
        if the_stack != []:
            the_stack.pop()
        else:
            continue
        
    if command[0] == "3":
        if the_stack:
            print(max(the_stack))
        
    if command[0] == "4":
            if the_stack:   
                print(min(the_stack))
        


new_stack = []

while the_stack:
    new_stack.append(the_stack.pop())
    
print(*new_stack, sep=", ")
    
    
    