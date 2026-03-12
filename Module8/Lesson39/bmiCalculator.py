# Write a Python program that takes height and weight as an input from the user, 
# calculates BMI and, based on the value of BMI, displays the resultant category in which the user falls.

height = float(input("Enter height in cm:"))
weight = float(input("Enter weight in kg:"))

bmi = weight/(height/100)**2
print("Your BMI value is", bmi)

if bmi<= 18.4:
    print("You are underweight.")
elif bmi<= 24.9:
    print("You are healthy.")
elif bmi <= 29.9:
    print("You are overweight.")
elif bmi <= 34.9:
    print("You are severly overweight.")
elif bmi <= 39.9:
    print("You are obese.")
else:
    print("You are severly obese.")