# WHILE LOOP

# increasing values
number = 20
while number <=25:
    print(number)
    number += 1

# decreasing values
count = 105
while count >=100:
    print(count)
    count -= 1


# Display even number from 50 to 10  using while loop and skip 42, 40

print("Even numbers from 50 down to 10 (skipping 42 and 42 and 40):")
number = 50
while number >= 10:
    if number !=42 and number !=40:
        print(number, end=" ")
    number -= 2 # Decrement by 2
print() # for clean newline after the output