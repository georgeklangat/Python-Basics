print("**********************************************************")
print("-----------------------------------------------------------")
print("Welcome to The computer game"
      " hoping that you will enjoy the game😘")
print("**********************************************************")
print("-----------------------------------------------------------")

playing=input("DO YOU WANT TO CONTINUE WITH THE GAME? : ").lower()
if playing !="yes":
    quit()
score = 0
count = 0
total = 0

# Central processing unit (CPU)
response = input("What does CPU stand for? ")
if response.lower()=="central processing unit":
    print("correct")
    score+=1
else:
    print("incorrect")
    count+=1
total += 1

# Read only memory(RAM)
response = input("What does ROM stand for? ")
if response.lower()=="read only memory":
    print("correct")
    score += 1
else:
    print("incorrect")
    count += 1
total += 1

# random access memory(RAM)
response = input("What does RAM stand for? ")
if response.lower()=="random access memory":
    print("correct")
    score += 1

else:
    print("incorrect")
    count += 1
total += 1

# Graphic processing unit(GPU)
response = input("What does GPU stand for? ")
if response.lower()=="graphic processing unit":
    print("correct")
    score += 1
else:
    print("incorrect")
    count += 1
total += 1

# Power Supply Unit
response = input("What does PSU stand for? ")
if response.lower()=="power supply unit":
    print("correct")
    score += 1
else:
    print("incorrect")
    count += 1
total += 1

# Total questions
print("TOTAL QUESTIONS: "+str(total))

# print("CORRECT scores: "+str(score))
# print("INCORRECT scores: "+str(count))

print("Correct percentage score is: "+str((score/total)*100)+"%" )
print("Incorrect percentage score is: "+str((count/total)*100)+"%" )

if score >=(total/2):
    print("CONGRAGULATION👏👏👏 you did it nicely")
else:
    print("😒😒sorry you may also try again")



