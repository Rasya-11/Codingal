# Write a Python program that takes a name as an input from the user and then creates a function that 
# accepts the same name as a parameter and introduces the user.

Name = input("Enter your Name:")

def introduction(x, age):
    print("Hello, I am", x, "I am", age, "years old.")
    
introduction(Name, 14)