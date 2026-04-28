# student_inheritance.py

# Parent class
class Person:
    def __init__(self, name_smg, age_smg):
        self.name_smg = name_smg
        self.age_smg = age_smg


# Child class
class Student(Person):
    def __init__(self, name_smg, age_smg, course_smg):
        super().__init__(name_smg, age_smg)  # call parent constructor
        self.course_smg = course_smg

    # method to display student information
    def display_student_smg(self):
        print("Name:", self.name_smg)
        print("Age:", self.age_smg)
        print("Course:", self.course_smg)


# create object
student1_smg = Student("Maria", 20, "BSIS")

# display info
student1_smg.display_student_smg()