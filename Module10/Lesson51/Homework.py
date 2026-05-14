import os

with open('file1.txt', 'w') as file:
    file.write("Python is easy to learn\n")
    file.write("File handling is useful")

with open('file2.txt', 'w') as file:
    file.write("Python programs use files\n")
    file.write("File handling is important")

print("Files created successfully")

print("\nReading file2.txt")

with open('file2.txt', 'r') as file2:
    data = file2.readlines()

    for line in data:
        words = line.split()
        print(words)

with open('file1.txt', 'r') as file1:
    data1 = file1.read()

with open('file2.txt', 'r') as file2:
    data2 = file2.read()

data1 += "\n"
data1 += data2

with open('mergedFile.txt', 'w') as mergedFile:
    mergedFile.write(data1)

print("\nFiles merged successfully")

OutputFile = open('UpdatedFile.txt', 'w')
InputFile = open('mergedFile.txt', 'r')

LinesSeenSoFar = set()

print("\nEliminating duplicate lines")

for line in InputFile:
    if line not in LinesSeenSoFar:
        OutputFile.write(line)
        LinesSeenSoFar.add(line)

OutputFile.close()
InputFile.close()

print("Duplicate lines removed")

if os.path.exists("UpdatedFile.txt"):
    print("\nUpdatedFile exists.")
else:
    print("\nThe file does not exist.")