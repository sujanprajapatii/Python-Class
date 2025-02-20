#int:Whole no.(positive or negative)
age=25
temperature=-5

#float:Decimal no.
height=5.9
weight=-3.14

#str: Text data,enclosed in quotes
greeting="Hello, World"

#bool:True or False values
is_active=True
is_verified=False

a = "apple" #global variable

def function():
    global a
    a = "banana" #local variable
    print(a)

function()
print(a)

#local variable
def my_function():
    x=10 #local variable
    print(x)
my_function()
print(x) #Error:x is not accessible outside the function
 
 #Global variable
y=20 #Global variable
def my_function():
    print(y) #Accessible inside the function
my_function()

#Mutable Data Types
my_list=[1,2,3]
my_list.append(4) #Modifies the existing list
print(my_list)

my_list=[1,2,3]
del my_list[1] #Removes element at index 1