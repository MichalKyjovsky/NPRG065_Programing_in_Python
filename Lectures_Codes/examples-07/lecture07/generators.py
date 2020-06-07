#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Let's have a function returning a list of squares till the given value
def get_squares(n):
    return [x ** 2 for x in range(n)]


# Now, we can print the squares
for i in get_squares(10):
    print(i)

# Everything works, but it is suboptimal. The get_squares function computes and returns a complete list of squares,
# which we do not need. For really big parameters we can even run out of the memory.
# It is completely enough to have the squares one by one.


# So, let's "repair" the function.
def get_squares2(n):
    for x in range(n):
        yield x ** 2


for i in get_squares2(10):
    print(i)

# The visible results are the same. But second solution is better as it computes squares as they are needed (the first
# one "precomputes" the whole list.

# The second function returns a generator object
# Let's test it.

gen_obj = get_squares2(4)
print(gen_obj)

# The generator supports iteration. I.e., we ca use it in the for loop (as above) and also
# we can directly use it with the built-in function next().

print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
# Further calls raises StopIteration
# print(next(gen_obj))


# There can be also return in a generator function. But it produces StopIteration exception
# (it is compatible with the for loop and other constructions depending on iterations - will
#  be covered later)
# Let's try it.

def counter_with_limit(limit=10):
    n = 0
    while n < limit:
        yield n
        n += 1
    return


print('counter_with_limit')
for i in counter_with_limit():
    print(i)



# Take a look again to the 'get_squares2' method. It can be rewritten in a shorter way via the 'yield from'
# The result is the same but it is shorter
def get_squares3(n):
    yield from (x**2 for x in range(n))


print('get_squares3')
for i in get_squares3(10):
    print(i)

# This leads us to the generator expressions, which looks like list comprehensions but they are in the round parentheses
# and returns a generator object instead of the list

print('generator expression')
for i in (x ** 2 for x in range(10)):
    print(i)

print((x ** 2 for x in range(10)))  # Just to prove that it returns a generator
print([x ** 2 for x in range(10)])  # and this returns a list


# We can also chain several generators together
def chain_generators(*gens):
    for gen in gens:
        yield from gen


print('Chained generators')
for i in chain_generators((x ** 2 for x in range(10)), (x ** 2 for x in range(10, 20))):
    print(i)


# But there is no need to create own chaining function. - Python already
# contains the chain function in the module itertools
# Note: chain works with anything that is iterable
import itertools
print('Chaining via itertools.chain')
for i in itertools.chain((x ** 2 for x in range(10)), (x ** 2 for x in range(10, 20))):
    print(i)



# We can interact with the generator object and send to it objects via the built-in function send()
# Let's consider the following function
def counter_with_interaction():
    n = 0
    while True:
        result = yield n    # This line is important. yield returns object sent to the generator via the send() function
        print(type(result), result)
        if result == 'Quit':
            break
        n += 1


# Examine the following code and its output
print('counter_with_interaction')
c = counter_with_interaction()
print(f'i1: {next(c)}')          # prints 0
print(f'i2: {c.send("Wow!")}')   # prints 1 but preceded by 'str Wow' as we sent 'Wow' to the generator
print(f'i3: {next(c)}')          # prints 2 preceded by 'None' as we did not send anything
try:
    print(f'i4: {c.send("Quit")}')   # raises StopIteration as the generator "called" return (before 'str Quit' is printed)
except StopIteration as si:          # we just catch the exception
    print(f'{type(si)} raised')


