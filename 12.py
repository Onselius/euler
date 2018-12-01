#! /usr/bin/python3
#File: 12.py
#Author: Lars Onselius
#Description: What is the value of the first triangle number to have over five hundred divisors?
#Arguments: 0

import itertools as it
import math

def n_o_d(number):
    nod = 0
    sqrt = int(math.sqrt(number))

    for i in range(1, sqrt + 1):
        if number % i == 0:
            nod += 2
    if sqrt * sqrt == number:
        nod -= 1
    print(str(number) + " " + str(nod))
    return nod

number = 1
it = 1
while (n_o_d(number) < 500):
    number += it
    it += 1

iterator = map(sum, map(range, it.count(2)))
for i in iterator:
    break
    count = [j for j in range(i+1) if i % (j+1) == 0]
    print(str(i) + " " + str(len(count)))
    if len(count) > 500:
        print(i)
        break


for i in it.count(1):
    break
    i = sum(range(i+1))
    count = 0
    for j in range(int(math.sqrt(i) + 1)):
        if i % (j+1) == 0:
            count += 1
    print(str(i) + " " + str(count))
    if count > 500:
        print(i)
        break
    
