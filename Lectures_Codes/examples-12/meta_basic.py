#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Spam:
    eggs = 'my eggs'


MSpam = type('MSpam', (object,), dict(eggs='my eggs'))

print(Spam)
print(MSpam)

print(type(Spam))
print(type(MSpam))
