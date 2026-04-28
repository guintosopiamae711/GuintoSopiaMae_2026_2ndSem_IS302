# inheritance_demo.py

# Parent class
class Animal:
    def __init__(self, name_smg):
        self.name_smg = name_smg

    def speak_smg(self):
        print(self.name_smg, "makes a sound")


# Child class
class Dog(Animal):
    def bark_smg(self):
        print(self.name_smg, "barks")


# create object
dog1_smg = Dog("Buddy")

# call methods
dog1_smg.speak_smg()
dog1_smg.bark_smg()