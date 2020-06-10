#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class C:
    @staticmethod
    def show(msg):
        print(msg)


# We call the static method on the class
C.show('Hello world')

# But we can call it on an instance also (still, it is a static method without self)
c = C()
c.show('Hello world again')

