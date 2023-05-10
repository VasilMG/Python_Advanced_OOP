def read_matrix():
    n = int(input())
    matrix = []
    for _ in range(n): # nr of rows
        row = [int(x) for x in input().split(" ")]
        matrix.append(row)
    return matrix

mm = read_matrix()

primary_sum = 0
secondary_sum = 0

for i in range(len(mm)):
    primary_sum += mm[i][i]
    secondary_sum += mm[i][len(mm) - i - 1]


print(abs(primary_sum - secondary_sum))