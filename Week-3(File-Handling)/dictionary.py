# thisdict={
#     "brand":"Ford", #Key:Value Pairs
#     "model":"Mustang",
#     "year":1964,
#     "year":2020 
# }
# print(thisdict)
my_dict = {'a': 1, 'b': 2}
print(my_dict.keys())  # Output: dict_keys(['a', 'b'])

print(my_dict.values())  # Output: dict_values([1, 2])

print(my_dict.items())  # Output: dict_items([('a', 1), ('b', 2)])

print(my_dict.get('a'))  # Output: 1
print(my_dict.get('c', 'Not Found'))  # Output: Not Found

my_dict.update({'b': 3, 'c': 4})
print(my_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}

value = my_dict.pop('a')
print(value)  # Output: 1
print(my_dict)  # Output: {'b': 3, 'c': 4}

item = my_dict.popitem()
print(item)  # Output: ('c', 4)

my_dict.clear()
print(my_dict)  # Output: {}

new_dict = my_dict.copy()