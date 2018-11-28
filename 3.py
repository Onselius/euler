#! /usr/bin/python3
#File: 3.py
#Author: Lars Onselius
#Description: Finding the prime factors of 600851475143
#Arguments: 0 

import math

number = 600851475143
#number = 13195

list_of_primes = []

while number % 2 == 0:
    number = int(number / 2)
    list_of_primes.append(2)

for i in range(3, number, 2):
    while number % i == 0:
        number = int(number / i)
        list_of_primes.append(i)
    if number == 1:
        break

print(list_of_primes)
print(sum(list_of_primes))

