food_portions = list(reversed([int(x) for x in input().split(', ')]))
stamina_portions = [int(x) for x in input().split(', ')]
daily_portions = [food_portions[x] + stamina_portions[x] for x in range(len(food_portions))]

peaks = (('Vihren', 80), ('Kutelo', 90), ('Banski Suhodol', 100), ('Polezhan', 60), ('Kamenitza', 70))

indx= 0
climbed = []
for power in daily_portions:
    if len(climbed) == 5:
        break
    if indx >= 4:
        indx = 4
    if power < peaks[indx][1]:
        continue
    elif power >= peaks[indx][1]:
        climbed.append(peaks[indx][0])
        indx += 1

if len(climbed) == 5:
    print(f"Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print(f"Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if climbed:
    print("Conquered peaks:")
    print(*climbed, sep='\n')
