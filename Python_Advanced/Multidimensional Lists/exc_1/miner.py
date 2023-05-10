

def get_next_position(direction, row, col):
    if direction == "up":
        return row - 1, col
    if direction == "down":
        return row + 1, col
    if direction == "left":
        return row, col - 1
    if direction == "right":
        return row, col + 1


size = int(input())
the_commands = input().split()
player_row = 0
player_col = 0
total_coal = 0
matrix = []
total_commands = len(the_commands)
for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == "s":
            player_row = row
            player_col = col
        if row_elements[col] == "c":
            total_coal += 1
    matrix.append(row_elements)

the_end = False

for the_dir in the_commands:
    total_commands -= 1
    next_row, next_col = get_next_position(the_dir, player_row, player_col)
    if next_row < 0 or next_row >= size or next_col < 0 or next_col >= size:
        continue

    matrix[player_row][player_col] = '*'
    player_row, player_col = next_row, next_col
    if matrix[next_row][next_col] == "e":
        the_end = True
        print(f"Game over! ({next_row}, {next_col})")
        break
    if matrix[next_row][next_col] == "c":
        total_coal -= 1
        matrix[next_row][next_col] = '*'

    if total_coal == 0:
        print(f"You collected all coal! ({player_row}, {player_col})")
        break


# if total_coal == 0:
#     print(f"You collected all coal! ({player_row}, {player_col})")

if the_end == False and total_coal > 0 and total_commands == 0:
    print(f"{total_coal} pieces of coal left. ({player_row}, {player_col})")
