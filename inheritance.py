# Acquiring attribute or a property from  something
# There must be a parent and the child

# Parent class
class Animal:
    def move(self):
        print("Animal is walking")

# child class
class Dog(Animal):
    def bark(self):
        print("Dog is barking")

a = Animal()
d = Dog()
d.bark()
d.move()

