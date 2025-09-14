from vhicleHerarcy import Vehicle
class Air(Vehicle):
    def __init__(self, brand, model, year, color, mileage, price, fuel_type, transmission, chassis_number, registration_number, max_altitude, max_speed, range):
        super().__init__(brand, model, year, color, mileage, price, fuel_type, transmission, chassis_number, registration_number)
        self.__max_altitude = max_altitude
        self.__max_speed = max_speed
        self.__range = range

    def get_max_altitude(self):
        return self.__max_altitude

    def get_max_speed(self):
        return self.__max_speed

    def get_range(self):
        return self.__range

    def display(self):
        print(f"Air Vehicle Information:")
        print(f"Brand: {self.get_brand()}")
        print(f"Model: {self.get_model()}")
        print(f"Year: {self.get_year()}")
        print(f"Color: {self.get_color()}")
        print(f"Mileage: {self.get_mileage()} km")
        print(f"Price: ${self.get_price()}")
        print(f"Fuel Type: {self.get_fuel_type()}")
        print(f"Transmission: {self.get_transmission()}")
        print(f"Chassis Number: {self.get_chassis_number()}")
        print(f"Registration Number: {self.get_registration_number()}")
        print(f"Max Altitude: {self.get_max_altitude()} meters")
        print(f"Max Speed: {self.get_max_speed()} km/h")
        print(f"Range: {self.get_range()} km")
class Helicopter(Air):
    def __init__(self, brand, model, year, color, mileage, price, fuel_type, transmission, chassis_number, registration_number, max_altitude, max_speed, range, rotor_diameter):
        super().__init__(brand, model, year, color, mileage, price, fuel_type, transmission, chassis_number, registration_number, max_altitude, max_speed, range)
        self.__rotor_diameter = rotor_diameter  # in meters

    def get_rotor_diameter(self):
        return self.__rotor_diameter

    def display(self):
        print(f"Helicopter Information:")
        print(f"Brand: {self.get_brand()}")
        print(f"Model: {self.get_model()}")
        print(f"Year: {self.get_year()}")
        print(f"Color: {self.get_color()}")
        print(f"Mileage: {self.get_mileage()} km")
        print(f"Price: ${self.get_price()}")
        print(f"Fuel Type: {self.get_fuel_type()}")
        print(f"Transmission: {self.get_transmission()}")
        print(f"Chassis Number: {self.get_chassis_number()}")
        print(f"Registration Number: {self.get_registration_number()}")
        print(f"Max Altitude: {self.get_max_altitude()} meters")
        print(f"Max Speed: {self.get_max_speed()} km/h")
        print(f"Range: {self.get_range()} km")
        print(f"Rotor Diameter: {self.get_rotor_diameter()} meters")