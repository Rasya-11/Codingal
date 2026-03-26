# Write a python program to create and print the fibonacci sequence using recursion. 
# A fibonacci sequence is the integer sequence of 0,1,1,2,3,5,8,13... 
# The first two terms of this series are 0 and 1. 
# All other terms are obtained by adding the two proceeding terms.

num = int(input("Enter a number: "))

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if num < 0:
    print("Sorry, Fibonacci sequence does not exist for negative numbers.")
else:
    print("Fibonacci sequence:")
    for i in range(num):
        print(fibonacci(i), end=" ")