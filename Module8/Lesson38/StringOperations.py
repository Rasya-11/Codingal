# Store the values of your first name and last name in respective variables. 
# Now add these two strings and store them in the variable full name. 
# Create another variable with the first name multiplied by any number of your choice as its value. 
# Print all the four variables Now add another variable to your program with any string of your choice. 
# Find its length, print its first and last character, and print a sub-string of this original string as well.

firstName = "Rasya"
lastName = "Katikaneni"
fullName = firstName +" "+ lastName

print("Full Name is", fullName)
print("String multiplied 5 times gives the result", firstName*5)

word = "python"
print("upper case word", word.upper())
print("lower case word", word.lower())
print("Length of string is", len(word))
print("First letter of the string is", word[0])
print("Last letter of the string is", word[5])
print("String sliced", word[0:3])
print("String sliced", word[1:4]) #Start index : End index + 1
print("String sliced", word[:3])
print("String sliced", word[::-1]) #Reversed string