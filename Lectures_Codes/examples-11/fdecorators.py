#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools


def simple_decorator(function):
    print('With our decorator')
    return function


@simple_decorator
def hello():
    print('hello world')


hello()


def debug(function):
    @functools.wraps(function)
    def logged_function(*args, **kw):
        print(f'called: {function.__name__}( {args}, {kw} )')
        result = function(*args, **kw)
        print(f'finished: {function.__name__}, with result = {result}')
        return result
    return logged_function


@debug
def fib(a):
    """
    Computes Fibonaci series.
    :param a:
    :return:
    """
    prev = 1
    prevprev = 1
    while a > 0:
        tmp = prev + prevprev
        prevprev = prev
        prev = tmp
        a -= 1
    return prev

print(fib.__name__)
print(fib.__doc__)

result = fib(10)

# Decorators can have parameters
#
# @decorator(arg)
# def func( ):
#     pass
#
# This is equivalent to
#
# def func( ):
#     pass
# func = decorator(arg)(func)


def debug_named(prefix):
    def internal_debug(function):
        @functools.wraps(function)
        def logged_function(*args, **kw):
            print(f'{prefix}: called: {function.__name__}( {args}, {kw} )')
            result = function(*args, **kw)
            print(f'{prefix}: finished: {function.__name__}, with result = {result}')
            return result
        return logged_function
    return internal_debug


@debug_named('DEBUG')
def fib(a):
    prev = 1
    prevprev = 1
    while a > 0:
        tmp = prev + prevprev
        prevprev = prev
        prev = tmp
        a -= 1
    return prev


result = fib(10)


# Decorators for methods are the same as for standalone function.
# Only, we have to explicitly take care about the self parameter
def audit(method):
    @functools.wraps(method)
    def wrapper(self, *args, **kw):
        before = repr(self)
        try:
            result = method(self, *args, **kw)
            after = repr(self)
        except Exception as e:
            print(f'{method.__name__} exception; before {before}')
            raise e
        print(f'{method.__name__}; before {before}\n after {after}')
        return result
    return wrapper


class Test:
    def __init__(self):
        self.a = 1

    @audit
    def update(self):
        if self.a >= 2:
            raise ValueError('Too big')
        self.a = self.a + 1

    def __repr__(self):
        return f'<{self.__class__.__name__} a = {repr(self.a)}>'


test = Test()
test.update()
# Uncomment the following line to test our decorator with an exception
# test.update()
