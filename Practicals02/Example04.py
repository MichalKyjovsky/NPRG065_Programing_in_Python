#! /usr/bin/env Python3 

import sys

lower_bound = int(sys.argv[1])
upper_bound = int(sys.argv[2])

if lower_bound > upper_bound:
    pom = lower_bound
    lower_bound = upper_bound
    upper_bound = pom

for i in range(lower_bound, upper_bound + 1): 
    for j in range(lower_bound, i):
        if i % j == 0:
            break
    else:
        print(i)
