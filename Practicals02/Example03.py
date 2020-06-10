#! /usr/bin/env Python3 

import sys

number = sys.argv[1]

number_str_arr = [number, number * 2, number * 3]
buffer_n = 0

for i in number_str_arr:
    buffer_n += int(i)

print(buffer_n)
