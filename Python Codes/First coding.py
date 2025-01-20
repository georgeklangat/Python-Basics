
'''#PRINT FUNCTON IN python
a=float(input("Enter the first number:"))
b=float(input("Enter the second number:"))
print("sum:",a+b)
avarage=(a+b)/2
print("avarage:",avarage)'''

'''#python list
l1=["John",102,"USA"]
l2=[1,2,3,4,5,6]
print(type(l1))
print(type(l2))'''

'''#python tuple
#This stores the sequence of immutable python objects
tuple=("Mangos","orages","salads","banana")
print(tuple)'''

#Dictionaries
'''employee={"Name:","John","Age:29","Salary:2500"}
print(type(employee))
print("printing the employee Data...")
print(employee)'''

'''num=int(input("Enter the number:"))
if num%2==0:
    print("The number is even number")
else:
    print("The number is odd")'''


'''first_name="George"
last_name="langat"
msg=f"{first_name} [{last_name}] is coder"
print(msg)

print(msg.upper())
print(len(msg)) #FING THE LENGTH OF THE STRING
print(msg.replace('is','is a determine coder')) #REPLACING THE WORD IN THE STRING
print(msg.find('c'))# RETURNING THE INDEX OF THE CHARACTER
print('George' in msg)#  fINDING A BOOLEAN IN THE CODE
print(type(msg))
'''
'''name="COMPUTER SCIENCE"
print(name.lower())'''

'''import math
x=6.7
print(math.ceil(x))

is_hot=False
is_cold=True
if is_hot:
    print("its a hot day")
    print("Drink a lot of water")
elif is_cold:
    print("its cold day")
    print("ware warm  cold")
else:
    print("Its a cold day")
    print("Wear warm clothes")
print("Enjoy your day dude")'''

'''weight=int(input("Weight:"))
unit=input ("kg or l:")
if unit.upper()== "L":
    converted= weight*0.45
    print(f"your are {converted} kilos")
else:
    converted= weight//0.45
    print(f"you are{converted} pounds")'''

'''i=1
while i<=30:
    print('  *'*i)
    i=i+1
print(' the programme is Done')'''


'''i=0
while i<=100:
    print(i)
    i=i+2
print("Done")'''

'''secret_number=9
guess_count=0
guess_limit=3
while guess_count<guess_limit:
    guess=int(input("Guess: "))
    guess_count+=1
    if guess==secret_number:
        print("You won countinue guessing")
else:
    print("You lost bana be serious and try again!")'''

'''command=""
while :
    command=input("> ").lower()
    if command=="start":
        print("The car started...")
    elif command=="stop":
        print("The car stopped")
    elif command=="help":
        print(
start- to start a car...
stop-to stop the car
quit-to quit
    )
    else:
        print("I dont understand")'''



'''x=int(input("Please Enter the first number:"))
operand=input("place the operand")

y=int(input("Please enter the second the number:"))
if operand=="/":
    print(x/y)
elif operand =="+":
    print(x+y)
elif operand =="-":
    print(x-y)
elif operand =="*":
    print(x*y)
else:
    print("Thee operand does not exit")
print("This is successful computation keep doing the MATH!")'''

'''marks=int(input("Enter the marks: "))

if marks >=70 and marks<=100:
  print("your Grade is: A")
elif marks>=60:
  print("Grade B")
elif marks >=50:
       print("Grade C")
elif marks >=40:
       print("Grade D")
else: marks <=39
print("Grade D")
print("You fail!")

while marks >100 or marks <0:
 print("Invalid choice")'''

'''command = ""
started=False
while True:
    command = input(">").lower()
    if command == "start":
        if started:
            print("car is already started")
        else:
            started=True
            print("car started...")
    elif command == "stop":
        if not started:
            print("car is already stopped.")
        else:
            started=False
            print("car stopped.")
    elif command == "help":
        print("""
start-to start the car
stop- to stop the car
quit-to quit""")
    elif command == "quit":
        break
    else:
        print("Sorry i don't understand the command")'''

'''list=[1,2,3,4,5]
sum=sum(list)

print(sum)'''