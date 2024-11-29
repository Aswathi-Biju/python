"""
Author: Aswathi Biju
Date: 29/11/2024
Description:
Program to check whether the given number
is a valid mobile number or not, using functions.
Rules:
1. Every number should contain exactly 10 digits.
2. The first digit should be 7 or 8 or 9
"""
def phone_number():
    number=input("Enter your Phone Number: ")
    if len(number)==10:
        print("Valid Phone number ")
    elif number[0]=="7":
        print("Valid Phone number ")
    elif number[0]=="8":
        print("Valid Phone number ")
    elif number[0]=="9":
        print("Valid Phone number ")
    else:
        print("Invalid Phone Number")
phone_number()
