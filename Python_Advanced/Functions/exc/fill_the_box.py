def fill_the_box(height, length, width, *args):
    start_size = height * length * width
    size = height * length * width
    boxes = []
    for s in args:
        if s == "Finish":
            break
        else:
            boxes.append(s)
    current_boxes = 0
    for cube in boxes:
        if cube == "Finish":
            break
        if size >= cube:
            size -= cube
            current_boxes += cube
        elif size < cube:
            current_boxes += (cube - (cube - size))
            size = 0
            break
        if size <= 0:
            break
    if current_boxes < sum(boxes) and size == 0:
        return f"No more free space! You have {sum(boxes) - current_boxes} more cubes."
    if current_boxes == sum(boxes) and size >= 0:
        return f"There is free space in the box. You could put {start_size - current_boxes} more cubes."


print(fill_the_box(5, 5,

2, 40, 11, 7, 3, 1, 5,

"Finish"))