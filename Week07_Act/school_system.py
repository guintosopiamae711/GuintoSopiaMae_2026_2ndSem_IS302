# school_system.py

# Parent class
class Person:
    def __init__(self, name_smg, age_smg):
        self.name_smg = name_smg
        self.age_smg = age_smg

    def display_info_smg(self):
        print("Name:", self.name_smg)
        print("Age:", self.age_smg)


# Child class: Student
class Student(Person):
    def __init__(self, name_smg, age_smg, course_smg):
        super().__init__(name_smg, age_smg)
        self.course_smg = course_smg

    def display_info_smg(self):
        print("=== Student Information ===")
        print("Name:", self.name_smg)
        print("Age:", self.age_smg)
        print("Course:", self.course_smg)


# Child class: Teacher
class Teacher(Person):
    def __init__(self, name_smg, age_smg, subject_smg):
        super().__init__(name_smg, age_smg)
        self.subject_smg = subject_smg

    def display_info_smg(self):
        print("=== Teacher Information ===")
        print("Name:", self.name_smg)
        print("Age:", self.age_smg)
        print("Subject:", self.subject_smg)


# create objects
student1_smg = Student("Maria", 20, "BSIS")
teacher1_smg = Teacher("Mr. Cruz", 40, "Mathematics")

# display outputs
student1_smg.display_info_smg()
print()
teacher1_smg.display_info_smg()