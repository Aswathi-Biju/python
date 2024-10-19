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
str1_length=len(str1)  #to know the length of the str1
sub_str1=str3[:len(str1)] #extracting first name
print(sub_str1)
sub_str2=str3[len(str1)+1:] #extracting last name
print(sub_str2)




