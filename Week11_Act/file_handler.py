STUDENT_FILE_SMG = "students.txt"


def save_student_smg(student_smg):
    """Append a new student record to students.txt."""
    try:
        with open(STUDENT_FILE_SMG, "a") as file_smg:
            file_smg.write(student_smg.to_record())
    except Exception as error_smg:
        print("Error saving student:", error_smg)


def view_students_smg():
    """Display all student records from students.txt."""
    try:
        with open(STUDENT_FILE_SMG, "r") as file_smg:
            records_smg = [line_smg.strip() for line_smg in file_smg if line_smg.strip()]

        if not records_smg:
            print("No records found.")
            return

        for record_smg in records_smg:
            try:
                student_id_smg, name_smg, course_smg = record_smg.split(",", 2)
                print(student_id_smg, name_smg, course_smg)
            except ValueError:
                print("Skipped invalid record:", record_smg)
    except FileNotFoundError:
        print("No records found.")


def find_student_smg(student_id_smg):
    """Search for a student by ID and return the found record."""
    try:
        with open(STUDENT_FILE_SMG, "r") as file_smg:
            for line_smg in file_smg:
                if not line_smg.strip():
                    continue
                try:
                    stored_id_smg, name_smg, course_smg = line_smg.strip().split(",", 2)
                except ValueError:
                    continue
                if stored_id_smg == student_id_smg:
                    return stored_id_smg, name_smg, course_smg
    except FileNotFoundError:
        return None
    return None
