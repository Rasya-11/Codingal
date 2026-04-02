# Write a program to create a dictionary and perform the following operations on that dictionary.

dict = {}
dict = {'name':"Rasya", 'age': 14}
print("The name is", dict['name'])
print("The age is", dict['age'])
dict['age'] = 15
print("The updated age is", dict['age'])
dict['grade'] = 9
print("The dictionary is", dict)
dict.pop('age')
print("The updated dictionary is", dict)
print("The grade is", dict.get('grade'))
dict.clear()
print("The updated dictionary is", dict)
