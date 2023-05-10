from collections import deque
seats = input().split(', ')
firs_line = deque([int(x) for x in input().split(', ')])
second_line = deque([int(x) for x in input().split(', ')])

turns = 0
taken_seats = []

while True:
    number_one = firs_line.popleft()
    number_two = second_line.pop()
    letter = chr(number_one + number_two)
    combinations = [(str(number_one) + letter), (str(number_two) + letter)]
    for item in combinations:
        if item in taken_seats:
            continue
        if item in seats:
            taken_seats.append(item)
            seats.remove(item)
            break
    else:
        firs_line.append(number_one)
        second_line.appendleft(number_two)
    turns += 1
    if turns == 10 or len(taken_seats) == 3:
        break

print(f'Seat matches: {", ".join(taken_seats)}')
print(f'Rotations count: {turns}')
