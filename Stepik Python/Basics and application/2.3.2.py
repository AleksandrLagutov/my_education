import itertools
def primes():
    a = 2
    while True:
        flag = True
        for i in range(2, int(a**0.5) + 1):
            if a % i == 0 and i != a:
                flag = False
        if flag:
            yield  a
        a += 1


print(list(itertools.takewhile(lambda x : x <= 31, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]