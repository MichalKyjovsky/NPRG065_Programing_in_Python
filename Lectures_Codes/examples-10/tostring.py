#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class WithoutStr:
    pass


class WithStr:
    def __str__(self):
        return '__str__() in the WithStr class'


class WithRepr:
    def __repr__(self):
        return '__repr__() in the WithStr class'


class WithStrAndRepr:
    def __str__(self):
        return '__str__() in the WithStr class'

    def __repr__(self):
        return '__repr__() in the WithStr class'


def print_with_class(o):
    print(f'{o.__class__.__name__}: {o}')  # Here, the __str__() will be called


instances = [WithoutStr(), WithStr(), WithRepr(), WithStrAndRepr()]
for i in instances:
    print_with_class(i)

s = str(WithStr())  # builtin str() converts objects to string
print_with_class(s)

print(instances)
