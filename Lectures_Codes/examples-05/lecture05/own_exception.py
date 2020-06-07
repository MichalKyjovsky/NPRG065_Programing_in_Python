#!/usr/bin/env python3


class MyException(Exception):
    pass


def foo():
    raise MyException


try:
    foo()
except MyException:
    print('MyException occurred')
    raise
