#Hierarchial Inheritance
#parent class
class Manager:
    def managerMethod(self):
        print("I am Manager")
#Child class
class Employee1(Manager):
    def employee1Method(self):
        print("I am Employee one")
#Second child class
class Employee2(Manager):
    def employee2Method(self):
        print("I am Employee two")

#Creating instances
emp1=Employee1()
emp2=Employee2()
#method calls
emp1.managerMethod()
emp1.employee1Method()
emp2.managerMethod()
emp2.employee2Method()