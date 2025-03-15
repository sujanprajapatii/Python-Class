#Global=value is changed
x=300
def myfunc():
    global x
    x=200
myfunc()
print(x)
#Nonlocal keyword=used in nested function
def myfunc():
    x="John"
    def myfunc2():
        nonlocal x
        x="hello"
    myfunc2()
    return x
print(myfunc())