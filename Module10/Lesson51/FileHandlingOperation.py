#Open a file in write mode using "with"

with open('file1.txt', 'w') as file:
    file.write("This file was opened using 'with'")
file.close()

with open('file2.txt', 'r') as file2:
    data = file2.readlines()
    for line in data:
        word = line.split()
        print (word)
file2.close()