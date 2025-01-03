# "b" - Binary Mode
# Purpose: Opens a file in binary mode.
# Behavior:
# Used for reading or writing binary data like images, videos, or other non-text files.
# Reads and writes bytes instead of strings.

f = open("binaryfile.bin","wb")
f.write(b"This is a binary file")
f.close()

# reading binary file
f = open("binaryfile.bin","rb")
binary_content = f.read()
print(binary_content)
f.close()