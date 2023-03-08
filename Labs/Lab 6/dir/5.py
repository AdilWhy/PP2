import random

list = [random.randint(1, 10) for i in range(5)]
print(list)
with open("out.txt", "w") as file:
    file.write(" ".join(str(i) for i in list))
    print("Writen")