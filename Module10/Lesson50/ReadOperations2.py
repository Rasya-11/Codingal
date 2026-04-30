
File = open('file2.txt', 'r')
print(File.read())
File.close()

File = open('file2.txt', 'w')
File.write("This is the write method.")
File.close()

File = open('file2.txt', 'a')
File.write("This is the append method.")
File.close()