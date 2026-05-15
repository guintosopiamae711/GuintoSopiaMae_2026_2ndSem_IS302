from student import Student
from file_handler import save_student_smg, view_students_smg, find_student_smg


def add_student_smg():
    student_id_smg = input("Enter Student ID: ").strip()
    name_smg = input("Enter Name: ").strip()
    course_smg = input("Enter Course: ").strip()

    if not student_id_smg or not name_smg or not course_smg:
        print("All fields are required.")
        return

    student_smg = Student(student_id_smg, name_smg, course_smg)
    save_student_smg(student_smg)
    print("Student added successfully")


def search_student_smg():
    search_id_smg = input("Enter Student ID to search: ").strip()

    if not search_id_smg:
        print("Student ID is required.")
        return

    student_smg = find_student_smg(search_id_smg)
    if student_smg:
        print("Student Found:")
        print(student_smg[0], student_smg[1], student_smg[2])
    else:
        print("Student not found")


if __name__ == "__main__":
    while True:
        print("\nSTUDENT INFORMATION SYSTEM")
        print("1 Add Student")
        print("2 View Students")
        print("3 Search Student")
        print("4 Exit")
        choice_smg = input("Enter choice: ").strip()

        if choice_smg == "1":
            add_student_smg()
        elif choice_smg == "2":
            view_students_smg()
        elif choice_smg == "3":
            search_student_smg()
        elif choice_smg == "4":
            print("Exiting the system...")
            break
        else:
            print("Invalid choice")
