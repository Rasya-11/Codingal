# Write a Python program for printing the sum of the first ten natural numbers using the while loop.

totalSum = 0
Num = 1

while Num<=10:
    totalSum += Num #totalSum = totalSum + Num
    Num += 1 #Num = Num + 1

print("The sum of the first ten natural numbers is", totalSum)