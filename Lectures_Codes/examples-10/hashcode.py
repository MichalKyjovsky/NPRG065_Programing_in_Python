#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class MutableItemWithoutHash:
    """Mutable object should not have the __hash__ defined."""
    def __init__(self, val):
        self.val = val

    def update(self, val):
        self.val = val

    def __eq__(self, other):
        return other.val == self.val


a = MutableItemWithoutHash(5)
b = MutableItemWithoutHash(5)

# Uncomment the following line - MutableItemWithoutHash objects are not hashable
# x = {a: 1, b: 2}


class ImmutableItemWithHash:
    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        return other.val == self.val

    def __hash__(self):
        return hash(self.val)

    def __str__(self):
        return f'Immutable({self.val})'


c = ImmutableItemWithHash(5)
d = ImmutableItemWithHash(5)

# now it works
x = {c: 1, d: 2}
# but c and d are equal and thus x has only a single key
for k in x:
    print(f'{k}:{x[k]}')


class Person:
    """A class with recommended implementation of __hash__"""
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __eq__(self, other):
        return self.age == other.age and self.name == other.name

    def __hash__(self):
        return hash((self.age, self.name))  # hash from a tuple of fields


person = Person(10, 'John Doe')
print(hash(person))
