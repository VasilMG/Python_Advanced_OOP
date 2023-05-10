the_numbers = input().split()

new_numbers = []

for i in range(len(the_numbers)):
    new_item = the_numbers.pop()
    new_numbers.append(new_item)
    
print(" ".join(new_numbers))