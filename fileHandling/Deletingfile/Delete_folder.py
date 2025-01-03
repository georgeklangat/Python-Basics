import os

folder_name = "test_folder"

try:
    os.rmdir(folder_name)
    print(f"{folder_name} has been deleted")
except FileNotFoundError:
    print(f"{folder_name} doesn't exist")
except OSError:
    print(f"{folder_name} doesn't exist")
