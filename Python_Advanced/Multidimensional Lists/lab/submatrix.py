import sys
from io import StringIO

testing_one = '''3, 6
7, 1, 3, 3, 2, 1
1, 3, 9, 8, 5, 6
4, 6, 7, 9, 1, 0
'''

testing_two = '''2, 4
10, 11, 12, 13
14, 15, 16, 17
'''


sys.stdin = StringIO(testing_one)






def read_matrix():
    n, m = [int(x) for x in input().split(", ")]
    matrix = []
    for _ in range(n): # nr of rows
        row = [int(x) for x in input().split(", ")]
        matrix.append(row)
    return matrix

mm = read_matrix()
print(mm)