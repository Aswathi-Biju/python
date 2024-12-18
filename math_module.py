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
num= int(input("Enter a number:"))
print("Square root of ",num,":", math.sqrt(num) )
print("Factorial of ",num,":", math.factorial(num) )
print(num,"raised to power 2:", math.pow(num,2) )
