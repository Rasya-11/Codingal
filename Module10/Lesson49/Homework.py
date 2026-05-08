# 1) Take two file names from the user
File1 = input("Enter the name of the first file (e.g., File2.txt): ")
File2 = input("Enter the name of the second file (e.g., File3.txt): ")

# 2) Open both files in read mode to show content
f1 = open(File1, 'r')
print("\nContent of file 1 before: \n", f1.read())
f1.close()

f2 = open(File2, 'r')
print("Content of file 2 before: \n", f2.read())
f2.close()

# 3) Open first file in append+ and second in read mode
f1 = open(File1, 'a+')
f2 = open(File2, 'r')

# 4) Read from f2 and write into f1
f1.write(f2.read())

# 5) Reset f1 cursor to read updated content
f1.seek(0)

# 6) Print results
print("\n--- After Appending ---")
print("Content of file 1 after: \n", f1.read())

# 7) Close both
f1.close()
f2.close()