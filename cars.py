class Car:
    runs = True
    number_of_wheels = 4

    def __init__(self, name):
        print(f"instantiating vehicle: {name}")
        self.name = name

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

