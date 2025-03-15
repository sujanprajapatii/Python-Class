import re
result = re.match(r'\d+', '123abc')
print(result.group())  # Output: 123

result = re.search(r'abc', '123abc456')
print(result.group())  # Output: abc

result = re.findall(r'\d+', 'abc123def456')
print(result)  # Output: ['123', '456']

result = re.sub(r'\d+', 'number', 'abc123def456')
print(result)  # Output: abcnumberdefnumber

result = re.split(r'\d+', 'abc123def456')
print(result)  # Output: ['abc', 'def', '']

txt="The rain in Spain"
x=re.search("^The.*Spain$",txt) #Tells to start from'The' and end with 'Spain'
print(x)

x=re.findall("ai",txt)
print(x)

x=re.search("\s",txt)
print("The first white space character is located in position:",x.start())

txt="The rain in Spain"
x=re.search(r"\bS\w+",txt)
print(x.string)