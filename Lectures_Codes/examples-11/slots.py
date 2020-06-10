#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class WithoutSlots:
    pass


class WithSlots:
    __slots__ = 'a', 'b'


wos1 = WithoutSlots()
wos1.a = 1
wos1.b = 2
wos1.c = 3  # all assignments are OK

print(wos1.__dict__)

ws1 = WithSlots()
ws1.a = 1
ws1.b = 2
# Uncomment the following line to get an error
# ws1.c = 3

# plus, there is no __dict__ attribute
# uncomment the following line to get an error
# print(ws1.__dict__)


class RateTimeDistance(dict):
    """A dictionary subclass that automatically adds values (based on other values)"""
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self._solve()

    def __getattr__(self, name):
        return self.get(name, None)

    def __setattr__(self, name, value):
        self[name] = value
        self._solve()

    def __dir__(self):
        return list(self.keys())

    def _solve(self):
        if self.rate is not None and self.time is not None:
            self['distance'] = self.rate*self.time
        elif self.rate is not None and self.distance is not None:
            self['time'] = self.distance / self.rate
        elif self.time is not None and self.distance is not None:
            self['rate'] = self.distance / self.time


rtd1 = RateTimeDistance()
print(rtd1)
rtd1.time = 9.5
print(rtd1)
rtd1.rate = 6.24
print(rtd1)
rtd2 = RateTimeDistance(rate=5.2, time=9.5)
print(rtd2)
