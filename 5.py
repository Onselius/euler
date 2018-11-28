#! /usr/bin/python3
#File: 5.py
#Author: Lars Onselius
#Description: Finding the smallest number that is evenly divsible by all number from 1 to 20
#Arguments: 0

import sys


for i in range(380, 1000000000000, 380):
    for j in range(20):
        j = j+1
        if not i % j == 0:
            break
        elif j == 20:
            print(i)
            sys.exit()
