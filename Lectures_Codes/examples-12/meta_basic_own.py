#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class TestAMeta(type):
    def __init__(cls, name, bases, namespace):
        super().__init__(name, bases, namespace)
        print(name)
        print(bases)
        print(namespace)


class TestA(metaclass=TestAMeta):
    s1 = 1

    def __init__(self):
        super().__init__()
        self.i1 = 1

    def m(self):
        print(self.i1)


a = TestA()



class TestBMeta(type):
    # __new__ method in metaclasses constructs the class. Note that since it is in the metaclass, it has different
    # signature than __new__ in classes. It also allows to do much more than the __new__ in classes.
    def __new__(metaclass, name, bases, namespace):
        name = 'TestBMeta'   # name of the class
        bases = (int,) + bases       # base classes (we are adding int)
        namespace['a'] = 1           # adding a class attribute
        return super().__new__(metaclass, name, bases, namespace)

    # Just for demonstration. __init__ in metaclasses can be omited because it's not very useful.
    # Most of the things have to be done in __new__ anyway.
    def __init__(cls, name, bases, namespace):
        super().__init__(name, bases, namespace)
        cls.b = 2


class B1(object):
    pass


print(B1.__name__)
print(issubclass(B1, int))
# Uncomment to get AttributeError
#print(B1.a)


class B2(object, metaclass=TestBMeta):
    pass


print(B2.__name__)
print(issubclass(B2, int))
print(B2.a)
print(B2.b)

