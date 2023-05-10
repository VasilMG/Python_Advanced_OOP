from os import listdir
from os.path import isdir, join

def directory(path, files_by_extention={}):
    for element in listdir(path):
        if isdir(join(path, element)):
            continue
        else:
            extention = element.split('.')[-1]
            if extention not in files_by_extention:
                files_by_extention[extention] = []
            files_by_extention[extention].append(element)
        result = {}
        for k, v in files_by_extention.items():
            result[k] = sorted(v)
    return result

all_files = directory('.\\')
print(all_files)

with open('.\\report.txt', 'w') as file:
    for k, v in sorted(all_files.items()):
        file.write(f'.{k}' + '\n')
        file.write('\n'.join([f'- - - {x}' for x in v]))
        file.write('\n')


