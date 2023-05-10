import sys
from io import StringIO
testing_one = '''3, 6
7 1 3 3 2 1
1 3 9 8 5 6
4 6 7 9 1 0
'''

testing_two = '''3, 3
1 2 3
4 5 6
7 8 9
'''

sys.stdin = StringIO(testing_two)

row_count, column_count = [int(x) for x in input().split(", ")]

matrix = []

column_sums = [0] * column_count 

for _ in range(row_count):
    matrix.append([int(x) for x in input().split()])

for row_index in range(row_count):            
    for column_index in range(column_count):
        column_sums[column_index] += matrix[row_index][column_index]

print('\n'.join([str(x) for x in column_sums]))


column_sums = []
for column_index in range(column_count):
    column_sums.append(0)
    for row_index in range(row_count):
        column_sums[-1] += matrix[row_index][column_index]


