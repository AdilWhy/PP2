import random 

def mult(list):
    mult = 1
    for i in range(len(list)):
        mult *= list[i]
list = [random.radint(1, 10) for i in range(10)]

print(list, mult(list))