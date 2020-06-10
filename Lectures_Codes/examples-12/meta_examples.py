#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import collections


class OrderedAttributes(type):
    """
    Classes created from this metaclass will remember the order in which the attributes are created
    """
    @classmethod
    def __prepare__(metacls, name, bases, **kwds):
        """
        The __prepare__() method is executed prior to the creation of the class.
        It creates the initial namespace object into which the definitions will be added.
        """
        return collections.OrderedDict()

    def __new__(cls, name, bases, namespace, **kwds):
        result = super().__new__(cls, name, bases, namespace)
        result._order = tuple(n for n in namespace if not n.startswith('__'))
        return result


class Something(metaclass=OrderedAttributes):
    this = 'text'

    def z(self):
        return False

    b = 'order is preserved'
    a = 'more text'


print(Something._order)


# We want to convert between different length units (inches, feet, meters,...).
# A possible simple solution is to define a "standard unit" and then conversion between
# the standard unit and all other units (another much more complex solution would be to
# a full matrix of conversions between all combinations of units).
# Thus, we create the Unit class, that has a reference to the standard unit and factor, how to
# convert between the unit and the std one.

class Unit:
    """Full name for the unit."""
    factor = 1.0
    standard = None  # Reference to the appropriate StandardUnit
    name = ""        # Abbreviation of the unit's name.
    @classmethod
    def value(class_, value):
        if value is None:
            return None
        return value / class_.factor

    @classmethod
    def convert(class_, value):
        if value is None:
            return None
        return value * class_.factor


# Then we will inherit all units from the unit.
# The issue here is that in the standard unit we need to refer to
# itself, but in the definition it is not possible, i.e.,
#
# class INCH(Unit):
#    standard = INCH
#
# is incorrect definition.
#
# We can overcome it as follows but it is ugly.
#
# class INCH:
#     pass
# INCH.standard = INCH
#
# Nicer solution is via metaclass where we can make the reference
# Note that we have to use the metaclass. It is not possible to use __new__ in the class StandardUnit because
# that one is called only when the class is instantiated and affects only the instance, but we don't instantiate
# INCH anywhere in the code and instead we e require the class INCH to already have the "standard" attribute set to INCH
class UnitMeta(type):
    def __new__(cls, name, bases, dict):
        new_class = super().__new__(cls, name, bases, dict)
        new_class.standard = new_class
        return new_class


class StandardUnit(Unit, metaclass=UnitMeta):
    pass


class INCH(StandardUnit):
    """Inches"""
    name = "in"


class FOOT(Unit):
    """Feet"""
    name = "ft"
    standard = INCH
    factor = 1/12


class CENTIMETER(Unit):
    """Centimeters"""
    name = "cm"
    standard = INCH
    factor = 2.54


class METER( Unit ):
    """Meters"""
    name = "m"
    standard = INCH
    factor = .0254


x = INCH.value(1)
print(FOOT.convert(x))
print(CENTIMETER.convert(x))
print(METER.convert(x))
print(INCH.convert(x))

one_meter = METER.value(1)
print(INCH.convert(one_meter))

print(INCH.standard.__name__)
print(FOOT.standard.__name__)
