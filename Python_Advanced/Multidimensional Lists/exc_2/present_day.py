def get_next_step(row, col, direction):
    if direction == "up":
        return row - 1, col
    if direction == "down":
        return row + 1, col
    if direction == "right":
        return row, col + 1
    if direction == "left":
        return row, col - 1

def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size

def get_around_cells(matrix, row, col):
    result = []
    if is_inside(row, col - 1, len(matrix)) and matrix[row][col - 1] == "V" or matrix[row][col - 1] == "X":
        result.append([row, col - 1])
    if is_inside(row, col + 1, len(matrix)) and matrix[row][col + 1] == "V" or matrix[row][col + 1] == "X":
        result.append([row, col + 1])
    if is_inside(row - 1, col, len(matrix)) and matrix[row - 1][col] == "V" or matrix[row - 1][col] == "X":
        result.append([row - 1, col])
    if is_inside(row + 1, col, len(matrix)) and matrix[row + 1][col] == "V" or matrix[row + 1][col] == "X":
        result.append([row + 1, col])
    return result

presents = int(input())
n = int(input())
matrix = []
santa_row = 0
santa_col = 0
nice_kids = 0
kids_with_presents = 0
for row in range(n):
    row_elements = input().split()
    for col in range(n):
        if row_elements[col] == "S":
            santa_row = row
            santa_col = col
        elif row_elements[col] == "V":
            nice_kids += 1
    matrix.append(row_elements)

while presents > 0:
    command = input()
    if command == "Christmas morning":
        break

    matrix[santa_row][santa_col] = "-"
    santa_row, santa_col = get_next_step(santa_row, santa_col, command)

    if matrix[santa_row][santa_col] == "V":
        presents -= 1
        kids_with_presents += 1

    elif matrix[santa_row][santa_col] == "C":
        cells_around = get_around_cells(matrix, santa_row, santa_col)
        for k_row, k_col in cells_around:
            if matrix[k_row][k_col] == "V":
                kids_with_presents += 1
            presents -= 1
            matrix[k_row][k_col] = "-"
            if presents == 0:
                break

    matrix[santa_row][santa_col] = "S"


if kids_with_presents != nice_kids and presents == 0:
    print("Santa ran out of presents!")

for row in matrix:
    print(*row, sep=" ")

if kids_with_presents == nice_kids:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids - kids_with_presents} nice kid/s.")
