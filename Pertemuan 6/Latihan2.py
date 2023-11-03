class Vehicle:
    def __init__(self, name, registId, acceleration):
        self.name = name
        self.registId = registId
        self.acceleration = acceleration

    def distance(self, time):
        return self.acceleration * time

class Truck(Vehicle):
    def __init__(self, name, registId, acceleration, tonnage):
        super().__init__(name, registId, acceleration)
        self.tonnage = tonnage

    def distance(self, time):
        return self.acceleration * (self.tonnage / 100) * time

class Car(Vehicle):
    def __init__(self, name, registId, acceleration, bodytype):
        super().__init__(name, registId, acceleration)
        self.bodytype = bodytype

    def distance(self, time):
        return self.acceleration * 20 * time

class Bike(Vehicle):
    def __init__(self, name, registId, acceleration, capacity):
        super().__init__(name, registId, acceleration)
        self.capacity = capacity

    def distance(self, time):
        return self.acceleration * (self.capacity / 100) * time

class Bus(Vehicle):
    def __init__(self, name, registId, acceleration, passengers):
        super().__init__(name, registId, acceleration)
        self.passengers = passengers

    def distance(self, time):
        return self.acceleration * (100 / self.passengers) * time

# Membuat objek dari masing-masing kelas
truck = Truck("Truck", "ZXS443", 2, 500)
car = Car("Car", "ABC123", 4, "Coupe")
bike = Bike("Bike", "HGD455", 10, 1000)
bus = Bus("Bus", "BD-1234", 3, 75)

# Menggunakan metode distance pada masing-masing objek
print("Distance Truck setelah 2 jam:", truck.distance(2))
print("Distance Car setelah 2 jam:", car.distance(2))
print("Distance Bike setelah 2 jam:", bike.distance(2))
print("Distance Bus setelah 2 jam:", bus.distance(2))
