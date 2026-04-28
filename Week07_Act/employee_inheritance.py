# employee_inheritance.py

# Parent class
class Employee:
    def __init__(self, name_smg, salary_smg):
        self.name_smg = name_smg
        self.salary_smg = salary_smg


# Child class
class Manager(Employee):
    def __init__(self, name_smg, salary_smg, department_smg):
        super().__init__(name_smg, salary_smg)  # call parent constructor
        self.department_smg = department_smg

    # method to display manager information
    def display_manager_smg(self):
        print("Name:", self.name_smg)
        print("Salary:", self.salary_smg)
        print("Department:", self.department_smg)


# create object
manager1_smg = Manager("John", 50000, "IT")

# display info
manager1_smg.display_manager_smg()