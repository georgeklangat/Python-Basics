class Person:
    # properties/Variables/Attributes/Characteristics
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    # Behaviour/Method/Function
    def study(self):
        print("Student is studying")

# creating and object
student1 = Person("George", 24,"male")
print(student1.name,student1.age,student1.gender)
student1.study()

student2 =Person("Alex",45,"male")
print(student2.name,student2.age,student2.gender)

student3 = Person("Beatrice",34,"female")
print(student3.name,student3.age,student3.gender)
