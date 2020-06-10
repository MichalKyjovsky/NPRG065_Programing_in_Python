#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Let's have a similar Dog class in the previous example
class Dog:
    barking = 'woof'

    tricks = []

    def __init__(self, name):
        self.name = name

    def bark(self, times):
        print(f'{self.name} says: {(self.barking + " ") * times}')

    def rename(self, name):
        self.old_name = self.name  # we can create new object variables in any method (but it is not recommended)
        self.name = name

    def bark_twice(self):
        self.bark(2)                 # We can call other methods via the self reference

    def add_trick(self, trick):
        print(f'{self.name} is learning "{trick}"')
        self.tricks.append(trick)   # We want to teach a particular dog some tricks
                                    # But here, we are using all the dogs

    def learned_tricks(self):
        print(f'{self.name} knows: {self.tricks}')


fido = Dog('Fido')    # Let's have a dog

fido.bark(1)          # Fido barks
Dog.bark(fido, 1)     # The same method called differently

fbark = fido.bark     # The method assigned to a variable
fbark(1)              # Fido barks

fido.rename('Pluto')  # Let's rename Fido
fido.bark(1)
fido.name = 'Fido'    # Let's have back our Fido
fido.bark(1)

fido.bark_twice()

pluto = Dog('Pluto')  # Let's have another dog
pluto.add_trick('roll over')  # We are teaching ALL the dogs
pluto.learned_tricks()
fido.learned_tricks()
