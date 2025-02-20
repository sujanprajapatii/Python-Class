#Multi-level Inheritance
#parent class
class Universe:
    def universeMethod(self):
        print("I am in the Universe")
#child class
class Earth(Universe):
    def earthMethod(self):
        print("I am on Earth")
#another child class
class Nepal(Earth):
    def nepalMethod(self):
        print("I am from Nepal")

#Creating instance
person=Nepal()
#method calls
person.universeMethod()
person.earthMethod()
person.nepalMethod()