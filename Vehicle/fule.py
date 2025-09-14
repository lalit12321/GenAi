from vhicleHerarcy import Vehicle
class FuelBasedVehicle(Vehicle):
    def __init__(self, brand, model, year, color, price, fuel_type, registration_number):
        super().__init__(brand, model, year, color, price, fuel_type, registration_number)
        
    def display(self):
        print(f"Color: {self.get_color()}, Price: ${self.get_price()}")
        print(f"Fuel Type: {self.get_fuel_type()}")
        print(f"Registration Number: {self.get_registration_number()}")

class ElectricVehicle(Vehicle):
    def __init__(self, brand, model, year, color, price, fuel_type, registration_number):
        super().__init__(brand, model, year, color, price, fuel_type, registration_number)
        
    def display(self):
        print(f"Color: {self.get_color()}, Price: ${self.get_price()}")
        print(f"Fuel Type: {self.get_fuel_type()}")
        print(f"Registration Number: {self.get_registration_number()}")

