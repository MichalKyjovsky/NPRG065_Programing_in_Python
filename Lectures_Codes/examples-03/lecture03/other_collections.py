#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##############
#   namedtuple
##############

# Let's have data about patients eyes
vision = (9.5, 8.8)  # (left eye, right eye)
print(f'Both eyes {vision}')
print(f'Left eye {vision[0]}, right eye {vision[1]}')   # we need to remember that left eye is the index 0 and rhe right 1

from collections import namedtuple
Vision = namedtuple('Vision', ['left', 'right'])  # defining a new namedtuple type

vision2 = Vision(9.5, 8.8)  # using it
print(f'Left eye {vision2.left}, right eye {vision2.right}')  # we can access elements by their names
print(f'Left eye {vision2[0]}, right eye {vision2[1]}')   # but still we can access them by indices



##############
#        deque
##############

from collections import deque

# can be initialized from anything iterable
dq = deque(['b', 'c', 'd'])

# Deque has a similar set of methods like a list, but is optimized for adding/removing object to/from both ends
# (i.e., to be used as a stack or queue)

dq.append('e')
dq.appendleft('a')

print(dq)

print(f'Popping the right element: {dq.pop()}')
print(f'Popping the left element: {dq.popleft()}')
print(dq)

dq.extend(['e', 'f'])
dq.extendleft(['a', '9', '8'])  # Note the order in the deque
print(dq)


##############
#     ChainMap
##############

# Several dicts grouped together. If a key is not available in the first dict, then the second one is used and so on.
# Can be used e.g. for default values

from collections import ChainMap

default_connection = {'host': 'localhost', 'port': 6666}
connection = {'host': 'www.cuni.cz'}

conn = ChainMap(connection, default_connection)
print(f'Host {conn["host"]}, port {conn["port"]}')  # port is taken from the first dict, host from the second one

conn2 = conn.new_child()  # new ChainMap with a additional (empty) dict (as a parameter, we can provide an existing dict)
conn2['port'] = 7777

print(f'Host {conn2["host"]}, port {conn2["port"]}')  # now, host is taken from the new dict

print(conn2.maps)  # a list with all the dicts

##############
#      Counter
##############

# A dict subclass for counting hashable objects.
# It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values.
# Counts are allowed to be any integer value including zero or negative counts.

from collections import Counter

cnt = Counter('mississippi')
for k in cnt:
    print(f' {k}: {cnt[k]} times')

# We can also directly sum, subtract, etc. the Counters
cnt_a = Counter(a=3, b=1)
cnt_b = Counter(a=1, b=2)
print(f'Summing counters {cnt_a + cnt_b}')
print(f'Subtracting counters {cnt_a - cnt_b}')   # subtract (keeping only positive counts)
print(f'Intersection of counters {cnt_a & cnt_b}')   # intersection:  min(c[x], d[x])
print(f'Union of counters {cnt_a | cnt_b}')   # union:  max(c[x], d[x])


##############
#  OrderedDict
##############

# An OrderedDict is a dict that remembers the order that keys were first inserted.
# If a new entry overwrites an existing entry, the original insertion position is left unchanged.
# Deleting an entry and reinserting it will move it to the end.

from collections import OrderedDict

d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}

od = OrderedDict(d)
print(od)
od['plum'] = 5
print(od)
del od['banana']
od['banana'] = 5
print(od)


##############
#  defaultdict
##############

from collections import defaultdict

# As the parameter, a factory for values is specified.
# It is used when a non-existent key is used (the regular dict returns None in such a case)
# Otherwise, it provides the same set of methods as the regular dict.

# Let's have an empty list as the default values
dd = defaultdict(list)
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
for k, v in s:
    dd[k].append(v)
print(dd.items())

# The int is ideal for counting
ddi = defaultdict(int)
s = 'mississippi'
for k in s:
    ddi[k] += 1
print(ddi.items())

##############
#        heapq
##############

# It is a priority queue with the smallest element on the top (internally using the heap queue algorithm)
# Heapsort implementation via heapq


import heapq


def heapsort(arr):
    h = []
    for value in arr:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]


arr = [9, 1, 0, 2, 8, 4, 3, 7, 5, 6]
print(arr)
arr = heapsort(arr)
print(arr)
