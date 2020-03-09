#! /usr/bin/env Python3 
# Implementation of Selection sort

import sys


def selection_sort(arr):
   
    input_arr = []

    for item in arr:
        input_arr.append(int(item))

    for i in range(len(input_arr)):
        minimum = min(input_arr[i:])
        min_index = input_arr.index(minimum)
        pom = input_arr[i]
        input_arr[i] = minimum
        input_arr[min_index] = pom
    return input_arr

array_to_sort = sys.argv[1:]
print("Unsorted: {}".format(array_to_sort))
print("Sorted: {}".format(selection_sort(array_to_sort)))


