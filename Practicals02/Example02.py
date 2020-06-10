#! /usr/bin/env Python 3

import sys
import os

input_str = sys.argv[1]
input_arr = input_str.split(os.sep)
input_arr.pop(0)

for i in input_arr:
    print(i)
