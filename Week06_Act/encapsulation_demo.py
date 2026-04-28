# encapsulation_demo.py

class Person:
    def __init__(self, name_smg, age_smg):
        self.__name_smg = name_smg   # private attribute
        self.__age_smg = age_smg     # private attribute

    # getter method for name
    def get_name_smg(self):
        return self.__name_smg

    # getter method for age
    def get_age_smg(self):
        return self.__age_smg


# create an object
p1_smg = Person("Maria", 20)

# display values using getter methods
print("Name:", p1_smg.get_name_smg())
print("Age:", p1_smg.get_age_smg())