"""
Author: Aswathi Biju
Date: 29/11/2024
Description:
Recursive function to multiply two positive numbers
"""
def multiply_of_two_numbers(number1,number2):
    if number2==1:
        return number1
    else:
        return number1+ multiply_of_two_numbers(number1,number2-1)
number1=int(input("Enter a first number: "))
number2=int(input("Enter a second number: "))
multiply_of_two_numbers(number1,number2)
print("Multiplication of two numbers: ",multiply_of_two_numbers(number1, number2))
