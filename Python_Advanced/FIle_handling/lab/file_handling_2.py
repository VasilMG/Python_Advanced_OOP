import io

file = io.open('numbers.txt')
the_sum = 0
for line in file:
    num = int(line)
    the_sum += num

print(the_sum)