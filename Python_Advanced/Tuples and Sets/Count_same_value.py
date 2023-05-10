text = [float(x) for x in input().split()]
times_count = {}
for number in text:
    if number not in times_count:
        times_count[number] = 0
    times_count[number] += 1
    
for key in times_count:
    print(f"{key} - {times_count[key]} times")

