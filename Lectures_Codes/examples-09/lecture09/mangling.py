#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def __update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    def test_parent(self):
        print(self.__update)


class MappingSubclass(Mapping):

    def __update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)

    def test_child(self):
        print(self.__update)


# print(Mapping.__update)  # Results in error
print(Mapping._Mapping__update)
print(MappingSubclass._Mapping__update)
print(MappingSubclass._MappingSubclass__update)

parent = Mapping([])
child = MappingSubclass([])
parent.test_parent()
child.test_parent()
child.test_child()
