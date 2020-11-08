# Title  : Hierarchical Inheritance
# Author : Kiran Raj R.
# Date   : 08:11:2020

class Automobile:
    def __init__(self, max_speed, fuel, wheels):
        self.fuel = fuel
        self.wheels = wheels
        self.max_speed = max_speed
    
    def print_details(self):
        print(f"Fuel type: {self.fuel}\nNumber of wheels: {self.wheels}\nMax speed: {self.max_speed}")
    
class Car(Automobile):
    def __init__(self, type, fuel,max_speed, company):
        super().__init__(max_speed, fuel, wheels=4)
        self.type = type
        self.company = company
    
    def print_details(self):
        print("-------- Car --------")
        print(f"Car type: {self.type}\nCompany: {self.company}")
        return super().print_details()

class Bus(Automobile):
    def __init__(self, type, max_speed, company):
        super().__init__(max_speed, fuel="Diesel", wheels=6)
        self.type = type
        self.company = company
    
    def print_details(self):
        print("-------- Bus --------")
        print(f"Car type: {self.type}\nCompany: {self.company}")
        return super().print_details()

bus1 = Bus("Carrier", "80km/hr", "TATA")
bus1.print_details()
car1 = Car("Sedan", "petrol", "120km/hr", "TATA")
car1.print_details()