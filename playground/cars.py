class Car:
    runs = True
    number_of_wheels = 4

    def __init__(self, name):
        print(f"instantiating vehicle: {name}")
        self.name = name

    def __str__(self):
        runStr = "is running"
        if self.runs is False:
            runStr = "is not running"

        return f"{self.name} {runStr} has {self.number_of_wheels} wheels"

    def __repr__(self):
        return f"Car({self.name})"
    
    def start(self):
        if self.runs:
            print(f"{self.name} car is started")
        else:
            print(f"{self.name} car is broken")

    @classmethod
    def get_number_of_wheels(cls):
        return cls.number_of_wheels
    

my_chevy = Car("chevy")
print(type(my_chevy))
my_chevy.start()
print(my_chevy.name)
my_chevy.runs = False
print(Car.runs)
my_chevy.start()
mustang = Car("mustang")
mustang.start()

print(isinstance(my_chevy, Car))

print(my_chevy)
print(repr(my_chevy))

print(mustang)