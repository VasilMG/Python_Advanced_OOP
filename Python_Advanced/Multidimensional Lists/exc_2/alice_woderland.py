
def get_direction(row, col, direction):
    if direction == "up":
        return row - 1, col
    if direction == "down":
        return row + 1, col
    if direction == "right":
        return row, col + 1
    if direction == "left":
        return row, col - 1
size = int(input())
matrix = []

alice_row = 0
alice_col = 0
for row in range(size):
    elements = input().split()
    for col in range(size):
        if elements[col] == "A":
            alice_row = row
            alice_col = col
    matrix.append(elements)

tea_bags = 0

while tea_bags < 10:
    matrix[alice_row][alice_col] = "*"
    direction = input()
    next_row, next_col = get_direction(alice_row, alice_col, direction)

    if 0 <= next_row and next_row < size and 0 <= next_col and next_col < size:
        alice_row = next_row
        alice_col = next_col
    else:
        break

    if matrix[alice_row][alice_col] =="." or matrix[alice_row][alice_col] =="*":
        continue
    if matrix[alice_row][alice_col] == "R":
        break

    tea_bags += int(matrix[alice_row][alice_col])

matrix[alice_row][alice_col] = "*"

if tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for row in matrix:
    print(* row, sep=" ")