#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import abc


# Self registering plugins

class Plugins(abc.ABCMeta):
    plugins = dict()

    def __new__(metaclass, name, bases, namespace):
        cls = super().__new__(metaclass, name, bases, namespace)
        if isinstance(cls.name, str):
            metaclass.plugins[cls.name] = cls
        return cls

    @classmethod
    def get(cls, name):
        return cls.plugins[name]


class PluginBase(metaclass=Plugins):
    @property
    @abc.abstractmethod
    def name(self):
        raise NotImplemented()


class SpamPlugin(PluginBase):
    name = 'spam'


class Ancestor(PluginBase):
    pass


class EggsPlugin(Ancestor):
    name = 'eggs'


# This fails with error "TypeError: Can't instantiate abstract class Ancestor with abstract methods name"
# Ancestor()

print(Plugins.get('spam'))
print(Plugins.plugins)

