# Program to display grade based on total marks
def determine_grade(marks):
    if marks >= 70:
        grade = "A"
    elif 60 <= marks <= 69:
        grade = "B"
    elif 50 <= marks <= 59:
        grade = "C"
    elif 40 <= marks <= 49:
        grade = "D"
    elif 0 <= marks <= 39:
        grade = "E"
    else:
        grade = "Invalid Marks"  # Handle invalid marks
    return grade

# Input marks and display grade
marks = int(input("Enter total marks: "))
print(f"Grade: {determine_grade(marks)}")

    