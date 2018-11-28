#! /usr/bin/python3
#File: 4.py
#Author: Lars Onselius
#Description: Find the largest palindrom number from 2 three digit numbers
#Arguments: 0

def check_if_palindrome(number):
    number = str(number)
    rebmun = number[::-1]
    for i in range(len(number)):
        if not number[i] == rebmun[i]:
            return False
    return True

largest = 999
for i in range(999, 0, -1):
    for j in range(999, 0, -1):
        product = i * j
        if check_if_palindrome(product):
            if product > largest:
                largest = product

print(largest)
