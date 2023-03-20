class Vehicle:
    
    def __init__(self, make, model, fuel="gas"):
        self.make = make
        self.model = model
        self.fuel = fuel

    def is_eco_friendly(self):
        if self.fuel == "gas":
            return False
        else:
            return True


class Car(Vehicle):

    def __init__(self, make, model, fuel="gas", num_of_wheels = 4):
        super().__init__(make, model, fuel)
        # self.make = make
        # self.model = model
        # self.fuel = fuel
        self.num_of_wheels = num_of_wheels


# print(Vehicle.is_eco_friendly())

vehicle = Vehicle("chevy", "equinox")

print(vehicle.is_eco_friendly())