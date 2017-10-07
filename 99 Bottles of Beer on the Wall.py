#!/usr/bin/env python3

for i in range(99,0,-1): #start from 99 and goto zero, decreasing in -1 integers

        if i == 1:              #when i is a specific value, print a unique output
                print(i, "bottle of beer on the wall," ,i,  "bottle of beer. Take one down, pass it around," ,(i-1),  "bottles of beer on the wall...")
                print()         #extra print() for spacing between lines
        else:                    #when i and anything but above, print standard response
                print(i, "bottles of beer on the wall," ,i,  "bottles of beer. Take one down, pass it around," ,(i-1), "bottles of beer on the wall...")
                print()
