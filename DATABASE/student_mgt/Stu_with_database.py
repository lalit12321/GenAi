from tabulate import tabulate
import mysql.connector as ms

subjects = ["Math", "Physics", "Chemistry", "English", "Computer Science"]

def get_connection():
    return ms.connect(user="root", password="", host="localhost", database="acro")

def add_student():
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
    con = get_connection()
    cr = con.cursor()
    sql = "INSERT INTO student(name, rollno, total, percentage, math, physics, chemistry, english, computer) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (name, rollno, total_marks, percentage, marks[0], marks[1], marks[2], marks[3], marks[4])
    cr.execute(sql, val)
    con.commit()
    con.close()
    print(f"\nStudent '{name}' added successfully!")

def show_students():
    con = get_connection()
    cr = con.cursor()
    cr.execute("SELECT name, rollno, total, percentage, math, physics, chemistry, english, computer FROM student")
    data = cr.fetchall()
    con.close()
    if data:
        headers = ["Name", "Roll No", "Total", "Percentage"] + subjects
        print(tabulate(data, headers, tablefmt="grid"))
    else:
        print("No students available.")

def update_student():
    rollno = input("Enter Roll Number of student to update: ")
    con = get_connection()
    cr = con.cursor()
    cr.execute("SELECT * FROM student WHERE rollno=%s", (rollno,))
    student = cr.fetchone()
    if not student:
        print("Student not found.")
        con.close()
        return
    print("Enter new details (leave blank to keep current value):")
    name = input(f"Name [{student[1]}]: ") or student[1]
    marks = []
    total_marks = 0
    for i, subject in enumerate(subjects):
        current_mark = student[4 + i]
        mark_input = input(f"{subject} [{current_mark}]: ")
        mark = float(mark_input) if mark_input else current_mark
        marks.append(mark)
        total_marks += mark
    percentage = total_marks / len(subjects)
    sql = "UPDATE student SET name=%s, total=%s, percentage=%s, math=%s, physics=%s, chemistry=%s, english=%s, computer=%s WHERE rollno=%s"
    val = (name, total_marks, percentage, marks[0], marks[1], marks[2], marks[3], marks[4], rollno)
    cr.execute(sql, val)
    con.commit()
    con.close()
    print("Student updated successfully.")

def delete_student():
    rollno = input("Enter Roll Number of student to delete: ")
    con = get_connection()
    cr = con.cursor()
    cr.execute("DELETE FROM student WHERE rollno=%s", (rollno,))
    con.commit()
    con.close()
    print("Student deleted successfully.")

def search_student():
    print("Search by:\n1. Roll Number\n2. Name")
    opt = input("Enter choice: ")
    con = get_connection()
    cr = con.cursor()
    if opt == "1":
        rollno = input("Enter Roll Number: ")
        cr.execute("SELECT name, rollno, total, percentage, math, physics, chemistry, english, computer FROM student WHERE rollno=%s", (rollno,))
    elif opt == "2":
        name = input("Enter Name: ")
        cr.execute("SELECT name, rollno, total, percentage, math, physics, chemistry, english, computer FROM student WHERE name LIKE %s", (f"%{name}%",))
    else:
        print("Invalid choice.")
        con.close()
        return
    data = cr.fetchall()
    con.close()
    if data:
        headers = ["Name", "Roll No", "Total", "Percentage"] + subjects
        print(tabulate(data, headers, tablefmt="grid"))
    else:
        print("Student not found.")

def highest_percentage():
    con = get_connection()
    cr = con.cursor()
    cr.execute("SELECT name, rollno, percentage FROM student ORDER BY percentage DESC LIMIT 1")
    student = cr.fetchone()
    con.close()
    if student:
        print(f"Highest Percentage: {student[2]:.2f}% by {student[0]} (Roll No: {student[1]})")
    else:
        print("No students available.")

while True:
    print("\n=== Student Management System ===")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Highest Percentage")
    print("7. Exit")
    choice = input("Enter your choice (1-7): ")
    if choice == "1":
        add_student()
    elif choice == "2":
        show_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        search_student()
    elif choice == "6":
        highest_percentage()
    elif choice == "7":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")