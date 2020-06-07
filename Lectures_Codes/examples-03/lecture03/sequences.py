#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# let's create several lists

alist1 = [1, 2, 3, 4, 5]
alist2 = ['a', 'b', 'c', 'd', 'e']

alist3 = []  # empty list
alist4 = list()  # Also creates an empty list. As an argument, anything iterable can be used and a list is created from it.

print(len(alist1))  # The builtin len() function returns the number of elements in a list

print(alist1[0])   # Prints out 0-th element of a list

# A negative index is relative to the end of sequence (-0 is still 0)
print(alist1[-1])  # Prints out the last element of a list

print(alist1)      # Prints out a whole list

alist1[0] = 100    # Lists are mutable
print(alist1)

alist1[1:3] = [101, 102, 103]  # We can replace several elements
print(alist1)

alist1[len(alist1):] = [6]  # We can append new elements
print(alist1)

alist1.append(7)   # But easier for appending is to call the append() method
print(alist1)

alist1[5:] = []    # We can remove elements from the list. The 5: means from the 5th element till end (and :5 would mean from beginning till 5th element
print(alist1)

copy_list = alist1[:]  # Copy of a list (a new list object but with same elements).

del alist1[4]      # The del operator can be used for removing elements too
print(alist1)

alist5 = alist1 + alist2   # + creates a new list
print(alist5)
# The above concatenation creates a "heterogeneous" list (contains ints and strings). It is possible but not advisable.

# The for cycle in Python iterates over iterable entities, e.g., lists, etc
for a in alist2:
    print(f' iterating over a list: {a}')

# Lists have many methods. Let's examine them.
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print('List of fruits: {}'.format(fruits))
print('How many apples are in the list: {}'.format(fruits.count('apple')))
print('How many tangerines are in the list: {}'.format(fruits.count('tangerine')))
print('Position of banana: {}'.format(fruits.index('banana')))
print('Position of banana starting a position 4: {}'.format(fruits.index('banana', 4)))
fruits.reverse()
print('Reversed list: {}'.format(fruits))
fruits.sort()
print('Sorted list: {}'.format(fruits))

# List can be used as stacks
fruits.append('grape')
print('Appended grape: {}'.format(fruits))
print('Pop removes and returns the last element "{}", resulting list {}'.format(fruits.pop(), fruits))

# Tuples are similar to list but immutable
atuple1 = (1, 2, 3, 4)
atuple2 = ('a', 'b', 'c', 'd')
nested_tuple = (atuple1, atuple2)
print(nested_tuple)

empty_tuple = ()

# We unpack tuples
a1, a2, a3, a4 = atuple1
print('{} {} {} {}'.format(a1, a2, a3, a4))

# We can iterate over tuples
for i in atuple1:
    print(f' element of the tuple: {i}')

# We can access individual elements in tuples
print(atuple1[0])

# But we cannot modify them
# Uncomment the following line to get an exception
# atuple1[0] = 1
