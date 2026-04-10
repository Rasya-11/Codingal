# Create a tuple named weather with these elements - (1, 0, 0, 0, 1, 1, 0). 
# If the element is 1 then the value of rainy increases by 1 otherwise the value of sunny 
# increases by 1. On the basis of the value of rainy and sunny, predict the weather.

Weather = (1,0,0,0,1,1,0)
Rainy = Weather.count(1)
Sunny = Weather.count(0)
if Rainy>Sunny:
    print("It is rainy.")
elif Rainy<Sunny:
    print("It is sunny.") 
else:
    print("The weather is moderate.")