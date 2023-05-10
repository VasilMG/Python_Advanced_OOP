def get_next_cells(player, direction, steps, matrix, collected, the_sum):
    player_row = player[0]
    player_col = player[1]
    if direction == 'up':
        for s in range(steps):
            new_row, new_col = player_row - 1, player_col
            if new_row < 0:
                new_row = len(matrix) - 1
            if matrix[new_row][new_col] == "D":
                collected['Christmas decorations'] += 1
                the_sum += 1

            elif matrix[new_row][new_col] == "G":
                collected['Gifts'] += 1
                the_sum += 1
            elif matrix[new_row][new_col] == "C":
                collected['Cookies'] += 1
                the_sum += 1
            if the_sum == items_count:
                matrix[player_row][player_col] = 'x'
                player_row, player_col = new_row, new_col
                matrix[player_row][player_col] = 'Y'
                return player, collected, the_sum
            matrix[player_row][player_col] = 'x'
            player_row, player_col = new_row, new_col
            matrix[player_row][player_col] = 'Y'
        player = player_row, player_col
        return player, collected, the_sum

    elif direction == 'down':
        for s in range(steps):
            new_row, new_col = player_row + 1, player_col
            if new_row >= len(matrix):
                new_row = 0
            if matrix[new_row][new_col] == "D":
                collected['Christmas decorations'] += 1
                the_sum += 1
            elif matrix[new_row][new_col] == "G":
                collected['Gifts'] += 1
                the_sum += 1
            elif matrix[new_row][new_col] == "C":
                collected['Cookies'] += 1
                the_sum += 1
            if the_sum == items_count:
                matrix[player_row][player_col] = 'x'
                player_row, player_col = new_row, new_col
                matrix[player_row][player_col] = 'Y'
                return player, collected, the_sum
            matrix[player_row][player_col] = 'x'
            player_row, player_col = new_row, new_col
            matrix[player_row][player_col] = 'Y'
        player = player_row, player_col
        return player, collected, the_sum

    elif direction == 'right':
        for s in range(steps):
            new_row, new_col = player_row, player_col + 1
            if new_col >= len(matrix[0]):
                new_col = 0
            if matrix[new_row][new_col] == "D":
                collected['Christmas decorations'] += 1
                the_sum += 1

            elif matrix[new_row][new_col] == "G":
                collected['Gifts'] += 1
                the_sum += 1
            elif matrix[new_row][new_col] == "C":
                collected['Cookies'] += 1
                the_sum += 1
            if the_sum == items_count:
                matrix[player_row][player_col] = 'x'
                player_row, player_col = new_row, new_col
                matrix[player_row][player_col] = 'Y'
                return player, collected, the_sum
            matrix[player_row][player_col] = 'x'
            player_row, player_col = new_row, new_col
            matrix[player_row][player_col] = 'Y'
        player = player_row, player_col
        return player, collected, the_sum

    elif direction == 'left':
        for s in range(steps):
            new_row, new_col = player_row, player_col - 1
            if new_col < 0:
                new_col = len(matrix[0]) - 1
            if matrix[new_row][new_col] == "D":
                collected['Christmas decorations'] += 1
                the_sum += 1

            elif matrix[new_row][new_col] == "G":
                collected['Gifts'] += 1
                the_sum += 1
            elif matrix[new_row][new_col] == "C":
                collected['Cookies'] += 1
                the_sum += 1
            if the_sum == items_count:
                matrix[player_row][player_col] = 'x'
                player_row, player_col = new_row, new_col
                matrix[player_row][player_col] = 'Y'
                return player, collected, the_sum
            matrix[player_row][player_col] = 'x'
            player_row, player_col = new_row, new_col
            matrix[player_row][player_col] = 'Y'
        player = player_row, player_col
        return player, collected, the_sum


n, m = [int(x) for x in input().split(', ')]
player = 0
matrix = []
items_count = 0
for row in range(n):
    row_elements = input().split()
    for col in range(m):
        if row_elements[col] == 'Y':
            player = row, col
        elif row_elements[col] == 'D' or row_elements[col] == 'C' or row_elements[col] == 'G':
            items_count += 1
    matrix.append(row_elements)


collected = {'Christmas decorations': 0, 'Gifts': 0, 'Cookies': 0}
the_sum = 0
while True:
    command = input().split('-')
    if command[0] == 'End':
        break
    direction = command[0]
    steps = int(command[1])
    player, collection, the_sum = get_next_cells(player,direction,steps,matrix,collected, the_sum)
    if the_sum == items_count:
        break

if the_sum == items_count:
    print("Merry Christmas!")

print("You've collected:")
for k, v in collection.items():
    print(f"- {v} {k}")
for row in matrix:
    print(' '.join([str(x) for x in row]))



