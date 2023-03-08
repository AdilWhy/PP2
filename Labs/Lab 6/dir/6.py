for i in range(65, 91):
    filename = chr(i) + ".txt"
    with open(f"/Users/adil/Desktop/Python/dir/files/{filename}", "w") as file:
        file.write("")
        print("Created")