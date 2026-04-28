# polymorphism_demo.py

# Class Dog
class Dog:
    def speak_smg(self):
        print("Dog barks")


# Class Cat
class Cat:
    def speak_smg(self):
        print("Cat meows")


# list of objects
animals_smg = [Dog(), Cat()]

# polymorphism in action
for animal_smg in animals_smg:
    animal_smg.speak_smg()