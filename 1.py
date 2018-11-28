#! /usr/bin/python3
#File: 1.py
#Author: Lars Onselius
#Description: Find the sum of all the multiples of 3 or 5 below 1000

def multiple_of_three(number):
    if number % 3 == 0:
        return True
    return False

def multiple_of_five(number):
    if number % 5 == 0:
        return True
    return False

total_sum = 0

for i in range(1000):
    if multiple_of_three(i) or multiple_of_five(i):
        total_sum += i

print(total_sum)
