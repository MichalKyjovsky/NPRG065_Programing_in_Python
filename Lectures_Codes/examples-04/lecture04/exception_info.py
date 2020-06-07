#!/usr/bin/env python3


def print_exception_info(ex):
    print(type(ex))   # the type of the exception instance
    print(ex.args)    # arguments stored in .args
    print(ex)


try:
    1 / 0  # try different "exceptional" code here
    # spam + 1
    # open('abcd')
    # ...
except Exception as ex:
    print_exception_info(ex)
