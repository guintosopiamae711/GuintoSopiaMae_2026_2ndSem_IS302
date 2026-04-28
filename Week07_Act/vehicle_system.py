# vehicle_system.py

# Parent class
class Vehicle:
    def __init__(self, brand_smg, model_smg):
        self.brand_smg = brand_smg
        self.model_smg = model_smg


# Child class
class Car(Vehicle):
    def __init__(self, brand_smg, model_smg, year_smg):
        super().__init__(brand_smg, model_smg)  # call parent constructor
        self.year_smg = year_smg

    # method to display car details
    def display_car_smg(self):
        print(self.brand_smg, self.model_smg, self.year_smg)


# create object
car1_smg = Car("Toyota", "Corolla", 2022)

# display info
car1_smg.display_car_smg()