#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Let's have a very simple function
def say_hello():
    print('Hello world')


# Now, we can call it
say_hello()

# Functions are first class objects.
# We can e.g., assign them
print_hello = say_hello

# Now, we can call the function via two names
print_hello()


# Now let's examine the parameters

# Let's have a function with both positional and keyword parameters
def my_print(msg, optional_message=''):
    print(optional_message, msg)


my_print(5)    # we can call it with the positional argument only
my_print(6, optional_message='output> ')   # we can specify both of them
my_print(7, 'cmd>')   # and even we can use the keyword one as a positional one (then the order of keyword ones is important)


# With the modified function, we can call it only with all arguments specified
def my_print2(msg, optional_message, optional_suffix):
    print(optional_message, msg, optional_suffix)


my_print2(5, 'output> ', ' <')   # we can call it with positional arguments
my_print2(5, optional_suffix=' <', optional_message='output> ')  # but also with keyword arguments - note that we can change the order


# Let's modify it further
def my_print3(msg, *, optional_message, optional_suffix):
    print(optional_message, msg, optional_suffix)


# Now, we can call it only with the last two arguments as keyword ones
my_print3(5, optional_suffix=' <', optional_message='output> ')
# my_print3(5, 'output> ', ' <')


# What if do not know number of arguments?
def print_all(*args):
    print(args)     # in the function, args is a tuple
    for a in args:
        print(' within print_all ', a)


print_all('hello', 'world', '!')


# Similarly, we can define a function to be usable with any number of keyword arguments
def keyword_function(**kwargs):
    print(kwargs)  # here, it is available as a dict
    for k in kwargs:
        print(' within keyword_function {} {}'.format(k, kwargs[k]))


keyword_function(arg1='value1', arg2='value2', arg3='value3')


# And of course, we can mix all of the approaches together
def position_and_keyword_function(pos1, pos2, *args, **kwargs):
    print(f' positional pos1={pos1} pos2={pos2}')
    print(f' var-positional args={args}')
    print(f' var-keyword args={kwargs}')


position_and_keyword_function(1, 2)   # arguments for pos1 and pos2 parameters are always required
position_and_keyword_function(1, 2, 3, 4)   # Additional positional arguments are in args
position_and_keyword_function(1, 2, 3, 4, arg1='value1', arg2='value2', arg3='value3')   # And we can add other keyword arrguments


# For var-positional and var-keyword arguments, we can use tuples and dicts, but we need to unpack them

atuple = (1, 2, 3, 4)
adict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

print_all(*atuple)
keyword_function(**adict)
position_and_keyword_function(1, 2, *atuple, **adict)


# Functions can be defined in functions
# e.g., to hide an implementation
def factorial(number):
    # error handling
    if not isinstance(number, int):
        return -1    # better would be to throw an exeption here
    if not number >= 0:
        return -1

    def inner_factorial(number):
        if number <= 1:
            return 1
        return number*inner_factorial(number-1)
    return inner_factorial(number)


print('Factorial of {} is {}'.format(10, factorial(10)))


# Visibility of variables in functions is as usual
def outer():
    test = 1
    def inner():
        test = 2
        print('  inner:', test)
    inner()
    print('  outer:', test)
print('Visibility test 1')
test = 0  # global scope
outer()
print('  global:', test)


# But we can change visibility with nonlocal and global statements
def outer():
    test = 1
    def inner():
        nonlocal test  # nearest enclosing scope
        test = 2
        print('  inner:', test)
    inner()
    print('  outer:', test)
print('Visibility test 2 (nonlocal)')
test = 0  # global scope
outer()
print('  global:', test)


def outer():
    test = 1
    def inner():
        global test  # global scope
        test = 2
        print('  inner:', test)
    inner()
    print('  outer:', test)
print('Visibility test 3 (global)')
test = 0  # global scope
outer()
print('  global:', test)


# Function parameters has no explicit type defined (it's obvious as Python is dynamically typed)
# However for documenting and reading code, explicit types would be nice. And we can add them via
# type hints.

def greeting(name: str) -> str:
    return 'Hello ' + name


# If we use hint, IDE warns us
print(greeting('world'))  # This OK

# Uncomment the following line to warning in IDE
# (end TypeError exception but it is raised in the function)
# print(greeting(5))


def power(base: float, exponent: float) -> float:
    """
    Returns the value of the first argument raised to the power of the second argument.
    :param base: the base
    :param exponent: the exponent
    :return: the value a :sup:b
    """
    return base ** exponent

# The typing module supports hints and contains many types for them.
