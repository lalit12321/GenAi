# student_module.py

subjects = ["Math", "Physics", "Chemistry", "English", "Computer Science"]

def add_student(students, name, rollno, marks):
    if len(marks) != len(subjects):
        raise ValueError(f"Marks for all {len(subjects)} subjects are required.")

    total_marks = sum(marks)
    percentage = round(total_marks / len(subjects), 2)
    student = (name, rollno, total_marks, percentage, tuple(marks))
    students.append(student)
    print(f"Student '{name}' added successfully!")


def display_students(students):
    if not students:
        print("No student records found.")
        return

    print("-" * 80)
    print("{:<5} {:<15} {:<10} {:<10} {:<12} {}".format(
        "No.", "Name", "Roll No", "Total", "Percentage", "Marks"
    ))
    print("-" * 80)
    for idx, student in enumerate(students, start=1):
        print("{:<5} {:<15} {:<10} {:<10} {:<12} {}".format(
            idx, student[0], student[1], student[2], student[3], student[4]
        ))
    print("-" * 80)


def search_by_rollno(students, rollno):
    for student in students:
        if student[1] == rollno:
            return student
    return None


def search_by_name(students, name):
    name = name.lower()
    return [student for student in students if student[0].lower() == name]


def filter_by_percentage(students, min_perc, max_perc):
    return [s for s in students if min_perc <= s[3] <= max_perc]


def filter_by_subject_marks(students, subject_index, min_mark):
    return [s for s in students if s[4][subject_index] >= min_mark]


def sort_students_by_name(students):
    return sorted(students, key=lambda s: s[0].lower())


def sort_students_by_percentage(students):
    return sorted(students, key=lambda s: s[3], reverse=True)


def delete_student(students, rollno):
    for idx, student in enumerate(students):
        if student[1] == rollno:
            del students[idx]
            print(f"Student with Roll No {rollno} deleted successfully!")
            return True
    print(f"No student found with Roll No {rollno}.")
    return False


def update_student_marks(students, rollno, new_marks):
    for idx, student in enumerate(students):
        if student[1] == rollno:
            if len(new_marks) != len(subjects):
                raise ValueError(f"Must provide marks for all {len(subjects)} subjects.")

            total_marks = sum(new_marks)
            percentage = round(total_marks / len(subjects), 2)
            updated_student = (student[0], student[1], total_marks, percentage, tuple(new_marks))
            students[idx] = updated_student
            print(f"Marks for Roll No {rollno} updated successfully!")
            return True
    print(f"No student found with Roll No {rollno}.")
    return False
