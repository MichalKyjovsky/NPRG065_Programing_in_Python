#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# FEATURES: simple examples of different sys functions
import sys

print(f"Commandline arguments: \"{sys.argv}\"")

print(f"Native byte order: {sys.byteorder}")

print(f"Python executable path: {sys.executable}")

print("Python commandline flags:")
print(sys.flags)

print("Floating number info:")
print(sys.float_info)

print(f"Default string encoding: {sys.getdefaultencoding()}")

print(f"Encoding used for file-names: {sys.getfilesystemencoding()}")

print(f"Maximum stack depth: {sys.getrecursionlimit()}")

print(f"Size of simple string object: {sys.getsizeof('foobar')}")

print("Python implementation information:")
print(sys.implementation)

print(f"Maximum variable size: {sys.maxsize}")

print("Search path for modules:")
print(sys.path)

print("Imported modules:")
print(sys.modules)

print(f"System platform: {sys.platform}")

print(f"Python interpreter version: {sys.version}")


print("Exiting the interpreter by sys.exit with status 42")
sys.exit(42)
print("This will not be reached")
