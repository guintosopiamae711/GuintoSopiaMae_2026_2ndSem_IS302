# employee_roles.py

# Parent Class
class Employee:
    def work_smg(self):
        print("Employee performs tasks")

# Child Class 1: Programmer
class Programmer(Employee):
    def work_smg(self):
        print("Programmer writes code")

# Child Class 2: Designer
class Designer(Employee):
    def work_smg(self):
        print("Designer creates UI designs")

# Instantiate objects for each role
employees_smg = [Programmer(), Designer()]

# Call the work method for each employee
for emp_smg in employees_smg:
    emp_smg.work_smg()