mytuple=("apple","banana","cherry")
for x in mytuple:
    print(x)
# myit=iter(mytuple)
# print(next(myit))
# print(next(myit))
# print(next(myit))

mystr="banana"
myit=iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# class MyNumbers:
#     def __iter__(self):
#         self.a=1
#         return self
#     def __next__(self):
#         if self.a<=20:
#         x=self.a
#         self.a+=1
#         return x
#         else:
#             raise StopIteration
# myclass=MyNumbers()
# myiter=iter(myclass)
# for x in myiter:
#     print(x)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
class MyNumbers:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a<=20:
            x=self.a
            self.a+=1
            return x
        else:
            raise StopIteration
myclass=MyNumbers()
myiter=iter(myclass)
for x in myiter:
    print(x)