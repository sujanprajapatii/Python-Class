#Multiple inheritance
class division:                 #class parent1:
    def __init__(self,a,b):         #statement
        self.n=a
        self.d=b
    def divide(self):
        return self.n/self.d
class modulus:                  #class parent2:
    def __init__(self,a,b):         #statement
        self.n=a
        self.d=b
    def mod_divide(self):
        return self.n%self.d
    
class div_mod(division,modulus): #class child(parent1,parent2):
    def __init__(self,a,b):         #statement
        self.n=a
        self.d=b
    def div_and_mod(self):
        divval=division.divide(self)
        modval=modulus.mod_divide(self)
        return(divval,modval)
x=div_mod(10,4)
print("division:",x.divide())
print("mod_division:",x.mod_divide())
print("divmod:",x.div_and_mod())