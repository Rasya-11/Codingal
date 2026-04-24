# Write a Python program that can calculate and return the total number of lines present inside a file. 
# First, you would be required to read the contents of the file.

File = open('file1.txt', 'r')
Content = File.read()
Counter = 0
lines = Content.split('\n') #It gives the list of content.
for i in lines:
    if i:
        Counter += 1
File.close()
print("The total number of lines is", Counter)