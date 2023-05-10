import sys
from io import StringIO

testing_one = '''2 3
1 2 3
4 5 6
swap 0 0 1 1
swap 10 9 8 7
swap 0 1 1 0
END
'''

testing_two = '''1 2
Hello World
0 0 0 1
swap 0 0 0 1
swap 0 1 0 0
END
'''
sys.stdin = StringIO(testing_one)

def is_otside(row, col, n, m):
    if row < 0 or row >= n or col < 0 or col >= m:
        return True
    else:
        return False

n, m = [int(x) for x in input().split()]
matrix = []

for _ in range(n):  # nr of rows
    row = [x for x in input().split()]
    matrix.append(row)



while True:
    command = input().split()
    if command[0] == "END":
        break
    if len(command) != 5 or command[0] != "swap":
        print(f"Invalid input!")
        continue

    r1, c1, r2, c2 = [int(x) for x in command[1:]]

    if is_otside(r1, c1, n, m) or is_otside(r2, c2, n, m):
        print(f"Invalid input!")
        continue
    else:
        matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]

    for the_row in matrix:
        print(*the_row, sep=" ")