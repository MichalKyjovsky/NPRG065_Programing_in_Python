#! /usr/bin/env Python3 

# Implement a function that counts a factorial of its argument
import sys


def factorial():
    tmp = 1
    upperBound = sys.argv[1]

    for i in range(1, int(upperBound) + 1):
        tmp *= i

    print(tmp)


factorial()
