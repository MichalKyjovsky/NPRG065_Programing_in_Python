#! /usr/bin/env Python3 

#Implement a function that returns maximum of two values given via arguments

def maximum_of_two():
    import sys
    
    if(sys.argv[1] > sys.argv[2]):
        print(sys.argv[1])
    else:
        print(sys.argv[2])

maximum_of_two()
