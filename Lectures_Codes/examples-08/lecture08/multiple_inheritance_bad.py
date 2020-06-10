#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Base class with cat behaviour
class Cat:
    def __init__(self):
        print("Cat init")
        self.cat = "cat"
        self.name = "Ashes"

    def meow(self):
        print(f"meow: {self.cat}")


# Base class with dog behaviour
class Dog:
    def __init__(self):
        print("Dog init")
        self.dog = "dog"
        self.name = "Max"

    def woof(self):
        print(f"woof: {self.dog}")


# Derived DogCat class combining both parents
class CatDog(Cat, Dog):
    def meow_woof(self):
        self.meow()
        self.woof()


# Resulting CatDog instance has behaviour of Cat and Dog
catdog = CatDog()
catdog.meow()
catdog.woof()  # !!! Problem here
# __init__ is just a method, the dogcat instance turns to have cat's __init__.
# The Dog __init__ is never called thus the dog field is not present
