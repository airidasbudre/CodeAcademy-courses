# Task 1

class Car():
    def __init__(self, year, model, fuel_type):
        self.year = year
        self.model = model
        self.fuel_type = fuel_type

    def drive(self):
        print("Driving")
    
    def add_fuel(self):
        print("Adding fuel")
    
    def Parking(self):
        print("Parking")

class Electric_Car(Car):
    def add_fuel(self):  
       print("Battery charged")

    def drive_automatically(self):
        print("Driving automatically")

audi = Car("2008", "A4", "diesel")
print(audi)

audi.add_fuel()
audi.Parking()
audi.drive()

tesla = Electric_Car("2020", "S", "electric")

tesla.drive_automatically()
tesla.Parking()
tesla.drive()
tesla.add_fuel()

