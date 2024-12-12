# Arrays carries similar datatypes unlike the list that carries different datatypes

courses = ["MIT","Cybersecurity","datascience"]
print(courses)

# Accessing an element in array
print(courses[1])

# Looping through an element
print("Courses are:")
for x in courses:
    print(x)


# Adding new element into an array
courses.append("Web development")
print(courses)


# Deleting and element
courses.remove("MIT")
print(courses)