#Method-Overloading:Must accept different parameters by a function,it is not in python by default
def add(*nums):
    return sum(nums)

#Call the function with different no. of parameters
result1=add(10,25)
result2=add(10,25,35)

print(result1)
print(result2)