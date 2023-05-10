
first_line = set([int(x) for x in input().split()])
second_line = set([int(x) for x in input().split()])
n = int(input())

for the_command in range(n):
    initial_command = input().split()
    command = [ x for x in initial_command if x.isalpha()]
    the_sequence = set([int(y) for y in initial_command if y.isdigit()])

    if command[0] == "Add":
        if command[1] == "First":
            first_line = first_line.union(the_sequence)
        if command[1] == "Second":
            second_line = second_line.union(the_sequence)
    elif command[0] == "Remove":
        if command[1] == "First":
            first_line = first_line.difference(the_sequence)
        if command[1] == "Second":
            second_line = second_line.difference(the_sequence)
    else:

        if first_line.issubset(second_line) or second_line.issubset(first_line):
            print("True")
        else:
            print("False")

print(*sorted(first_line), sep=", ")
print(*sorted(second_line), sep=", ")