# Write a program to create a class Parrot and perform the following tasks - 
# Create a class variable species 
# Create a __init__ method that has instance variables - name and age 
# Create instances of class Parrot, passing arguments as well
# Print Class variable by accessing it 
# Print Instance variables as well

class Parrot:
    species = "bird" # Class Variable
    def __init__(self, name, age): # init method has instance variables (name and age)
        self.name = name # Self means the things containing in the class. - They are used to access variables belonging to the class
        self.age = age

ob1 = Parrot("Coco",6) # ob1 is an instance of class Parrot, here the instance variables' values are being passed
ob2 = Parrot("Lucy",5)

print("Species of object 1 is", ob1.species)
print("Species of object 2 is", ob2.species)

print(ob1.name, "is", ob1.age, "years old.")
print(ob2.name, "is", ob2.age, "years old.")
