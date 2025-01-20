import random
top_of_range = input("Type the number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Enter the number that is greater than 0 next time")
        quit()
else:
    print("Enter the number that is greater than 0 next time")
    quit()

random_number = random.randint(0,top_of_range)

guess = 0

while True:
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Enter a number next time")
        continue
    if user_guess == random_number:
        print("you got it")
        break
    else:
        print("You got wrong")
print(f"You got in {guess} guesses")