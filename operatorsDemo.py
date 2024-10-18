'''
Author: Aswathi Biju
Date: 18/10/2024
Description: program that demonstrates the usage of arithmetic, comparison, and logical operators.
Perform a few operations and print the results.
Sum: 15, Division: 2.0
Is a greater than b?: True
Are a and b equal?: False
Logical AND: True
Logical OR: True
'''
num1= int(input("Enter your number:"))
num2= int(input("Enter your number:"))
sum= num1+num2
print("Sum=", num1+num2,", Division=",num1/num2)
print("Is num1 greater than num2?", num1>num2)
print("Are num1 and num2 equal?:", num1==num2)
print("LOGIC AND:",num1>0 and num2>0)
print("LOGIC OR:",num1>0 or num2>num1)
