import math
import random

def ounces_to_Gramm(grams):
    return grams * 28.3495231

def to_Centrigade(F):
    return 5 / 9 * (F - 32)

def solve(numheads, numlegs):
    for i in range(numheads):
        rabbits = i * 4
        chickens = (numheads - i) * 2
        if rabbits + chickens == numlegs:
            return int(rabbits / 4), int(chickens / 2)

def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
    
def filter_prime(nums):
    prime_list = []
    for i in nums:
        if is_prime(i):
            prime_list.append(i)
    return prime_list

def reverse(s):
    for i in range(len(s) - 1, -1, -1):
        print(s[i], end = "")

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i:i + 2] == [3, 3]:
            return True
    return False

def spy_game(nums):
    for i in range(len(nums) - 1):
        if nums[i:i + 3] == [0, 0, 7]:
            return True
    return False

def volume_of_Sphere(radius):
    return math.pi * 4 / 3 * pow(radius, 3)

def unique_list(list):
    unique_list = []
    for i in list:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list

def palindrome(s):
    for i in range(len(s)):
        if s[i] != s[len(s) - i]:
            return False
    return True

def histogram(nums):
    for i in nums:
        print("*" * i)

# Guess the number 

input_name = input("Hello! What is your name?\n")

guess_number = random.randint(1, 20)

print("Well, " + input_name + ", I am thinking of a number between 1 and 20.\nTake a guess.\n")

i = 1

while True:
    input_number = int(input())
    if input_number == guess_number:
        print("Good job, " + input_name + "! You guessed my number in", i, "guesses!")
        break
    elif input_number > guess_number:
        i += 1
        print("Your guess is too big")
    else:
        i += 1
        print("Your guess is too low")
