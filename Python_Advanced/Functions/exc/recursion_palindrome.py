def palindrome(word, indx):
    if indx >= len(word) // 2:
        return f'{word} is a palindrome'

    leff = word[indx]
    right = word[-1 - indx]

    if leff != right:
        return f"{word} is not a palindrome"

    return palindrome(word, indx + 1)



print(palindrome("abcba", 0))
print(palindrome("peter", 0))