n = int(input())

even = set()
odd = set()
for row in range(1, n + 1):
    name = input()
    the_sum_divided = sum([ord(char) for char in name]) // row
    if the_sum_divided % 2 == 0:
        even.add(the_sum_divided)
    else:
        odd.add(the_sum_divided)
        
even_sum = sum(even)
odd_sum = sum(odd)

if even_sum == odd_sum:
    result = even.union(odd)
elif even_sum > odd_sum:
    result = odd.symmetric_difference(even)
else:
    result = odd.difference(even)
    
print(*result, sep=", ")