# Write a Python program to create a calculator. Create individual functions for different operators 
# - addition, subtraction, division, multiplication and return the output value.

num1 = int(input("Enter number one:"))
num2 = int(input("Enter number two:"))

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def division(x,y):
    return x/y

def floorDivision(x,y):
    return x//y

def modulus(x,y):
    return x%y

print("Sum is:", add(num1,num2))
print("Difference is:", subtract(num1,num2))
print("Product is:", multiply(num1,num2))
print("Quotient is:", division(num1,num2))
print("Floor Division value is:", floorDivision(num1,num2))
print("Remainder is:", modulus(num1,num2))