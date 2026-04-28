# employee_system.py

class Employee:
    def __init__(self, name_smg):
        self.__name_smg = name_smg      # private attribute
        self.__salary_smg = 0           # private attribute

    # method to set salary
    def set_salary_smg(self, salary_smg):
        if salary_smg > 0:
            self.__salary_smg = salary_smg
        else:
            print("Invalid salary amount")

    # method to get salary
    def get_salary_smg(self):
        return self.__salary_smg


# create an employee object
emp_smg = Employee("Ana")

# set and display salary
emp_smg.set_salary_smg(30000)
print("Salary:", emp_smg.get_salary_smg())