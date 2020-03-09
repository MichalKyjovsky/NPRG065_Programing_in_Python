#! /usr/bin/env Python3 

import sys

arguments = []
operators = []
input_arr = sys.argv[1:]

for item in input_arr:
    if item == '+' or item == '-' or item == '*' or item == '/':
        operators.append(item)
    else:
        arguments.append(item)

print(arguments)
print(operators)

while operators:
    x = int(arguments.pop(len(arguments) - 1))
    y = int(arguments.pop(len(arguments) - 1))
    operator = operators.pop(0)

    if operator == '+':
        arguments.append(x + y)
    elif operator == '-':
        arguments.append(y - x)
    elif operator == '*':
        arguments.append(x * y)
    else:
        arguments.append(y / x)

print(arguments.pop(0))

