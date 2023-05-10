text = input()
stack = []

for i in range(len(text)):
    chr = text[i]
    if chr == "(":
        stack.append(i)
    if chr == ")":
        last_open = stack.pop()
        new_subexpression = text[last_open: i + 1]
        print(new_subexpression)
    
    
