#super() function allows you to access methods and attributes of parent class within a child class
#Parent class
class ParentDemo:
    def __init__(self,msg):
        self.message=msg
    def showMessage(self):
        print(self.message)
#Child class
class ChildDemo(ParentDemo):
    def __init__(self,msg):
        #use of super function
        super().__init__(msg)
#creating instance
obj = ChildDemo("Welcome to Tutorialspoint!")
# Calling method to display the message
obj.showMessage()