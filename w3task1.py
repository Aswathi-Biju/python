"""
1. Write a Python function to find the maximum of three numbers.
"""
def maximum(number1,number2,number3):
    number_list=[number1,number2,number3]
    number_list.sort()
    print("Maximum Number is: ",number_list[-1])
number1=int(input("Enter a first number: "))
number2=int(input("Enter a second number: "))
number3=int(input("Enter a third number: "))
maximum(number1,number2,number3)

