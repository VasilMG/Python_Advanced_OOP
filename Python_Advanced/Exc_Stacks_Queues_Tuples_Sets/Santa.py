from collections import deque
materials = [int(x) for x in input().split()]
magic = deque([int(x) for x in input().split()])

crafting_table = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

crafted_toys = {}

while materials and magic:
    current_material = materials.pop()
    the_magic = magic.popleft()
    result = current_material * the_magic

    if current_material == 0 and the_magic == 0:
        continue
    if current_material == 0:
        magic.appendleft(the_magic)
        continue
    if the_magic == 0:
        materials.append(current_material)
        continue

    if result in crafting_table:
        toy_name = crafting_table[result]
        if toy_name in crafted_toys:
            crafted_toys[toy_name] += 1
        else:
            crafted_toys[toy_name] = 1
        continue

    if result < 0:
        materials.append(current_material + the_magic)

    else:
        materials.append(current_material + 15)


if ("Doll" in crafted_toys and "Wooden train" in crafted_toys) or ("Teddy bear" in crafted_toys and "Bicycle" in crafted_toys):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")


if materials:
    print(f"Materials left: {', '.join([str(x) for x in reversed(materials)])}")
if magic:
    print(f"Magic left: {', '.join([str(x) for x in magic])}")


for toy, count in sorted(crafted_toys.items()):
    print(f"{toy}: {count}")