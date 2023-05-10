import sys
from io import StringIO

testing_one = '''3
ABC
DEF
X!@
!
'''

testing_two = '''4
asdd
xczc
qwee
qefw
4
'''


sys.stdin = StringIO(testing_two)






def read_matrix():
    n = int(input())
    matrix = []
    for _ in range(n): # nr of rows
        row = list(input())
        matrix.append(row)
    return matrix

mm = read_matrix()

symbol = input()
is_found = False
n = len(mm)
for row_index in range(n):
    if is_found:
        break
    for column_index in range(n):
        if mm[row_index][column_index] == symbol:
            is_found = True
            print(f'({row_index}, {column_index})')
            break

if not is_found:
    print(f"{symbol} does not occur in the matrix")