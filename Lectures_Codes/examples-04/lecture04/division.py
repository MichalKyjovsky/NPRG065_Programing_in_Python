#!/usr/bin/env python3

import sys

try:
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    a = x / y
except ZeroDivisionError:
    print('Cannot divide by zero')
except ValueError:
    print('An argument is not a number')
except IndexError:
    print('Not enough arguments')
else:
    print(f'{x} / {y} = {a}')
finally:
    print('I am ready to compute another exercise. Run me again.')
