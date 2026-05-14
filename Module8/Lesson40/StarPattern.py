# Write a Python program for printing the stars in a pattern using Nested for loop.
# py -3.10 "C:\Users\Prashant\Desktop\Codingal1\Codingal\Module8\Lesson40\StarPattern.py"


n = int(input("Enter number of rows:"))
for i in range(1,n+1): #outer loop
    for j in range(i): #inner loop
        print("*", end=" ")
    print()