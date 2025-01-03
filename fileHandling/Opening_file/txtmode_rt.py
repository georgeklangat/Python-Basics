# "t" - Text Mode (Default)
# Purpose: Opens a file in text mode.
# Behavior:
# This is the default mode for reading and writing text.
# Reads and writes strings.

f = open("readfile.txt","rt")
print(f.read())
f.close()