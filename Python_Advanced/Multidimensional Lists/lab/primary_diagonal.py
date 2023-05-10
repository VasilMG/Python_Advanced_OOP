import sys
from io import StringIO

testing_one = '''3
11 2 4
4 5 6
10 8 -12
'''

testing_two = '''3
1 2 3
4 5 6
7 8 9
'''


sys.stdin = StringIO(testing_one)


def read_matrix():
    n = int(input())
    matrix = []
    for _ in range(n): # nr of rows
        row = [int(x) for x in input().split(" ")]
        matrix.append(row)
    return matrix

mm = read_matrix()
diagonal_sum = 0

for row_index in range(len(mm)):
    for column_index in range(len(mm[row_index])):
        if column_index == row_index:
            diagonal_sum += mm[row_index][column_index]

print(diagonal_sum)



