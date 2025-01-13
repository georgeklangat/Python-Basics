# Dictionary -key-value pair
student = {
    "firstname": "jane",
    "age":25,
    "course":"web Development",
    "gender":"female",
}

print(student)
print(student["gender"])
print(type(student))

# EXAMPLE 2
# Dictionary of marks for students in COM 404
COM_404_dict = {
    "Student1": 85,
    "Student2": 90,
    "Student3": 78,
    "Student4": 92,
    "Student5": 88
}

# Display the contents of the dictionary
# for student, mark in COM_404_dict.items():
#     print(f"{student}: {mark}")

for student,marks in COM_404_dict.items():
    print(f"{student} : {marks}")
