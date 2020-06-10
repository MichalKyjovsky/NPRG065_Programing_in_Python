#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def f1(self, x, y):
    return x + y


class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g


def f2(self, x):
    self.a = x


class D:
    def __init__(self):
        self.a = 5

    update = f2

    def show(self):
        print(self.a)


c = C()

print(c.f(1, 2))
print(c.g())
print(c.h())

d = D()
d.show()
d.update(10)
d.show()
