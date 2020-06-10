#! /usr/bin/env Python3 

# Implement a function that prints out its cmd line arguments in reverse order

import sys


def reverse_order(arguments):
    for i in range(len(arguments) - 1, 0, -1):
        print(arguments[i])


reverse_order(sys.argv)
