#JSON to Python
import json
#some JSON:
x='{"name":"John","age":30,"city":"New York"}'
#parse x:
y=json.loads(x)
#the result is a python dictionary:
print(y["age"])

#Python to JSON
import json
#a python object(directory):
x={
    "name":"John",
    "age":30,
    "city":"New York"
}
#convert into JSON:
y=json.dumps(x)

#the result is a JSON string:
print(y) 
