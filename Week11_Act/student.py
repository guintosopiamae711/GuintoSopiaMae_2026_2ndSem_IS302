class Student:
    def __init__(self, student_id_smg, name_smg, course_smg):
        self.student_id_smg = student_id_smg
        self.name_smg = name_smg
        self.course_smg = course_smg

    def display_info(self):
        print(self.student_id_smg, self.name_smg, self.course_smg)

    def to_record(self):
        return f"{self.student_id_smg},{self.name_smg},{self.course_smg}\n"
