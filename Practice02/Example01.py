#! /usr/bin/env Python3

import sys 


n = int(sys.argv[1])


for i in range(1,11):
    print('{0:2d} * {1:2d} = {2:2d}'.format(i,n, i*n))
