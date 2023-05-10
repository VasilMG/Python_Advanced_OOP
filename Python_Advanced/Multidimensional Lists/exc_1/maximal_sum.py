import sys
from io import StringIO

testing_one = '''4 5
1 5 5 2 4
2 1 4 14 3
3 7 11 2 8
4 8 12 16 4
'''

testing_two = '''5 6
1 0 4 3 1 1
1 3 1 3 0 4
6 4 1 2 5 6
2 2 1 5 4 1
3 3 3 6 0 5
'''


sys.stdin = StringIO(testing_two)



n, m = [int(x) for x in input().split()]
mm = []
for _ in range(n): # nr of rows
    row = [int(x) for x in input().split()]
    mm.append(row)



current_sum = 0
max_sum = float("-inf")
size = 3
current_square = []
max_square = []

for row_index in range(n - (size - 1)):
    for column_index in range(m - (size - 1)):
        for p in range(size):
            current_sum += sum(mm[row_index + p][column_index: column_index + size])
            current_square.append(mm[row_index + p][column_index: column_index + size])

        if current_sum > max_sum:
            max_sum = current_sum
            max_square = current_square
            current_square = []
            current_sum = 0
        else:
            current_sum = 0
            current_square = []


print(f"Sum = {max_sum}")
for z in range(len(max_square)):
    print(" ".join(str(x) for x in max_square[z]))