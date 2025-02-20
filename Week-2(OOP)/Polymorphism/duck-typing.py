#Duck-Typing
class Duck:
    def sound(self):
        return "Quack,quack!"
class AnotherBird:
    def sound(self):
        return "I am similar to a duck!"
def makeSound(duck):
    print(duck.sound())

#Creating instance
duck=Duck()
anotherbird=AnotherBird()
#Calling methods
makeSound(duck)
makeSound(anotherbird)