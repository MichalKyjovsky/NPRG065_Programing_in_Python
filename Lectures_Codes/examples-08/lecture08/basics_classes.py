#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Dog:
    # Class variables (like static fields in Java)
    kind = 'canine'
    barking = 'woof'

    # Initializing method (a constructor).
    # We need to pass explicitly a reference to the current object.
    # The reference is the first parameter and typically it is named self.
    def __init__(self, name):
        # object variable (like regular fields in Java)
        self.name = name

    def bark(self, times):
        # we can use both object and class variables via the self reference
        print(f'{self.name} says: {(self.barking + " ") * times}')


print(Dog.kind)      # -> canine
d = Dog('Fido')      # instantiating new objects
e = Dog('Buddy')
print(d.kind)        # -> canine
print(e.kind)        # -> canine
print(d.name)        # -> Fido
print(e.name)        # -> Buddy
d.bark(2)            # Fido says: Woof woof
e.bark(2)            # Buddy says: Woof woof

d.name = 'Pluto'     # object variables can be set "from outside"
d.bark(3)            # Pluto says: woof woof woof

d.barking = 'haf'    # hiding class variable via object variable

d.bark(3)            # Pluto is Czech and says: haf haf haf

print(dir(d))        # There are many "builtin" object methods
                     # dir(a) returns a list with all the names defined on the given argument

del e                # we can explicitly remove the object
# Uncomment the following line to get an error
# print(e)
