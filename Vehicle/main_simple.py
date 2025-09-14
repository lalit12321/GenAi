from landVehicles import Bike, Car, ElectricCar, ElectricBike

def display_menu():
    print("\n=== Vehicle Management System ===")
    print("1. Add Vehicle")
    print("2. Display All Vehicles")
    print("3. Search Vehicle by Registration Number")
    print("4. Exit")
    return input("Enter your choice (1-4): ")

def add_vehicle():
    print("\n=== Add Vehicle ===")
    print("1. Bike")
    print("2. Car")
    print("3. Electric Bike")
    print("4. Electric Car")
    choice = input("Enter your choice (1-4): ")
    
    # Common attributes for all vehicles
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

    if choice == '1':  # Bike
        return Bike(brand, model, year, color, price, fuel_type, registration_number)
    elif choice == '2':  # Car
        return Car(brand, model, year, color, price, fuel_type, registration_number)
    elif choice == '3':  # Electric Bike
        return ElectricBike(brand, model, year, color, price, fuel_type, registration_number)
    elif choice == '4':  # Electric Car
        return ElectricCar(brand, model, year, color, price, fuel_type, registration_number)

def main():
    vehicles = []
    while True:
        choice = display_menu()
        
        if choice == '1':
            vehicle = add_vehicle()
            if vehicle:
                vehicles.append(vehicle)
                print("\nVehicle added successfully!")
                vehicle.display()
        
        elif choice == '2':
            if not vehicles:
                print("\nNo vehicles in the system!")
            else:
                print("\n=== All Vehicles ===")
                for i, vehicle in enumerate(vehicles, 1):
                    print(f"\nVehicle {i}:")
                    vehicle.display()
        
        elif choice == '3':
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
        
        elif choice == '4':
            print("\nThank you for using Vehicle Management System!")
            break
        
        else:
            print("\nInvalid choice! Please try again.")

if __name__ == "__main__":
    main()
