from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, model, year, color, price, fuel_type, registration_number):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__color = color
        self.__price = price
        self.__fuel_type = fuel_type
        self.__registration_number = registration_number

    
    # def get_brand(self): 
    #     return self.__brand
    # def get_model(self):
    #     return self.__model
    # def get_year(self): 
    #     return self.__year
    # def get_color(self): 
    #     return self.__color
    # def get_price(self): 
    #     return self.__price
    # def get_fuel_type(self): 
    #     return self.__fuel_type
    # def get_registration_number(self): 
    #     return self.__registration_number


    @abstractmethod
    def display(self):
        pass
