class Vehicle:
    def __init__(self, name, type):
        self.name = name
        self.kind = type
        self.car = self.Car()
        self.bike = self.Bike()
    
    def show(self):
        print("Name : ",self.name)
        print("Kind : ",self.kind)
    
    class Car:
        def __init__(self):
            self.name = "MARUTI SUZUKI"
            self.speed = "120 km/hr"
        def show(self):
            print("Name : ",self.name)
            print("Speed : ",self.speed)
    
    class Bike:
        def __init__(self):
            self.name = "YAMAHA"
            self.speed = "80 km/hr"
        def show(self):
            print("Name : ",self.name)
            print("Speed : ",self.speed)

a = Vehicle("Sedan","Car")
b = Vehicle("Scooter","Bike")
a.show()
print("\n")
b.show()
print("\n")
c = b.Car()
c1 = b.Bike()
c.show()
print("\n")
c1.show()                            