from collections import deque
def get_next(command, rover, matrix):
    r_row, r_col = rover
    if command == 'up':
        new_row, new_col =  (r_row - 1, r_col)
        if new_row < 0:
            new_row = len(matrix) - 1
            return new_row, new_col
        return new_row, new_col
    elif command == 'down':
        new_row, new_col = (r_row + 1, r_col)
        if new_row > len(matrix) - 1:
            new_row = 0
            return new_row, new_col
        return new_row, new_col
    elif command == 'right':
        new_row, new_col = (r_row, r_col + 1)
        if new_col > len(matrix) - 1:
            new_col = 0
            return new_row, new_col
        return new_row, new_col

    elif command == 'left':
        new_row, new_col = (r_row, r_col - 1)
        if new_col < 0:
            new_col = len(matrix) - 1
            return new_row, new_col
        return new_row, new_col



matrix = []
rover = 0
found_resources = set()

for row in range(6):
    row_elements = input().split()
    for j in range(6):
        if row_elements[j] == 'E':
            rover = (row, j)
    matrix.append(row_elements)


commands = deque(input().strip().split(', '))

while commands:
    current_command = commands.popleft()
    new_row, new_col = get_next(current_command, rover, matrix)
    if matrix[new_row][new_col] == 'W':
        rover = (new_row, new_col)
        found_resources.add("W")
        print(f"Water deposit found at ({new_row}, {new_col})")

    elif matrix[new_row][new_col] == 'M':
        rover = (new_row, new_col)
        found_resources.add("M")
        print(f"Metal deposit found at ({new_row}, {new_col})")
    elif matrix[new_row][new_col] == 'C':
        rover = (new_row, new_col)
        found_resources.add("C")
        print(f"Concrete deposit found at ({new_row}, {new_col})")
    elif matrix[new_row][new_col] == 'R':
        print(f"Rover got broken at ({new_row}, {new_col})")
        break

    else:
        rover = (new_row, new_col)



if len(found_resources) == 3:
    print(f"Area suitable to start the colony.")
else:
    print(f"Area not suitable to start the colony.")
