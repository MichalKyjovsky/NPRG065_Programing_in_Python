#!/usr/bin/env python3
# -*- coding: utf-8 -*-


##############
#          map
##############


# map(f, iterA, iterB, ...) returns an iterator over the sequence
#    f(iterA[0], iterB[0]), f(iterA[1], iterB[1]), f(iterA[2], iterB[2]), ...

def upper(s: str) -> str:
    """
    Return a copy of the string with all the characters converted to uppercase
    """
    return s.upper()


print(list(map(upper, ['sentence', 'fragment'])))

# or we can use the lambda function instead of the upper function
print(list(map(lambda s: s.upper(), ['sentence', 'fragment'])))

# but shorter and more "Pythonic" way is to use comprehensions
print([s.upper() for s in ['sentence', 'fragment']])


##############
#       filter
##############

# filter(predicate, iter) returns an iterator over all the sequence elements that satisfies the given predicate

def is_even(x: int) -> bool:
    """
    Test evenness of the given number.
    """
    return (x % 2) == 0


print(list(filter(is_even, range(10))))

# but as above, a better way is to use comprehensions
print([a for a in range(10) if (a % 2) == 0])


##############
#    enumerate
##############

# enumerate(iter, start=0) counts off the elements in the iterable returning 2-tuples containing the count (from start) and each element.

print([e for e in enumerate(['subject', 'verb', 'object'])])


##############
#       sorted
##############

# sorted(iterable, key=None, reverse=False) collects all the elements of the iterable into a list, sorts the list, and returns the sorted result.
# The key and reverse arguments are passed through to the constructed list’s sort() method.

import random
rand_list = random.sample(range(10000), 8)
print(rand_list)
print(sorted(rand_list))
print(sorted(rand_list, reverse=True))


##############
#     any & all
##############

# any() returns True if any element in the iterable is a true value
# all() returns True if all of the elements are true values

def print_and_apply(ls, f):
    print(f'{f.__name__}({ls}) -> {f(ls)}')


print_and_apply([0, 1, 0], any)
print_and_apply([0, 0, 0], any)
print_and_apply([1, 1, 1], any)
print_and_apply([0, 1, 0], all)
print_and_apply([0, 0, 0], all)
print_and_apply([1, 1, 1], all)


##############
#          zip
##############

# zip(iterA, iterB, ...) takes one element from each iterable and returns them in a tuple

print(list(zip(['a', 'b', 'c'], (1, 2, 3))))

# If the iterables are of different lengths, the resulting stream will be the same length as the shortest iterable.

print(list(zip(['a', 'b'], (1, 2, 3))))


##############
#     operator
##############

# The operator module containing a set of efficient functions corresponding to the intrinsic operators of Python

import operator

print(operator.add(5, 6))
print(dir(operator))

##############
#    functools
##############

# The module containing some higher-order functions
# a higher-order functions ~ functions over functions

# partial()

# partial() "prefills" arguments of a given function
# It takes the arguments (function, arg1, arg2, ..., kwarg1=value1, kwarg2=value2).
# The resulting object is callable, so you can just call it to invoke function with the filled-in arguments.

import functools


def log(message, subsystem):
    """Write the contents of 'message' to the specified subsystem."""
    print('%s: %s' % (subsystem, message))


server_log = functools.partial(log, subsystem='server')
server_log('Unable to open socket')


# reduce()

# reduce(func, iter, [initial_value]) cumulatively performs an operation on all the iterable’s elements
print(functools.reduce(operator.add, [1, 2, 3, 4]))
print(functools.reduce(operator.mul, [1, 2, 3, 4], 1))
