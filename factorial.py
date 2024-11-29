"""
Author: Aswathi Biju
Date: 29/11/2024
Description:
Program to find the factorial of a number using Recursion.
"""
def factorial(number):
    if number==0:
        return 1
    else:
        return number*factorial(number-1)
print(factorial(5))


