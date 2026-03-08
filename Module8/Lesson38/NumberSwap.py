# First of all, take two numbers from the user, store them in variables x and y, respectively. 
# Write a Python program to swap the values present inside x and y and display the results.

x = input("Enter the value of X.")
y = input("Enter the value of Y.")
temp = x
x = y
y = temp
print("Value of X after swaping is", x)
print("Value of Y after swaping is", y)