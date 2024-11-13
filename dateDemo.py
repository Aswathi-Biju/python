'''
Author: Aswathi Biju
Date: 19/10/2024
Description: program that create, concatenate,
and print a string and access a sub-string from a given string.
'''
from datetime import datetime
current=datetime.now()
format_1=current.strftime("%Y-%m-%d %H:%M:%S")
format_2=current.strftime("%m/%d%Y")
format_3=current.strftime("%A, %B %d, %Y")
format_4=current.strftime("%A, %B %d, %Y %H:%M:%S")
format_5=current.strftime("%A, %B %d, %Y %H:%M:%S %p")
format_6=current.strftime("%a-%b-%d %H:%M:%S %Z %Y")
format_7=current.strftime("%d")
format_8=current.strftime("%H:%M:%S")
format_9=current.strftime("%B")
format_10=current.strftime("%Y")
print(format_1)
print(format_2)
print(format_3)
print(format_4)
print(format_5)
print(format_6)
print(format_7)
print(format_8)
print(format_9)
print(format_10)
