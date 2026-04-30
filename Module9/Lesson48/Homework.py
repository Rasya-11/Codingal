# Parent class
class Shape:
    def __init__(self, name):
        self.name = name   # encapsulated attribute

    def area(self):
        pass   # to be overridden by child classes


# Child class: Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.__length = length     # private variable
        self.__width = width

    def area(self):
        return self.__length * self.__width


# Child class: Square
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.name = "Square"


# Child class: Circle
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.__radius = radius

    def area(self):
        return 3.14 * self.__radius ** 2


# Creating objects
rect = Rectangle(5, 3)
square = Square(4)
circle = Circle(3)

# Polymorphism
for shape in (rect, square, circle):
    print(shape.name, "area is", shape.area())