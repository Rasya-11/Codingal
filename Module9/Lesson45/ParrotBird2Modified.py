class Parrot:
    species = "bird" 

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sing(self, song):
        return self.name + " sings " + song

    def dance(self):
        return self.name + " is dancing"


ob1 = Parrot("Coco", 6)
ob2 = Parrot("Lucy", 5)
ob3 = Parrot("Milo", 4)

print(ob1.name, "is", ob1.age, "years old.")
print(ob2.name, "is", ob2.age, "years old.")
print(ob3.name, "is", ob3.age, "years old.")

print(ob1.sing("Happy"))
print(ob2.sing("Birthday Song"))
print(ob3.dance())