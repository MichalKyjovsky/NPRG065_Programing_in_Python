#!/usr/bin/env python3

import sys  # we will need the several modules later
import math

# Let's play more with numbers.
# To determine a type of any object, we can use the builtin function type().

###########################################
#                                         #
#  ints                                   #
#                                         #
###########################################

print(type(1))  # The type of 1 is int.

# OK, int is a class. But is not it inefficient to have even integers instances of a class?
# No, it is not. Internally, the Python uses "primitive" type to hold integer values.

print(type(2 ** 1000))   # The type of "large" integers is also int. But it definitely cannot be stored to the "primitive" int.

# For "large" integers, the Python uses (transparently) a different internal representation (a sequence of numbers).
# Where is the boundary between "regular" and "large" integers?

print(sys.maxsize)  # The largest of the regular integer values

# How many bits the regular integers occupy?
print(math.log(sys.maxsize, 2))

# Is not computing with int objects inefficient?
# For the commonly used numbers (-5 to 256) Python creates a pool of objects that are reused
# Let's check it with the id() function
# Note: id() returns a unique identification of an object
# In CPython it is the address of the object in memory

print(f'id(1) = {id(1)}')
print(f'id(2) = {id(2)}')
print('id(1 + 1) has to be the same value as id(2)')
print(f'id(1 + 1) = {id(1 + 1)}')
print('But it is not true for ints outside -5..256 interval')
print(f'id(257) = {id(257)}')
print(f'id(256 + 1) = {id(256 + 1)}')

###########################################
#                                         #
#  Decimal and Fraction                   #
#                                         #
###########################################

# Floats are nice but inherently imprecise. Let's consider the following comaparison.
# It should be evaluated to True, but it is not (0.1 cannot be exactly represented in float}

print(0.1 + 0.1 + 0.1 == 0.3)

print(1/10 + 1/10 + 1/10 == 3/10)  # Even this is not true.

# 0.1 cannot be precisely represented
# Let's try to print 0.1
print(f'Printing 0.1: {0.1}')
# It prints 0.1, but by default, only a limited number of significant digits is printed
# Let's try to print 0.1 to 20 significant digits
print(f'Printing 0.1 to 20 significant digits: {0.1:.20g}')


# But sometimes precise arithmetic is needed (e.g., counting money]).
# Let's use Decimal and Fraction types.
# They are not builtin types, i.e., they need to be imported, but they are in the Python standard library.


from decimal import Decimal   # Decimal - precise float-point numbers
# from - import  imports the given entity to be used by a 'short' name only
# We can also use import decimal.Decimal but then it would be necessary to use the long name
# end, even more, it could have performance penalties

print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') == Decimal('0.3'))  # Now, it is true


from fractions import Fraction  # Fraction - precise fractions

print(Fraction(1, 10) + Fraction(1, 10) + Fraction(1, 10) == Fraction(3, 10))  # This is also true
