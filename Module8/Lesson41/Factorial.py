# Write a Python program that finds the factorial of a number using recursion and returns the result. 
# (Example - If number = 5, factorial = 5*4*3*2*1 = 120)

# 3!=3*2*1
# 4!=4*3*2*1
# 5!=5*4*3*2*1= 5*4!

num = int(input("Enter a number:"))

def factorial(n):
    if n == 1:
        return n
    else:
        return n*factorial(n-1)
    
if num<0:
    print("Sorry, factorial does not exist for negative numbers.")
elif num==0:
    print("Factorial of 0 is 1.")
else:
    print("Factorial of", num, "is", factorial(num))