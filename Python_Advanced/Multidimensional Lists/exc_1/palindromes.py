n, m = [int(x) for x in input().split()]


mm = []

for row in range(n):
    current_row = []
    for column in range(m):
        current_item = ""
        first_last = 97 + row
        middle = 97 + row + column
        current_item += chr(first_last) + chr(middle) + chr(first_last)
        current_row.append(current_item)
    mm.append(current_row)

for the_row in mm:
    print(" ".join(the_row))