#!/usr/bin/env python3

# Printing out multiplication table of a given number


def multi(number):
    print('Multiplication table of ', number)
    for i in range(11):
        print(i * number)


multi(5)
