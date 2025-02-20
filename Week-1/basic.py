#Basic Data Types
age = 21          #int
height = 5.9      #float
name = "Alice"    #string
is_student = True #boolean

#Control Str

#Conditionals
if age > 18:
    print("Adult")
elif age == 18:
    print("Just became an adult")
else:
    print("Minor")

#For Loop
for i in range(5): #Iterates from 0 to 4
    print(f"Number: {i}") #The f before the string allows you to include variables or expressions inside {}.

#While loop
count=0
while count < 3:
    print("Counting:",count)
    count += 1

#Functions
def greet(name):
    return f"Hello, {name}"

#Function call
print(greet(name)) #Output: Hello,Alice

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

#Complex Data Types

# list:ordered,mutable collection
fruits=["apple", "banana" ,"Cherry"]

# tuple:Ordered,imutable collection
coordinates=(10,20)

# dict: key-value pairs, like a map
person={"name" : "Alice", "age":25}

#set:Unordered collection of unique items

