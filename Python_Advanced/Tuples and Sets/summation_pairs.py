nmbrs = list(map(int, input().split()))
the_sum = int(input())
unique = set()
iteration = 0

for i in nmbrs:
    for j in nmbrs:
        iteration += 1
        sbor = i + j
        
        if sbor == the_sum:
            print(f"{i} + {j} = {sbor}")
            tt = (i, j)
    

