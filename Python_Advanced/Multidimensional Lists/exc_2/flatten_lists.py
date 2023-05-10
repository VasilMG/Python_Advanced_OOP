n = input()
mm = [x.strip() for x in n.split("|")]

mm1 = []

for j in range(len(mm) - 1, -1, -1):
    mm1 += [y.strip() for y in  mm[j].split()]

print(*mm1, sep=" ")

