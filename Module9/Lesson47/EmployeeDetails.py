# Write a program to create a parent class Person (attributes - name, idnumber) 
# with a method display to display the attributes. 
# Create a child class Employee (attributes - name, idnumber, salary, post). 
# Access the attributes of parent class in child class. 
# Then, create an object for child class and call the display method to display the name and idnumber.

class Person():
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print(self.name, self.idnumber)

class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
        Person.__init__(self,name,idnumber)
        print(self.salary, self.post)

obj = Employee("Rasya", 12345, 8971, "Junior")
obj.display()