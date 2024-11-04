class Human:
    def __init__(self, name="Human"):
        self.name = name
class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []
    def add_passenger(self, *args):
            for passenger in args:
                self.passengers.append(passenger)
    def print_passengers_names(self):
            if self.passengers != []:
                print(f"Names of{self.brand} passengers: ")
                for passenger in self.passengers:
                    print(passenger.name)
            else:
                print(f"There no passengers in {self.brand}. ")

Feleen = Human("Feleen")
Miguel = Human("Miguel")
car = Auto("BMW M5 F10")
car.add_passenger( Feleen,Miguel)
car.print_passengers_names()
hdfdjhhdf