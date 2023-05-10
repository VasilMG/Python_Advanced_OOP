text = input()
symbbol = {}

for i in text:
    if i not in symbbol:
        symbbol[i] = 1
    else:
        symbbol[i] += 1
        
for key, value in sorted(symbbol.items()):
    print(f"{key}: {value} time/s")