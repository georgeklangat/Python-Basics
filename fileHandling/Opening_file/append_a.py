# "a" - Append Mode
# Purpose: Opens a file for appending.
# Behavior:
# If the file exists, new data is added to the end of the file without erasing its content.
# If the file does not exist, it is created.

f = open("readfile.txt","a")
f.write("Welcome to the world of coding, make sure you enjoy it right!")
f.close()