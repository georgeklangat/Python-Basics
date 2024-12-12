temperature = int(input("Enter the temperature: "))

if temperature > 25:
    print("It is too hot")
else:
    print("It is too cold")


# A program that checks three numbers and returns the smallest
num1 = int(input("Enter a  first number: "))
num2 = int(input("Enter  a second number: "))
num3 = int(input("Enter a third number: "))

if num1 < num2 and num1 < num3:
    print(num1, "is the smallest number")
elif num2 < num1 and num2 < num3:
    print(num2, "is the smallest number")
else:
    print(num3, "is the smallest number")


# program to check whether a number is even or odd
number = 67

if number % 2 == 0:
    print(number, "is an even number")
else:
    print(number, "is an odd number")

