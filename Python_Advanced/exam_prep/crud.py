signs = []
mm = []
for row in range(6):
    row_elements = input().split()
    for col in range(6):
        if row_elements[col].isalpha() or row_elements[col].isdigit():
            signs.append((row, col))
    mm.append(row_elements)

coordinates = list(input())

player = (int(coordinates[1]), int(coordinates[4]))

directions = {"up": lambda x: (x[0] - 1, x[1]), 'down': lambda x: (x[0] + 1, x[1]),
                  'left': lambda x: (x[0], x[1] - 1), 'right': lambda x: (x[0], x[1] + 1)}

while True:
    command = input().split(', ')
    if command[0] == 'Stop':
        break

    if command[0] == 'Create':
        next_coordinates = directions[command[1]](player)
        if next_coordinates not in signs:
            mm[next_coordinates[0]][next_coordinates[1]] = command[2]
            if command[2] != '.':
                signs.append(next_coordinates)
        player = next_coordinates


    elif command[0] == 'Update':
        next_coordinates = directions[command[1]](player)
        if next_coordinates in signs:
            mm[next_coordinates[0]][next_coordinates[1]] = command[2]
            if command[2] != '.':
                signs.remove(next_coordinates)
        player = next_coordinates

    elif command[0] == 'Delete':
        next_coordinates = directions[command[1]](player)
        if next_coordinates in signs:
            mm[next_coordinates[0]][next_coordinates[1]] = '.'
            signs.remove(next_coordinates)
        player = next_coordinates

    elif command[0] == 'Read':
        next_coordinates = directions[command[1]](player)
        if next_coordinates in signs:
            print(mm[next_coordinates[0]][next_coordinates[1]])
        player = next_coordinates

for row in mm:
    print(' '.join([str(x) for x in row]))




