#Hybrid Inheritance
#Parent class
class CEO:
    def ceoMethod(self):
        print("I am the CEO")
class Manager(CEO):
    def managerMethod(self):
        print("I am the Manager")
class Employee1(Manager):
    def employee1Method(self):
        print("I am Employee one")
class Employee2(Manager):
    def employee2Method(self):
        print("I am Employee two")
#Creating instances
emp=Employee2()
#method calls
emp.managerMethod()
emp.ceoMethod()