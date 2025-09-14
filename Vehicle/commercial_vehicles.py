from landVehicles import Truck, Bus

class CommercialVehicle:
    def __init__(self, license_type, max_operating_hours):
        self.__license_type = license_type
        self.__max_operating_hours = max_operating_hours

    def get_license_type(self):
        return self.__license_type

    def get_max_operating_hours(self):
        return self.__max_operating_hours

class CommercialTruck(Truck, CommercialVehicle):
    def __init__(self, brand, model, year, color, mileage, price, fuel_type, transmission, 
                 chassis_number, registration_number, load_capacity, license_type, max_operating_hours,
                 cargo_type):
        Truck.__init__(self, brand, model, year, color, mileage, price, fuel_type, transmission, 
                      chassis_number, registration_number, load_capacity)
        CommercialVehicle.__init__(self, license_type, max_operating_hours)
        self.__cargo_type = cargo_type

    def get_cargo_type(self):
        return self.__cargo_type

    def display(self):
        super().display()
        print(f"License Type: {self.get_license_type()}")
        print(f"Max Operating Hours: {self.get_max_operating_hours()} hours")
        print(f"Cargo Type: {self.get_cargo_type()}")

class CommercialBus(Bus, CommercialVehicle):
    def __init__(self, brand, model, year, color, mileage, price, fuel_type, transmission, 
                 chassis_number, registration_number, seating_capacity, license_type, max_operating_hours,
                 route_type):
        Bus.__init__(self, brand, model, year, color, mileage, price, fuel_type, transmission, 
                    chassis_number, registration_number, seating_capacity)
        CommercialVehicle.__init__(self, license_type, max_operating_hours)
        self.__route_type = route_type

    def get_route_type(self):
        return self.__route_type

    def display(self):
        super().display()
        print(f"License Type: {self.get_license_type()}")
        print(f"Max Operating Hours: {self.get_max_operating_hours()} hours")
        print(f"Route Type: {self.get_route_type()}")
