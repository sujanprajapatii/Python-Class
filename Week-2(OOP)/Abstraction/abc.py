from abc import ABC,abstractmethod
class democlass(ABC):
    @abstractmethod
    def method1(self):
        print("abstract method")
        return
    def method2(self):
        print("concrete method")

class concreteclass(democlass):
    def method1(self):
        super().method1()
        return
#Creating instance
obj=concreteclass()
#calling
obj.method1()
obj.method2()