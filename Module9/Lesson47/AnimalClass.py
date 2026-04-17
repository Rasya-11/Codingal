# Write a program to implement abstraction on animal class (base class). 
# The abstract method will be move that is for displaying what subclasses can do.

from abc import ABC,abstractmethod

class animal(ABC):
    def move(self):
        pass

class dog(animal):
    def move(self):
        print("Dogs are mammals which bark.")
    
class lion(animal):
    def move(self):
        print("Lions are large cats which are carnivores.")

class fish(animal):
    def move(self):
        print("Fish live underwater and breathe using gills.")

objD = dog()
objD.move()

objL = lion()
objL.move()

objF = fish()
objF.move()