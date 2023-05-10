def reverse_text(text):
    indx = -1
    while indx >= -len(text):
        yield text[indx]
        indx -= 1

for char in reverse_text("step"):
    print(char, end='')