# Write a Python program to create a Python list of your favourite fruits (minimum 5). 
# Then perform the given operations on it.

Fruits = ["apple", "banana", "grapes", "orange", "kiwi"]
print("The length of the list is", len(Fruits))
print("The first element is", Fruits[0])
print("The last element is", Fruits[-1])
Fruits.append("papaya")
print("The updated list is", Fruits)
Fruits.remove("orange")
print("The updated list, after removing orange is", Fruits)
Fruits.sort()
print("The sorted list is", Fruits)
Fruits.reverse()
print("The reversed list is", Fruits)
L1 = Fruits[0:3]
print("The sliced list is", L1)
L2 = Fruits[1:4]
print("The sliced list is", L2)