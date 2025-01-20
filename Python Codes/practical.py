'''message="hello , world"
for char in message:
    print(char)

student_grade={'George':85,'Emmanuel':75,'mathew':78}
for name,grade in student_grade.items():
    print(f"{name}:{grade}")

student_grade={'George':85,'Emmanuel':75,'mathew':78}
for key,grade in student_grade.items():
    print(f"{key}:{grade}")


    #complex real world use of the for loop
transactions = [
        {'customer': 'Alice', 'amount': 50},
        {'customer': 'Bob', 'amount': 75},
        {'customer': 'Alice', 'amount': 30},
        {'customer': 'Charlie', 'amount': 100},
        {'customer': 'Bob', 'amount': 60}
    ]
sales_totals = {}

for transaction in transactions:
    customer = transaction['customer']
    amount = transaction['amount']

    if customer in sales_totals:
        sales_totals[customer] += amount
    else:
        sales_totals[customer] = amount

for transaction in transactions:
    customer = transaction['customer']
    amount = transaction['amount']

    print(f"Customer: {customer}, Amount: {amount}")


#password checker
def check_password_strength(password):
    length = len(password)
    is_strong = True

    if length < 8:
        print("Weak password! Password should be at least 8 characters long.")
        is_strong = False

    if not any(char.isdigit() for char in password):
        print("Weak password! Password should contain at least one digit.")
        is_strong = False

    if not any(char.isalpha() for char in password):
        print("Weak password! Password should contain at least one letter.")
        is_strong = False

    if is_strong:
        print("Strong password! Good job!")

# Test the password strength checker
passwords = ["abc123", "Password123", "mysecretpass", "strongPassword12"]

for password in passwords:
    print("Checking password:", password)
    check_password_strength(password)
    print()

#printing the odd numbers from 1 to 10
total = 0
for i in range(1,10):
    total+=i
print(total)

squares=[x**2 for x in range(1,6)]
print(squares)

student_name_1 = 'Itika'
student_name_2 = 'Parker'

# Creating a dictionary of records of the students
records = {'Itika': 90, 'Arshia': 92, 'Peter': 46}

def marks(student_name):
    for a_student in records:  # iterate over the keys of the dictionary
        if a_student == student_name:
            return records[a_student]
    return f"There is no student named {student_name} in the records."

# accessing the marks using the `marks()` function
print(f"Marks of {student_name_1} are:", marks(student_name_1))
print(f"Marks of {student_name_2} are:", marks(student_name_2))

def greet_user(first_name,last_name):
    print(f'hi {first_name},{last_name}')
    print("welcome abroad")

print("start")
greet_user(last_name="john",first_name="langat")
greet_user("mary","chumbaa")
print ("finish")


def squares(number):
    return number*number
print(squares(3))'''

'''#PRINTING PROPER ERROR MESSSAGE:Usig TRY and EXCEPT
try:
    age=int(input('age: '))
    income=20000
    risk=income/age
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0')
except ValueError:
    print('Invalid value')'''

'''#CLASSES IN PYTHON-
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y = y
    def move(self):
        print("move")
    def draw(self):
        print("draw")
point1=Point(10,20)
print(point1.x )
point1.move()
point1.draw()'''

import random


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


george = Dice()  # instances of a class
print(george.roll())
