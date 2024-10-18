'''
Author: Aswathi Biju
Date: 18/10/2024
Description: program that uses functions from the math module to perform the following operations on a number provided by the user:
1. Find the square root.
2. Calculate the factorial.
3. Raise the number to the power of 2.
Enter a number: 5
Square root of 5: 2.23606797749979
Factorial of 5: 120
5 raised to power 2: 25.0
'''
import math
num1= int(input("Enter a number:"))
print("Square root of ",num1,":", math.sqrt(num1) )
print("Factorial of ",num1,":", math.factorial(num1) )
print(num1,"raised to power 2:", math.pow(num1,2) )
