#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Class inheritance is denoted by specifying base class name in round brackets
# following class definition.
# The derived classes inherit methods from base. The inherited methods can be
# overridden in the derived class. When overriding the __init__ method an
# explicit call to ancestor __init__ may be necessary.


class Base:
    def __init__(self, value):
        self.value = value

    def foo(self):
        print("Base foo: " + self.value)

    def call_foo(self):
        self.foo()


class Derived(Base):
    """Derived class inherits foo method and value field from Base. The
    __init__ method is inherited from Base. There is no need to call it
    explicitly"""

    def bar(self):
        print("Derived bar: " + self.value)


class Override(Base):
    """Override class also inherits from Base class, but it replaces foo by its
    own implementation. Also __init__ is replaced, thus it is necessary to
    call Base initializer manually or provide self.value."""

    def __init__(self):
        super().__init__("fixed value")

    def foo(self):
        print("Override foo: " + self.value)


derived = Derived("something")

# Derived class inherits foo method and defines new bar method.
derived.foo()
derived.bar()

# Override class overrides foo and __init__ methods.
# Inherited call_foo call the overridden foo.
override = Override()
override.foo()
override.call_foo()
