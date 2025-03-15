# try:
#     with open("sujan.txt","r") as file:
#         data=file.read()
# except FileNotFoundError:
#     print("File not found.")

# f=open("sujan.txt", "r")
# print(f.read())
f=open("./Week-3/sujan.txt","r") #./skips the file which is infront of these file 

# for x in f: By looping through the lines of the file, you can read the whole file, line by line:
#     print(x)
print(f.readline())
f.close() 
#You should always close your files. In some cases, due to buffering, changes made to a file may not show until you close the file.
