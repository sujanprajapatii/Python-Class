#Single Inheritance
#Parent class
class parent:
    def parentMethod(self):
        print("Calling parnet method")
#Child class
class Child(parent):
    def childMethod(self):
        print("Calling child method")
#instance of child
c=Child()
#calling methof of child class
c.childMethod()
#calling method of parent child
c.parentMethod()
