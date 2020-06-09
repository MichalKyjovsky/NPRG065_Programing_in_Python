#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


class Die:
    """A descriptor simulating rolling a die."""
    def __init__(self, sides=6):
        self.sides = sides

    def __get__(self, instance, owner):
        return int(random.random() * self.sides) + 1


class Game:
    die6 = Die()
    die12 = Die(12)


print(Game.die6)
print(Game.die6)
print(Game.die6)
print(Game.die12)
print(Game.die12)
print(Game.die12)


class Celsius:
    """A descriptor ensuring we always have a float value.
       Plus, we cannot delete an attribute."""
    def __init__(self, value=0.0):
        self.value = float(value)

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = float(value)


class Temperature:
    celsius = Celsius(5)


t1 = Temperature()
print(t1.celsius)
# Uncomment the following line to get an error.
# del t1.celsius


class ADescriptor:
    """A descriptor with tracing calls."""
    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        print(f'__get__(instance: {instance}, owner: {owner})')
        return self.value

    def __set__(self, instance, value):
        print(f'__set__(instance: {instance})')
        self.value = value


class TestADescriptor:
    value = ADescriptor(5)


test = TestADescriptor()
print(test.value)   # instance is the object, on which we access the attribute, owner is the class containing the descriptor
test.value = 10

print(TestADescriptor.value)  # here, access the descriptor on the class and thus instance is None

test2 = TestADescriptor()
print(test2.value)   # see, that the value in the descriptor is shared - that is why we have the instance parameter


# builtin property() is a descriptor
# here, how the property is implemented
class Property(object):
    """Emulation of the builtin property"""

    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        if doc is None and fget is not None:
            doc = fget.__doc__
        self.__doc__ = doc

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(obj)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(obj, value)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(obj)

    def getter(self, fget):
        return type(self)(fget, self.fset, self.fdel, self.__doc__)

    def setter(self, fset):
        return type(self)(self.fget, fset, self.fdel, self.__doc__)

    def deleter(self, fdel):
        return type(self)(self.fget, self.fset, fdel, self.__doc__)
