#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Test:
    def __init__(self):
        self.a = 'a'
        self.b = 'b'

    def __getattr__(self, name):
        return 123456

    def __setattr__(self, name, value):
        print(f'set {name} to {repr(value)}')
        if name in ('a', 'b'):  # we set only a and b, other names are ignored
            object.__setattr__(self, name, value)  # to actually set the value, we call __setattr__ from the object class


t = Test()

print(f'object variables: {t.__dict__.keys()}')
print(t.a)  # for existing attributes, __getattr__is not used
print(t.b)
print(t.c)  # for non-existing attributes, __getattr__ is called
print(t.d)

t.a = 1     # __setattr__ is used always
t.b = 2

t.c = 10
print(t.c)  # c still does not exists (__getattr__ is used)
