#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import abc


class PluginBase(abc.ABC):

    @abc.abstractmethod
    def process(self, input):
        return


class ToUpperPlugin(PluginBase):
    """Good implementation of the plugin."""
    def process(self, input):
        return input.upper()


class BadPlugin(PluginBase):
    """Bad implementation - it does not override the abstract method.
       Even the IDE warns us."""
    def other_method(self):
        pass


class ToLowerPlugin:
    """We can omit subclassing, but then we need to register the class via the PluginBase.register method"""
    def process(self, input):
        return input.upper()


# Registering a class that do not directly subclass our base class
PluginBase.register(ToLowerPlugin)


toUpper = ToUpperPlugin()
print(toUpper.process('Hello'))

# We cannot instantiate BadPlugin as it does not override the process method
# Uncomment the following line to get an error
# bad = BadPlugin()

print(f'{ToUpperPlugin.__name__} is subclass of {PluginBase.__name__}: {issubclass(ToUpperPlugin, PluginBase)}')
print(f'toUpper is instance of {PluginBase.__name__}: {isinstance(toUpper, PluginBase)}')

toLower = ToLowerPlugin()
print(toLower.process('Hello'))

# Even though ToLowerPlugin does not subclass PluginBase directly, isinstance and issubclass claim it is a subclass
print(f'{ToLowerPlugin.__name__} is subclass of {PluginBase.__name__}: {issubclass(ToLowerPlugin, PluginBase)}')
print(f'toLower is instance of {PluginBase.__name__}: {isinstance(toLower, PluginBase)}')


# Abstract base classes can have implementation

class AnotherPluginBase(abc.ABC):
    @abc.abstractmethod
    def process(self, input):
        """Abstract methods can have an implementation. It is available via super() call"""
        print('Process called')
        return


class AnotherToUpper(AnotherPluginBase):
    def process(self, input):
        """ Calling inherited implementation"""
        super(AnotherToUpper, self).process(input)
        return input.upper()


anotherToUpper = AnotherToUpper()
print(anotherToUpper.process('Hello'))


# We can have even abstract properties

class YetAnotherPluginBase(abc.ABC):
    @property
    @abc.abstractmethod
    def name(self):
        return

    @property
    @abc.abstractmethod
    def editable(self):
        return

    @editable.setter
    @abc.abstractmethod
    def editable(self, value):
        pass


class YetAnotherToUpper(YetAnotherPluginBase):
    def __init__(self):
        self._name = 'ToUpper Plugin'
        self._editable = False

    @property
    def name(self):
        return self._name

    @property
    def editable(self):
        return self._editable

    @editable.setter
    def editable(self, value):
        self._editable = value


yetAnotherToUpper = YetAnotherToUpper()
yetAnotherToUpper.editable = True
print(yetAnotherToUpper.name)
print(yetAnotherToUpper.editable)
