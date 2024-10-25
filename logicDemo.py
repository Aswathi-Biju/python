'''
Author: Aswathi Biju
Date: 25/10/2024
Description: program to find the largest of three numbers.
The program should take three numbers as input from the user and determine which one is the largest.
Use conditional statements to compare the numbers.
'''
num1= int(input("Enter first number: "))
num2= int(input("Enter second number: "))
num3= int(input("Enter third number: "))
if num1> num2 and num1>num3:
    print("The largest number is: ",num1)
elif num2>num3 :
    print("The largest number is: ", num2)
else:
    print("The largest number is: ", num3)


