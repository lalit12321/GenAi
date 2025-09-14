from fule import FuelBasedVehicle, ElectricVehicle

class Bike(FuelBasedVehicle):
    def __init__(self, brand, model, year, color, price, fuel_type, registration_number):
        super().__init__(brand, model, year, color, price, fuel_type, registration_number)

    def display(self):
        print(f"Bike: {self.get_brand()} {self.get_model()} ({self.get_year()})")
        super().display()

class Car(FuelBasedVehicle):
    def __init__(self, brand, model, year, color, price, fuel_type, registration_number):
        super().__init__(brand, model, year, color, price, fuel_type, registration_number)


    def display(self):
        print(f"Car: {self.get_brand()} {self.get_model()} ({self.get_year()})")
        super().display()
class Truck(FuelBasedVehicle):
    def __init__(self, brand, model, year, color, mileage, price, fuel_type, transmission, chassis_number, registration_number, load_capacity):
        super().__init__(brand, model, year, color, mileage, price, fuel_type, transmission, chassis_number, registration_number, fuel_tank_capacity=0)
        self.__load_capacity = load_capacity 

    def get_load_capacity(self):
        return self.__load_capacity

    def display(self):
        print(f"Truck: {self.get_brand()} {self.get_model()} ({self.get_year()})")
        super().display()
        print(f"Load Capacity: {self.get_load_capacity()} tons")
class Bus(FuelBasedVehicle):
    def __init__(self, brand, model, year, color, mileage, price, fuel_type, transmission, chassis_number, registration_number, seating_capacity):
        super().__init__(brand, model, year, color, mileage, price, fuel_type, transmission, chassis_number, registration_number, fuel_tank_capacity=0)
        self.__seating_capacity = seating_capacity  # number of seats

    def get_seating_capacity(self):
        return self.__seating_capacity

    def display(self):
        print(f"Bus: {self.get_brand()} {self.get_model()} ({self.get_year()})")
        super().display()
        print(f"Seating Capacity: {self.get_seating_capacity()} seats")
class ElectricCar(ElectricVehicle):
    def __init__(self, brand, model, year, color, price, fuel_type, registration_number):
        super().__init__(brand, model, year, color, price, fuel_type, registration_number)

    def display(self):
        print(f"Electric Car: {self.get_brand()} {self.get_model()} ({self.get_year()})")
        super().display()

class ElectricBike(ElectricVehicle):
    def __init__(self, brand, model, year, color, price, fuel_type, registration_number):
        super().__init__(brand, model, year, color, price, fuel_type, registration_number)

    def display(self):
        print(f"Electric Bike: {self.get_brand()} {self.get_model()} ({self.get_year()})")
        super().display()
