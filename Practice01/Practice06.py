#! /usr/bin/env Python3 

# Implement a program that returns a maximum, minimum and average of non-negative numbers given via cmd line arguments

import sys

def min_max_avg(args):
    arr = [0]*(len(args) - 1)

    for i in range(1,len(args)):
        arr[i - 1] = int(args[i])

    sum_of_arr = sum(arr)

    print('Maximum:')
    print(max(arr))
    print('Minimum:')
    print(min(arr))
    print('Average:')
    print(sum_of_arr / len(arr))

min_max_avg(sys.argv)
    
        
