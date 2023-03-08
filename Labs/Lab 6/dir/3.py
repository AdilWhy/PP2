import os

path = "/Users/adil/Desktop/Python"

if os.path.exists(path):
    print(f"{path} exists.")
    dirname, filename = os.path.split(path)
    print(f"Directory: {dirname}")
    print(f"Filename: {filename}")
else:
    print(f"{path} does not exist.")