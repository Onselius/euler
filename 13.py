#! /usr/bin/python3
#File: 13.py
#Author: Lars Onselius
#Description: Find the 10 first digit of a sum of numbers
#Arguments: 0

data = [int(line) for line in open("input13").readlines()]
summa = sum(data)
print(summa)
print(str(summa)[:10])
