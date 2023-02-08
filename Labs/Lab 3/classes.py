import math

class klass:
    def getString():
        line = input()
        return line
    def printString(line):
        print(line.upper())


class Shape:
    def area():
        return print(0)

class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return print(self.length * self.length)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return print(self.length * self.width)
    

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        return print(self.x, self.y)  
     
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    
    def dist(self, x, y):
        return math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)


class Account:
    def __init__(self):
        self.balance = 5000
        self.owner = "Someone"

    def deposit(self, money):
        self.balance = self.balance + money
        return print("Balance now:", self.balance)
    
    def withdraw(self, withdraw_money):
        if self.balance < withdraw_money:
            print("Withdraw must be lower than you balance!")
        else:
            self.balance = self.balance - withdraw_money
            print("Successful withdraw!")
            return self.balance

# klass.printString(klass.getString())

# s = Shape.area()

# shape_square = Square(int(input("Length of Square:\n")))
# shape_square.area()

# rectangle_length, rectangle_width = input("Rectangle's length and width:\n").split()
# shape_rectangle = Rectangle(int(rectangle_length), int(rectangle_width))
# shape_rectangle.area()

# print(Point(5, 3).dist(6, 4))

withdraw = int(input("How much money you want to withdraw?:\n"))

deposit = int(input("How much money you want to deposit:\n"))

bank = Account()
bank.deposit(deposit)

bank.withdraw(withdraw)