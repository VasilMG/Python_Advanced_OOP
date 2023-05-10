n = int(input())
the_list = set()
for i in range(n):
    command = input()
    the_list.add(command)
    
print("\n".join(the_list))