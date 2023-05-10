import sys
from io import StringIO

testing_one = '''3 4
A B B D
E B B B
I J B B
'''

testing_two = '''2 2
a b
c d
'''

testing_three = '''5 4
A A B D
A A B B
I J B B
C C C G
C C K P'''


sys.stdin = StringIO(testing_three)



n, m = [int(x) for x in input().split()]
matrix = []
for _ in range(n): # nr of rows
    row = [x for x in input().split()]
    matrix.append(row)


squares = 0

for row_index in range(n - 1): 
    for column_index in range(m - 1): 
        if matrix[row_index][column_index] == matrix[row_index][column_index +1] == matrix[row_index +1 ][column_index] == matrix[row_index + 1][column_index + 1]:
            squares += 1

print(squares)