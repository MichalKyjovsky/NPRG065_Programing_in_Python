#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def prefix(class_):
    class_.log_prefix = 'DEBUG'
    return class_


@prefix
class Foo:
    def __init__(self):
        print(f'{self.log_prefix}: instance created')


foo = Foo()


# We can also add methods via the decorator

def bar(class_):
    def bar(self):
        print(f'{self.__class__.__name__}({self})')
    class_.bar = bar
    return class_


@bar
class Bar:
    def __init__(self):
        self.a = 1


b = Bar()
b.bar()


# But there are limitations
# We cannot override the added method as it has been added AFTER the class definition
@bar
class AnotherBar:
    def bar(self):
        print('overriding bar')


ab = AnotherBar()
ab.bar()  # uses bar() from the decorator
