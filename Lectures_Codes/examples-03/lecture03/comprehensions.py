#!/usr/bin/env python3


# Let's create a list of squares
squares = []
for x in range(10):
    squares.append(x**2)
# It's fine but it takes 3 lines
# A better option is to use the list comprehensions

squares = [x**2 for x in range(10)]

# A list comprehension consists of brackets containing an expression followed by a for clause,
# then zero or more for or if clauses. The result will be a new list resulting from evaluating
# the expression in the context of the for and if clauses which follow it.

# Comprehensions can be quite complex and can mix several fors.
# E.g., a list of combinations of the elements of two lists if they are not equal
print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])

# Comprehensions can be nested
# Let's have a matrix
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# and a transposed matrix
print([[row[i] for row in matrix] for i in range(4)])




# As for lists, we can have set comprehensions, but now in curly braces
word = 'Hello'
print( {c for c in word} )   # Note that we have only 4 elements in the set while in the string we have 5 chars
print( {c for c in word if c < 'l'} )  # Conditions can be used too



# As for the sets, comprehensions can be used also for dicts. They are also in curly braces but we need to specify
# both the key and value (separated by the : )
# Here we build a dict with chars in the string as keys and the opposite case char as the value.
# Note that for 'l', there is just a single key
print( {c: c.swapcase() for c in word} )
