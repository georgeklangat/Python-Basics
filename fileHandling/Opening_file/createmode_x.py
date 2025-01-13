# "x" - Create Mode
# Purpose: Creates a new file.
# Behavior:
# If the file exists, an error occurs (FileExistsError).

try:
    f = open("newfile.txt","x")
    f.write("you cant imagine this is Newly created file!")
    f.close()
except FileExistsError:
    print("File Exists!")