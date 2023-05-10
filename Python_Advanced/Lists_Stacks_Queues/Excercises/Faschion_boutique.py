the_clothes = list(map(int, input().split()))
capacity = int(input())

the_sum = 0
stack = 1

while len(the_clothes) > 0:
    current_clothes = the_clothes[-1]
    the_sum += current_clothes
    if the_sum <= capacity:
        the_clothes.pop()
    else:
        stack += 1
        the_sum = 0
        
print(stack) 
        
        
        
    