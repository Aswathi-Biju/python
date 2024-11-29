"""
Author: Aswathi Biju
Date: 29/11/2024
Description:
Recursive function to add two positive numbers.
"""
def sum_of_two_positive_numbers_add(number1,number2):
    if number2==0:
        return number1
    else:
        return sum_of_two_positive_numbers_add(number1+1,number2-1)
number1=int(input("Enter a first positive number: "))
number2=int(input("Enter a second positive number"))
sum_of_two_positive_numbers_add(number1,number2)
print("Sum of two numbers: ", sum_of_two_positive_numbers_add(number1, number2))
