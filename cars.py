class Car:
    runs = True

    def __init__(self, name):
        print(f"instantiating vehicle: {name}")
        self.name = name

    def start(self, name):
        self.name = name

        if self.runs:
            print(f"{self.name} car is started")
        else:
            print(f"{self.name} car is broken")



my_chevy = Car("chevy")

print(type(my_chevy))

my_chevy.start("Chevy")
print(my_chevy.name)

my_chevy.runs = False

print(Car.runs)

my_chevy.start("Chevy")


mustang = Car("mustang")

mustang.start("mustard")