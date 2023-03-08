import os

path = "/Users/adil/Desktop/Python/dir/files/A.txt"
if os.path.exists(path):
    if os.access(path, os.W_OK) and os.access(path, os.R_OK):
        os.remove(path)
        print("removed")
    else:
        print("no permissions")
else:
    print("No such path")