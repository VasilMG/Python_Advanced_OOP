size = int(input())
submarine = 0
mm = []
cruisers = []
mines = []

for row in range(size):
    row_elements = list(input())
    for col in range(len(row_elements)):
        if row_elements[col] == 'S':
            submarine = (row, col)
        elif row_elements[col] == 'C':
            cruisers.append((row, col))
        elif row_elements[col] == '*':
            mines.append((row, col))
    mm.append(row_elements)

directions = {"up": lambda x: (x[0]-1, x[1]), 'down': lambda x: (x[0]+ 1, x[1]),
              'left': lambda x: (x[0], x[1] - 1), 'right': lambda x: (x[0], x[1] +1)}

mines_count = 0
cruisers_destroyed = 0
while True:
    command = input()
    next_coordinates = directions[command](submarine)
    mm[submarine[0]][submarine[1]] = '-'
    submarine = next_coordinates

    if next_coordinates in mines:
        mines_count += 1
        mm[submarine[0]][submarine[1]] = '-'
        mines.remove(next_coordinates)
        if mines_count == 3:
            mm[submarine[0]][submarine[1]] = 'S'
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{submarine[0]}, {submarine[1]}]!")
            break
    elif next_coordinates in cruisers:
        cruisers_destroyed +=1
        mm[submarine[0]][submarine[1]] = '-'
        cruisers.remove(next_coordinates)
        if cruisers_destroyed == 3:
            mm[submarine[0]][submarine[1]] = 'S'
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break

print('\n'.join([''.join(x) for x in mm]))



