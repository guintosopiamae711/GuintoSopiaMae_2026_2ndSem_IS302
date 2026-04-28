# student_private.py

class Student:
    def __init__(self, name_smg, student_id_smg, gpa_smg):
        self.__name_smg = name_smg           # private attribute
        self.__student_id_smg = student_id_smg
        self.__gpa_smg = gpa_smg

    # method to display student information
    def get_student_info_smg(self):
        print("Name:", self.__name_smg)
        print("Student ID:", self.__student_id_smg)
        print("GPA:", self.__gpa_smg)


# create an object
student1_smg = Student("Juan", "2023-001", 1.75)

# display student info
student1_smg.get_student_info_smg()