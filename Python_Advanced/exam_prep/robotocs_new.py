from collections import  deque

def seconds_to_string(seconds):
    seconds %= 24 * 60 * 60

    hours = seconds // (60 * 60)
    seconds %= (60 * 60)
    minutes = seconds // 60
    seconds %= 60

    return  f'[{hours:02d}:{minutes:02d}:{seconds:02d}]'

the_robots = input().split(';')
robots = {}

for i in range(len(the_robots)):
    name, w_time = the_robots[i].split('-')
    robots[name] = {}
    robots[name]["w_time"] = int(w_time)
    robots[name]["ready"] = -1

hours, minutes, secs = [int(x) for x in input().split(':')]
time_in_secs = (hours * 3600) + (minutes*60) + secs
items = deque()

while True:
    command = input()
    if command == 'End':
        break
    items.append(command)

while items:
    product = items.popleft()
    time_in_secs += 1
    free_robot = 0
    for key in robots:
        if time_in_secs >= robots[key]['ready']:
            robots[key]['ready'] = time_in_secs + robots[key]["w_time"]
            print(f"{key} - {product} {seconds_to_string(time_in_secs)}")
            free_robot += 1
            break

    if free_robot == 0:
        items.append(product)








