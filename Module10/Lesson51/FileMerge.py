# Write a Python program to merge the contents of two different files into a third file. 
# Create this new third file first and then copy the contents.

#reading data from file1
with open('file1.txt', 'r') as file1:
    data1 = file1.read()

#reading data from file2
with open('file2.txt', 'r') as file2:
    data2 = file2.read()

#merging two files
#add the data of file2 in file1 from next line
data1 += "\n"
data1 += data2

with open('mergedFile.txt', 'w') as mergedFile:
    mergedFile.write(data1)