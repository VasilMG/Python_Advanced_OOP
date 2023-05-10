# n = int(input())
# uniques = set()

# for i in range(n):
#     command = input().split()
#     for i in command:
#         uniques.add(i)
    
# print("\n".join(uniques))

n = int(input())
the_set = set()

for i in range(n):
    current = set(input().split())
    the_set = the_set.union(current) 
    

[print(x) for x in the_set]