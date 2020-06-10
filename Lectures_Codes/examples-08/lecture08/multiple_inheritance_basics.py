#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Base class with cat behaviour
class Cat:
    def meow(self):
        print("meow")


# Base class with dog behaviour
class Dog:
    def woof(self):
        print("woof")


# Derived DogCat class combining both parents
class CatDog(Cat, Dog):
    def meow_woof(self):
        self.meow()
        self.woof()


# Resulting CatDog instance has behaviour of Cat and Dog
catdog = CatDog()
catdog.meow()
catdog.woof()
catdog.meow_woof()
