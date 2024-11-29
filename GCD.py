"""
Author: Aswathi Biju
Date: 29/11/2024
Description:
Recursive function to find the greatest common divisor of two positive numbers.
"""
def greatest_common_divisor(num1,num2):
    if num1%num2==0:
        return num2
    else:
        return greatest_common_divisor(num2,num1%num2)
num1=int(input("Enter a positive number: "))
num2=int(input("Enter a positive number: "))
greatest_common_divisor(num1,num2)
print("The greatest common divisor is", greatest_common_divisor(num1, num2))
