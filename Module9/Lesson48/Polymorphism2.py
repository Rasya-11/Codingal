
class square:
    def __init__(self, side):
        self.side = side
    def area(self):
        print("My area is", self.side**2)

class circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        print("My area is", 3.14*self.radius*self.radius)

objS = square(4)
objC = circle(3)

for shape in (objS, objC):
    shape.area()