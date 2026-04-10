class Student_nbs:
    def __init__(self_nbs, name_nbs, student_id_nbs, course_nbs):
        self_nbs.name_nbs = name_nbs
        self_nbs.student_id_nbs = student_id_nbs
        self_nbs.course_nbs = course_nbs
    
    def display_student_nbs(self_nbs):
        print("Name:", self_nbs.name_nbs)
        print("Student ID:", self_nbs.student_id_nbs)
        print("Course:", self_nbs.course_nbs)

student1_nbs = Student_nbs("Maria", "2023-001", "BSIS")
student1_nbs.display_student_nbs()
