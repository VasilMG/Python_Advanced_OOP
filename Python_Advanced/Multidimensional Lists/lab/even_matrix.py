def read_matrix():
    n = int(input())
    matrix = []
    for _ in range(n): # nr of rows
        row = [int(x) for x in input().split(", ")]
        matrix.append(row)
    return matrix


mm = read_matrix()

print([[x for x in row if x % 2 == 0] for row in mm])