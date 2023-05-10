from collections import  deque
the_green_light = int(input())
the_free_window = int(input())

cars = deque()
passed_count = 0
crached = False

while not crached:
    command = input()
    if command == 'END':
        print("Everyone is safe.")
        print(f"{passed_count} total cars passed the crossroads.")
        break

    if command != 'green':
        cars.append(command)
    if command == 'green':
        green_light = the_green_light
        free_window = the_free_window
        while cars:
            current_car = cars.popleft()
            if len(current_car) < green_light:
                passed_count += 1
                green_light -= len(current_car)
            elif len(current_car) <= green_light + free_window or len(current_car) == green_light:
                passed_count += 1
                break
            elif len(current_car) > green_light + free_window:
                indx = green_light + free_window
                print("A crash happened!")
                print(f"{current_car} was hit at {current_car[indx]}.")
                crached = True
                break

            if green_light == 0:
                break
