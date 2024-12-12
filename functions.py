# function is a block of code expected to do a particular task
# There are two types of functions
# 1. Build in functions-functions that already exist in python eg,max(),min()
# 2. User-Defined functions- defining or creating a function as a user

# 1. Build-in libray functions

y = max(34,78,65,45,46)
print(y)

x = min(43,54,23,67)
print(x)

z = pow(2,3)
print("The result is",z)


# 2. User-Defined functions

def greeting():
    print("Hello there")

greeting() # calling a function

# function to add
def add():
    num1 = 7
    num2 = 80
    print(num1+num2)
add()

# Parameter/Variable and Argument/Value
def multiply(x,y):
    print(x*y)

multiply(2,3)
multiply(12,30)
multiply(45,67)

def doctor(name):
    print(name)
doctor("John")
doctor("mary")
doctor("Glory")
