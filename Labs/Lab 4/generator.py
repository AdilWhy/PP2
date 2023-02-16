def first_generator(n):
    for i in range(n):
        yield i * i


def even_numbers(n):
    for num in range(0, n+1, 2):
        yield str(num)

def third_generator(n):
    for num in range(n + 1):
        if num % 3 == 0 and num % 4 == 0:
            yield num

def fourth_generator(a, b):
    for i in range(a, b+1):
        yield i ** 2

def fifth_generator(n):
    for i in range(n, -1, -1):
        yield i

# gen = first_generator(int(input()))
# for i in gen:
#     print(i)


# n = int(input("Enter a number: "))
# print(', '.join(even_numbers(n)))

# gen = third_generator(int(input()))
# for i in gen:
#     print(i)

# for num in fourth_generator(1, 5):
#     print(num)

# for num in fifth_generator(10):
#     print(num, end = " ")