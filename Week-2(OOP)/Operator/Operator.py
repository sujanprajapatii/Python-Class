#Membership Operator
#Example 1:'in'
fruits=["apple","banana","cherry"]
print("banana" in fruits) #Output:True

#Example 2:'not in' operator
text="Hello World"
print("z" not in text) #Output:True

#Example 2:'in' Operator
print("ell" in "Hello") #Output:True

#Identity Operator
str1="hello"
str2="hello"
print(str1 is str2) #Output:True

a=[1,2,3]
b=[1,2,3]
print(a is b) #Output:False (Due to duplication of memory allocations)

x=10
y=20
print(x is not y) #Output:True

print(0.1+0.2==0.3)#False due to floating-point inaccuracy
