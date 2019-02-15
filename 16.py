#! /usr/bin/python3
#File: 14.py
#Author: Lars Onselius
#Description: Sum of the digits of 2**1000
#Arguments: 0


digits = 2**1000

print(digits)
sum = 0
for i in str(digits):
    sum += int(i)

print(sum)


