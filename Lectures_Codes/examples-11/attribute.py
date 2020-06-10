#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Test:
    def __init__(self):
        self.a = 'a'
        self.b = 'b'

    def __setattr__(self, name, value):
        print(f'set {name} to {repr(value)}')
        if name in ('a', 'b'):
            object.__setattr__(self, name, value)


class Test2:
    def __init__(self):
        self.a = 'a'
        self.b = 'b'

    def __setattr__(self, name, value):
        print(f'set {name} to {repr(value)}')
        if name in ('a', 'b'):
            object.__setattr__(self, name, value)

    def __getattribute__(self, name):
        if name.startswith('_'):  # forbidding access to "private" and special attributes
            raise AttributeError()
        return object.__getattribute__(self, name)


t = Test()

print(f'object variables: {t.__dict__.keys()}')
print(t.a)
print(t.b)
print(t.__dict__)

t2 = Test2()
print(t2.a)
print(t2.b)
# Uncomment the following line to get an error
# print(t2.__dict__)

