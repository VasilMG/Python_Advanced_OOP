from collections import deque
dd = {}
flowers = ["rose", "tulip", "lotus", "daffodil"]
the_words = {}
for i in flowers:
    word = ""
    for j in range(len(i)):
        if i[j] not in word:
            word += i[j]
    the_words[word] = {}
    the_words[word]['found'] = set()
    the_words[word]['name'] = i

vowels = deque(x for x in input().split())
consonants = deque(x for x in input().split())
word_found = ""
while vowels and consonants:
    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()
    for k in the_words:
        if current_vowel in k:
            the_words[k]['found'].add(current_vowel)

        if current_consonant in k:
            the_words[k]['found'].add(current_consonant)
    for k, v in the_words.items():
        if len(k) == len(v['found']):
            word_found = the_words[k]['name']
            break
    if len(word_found) > 0:
        break

if word_found:
    print(f"Word found: {word_found}")
    if vowels:
        print(f"Vowels left: {' '.join(vowels)}")
    if consonants:
        print(f"Consonants left: {' '.join(consonants)}")
else:
    print(f"Cannot find any word!")
    if vowels:
        print(f"Vowels left: {' '.join(vowels)}")
    if consonants:
        print(f"Consonants left: {' '.join(consonants)}")






