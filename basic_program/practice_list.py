a=[]
r=int(input("No. of records:"))
for i in range(r):
    x=input("Enter a name:")
    a.append(x)
print(a)
name1=input("Enter the removing name:")
name2=input("Enter the replace name:")
i=a.index(name1)
a.remove(name1)
a.insert(i,name2)
print(a)

