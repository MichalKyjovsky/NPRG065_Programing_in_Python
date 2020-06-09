#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class A:
    def __init__(self):
        print(f'Creating instance of {self.__class__.__name__} id: {id(self)}')

    def __del__(self):
        print(f'Destroying instance of {self.__class__.__name__} id: {id(self)}')


a1 = A()
del a1     # Explicitly destroying the instance
a2 = A()
a2 = A()   # "Forgetting" a reference to the instance - should be removed by GC

# Terminating interpreter - not guaranteed that __del__() will be called
# But probably it will be called
