class Car_nbs:
    def __init__(self_nbs, brand_nbs, model_nbs, year_nbs):
        self_nbs.brand_nbs = brand_nbs
        self_nbs.model_nbs = model_nbs
        self_nbs.year_nbs = year_nbs
    
    def display_car_nbs(self_nbs):
        print(self_nbs.brand_nbs, self_nbs.model_nbs, self_nbs.year_nbs)

car1_nbs = Car_nbs("Toyota", "Corolla", 2020)
car1_nbs.display_car_nbs()
