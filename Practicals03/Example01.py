#! /usr/bin/env Python3 

list_of_tuples = []
list_of_tuples_comprehension = ([(i, j, i * j) for i in range(1, 11) for j in range(1, 11)])

for i in range(1, 11):
    for j in range(1, 11):
        list_of_tuples.append((i, j, i * j))

print(list_of_tuples)
print('************')
print(list_of_tuples_comprehension)
