# animal_override.py

class Animal:
    def speak_smg(self):
        print("Animal makes a sound")


class Dog(Animal):
    def speak_smg(self):
        print("Dog barks")


class Cat(Animal):
    def speak_smg(self):
        print("Cat meows")


animals_smg = [Dog(), Cat()]

for animal_smg in animals_smg:
    animal_smg.speak_smg()