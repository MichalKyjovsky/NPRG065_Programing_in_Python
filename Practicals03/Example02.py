#! /usr/bin/env Pyrhon3 

list_of_tuples_even = []
list_of_tuples_odd = []

for i in range(1, 11):
    for j in range(1, 11):
        if i % 2 == 0:
            list_of_tuples_even.append((i, j, i * j))
        else:
            list_of_tuples_odd.append((i, j, i * j))

print(list_of_tuples_odd)
print('******************')
print(list_of_tuples_even)
