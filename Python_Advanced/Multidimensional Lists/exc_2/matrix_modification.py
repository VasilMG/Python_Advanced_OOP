import sys
from io import StringIO

testing_one = '''3
1 2 3
4 5 6
7 8 9
Add 0 0 5
Subtract 1 1 2
END
'''

testing_two = '''4
1 2 3 4
5 6 7 8
8 7 6 5
4 3 2 1
Add 4 4 100
Add 3 3 100
Subtract -1 -1 42
Subtract 0 0 42
END
'''
sys.stdin = StringIO(testing_one)

n = int(input())
matrix = []
for _ in range(n): # nr of rows
    row = [int(x) for x in input().split(" ")]
    matrix.append(row)


while True:
    command = input().split()
    if command[0] == "END":
        break

    if command[0] == "Add":
        row_index = int(command[1])
        column_index = int(command[2])
        the_number = int(command[3])
        if row_index <0 or row_index >= n or column_index < 0 or column_index >= n:
            print(f"Invalid coordinates")
            continue

        matrix[row_index][column_index] = matrix[row_index][column_index] + the_number

    if command[0] == "Subtract":
        row_index = int(command[1])
        column_index = int(command[2])
        the_number = int(command[3])
        if row_index < 0 or row_index >= n or column_index < 0 or column_index >= n:
            print(f"Invalid coordinates")
            continue

        matrix[row_index][column_index] = matrix[row_index][column_index] - the_number

for the_row in matrix:
    print(" ".join([str(x) for x in the_row ]))
