"""
Date: 06/12/2024
Author by: Aswathi Biju
Description: Program to define a module to find Fibonacci Numbers
and import the module to another program.
"""
def find_fibonacci(number):
    initial_num=0
    next_num=1
    fibonacci=[0]
    for i in range(number-1):
        fibonacci.append(next_num)
        initial_num,next_num=next_num,initial_num+next_num
    print("Fibonacci Sequence: ",fibonacci)
    return fibonacci
  # next file
from Fibonacci import find_fibonacci
number=int(input("Enter a number: "))
find_fibonacci(number)






