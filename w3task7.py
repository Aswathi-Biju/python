"""
7. Write a Python function that accepts a string and counts the number of upper and lower case letters.
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12
"""
def case_letters():
    uppercase_letters = 0
    lowercase_letters = 0
    for characters in string:
        if characters.isupper():
            uppercase_letters += 1
        elif characters.islower():
            lowercase_letters += 1
    print("No. of Upper case Characters : ", uppercase_letters)
    print("No. of Lower case Characters : ", lowercase_letters)
string="The quick Brow Fox"
print("The string is: ",string)
case_letters()
