import ModuleForStudent as ms
students = []

while True:
    print("\n=== Student Management System ===")
    print("1. Add Student")
    print("2. Show All Students")
    print("3. Search by Roll Number")
    print("4. Search by Name")
    print("5. Show Students with Percentage > 80")
    print("6. Sort Students by Name")
    print("7. Sort Students by Percentage (Descending)")
    print("8. Update Student Marks by Roll Number")
    print("9. Delete Student by Roll Number")
    print("10. Exit")

    choice = input("Enter your choice (1-10): ").strip()

    if choice == "1":
        try:
            name = input("Enter Student Name: ").strip()
            rollno = input("Enter Roll Number: ").strip()

            print(f"\nEnter marks for {len(ms.subjects)} subjects:")
            marks = []
            for subj in ms.subjects:
                while True:
                    try:
                        mark = float(input(f"{subj}: "))
                        if 0 <= mark <= 100:
                            marks.append(mark)
                            break
                        else:
                            print("Marks must be between 0 and 100.")
                    except ValueError:
                        print("Invalid input. Enter a number.")

            ms.add_student(students, name, rollno, marks)

        except Exception as e:
            print(f"Error: {e}")

    elif choice == "2":
        print("\nAll Students:")
        ms.display_students(students)

    elif choice == "3":
        search_roll = input("Enter Roll Number to search: ").strip()
        result = ms.search_by_rollno(students, search_roll)
        if result:
            print("\nStudent Found:")
            print(result)
        else:
            print("No student found with this Roll Number.")

    elif choice == "4":
        search_name = input("Enter Name to search: ").strip()
        results = ms.search_by_name(students, search_name)
        if results:
            print("\nMatching Students:")
            ms.display_students(results)
        else:
            print("No student found with this Name.")

    elif choice == "5":
        high_perc_students = ms.filter_by_percentage(students, 80, 100)
        print("\nStudents with Percentage > 80:")
        ms.display_students(high_perc_students)

    elif choice == "6":
        sorted_students = ms.sort_students_by_name(students)
        print("\nStudents Sorted by Name:")
        ms.display_students(sorted_students)

    elif choice == "7":
        sorted_students = ms.sort_students_by_percentage(students)
        print("\nStudents Sorted by Percentage (Descending):")
        ms.display_students(sorted_students)

    elif choice == "8":
        rollno = input("Enter Roll Number to update marks: ").strip()
        print(f"\nEnter new marks for {len(ms.subjects)} subjects:")
        new_marks = []
        for subj in ms.subjects:
            while True:
                try:
                    mark = float(input(f"{subj}: "))
                    if 0 <= mark <= 100:
                        new_marks.append(mark)
                        break
                    else:
                        print("Marks must be between 0 and 100.")
                except ValueError:
                    print("Invalid input. Enter a number.")

        try:
            ms.update_student_marks(students, rollno, new_marks)
        except Exception as e:
            print(f"Error: {e}")

    elif choice == "9":
        rollno = input("Enter Roll Number to delete: ").strip()
        ms.delete_student(students, rollno)

    elif choice == "10":
        print("\nExiting... Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 10.")
