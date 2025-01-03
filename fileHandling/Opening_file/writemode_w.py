# "w" - Write Mode
# Purpose: Opens a file for writing.
# Behavior:
# If the file exists, its content is overwritten.
# If the file does not exist, it is created.

f = open("example.txt","w")
f.write("This text is overwritten")
f.close()
