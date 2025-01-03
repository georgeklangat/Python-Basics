import os

file_name = "example1.txt"

if os.path.exists(file_name):
    os.remove(file_name)
    print(f"{file_name} has been deleted")
else:
    print(f"{file_name} does not exist")

