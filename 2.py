#! /usr/bin/python3
#File: 2.py
#Author: Lars Onselius
#Description: Adding up the sum of a Fibonacci squence of even numbers below 4 000 000
#Arguments: 0

total_sum = 2
term = 0
x = 1
y = 2

while term < 4000000:
    term = x + y
    x = y
    y = term
    if term % 2 == 0:
        total_sum += term
    
print(total_sum)
