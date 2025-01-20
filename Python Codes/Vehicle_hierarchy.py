class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")


class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Number of doors: {self.num_doors}")


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, num_wheels):
        super().__init__(make, model, year)
        self.num_wheels = num_wheels

    def display_info(self):
        super().display_info()
        print(f"Number of wheels: {self.num_wheels}")


class Truck(Vehicle):
    def __init__(self, make, model, year, payload_capacity):
        super().__init__(make, model, year)
        self.payload_capacity = payload_capacity

    def display_info(self):
        super().display_info()
        print(f"Payload capacity: {self.payload_capacity} lbs")


# Create instances of the subclasses
car1 = Car("Toyota", "Camry", 2022, 4)
motorcycle1 = Motorcycle("Harley-Davidson", "Sportster", 2021, 2)
truck1 = Truck("Ford", "F-150", 2023, 2000)

# Display information for each vehicle
car1.display_info()
motorcycle1.display_info()
truck1.display_info()
