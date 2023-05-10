# diretions with steps. Step could be 1
def get_next_step(row, col, direction, steps):
    if direction == "up":
        return row - steps, col
    if direction == "down":
        return row + steps, col
    if direction == "right":
        return row, col + steps
    if direction == "left":
        return row, col - steps
# for a square matrix if coordinates are in
def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size

# get the left, right, up, down cell if they are in the matrix:
def get_around_cells(matrix, row, col):
    result = []
    if is_inside(row - 1, col, len(matrix)) and matrix[row - 1][col] == "V" or matrix[row - 1][col] == "X":
        result.append([row - 1, col])
    if is_inside(row + 1, col, len(matrix)) and matrix[row + 1][col] == "V" or matrix[row - 1][col] == "X":
        result.append([row - 1, col])
    if is_inside(row, col - 1, len(matrix)) and matrix[row][col - 1] == "V" or matrix[row][col - 1] == "X":
        result.append([row, col - 1])
    if is_inside(row, col + 1, len(matrix)) and matrix[row][col + 1] == "V" or matrix[row][col + 1] == "X":
        result.append([row, col + 1])


sorted(list, reverse=True, key= lambda x : x % 2) # or key = order_by_division_2 