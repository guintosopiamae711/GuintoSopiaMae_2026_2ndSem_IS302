class Person_nbs:
    def __init__(self_nbs, name_nbs, age_nbs):
        self_nbs.name_nbs = name_nbs
        self_nbs.age_nbs = age_nbs
    
    def display_info_nbs(self_nbs):
        print("Name:", self_nbs.name_nbs)
        print("Age:", self_nbs.age_nbs)

p1_nbs = Person_nbs("Juan", 20)
p1_nbs.display_info_nbs()
