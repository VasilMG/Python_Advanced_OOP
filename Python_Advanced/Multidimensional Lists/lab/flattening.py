def read_matrix():
    n = int(input())
    matrix = []
    for _ in range(n): # nr of rows
        row = [int(x) for x in input().split(", ")]
        matrix.append(row)
    return matrix


mm = read_matrix()
ll = [x for row in mm for x in row]

print(ll)