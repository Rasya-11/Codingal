class Shape:
    def area(self):
        print("Area calculation")

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        print("Area of square is", self.side ** 2)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        print("Area of rectangle is", self.length * self.width)

objS = Square(4)
objR = Rectangle(5, 3)

for shape in (objS, objR):
    shape.area()