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


    @abstractmethod
    def display(self):
        pass
