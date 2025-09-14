from landVehicles import Car

class PassengerCar(Car):
    def __init__(self, brand, model, year, color, price, fuel_type, registration_number):
        super().__init__(brand, model, year, color, price, fuel_type,  registration_number)
        
    
    def display(self):
        super().display()
        

class Sedan(PassengerCar):
    def __init__(self, brand, model, year, color,  price, fuel_type,  registration_number):
        super().__init__(brand, model, year, color,  price, fuel_type, registration_number, "Sedan")
        

    def display(self):
        super().display()
       

class SUV(PassengerCar):
    def __init__(self, brand, model, year, color, price, fuel_type, registration_number, num_doors):
        super().__init__(brand, model, year, color, price, fuel_type, registration_number, "SUV")
        

    def display(self):
        super().display()
       