#!/usr/bin/env python3


def foo():
    return 1 / 0


def bar():
    foo()


def baz():
    bar()


baz()
