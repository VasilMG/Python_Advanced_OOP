# def read_matrix():
#     n, m = [int(x) for x in input().split(", ")]
#     matrix = []
#     for _ in range(n): # nr of rows
#         row = [int(x) for x in input().split(", ")]
#         matrix.append(row)
#     return matrix


n, m = [int(x) for x in input().split(", ")]
matrix = []
the_sum = 0
for _ in range(n): # nr of rows
    row = [int(x) for x in input().split(", ")]
    matrix.append(row)
    the_sum += sum(row)


print(the_sum)
print(matrix)
