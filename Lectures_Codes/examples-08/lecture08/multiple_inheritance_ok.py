#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Base class with animal behaviour
class Animal:
    def __init__(self, name):
        super().__init__()
        print("Animal init")
        self.name = name


# Base class with cat behaviour
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
        print("Cat init")
        self.cat = "cat"

    def meow(self):
        print(f"meow: {self.cat}")


# Base class with dog behaviour
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        print("Dog init")
        self.dog = "dog"

    def woof(self):
        print(f"woof: {self.dog}")


# Derived DogCat class combines both parents
class CatDog(Cat, Dog):
    def __init__(self, name):
        super().__init__(name)

    def meow_woof(self):
        self.meow()
        self.woof()


# Using super the __init__s are combined and called in correct order.
catdog = CatDog("Max")
catdog.meow()
catdog.woof()
catdog.meow_woof()

