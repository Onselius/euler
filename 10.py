#! /usr/bin/python3
#File: 10.py
#Author: Lars Onselius
#Description: Find the sum of all the primes below two million.
#Arguments: 0 

def sieve_of_eratosthenes(max_integer):
    sieve = [True for _ in range(max_integer + 1)]
    sieve[0:1] = [False, False]
    for start in range(2, max_integer + 1):
        if sieve[start]:
            for i in range(2 * start, max_integer + 1, start):
                sieve[i] = False
    primes = []
    for i in range(2, max_integer + 1):
        if sieve[i]:
            primes.append(i)
    return primes

primes = sieve_of_eratosthenes(2000000)
print(sum(primes))
