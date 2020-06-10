#! /usr/bin/env Pyrhon3 

# Implement a program that prints out a multiplication table for a number given as its cmd line argument

import sys


def multiplication_table(arg):
    for i in range(1, 11):
        print(str(i) + ' * ' + str(int(arg)) + ' = ' + str(i * (int(arg))))


multiplication_table(sys.argv[1])
