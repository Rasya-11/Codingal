File1 = input("Enter the name of the first file (e.g., File2.txt): ")
File2 = input("Enter the name of the second file (e.g., File3.txt): ")

f1 = open(File1, 'r')
print("\nContent of file 1 before: \n", f1.read())
f1.close()

f2 = open(File2, 'r')
print("Content of file 2 before: \n", f2.read())
f2.close()

f1 = open(File1, 'a+')
f2 = open(File2, 'r')

f1.write(f2.read())
f1.seek(0)

print("\n--- After Appending ---")
print("Content of file 1 after: \n", f1.read())

f1.close()
f2.close()