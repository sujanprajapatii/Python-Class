# f=open("sujan1.txt","a")# append=pre-defined method used to add a single item to certain collection types. 
f=open("sujan1.txt","w")
f.write("Byeeeeeeeeee")
f.close()
#Open and read the file after the overwriting:
f=open("sujan1.txt","r")
print(f.read())