"""
22/11/2024
Author:Aswathi Biju
Description:

"""
list1=[52,45,56,27]
list2=[10,72,89,13]
list3=list1+list2
list3.sort()
print("merged list=",list3)
even_list=[ ]
odd_list=[ ]
for number in list3:
    if number%2==0:
        even_list.append(number)
    else:
        odd_list.append(number)
print("even list=",even_list)
print("odd list=",odd_list)
new_list=even_list+odd_list
print("final list=",new_list)
