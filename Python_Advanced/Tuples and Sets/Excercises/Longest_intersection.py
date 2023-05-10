n = int(input())
intersection_lenght = 0
the_longest = {}

for i in range(n):
    command = input().split("-")
    start_one , end_one = command[0].split(",")
    start_two , end_two = command[1].split(",")
    first_set = set(x for x in range(int(start_one), int(end_one) + 1))
    second_set = set(y for y in range(int(start_two), int(end_two) + 1))
    intersection = first_set.intersection(second_set)
    if len(intersection) > intersection_lenght:
        intersection_lenght = len(intersection)
        the_longest = intersection
    
the_list = list(the_longest)
print(f"Longest intersection is {the_list} with length {intersection_lenght}")
