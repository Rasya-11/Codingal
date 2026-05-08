f1 = open('file1.txt', 'r')
print("--- Full Content of File 1 ---")
print(f1.read())
f1.close()

f1 = open('file1.txt', 'r')
print("\n--- Reading first 8 characters ---")
print(f1.read(8))
f1.close()

f2 = open('file2.txt', 'w')
f2.write("This is the write method.")
f2.close()

f2 = open('file2.txt', 'a')
f2.write("\n This is the append method.")
f2.close()

f3 = open('file3.txt', 'r')
f4 = open('Newfile.txt', 'w')

lines = f3.readlines()
print("\n Filtering File 3 (Removing 'Coding' lines)")
for line in lines:
    if not (line.startswith('Coding')):
        print("Copying:", line.strip())
        f4.write(line)

f3.close()
f4.close()

f3 = open('file3.txt', 'r')
f5 = open('Newfile2.txt', 'w')

lines = f3.readlines()
print("\n Extracting Odd Lines")
for i in range(1, len(lines) + 1):
    if i % 2 != 0:
        f5.write(lines[i-1])

f3.close()
f5.close()
