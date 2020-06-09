#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum


# Let's have plain enum
# The enum elements are effectively constants
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


red = Color.RED    # We can assign the enum elements
print(red)         # and print them

if red is Color.RED:    # We can compare the values
    print('It is red')
else:
    print('It is not red')

print('Iteration')
for color in Color:     # We can iterate over the elements
    print(color)        # Order of iteration is order of the definition

# The enum elements are instances of the particular enum
print('Testing isinstance(red, Color)')
print(isinstance(red, Color))


# There is no need to order the values
class TrafficLight(Enum):
    YELLOW = 2
    GREEN = 3
    RED = 1


for light in TrafficLight:   # Still iterating in the order of definition
    print(light)


# We can have values of a different type
class Direction(Enum):
    LEFT = 'left'
    RIGHT = 'right'


for direction in Direction:
    print(f'Name: {direction.name}, Value: {direction.value}')   # We can access the element's name and value

# We can access elements via their value
green = Color(2)
print(green)

# We cannot have two elements with the same name
# Uncomment the following to obtain an error
#class BadColor(Enum):
#    RED = 1
#    RED = 2


# But we can have two elements with the same value (but is not ideal)
class Shape(Enum):
    SQUARE = 2
    DIAMOND = 1
    CIRCLE = 3
    ALIAS_FOR_SQUARE = 2


square = Shape(2)     # returns the first element with the given value
print(square)


from enum import unique


# We can ensure the uniqueness of the values
# Uncomment the last element to obtain an error
@unique
class UniqueShape(Enum):
    SQUARE = 2
    DIAMOND = 1
    CIRCLE = 3
#    ALIAS_FOR_SQUARE = 2


from enum import auto


# If the values are not important, we can ask for some values
class AutoColor(Enum):
    RED = auto()
    BLUE = auto()
    GREEN = auto()


for color in AutoColor:
    print(f'Name: {color.name}, Value: {color.value}')


# The __members__ attribute holds a dictionary with name:element pairs

for name, element in AutoColor.__members__.items():
    print(f'Name: {name}, Element: {element}')


# Enums are classes and can have methods (and anything else like regular classes)
class Snake(Enum):
    PYTHON = 1
    VIPER = 2

    def say(self):
        print(f'{self.name} says hiss')


python = Snake.PYTHON
python.say()


# We cannot extend enums
# Uncomment the following lines to obtain an error
#class MoreColor(Color):
#    BLACK = 4

# We can define enums programmatically
# The definition below is equivalent to
# class Animal(Enum):
#    ANT = 1
#    BEE = 2
#    CAT = 3
#    DOG = 4
Animal = Enum('Animal', 'ANT BEE CAT DOG')

for i in Animal:
    print(i)


from enum import IntEnum


# IntEnum - an enum that is also int
# Elements behave like ints
class Digit(IntEnum):
    ZERO = 0
    ONE = 1
    TWO = 2


if Digit.ZERO == 0:
    print(f'{Digit.ZERO} is equal to 0')
else:
    print(f'{Digit.ZERO} is not equal to 0')

alist = ['a', 'b', 'c']
print(alist[Digit.ONE])

print([i for i in range(Digit.TWO)])


# IntFlag is like IntEnum, but additionally can be combined using the bitwise operators (&, |, ^, ~) and the result is still an IntFlag member.
from enum import IntFlag


class Perm(IntFlag):
    R = 4
    W = 2
    X = 1


print(Perm.R | Perm.W)
RW = Perm.R | Perm.W
print(Perm.R in RW)

