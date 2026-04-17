class Car_smg:
    def __init__(self_smg, brand_smg, model_smg, year_smg):
        self_smg.brand_smg = brand_smg
        self_smg.model_smg = model_smg
        self_smg.year_smg = year_smg
    
    def display_car_smg(self_smg):
        print(self_smg.brand_smg, self_smg.model_smg, self_smg.year_smg)

car1_smg = Car_smg("Toyota", "Corolla", 2020)
car1_smg.display_car_smg()
