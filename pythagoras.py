"""
Author: Aswathi Biju
Date: 29/11/2024
Description:
A program that accepts the lengths of three sides of a triangle as inputs.
The program should output whether or not the triangle is a right triangle
(Recall from the Pythagorean Theorem that in a right triangle,
the square of one side equals the sum of the squares of the other two sides).
Implement using functions.
Example Runs:
Example 1
    Enter the length of the first side: 3
    Enter the length of the second side: 4
    Enter the length of the third side: 5
    The given triangle is a right triangle.
Example 2:
    Enter the length of the first side: 2
    Enter the length of the second side: 3
    Enter the length of the third side: 4
    The given triangle is not a right triangle.
"""
def is_it_a_triangle_or_not(side1, side2, side3):
    side_list=[side1,side2,side3]
    side_list.sort()
    result1=(side_list[0]**2)+(side_list[1]**2)
    result2=side_list[2]**2
    if result1==result2:
        print("The given triangle is a right triangle.")
    else:
        print("The given triangle is not a right triangle.")
is_it_a_triangle_or_not(5,4,3)
