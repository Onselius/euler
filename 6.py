#! /usr/bin/python3
#File: 6.py
#Author: Lars Onselius
#Description: Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
#Arguments: 0

def sum_of_number(number):
    def_sum = 0
    for i in range(number):
        i += 1
        def_sum += i * i
    return def_sum

def square_of_number(number):
    def_sum = 0
    for i in range(number):
        i += 1
        def_sum += i
    return def_sum * def_sum

sum_of_squares = sum_of_number(100)
square_of_sums = square_of_number(100)

print(sum_of_squares)
print(square_of_sums)

print(square_of_sums - sum_of_squares)
