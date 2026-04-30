# Write a Python program to copy odd lines from one file to another file. 
# For copying it in a new file, 
# create a new empty file and upload it similarly as you do for the given file.

File = open('file3.txt', 'r')
File2 = open('Newfile2', 'w')

Content = File.readlines() #readlines function will give all lines of the file as stored in form of a list.
for i in range(1, len(Content)+1):
    if (i % 2 != 0): #Condition for checking the Odd line
        print(Content[i-1]) #Accessing the line using the index
        File2.write(Content[i-1])
    else:
        pass

File.close()
File2.close()