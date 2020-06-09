#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class File:
    """
    Our context manager for files. It is totally useless as the file objects are context
    managers, but it allows us to see the concept.
    """
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print('Enter called')
        self.open_file = open(self.filename, self.mode)
        return self.open_file

    def __exit__(self, *args):
        print('Exit called')
        self.open_file.close()


with File('foo.txt', 'w') as file:
    file.write('foo')
    print('Leaving with')

print('Outside with')

with File('foo.txt', 'w') as file:
    file.write('foo')
    raise AssertionError()  # even with the exception, exit is called and file closed
