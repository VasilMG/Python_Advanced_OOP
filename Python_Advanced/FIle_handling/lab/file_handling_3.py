from os import remove
from os.path import exists
# if the path exists ---> os.remove or remove(path_name) i iztriva file.
#
#
# file = open('.\\my_first_file.txt', 'w')
# file.write('Yeeeeee')
# file.close()

import io
import  re
def read_words():
    with open('words.txt', 'r') as file_words:
        return file_words.read().split(" ")

def count_words_in_file(words):
    words_count = {
        word: 0 for word in words
    }
    with open('input.txt', 'r') as file_input:
        for line in file_input:
            words_in_line = [w.lower() for w in re.findall(r'\b\S+\b', line)]
            for word in words:
                words_count[word] += words_in_line.count(word.lower())
    return  words_count

print('\n'.join([f'{k} -- {v}' for k, v in sorted(count_words_in_file(read_words()).items(), key= lambda x: -x[1])]))