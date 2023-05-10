import io
with io.open('.\\text.txt', 'r') as file:
    line_nr = 0
    new_line = ''
    symbols = {"-", ",", ".", "!", "?"}
    for line in file:
        if line_nr % 2 == 0:
            for s in line.strip():
                if s in symbols:
                    line = line.replace(s, '@')
            line_nr += 1
            spl_line = line.split()
            
            new = list(reversed(spl_line))
            print(' '.join(new))
        else:
            line_nr += 1
