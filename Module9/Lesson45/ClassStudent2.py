# Write a program to create a class with name Student and perform the following tasks - 
# Create a class variable grade and name 
# Create a function to print a sentence 
# Create a function to print class variables grade and name 
# Create an object of class Student Call the two functions to execute them

class Student:
    grade = 9
    name = "Rasya"
    def Introduction(self):
        print("I am Student")
    def Introduction2(self):
        print("My name is", self.name, "and I am in grade", self.grade)

ob = Student()
ob.Introduction()
ob.Introduction2()