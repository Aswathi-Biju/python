'''
Author: Aswathi Biju
Date: 19/10/2024
Description: program that create, concatenate,
and print a string and access a sub-string from a given string.
'''
str1=input("Enter your first name: ")
str2=input("Enter your last name: ")
str3= str1+" "+str2
print(str3)
str1_length=len(str1)
sub_str=str3[len(str1)+1:]
print(sub_str)
sub_str2=str3[:len(str1)]
print(sub_str2)
