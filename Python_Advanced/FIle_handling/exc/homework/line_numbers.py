import io
from io import open
from string import punctuation

x = {x for x in punctuation}
print(x)


with open('.\\text.txt', 'r') as file_input, open('.\\output.txt', 'w') as output:
    for indx, line in enumerate(file_input):
        the_letters = len([x for x in line if x.isalpha()])
        the_symbols = len([x for x in line if x in punctuation])
        output.write(f'Line {indx + 1}: {line.strip()} ({the_letters})({the_symbols})\n')