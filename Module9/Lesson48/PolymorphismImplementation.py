# Write a program to create two classes Dog and Cat, with the same attributes - 
# (name and age) and methods - (info and make_sound). 
# Create different objects for each class and pass the parameters. 
# Showcase the concept of polymorphism in this program.

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print("I am a dog, my name is", self.name, "and I am", self.age, "years old.")
    def make_sound(self):
        print("I can bark.")

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print("I am a cat and my name is", self.name, "and I am", self.age, "years old.")
    def make_sound(self):
        print("I can meow.")

objD = Dog("Coco", 3)
objC = Cat("Kitty", 2)

for animal in (objD, objC):
    animal.info()
    animal.make_sound()