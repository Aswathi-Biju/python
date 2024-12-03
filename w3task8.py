"""
8. Write a Python function that takes a list and
returns a new list with distinct elements from the first list.
Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]
"""
def get_distinct_elements(sample_list):
    unique_list=list(set(sample_list))
    return unique_list
sample_list=[1,2,3,3,3,3,4,5]
print("Sample List : ", sample_list)
print("Unique List : ", get_distinct_elements(sample_list))
