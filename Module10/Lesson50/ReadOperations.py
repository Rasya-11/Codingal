# Here is a file attached. You have to perform the following operations of File Handling using Python

File = open('file1.txt', 'r')
print(File.read())
File.close()
File = open('file1.txt', 'r')
print("Read in parts \n", File.read(8))
File.close()
File = open('file1.txt', 'a')
File.write("This is the write method.")
File.close()