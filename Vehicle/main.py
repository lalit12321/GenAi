from commercial_vehicles import CommercialBus, CommercialTruck
from passenger_vehicles import SUV, Sedan
from landVehicles import Bike, Car, ElectricCar, ElectricBike

def display_menu():
    print("\n=== Vehicle Management System ===")
    print("1. Add Regular Vehicles")
    print("2. Add Passenger Vehicles")
    print("3. Add Commercial Vehicles")
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
    
    # Common attributes for all vehicles
    brand = input("Enter brand: ")
    model = input("Enter model: ")
    year = int(input("Enter year: "))
    color = input("Enter color: ")
    mileage = float(input("Enter mileage (km): "))
    price = float(input("Enter price ($): "))
    transmission = input("Enter transmission type: ")
    chassis_number = input("Enter chassis number: ")
    registration_number = input("Enter registration number: ")

    if choice in ['1', '2']:  # Fuel-based vehicles
        fuel_type = input("Enter fuel type: ")
    else:  # Electric vehicles
        fuel_type = "Electric"
        battery_capacity = float(input("Enter battery capacity (kWh): "))

    if choice == '1':  # Bike
        engine_capacity = int(input("Enter engine capacity (cc): "))
        return Bike(brand, model, year, color, mileage, price, fuel_type, transmission,
                   chassis_number, registration_number, engine_capacity)
    elif choice == '2':  # Car
        return Car(brand, model, year, color, mileage, price, fuel_type, transmission,
                  chassis_number, registration_number)
    elif choice == '3':  # Electric Bike
        return ElectricBike(brand, model, year, color, mileage, price, fuel_type, transmission,
                          chassis_number, registration_number, battery_capacity)
    elif choice == '4':  # Electric Car
        return ElectricCar(brand, model, year, color, mileage, price, fuel_type, transmission,
                         chassis_number, registration_number, battery_capacity)

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
    mileage = float(input("Enter mileage (km): "))
    price = float(input("Enter price ($): "))
    fuel_type = input("Enter fuel type: ")
    transmission = input("Enter transmission type: ")
    chassis_number = input("Enter chassis number: ")
    registration_number = input("Enter registration number: ")
    num_doors = int(input("Enter number of doors: "))

    if choice == '1':  # Sedan
        trunk_capacity = float(input("Enter trunk capacity (liters): "))
        return Sedan(brand, model, year, color, mileage, price, fuel_type, transmission,chassis_number, registration_number, num_doors, trunk_capacity)
    elif choice == '2':  # SUV
        ground_clearance = float(input("Enter ground clearance (mm): "))
        return SUV(brand, model, year, color, mileage, price, fuel_type, transmission,
                  chassis_number, registration_number, num_doors, ground_clearance)

def add_commercial_vehicle():
    print("\n=== Add Commercial Vehicle ===")
    print("1. Commercial Truck")
    print("2. Commercial Bus")
    choice = input("Enter your choice (1-2): ")

    # Common attributes
    brand = input("Enter brand: ")
    model = input("Enter model: ")
    year = int(input("Enter year: "))
    color = input("Enter color: ")
    mileage = float(input("Enter mileage (km): "))
    price = float(input("Enter price ($): "))
    fuel_type = input("Enter fuel type: ")
    transmission = input("Enter transmission type: ")
    chassis_number = input("Enter chassis number: ")
    registration_number = input("Enter registration number: ")
    license_type = input("Enter license type: ")
    max_operating_hours = float(input("Enter maximum operating hours: "))

    if choice == '1':  # Commercial Truck
        load_capacity = float(input("Enter load capacity (tons): "))
        cargo_type = input("Enter cargo type: ")
        return CommercialTruck(brand, model, year, color, mileage, price, fuel_type, transmission,
                             chassis_number, registration_number, load_capacity, license_type,
                             max_operating_hours, cargo_type)
    elif choice == '2':  # Commercial Bus
        seating_capacity = int(input("Enter seating capacity: "))
        route_type = input("Enter route type: ")
        return CommercialBus(brand, model, year, color, mileage, price, fuel_type, transmission,
                           chassis_number, registration_number, seating_capacity, license_type,
                           max_operating_hours, route_type)

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
