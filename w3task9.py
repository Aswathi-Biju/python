"""
9. Write a Python function that takes
 a number as a parameter and checks whether the number is prime or not.
Note : A prime number (or a prime) is a natural number greater than 1
and that has no positive divisors other than 1 and itself.
"""
def prime_or_not(number):
    for i in range(2, number):
        if number % i == 0:
            print(f"{number} is a prime number")
            break
        else:
            print(f"{number} is not a prime number")
            break
number=int(input("Enter a number: "))
prime_or_not(number)
