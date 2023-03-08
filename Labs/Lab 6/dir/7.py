with open("textfile.txt", "r") as file:
    with open("out.txt", "w") as f:
            f.write(file.read())
            print("Succesfull")