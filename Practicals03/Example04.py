#! /usr/bin/env Python3 


import sys

input_word = sys.argv[1]
count = 0
checker = []

for letter in input_word:
    if letter in checker:
        continue
    for char in input_word:
        if letter == char:
            count += 1
    print('{}: {}'.format(letter, count))
    count = 0
    checker.append(letter)

