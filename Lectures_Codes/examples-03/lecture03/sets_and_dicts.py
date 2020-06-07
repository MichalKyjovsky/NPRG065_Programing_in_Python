#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Let's create a set

aset1 = {'one', 'two', 'three', 'four', 'five'}
print(aset1)  # Notice that the printed order is different (sets are unordered)

# We can create a set from anything iterable
alist = ['one', 'two', 'three']
aset2 = set(alist)

# We can add a new element to the set
aset1.add('six')
print(aset1)

# We can add an existing element but it has no effect
aset1.add('six')
print(aset1)

print('one' in aset1)  # Testing existence

print(aset1.isdisjoint(aset2))  # Testing whether intersection is empty

print(aset2 <= aset1)  # Testing whether aset2 is subset of aset1
print(aset2.issubset(aset1))  # The same as above

print(aset2 < aset1)  # Testing whether aset2 is proper subset of aset1

print(aset1 | aset2)       # Union of sets
print(aset1.union(aset2))  # As above

print(aset1 & aset2)       # Intersection of sets
print(aset1.intersection(aset2))  # As above

print(aset1 - aset2)       # Difference of sets
print(aset1.difference(aset2))  # As above

print(aset1 ^ aset2)       # Symmetric difference (elements in either the set or other but not both)
print(aset1.symmetric_difference(aset2))  # As above

aset1.remove('six')   # Removing an element
print(aset1)

aset1.discard('six')  # As above but generates no error in the case the element is not present
print(aset1)

print(aset1.pop())   # Removes and returns an arbitrary element

# frozensets works as regular sets but cannot be modified after creation

afset = frozenset(alist)
# Uncomment the following line to get an exception (no add() method)
# afset.add('six')



# Let's create several dicts
adict1 = {'one': 1, 'two': 2, 'three': 3}
# All the below creations create the same dictionary as above
adict2 = dict(one=1, two=2, three=3)
adict3 = dict([('two', 2), ('one', 1), ('three', 3)])
adict4 = dict(zip(['one', 'two', 'three'], [1, 2, 3]))  # the builtin function zip() zips several lists into a list of tuples

print(adict1['one'])    # dicts can be indexed by the keys

adict1['four'] = 4      # We can add new elements.
print(adict1)

adict1['five'] = 6      # Oh, we have made a mistake here. Let's correct it.
adict1['five'] = 5
print(adict1)           # See that each key is just once in the dict (i.e., the keys behave as a set)

print('one' in adict1)    # Testing existence of a key in the dict

print(adict1.keys())      # Keys in the dict
print(adict1.values())    # Values in the dict
print(adict1.items())     # Tuples (key, value)

# All the three methods return objects that look like list, but they are view objects.
# They provide a dynamic view on the dictionary’s entries, which means that when
# the dictionary changes, the view reflects these changes.
