import sys
from io import StringIO

testing_one = '''4
8 3 2 5
6 4 7 9
9 9 3 6
6 8 1 2
1,2 2,1 2,0
'''

testing_two = '''3
7 8 4
3 1 5
6 4 9
0,2 1,0 2,2
'''
sys.stdin = StringIO(testing_two)

def read_matrix():
    n = int(input())
    matrix = []
    for _ in range(n): # nr of rows
        row = [int(x) for x in input().split(" ")]
        matrix.append(row)
    return matrix

mm = read_matrix()

def get_children(mm, row, col):
    possible_children = [
        [row - 1, col - 1],
        [row - 1, col],
        [row - 1, col + 1],
        [row, col - 1],
        [row, col + 1],
        [row + 1, col - 1],
        [row + 1, col],
        [row + 1, col + 1],
    ]
    result = []
    for child_row, child_col in possible_children:
        if 0 <= child_row < len(mm) and 0 <= child_col < len(mm) and mm[child_row][child_col] > 0:
            result.append([child_row, child_col])
    return result



bombs = input().split()

for bomb in bombs:
    row, col = [int(x) for x in bomb.split(",")]
    power = mm[row][col]

    if power <= 0:
        continue

    mm[row][col] = 0
    children = get_children(mm, row, col)
    for child_row, child_col in children:
        mm[child_row][child_col] -= power

alive_cells_count = 0
alive_sum = 0

for r in mm:
    for el in r:
        if el > 0:
            alive_sum += el
            alive_cells_count += 1

print(f"Alive cells: {alive_cells_count}")
print(f"Sum: {alive_sum}")

for line in mm:
    print(*line, sep=" ")
