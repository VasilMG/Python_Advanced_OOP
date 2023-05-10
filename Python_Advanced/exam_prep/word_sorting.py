def words_sorting(*args):
    the_words = {}
    for k in args:
        the_words[k] = sum(ord(x) for x in k)
    the_sum = 0
    for v in the_words.values():
        the_sum += v
    if the_sum % 2 == 0:
        return '\n'.join([f'{k} - {v}' for k, v in sorted(the_words.items(), key= lambda x: x[0])])
    if the_sum % 2 != 0:
        return '\n'.join([f'{k} - {v}' for k, v in sorted(the_words.items(), key= lambda x: -x[1])])

print(

words_sorting(

'escape',

'charm',

'mythology',

    'charm'

))