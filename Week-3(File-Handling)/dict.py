car={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
    # "colors":["red","white","blue"]
}
#car.update({"year":2020})
#car.pop("model") #delete
#car.popitem()
#print(car)
# x=thisdict.keys()
# print(x)
# x=car.keys()
#x=car.values()
#if "color" in car:
    #print("Yes,'model' is one of the keys in the car dictionary")
#else:
    #print("No")
#x=car.items()
#print(x)#before change
#car["color"]="white"
#car["color"]="red"
#car["year"]=2020
#print(x)#after change
#print(car)
#for x in car:
   # print(x) #keys print
#for x in car:
    #print(car[x]) #values print
#for x in car.values():
   # print(x) #values print
mydict=car.copy()
print(mydict)
mydict=dict(car)
print(mydict)