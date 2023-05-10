from collections import deque
elves = deque([int(x) for x in input().split()])
boxes = deque([int(x) for x in input().split()])

total_energy = 0
made_toys = 0

count = 0

while len(elves) > 0 and len(boxes) > 0:
    current_elf = elves.popleft()
    if current_elf < 5:
        continue
    current_box = boxes.pop()
    count += 1
    if current_elf >= current_box:
        if count % 3 == 0 and count % 5 == 0:
            if current_elf >= 2 * current_box:
                current_elf -= 2 * current_box
                total_energy += 2 * current_box
                elves.append(current_elf)
            else:
                continue
        elif count % 5 == 0:
            if current_elf >= current_box:
                current_elf -= current_box
                total_energy += current_box
                elves.append(current_elf)
            else:
                continue

        elif count % 3 == 0:
            if current_elf >= current_box * 2:
                current_elf -= 2 * current_box
                total_energy += current_box * 2
                made_toys += 2
                current_elf += 1
                elves.append(current_elf)
            else:
                current_elf = current_elf *2
                boxes.append(current_box)
                elves.append(current_elf)
                continue

        else:
            current_elf -= current_box
            total_energy += current_box
            made_toys += 1
            current_elf += 1
            elves.append(current_elf)

    else:
        boxes.append(current_box)
        current_elf = current_elf * 2
        elves.append(current_elf)


print(f"Toys: {made_toys}")
print(f"Energy: {total_energy}")

if elves:
    print(f"Elves left: {', '.join([str(x) for x in elves])}")

if boxes:
    print(f"Boxes left: {', '.join([str(x) for x in boxes])}")