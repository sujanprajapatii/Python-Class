#Inheritance:allows a class to inherit attributes and methods from another class.
class Animal:
    def speak(self):
        print("Animal Speaks")
class Dog(Animal): #Inherits from Animal
    def bark(self):
        print("Woof!")
dog=Dog()
dog.speak() #Output:Animal Speaks
dog.bark() #Output:Woof!




