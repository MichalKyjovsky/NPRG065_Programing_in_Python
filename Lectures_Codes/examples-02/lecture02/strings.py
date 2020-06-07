#!/usr/bin/env python3


# Both single and double quotes can be used for string literals.

str1 = 'Single quotes allows embedded "double" quotes'

str2 = "Double quotes allows embedded 'single' quotes"

str3 = '''Triple quoted strings may
span multiple
lines'''

str4 = ('we can break ' 'long strings '
        'even over ' 'multiple '
        'lines')

print(str4)

print('\\Escape sequences\\ can be used like in Java \u263a \n but there are more possibilities, e.g., \x40')

print(r'Within "raw strings", nothing is interpreted \u263a \\ \\')


# Commonly, we need to create a string composed of multiple other objects, i.e., something like the printf function.
# The string's format method is the answer.

# {<number>} is replaced with corresponding positional argument of the format method
print('{0} + {1} = {2}'.format(1, 2, 1 + 2))

# If the the arguments are used in sequence, numbers can be skipped
print('{} + {} = {}'.format(1, 2, 1 + 2))

# Similar formatting characters like in C can be used
print('int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}'.format(42))
print('float: {0:.2f}'.format(1/3))

# Or using named arguments
print('Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W'))


# And there are a huge number of other possibilities of the format method
# see https://docs.python.org/3.7/library/string.html#formatstrings

# Since Python 3.6, the formatted strings can be used - they are prefixed by f and implicitly employ the format method
# In the curly braces, variables etc. can be used directly

var = 42
print(f'int: {var:d};  hex: {var:x};  oct: {var:o};  bin: {var:b}')

number = 1024
print(f'{number:#0x}')

# Strings have many useful methods.
# To list all the methods (and other elements) of objects, we can use the builtin function dir().


print(dir('Python'))   # list all the methods of the object

print('no capital char at the beginning'.capitalize())

print('Python'.find('on'))  # if we want to find an exact position of a substring

print('on' in 'Python')  # if we want only to test existence of a substring, the in operator is a better option

print('Python'.startswith('Py'))
print('Python'.endswith('on'))

print('1,2,3'.split(','))  # returns a list with elements

# WARNING: there are no length or size methods. Instead, the builtin len() function is used.
# It is used for any Python type (lists, etc.) that has a semantics of a container with elements.

print(len('Python'))  # contains six characters


# Strings are iterable, so we can use them in the for loop

print('Iterating over a string')
for c in 'Python':
    print(f' {c}')
