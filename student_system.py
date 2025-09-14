def create_student(name, roll, subjects, marks):
    total = sum(marks)
    percentage = total / len(subjects) if subjects else 0
    # Return a tuple containing all student information
    return (name, roll, tuple(subjects), tuple(marks), total, percentage)

def print_table(students):
    # Print header
    print("\n" + "="*80)
    print(f"{'Name':<15} {'Roll':<8} {'Subjects':<30} {'Marks':<15} {'Total':<8} {'%':<6}")
    print("="*80)
    
    # Print each student's data
    for student in students:
        name, roll, subjects, marks, total, percentage = student
        subjects_str = ", ".join(subjects)
        marks_str = ", ".join(map(str, marks))
        print(f"{name:<15} {roll:<8} {subjects_str:<30} {marks_str:<15} {total:<8} {percentage:>5.1f}")
    print("="*80)

def main():
    # Initialize empty list to store student records
    students = []

    # Sample data - adding tuples to the list
    students.append(create_student("Rahul Kumar", "A101", ["Math", "Science", "English"], [85, 92, 78]))
    students.append(create_student("Priya Singh", "A102", ["Math", "Science", "English"], [90, 88, 95]))
    students.append(create_student("Amit Sharma", "A103", ["Math", "Science", "English"], [75, 82, 88]))
    
    # Sort students by name (demonstration of list method)
    students.sort(key=lambda x: x[0])
    
    # Print the student table
    print("\nStudent Management System")
    print_table(students)

if __name__ == "__main__":
    main()
