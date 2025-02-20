#From tutorialspoint
from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def draw(self):
        "Abstract method"
        return

class circle(shape):
    def draw(self):
         super().draw()
         print("Draw a circle")
         return
    
class rectangle(shape):
    def draw(self):
         super().draw()
         print("Draw a rectangle")
         return
    
shapes=[circle(),rectangle()] #Listing
for shp in shapes: #shp becomes instance for both circle() and rectangle()
    shp.draw()

#Next Example
#define parent class
class Parent:
    def myMethod(self):
        print('Calling parent Method')
#define child class
class Child(Parent):
    def myMethod(self):
        print('Calling child method')
#instance of child
c=Child()
#child calls overridden method
c.myMethod()

#Next Example
class Employee:
    def __init__(self,nm,sal):
        self.name=nm
        self.salary=sal
    def getName(self):
        return self.name
    def getSalary(self):
        return self.salary
    
class SalesOfficer(Employee):
    def __init__(self,nm,sal,inc):
        super().__init__(nm,sal)
        self.incnt=inc
    def getSalary(self):
        return self.salary+self.incnt
    
e1=Employee("Rajesh",9000)
print("Total salary for {} is Rs {}".format(e1.getName(),e1.getSalary()))
s1=SalesOfficer('kiran',10000,1000)
print("Total salary for {} is Rs {}".format(s1.getName(),s1.getSalary()))