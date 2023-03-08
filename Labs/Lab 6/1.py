import random 
import time
import re
from math import sqrt

def mult(list):
    mult = 1
    for i in range(len(list)):
        mult *= list[i]
    return mult

def counter(str):
    upper_cnt = 0
    lower_cnt = 0
    str = re.sub("[^a-zA-Z]+", "", str)
    for c in str:
        match c.isupper():
            case 0:
                lower_cnt += 1
            case 1:
                upper_cnt += 1
    return lower_cnt, upper_cnt

def is_palindrome(str):
    return str == str[::-1]

lst = [random.randint(1, 10) for i in range(10)]

number = random.randint(1, 100000)
seconds = random.randint(1, 3000)
tuple = (5, True, 0, 1)
# time.sleep(seconds / 1000)
# print(list, mult(lst))
# print(counter("Hello World"))
# print(is_palindrome("palilap"))
# print(f"Square root of {number} after {seconds} miliseconds is {sqrt(number)}")
# print(all(tuple))