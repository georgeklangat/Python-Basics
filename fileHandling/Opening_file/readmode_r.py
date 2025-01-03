# "r" - Read Mode (Default)
# Purpose: Opens a file for reading.
# Behavior:
# File must exist; otherwise, an error occurs (FileNotFoundError).
# Does not allow writing.


f = open("readfile.txt", "r")
content = f.read()
print(content)
f.close()