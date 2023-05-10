import sys
from io import StringIO

testing_one = '''3
1, 2, 3
4, 5, 6
7, 8, 9
'''

sys.stdin = StringIO(testing_one)


def read_matrix():
    n = int(input())
    matrix = []
    for _ in range(n): # nr of rows
        row = [int(x) for x in input().split(", ")]
        matrix.append(row)
    return matrix

mm = read_matrix()

primary_sum = 0
secondary_sum = 0
l_primary = []
l_secondary = []

for i in range(len(mm)):
    primary_sum += mm[i][i]
    secondary_sum += mm[i][len(mm) - i - 1]
    l_primary.append(mm[i][i])
    l_secondary.append(mm[i][len(mm) - i - 1])

print(f"Primary diagonal: {', '.join([str(x) for x in l_primary])}. Sum: {primary_sum}")
print(f"Secondary diagonal: {', '.join([str(x) for x in l_secondary])}. Sum: {secondary_sum}")