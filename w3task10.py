"""
10. Write a Python program to print the even numbers from a given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]
"""
def even_numbers(demo_list):
    final_list = []
    for number in demo_list:
        if number % 2 == 0:
            final_list.append(number)
        else:
            pass
    print(final_list)
even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])
