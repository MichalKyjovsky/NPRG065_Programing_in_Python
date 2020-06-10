#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class PrecomputedPow2:

    class _pow2_iter:
        """Iterator class"""
        def __init__(self, pows):
            self.pows = pows
            self.current = 0

        def __iter__(self):
            return self

        def __next__(self):
            i = self.current
            if i >= len(self.pows):
                raise StopIteration
            self.current += 1
            return self.pows[i]

    def __init__(self, max_value):
        self.max_value = max_value
        self.pows = [a * a for a in range(max_value + 1)]

    def __iter__(self):
        return PrecomputedPow2._pow2_iter(self.pows)

    def __len__(self):
        return len(self.pows)

    def __getitem__(self, item):
        return self.pows[item]

    def __contains__(self, item):
        return item in self.pows


class PrecomputedPow3:

    def __init__(self, max_value):
        self.max_value = max_value
        self.pows = [a * a * a for a in range(max_value + 1)]

    def __iter__(self):
        for x in self.pows:
            yield x

    def __len__(self):
        return len(self.pows)

    def __getitem__(self, item):
        return self.pows[item]

    def __contains__(self, item):
        return item in self.pows


pows = PrecomputedPow2(10)
for a in pows:  # iterator is used
    print(a)

for i in range(len(pows)):
    print(pows[i])   # getitem is used

# Uncomment the following line to get an error - we do not have __setitem__ implemented
# pows[1] = 34


def print_is_in(val, container):
    print(f'Is {val} in our container? {val in container}')


print_is_in(81, pows)
print_is_in(82, pows)



pows = PrecomputedPow3(10)
for a in pows:  # iterator is used
    print(a)

for i in range(len(pows)):
    print(pows[i])   # getitem is used

# Uncomment the following line to get an error - we do not have __setitem__ implemented
# pows[1] = 34


def print_is_in(val, container):
    print(f'Is {val} in our container? {val in container}')


print_is_in(81, pows)
print_is_in(82, pows)
