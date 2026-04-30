# Write a Python program to remove lines of a file starting with prefix - 
# Coding and store the contents in a new file.

File = open('file3.txt', 'r')
File2 = open('Newfile.txt', 'w')

for line in File.readlines():
    if not(line.startswith('Coding')):
        print(line)
        File2.write(line)

File.close()
File2.close()