def get_line(i, n):
    spaces_count = n - 1 - i
    star_count = i + 1
    return ' ' * spaces_count + "* " * star_count

def print_rhombus(n):
    for i in range(n):
        print(get_line(i, n))
    for i in range(n-2 , -1, -1):
        print(get_line(i, n))




print_rhombus(int(input()))