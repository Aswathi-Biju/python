"""
2. Write a Python function to sum all the numbers in a list.
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20
"""
def sum(list):
    sum=0
    for i in list:
        sum+=i
    print("The sum of list is: ",sum)
list = []
for i in range(5):
    list.append(int(input(f"Enter number_{i + 1}: ")))
print("The list is: ",list)
sum(list)
