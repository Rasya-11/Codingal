
File = open('file1.txt', 'w')
File.write("This is the write method.")
File.close()

File = open("file1.txt", 'a')
File.write("This is the append method.")
File.close()