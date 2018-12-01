#! /usr/bin/python3
#File: 9.py
#Author: Lars Onselius
#Description: Find the Pythoragian triplet whoose sum is 1000
#Arguments: 0

#Find all numbers that have a sum that equals to 1000
def sum_is_thousand():
    for a in range(998):
        for b in range(a, 997-a):
            for c in range(b, 996):
                if a + b + c == 1000:
                    if a * a + b * b == c * c:
                        if a > 0 and b > 0:
                            print("Boom: Found it!")
                            return [a, b, c]

answer = sum_is_thousand()
print(answer)
print(answer[0] * answer[1] * answer[2])
