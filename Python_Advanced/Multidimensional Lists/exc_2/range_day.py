def get_next_step(row, col, direction, steps):
    if direction == "up":
        return row - steps, col
    if direction == "down":
        return row + steps, col
    if direction == "right":
        return row, col + steps
    if direction == "left":
        return row, col - steps

def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size



size = 5
player_row = 0
player_col = 0
number_x = 0
matrix = []

for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == "A":
            player_row = row
            player_col = col
        if row_elements[col] == "x":
            number_x += 1
    matrix.append(row_elements)

matrix[player_row][player_col] = "."
hit_targets = []

n = int(input())
for _ in range(n):
    command_parts = input().split()
    first_command = command_parts[0]
    direction = command_parts[1]

    if first_command == "move":
        steps = int(command_parts[2])
        new_row, new_col = get_next_step(player_row, player_col, direction, steps)
        if is_inside(new_row, new_col, size) and matrix[new_row][new_col] == ".":
            player_row, player_col = new_row, new_col
    else:
        bullet_row, bullet_col = get_next_step(player_row, player_col, direction, steps=1)
        while is_inside(bullet_row, bullet_col, size):
            if matrix[bullet_row][bullet_col] == "x":
                number_x -= 1
                hit_targets.append([bullet_row, bullet_col])
                matrix[bullet_row][bullet_col] = "."
                break
            else:
                bullet_row, bullet_col = get_next_step(bullet_row, bullet_col, direction, steps=1)

        if number_x == 0:
            break

if number_x == 0:
    print(f"Training completed! All {len(hit_targets)} targets hit.")
else:
    print(f"Training not completed! {number_x} targets left.")

if hit_targets:
    [print(x) for x in hit_targets]