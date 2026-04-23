# Write a program to create a class Computer with a private attribute max_price and 
# methods sell(to display) the selling price and setmaxprice(change the private attribute max_price). 
# Now create an object for the class Computer. 
# Try changing the value of max price and use the sell function to display the updated price. 
# Use a setter function to update the value and again display the price.

class Computer:
    def __init__(self):
        self.__max_price = 900 #__max_price is the private attribute.
    def sell(self):
        print("The selling price is", self.__max_price)
    def setMaxPrice(self, Price): #private attribute can only be modified by using a function that is written inside the class.
        self.__max_price = Price

obj = Computer()
obj.sell()

obj.__max_price = 1000
obj.sell()

obj.setMaxPrice(1200) #calling the method to change the private attribute.
obj.sell()