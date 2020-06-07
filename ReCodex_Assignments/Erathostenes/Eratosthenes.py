from sys import stdin
from math import sqrt


def eratosthenes(upper_bound: int):
    if upper_bound < 2:
        return 0
    else:
        primes_arr = [True] * upper_bound
        primes_arr[0] = False
        primes_arr[1] = False
        index = 2
        limit = sqrt(upper_bound)

        while index < limit:
            if primes_arr[index]:
                j_index = index ** 2
                while j_index < upper_bound:
                    primes_arr[j_index] = False
                    j_index += index
            index += 1

    return sum(primes_arr)


print(eratosthenes(int(stdin.readline())))
