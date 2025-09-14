
students = []

subjects = ["Math", "Physics", "Chemistry", "English", "Computer Science"]

while True:
    print("\n=== Student Management System ===")
    print("1. Add Student")
    print("2. View All Students")
    print("3. View Subject List")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        print("How many students do you want to add?")
        try:
            n = int(input("Enter number of students: "))
            if n <= 0:
                print("Please enter a positive integer.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        for _ in range(n):
            name = input("Enter Student Name: ")
            rollno = input("Enter Roll Number: ")
        
            marks = []
            total_marks = 0
            for subject in subjects:
                while True:
                    try:
                        mark = float(input(f"Enter marks for {subject}: "))
                        if 0 <= mark <= 100:
                            marks.append(mark)
                            total_marks += mark
                            break
                        else:
                            print("Marks should be between 0 and 100.")
                    except ValueError:
                        print("Please enter a valid number.")

            percentage = total_marks / len(subjects)


            student = (name, rollno, total_marks, round(percentage, 2), tuple(marks))
            students.append(student)
        
            print(f"\nStudent '{name}' added successfully!")
    
    elif choice == "2":
        print("\n--- All Students ---")
        if len(students) == 0:
            print("No students available.")
        else:

            header = ["S.No", "Name", "Roll No", "Total Marks", "Percentage"] + subjects
            print("-" * 100)
            print("{:<5} {:<15} {:<10} {:<12} {:<10} {}".format(
                header[0], header[1], header[2], header[3], header[4],
                "  ".join(f"{sub:<15}" for sub in subjects)
            ))
            print("-" * 100)

            for idx, student in enumerate(students, start=1):
                marks_str = "  ".join(f"{mark:<15}" for mark in student[4])
                print("{:<5} {:<15} {:<10} {:<12} {:<10} {}".format(
                    idx, student[0], student[1], student[2], f"{student[3]}%", marks_str
                ))

            print("-" * 100)
    
    elif choice == "3":
        print("\n--- Subject List ---")
        for sub in subjects:
            print(f"- {sub}")
    
    elif choice == "4":
        print("\nExiting... Goodbye!")
        break
    
    else:
        print("\nInvalid choice, please try again.")
1