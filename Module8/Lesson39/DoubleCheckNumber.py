# Write a Python program to check whether a number entered by the user is greater than 50 or not. 
# Also, if it is greater than 50, then check whether it is odd or even.

num = int(input("Enter a number:"))

if num>=50:
    print("Number is greater than 50.")
    if num%2==0:
        print("Number is even.")
    else:
        print("Number is odd.")
else:
    print("Number is less than 50.")