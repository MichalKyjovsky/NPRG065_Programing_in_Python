#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# We can specify an encoding (of string literals) by putting a specially-formatted comment as the first or
# second line of the source code. The Python default is utf-8 (i.e., the 2nd line in this file is useless
# but nevertheless it should be used even for documentation purposes).

bbb1 = b'\x00\x00'  # the bytes object containing two zero bytes
bbb2 = bytes(2)     # as above

print(bbb1 == bbb2)

bbb1 = b'\xc4\x9b'  # the bytes object with two bytes
print(bbb1)

str1 = bbb1.decode()  # the decode() method returns a string corresponding to the bytes object - by default, utf-8 is used
print(str1)           # it corresponds to the ě charcter

bbb2 = str1.encode()  # converts string to the correspondings bytes
print(bbb1 == bbb2)   # again, the default is utf-8

bbarr = bytearray(b'hello')  # bytes are immutable, bytearrays are mutable
bb = b'hello'

print(bbarr == bb)  # bytes and bytearrays can be used interchangeably

# bytes and bytearray have the same set of methods, which is almost the same as methods of strings
# Even the format method is present.

# How to access individual characters in strings / bytes in bytes will be later

# We can also iterate over bytes
for b in bb:
    print(b)

# If we need to serialize numbers (e.g., for sending them over network to a program in a different language,
# we can easily convert them to bytes

value = 4096
b_value = value.to_bytes(length=4, byteorder='big')
print(b_value)

# Of course, we can convert bytes back to a number
print(int.from_bytes(b_value, byteorder='big'))
