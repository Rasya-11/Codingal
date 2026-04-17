# Write a program to create a parent class Person (attributes - fname, lname) 
# with a method printname to display the full name. 
# Create a child class Student (attributes - fname, lname, year). 
# Access the attributes of parent class in child class using super() function. 
# Then, create an object for the child class and call the display method to display the full name. 
# Also, print the graduation year.

class Person():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def fullName(self):
        print("The full name is", self.fname, self.lname)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.year = year

obj = Student("Rasya", "Rao", 9)
obj.fullName()
print(obj.year)