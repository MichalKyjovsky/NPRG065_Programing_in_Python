#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Cashdesk example, we want to sum items in order to obtain total price.


# No overloads
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


bill = [Item("book", 250), Item("pen", 10), 42]

print(f"total: {bill[0].price + bill[1].price + 42}")


# Overloaded __add__ used to redefine + operator
class AdditiveItem(Item):
    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self.price + other
        else:
            return self.price + other.price


bill = [AdditiveItem("book", 250), AdditiveItem("pen", 10), 42]
# No need to use .price
print(f"total: {bill[0] + bill[1] + bill[2]}")

print(type(bill[0]))  # AdditiveItem
print(type(bill[0] + bill[1]))  # Integer

# Integer do not have __add__ overloaded to add items
# Thus calling (0 + bill[0] + bill[1] + bill[2]) fails


# Solution: Overloaded __radd__ (reverse order adding). Is used when __add__ cannot be used
class RevAdditiveItem(AdditiveItem):
    def __radd__(self, other):
        return self.price + other


bill = [RevAdditiveItem("book", 250), RevAdditiveItem("pen", 10), 42]

# No problem with summing item and number
print(f"total: {0 + bill[0] + bill[1] + bill[2]}")
# Or even call sum
print(f"total: {sum(bill)}")
