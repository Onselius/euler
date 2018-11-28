#! /usr/bin/python3
#File: 7.py
#Author: Lars Onselius
#Description: Find the 10 001th prime number
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

primes = []

for i in range(10000, 100000000000000000000, 10000):
    primes = sieve_of_eratosthenes(i)
    if len(primes) > 10001:
        break

print(primes[10000])
