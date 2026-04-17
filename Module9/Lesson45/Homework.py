class Robot:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return "Hello, my name is", self.name

robot1 = Robot("Tom")
robot2 = Robot("Jerry")

print(robot1.introduce())
print(robot2.introduce())