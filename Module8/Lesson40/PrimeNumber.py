# Write a Python program to take a number as input from the user 
# and check whether it is a prime number or not.

n = int(input("Enter a number:"))

if n<=1:
    print(n, "is not a prime number.")
else:
    for i in range(2,n):
        if n%i==0: #Checking whether the number is divisble by i
            print(n, "is not a prime number.")
            break
        else:
            print(n, "is a prime number.")
            break