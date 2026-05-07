# Write a Python program to duplicate from one file and then copy it to another file. 
# For copying it in a new file, create a new empty file and upload it in a 
# similar way as you do for the given file.

OutputFile = open('UpdatedFile.txt', 'w')
InputFile = open('NewFile.txt', 'r')
LinesSeenSoFar = set() #Conatains the lines that are already seen.
print("Eliminating Duplicate lines.")
for line in InputFile:
    if line not in LinesSeenSoFar:
        OutputFile.write(line)
        LinesSeenSoFar.add(line)

OutputFile.close()
InputFile.close()