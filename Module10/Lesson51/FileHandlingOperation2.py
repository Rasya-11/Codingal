
import os
if os.path.exists("demofile.txt"):
    print("File exists.")
    os.remove("demofile.txt")
else:
    print("The file does not exist.")
os.rmdir('demofolder')