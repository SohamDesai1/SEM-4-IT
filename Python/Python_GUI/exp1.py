class Vehicle:
    def _init_(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def info(self):
        print("Vehicle information\nMaximum Speed:", self.max_speed, "\nMileage:", self.mileage)


class Bus(Vehicle):
    def bus_fare(self, distance, seating_capacity=50):
        def_fare = self.seating_capacity * 20 * distance
        print("Bus fare:", def_fare)

    def show(self):
        print("Speed:", self.max_speed, "\nMileage:", self.mileage)


def_fare = 100
total_bus_fare = def_fare + 0.1 * def_fare
print("BUS: The Group will incurr an expenditure of", str(total_bus_fare), "for travelling 100 km distance one way")


class Taxi(Vehicle):
    def show(self):
        print("Speed:", self.max_speed, "\nMileage:", self.mileage)

    def taxi_fare(self, distance):
        fare = self.seating_capacity * 20 * distance
        print("TAXI: The passengers will incur an expenditure of", str(fare), "for travelling 100 km distance one way")


Bus_obj = Bus(100, 10)
Bus_obj.show()