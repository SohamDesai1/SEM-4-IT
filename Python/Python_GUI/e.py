class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def show(self):
        print("Name:", self.name, "\nMileage:", self.mileage, "\nCapacity:", self.capacity)


class Bus(Vehicle):
    def fare(self, distance):
        def_fare = 0
        def_fare = self.capacity * 20 * distance
        print("Fare:", def_fare)
        total_bus_fare = def_fare + 0.1 * def_fare
        print("Total fare:", total_bus_fare)


class Taxi(Vehicle):
    def fare(self, distance):
        def_fare = 0
        def_fare = self.capacity * 10 * distance
        print("Fare:", def_fare)
        total_bus_fare = def_fare + 0.05 * def_fare
        print("Total fare:", total_bus_fare)


School_bus = Bus("School Volvo", 12, 50)
School_bus.show()
School_bus.fare(100)
taxi = Taxi("Taxi", 10, 10)
taxi.show()
taxi.fare(100)
