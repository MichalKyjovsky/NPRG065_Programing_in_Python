#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class MyInt:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        print('lt called')
        if isinstance(other, MyInt):
            return self.value < other.value
        return False

    def __le__(self, other):
        print('le called')
        if isinstance(other, MyInt):
            return self.value <= other.value
        return False

    def __eq__(self, other):
        print('eq called')
        if isinstance(other, MyInt):
            return self.value == other.value
        return False

    def __gt__(self, other):
        print('gt called')
        if isinstance(other, MyInt):
            return self.value > other.value
        return False

    def __ge__(self, other):
        print('ge called')
        if isinstance(other, MyInt):
            return self.value >= other.value
        return False

    def __str__(self):
        return str(self.value)


i5 = MyInt(5)
i10 = MyInt(10)
j10 = MyInt(10)

print(f'5 < 10: {i5 < i10}')
print(f'5 > 10: {i5 > i10}')
print(f'5 <= 10: {i5 <= i10}')
print(f'5 >= 10: {i5 >= i10}')
print(f'5 == 10: {i5 == i10}')
print(f'5 != 10: {i5 != i10}')  # negated eq will be called
print(f'10 == 10: {i10 == j10}')

# try to comment out gt and ge and see the output
