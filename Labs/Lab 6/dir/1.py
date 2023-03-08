import os

path = "/Users/adil/Desktop/Python"
print("Directories:")
for dir_name in os.listdir(path):
    if os.path.isdir(os.path.join(path, dir_name)):
        print(dir_name)

# List only files
print("\nFiles:")
for file_name in os.listdir(path):
    if os.path.isfile(os.path.join(path, file_name)):
        print(file_name)

# List directories and files
print("\nDirectories and Files:")
for name in os.listdir(path):
    full_path = os.path.join(path, name)
    if os.path.isdir(full_path):
        print("[DIR] " + name)
    elif os.path.isfile(full_path):
        print("[FILE] " + name)