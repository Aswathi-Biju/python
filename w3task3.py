"""
3. Write a Python function to multiply all the numbers in a list.
Sample List : (8, 2, 3, -1, 7)
Expected Output : -336
"""
def multiply(list):
    multiply=1
    for i in list:
        multiply*=i
    print("The multiplication of list is: ",multiply)
list = []
for i in range(5):
    list.append(int(input(f"Enter number_{i + 1}: ")))
print("The list is: ",list)
multiply(list)
