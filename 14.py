#! /usr/bin/python3
#File: 14.py
#Author: Lars Onselius
#Description: Find the longest Collatz sequence
#Arguments: 0

highest = 0
number = 0
for i in range(1,1000000):
    count = 0
    original = i 
    while i != 1:
        if i % 2 == 0:
            i = i / 2
        else:
            i = (i * 3) + 1
        count = count + 1

    if count > highest:
        highest = count
        number = original

print("Highest count is " + str(highest) + ", from the number " + str(number))

