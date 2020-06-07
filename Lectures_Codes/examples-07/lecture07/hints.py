#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Function parameters has no explicit type defined (it's obvious as Python is dynamically typed)
# However for documenting and reading code, explicit types would be nice. And we can add them via
# type hints.

def greeting(name: str) -> str:
    return 'Hello ' + name


# If we use hint, IDE warns us
print(greeting('world'))  # This OK

# Uncomment the following line to warning in IDE
# (end TypeError exception but it is raised in the function)
# print(greeting(5))


def power(base: float, exponent: float) -> float:
    """
    Returns the value of the first argument raised to the power of the second argument.
    :param base: the base
    :param exponent: the exponent
    :return: the value a :sup:b
    """
    return base ** exponent

# The typing module supports hints and contains many types for them.
