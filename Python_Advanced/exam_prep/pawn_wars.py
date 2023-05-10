def characters_return(matrix):
    row_str = {}
    n = 8
    for c_row in range(len(matrix)):
        row_str[c_row] = n
        n -= 1

    col_str = {}
    n = 97
    for c_col in range(len(matrix)):
        col_str[c_col] = chr(n)
        n += 1

    return row_str, col_str

def check_for_capture(player, matrix):
    possible_captures = possible_capture(player, matrix)
    result = []
    for position in possible_captures:
        if player[0] == 'white':
            p_row, p_col = position
            if matrix[p_row][p_col] == 'b':
                result.append(position)
        if player[0] == 'black':
            p_row, p_col = position
            if matrix[p_row][p_col] == 'w':
                result.append(position)
    return result

def player_move(player):
    current_player = player[0]
    row, column = player[1]
    if current_player == 'white':
        new_row, new_column = (row - 1, column)
        return (current_player, (new_row, new_column))
    elif current_player == 'black':
        new_row, new_column = (row + 1, column)
        return (current_player, (new_row, new_column))

def possible_capture(player, matrix):
    current_player = player[0]
    row, column = player[1]
    result = []
    if current_player == 'white':
        possible_coordinates = [(row - 1, column - 1), (row- 1, column + 1)]
        for r in possible_coordinates:
            the_row, the_column = r
            if 0 <= the_row < len(matrix) and 0 <= the_column < len(matrix):
                result.append(r)

    if current_player == 'black':
        possible_coordinates = [(row + 1, column - 1), (row + 1, column + 1)]
        for r in possible_coordinates:
            the_row, the_column = r
            if 0 <= the_row < len(matrix) and 0 <= the_column < len(matrix):
                result.append(r)
    return result


matrix = []
players = {}
white = 0
black = 0
for i in range(8):
    row_elements = input().split()
    for j in range(len(row_elements)):
        if row_elements[j] == 'w':
            white = ('white', (i, j))

        elif row_elements[j] == 'b':
            black = ('black', (i, j))
    matrix.append(row_elements)



the_players = [white, black]
row, column = white[1]
current_player = white
row_str, col_str = characters_return(matrix)

while True:
    current_player = the_players[0]
    captures = check_for_capture(current_player, matrix)
    if len(captures) > 0:
        c_row, c_col = captures[0]
        print(f'Game over! {current_player[0].capitalize()} win, capture on {col_str[c_col]}{row_str[c_row]}.')
        break

    row, column = current_player[1]
    matrix[row][column] = '-'
    current_player = player_move(current_player)
    new_row, new_col = current_player[1]
    if current_player[0] == 'white':
        matrix[new_row][new_col] = 'w'

    elif current_player[0] == 'black':
        matrix[new_row][new_col] = 'b'

    if new_row == 0 and current_player[0] == "white":
        print(f'Game over! {current_player[0].capitalize()} pawn is promoted to a queen at {col_str[new_col]}{row_str[new_row]}.')
        break
    if new_row == len(matrix) - 1 and current_player[0] == "black":
        print(f'Game over! {current_player[0].capitalize()} pawn is promoted to a queen at {col_str[new_col]}{row_str[new_row]}.')
        break
    the_players[0] = current_player
    the_players[0],the_players[1] = the_players[1],the_players[0]






