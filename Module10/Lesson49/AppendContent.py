# Write a Python program that can append the content of one file to another file.

# 1) Take two file names from the user:
#    a) First file → the file where content will be added.
#    b) Second file → the file whose content will be copied.

File1 = input("Enter the name of the first file.")
File2 = input("Enter the name of the second file.")

# 2) Open both files in read mode:
#    a) Read and print the content of the first file.
#    b) Read and print the content of the second file.
#    c) Close both files.

F1 = open(File1)
print("Conetent of First file before appending: \n", F1.read())
F1.close()
F2 = open(File2)
print("Conetent of Second file before appending: \n", F2.read())
F2.close()

# 3) Open the first file in append mode and the second file in read mode:
#    a) Read the second file’s content.
#    b) Write (append) it into the first file.

f1 = open(File1, 'a+')
f2 = open(File2, 'r')
f1.write(f2.read())

# 4) Move the cursor back to the beginning using `seek(0)`:
#    a) This helps to read the full updated content from the start.

f1.seek(0)
f2.seek(0)

# 5) Print the content of both files after appending.

print("Conetent of file 1 after appending is: \n", f1.read())
print("Conetent of file 2 after appending is: \n", f2.read())

# 6) Close both files to save and finish.

f1.close()
f2.close()