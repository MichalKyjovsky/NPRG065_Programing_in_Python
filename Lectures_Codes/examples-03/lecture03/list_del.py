#!/usr/bin/env python3
# -*- coding: utf-8 -*-


a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)  # -> [1, 66.25, 333, 333, 1234.5]
del a[2:4]
print(a)  # -> [1, 66.25, 1234.5]
del a[:]
print(a)  # -> []

del a     # removes the "a" variable completely
print(a)  # -> ends up with the NameError
