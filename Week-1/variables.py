a = "apple" #global variable

def function():
    global a
    a = "banana" #local variable
    print(a)

function()
print(a)    
