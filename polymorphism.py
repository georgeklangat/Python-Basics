# same Method across the classes having different forms

class Rectangle:
    def shape(self):
        print("Drawing a Rectangle")


class Rombus:
    def shape(self):
        print("Drawing a Rombus")


class Parallelogram:
    def shape(self):
        print("Drawing a Parallelogram")


r = Rectangle()
r.shape()

rhom = Rombus()
rhom.shape()

p = Parallelogram()
p.shape()