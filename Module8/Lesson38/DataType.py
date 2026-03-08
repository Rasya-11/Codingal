# Store your Name, Age, Weight, Whether you are a student or not (True for yes, False for no) 
# in respective variables. What do you think is the data type of each variable? Print the data type of 
# every variable. Change the datatype of Age to string and Weight to an integer.

name = "Rasya"
age = 14
weight = 47.5
isStudent = True
print("Name is ", name, "The data type of name is ", type(name))
print("Age is ", age, "Its data type is ", type(age))
print("Data type of student is", type(isStudent))
print("Weight is ", weight, "Its data type is ", type(weight))

print("After type casting")
age = str(age)
print("data type of age is", type(age))
weight = int(weight)
print("data type of weight, after type casting is", type(weight))