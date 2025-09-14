employees = []

while True:
    print("\n=== Employee Management System ===")
    print("1. Add Employee")
    print("2. Show All Employees")
    print("3. Search by ID")
    print("4. Search by Name")
    print("5. Salary > 30000")
    print("6. Salary < 15000")
    print("7. Salary between 9000 and 22000")
    print("8. Name ends with 'l'")
    print("9. Odd ID Records")
    print("10. Even ID Records")
    print("11. Second last char is 'a'")
    print("12. Second char is 'A'")
    print("13. Name starts with 'A'")
    print("14. Exit")

    choice = input("Enter your choice (1-14): ")

    if choice == "1":
        try:
            name = input("Enter Employee Name: ").strip()
            if not name.isalpha() or len(name) < 2:
                raise ValueError("Name must contain only letters and be at least 2 characters long.")

            designation = input("Enter Designation: ").strip()
            if not designation.isalpha() or len(designation) < 2:
                raise ValueError("Designation must contain only letters and be at least 2 characters long.")

            emp_id = input("Enter Employee ID (numeric): ").strip()
            if not emp_id.isdigit():
                raise ValueError("Employee ID must be a number.")
            emp_id = int(emp_id)

            if any(emp[3] == emp_id for emp in employees):
                raise ValueError("An employee with this ID already exists.")

            salary_input = input("Enter Salary: ").strip()
            salary = float(salary_input)
            if salary <= 0:
                raise ValueError("Salary must be a positive number.")

            employee = (name, designation, salary, emp_id)
            employees.append(employee)
            print(f"\nEmployee '{name}' added successfully!")

        except ValueError as e:
            print(f"Error: {e}")

    elif choice == "2":
        print("\n--- All Employees ---")
        if len(employees) == 0:
            print("No records found.")
        else:
            print("-" * 80)
            print("{:<5} {:<15} {:<15} {:<10} {:<10}".format("No.", "Name", "Designation", "Salary", "ID"))
            print("-" * 80)
            for idx, emp in enumerate(employees, start=1):
                print("{:<5} {:<15} {:<15} {:<10} {:<10}".format(
                    idx, emp[0], emp[1], emp[2], emp[3]
                ))
            print("-" * 80)

    elif choice == "3":
        try:
            search_id = int(input("Enter ID to search: ").strip())
            found = False
            for emp in employees:
                if emp[3] == search_id:
                    print(f"Found: {emp}")
                    found = True
            if not found:
                print("No employee with this ID found.")
        except ValueError:
            print("Invalid input. Please enter a numeric ID.")

    elif choice == "4":
        search_name = input("Enter Name to search: ").strip().lower()
        if not search_name.isalpha():
            print("Invalid input. Name must contain only letters.")
        else:
            found = False
            for emp in employees:
                if emp[0].lower() == search_name:
                    print(f"Found: {emp}")
                    found = True
            if not found:
                print("No employee with this Name found.")

    elif choice == "5":
        print("\nEmployees with Salary > 30000:")
        found = False
        for emp in employees:
            if emp[2] > 30000:
                print(emp)
                found = True
        if not found:
            print("No employee matches the criteria.")

    elif choice == "6":
        print("\nEmployees with Salary < 15000:")
        found = False
        for emp in employees:
            if emp[2] < 15000:
                print(emp)
                found = True
        if not found:
            print("No employee matches the criteria.")

    elif choice == "7":
        print("\nEmployees with Salary between 9000 and 22000:")
        found = False
        for emp in employees:
            if 9000 <= emp[2] <= 22000:
                print(emp)
                found = True
        if not found:
            print("No employee matches the criteria.")

    elif choice == "8":
        print("\nEmployees where Name ends with 'l' (case-insensitive):")
        found = False
        for emp in employees:
            if emp[0].lower().endswith('l'):
                print(emp)
                found = True
        if not found:
            print("No employee matches the criteria.")

    elif choice == "9":
        print("\nEmployees with Odd ID:")
        found = False
        for emp in employees:
            if emp[3] % 2 != 0:
                print(emp)
                found = True
        if not found:
            print("No employee matches the criteria.")

    elif choice == "10":
        print("\nEmployees with Even ID:")
        found = False
        for emp in employees:
            if emp[3] % 2 == 0:
                print(emp)
                found = True
        if not found:
            print("No employee matches the criteria.")

    elif choice == "11":
        print("\nEmployees where Second Last Character of Name is 'a' (case-insensitive):")
        found = False
        for emp in employees:
            if len(emp[0]) >= 2 and emp[0][-2].lower() == 'a':
                print(emp)
                found = True
        if not found:
            print("No employee matches the criteria.")

    elif choice == "12":
        print("\nEmployees where Second Character is 'A' (case-insensitive):")
        found = False
        for emp in employees:
            if len(emp[0]) >= 2 and emp[0][1].lower() == 'a':
                print(emp)
                found = True
        if not found:
            print("No employee matches the criteria.")

    elif choice == "13":
        print("\nEmployees whose Name starts with 'A' (case-insensitive):")
        found = False
        for emp in employees:
            if emp[0][0].lower() == 'a':
                print(emp)
                found = True
        if not found:
            print("No employee matches the criteria.")

    elif choice == "14":
        print("\nExiting... Goodbye!")
        break

    else:
        print("\nInvalid choice. Please enter a number between 1 and 14.")
