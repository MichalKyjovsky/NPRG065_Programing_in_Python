#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal:
    def __init__(self):
        super().__init__()
        print('Animal.__init__')

    def foo(self):
        print('Animal.foo')


class HasLegs(Animal):
    def __init__(self):
        super().__init__()
        print('HasLegs.__init__')

    def foo(self):
        print('HasLegs.foo')
        super().foo()


class FourLegged(HasLegs):
    def __init__(self):
        super().__init__()
        print('FourLegged.__init__')

    def foo(self):
        print('FourLegged.foo')
        super().foo()


class Furry(Animal):
    def __init__(self):
        super().__init__()
        print('Furry.__init__')

    def foo(self):
        print('Furry.foo')
        super().foo()


class Cat(FourLegged, Furry, Animal):
    def __init__(self):
        super().__init__()
        print('Cat.__init__')

    def foo(self):
        print('Cat.foo')
        super().foo()

print(Cat.mro())

cat = Cat()

cat.foo()
