#! /usr/bin/env Python3 

#Implement a program that prints out a "pine tree" from stars 

import sys

def pine_tree(arg):
    width_of_tree = 1

    for i in range(1, int(arg) - 1):
        width_of_tree += 2

    for i in range(1, int(arg)):
        #if width = 5 then it goes 0,1,2
        for j in range(int(width_of_tree/ 2) + i):
            if( j < int(width_of_tree / 2) - i + 1):
                print(' ',end='')
            else:
                print('*',end='')
        print()
    
    for i in range(int(width_of_tree / 2) + 1):
        if(i < int(width_of_tree / 2)):
            print(' ',end='')
        else:
            print('*',end='')

    print()


pine_tree(sys.argv[1])

   
         
