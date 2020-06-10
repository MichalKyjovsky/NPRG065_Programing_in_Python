#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# We want to have a float objects but also with information about units (e.g., km, kg)


class BadFloatUnit(float):
    """"Bad example. Will not work. We cannot override __init__ for builtin immutable classes"""
    def __init__(self, value, unit):
        super().__init__(value)
        self.unit = unit


class FloatUnits(float):
    """Correct example"""
    def __new__(cls, value, unit):
        obj = super().__new__(cls, value)
        obj.unit = unit
        return obj


# Uncomment to obtain an error
#bad = BadFloatUnit(10, 'km')

correct = FloatUnits(10, 'km')
print(f'{correct} {correct.unit}')
