# BREAK STATEMENT

num = 20
while num <= 25:
    print(num)
    if num == 23:
        break
    num += 1


# CONTINUE STATEMENT
divices = ["laptop","phone","tablet"]
for x in divices:
    if x == "phone":
        continue
    print(x)