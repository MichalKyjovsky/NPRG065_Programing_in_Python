#!/usr/bin/env python3

# Computing Fibonacci numbers in multiple ways


def fib(a):
    if a < 1:
        return 1
    else:
        return fib(a - 1) + fib(a - 2)


def fib2(a):
    prev = 1
    prevprev = 1
    while a > 0:
        tmp = prev + prevprev
        prevprev = prev
        prev = tmp
        a -= 1
    return prev


print(fib(10))
print(fib2(10))
