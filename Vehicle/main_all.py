from landVehicles import Bike, Car, ElectricCar, ElectricBike
from passenger_vehicles import Sedan, SUV
from commercial_vehicles import CommercialTruck, CommercialBus

def display_menu():
    print("\n=== Vehicle Management System ===")
    print("1. Add Regular Vehicle")
    print("2. Add Passenger Vehicle")
    print("3. Add Commercial Vehicle")
    print("4. Display All Vehicles")
    print("5. Search Vehicle by Registration Number")
    print("6. Exit")
    return input("Enter your choice (1-6): ")

def add_regular_vehicle():
    print("\n=== Add Regular Vehicle ===")
    print("1. Bike")
    print("2. Car")
    print("3. Electric Bike")
    print("4. Electric Car")
    choice = input("Enter your choice (1-4): ")
    
    # Common attributes
    brand = input("Enter brand: ")
    model = input("Enter model: ")
    year = int(input("Enter year: "))
    color = input("Enter color: ")
    price = float(input("Enter price ($): "))
    registration_number = input("Enter registration number: ")

    if choice in ['1', '2']:  # Fuel-based vehicles
        fuel_type = input("Enter fuel type (Petrol/Diesel): ")
    else:  # Electric vehicles
        fuel_type = "Electric"

    if choice == '1':
        return Bike(brand, model, year, color, price, fuel_type, registration_number)
    elif choice == '2':
        return Car(brand, model, year, color, price, fuel_type, registration_number)
    elif choice == '3':
        return ElectricBike(brand, model, year, color, price, fuel_type, registration_number)
    elif choice == '4':
        return ElectricCar(brand, model, year, color, price, fuel_type, registration_number)

def add_passenger_vehicle():
    print("\n=== Add Passenger Vehicle ===")
    print("1. Sedan")
    print("2. SUV")
    choice = input("Enter your choice (1-2): ")
    
    # Common attributes
    brand = input("Enter brand: ")
    model = input("Enter model: ")
    year = int(input("Enter year: "))
    color = input("Enter color: ")
    price = float(input("Enter price ($): "))
    fuel_type = input("Enter fuel type (Petrol/Diesel): ")
    registration_number = input("Enter registration number: ")

    if choice == '1':
        return Sedan(brand, model, year, color, price, fuel_type, registration_number)
    elif choice == '2':
        return SUV(brand, model, year, color, price, fuel_type, registration_number)

def add_commercial_vehicle():
    print("\n=== Add Commercial Vehicle ===")
    print("1. Commercial Car")
    print("2. Taxi")
    choice = input("Enter your choice (1-2): ")
    
    # Common attributes
    brand = input("Enter brand: ")
    model = input("Enter model: ")
    year = int(input("Enter year: "))
    color = input("Enter color: ")
    price = float(input("Enter price ($): "))
    fuel_type = input("Enter fuel type (Petrol/Diesel): ")
    registration_number = input("Enter registration number: ")
    license_type = input("Enter license type (Commercial/Taxi): ")

    if choice == '1':
        return CommercialTruck(brand, model, year, color, price, fuel_type, registration_number, license_type)
    elif choice == '2':
        return CommercialBus(brand, model, year, color, price, fuel_type, registration_number, license_type)

def main():
    vehicles = []
    while True:
        choice = display_menu()
        
        if choice == '1':
            vehicle = add_regular_vehicle()
            if vehicle:
                vehicles.append(vehicle)
                print("\nVehicle added successfully!")
                vehicle.display()
        
        elif choice == '2':
            vehicle = add_passenger_vehicle()
            if vehicle:
                vehicles.append(vehicle)
                print("\nVehicle added successfully!")
                vehicle.display()
        
        elif choice == '3':
            vehicle = add_commercial_vehicle()
            if vehicle:
                vehicles.append(vehicle)
                print("\nVehicle added successfully!")
                vehicle.display()
        
        elif choice == '4':
            if not vehicles:
                print("\nNo vehicles in the system!")
            else:
                print("\n=== All Vehicles ===")
                for i, vehicle in enumerate(vehicles, 1):
                    print(f"\nVehicle {i}:")
                    vehicle.display()
        
        elif choice == '5':
            reg_num = input("\nEnter registration number to search: ")
            found = False
            for vehicle in vehicles:
                if vehicle.get_registration_number().lower() == reg_num.lower():
                    print("\nVehicle found:")
                    vehicle.display()
                    found = True
                    break
            if not found:
                print("\nVehicle not found!")
        
        elif choice == '6':
            print("\nThank you for using Vehicle Management System!")
            break
        
        else:
            print("\nInvalid choice! Please try again.")

if __name__ == "__main__":
    main()
