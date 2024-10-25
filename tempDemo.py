'''
Author: Aswathi Biju
Date: 25/10/2024
Description: program to convert temperature values back and forth between Celsius and Fahrenheit. The user should be able to input a temperature in Celsius or Fahrenheit, 
and the program should convert it to the other unit 
'''
temp=float(input("Enter Temperature: "))
unit= input("Is this in Celsius or Fahrenheit?  ")
if unit == "C":
    f= (9/5*temp)+32
    print(temp,"Celsius is",f,"Fahrenheit")
else:
    c= 5/9*(temp-32)
    print(temp,"Fahrenheit is",c,"Celsius")


