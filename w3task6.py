""" 6. Write a Python function to check whether a number falls within a given range."""
def is_within_range(number, lower_range, upper_range):
    if lower_range <= number <= upper_range:
        print(f"{number} is within the range [{lower_range}, {upper_range}].")
        return True
    else:
        print(f"{number} is not within the range [{lower_range}, {upper_range}].")
        return False
number = int(input("Enter the number to check: "))
lower_range = int(input("Enter the lower bound of the range: "))
upper_range = int(input("Enter the upper bound of the range: "))
is_within_range(number, lower_range, upper_range)



