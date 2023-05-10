from os import listdir
from os.path import isdir, join

def directory(path, files_by_extention):
    for element in listdir(path):
        if isdir(join(path, element)):
            directory(join(path, element), files_by_extention)
        else:
            extention = element.split('.')[-1]
            if extention not in files_by_extention:
                files_by_extention[extention] = []
            files_by_extention[extention].append(element)

result = {}
directory('.\\', result)

for k, v in result.items():
    print(f'{k} -->{v}')