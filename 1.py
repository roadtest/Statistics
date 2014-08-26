#!/usr/bin/python3
filedata = None
file = open('file.txt', 'r') 
filedata = file.read()
file.close()

# Replace the target string
newdata=filedata.replace("abc", "abcd")

# Write the file out again
file = open('file.txt', 'w')
file.write(newdata)
file.close()

#
