n , m  = list(map(int, (input().split())))
first_set = set()
second_set = set()

for i in range(n+m):
    command = int(input())
    if i < n:
        first_set.add(command)
    else:
        second_set.add(command)
        
the_intersection = list(map(str, (first_set.intersection(second_set))))
print("\n".join(the_intersection))