def is_outside(row, col, size):
    return row < 0 or row >= size or col < 0 or col >= size


def get_children(row, col, lenght):
    possible_children = [
        [row - 2, col - 1],
        [row - 2, col + 1],
        [row - 1, col + 2],
        [row - 1, col - 2],
        [row + 1, col - 2],
        [row + 1, col + 2],
        [row + 2, col - 1],
        [row + 2, col + 1]
    ]
    result = []
    for new_row, new_col in possible_children:
        if not is_outside(new_row, new_col, lenght):
            result.append(f"{new_row} {new_col}")

    return result

def get_knights(n, matrix):
    the_knights = []
    for row in range(n):
        for col in range(n):
            if matrix[row][col] == "K":
                the_knights.append([row, col])
    return the_knights

def get_the_most(dict):
    the_one = ""
    for k, v in dict.items():
        if v == max(dict.values()):
            the_one = k
    return the_one

def the_new_matrix(knight, matrix):
    r_row, r_col = [int(x) for x in knight.split()]
    matrix[r_row][r_col] = "0"
    return matrix


n = int(input())
matrix = []
for row in range(n):
    the_input = input()
    matrix.append(list(the_input))
the_best = 0
the_removed = 0

while True:
    the_best = 0
    best_row = 0
    best_col = 0
    knights = get_knights(n, matrix)
    for i in knights:
        combinations = 0
        k_row, k_col = [int(x) for x in i]
        children = get_children(k_row, k_col, n)
        for c in children:
            c_row, c_col = [int(x) for x in c.split()]
            if matrix[c_row][c_col] == "K":
                combinations += 1

        if combinations > the_best:
            the_best = combinations
            best_row = k_row
            best_col = k_col
        else:
            continue
    if the_best == 0:
        break

    matrix[best_row][best_col] = "0"
    the_removed += 1


print(the_removed)

