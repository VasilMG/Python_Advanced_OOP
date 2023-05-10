def get_primes(list):
    for i in list:
        if i > 1:
            for j in range(2, int(i /2) + 1):
                if i % j == 0:
                    break
            else:
                yield i






# print(list(get_primes([-2, 0, 0, 1, 1, 0])))


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))