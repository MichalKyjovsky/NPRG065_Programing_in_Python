#!/usr/bin/env python3


def fib(a):
    prev = 1
    prevprev = 1
    while a > 0:
        tmp = prev + prevprev
        prevprev = prev
        prev = tmp
        a -= 1
    return prev


if __name__ == "__main__":
    import sys
    print(fib(int(sys.argv[1])))
