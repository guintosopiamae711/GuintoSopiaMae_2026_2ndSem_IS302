class Student_smg:
    def __init__(self_smg, name_smg, student_id_smg, course_smg):
        self_smg.name_smg = name_smg
        self_smg.student_id_smg = student_id_smg
        self_smg.course_smg = course_smg
    
    def display_student_smg(self_smg):
        print("Name:", self_smg.name_smg)
        print("Student ID:", self_smg.student_id_smg)
        print("Course:", self_smg.course_smg)

student1_smg = Student_smg("Maria", "2023-001", "BSIS")
student1_smg.display_student_smg()
