import sys
from io import StringIO

testing_one = '''3, 6
7, 1, 3, 3, 2, 1
1, 3, 9, 8, 5, 6
4, 6, 7, 9, 1, 0
'''

testing_two = '''3, 6
7, 1, 3, 3, 2, 1
1, 3, 9, 8, 5, 60
4, 6, 7, 9, 10, 10
'''



sys.stdin = StringIO(testing_one)



n, m = [int(x) for x in input().split(", ")]
matrix = []
for _ in range(n): # nr of rows
    row = [int(x) for x in input().split(", ")]
    matrix.append(row)

the_sum = float("-inf")
the_winner = []

for the_row in range(n-1):
    for the_col in range(m -1):
        current_sum = matrix[the_row][the_col] + matrix[the_row][the_col +1] + matrix[the_row + 1][the_col] + matrix[the_row + 1][the_col + 1]
        if current_sum > the_sum:
            current_box = []
            the_sum = current_sum
            current_box.append(f"{matrix[the_row][the_col]} {matrix[the_row][the_col+1]}")
            current_box.append(f"{matrix[the_row + 1][the_col]} {matrix[the_row + 1][the_col + 1]}")
            the_winner = current_box



for w in the_winner:
    print(" ".join(w.split()))

print(the_sum)
