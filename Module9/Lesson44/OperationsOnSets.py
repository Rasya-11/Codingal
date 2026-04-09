# Write a program to create a set and perform the mentioned operations on that set

My_Set = {}
My_Set2 = {1,2,3,4}
My_Set3 = {1,2,2,3,3,3,4}
print(My_Set3)
My_Set4 = set([1,2,3])
print("set from list:", My_Set4) # set method is used to convert a list to a set.
My_Set5 = My_Set4.pop()
print(My_Set5)
My_Set2.add(5)
print(My_Set2)
My_Set6 = {2,4,6}
DifferenceSet = My_Set6 - My_Set3
# DifferenceSet = My_Set6.difference(My_Set3) # Element that are present in My_Set6 but are not present in My_Set3
print(DifferenceSet)
SymmetricDifference = My_Set6^My_Set3
# SymmetricDifference = My_Set6.symmetric_difference(My_Set3) # Unique elements present in Set6 and Set3
print(SymmetricDifference)